# HebrewDate

## HebrewDate

```java
public final class HebrewDate {
	public final int year;
	public final int month;
	public final int day;

	public HebrewDate(int year, int month, int day);

	public static HebrewDate fromEpochDays(int epochDays);

	public static boolean isLeapYear(int year);
	public static int numMonthInYear(int year);
	public static int numDaysInYear(int year);
	public static int numDaysInMonth(int year, int month);
	public static boolean hasLongHeshvan(int year);
	public static boolean hasShortKislev(int year);

	public int epochDays();
	public int weekDay();
	public HebrewHoliday holiday();
}
```

## HebrewHoliday

```java
public enum HebrewHoliday {
	NONE,
	PESACH,
	CHOL_HAMOED_PESACH,
	PESACH_VII,
	YOM_HASHOAH,
	YOM_HAZIKKARON,
	YOM_HAATZMAUT,
	PESACH_SHENI,
	LAG_BAOMER,
	YOM_YERUSHALAYIM,
	SHAVUOT,
	SHIVA_ASAR_BETAMMUZ,
	TISHA_BEAV,
	TU_BEAV,
	ROSH_HASHANA,
	ROSH_HASHANA_II,
	TZOM_GEDALIAH,
	YOM_KIPPUR,
	SUKKOT,
	CHOL_HAMOED_SUKKOT,
	HOSHANA_RABBAH,
	SIMCHAT_TORAH,
	CHANUKKA_I,
	CHANUKKA_II,
	CHANUKKA_III,
	CHANUKKA_IV,
	CHANUKKA_V,
	CHANUKKA_VI,
	CHANUKKA_VII,
	CHANUKKA_VIII,
	ASARA_BETEVET,
	TU_BISHVAT,
	TAANIT_ESTHER,
	PURIM,
	SHUSHAN_PURIM
}
```

## Torah

```java
public final class Torah {
	public final Parashah[] parashot;
	public final SpecialReading special;

	public Torah(HebrewDate date);
	public Torah(HebrewDate date, boolean diaspora);
}
```

## Parashah

```java
public enum Parashah {
	BERESHIT,
	NOACH,
	LECHLECHA,
	VAYERA,
	CHAYEISARAH,
	TOLEDOT,
	VAYETZE,
	VAYISHLACH,
	VAYESHEV,
	MIKETZ,
	VAYIGASH,
	VAYECHI,
	SHEMOT,
	VAEIRA,
	BO,
	BESHALACH,
	YITRO,
	MISHPATIM,
	TERUMAH,
	TETZAVEH,
	KITISA,
	VAYAKHEL,
	PEKUDEI,
	VAYIKRA,
	TZAV,
	SHEMINI,
	TAZRIA,
	METZORA,
	ACHAREIMOT,
	KEDOSHIM,
	EMOR,
	BEHAR,
	BECHUKOTAI,
	BAMIDBAR,
	NASO,
	BEHAALOTECHA,
	SHELACH,
	KORACH,
	CHUKAT,
	BALAK,
	PINCHAS,
	MATOT,
	MASEI,
	DEVARIM,
	VAETCHANAN,
	EIKEV,
	REEH,
	SHOFTIM,
	KITEITZEI,
	KITAVO,
	NITZAVIM,
	VAYEILECH,
	HAAZINU,
	VEZOTHABERACHAH
}
```

## SpecialReading

```java
public enum SpecialReading {
	SHEKALIM,
	ZAHOR,
	PARAH,
	HAHODESH,
	HAGGADOL,
	ROSH_HASHANAH_I,
	YOM_KIPPUR,
	SUCCOTH_I,
	HOL_HAMOED_SUCCOTH,
	SHEMINI_AZERETH,
	PESAH_I,
	PESAH_VII,
	PESAH_VIII,
	SHAVUOTH_II,
	HOL_HAMOED_PESAH
}
```