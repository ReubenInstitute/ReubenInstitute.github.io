# Geo

## Geo

```java
public final class Geo {
	public static final double EARTH_WGS84_RADIUS;
	public static final double EARTH_RADIUS;
}
```

## Location

```java
public class Location {
	public final double latitude;
	public final double longitude;

	public Location(double latitude, double longitude);

	public double distance(Location other);
	public double direction(Location other);
}
```

## Place

```java
public enum Place {
	NONE,
	OFAKIM,
	OR_HAGANUZ,
	EILAT,
	// … many other Israel / world locations …
	TEL_AVIV,
	UMAN,
	AMSTERDAM,
	BANGKOK,
	BUDAPEST,
	DUBAI,
	LONDON,
	NEW_YORK,
	PARIS,
	KYIV,
	ROME;

	public final double latitude;
	public final double longitude;
	public final double area;

	public Location location();
	public static Place fromCoordinates(double latitude, double longitude);
	public static Place closest(Location loc);
	public boolean isDiaspora();
}
```

## PlaceNames

```java
public class PlaceNames {
	public static String hebrewName(Place place, java.util.Locale locale);
	public static String englishName(Place place, java.util.Locale locale);
}
```
