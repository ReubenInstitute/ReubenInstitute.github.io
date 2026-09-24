#!/usr/bin/env python3
"""Rebuild the /deb and /pip/simple package repos from their source repos.

Run this from inside the reubeninstitute.github.io checkout after pushing
changes to a package's source repo. It does not touch git — commit and push
this repo yourself afterward.
"""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

PAGES_ROOT = Path(__file__).resolve().parent
DEB_DIR = PAGES_ROOT / "deb"
PIP_DIR = PAGES_ROOT / "pip" / "simple"
GPG_KEYID = "807CCC20F26CFF08"

# name: pip/PEP503 project name (as in pyproject.toml [project] name)
# source: local clone of the package's own repo
# deb_pkg: Debian package name (as in packaging/deb/control)
PACKAGES = [
    {"name": "Hebrew", "source": Path("/root/WORK/Hebrew"), "deb_pkg": "python3-hebrew"},
    {"name": "Date", "source": Path("/root/WORK/Date"), "deb_pkg": "python3-date"},
    {"name": "Astro", "source": Path("/root/WORK/Astro"), "deb_pkg": "python3-astro"},
]


def run(cmd, cwd=None):
    print(f"+ {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def normalize(name):
    # PEP 503 normalization
    import re
    return re.sub(r"[-_.]+", "-", name).lower()


def build_deb(pkg):
    for old in pkg["source"].glob(f"{pkg['deb_pkg']}_*_all.deb"):
        old.unlink()
    run(["sh", "packaging/deb/build.sh"], cwd=pkg["source"])
    debs = list(pkg["source"].glob(f"{pkg['deb_pkg']}_*_all.deb"))
    if len(debs) != 1:
        sys.exit(f"expected exactly one .deb for {pkg['name']}, got {debs}")
    return debs[0]


def build_sdist(pkg):
    dist = pkg["source"] / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    run([sys.executable, "-m", "build", "--sdist"], cwd=pkg["source"])
    sdists = sorted(dist.glob("*.tar.gz"))
    if not sdists:
        sys.exit(f"no sdist produced for {pkg['name']}")
    return sdists[-1]


def place_deb(pkg, deb_path):
    DEB_DIR.mkdir(parents=True, exist_ok=True)
    for old in DEB_DIR.glob(f"{pkg['deb_pkg']}_*_all.deb"):
        old.unlink()
    dest = DEB_DIR / deb_path.name
    shutil.copy2(deb_path, dest)
    print(f"placed {dest}")


def place_sdist(pkg, sdist_path):
    proj_dir = PIP_DIR / normalize(pkg["name"])
    proj_dir.mkdir(parents=True, exist_ok=True)
    for old in proj_dir.glob("*.tar.gz"):
        old.unlink()
    dest = proj_dir / sdist_path.name
    shutil.copy2(sdist_path, dest)
    print(f"placed {dest}")
    return dest


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


def write_project_index(name, sdist_dest):
    proj_dir = sdist_dest.parent
    digest = sha256_of(sdist_dest)
    html = (
        "<!DOCTYPE html>\n<html><body>\n"
        f'<a href="{sdist_dest.name}#sha256={digest}">{sdist_dest.name}</a>\n'
        "</body></html>\n"
    )
    (proj_dir / "index.html").write_text(html)


def write_root_index():
    names = sorted(p.name for p in PIP_DIR.iterdir() if p.is_dir())
    links = "\n".join(f'<a href="{n}/">{n}</a>' for n in names)
    html = f"<!DOCTYPE html>\n<html><body>\n{links}\n</body></html>\n"
    (PIP_DIR / "index.html").write_text(html)


def main():
    for pkg in PACKAGES:
        print(f"=== {pkg['name']} ===")
        deb_path = build_deb(pkg)
        place_deb(pkg, deb_path)
        sdist_path = build_sdist(pkg)
        dest = place_sdist(pkg, sdist_path)
        write_project_index(pkg["name"], dest)

    write_root_index()
    rebuild_apt_index()
    print("Done. Review changes, then commit and push this repo.")


if __name__ == "__main__":
    main()
