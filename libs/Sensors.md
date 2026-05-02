# Sensors

## Gyroscope

```java
public class Gyroscope {
	public Vector3D angularVelocity;
	public Vector3D bias;
	public Vector3D correctedAngularVelocity;
	public Quaternion quaternion;

	public Gyroscope();
	public void update(Vector3D angularVelocity, DateTime timestamp);
	public void applyBiasCorrection(Vector3D correction);
	public void setOrientation(Quaternion q);
}
```

## Accelerometer

```java
public class Accelerometer {
	public Vector3D acceleration;
	public DateTime timestamp;
	public Vector3D gravity;

	public Accelerometer();
	public void update(Vector3D acceleration, DateTime timestamp);
}
```

## Magnetometer

```java
public class Magnetometer {
	public Vector3D magneticField;
	public DateTime timestamp;
	public Vector3D magneticHorizontal;

	public Magnetometer();
	public void update(Vector3D magneticField, DateTime timestamp, Vector3D gravity);
}
```

## Barometer

```java
public class Barometer {
	public float pressure;
	public DateTime timestamp;
	public double altitude;

	public Barometer();
	public void update(float pressure, DateTime timestamp);
	public void applyAltitudeCorrection(double correction);
	public boolean hasData();
}
```

## GPS

```java
public class GPS {
	public double latitude, longitude, altitude;
	public float horizontalAccuracy, verticalAccuracy;
	public float speed, bearing;
	public float speedAccuracy, bearingAccuracy, timeAccuracy;
	public double elapsedRealtime;
	public DateTime datetime;
	public Location location;
	public Vector2D velocity;

	public GPS();
	public void update(double latitude, double longitude, float horizontalAccuracy,
			double altitude, float verticalAccuracy,
			float speed, float bearing, float speedAccuracy, float bearingAccuracy,
			DateTime datetime, double elapsedRealtime, float timeAccuracy);
	public boolean hasData();
	public boolean isPositionReliable();
	public boolean isVelocityReliable();
	public boolean isFresh(DateTime now);
	public boolean isReliable(DateTime now);
}
```

## Fusion

```java
public class Fusion {
	public final Gyroscope gyroscope;
	public final Accelerometer accelerometer;
	public final Magnetometer magnetometer;
	public final Barometer barometer;
	public final GPS gps;

	public Vector2D speed;
	public double verticalSpeed;
	public Location location;
	public double altitude;
	public Vector3D orientation;

	public double[][] covariance;
	public Matrix kalmanGain;
	public Matrix magnetometerKalmanGain;

	public Vector3D expectedGravityDirection;
	public Vector3D gravityError;
	public Vector3D expectedMagneticField;
	public Vector3D magneticError;
	public Vector2D gpsPositionError;
	public Vector2D gpsVelocityError;
	public Vector3D gpsHeadingError;
	public double barometerAltitudeError;

	public Fusion(Gyroscope gyroscope, Accelerometer accelerometer,
			Magnetometer magnetometer, Barometer barometer, GPS gps,
			Location initialLocation, double initialAltitude);

	public void updateGyroscope(Vector3D angularVelocity, DateTime timestamp);
	public void updateAccelerometer(Vector3D acceleration, DateTime timestamp);
	public void updateMagnetometer(Vector3D magneticField, DateTime timestamp);
	public void updateBarometer(float pressure, DateTime timestamp);
	public void updateGps(double latitude, double longitude, float horizontalAccuracy,
			double altitude, float verticalAccuracy,
			float speed, float bearing, float speedAccuracy, float bearingAccuracy,
			DateTime datetime, double elapsedRealtime, float timeAccuracy);
	public void fuse(DateTime timestamp);
}
```