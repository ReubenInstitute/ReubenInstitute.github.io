# Algebra

## Vector2D

```java
public class Vector2D {
	public final double x;
	public final double y;

	public Vector2D(double x, double y);

	public Vector2D add(Vector2D other);
	public Vector2D subtract(Vector2D other);
	public Vector2D scale(double s);
	public double dot(Vector2D other);
	public double length();
	public Vector2D normalise();
}
```

## Vector3D

```java
public class Vector3D {
	public final double x;
	public final double y;
	public final double z;

	public Vector3D(double x, double y, double z);

	public Vector3D add(Vector3D other);
	public Vector3D subtract(Vector3D other);
	public Vector3D cross(Vector3D other);
	public double dot(Vector3D other);
	public double length();
	public Vector3D normalise();
	public Vector3D scale(double s);
}
```

## Quaternion

```java
public class Quaternion {
	public final double w, x, y, z;

	public Quaternion(double w, double x, double y, double z);

	public Quaternion hamiltonProduct(Quaternion q);
	public Quaternion normalise();
	public Quaternion conjugate();
	public Vector3D rotate(Vector3D v);
	public static Quaternion fromAxisAngle(Vector3D axis, double angle);
}
```

## Matrix

```java
public class Matrix {
	public final double[][] data;

	public Matrix(int rows, int cols);
	public static Matrix identity(int n);
	public static Matrix fromArray(double[][] data);

	public Matrix transpose();
	public Matrix multiply(Matrix other);
	public Matrix subtract(Matrix other);
	public Matrix add(Matrix other);
	public void symmetrise();
	public Matrix invert3x3();
}
```
