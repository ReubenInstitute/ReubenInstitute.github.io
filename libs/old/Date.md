# Date & Time Library

## Date Class

### Attributes

* `year` – The Gregorian year (e.g., 2026).
* `month` – The month of the year as an integer (1 = January, 12 = December).
* `day` – The day of the month, starting at 1.
* `ordinal` – The absolute day count since 1 January 0001 (the Chronological Julian Day Number). This integer is the backbone of all calendar arithmetic and conversion.



### Constructors

```python
def __init__(self, year=1, month=1, day=1)
```

Creates a `Date` from a Gregorian year, month, and day.

---

```python
@classmethod
def fromordinal(cls, ordinal)
```

Creates a `Date` from an absolute ordinal day count.

### Properties

```python
@property
def next(self)
```

Returns the following calendar day as a new `Date`.

```python
@property
def prev(self)
```

Returns the preceding calendar day as a new `Date`.

```python
@property
def dayofweek(self)
```

Returns the day of the week as an integer, where 1 = Sunday and 7 = Saturday.

### Operators

```python
def __add__(self, days)
```

Returns a new `Date` advanced by the given number of days.

```python
def __sub__(self, days)
```

Returns a new `Date` moved back by the given number of days.

### Static Helpers

```python
@staticmethod
def isleapyear(year)
```

Returns `True` if the given Gregorian year is a leap year.

```python
@staticmethod
def numdaysinmonth(month, year)
```

Returns the number of days in the given month (1–12), accounting for leap years when `month` is February.


## Time Class

### Attributes

* `hour` – The hour component (0–23).
* `minute` – The minute component (0–59).
* `second` – The second component (0–59).
* `serial` – Total seconds since midnight (0–86399). This integer is the backbone of all time arithmetic, and the only place where the constant `86400` is used as a wrap-around limit.

### Constructors

```python
def __init__(self, hour=0, minute=0, second=0)
```

Creates a `Time` from hour, minute, and second components.

```python
@classmethod
def fromserial(cls, serial)
```

Creates a `Time` from a total-seconds-since-midnight value.

### Operators

```python
def __add__(self, seconds)
```

Returns a new `Time` advanced by the given number of seconds, wrapping within the 24-hour day (modulo 86400).


## DateTimeSpan Class

### Attributes

* `days` – The difference in whole calendar days.
* `seconds` – The remaining seconds within the day (always 0–86399).

### Constructors

```python
def __init__(self, days, seconds)
```

Creates a `DateTimeSpan` from a day count and a seconds count.


## DateTime Class

### Attributes

* `date` – The `Date` component.
* `time` – The `Time` component.

### Constructors

```python
def __init__(self, date, time)
```

Creates a `DateTime` from a `Date` and a `Time`.

```python
@classmethod
def fromjulianday(cls, julianday)
```

Creates a `DateTime` from an astronomical Julian Day number.

### Properties

```python
@property
def julianday(self)
```

Returns the astronomical Julian Day number (float), derived from the `ordinal` and `serial` of its components.

### Operators

```python
def __sub__(self, other)
```

Returns a `DateTimeSpan` representing the elapsed time between two `DateTime` objects.

```python
def __add__(self, seconds)
```

Returns a new `DateTime` advanced by the given number of seconds. Date overflow (crossing midnight) is handled automatically.

```python
def __lt__(self, other)
def __le__(self, other)
def __gt__(self, other)
def __ge__(self, other)
```

Compares two `DateTime` objects chronologically — first by `ordinal`, then by `serial`.
