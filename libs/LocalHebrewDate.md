# Local Hebrew Date Library

The `LocalHebrewDate` class is the central halachic‑time engine.  Given a Hebrew date, a geographic location, and a custom‑opinion preset, it computes every zman (prayer‑time boundary) for that yemama (the full night‑followed‑by‑day halachic cycle).  It also provides the seasonal‑hour mapping and the band definitions that drive both the academic and civil clock faces.


## LocalHebrewDate Class

### Attributes

* `hebrewdate` – The `HebrewDate` of this yemama.
* `location` – The `Location` used for all astronomical and halachic calculations.
* `custom` – The `Custom` settings (day definition, dawn, misheyakir, nightfall, and watch count).

### Constructors

```python
def __init__(self, hebrewdate, location, custom)
```

Creates a LocalHebrewDate that immediately knows all its zmanim.  The constructor stores the arguments and lazily computes events, bands, and sun objects on first access.

### Properties – Solar & Twilight

```python
@property
def sun(self)
```

The Sun object for the current Hebrew date.

```python
@property
def sunyesterday(self)
```

The Sun object for the previous Hebrew date.

```python
@property
def sunrise(self)
```

Sunrise as a DateTime (UTC).

```python
@property
def sunset(self)
```

Sunset as a DateTime (UTC).

```python
@property
def dawn(self)
```

Halachic dawn as a DateTime, according to the custom’s dawn setting.

```python
@property
def nightfall(self)
```

Halachic nightfall as a DateTime.  For GRA, this is computed from the previous day’s sunset; for MA, from the current day’s sunset.

```python
@property
def misheyakir(self)
```

Misheyakir (earliest tallit/tefillin) as a DateTime.

### Properties – Yemama Boundaries

```python
@property
def yemamastart(self)
```

The start of the halachic cycle (previous evening: sunset for GRA, nightfall for MA).

```python
@property
def daystart(self)
```

The start of halachic daylight (sunrise for GRA, dawn for MA).

```python
@property
def yemamaend(self)
```

The end of the halachic cycle (sunset for GRA, nightfall for MA).

### Properties – Daily Zmanim

```python
@property
def shemaend(self)
```

End of the Shema period (3 seasonal hours after daystart).

```python
@property
def amidahend(self)
```

End of the Amidah period (4 seasonal hours after daystart).

```python
@property
def noon(self)
```

Halachic midday (6 seasonal hours after daystart).

```python
@property
def mincha(self)
```

Mincha Gedolah (6.5 seasonal hours after daystart).

```python
@property
def minchaketana(self)
```

Mincha Ketana (9.5 seasonal hours after daystart).

```python
@property
def plagmincha(self)
```

Plag Mincha (10.75 seasonal hours after daystart).

```python
@property
def midnight(self)
```

Halachic midnight (exactly halfway between yemamastart and daystart).

### Properties – Lengths

```python
@property
def daylength(self)
```

Duration of the halachic daytime in seconds.

```python
@property
def nightlength(self)
```

Duration of the halachic night in seconds.

### Properties – Navigation

```python
@property
def previousyemama(self)
```

A new LocalHebrewDate for the previous Hebrew date, using the same location and custom settings.

```python
@property
def nextyemama(self)
```

A new LocalHebrewDate for the next Hebrew date, using the same location and custom settings.

### Properties – Bands & Events

```python
@property
def halakhicbands(self)
```

A list of Band objects representing the eight prayer bands (Nightfall, Dawn, Misheyakir, Shema, Amidah, Mincha Gedolah, Mincha Ketana, Plag Mincha).  Each band has start/end Events with full DateTime and LocalHebrewDateTime representations.

```python
@property
def daynightbands(self)
```

A list of Band objects that divide the full yemama cycle into night watches, twilight gaps, morning, and afternoon.  The watch count (3 or 4) is controlled by custom.watches.

```python
@property
def events(self)
```

A list of all 14 zmanim Event objects for this yemama, each tagged with its Zman enum and carrying a localHebrewDateTime with the seasonal hour.

### Methods

```python
def hour(self, time)
```

Given a civil Time (UTC), returns the corresponding seasonal hour as a float (0.0–24.0) on the academic dial.

```python
def angle(self, hour)
```

Given a seasonal hour (float), returns the angle in degrees (0° = noon) for drawing the clock hand.  The angle automatically adapts to the varying day/night arc lengths of the yemama.
