# SPATIAL-SENSE System Architecture Specification

## Project Identity
- **Project Title**: SPATIAL-SENSE
- **Full Nomenclature**: A 360° Wearable Haptic-Sonar Waistband for Upper-Torso and Head-Level Collision Protection in Deaf-Blind Mobility
- **Competition**: Vishwakarma Awards 2026–27 (Stage 2)
- **Theme**: Theme 2 — Assistive Solutions (EnAble India), IIT Indore
- **Team**: TEAM TECHTONICS

---

## 1. Perception Subsystem: Dual-Elevation Optical Sensing

```
                         +25° Elevation Cone (Up to 2.1 m)
                          /
                         /  [Head & Cranium Protection]
                        /
Waist Level (0°) ======o=================================> (Waist Protection)
                       |
                       |  [SPATIAL-SENSE Wearable Belt]
```

### Optical Array Configuration
- **Emitter/Receiver**: 8x STMicroelectronics VL53L1X Time-of-Flight (ToF) micro-LiDAR modules.
- **Wavelength**: 940 nm Class-1 eye-safe infrared VCSEL (IEC 60825-1:2014 compliant).
- **Field of View (FoV)**: 27° conical diagonal projection per sensor.
- **Elevation Geometry**:
  - **Waist-Level Plane (0°)**: 4 sensors located at Front (0°), Right (90°), Rear (180°), and Left (270°). Detects waist-level walls, pedestrians, pillars, and street furniture.
  - **Overhead Plane (+25°)**: 4 alternating sensors located at Front-Right (45°), Rear-Right (135°), Rear-Left (225°), and Front-Left (315°). Projects an upward protective cone from chest level to 2.1 m height, detecting low-hanging tree branches, shop awnings, and open windows.
- **Interleaved Multiplexing**:
  - Controlled via Texas Instruments TCA9548A 8-channel I²C switch (Address `0x70`).
  - Interleaved sequence: `1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4 -> 8` with 4 ms phase offsets.
  - Prevents optical photon crosstalk and false distance dropouts while maintaining 15 Hz aggregate refresh rate.

---

## 2. Processing Subsystem: ESP32-S3 Dual-Core DSP

- **Core 0 (Sensor Engine)**: Non-blocking Fast-Mode I²C (400 kHz) bus transactions, TCA9548A multiplexer channel selection, interleaved firing timing, and 3-tap temporal median filtering.
- **Core 1 (Haptic Engine)**: Distance-to-cadence mapping, spatial haptic vector interpolation across physical nodes, and 3-second alert decay window.
- **ULP Coprocessor**: Continuous polling of the Bosch BMI160 6-DOF IMU. Automatically transitions system into 15 µA light sleep when stationary; wakes main processing cores within 5 ms upon step detection.
- **Latency Budget**: Total end-to-end sensor-to-actuation processing response is under 15 ms.

---

## 3. Actuation Subsystem: Resonant Tactile Feedback

- **Actuator Selection**: 8x Linear Resonant Actuators (LRAs) tuned to mechanical resonance ($205\text{ Hz} \pm 3\text{ Hz}$).
- **Driver Circuitry**: 8x TI DRV2605L motor controllers communicating over dedicated I²C Bus 1. Auto-tracks back-EMF resonance and enforces a 150 mA hardware current limit.
- **Tactile Acceleration**: Up to 2.2 G peak acceleration with 5 ms fast rise time against the user's abdominal wall.
- **Cadence Gradient**:
  - Distance $\ge 2.5\text{ m}$: Quiescent.
  - Distance $= 2.5\text{ m}$: 1.2 s gentle pulse rhythm.
  - Distance $= 0.4\text{ m}$: 12 Hz emergency tactile burst.

---

## 4. Power & Safety Subsystem

- **Battery**: 3.7 V 2500 mAh rechargeable Li-ion 1S cell (IEC 62133 safety reference).
- **Hardware BMS**: 4.25 V over-voltage protection, 2.80 V under-voltage protection, 2.0 A over-current protection.
- **Thermal Safety**: Designed to sustain skin-facing pod surface temperature below 34.5°C under continuous 60-minute actuation.
- **Charging Interface**: Standard 5V USB-C interface.

---

## 5. User Interface & Accessibility

- **Deaf-Blind End User Mode**: 100% non-visual, non-auditory primary alerts. Includes a zero-sight hardware self-test (double-tapping the belt button triggers a clockwise haptic verification sweep).
- **O&M Trainer Mirror**: Offline-first BLE companion mobile app displaying a real-time 360° radar view of detected obstacles and telemetry for orientation and mobility trainers.
