# Hebrew Date Library

## HebrewDate Class

### Attributes

* `year` – The Hebrew year number (e.g., 5786).
* `month` – The month of the year as a `HebrewMonth` enum member.
* `day` – The day of the month, starting at 1.
* `ordinal` – The absolute day count since the Hebrew calendar epoch. Used for conversion to and from `Date`.

### Constructors

```python
def __init__(self, year=1, month=HebrewMonth.TISHREI, day=1)
```

Creates a HebrewDate from a Hebrew year, month, and day.

```python
@classmethod
def fromordinal(cls, ordinal)
```

Creates a HebrewDate from an absolute ordinal day count.

```python
@classmethod
def fromdate(cls, date)
```

Creates a HebrewDate from a Date object.

### Properties

```python
@property
def next(self)
```

Returns the following Hebrew calendar day as a new HebrewDate.

```python
@property
def prev(self)
```

Returns the preceding Hebrew calendar day as a new HebrewDate.

```python
@property
def dayofweek(self)
```

Returns the day of the week as an integer, where 1 = Sunday and 7 = Saturday.

### Static Helpers

```python
@staticmethod
def isleapyear(year)
```

Returns True if the given Hebrew year is a leap year (contains Adar II).

```python
@staticmethod
def nummonthinyear(year)
```

Returns the number of the last month in the year (12 = Adar, 13 = Adar II).

```python
@staticmethod
def elapseddays(year)
```

Returns the number of days from the creation epoch to the start of Tishrei of the given year.

```python
@staticmethod
def numdaysinyear(year)
```

Returns the total number of days in the given Hebrew year.

```python
@staticmethod
def haslongheshvan(year)
```

Returns True if Cheshvan has 30 days in the given year.

```python
@staticmethod
def hasshortkislev(year)
```

Returns True if Kislev has 29 days in the given year.

```python
@staticmethod
def numdaysinmonth(year, month)
```

Returns the number of days in the given month of the given year.
