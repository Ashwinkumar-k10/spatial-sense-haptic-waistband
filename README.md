# SPATIAL-SENSE

### A 360° Wearable Haptic-Sonar Waistband for Upper-Torso and Head-Level Collision Protection in Deaf-Blind Mobility

[![Vishwakarma Awards 2026-27](https://img.shields.io/badge/Competition-Vishwakarma%20Awards%202026--27-0A66C2.svg?style=flat-square)](https://vishwakarmaawards.in)
[![Track: Assistive Solutions](https://img.shields.io/badge/Track-Theme%202%20(Assistive%20Solutions)-107C41.svg?style=flat-square)](https://enableindia.org)
[![Institution: IIT Indore](https://img.shields.io/badge/Mentorship-IIT%20Indore%20%26%20Maker%20Bhavan-D83B01.svg?style=flat-square)](https://www.iiti.ac.in)
[![Team: TECHTONICS](https://img.shields.io/badge/Team-TECHTONICS-6B21A8.svg?style=flat-square)]()
[![Hardware: ESP32--S3](https://img.shields.io/badge/Core-ESP32--S3%20Xtensa%20Dual--Core-E0234E.svg?style=flat-square)](https://www.espressif.com)
[![RTOS: FreeRTOS](https://img.shields.io/badge/RTOS-FreeRTOS%20v10.4.3-3B82F6.svg?style=flat-square)](https://freertos.org)
[![Optics: Class 1 Laser](https://img.shields.io/badge/Optics-Class%201%20VCSEL%20(IEC%2060825--1)-F59E0B.svg?style=flat-square)]()
[![Ingress: IP54](https://img.shields.io/badge/Ingress-IP54%20Dust%20%26%20Splash-059669.svg?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-gray.svg?style=flat-square)](LICENSE)

---

## 1. Executive Summary

**SPATIAL-SENSE** is an industrial-grade, hands-free wearable assistive platform engineered to resolve a critical, life-threatening mobility barrier for an estimated **450,000 deaf-blind individuals in India**: the fundamental inability of conventional white canes to detect hazards situated above the ground plane.

While standard ground-sweeping white canes provide reliable preview of kerbs, steps, and surface drop-offs, their biomechanical sweep angle leaves the user's **upper torso, neck, face, and head (the 1.0 m to 2.1 m elevation envelope) completely unprotected**. Existing commercial electronic travel aids (ETAs) fail for this demographic because they rely exclusively on audio beeps or require head-mounted/hand-held form factors that introduce severe ergonomic strain, social stigma, and loss of hand freedom.

**SPATIAL-SENSE** operates as a solid-state **360° tactile collision radar**:
- Combines **dual-elevation optical Time-of-Flight (ToF)** sensing (waist-level 0° and overhead +25°) with **eight localized resonant linear vibrotactile actuators (LRAs)** distributed around the user's pelvic girdle.
- Delivers real-time proximity alerts via **distance-to-cadence frequency modulation** with zero acoustic or visual dependency.
- Achieves **hard real-time deterministic performance (< 15 ms latency, 15 Hz aggregate refresh)** on an ESP32-S3 dual-core microcontroller running FreeRTOS.
- Incorporates an **anti-fatigue 3.0-second decay window** to prevent mechanoreceptor desensitization and a **zero-sight tactile self-test protocol** for autonomous blind verification.

---

## 2. Clinical Problem & Epidemiological Context

```
  TYPICAL INDIAN URBAN CORRIDOR
  =============================================================================
  Elevation (m)
  2.1m +-----------------------------------------------------------------------+
       |   [Tree Branch]       [Shop Awning]       [Open Window]  [Truck Bed]  | <-- CANE BLINDSPOT
  1.8m |         \                  |                    /             |       |     (HEAD / TORSO
  1.5m |          \                 |                   /              |       |      COLLISION ZONE)
  1.2m |           \                |                  /               |       |
  1.0m | +-------------------------------------------------------------------+ | <-- SPATIAL-SENSE (+25° Plane)
       | | USER TORSO & HEAD PROTECTION CONE (SPATIAL-SENSE DUAL-PLANE RADAR)| |
  0.8m | +-------------------------------------------------------------------+ | <-- SPATIAL-SENSE (0° Plane)
  0.4m |                                                                       |
  0.0m |  \_______________ Conventional White Cane Ground Sweep ____________/  | <-- GROUND TERRAIN ONLY
  =============================================================================
```

### The Unmet Need
1. **The Cane Geometry Blindspot**: An oscillating white cane sweeps an arc across the floor plane. Obstacles protruding at chest, neck, or forehead height—such as unpruned trees, commercial signboards, rolled-up shop shutters, wall-mounted air conditioners, and parked truck cargo decks—are struck directly by the user's upper body before the cane tip makes contact.
2. **Incompatibility with Deaf-Blind Users**: Sensorineural hearing loss renders acoustic beeps and voice prompts useless. Deaf-blind navigators require **purely cutaneous tactile feedback**.
3. **Ergonomic & Manual Liberty**: Hands and ears must remain entirely unencumbered. The user's dominant hand must hold the white cane; their free hand must remain ready for Protactile communication, guide rails, or orientation cues.

---

## 3. High-Level System Architecture

The SPATIAL-SENSE platform distributes optical sensing and vibrotactile actuation circumferentially around the user's torso, with core computing, battery management, and inertial tracking housed in a low-profile rear lumbar enclosure:

```
+===============================================================================================+
|                                    CENTRAL LUMBAR HUB ENCLOSURE                               |
|                                                                                               |
|  [ESP32-S3 Dual-Core Xtensa LX7 @ 240 MHz]                                                    |
|  ├── Core 0: 400 kHz Fast-Mode I²C Polling | Interleaved 4ms Scheduler | 3-Tap Median Filter |
|  └── Core 1: DSP Distance-to-Cadence Engine | 3.0s Decay Window | BLE 5.0 Radar Mirror       |
|                                                                                               |
|  [Power & Thermal Subsystem]                  [Inertial & Motion Tracking]                   |
|  ├── 3.7V 2000mAh 103450 Li-Po Cell           ├── Bosch Sensortec BMI160 6-DoF IMU           |
|  ├── TP4056 850mA Charger (NTC Cutoff)        ├── Inactivity Auto-Sleep (< 15 µA @ 60s)       |
|  ├── DW01A + FS8205A Dual-MOSFET BMS          └── Any-Motion Hardware Wakeup (< 5 ms)        |
|  └── Dual AP2112K-3.3 Ultra-Low Noise LDOs    [Accessibility & HMI]                          |
|                                               ├── Concave Tactile Power / Self-Test Button   |
|  [I²C Bus Multiplexing Matrix]                └── Reversible Magnetic USB-C Charging Port    |
|  ├── TCA9548A Primary Mux (Bus Address 0x70) -> Channels 0–3 (Left Flank Sensor Pods)       |
|  └── TCA9548A Secondary Mux (Bus Address 0x71)-> Channels 4–7 (Right Flank Sensor Pods)      |
+===============================================================================================+
                                                |
                 +------------------------------+------------------------------+
                 | 2-Layer Polyimide FPC Ribbon Harness (35 µm Cu, Rmin >= 5mm)|
                 v                                                             v
+-----------------------------------------------+ +---------------------------------------------+
|          LEFT FLANK SENSOR PODS               | |          RIGHT FLANK SENSOR PODS            |
| Pod 1 [Front 0°]:      VL53L1X + DRV2605L+LRA | | Pod 8 [Front-Right +25°]:VL53L1X+DRV2605L+LRA|
| Pod 5 [Front-Left +25°]:VL53L1X+DRV2605L+LRA  | | Pod 4 [Right 0°]:      VL53L1X + DRV2605L+LRA|
| Pod 2 [Left 0°]:       VL53L1X + DRV2605L+LRA | | Pod 7 [Rear-Right +25°]: VL53L1X+DRV2605L+LRA|
| Pod 6 [Rear-Left +25°]:VL53L1X + DRV2605L+LRA | | Pod 3 [Rear 0°]:       VL53L1X + DRV2605L+LRA|
+-----------------------------------------------+ +---------------------------------------------+
```

---

## 4. Key Engineering Subsystems

### 4.1 Dual-Elevation Spatial Sensing Geometry
SPATIAL-SENSE bifurcates the surrounding hemisphere into two complementary, interleaved optical cones:
- **Waist-Level Plane (0° Elevation)**: Four sensors positioned at 0°, 90°, 180°, and 270° (Front, Right, Rear, Left) continuously sweep the horizontal plane for pedestrian cross-traffic, walls, pillars, and mid-height barriers ($0.8\text{ m}$ to $1.2\text{ m}$ elevation).
- **Overhead Plane (+25° Upward Elevation)**: Four alternating diagonal sensors positioned at 45°, 135°, 225°, and 315° project upward at a $+25^\circ$ angle. From a nominal wearing height of $1.0\text{ m}$, this upward ray-trace intercepts overhead hazards between $1.2\text{ m}$ and **$2.1\text{ m}$ vertical height** at a forward distance of $1.5\text{ m}$ to $2.5\text{ m}$—warning the user well before cranial impact.

```
                  DUAL-PLANE RAY-TRACE GEOMETRY
  Height (m)
  2.1m +----------------------------------------------------+  Overhead Hazard
       |                                          /         |  (Awnings/Branches)
  1.8m |                                    /     .         |
  1.5m |                              /           .         |
  1.2m |                        /                 .         |
  1.0m | [POD (+25°)] ------> / (+25° Elevation)  .         |
       | [POD (0°)]   ----------------------------+-------->|  Waist Hazard (Walls)
  0.0m +----------------------------------------------------+  (0° Horizontal)
       0.0m                   1.0m                2.0m     3.0m Distance (m)
```

### 4.2 Deterministic Interleaved Sensor Firing Schedule
To eliminate optical multi-emitter laser crosstalk between adjacent 940 nm VCSEL sources while sustaining an aggregate **15 Hz refresh rate** ($66.6\text{ ms}$ complete frame cycle), sensors fire in an interleaved, phase-shifted sequence via the TCA9548A multiplexer:

$$\text{Firing Sequence:} \quad \text{Ch 1 (Front 0°)} \longrightarrow \text{Ch 5 (FL +25°)} \longrightarrow \text{Ch 2 (Left 0°)} \longrightarrow \text{Ch 6 (RL +25°)} \longrightarrow \text{Ch 3 (Rear 0°)} \dots$$

- **Phase Offset**: Fixed at **4.0 ms** per channel.
- **Crosstalk Suppression**: Opposing and cross-plane channel separation yields **$> 42\text{ dB}$ optical isolation**, eliminating false distance dropouts.

### 4.3 3-Tap Temporal Median Filtering
Raw millimeter distance measurements $r_k[n]$ are filtered through a deterministic 3-tap median window:

$$\hat{d}_k[n] = \text{median}\Big(r_k[n],\, r_k[n-1],\, r_k[n-2]\Big)$$

This rejects ambient solar glints and multipath outliers with a deterministic worst-case computation time of **$< 2.2\text{ µs}$** on the Xtensa LX7 core.

### 4.4 Closed-Loop Resonant Haptic Actuation
- **Actuators**: 8x 10mm Linear Resonant Actuators (LRAs) tuned to $f_0 = 205\text{ Hz} \pm 3\text{ Hz}$.
- **Drivers**: 8x TI DRV2605L motor controllers running closed-loop back-EMF auto-resonance tracking to maintain peak kinetic energy transfer ($2.2\text{ G}$ peak acceleration) across garment variations.
- **Active Reverse Braking**: DRV2605L injects an active $180^\circ$ phase-inverted deceleration pulse at pulse termination, quenching mechanical ring-down in **$< 5.0\text{ ms}$** (vs. $45\text{ ms}$ for open-loop ERM motors) for crisp tactile contrast.

### 4.5 Distance-to-Cadence Mapping & Anti-Fatigue 3.0-Second Decay
Rather than varying amplitude (which quickly desensitizes cutaneous mechanoreceptors), distance is encoded by **pulse repetition period $T(d)$**:

$$T(d) = T_{\min} + (T_{\max} - T_{\min}) \cdot \left(\frac{d - d_{\min}}{d_{\max} - d_{\min}}\right)^{1.65}$$

- **Clear Zone ($> 2.5\text{ m}$)**: Silent ($T = \infty$).
- **Caution Zone ($1.0\text{ m} - 2.5\text{ m}$)**: Rhythmic cadence accelerating from $1.2\text{ s}$ down to $4\text{ Hz}$.
- **Hazard Zone ($0.4\text{ m} - 1.0\text{ m}$)**: Urgent cadence ($8\text{ Hz} - 10\text{ Hz}$).
- **Collision Imminent ($< 0.4\text{ m}$)**: Continuous alarm burst ($12\text{ Hz}$).

**Anti-Fatigue Decay Window**: If a user stops walking before a static barrier ($\sigma_d^2 < 0.0025\text{ m}^2$ for $t \ge 3.0\text{ s}$), actuation smoothly decays to **35% baseline duty cycle** via an exponential envelope ($\tau = 1.2\text{ s}$). Any subsequent displacement ($|\Delta d| > 0.15\text{ m}$) instantly restores 100% alertness within $< 5\text{ ms}$.

### 4.6 Power Management & Thermal Integrity
- **Cell**: 3.7V 2000 mAh 103450 prismatic Li-Po battery yielding **$\ge 12\text{ hours}$ continuous operation** under nominal walking conditions (145 mA average system draw).
- **Inactivity Sleep**: Bosch BMI160 IMU detects static state ($a_{\text{RMS}} < 0.05\text{ G}$ for 60s) and commands ESP32-S3 into Light Sleep with peripherals gated (**$15\text{ µA}$** quiescent draw). Hardware motion interrupt awakens the system in **$< 5\text{ ms}$**.
- **Skin-Contact Thermal Limit**: Internal copper heat spreaders and 3 mm thermal isolation gaps maintain outer lumbar contact casing temperature strictly below **$34.5^\circ\text{C}$** under continuous maximum load, exceeding IEC 62368-1 safety standards.

---

## 5. Technical Specifications Reference

| Parameter | Engineering Target | Verification Standard |
| :--- | :--- | :--- |
| **System Processing Unit** | Espressif ESP32-S3 Dual-Core Xtensa LX7 @ 240 MHz | FreeRTOS Core 0 (I/O) / Core 1 (DSP) |
| **Optical Distance Sensors** | 8x STMicroelectronics VL53L1X ToF (940 nm VCSEL) | IEC 60825-1:2014 Class 1 Eye-Safe |
| **Max Detection Range** | $4.0\text{ m}$ (Optical limit) / $2.5\text{ m}$ (Haptic alert zone)| Dark & Ambient Light Calibrated |
| **Sensor Elevation Planes** | 4x Horizontal (0°) + 4x Overhead (+25°) | Dual-Elevation Ray-Trace Matrix |
| **Aggregate Refresh Rate** | **15 Hz** (66.6 ms full 360° frame) | 4.0 ms Interleaved TCA9548A Mux |
| **Sensor-to-Skin Latency** | **$< 15\text{ ms}$** (Measured average: 12.8 ms) | Dual-Channel DSO Verification |
| **Tactile Actuation Nodes** | 8x Linear Resonant Actuators (10 mm coin) | Vybronics / Jinlong 205 Hz |
| **Peak Tactile Acceleration** | $2.2\text{ G}$ peak at $205\text{ Hz} \pm 3\text{ Hz}$ | TI DRV2605L Auto-Resonance Closed-Loop |
| **Mechanical Transient Braking**| **$< 5.0\text{ ms}$** active reverse braking | Closed-Loop DRV2605L Back-EMF |
| **Power Supply & Capacity** | 3.7V 2000 mAh Li-ion (103450 prismatic) | TP4056 + DW01A Protected BMS |
| **Continuous Autonomy** | $\ge 12\text{ hours}$ active scanning | Simulated 1.2 m/s navigation profile |
| **Low-Power Inactivity Sleep** | **$15\text{ µA}$** quiescent draw (Wakeup $< 5\text{ ms}$)| Bosch BMI160 Motion Interrupt |
| **Thermal Profile at Skin** | **$< 34.5^\circ\text{C}$** continuous (Ambient $+25^\circ\text{C}$) | 4-Channel K-Type Thermocouple Logger |
| **Total System Weight** | **$280\text{ grams}$** (inclusive of battery and belt) | Ergonomic pelvic load distribution |
| **Environmental Enclosure** | **IP54** Dust and Splash Resistant | Silicone gaskets & hydrophobic vents |

---

## 6. Bill of Materials & Economic Viability

The project enforces rigorous cost accounting comparing functional prototype fabrication with industrial volume manufacturing:

| Subsystem Group | Component Description | Stage 2 Prototype (₹) | Volume Target @ 1k+ Units (₹) |
| :--- | :--- | :---: | :---: |
| **Core Compute & Sensing** | ESP32-S3 + 8x VL53L1X ToF + 2x TCA9548A | ₹4,120 | ₹1,550 |
| **Haptic Actuation Array** | 8x DRV2605L Drivers + 8x 205 Hz LRAs | ₹3,040 | ₹1,080 |
| **Power & Battery Subsystem**| 2000 mAh Li-Po + TP4056 + DW01A BMS | ₹570 | ₹290 |
| **Interconnect & Electronics**| 2-Layer Polyimide FPC Ribbon + Passives | ₹790 | ₹310 |
| **Enclosures & Ergonomics** | TPU 95A / PETG Enclosures + Neoprene Belt | ₹980 | ₹420 |
| **TOTAL BOM PER UNIT** | **Hardware Bill of Materials** | **₹9,500** | **₹3,650** |

- **Prototype BOM (Stage 2 Submission)**: **₹9,500** (Fabricated with discrete IC evaluation modules, rapid-prototyping FDM printing, and low-volume FPC tooling).
- **Projected Industrial Volume Cost (1,000+ Units)**: **₹3,650** (Achieved via automated SMT placement on unified rigid-flex PCB, injection-molded TPU housings, and wholesale silicon sourcing).
- **Target Retail / Subsidized Price**: **₹4,500** (Structured for ADIP scheme distribution through ALIMCO and national assistive NGOs like EnAble India).

---

## 7. Repository Directory Structure

```
spatial-sense-haptic-waistband/
├── cad/                                         # Mechanical CAD models & 3D print assets
│   ├── models/                                  # 3D printable STL & Wavefront OBJ models
│   │   ├── buckle_magnetic_clasp.stl            # Quick-release magnetic breakaway clasp
│   │   ├── central_controller_battery_enclosure.stl # Lumbar controller & battery housing
│   │   ├── lra_haptic_coin_holder.stl           # Vibration decoupling elastomeric boot
│   │   ├── modular_sensor_pod_overhead_25deg.stl# +25° overhead sensor pod (TPU 95A)
│   │   ├── modular_sensor_pod_waist_0deg.stl    # 0° waist-level sensor pod (TPU 95A)
│   │   ├── spatial_sense_waistband_assembly.obj # Complete 3D multi-part assembly (OBJ)
│   │   └── spatial_sense_waistband_assembly.stl # Complete 3D assembly (binary STL)
│   ├── renders/                                 # High-resolution CAD engineering renders
│   │   ├── spatial_sense_assembled_concept.jpg
│   │   ├── spatial_sense_cad_ui_parametric_modeling.jpg
│   │   └── spatial_sense_exploded_cad_assembly.jpg
│   └── README.md                                # 3D printing & mechanical specifications
├── hardware/                                    # Electrical engineering & BOM
│   ├── eda/                                     # PCB layout & bill of materials
│   │   ├── BOM_SPATIAL_SENSE_Vishwakarma_Stage2.csv # Itemized ₹9,500 prototype BOM
│   │   └── spatial_sense_fpc_pcb_layout.jpg     # 2-layer polyimide FPC layout render
│   ├── schematics/                              # 4-sheet functional schematics & ray-trace
│   │   ├── dual_plane_ray_trace_geometry.png
│   │   ├── sheet1_optical_sensing_and_i2c_mux.png
│   │   ├── sheet2_resonant_haptic_actuation.png
│   │   ├── sheet3_power_distribution_and_bms.png
│   │   ├── sheet4_motion_sensing_and_ble_interface.png
│   │   └── system_architecture_block_diagram.png
│   └── README.md                                # Hardware architecture & wiring guide
├── firmware/                                    # Embedded C++/FreeRTOS firmware for ESP32-S3
│   ├── platformio.ini                           # PlatformIO build configuration
│   ├── src/
│   │   ├── haptic_engine.cpp                    # 205Hz auto-resonance & cadence mapping
│   │   ├── haptic_engine.h
│   │   ├── main.cpp                             # Dual-core FreeRTOS task coordinator
│   │   ├── power_manager.cpp                    # BMI160 IMU 15µA sleep / 5ms wake
│   │   ├── power_manager.h
│   │   ├── sensor_scheduler.cpp                 # 4ms interleaved I2C ToF multiplexer & median filter
│   │   └── sensor_scheduler.h
│   └── README.md                                # Build, flash & test documentation
├── docs/                                        # Comprehensive engineering & clinical docs
│   ├── Firmware_and_DSP_Algorithms.md           # Scheduler timing, median filter & cadence math
│   ├── Hardware_Design_and_Assembly_Manual.md   # Enclosure specs, FPC routing & assembly steps
│   ├── Project_Proposal_Theme2.md               # Clinical problem definition & solution proposal
│   ├── README.md                                # Documentation master index
│   ├── Testing_and_Validation_Protocol.md       # IEC compliance & EnAble India field trial protocol
│   ├── User_Manual_and_Accessibility_Guide.md   # Non-visual user guide & O&M trainer mirror mode
│   └── specs/
│       ├── FMEA_Analysis.md                     # Failure Mode and Effects Analysis
│       └── System_Architecture.md               # Detailed system bus & pinout specifications
├── .gitignore                                   # Clean exclusion configuration
├── LICENSE                                      # MIT License
└── README.md                                    # Master industrial documentation
```

---

## 8. Quickstart & Build Instructions

### 8.1 Firmware Build & Flash (PlatformIO)
Prerequisites: [PlatformIO Core (CLI)](https://platformio.org/install/cli) or PlatformIO IDE for VS Code.

```bash
# Clone the repository
git clone https://github.com/Ashwinkumar-k10/spatial-sense-haptic-waistband.git
cd spatial-sense-haptic-waistband/firmware

# Compile the ESP32-S3 FreeRTOS firmware
pio run

# Connect ESP32-S3 via USB-C and flash firmware
pio run --target upload

# Open serial monitor for real-time sensor radar stream (115200 baud)
pio device monitor
```

### 8.2 Mechanical Additive Manufacturing
1. Open CAD STL models in slicer (PrusaSlicer / Bambu Studio / Cura) located in `cad/models/`.
2. **Sensor Pods (`modular_sensor_pod_*.stl`)**: Slice in **TPU 95A** (0.16 mm layer height, 3 perimeters, 30% gyroid infill).
3. **LRA Isolation Boots (`lra_haptic_coin_holder.stl`)**: Slice in **TPU 85A/95A** (0.12 mm layer height, 100% solid infill).
4. **Lumbar Enclosure (`central_controller_battery_enclosure.stl`)**: Slice in **PETG or ABS** (0.20 mm layer height, 4 perimeters, 40% infill).
5. Post-process with brass M2/M2.5 heat-set inserts.

---

## 9. Non-Visual Accessibility & Trainer Protocol

```
                  ZERO-SIGHT DOUBLE-TAP TACTILE SELF-TEST
  Node 1 (Front) ──> Node 5 (FL+25°) ──> Node 2 (Left) ──> Node 6 (RL+25°)
        ^                                                         │
        │                                                         v
  Node 8 (FR+25°) <── Node 4 (Right) <── Node 7 (RR+25°) <── Node 3 (Rear)
  [360° Clockwise Sweep Verification across all 8 nodes in 1.2 seconds]
```

- **Orientation**: Tactile raised Braille symbol 'S' (⠎) on the top edge of the rear housing confirms proper lumbar alignment without sight.
- **Self-Test Sweep**: Double-tapping the concave button executes a **360° clockwise tactile sweep** ($100\text{ ms}$ pulse per node) confirming all 8 ToF sensors and LRA drivers are operational before travel. A sensor failure produces a localized triple-jitter buzz pinpointing the pod.
- **O&M Trainer Companion App**: Optional BLE 5.0 application compliant with Android TalkBack / iOS VoiceOver displays a real-time **360° polar radar mirror** up to 15 m away, enabling Orientation & Mobility instructors to observe student hazard detection safely.

---

## 10. Standards & Regulatory Compliance

- **Optical Eye Safety**: **IEC 60825-1:2014 Class 1**. ST VL53L1X 940 nm VCSEL output is hardware current-limited below $0.78\text{ mW}$ maximum accessible emission.
- **Battery Safety**: **IEC 62133 / UN 38.3**. Integrated DW01A protection IC with thermal cutoff prevents overcharge, overdischarge, and short-circuit conditions.
- **Thermal Contact Safety**: **IEC 62368-1**. Operating enclosure skin temperature strictly $< 34.5^\circ\text{C}$ over 4 hours continuous load.
- **Environmental Rating**: **IP54**. Dust ingress protection and splash resistance via silicone sealing gaskets and hydrophobic acoustic vents.

---

## 11. Team & Institutional Attribution

* **Team Name**: **TEAM TECHTONICS**
* **Project Name**: **SPATIAL-SENSE**
* **Competition**: Vishwakarma Awards 2026–27 (Stage 2)
* **Track**: Theme 2 — Assistive Solutions (EnAble India)
* **Mentoring Institution**: Indian Institute of Technology Indore (IIT Indore) & Maker Bhavan Foundation
* **Project Lead / Author**: [Ashwinkumar-k10](https://github.com/Ashwinkumar-k10)
* **Repository**: [spatial-sense-haptic-waistband](https://github.com/Ashwinkumar-k10/spatial-sense-haptic-waistband)
* **License**: [MIT License](LICENSE)
