# Date

## Date

```java
public final class Date {
	public final int year;
	public final int month;
	public final int day;

	public Date(int year, int month, int day);

	public static Date today();
	public static Date fromEpochDays(int epochDays);
	public static Date fromJulianDay(double julianDay);

	public static boolean isLeapYear(int year);
	public static int numDaysInMonth(int month, int year);

	public int epochDays();
	public double julianDay();
	public int weekDay();

	public Date add(DaysSpan span);
	public Date subtract(DaysSpan span);
	public DaysSpan difference(Date other);
}
```

## DaysSpan

```java
public final class DaysSpan {
	public final int days;

	public DaysSpan(int days);
}
```

## Time

```java
public final class Time {
	public final int hour;
	public final int minute;
	public final double second;

	public Time(int hour, int minute, double second);

	public static Time now();
	public static Time fromDaySeconds(double daySeconds);

	public double daySeconds();
	public String toString();
}
```

## HoursSpan

```java
public final class HoursSpan {
	public final int hours;

	public HoursSpan(int hours);
}
```

## SecondsSpan

```java
public final class SecondsSpan {
	public final double seconds;

	public SecondsSpan(double seconds);
}
```

## DateTime

```java
public final class DateTime {
	public final Date date;
	public final Time time;

	public DateTime(Date date, Time time);

	public static DateTime now();
	public static DateTime fromJulianDay(double julianDay);

	public double julianDay();
	public DateTime local();

	public DateTime add(DaysSpan span);
	public DateTime subtract(DaysSpan span);
	public DateTime add(HoursSpan span);
	public DateTime subtract(HoursSpan span);
	public DateTime add(SecondsSpan span);
	public DateTime subtract(SecondsSpan span);

	public SecondsSpan difference(DateTime other);
}
```
