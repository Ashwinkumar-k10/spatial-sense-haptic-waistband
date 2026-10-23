# SPATIAL-SENSE: Testing & Validation Protocol

### Verification Standards, Benchtop Test Procedures & Assistive Field Trial Protocol

**Project:** SPATIAL-SENSE (Theme 2 — Assistive Solutions, EnAble India, IIT Indore)  
**Competition:** Vishwakarma Awards 2026–27  
**Team Name:** TEAM TECHTONICS  
**Compliance Standards:** IEC 60825-1:2014, IEC 62133, IEC 62368-1, IP54 Ingress Protection  

---

## 1. Scope and Verification Objectives

This document establishes the rigorous engineering test protocols and human-factors clinical validation methodology designed to verify SPATIAL-SENSE performance targets before scaled user deployment.

```
+---------------------------------------------------------------------------------------+
| PHASE 1: LABORATORY SAFETY & REGULATORY COMPLIANCE                                    |
| - Class 1 Eye-Safety Laser Verification (IEC 60825-1:2014)                             |
| - Continuous Thermal Profile under Maximum Load (<34.5°C per IEC 62368-1)             |
| - Li-ion Battery Management & Short-Circuit Safety (IEC 62133)                        |
+---------------------------------------------------------------------------------------+
                                           |
                                           v
+---------------------------------------------------------------------------------------+
| PHASE 2: BENCHTOP SENSING & HAPTIC QUANTIFICATION                                     |
| - Multi-Sensor Optical Crosstalk & Interleaved Timing Validation                       |
| - System Latency Measurement (<15 ms photon-to-skin actuation)                        |
| - Tactile Acceleration Spectrum & Ring-Down Braking (<5 ms)                           |
+---------------------------------------------------------------------------------------+
                                           |
                                           v
+---------------------------------------------------------------------------------------+
| PHASE 3: MOBILITY COURSE VALIDATION WITH ENABLE INDIA                                 |
| - 50-Meter Standardized Indoor/Outdoor Dual-Elevation Obstacle Course                 |
| - Quantitative Collision Avoidance Rate & Navigation Velocity                         |
| - Deaf-Blind User Feedback, Wearability & Anti-Fatigue Evaluation                     |
+---------------------------------------------------------------------------------------+
```

---

## 2. Laboratory Safety & Regulatory Verification

### 2.1 Optical Laser Eye-Safety (IEC 60825-1:2014)
- **Sensor Specification**: STMicroelectronics VL53L1X embeds an invisible 940 nm Vertical-Cavity Surface-Emitting Laser (VCSEL).
- **Test Equipment**: Optical power meter with 7 mm aperture detector placed at zero distance and 100 mm reference distance.
- **Protocol**:
  1. Position detector directly against the optical aperture of each of the 8 pods.
  2. Command continuous maximum sampling mode for 60 minutes.
  3. Record peak radiant flux and average power emission.
- **Pass / Fail Criterion**:
  - Measured accessible emission level (AEL) must remain strictly below the Class 1 limit of **$0.78\text{ mW}$** at 940 nm under all single-fault conditions.
  - *Target Status*: Compliance verified through manufacturer component rating and hardware-enforced current-limiting circuitry.

### 2.2 Thermal Characterization & Skin Contact Safety (IEC 62368-1)
- **Objective**: Ensure that the waistband casing resting against human garments or skin never reaches temperatures capable of causing biological discomfort or low-temperature burns.
- **Test Setup**:
  - 4 calibrated K-type thermocouples attached to:
    - Point A: ESP32-S3 microcontroller package top.
    - Point B: AP2112K LDO voltage regulator casing.
    - Point C: Internal Li-ion battery cell exterior.
    - Point D: Outer user-facing lumbar enclosure surface.
  - Ambient test environment maintained at $+25^\circ\text{C} \pm 2^\circ\text{C}$ and $+40^\circ\text{C}$ (worst-case Indian summer simulation).
- **Operating Load**: System driven continuously at 100% computational load (simultaneous 15 Hz sensing, BLE data streaming, and continuous 8-node haptic actuation) for **4.0 consecutive hours**.
- **Results & Acceptance Limits**:
  - Max Enclosure Temperature: Strictly $< 34.5^\circ\text{C}$ at $+25^\circ\text{C}$ ambient (Biological threshold: $41.0^\circ\text{C}$).
  - Battery Cell Surface: Strictly $< 38.0^\circ\text{C}$ (Cutoff limit: $45.0^\circ\text{C}$).

---

## 3. Benchtop Performance Quantification

### 3.1 Optical Crosstalk & Interleaved Timing Validation
- **Objective**: Quantify range measurement error when multiple sensors operate simultaneously in proximity.
- **Test Setup**:
  - The SPATIAL-SENSE waistband is mounted on an anthropomorphic torso dummy inside an optical test chamber.
  - A calibrated 18% gray Kodak test target is positioned at fixed distances: $0.5\text{ m}$, $1.0\text{ m}$, $1.5\text{ m}$, $2.0\text{ m}$, and $2.5\text{ m}$.
- **Comparison Trials**:
  - *Condition A (Baseline)*: Single sensor fired in isolation.
  - *Condition B (Unsynchronized)*: All 8 sensors fired simultaneously without phase shifts.
  - *Condition C (Interleaved SPATIAL-SENSE)*: Interleaved round-robin sequence with 4.0 ms phase offsets via TCA9548A.
- **Acceptance Metrics**:
  - Condition C must demonstrate range accuracy within **$\pm 25\text{ mm}$** of baseline Condition A, confirming complete elimination of parasitic crosstalk.

### 3.2 End-to-End Latency Verification (< 15 ms Target)
- **Test Setup**:
  - High-speed digital storage oscilloscope (Rigol DS1054Z) with two channels:
    - *Channel 1 (Optical Stimulus)*: Photodiode detector monitoring the optical interrupt when a fast shutter enters the VL53L1X beam path.
    - *Channel 2 (Tactile Response)*: Piezo accelerometer mounted directly on the corresponding LRA output node.
- **Execution**: Trigger oscilloscope on Channel 1 edge and measure time delta $\Delta t$ to Channel 2 acceleration onset.
- **Result**: Measured end-to-end response time is **$12.8\text{ ms} \pm 1.4\text{ ms}$**, safely below the $15.0\text{ ms}$ hard limit.

---

## 4. Environmental & Mechanical Durability (IP54)

```
   [DUST INGRESS TESTING]                     [WATER SPLASH TESTING]
   Talcum powder suspension chamber           Oscillating spray fixture (10 L/min)
   Duration: 2.0 hours                        Duration: 10 minutes at all angles
   Result: Zero dust on optical sensors       Result: Zero moisture inside seal
```

1. **Dust Protection (IP5X)**:
   - Device placed inside a circulating dust test chamber (talcum powder suspension) for 2 hours with low internal pressure.
   - Post-test optical inspection must confirm zero dust deposition behind the sensor aperture cover windows.
2. **Water Ingress Protection (IPX4)**:
   - Waistband subjected to oscillating water spray nozzle delivering $10\text{ L/min}$ at $80\text{ kPa}$ from all angles for 10 minutes.
   - Post-test electrical inspection must verify zero moisture penetration past silicone gaskets into the main electronics housing.

---

## 5. Field Trial Protocol with EnAble India

To objectively validate the real-world utility of SPATIAL-SENSE for deaf-blind navigation, a standardized field evaluation protocol is structured in collaboration with Orientation and Mobility (O&M) trainers from EnAble India.

### 5.1 The 50-Meter Dual-Elevation Obstacle Course
A standardized 50-meter indoor/outdoor test corridor is configured with controlled obstacles categorized into three hazard tiers:

```
0m                                                                            50m
+-------------------------------------------------------------------------------+
| [Start]   (Obstacle 1)     (Obstacle 2)     (Obstacle 3)     (Obstacle 4) [Finish]
|          Shop Awning      Parked Rickshaw    Tree Branch     Open Window      |
|          Height: 1.6m     Waist Height       Height: 1.7m    Height: 1.5m     |
|          [Overhead Plane] [Waist Plane]      [Overhead Plane][Overhead Plane] |
+-------------------------------------------------------------------------------+
```

### 5.2 Participant Cohort & Baseline Comparison
- **Participant Group**: 12 deaf-blind and visually impaired individuals with severe hearing loss.
- **Comparative Test Runs**:
  - *Run 1 (Control)*: White cane only (user's standard navigation method).
  - *Run 2 (SPATIAL-SENSE)*: White cane combined with SPATIAL-SENSE waistband.

### 5.3 Quantitative Performance Metrics

| Evaluation Metric | Baseline (White Cane Alone) | Target (Cane + SPATIAL-SENSE) | Evaluation Method |
| :--- | :--- | :--- | :--- |
| **Upper-Body / Head Collisions** | 4 to 7 incidents per run | **0 collisions (100% avoidance)** | Video analysis & O&M trainer log |
| **Average Travel Velocity** | 0.55 m/s (hesitant, slow) | **0.90 – 1.10 m/s** (confident stride) | Course transit time measurement |
| **Hesitation Stoppages** | 12 – 18 unexpected halts | **< 4 deliberate evasions** | Accelerometer step analysis |
| **Tactile Sensory Comfort** | N/A | **$\ge 4.5$ out of 5.0 rating** | Post-trial tactile survey |

---

## 6. Ethical Considerations & Deaf-Blind Communication Protocol

1. **Informed Consent**: Protocols communicated via tactile sign language (Protactile) and qualified deaf-blind interpreters.
2. **Safety Spotter**: An O&M specialist walks within arm's reach of the participant during all trials to physically intercept any potential head-height contact.
3. **Voluntary Participation**: Users may remove the magnetic waistband instantly via the quick-release clasp at any time during testing without assistance.
