#!/usr/bin/env python3
"""Rebuild the /deb and /pip/simple package repos from their source repos.

By default, fetches every package into ~/.cache/reubeninstitute, `git
pull`ing each one to the latest commit (cloning it first if missing) — no
local setup required:

    python3 rebuild.py

Pass a folder to use instead: it's used exactly as-is, no pulling or
cloning, so it stays entirely under your own control:

    python3 rebuild.py /root/WORK  # reuses /root/WORK/<name> as-is

Run this from inside the ReubenInstitute.github.io checkout. It does not
touch this repo's git — commit and push it yourself afterward.
"""
import argparse
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

PAGES_ROOT = Path(__file__).resolve().parent
DEB_DIR = PAGES_ROOT / "deb"
PIP_DIR = PAGES_ROOT / "pip" / "simple"
GPG_KEYID = "807CCC20F26CFF08"
GITHUB_ORG = "https://github.com/ReubenInstitute"
DEFAULT_CLONE_BASE = Path.home() / ".cache" / "reubeninstitute"

# name: pip/PEP503 project name (as in pyproject.toml [project] name), and the
# repo name under github.com/ReubenInstitute
# deb_pkgs: Debian package name(s) built by packaging/deb/build.sh (as in packaging/deb/control*)
PACKAGES = [
    {"name": "Hebrew", "deb_pkgs": ["python3-hebrew"]},
    {"name": "Date", "deb_pkgs": ["python3-date"]},
    {"name": "Astro", "deb_pkgs": ["python3-astro"]},
    {"name": "HebrewDate", "deb_pkgs": ["python3-hebrewdate"]},
    {"name": "HebrewYemama", "deb_pkgs": ["python3-hebrewyemama"]},
    {"name": "Scriptures", "deb_pkgs": ["python3-scriptures", "scriptures-data", "scriptures-web"]},
    {"name": "StyledScriptures", "deb_pkgs": ["python3-styledscriptures", "styledscriptures-data", "styledscriptures-web"]},
    {"name": "Fonts", "deb_pkgs": ["fonts"], "pip": False},
    {"name": "audiobible-shmueloff-source", "deb_pkgs": ["audiobible-shmueloff-source"], "pip": False},
    {"name": "audiobible-shmueloff-original", "deb_pkgs": ["audiobible-shmueloff-original"], "pip": False},
    {"name": "audiobible-shmueloff-darkknox2", "deb_pkgs": ["audiobible-shmueloff-darkknox2"], "pip": False},
    {"name": "audiobible-darkknox2-english", "deb_pkgs": ["audiobible-darkknox2-english"], "pip": False},
    {"name": "audiobible-titles", "deb_pkgs": ["audiobible-titles"], "pip": False},
    {"name": "AudioBible", "deb_pkgs": ["audiobible-web"], "pip": False},
]


def resolve_source(pkg, clone_base):
    name = pkg["name"]
    existing = clone_base / name
    if existing.is_dir():
        run(["git", "pull"], cwd=existing)
        return existing
    run(["git", "clone", f"{GITHUB_ORG}/{name}.git", str(existing)])
    return existing


def use_as_is(pkg, folder):
    return folder / pkg["name"]


def run(cmd, cwd=None):
    print(f"+ {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def normalize(name):
    # PEP 503 normalization
    import re
    return re.sub(r"[-_.]+", "-", name).lower()


def source_version(pkg):
    control_dir = pkg["source"] / "packaging" / "deb"
    control_file = control_dir / "control"
    if not control_file.exists():
        control_file = control_dir / f"control-{normalize(pkg['name'])}"
    for line in control_file.read_text().splitlines():
        if line.startswith("Version:"):
            return line.split(":", 1)[1].strip()
    sys.exit(f"no Version line in {control_file}")


def published_version(pkg):
    matches = list(DEB_DIR.glob(f"{pkg['deb_pkgs'][0]}_*_all.deb"))
    if not matches:
        return None
    return matches[0].name.removeprefix(f"{pkg['deb_pkgs'][0]}_").removesuffix("_all.deb")


def build_deb(pkg):
    for deb_pkg in pkg["deb_pkgs"]:
        for old in pkg["source"].glob(f"{deb_pkg}_*_all.deb"):
            old.unlink()
    run(["sh", "packaging/deb/build.sh"], cwd=pkg["source"])
    debs = []
    for deb_pkg in pkg["deb_pkgs"]:
        matches = list(pkg["source"].glob(f"{deb_pkg}_*_all.deb"))
        if len(matches) != 1:
            sys.exit(f"expected exactly one .deb for {deb_pkg}, got {matches}")
        debs.append(matches[0])
    return debs


def build_dist(pkg):
    dist = pkg["source"] / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    run([sys.executable, "-m", "build"], cwd=pkg["source"])
    sdists = sorted(dist.glob("*.tar.gz"))
    wheels = sorted(dist.glob("*.whl"))
    if not sdists:
        sys.exit(f"no sdist produced for {pkg['name']}")
    if not wheels:
        sys.exit(f"no wheel produced for {pkg['name']}")
    return [sdists[-1], wheels[-1]]


def place_deb(pkg, deb_paths):
    DEB_DIR.mkdir(parents=True, exist_ok=True)
    for deb_pkg in pkg["deb_pkgs"]:
        for old in DEB_DIR.glob(f"{deb_pkg}_*_all.deb"):
            old.unlink()
    for deb_path in deb_paths:
        dest = DEB_DIR / deb_path.name
        shutil.copy2(deb_path, dest)
        print(f"placed {dest}")


def place_dist(pkg, dist_paths):
    proj_dir = PIP_DIR / normalize(pkg["name"])
    proj_dir.mkdir(parents=True, exist_ok=True)
    for old in list(proj_dir.glob("*.tar.gz")) + list(proj_dir.glob("*.whl")):
        old.unlink()
    dests = []
    for dist_path in dist_paths:
        dest = proj_dir / dist_path.name
        shutil.copy2(dist_path, dest)
        print(f"placed {dest}")
        dests.append(dest)
    return dests


def sha256_of(path):
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def rebuild_apt_index():
    result = subprocess.run(
        ["dpkg-scanpackages", "--multiversion", ".", "/dev/null"],
        cwd=DEB_DIR, check=True, capture_output=True, text=True,
    )
    (DEB_DIR / "Packages").write_text(result.stdout)
    run(["gzip", "-kf", "Packages"], cwd=DEB_DIR)
    release = subprocess.run(
        ["apt-ftparchive", "-c", "apt-ftparchive.conf", "release", "."],
        cwd=DEB_DIR, check=True, capture_output=True, text=True,
    )
    (DEB_DIR / "Release").write_text(release.stdout)
    run(["gpg", "--batch", "--yes", "--pinentry-mode", "loopback", "--passphrase", "",
         "--default-key", GPG_KEYID, "--detach-sign", "--armor", "-o", "Release.gpg", "Release"], cwd=DEB_DIR)
    run(["gpg", "--batch", "--yes", "--pinentry-mode", "loopback", "--passphrase", "",
         "--default-key", GPG_KEYID, "--clearsign", "-o", "InRelease", "Release"], cwd=DEB_DIR)


def write_project_index(name, dist_dests):
    proj_dir = dist_dests[0].parent
    links = "\n".join(
        f'<a href="{dest.name}#sha256={sha256_of(dest)}">{dest.name}</a>'
        for dest in dist_dests
    )
    html = f"<!DOCTYPE html>\n<html><body>\n{links}\n</body></html>\n"
    (proj_dir / "index.html").write_text(html)


def write_root_index():
    names = sorted(p.name for p in PIP_DIR.iterdir() if p.is_dir())
    links = "\n".join(f'<a href="{n}/">{n}</a>' for n in names)
    html = f"<!DOCTYPE html>\n<html><body>\n{links}\n</body></html>\n"
    (PIP_DIR / "index.html").write_text(html)


def main():
    parser = argparse.ArgumentParser(
        description="Rebuild the /deb and /pip/simple package repos from their source repos.")
    parser.add_argument("folder", nargs="?", type=Path,
        help="use these clones as-is, no pulling or cloning")
    parser.add_argument("--clear-cache", action="store_true",
        help=f"delete {DEFAULT_CLONE_BASE} and exit")
    args = parser.parse_args()

    if args.clear_cache:
        if args.folder:
            parser.error("--clear-cache cannot be combined with a folder")
        shutil.rmtree(DEFAULT_CLONE_BASE, ignore_errors=True)
        print(f"Removed {DEFAULT_CLONE_BASE}")
        return

    if args.folder:
        for pkg in PACKAGES:
            pkg["source"] = use_as_is(pkg, args.folder)
    else:
        DEFAULT_CLONE_BASE.mkdir(parents=True, exist_ok=True)
        for pkg in PACKAGES:
            pkg["source"] = resolve_source(pkg, DEFAULT_CLONE_BASE)

    try:
        for pkg in PACKAGES:
            print(f"=== {pkg['name']} ===")
            if source_version(pkg) == published_version(pkg):
                print(f"unchanged at {source_version(pkg)}, skipping")
                continue
            deb_path = build_deb(pkg)
            place_deb(pkg, deb_path)
            if pkg.get("pip", True):
                dist_paths = build_dist(pkg)
                dests = place_dist(pkg, dist_paths)
                write_project_index(pkg["name"], dests)
    finally:
        write_root_index()
        rebuild_apt_index()

    print("Done. Review changes, then commit and push this repo.")


if __name__ == "__main__":
    main()
