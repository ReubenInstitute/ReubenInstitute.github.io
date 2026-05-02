# HebrewDate app for Android

HebrewDate is an offline Hebrew calendar and astronomical clock that computes all displayed data from first principles — no pre-loaded tables, no network calls. The app derives the Hebrew and Gregorian dates, holiday indicators, and weekly Torah portions directly from mathematical algorithms. Sunrise, sunset, moonrise, moonset, and the current lunar phase are calculated for the device's GPS coordinates, or for any manually entered location, making it equally useful as a precise halachic-time reference and as a general astronomical tool. All computation happens on-device, guaranteeing full functionality without Internet access.

The app is built on the Institute's free-software domain libraries (Date, HebrewDate, HebrewHoliday, HebrewNumbers, Torah, Sun, Moon, etc.), released under the GNU General Public License v3. The app itself is a thin proprietary UI layer over these freely available libraries.

## Free vs. Pro Tier

| Feature | Free Tier | Pro Tier |
|---|---|---|
| Hebrew Date (day, month, year) | device clock | GPS |
| Hebrew Holiday | device clock | GPS |
| Halachic Times | – (planned: GPS, ad‑supported) | GPS (planned) |
| Widget: Hebrew Date & Holiday | Yes | Yes |
| Widget: Upcoming Halachic Time | No | Yes (planned) |
| Widget: Next Holiday | No | Yes (planned) |
| Settings: Calculation Opinion (Magen Avraham / Gra) | No | Yes (planned) |

*Halachic times and calculation customisation are planned for a future release.*

## Interface

Navigation is entirely gesture-based: a two-finger swipe switches between the three screens (main day view, month calendar, and settings), while single-finger swipes move the displayed date forward or backward in time.

The interface is deliberately minimal — no buttons, no explanatory labels — so that every pixel conveys information.

### Main Screen (Day View)

The main screen displays the full Gregorian date (day, month name, year) alongside the Hebrew date (gematria day, month name, gematria year). Below them runs a live Gregorian clock (HH:mm:ss) and a Hebrew-time clock, where the hour and minute are rendered as Hebrew numerals and the seconds as a plain number. When the day falls on a holiday or fast, the Hebrew name appears; the weekly Torah portion for the upcoming Shabbat is shown every day of the week.

The lower portion of the screen shows sunrise and sunset times, along with moonrise and moonset. A moon-phase emoji, chosen to match the observer's hemisphere, indicates the current lunar phase. All sun and moon data are computed for the device's GPS coordinates, or for any manually entered location.

Environmental data (temperature, air pressure, altitude) and live satellite status are already displayed when sensor data is available. 

### Calendar Screen (Month View)

A month-grid calendar that can be browsed forward and backward through months and years. The current implementation displays a Hebrew month: each cell shows the Hebrew day numeral (gematria) with the corresponding Gregorian day number underneath. Holiday and fast-day names appear directly in the cells. A mirrored Gregorian-month view, with Hebrew date overlays and the same holiday and Torah-portion markings, is planned for a future release.

### Widget

The home-screen widget displays the current Hebrew date, Gregorian date, and holiday, updating automatically to provide an at-a-glance view of the calendar without opening the app.

**Planned Pro widget additions:** upcoming Halachic time and the next upcoming holiday.

## Planned Features

### Halachic Times
The app will display the following halachic times, calculated for the device’s precise GPS location:

- Alot HaShachar
- HaNetz HaChama
- Sof Zman Kriyat Shema
- Sof Zman Tefillah
- Chatzot Hayom
- Mincha Gedolah
- Mincha Ketanah
- Plag HaMincha
- Shkiah
- Tzeit HaKochavim
- Tzeit HaKochavim (Rabbeinu Tam)
- Chatzot Halayla

Users will be able to choose between the calculation methods of **Magen Avraham** (Rabbi Avraham Gombiner) and the **Gra** (Vilna Gaon, Rabbi Eliyahu ben Shlomo Zalman Kramer) in the settings (Pro feature).

### Settings (Planned)
The settings screen will offer:
- Status Bar toggles: Hebrew Date, Hebrew Holiday, Upcoming Halachic Time
- Notification toggle for upcoming Halachic Time
- Radio button for calculation opinion (Magen Avraham / Gra) – Pro only

### Multilingual Support
The app is designed to support the following languages:
Amharic, Arabic, Aramaic, English, French, German, Hebrew, Italian, Portuguese, Russian, Spanish, Yiddish.