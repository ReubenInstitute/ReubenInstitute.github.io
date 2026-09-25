# Misc

## Names

Multilingual display strings for Gregorian months, Hebrew months, and Hebrew holidays.

```java
public final class Names {
	public static String gregorianMonthName(int month, Language lang);
	public static String gregorianMonthShortName(int month, Language lang);
	public static String hebrewMonthName(int month, int year, Language lang);
	public static String hebrewHolidayName(HebrewHoliday holiday, Language lang);
}
```

## Language

Enumeration of all supported locale languages, used by Names.

```java
public enum Language {
	ENGLISH,
	HEBREW,
	SPANISH,
	RUSSIAN,
	AMHARIC,
	ARABIC
}
```
