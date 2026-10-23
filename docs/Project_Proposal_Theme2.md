# SPATIAL-SENSE: Project Proposal

### A 360° Wearable Haptic-Sonar Waistband for Upper-Torso and Head-Level Collision Protection in Deaf-Blind Mobility

**Competition:** Vishwakarma Awards 2026–27  
**Track:** Theme 2 — Assistive Solutions (EnAble India)  
**Mentoring Institution:** IIT Indore & Maker Bhavan Foundation  
**Team Name:** TEAM TECHTONICS  
**Document Revision:** Stage 2 Final Submission Specification  

---

## 1. Executive Summary & Problem Definition

In India, an estimated **450,000 deaf-blind individuals** (and millions more with combined visual and age-related hearing impairment) face severe mobility constraints and chronic physical danger during daily navigation. 

### The Fundamental Cane Sweep Geometry Blindspot
The primary mobility tool for the visually impaired is the conventional white cane. By physical design and biomechanics:
- The cane tip oscillates along the ground plane in an arc (30° to 45° left and right of the user's travel axis).
- It provides tactile preview of the surface 1 to 2 paces ahead, reliably warning of curbs, surface drop-offs, potholes, steps, and obstacles up to roughly knee or waist height.
- **The Blindspot**: The physical geometry of the cane leaves the user's **upper torso, chest, neck, face, and cranium (the zone between 1.0 m and 2.1 m elevation) entirely unprotected**.

### Overhead and Waist-Level Hazards in the Indian Infrastructure
In typical Indian urban and semi-urban environments, hazardous overhead obstacles abound:
- Low-hanging, unpruned tree branches and bamboo scaffolding.
- Commercial shop awnings, metal signboards, and roll-up shutter edges protruding into sidewalks.
- Open casement windows, air conditioner outdoor compressor units, and wall-mounted electrical junction boxes.
- Protruding cargo beds of parked or idling auto-rickshaws and medium goods vehicles (tata ace / tempo).

### The Critical Gap for the Deaf-Blind Population
Existing commercial electronic travel aids (ETAs) such as ultrasonic smart canes or optical smart glasses invariably rely on **audio feedback** (piezo beeps, frequency-modulated tones, or synthesized voice alerts). For a deaf-blind individual, auditory feedback is completely imperceptible. 

Furthermore, head-mounted or hand-held devices introduce severe usability penalties:
1. **Head-mounted cameras/sensors**: Socially stigmatizing, heavy on the nose bridge/ears, cause severe neck fatigue during prolonged walking, and risk dislodging upon minor contact.
2. **Hand-held devices**: Occupy the user's free hand, depriving them of the ability to hold a cane, use tactile sign language (Protactile), touch guide rails, or maintain balance.

---

## 2. Proposed Technical Solution: SPATIAL-SENSE

**SPATIAL-SENSE** is an ergonomic, solid-state, hands-free wearable waistband acting as a **360° tactile collision radar**. It operates on three foundational engineering principles:

```
                  +----------------------------------------------+
                  |         OVERHEAD PLANE (+25° ELEVATION)      |
                  |  4x VL53L1X ToF (FL, FR, RL, RR)             |
                  |  Detects: Awnings, Branches, Trucks (up to 2.1m)|
                  +----------------------+-----------------------+
                                         |
                                         v
   +-------------------------------------+-------------------------------------+
   |                      CENTRAL ESP32-S3 CORE                              |
   |   - Interleaved 4ms Phase-Shifted ToF Polling via TCA9548A Mux            |
   |   - Real-Time Dual-Core FreeRTOS Pipeline (<15ms Latency)                |
   |   - Distance-to-Cadence Mapping (1.2s -> 12Hz) with 3.0s Fatigue Decay    |
   +-------------------------------------+-------------------------------------+
                                         |
                                         v
                  +----------------------+-----------------------+
                  |         WAIST-LEVEL PLANE (0° ELEVATION)     |
                  |  4x VL53L1X ToF (Front, Rear, Left, Right)   |
                  |  Detects: Walls, Pedestrians, Posts (0.8-1.2m)|
                  +----------------------------------------------+
```

1. **Dual-Elevation Spatial Geometry**:
   - **Waist-Level Horizontal Plane (0°)**: Four Time-of-Flight (ToF) sensors scan orthogonal directions (Front, Rear, Left, Right) to detect walls, pillars, approaching pedestrians, and waist-height obstacles.
   - **Overhead Plane (+25° Upward Tilt)**: Four alternating ToF sensors scan at an upward elevation of +25° (Front-Left, Front-Right, Rear-Left, Rear-Right). From a typical wearing height of 1.0 m, a 25° upward cone projects coverage reaching from 1.2 m to **2.1 m vertical height** within a 1.5 m to 2.5 m forward radius—intercepting overhead hazards before head impact.

2. **360° Directional Vibrotactile Mapping**:
   - Eight Linear Resonant Actuators (LRAs) are embedded directly against the user’s waist circumference, mapped 1:1 to the eight sensor vectors.
   - Obstacle location is intuitively resolved by the human brain: an obstacle to the front-right vibrates the front-right mechanoreceptors; an obstacle behind vibrates the dorsal waistline.

3. **Proximity-to-Cadence Dynamic Encoding**:
   - Rather than varying intensity (which desensitizes skin mechanoreceptors), distance is encoded by **pulse cadence**:
     - Far zone ($2.5\text{ m}$): Slow, gentle reminder pulses ($1.2\text{ s}$ intervals).
     - Mid zone ($1.2\text{ m}$): Intermediate pulses ($4\text{ Hz}$).
     - Danger zone ($0.4\text{ m}$): Rapid, urgent tactile bursts ($12\text{ Hz}$).
   - **Anti-Fatigue Decay Window**: When a user halts before an obstacle, tactile actuation smoothly decays to 35% duty cycle after **3.0 seconds**, eliminating numbness while retaining spatial awareness.

---

## 3. Beneficiary Analysis & Target Population

| Beneficiary Category | Primary Need / Limitation | SPATIAL-SENSE Value Proposition |
| :--- | :--- | :--- |
| **Primary: Deaf-Blind Individuals (~450k in India)** | Cannot see overhead hazards; cannot hear acoustic beeps from smart canes; needs tactile-only communication. | 100% silent, non-auditory, intuitive 360° tactile waist feedback. Completely hands-free, allowing continuous white cane operation. |
| **Secondary: Visually Impaired Elderly with Presbycusis** | Reduced high-frequency auditory perception; cane sweep fatigue; elevated fall and head-injury risk. | Hands-free posture; lightweight waist distribution (<280g); non-fatiguing haptic warnings that bypass degraded hearing. |
| **Institutional: EnAble India & O&M Trainers** | Lack of objective, real-time spatial awareness feedback during indoor/outdoor mobility training sessions. | Companion BLE application with 360° visual radar mirror allows trainers to monitor real-time obstacle proximity remotely. |

---

## 4. Key Engineering Target Specifications

| Parameter | Proposed Design Specification | Design Justification |
| :--- | :--- | :--- |
| **Microcontroller** | Espressif ESP32-S3 Dual-Core Xtensa LX7 @ 240 MHz | Core 0 dedicated to I2C sensor scheduling; Core 1 for DSP haptics & BLE. |
| **Optical Ranging Sensors** | 8x STMicroelectronics VL53L1X FlightSense ToF | 940 nm VCSEL laser Class 1 eye-safe; 4.0 m max range; 27° field of view. |
| **I2C Multiplexer** | 2x TI TCA9548A Low-Voltage 8-Channel Switch | Overcomes single fixed I2C address (0x29) of VL53L1X; 400 kHz Fast-Mode. |
| **Haptic Actuators** | 8x Linear Resonant Actuators (LRA, 10 mm coin) | 205 Hz resonant frequency; 2.2 G peak acceleration; 5 ms fast transient braking. |
| **Haptic Drivers** | 8x TI DRV2605L Haptic Driver ICs | Hardware auto-resonance tracking, back-EMF calibration, 150 mA current limit. |
| **Inertial Measurement Unit** | Bosch Sensortec BMI160 6-DoF IMU | Zero-motion detection triggers ultra-low-power sleep (15 µA) after 60s inactivity. |
| **System Latency** | **< 15 ms** (Sensor capture to skin actuation) | Prevents obstacle collision at brisk walking pace (1.2 m/s). |
| **Aggregate Sensor Refresh** | **15 Hz** (66 ms full 360° cycle) | Interleaved round-robin firing with 4 ms phase offsets prevents optical crosstalk. |
| **Total Weight** | **280 grams** (including 2000 mAh Li-ion cell) | Ergonomically balanced across pelvic girdle; zero neck or wrist strain. |
| **Battery Autonomy** | **12 hours continuous operation** | 3.7V 2000 mAh Li-ion (103450 cell); ~145 mA average active system draw. |
| **Enclosure Rating** | **IP54 Dust and Splash Resistant** | Hydrophobic mesh acoustic/optical vents; TPU gasket seals. |

---

## 5. Cost Breakdown & Economic Viability

The project maintains transparent financial accounting across development stages:

1. **Stage 2 Functional Prototype BOM**: **₹9,500**  
   - Includes discrete breakout boards, industrial-grade 3D printed TPU/PETG enclosures, custom 2-layer polyimide FPC harness, high-precision ST/TI semiconductor components, and rapid fabrication tooling.
2. **Projected Volume Manufacturing Cost (1,000+ units)**: **₹3,650**  
   - Achieved via bare silicon component placement on single rigid-flex assembly, injection-molded TPU enclosures, bulk component reel sourcing, and automated testing jigs.
3. **Target Retail / Subsidized Price**: **₹4,500**  
   - Positioned to be accessible through government assistive aid schemes (e.g., ADIP Scheme in India) and NGO procurement channels (EnAble India, NAB India).

---

## 6. Implementation Roadmap

```
+-----------------------------------------------------------------------------------+
| MONTH 1-2: Core Hardware & Optics | MONTH 3-4: DSP & Tactile Architecture         |
| - 8-channel interleaved FPC layout| - Auto-resonance DRV2605L calibration (205Hz) |
| - 0° & +25° ray-trace verification| - 3-tap median filter & cadence curve tuning  |
| - Optical crosstalk bench test    | - Anti-fatigue 3.0s decay window validation   |
+-----------------------------------+-----------------------------------------------+
| MONTH 5: Mechanical & IP54 Sealing| MONTH 6: Clinical & O&M Field Validation      |
| - Dual-durometer TPU/PETG housing | - 50m structured obstacle course trial        |
| - Thermal profiling (<34.5°C skin)| - EnAble India deaf-blind cohort testing      |
| - Quick-release magnetic buckle   | - O&M trainer companion app radar validation  |
+-----------------------------------------------------------------------------------+
```

---

## 7. Expected Impact & Alignment with EnAble India

1. **Restoration of Independent Travel**: Eliminates debilitating fear of overhead head injuries, expanding travel radius for deaf-blind individuals by an estimated 3x.
2. **Preservation of Ergonomics**: Unlike handheld or head-mounted gear, the hands-free waist form factor ensures natural arm swing and uninhibited cane manipulation.
3. **Institutional Scalability**: With a target BOM under ₹3,650 in volume, SPATIAL-SENSE can be distributed through national disability initiatives at 1/10th the cost of imported single-direction ETAs.
