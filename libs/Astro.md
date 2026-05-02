# Astro

## Astro

```java
public final class Astro {
	public static final double J2000;
	public static final double EARTH_OBLIQUITY;
}
```

## Sun

```java
public class Sun {
	public Sun(Location location);

	public DateTime sunrise(Date date);
	public DateTime sunset(Date date);
}
```

## Moon

```java
public class Moon {
	public final DateTime rise;
	public final DateTime set;
	public final double illuminationFraction;
	public final double phase;
	public final double angle;
	public final String emoji;

	public Moon(Location location, DateTime datetime);
}
```
