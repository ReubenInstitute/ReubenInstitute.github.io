# GPS Hebrew Clock

Read the [Manual](HebrewClockManual.md)

A timepiece that tells the hour the ancient way—dividing daylight and darkness into twelve proportional parts, shifting with the seasons. The Hebrew Clock presents the full seasonal day on a single dial: the halakhic bands, night watches, moon arc, and observance ring all remain complete at every size. 

Four distinct form factors cover every setting, from pocket to wall. Each size is available with a choice of display technology—LCD for bright indoor use, OLED for dark rooms, or e‑paper for sunlight and low power—alongside backup battery options ranging from a single removable cell to multiple user‑supplied 18650 cells.


| name | size | battery | lcd | oled | e‑paper |
|------|------|---------|-----|------|---------|
| Travel | 6 × 6| | HCT-L | HCT-O | HCT-E |
| Travel | 6 × 6 | BL-5C | HCT-L/N | HCT-O/N | HCT-E/N |
| Travel | 6 × 6 | 1 x 18650 | HCT-L/C | HCT-O/C | HCT-E/C |
| Bedside | 9 × 9 | | HCB-L | HCB-O | HCB-E |
| Bedside | 9 × 9 | BL-5C | HCB-L/N |  | HCB-E/N |
| Bedside | 9 × 9 | 2 x 18650 | HCB-L/C | HCB-O/C | HCB-E/C |
| Desktop | 13 × 13 | | HCD-L | HCD-O | HCD-E |
| Desktop | 13 × 13 | 4 x 18650 | HCD-L/C | HCD-O/C | HCD-E/C |
| Wall | 20 × 20 | | HCW-L | HCW-O | HCW-E |
| Wall | 20 × 20 | 4 x 18650 | HCW-L/C | HCW-O/C | HCW-E/C |

## Hebrew Travel Clock (6 × 6 cm)

Compact and portable. The Travel edition carries the full Hebrew Clock in a size that fits a pocket, bag, or siddur pouch. Its display and battery combinations are kept light and simple, making it the natural choice for maintaining the day’s structure on the go.

## Hebrew Bedside Clock (9 × 9 cm)

Quiet and personal. Sized for the nightstand, the Bedside edition keeps every ring and marking legible from the pillow. It preserves the full instrument without brightness or distraction, utilizing battery options chosen for long, uninterrupted use through the night.

## Hebrew Desktop Clock (13 × 13 cm)

Balanced and versatile. Designed for a desk, shelf, or study table, the Desktop edition keeps the sacred rhythm of the day within sight while working, learning, or writing. The dial remains fully detailed at a scale suited for a personal workspace.

## Hebrew Wall Clock (20 × 20 cm)

Commanding and communal. The Wall edition presents the full dial in generous proportions, clearly legible from across a room. It is designed for synagogues, batei midrash, community spaces, or a prominent home wall where the instrument can be read by many.

# Coming soon

## Hebrew Calendar & Clock Info Panel (15-inch)

A fixed, self-contained display for public and shared spaces, including synagogues, batei midrash, and community buildings. The integrated 15‑inch screen presents zmanim across multiple customs side by side. All hardware and software are built into a single, plug-and-play unit.

## Hebrew Calendar & Clock Info HDMI Stick

A compact, self-contained solution for locations already equipped with a large screen or television. The stick plugs directly into an HDMI port to present zmanim across multiple customs side by side. All software and display processing are built directly into the stick, requiring no additional hardware.

## Hebrew Wristwatch

Personal and immediate. A standalone wearable clock with an integrated battery, bringing the same seasonal hour, zmanim, and observance awareness to the most intimate format.

## Hebrew Calendar & Clock for Mobile

A fully featured, free utility. The Hebrew Calendar app for Android and iOS is complete on its own, offering comprehensive daily tracking. An optional Pro tier enables the animated clock display, accessible via direct purchase or by completing a designated activity.

## Hebrew Calendar & Clock for Wearable

Designed for the wrist. The Hebrew Calendar & Clock app operates as a dedicated watch face for WearOS and watchOS smartwatches, bringing the complete seasonal dial and zmanim to existing wearable devices.

## Specs

| Name | Model | Description |
|---|---|---|
| **MCU** | ESP32 / STM32WB55 | Microcontroller platforms for the clock. |
| **RTC** | DS3231 | Maintains accurate timekeeping even when the main power is off (using a backup battery). |
| **GPS** | NEO-8M | Provides precise time synchronization using satellite signals and retrieves location data (latitude, longitude, altitude). |
| **Temperature, Humidity, & Pressure Sensor** | BME280 | Measures ambient temperature, barometric pressure, and humidity. |
| **Motion Sensor** | MPU6050 | Tracks acceleration and gyroscopic motion. |
| **Magnetic Sensor** | HMC5883L | Functions as a digital compass to determine cardinal directions. |
| **Light Sensor** | BH1750 | Measures ambient light levels. |
