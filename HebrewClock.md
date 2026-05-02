# GPS Hebrew Clock

A clock that displays both Gregorian and Hebrew dates using an Arduino board, a GPS module, and a LED screen. The time is automatically adjusted using real-time data from the GPS module. The software calculates all official Hebrew holidays, fasts, and Israeli national hoslidays.

### Wall/Desktop

| Size | Display | Resolution |
|---|---|---|
|  | LED Panel | 256x64 |
| 4-7 inch | LCD | 320x240 |
| 4-7 inch | E-Paper | 320x240 |

### Mobile

| Size | Display | Resolution |
|---|---|---|
| 4 inch | LCD | 320x240 |
| 4 inch | E-Paper | 320x240 |

### Wearable

| Size | Display | Resolution |
|---|---|---|
| 1 inch | OLED | 240x240 |

## Components

| Name | Model | Description |
|---|---|---|
| **MCU** | STM32F405 | A high-performance microcontroller with an ARM Cortex-M4 core, handling all clock calculations, display updates, and sensor data processing. |
| **Temperature, Humidity, & Pressure Sensor** | BME280 | Measures ambient temperature, barometric pressure, and humidity, used for weather-related features. |
| RTC | DS3231 | Maintains accurate timekeeping even when the main power is off (using a backup battery). |
| **GPS** | NEO-6M | Provides precise time synchronization using satellite signals and retrieves location data (latitude, longitude, altitude). |
| **Motion Sensor** | MPU6050 | Tracks acceleration and gyroscopic motion, used for gesture-based interactions |
| **Magnetic Sensor** | HMC5883L | Functions as a digital compass to determine cardinal directions, used for orienting the display or additional features. |
| **Light Sensor** | BH1750 | Measures ambient light levels in lux. |
