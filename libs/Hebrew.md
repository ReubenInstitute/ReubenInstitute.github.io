# Hebrew

## Hebrew

```java
public final class Hebrew {
	public static String normalize(String text);
	public static String addDageshHazzak(String text);
	public static String stripPunctuation(String text);
	public static String stripCantillation(String text, boolean stripMeteg);
	public static String stripDiacritics(String text, boolean stripRafe);
	public static String stripHebrewPunctuation(String text, boolean stripMaqaf, boolean stripMasora);
	public static String stripYY(String text);
	public static String stripYHWH(String text);
	public static String presentation(String text);
	public static String rawText(String text);
	public static String transliterate(String text);
}
```

## HebrewNumbers


```java
public final class HebrewNumbers {
	public static String intToGematria(int num, boolean gershayim);
	public static int gematriaToInt(String str);
}
```
