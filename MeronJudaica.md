# Meron Judaica Store

Meron Judaica is the store of the Institute. It sells physical publications based on Institute texts and designs, alongside its own artisanal products — string art and anamorphic blocks — which are produced  independently. This collaboration ensures textual accuracy while allowing us to focus on craftsmanship and production.

---

## Print

We publish meticulously curated texts derived from the ancient Leningrad Codex. Our publications combine scholarly precision with modern design, featuring enhanced typography, poetic layouts, and innovative formats for contemporary study.

### 📚 Printed Psalms Book
A comprehensive edition containing the complete book of Psalms. The text is presented in a poetic, line-by-line layout, similar to song lyrics, which results in a longer presentation than traditional block-text formats. Verse text appears in a larger, dark serif font for emphasis and readability.

#### Sizes:
- **Liturgical**: 22×31 cm (Hardcover & Leather-like only) - Synagogue-sized edition with enhanced visibility
- **Standard**: 17×24 cm - Comfortable reading and study at home or in a group setting
- **Small**: 12×17 cm - Compact and convenient, great for carrying in a bag
- **Pocket**: 6×8.5 cm - Ultra-portable, designed to fit easily in a pocket

#### Formats:
- **Paperback**: Lightweight and portable, perfect for on-the-go study
- **Hardcover**: Durable and long-lasting, ideal for frequent use or as a keepsake
- **Leather-like**: A premium, luxurious option with Smyth sewn binding and gold/silver/bronze leaf lettering

<!--
**Pricing:**

| Edition                     | Our Price (₪) | Market Price (₪) |
|-----------------------------|---------------|------------------|
| Pocket Hardcover            | 25            | 18               |
| Pocket Leather-like         | 45            | 32               |
| Small Paperback             | 20            | 15               |
| Small Hardcover             | 35            | 25               |
| Small Leather-like          | 85            | 55               |
| Standard Paperback          | 75            | 45               |
| Standard Hardcover          | 150           | 85               |
| Standard Leather-like       | 300           | 170              |
| Liturgical Hardcover        | 350           | 220              |
| Liturgical Leather-like     | 650           | 380              |
-->

### 📖 Psalms Daily Reading Sets

For ease of daily study, the complete collection of Psalms is available in booklet format. Each booklet contains the Psalms designated for a specific day's reading and features our exact Hebrew text in a poetic, line-by-line layout.

- **The Four-Week Method Set (28 Booklets):** Our primary offering, based on a mathematically optimized schedule that ensures balanced daily reading lengths. Housed in a simple, printed cardboard case with an open front or cut-out windows for easy access.
- **Traditional 30-Day Set (30 Booklets):** For those who specifically adhere to the historical 30-day division cycle.

### 📖 Parashah Weekly Booklets

Weekly publications that present the Torah portion (Parashah) of that week. These booklets combine scholarly precision with modern design, featuring Hebrew text sourced from the ancient Leningrad Codex and English translations based on the JPS 1917 edition.

#### Features:

- Modern punctuation and formatting with headings for easy reading
- Rounded external page corners
- Fore-edge painted
- AI-generated illustrations

#### Sizes:

- **Standard**: 17x25 cm – Comfortable reading and study at home or in a group setting
- **Small**: 12x17 cm – Compact and convenient, great for carrying in a bag
- **Pocket**: 6x8.5 cm – Ultra-portable, designed to fit easily in a pocket

#### Formats:

- **Paperback**: Lightweight and portable, perfect for on-the-go study
- **Hardcover**: Durable and long-lasting, ideal for frequent use or as a keepsake
- **Leather**: A premium, luxurious option with Smyth sewn binding and gold leaf lettering

#### Versions:

- **English**: English only – Ideal for readers who prefer to study in English
- **Hebrew**: Hebrew only – Perfect for engaging directly with the original Hebrew text
- **Bilingual**: English with Hebrew on the opposite page – Allows for comparative study

#### Colors by Book:

| Book         | Color       | Hexadecimal | Symbolism |
|--------------|-------------|-------------|-----------|
| Genesis      | Earthy Green | #556B2F     | Fertility, growth, creation |
| Exodus       | Deep Blue    | #00008B     | Waters of Nile/Red Sea, revelation |
| Leviticus    | Crimson Red  | #DC143C     | Sacrificial rituals, holiness |
| Numbers      | Warm Sand    | #F4A460     | Desert wanderings, journey |
| Deuteronomy  | Royal Purple | #800080     | Wisdom, royalty, covenant |

### 📖 Weekly Parashah Scroll Edition

A unique box set containing 54 individual scrolls, each housed in a protective plastic cylinder, representing the entire yearly cycle of Torah readings. Includes a stylish, pen-like holder for carrying two scrolls at a time. The entire collection is presented in a beautifully designed box.

### 📖 "In Halakhah, Haggadah, and its History" Booklet Series

Offers an accessible and insightful journey into Jewish tradition, exploring holidays, core concepts, and narratives. Each volume meticulously integrates quoted examples from foundational texts (Torah, Talmud, Zohar) alongside insights from major commentators to illustrate the historical evolution of Jewish practices.

### 📖 "Zaggin Didhav" (זגין דדהב) – Bells of Gold

A publication dedicated to Aramaic scriptures. Presents segments from both Talmuds, Zohar, and chapters from Ezra/Daniel with full Hebrew letters and diacritics, modern punctuation, and curly quotes. Features a unique side-by-side format: original Aramaic text on one page with a precise Hebrew translation on the opposing page.

---

## Art

We use in-house software to generate nail paths and thread sequences from source images, and to calculate the anamorphic projections for each block shape.

### 🎨 String Art

A wooden frame — circular, square, octagonal, or custom — with nails placed along the edge or along the inner path of the design. Black or colored thread is stretched between the nails to form an image.

Suitable subjects are strong, recognizable images that read well in thread lines: Rabbi Shimon bar Yochai, the Shema Yisrael, the Lubavitcher Rebbe, and similar iconic portraits or texts.

### 🎨 Anamorphic Blocks

A pyramid-like block or box, usually made of cardboard or another rigid material. A printed image is applied to the slanted faces so that when viewed from the front, the image appears to recede inward, creating a 3D optical illusion.

Suitable subjects are images with strong perspective or architectural depth: a synagogue interior, the entrance to a tomb site, a study hall, or similar scenes that make sense as a receding space.

### How it's made

The **String Art Generator** is a complete web application featuring image upload, parameter configuration, and real-time generation. The system supports multiple frame types — including circular, square, octagonal, and custom SVG paths — and implements a Bresenham line algorithm for precise pixel sampling. A responsive frontend interface provides pause/resume functionality, while the backend handles image processing, pin coordinate calculation, and step-by-step line generation with wire length tracking. The application can export patterns in multiple formats, including pin sequence tables suitable for instruction booklets.

The **anamorphic blocks system** is a functional web application for designing and previewing 3D optical illusion blocks. It features a Three.js 3D viewer that displays rectangular frustums with correct projective texture mapping, alongside parameter controls for block dimensions, cropping, and automatic proportion calculation based on source images. The software can extract individual face images for printing and generate OBJ models for visualization. Supporting documentation includes a complete jig design for physical production and multiple pre-defined collections for different visual effects.
