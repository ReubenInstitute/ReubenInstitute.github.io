# Astronomy Library

The Astronomy Library supplies the solar and lunar calculations that drive every zman and clock face.  It consists of a shared constants module, a small holder for celestial coordinates, and two main classes — `Sun` and `Moon` — that compute rise, set, and illumination times from a location and a date.


## Constants

* `J2000` – The Julian Day Number of the J2000.0 epoch (2451545.0).  All orbital calculations are expressed as offsets from this instant.
* `EARTH_OBLIQUITY` – The obliquity of the ecliptic in radians (≈ 23.4397°).


## CelestialLocation Class

A lightweight container for a right‑ascension / declination pair, returned by several internal coordinate transformations.

### Attributes

* `rightascension` – Right ascension in radians.
* `declination` – Declination in radians.

### Constructors

```python
def __init__(self, rightascension, declination)
```

Creates a CelestialLocation from right ascension and declination (both in radians).

## Sun Class

Computes sunrise, sunset, solar noon, and twilight times for a given location and civil date.  The class is mutable — use setlocation or setdate to reuse an existing instance.

### Attributes

* location – The Location object used for calculation.
* date – The Date for which rise/set/noon were computed.
* risetime – Sunrise as a DateTime (UTC).
* settime – Sunset as a DateTime (UTC).
* noontime – Solar noon as a DateTime (UTC).

### Constructors

```python
def __init__(self, location, date)
```

Creates a Sun object and immediately computes sunrise, sunset, and noon for the given location and date.

### Methods

```python
def setlocation(self, location)
```

Changes the location and recomputes all times.

```python
def setdate(self, date)
```

Changes the date and recomputes all times.

```python
def update(self)
```

Recomputes risetime, settime, and noontime from the stored location and date.  Called automatically by setlocation, setdate, and the constructor.

```python
def dawntime(self, angleDegrees)
```

Returns the time (as a DateTime) when the sun reaches the given depression angle below the horizon before sunrise.  For example, 16.1° corresponds to the common halachic dawn.

```python
def dusktime(self, angleDegrees)
```

Returns the time (as a DateTime) when the sun reaches the given depression angle below the horizon after sunset.


## Moon Class

Computes moonrise, moonset, illumination fraction, phase, and the always‑up / always‑down status for a given location and civil date.  Times that do not occur on the given date are stored as None.

### Attributes

* location – The Location object used for calculation.
* datetime – The DateTime for which the moon data was computed.
* rise – Moonrise as a DateTime, or None if the moon does not rise that day.
* set – Moonset as a DateTime, or None if the moon does not set that day.
* isalwaysup – True if the moon remains above the horizon for the entire civil day.
* illuminationfraction – Illuminated fraction of the moon’s disc (0.0 = new, 1.0 = full).
* phase – Phase angle in the range 0.0‑1.0 (0.0 = new, 0.5 = full, 1.0 = next new).
* angle – Position angle of the bright limb in radians.
* emoji – A single‑character moon‑phase emoji (e.g. "🌑", "🌓", "🌕") chosen for the given latitude.

### Constructors

```python
def __init__(self, location, datetime)
```

Creates a Moon object and immediately computes all moon data for the given location and datetime.

### Static Helpers

```python
@staticmethod
def moonphaseemoji(phase, latitude)
```

Returns a moon‑phase emoji string for the given phase (0.0‑1.0) and latitude (positive = northern hemisphere).  This is the same function used internally to set the emoji attribute.
