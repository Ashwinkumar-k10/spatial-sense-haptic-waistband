# SPATIAL-SENSE

### A 360° Wearable Haptic-Sonar Waistband for Upper-Torso and Head-Level Collision Protection in Deaf-Blind Mobility

[![Vishwakarma Awards 2026-27](https://img.shields.io/badge/Competition-Vishwakarma%20Awards%202026--27-blue.svg)](https://vishwakarmaawards.in)
[![Track](https://img.shields.io/badge/Theme%202-Assistive%20Solutions%20(EnAble%20India)-green.svg)]()
[![Institution](https://img.shields.io/badge/IIT%20Indore-Mentorship-orange.svg)]()
[![Team](https://img.shields.io/badge/Team-TECHTONICS-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

---

## Executive Summary

**SPATIAL-SENSE** is an ergonomic, hands-free wearable assistive device engineered to solve a critical, life-threatening mobility barrier for over **450,000 deaf-blind individuals in India**: the inability of standard ground-sweeping white canes to detect hazards situated above the ground plane.

While conventional white canes reliably detect curbs, steps, and terrain drop-offs, their physical sweep angle leaves the user's upper torso and cranium completely exposed to overhead tree branches, commercial shop awnings, open casement windows, and projecting truck cargo beds. Acoustic smart canes fail for this demographic due to severe sensorineural hearing loss.

**SPATIAL-SENSE** acts as a solid-state **360° tactile radar**. It combines dual-elevation optical Time-of-Flight (ToF) sensing (waist-level 0° and overhead +25°) with localized resonant vibrotactile pressure gradients delivered across eight haptic nodes around the user's waist—operating with **zero auditory or visual dependency**.

---

## Key Engineering Innovations

1. **Dual-Elevation Spatial Sensing Geometry**:
   - **Waist-Level Plane (0°)**: 4 sensors (Front, Rear, Left, Right) scan parallel to the ground for walls, pedestrians, and waist-height obstacles.
   - **Overhead Plane (+25°)**: 4 alternating sensors (Front-Left, Front-Right, Rear-Left, Rear-Right) project a protective cone from chest level up to 2.1 m height to detect overhead tree limbs, awnings, and signboards.
2. **Deterministic Interleaved Crosstalk Mitigation**:
   - Executes an interleaved firing sequence (`1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4 -> 8`) with **4 ms phase offsets** via a TCA9548A multiplexer.
   - Eliminates multi-emitter laser crosstalk while sustaining a **15 Hz aggregate refresh rate**.
3. **Hard Real-Time Dual-Core DSP (<15 ms Latency)**:
   - ESP32-S3 dual-core microcontroller running FreeRTOS.
   - Core 0 executes non-blocking Fast-Mode I²C (400 kHz) sensor polling and median distance filtering.
   - Core 1 handles distance-to-cadence mapping and spatial haptic interpolation without latency-heavy neural networks.
4. **Resonant Tactile Actuation (205 Hz ± 3 Hz)**:
   - 8x Linear Resonant Actuators (LRAs) driven by TI DRV2605L motor controllers with real-time back-EMF auto-resonance tracking.
   - Generates crisp 5 ms transient braking and up to **2.2 G peak tactile acceleration** with a 150 mA hardware current limit.
5. **Distance-to-Cadence Proximity Mapping & Anti-Fatigue Decay**:
   - Proximity translates to pulse repetition cadence: a gentle 1.2 s pulse at 2.5 m accelerating smoothly to an urgent 12 Hz tactile burst at 0.4 m.
   - **Anti-Fatigue Decay Window**: If the user pauses before an obstacle, pulse intensity gracefully decays to 35% after **3.0 seconds**, preventing mechanoreceptor desensitization.
6. **Inclusive Non-Visual Accessibility**:
   - Zero-sight hardware self-test: double-tapping the physical belt button triggers a clockwise haptic verification sweep across all eight nodes.
   - Offline-first BLE 5.0 companion application compliant with TalkBack and VoiceOver, plus a 360° real-time graphical radar mirror for Orientation and Mobility (O&M) trainers.

---

## Repository Directory Tree

```
SPATIAL-SENSE/
├── cad/                                    # Mechanical CAD models, enclosures & 3D print assets
│   ├── models/                             # Printable 3D models (STL & OBJ)
│   │   ├── spatial_sense_waistband_assembly.stl     # Full wearable waistband 3D assembly
│   │   ├── spatial_sense_waistband_assembly.obj     # Multi-part Wavefront OBJ 3D model
│   │   ├── modular_sensor_pod_waist_0deg.stl        # 0° waist-level sensor pod (TPU)
│   │   ├── modular_sensor_pod_overhead_25deg.stl    # +25° overhead sensor pod (TPU)
│   │   ├── central_controller_battery_enclosure.stl # Rear electronics & battery housing
│   │   ├── lra_haptic_coin_holder.stl               # LRA motor mount with acoustic dampening
│   │   └── buckle_magnetic_clasp.stl                # Quick-release breakaway belt clasp
│   ├── renders/                            # High-resolution CAD visualization renders
│   │   ├── spatial_sense_exploded_cad_assembly.jpg
│   │   ├── spatial_sense_assembled_concept.jpg
│   │   └── spatial_sense_cad_ui_parametric_modeling.jpg
│   └── README.md                           # 3D printing & mechanical specifications
├── hardware/                               # Electrical engineering, schematics & BOM
│   ├── schematics/                         # 4-sheet functional electrical schematics
│   │   ├── sheet1_optical_sensing_and_i2c_mux.png
│   │   ├── sheet2_resonant_haptic_actuation.png
│   │   ├── sheet3_power_distribution_and_bms.png
│   │   ├── sheet4_motion_sensing_and_ble_interface.png
│   │   ├── system_architecture_block_diagram.png
│   │   └── dual_plane_ray_trace_geometry.png
│   ├── eda/                                # PCB layouts & bill of materials
│   │   ├── spatial_sense_fpc_pcb_layout.jpg         # 2-layer polyimide FPC layout
│   │   └── BOM_SPATIAL_SENSE_Vishwakarma_Stage2.csv # Itemized ₹9,500 prototype BOM
│   └── README.md                           # Hardware architecture & wiring documentation
├── firmware/                               # Embedded C++/FreeRTOS firmware for ESP32-S3
│   ├── src/
│   │   ├── main.cpp                        # Dual-core FreeRTOS task coordinator
│   │   ├── sensor_scheduler.h              # Interleaved multiplexer scheduler header
│   │   ├── sensor_scheduler.cpp            # Fast-Mode I2C & median filter implementation
│   │   ├── haptic_engine.h                 # 205Hz auto-resonance driver header
│   │   ├── haptic_engine.cpp               # Distance-to-cadence & decay implementation
│   │   ├── power_manager.h                 # BMI160 IMU motion detection header
│   │   └── power_manager.cpp               # 15uA light sleep & 5ms wake implementation
│   ├── platformio.ini                      # PlatformIO build configuration
│   └── README.md                           # Build, flash & test instructions
├── docs/                                   # Stage 2 presentation deck & technical specifications
│   ├── presentation/
│   │   ├── SPATIAL_SENSE_Theme2_Vishwakarma_2026_27.pptx # Editable 14-slide presentation
│   │   ├── SPATIAL_SENSE_Theme2_Presentation.pdf          # High-resolution PDF export
│   │   └── slides/                         # 14 rendered slide PNG images (1920x1080)
│   ├── specs/
│   │   ├── System_Architecture.md          # Comprehensive hardware/firmware specification
│   │   └── FMEA_Analysis.md                # Failure Mode and Effects Analysis
│   └── README.md
├── .gitignore
├── LICENSE                                 # MIT License
└── README.md                               # Project documentation master
```

---

## Bill of Materials & Unit Economics

| Subsystem Group | Part Designation | Prototype Qty | Estimated Cost (INR) |
|---|---|:---:|:---:|
| **Core Processing & Power** | ESP32-S3-WROOM-1 + BMS + 2500 mAh Li-ion | 1 Set | ₹1,450 |
| **Optical Sensing Array** | ST VL53L1X ToF Sensors + Protective Optics | 8 Units | ₹3,200 |
| **Multiplexed Haptic Drivers** | TI DRV2605L Drivers + TCA9548A Multiplexer PCB | 8 Drivers + Mux | ₹2,100 |
| **Resonant Actuators** | Precision 205 Hz LRA Coin Actuators | 8 Units | ₹1,250 |
| **Harness, Enclosure & Belt** | Modular TPU Pods, Neoprene Belt & Polyimide FPC | 1 Assembly | ₹1,500 |
| **TOTAL FUNCTIONAL PROTOTYPE BOM** | **Source-Stated Prototype Estimate** | — | **₹9,500** |

- **Commercial Volume Manufacturing**: Projected at **₹3,650 per unit** (1,000+ units) via automated SMT assembly, reel sourcing, and injection tooling.
- **Target Retail Price**: **₹4,500**, providing an affordable, accessible solution compared to imported haptic vests (₹1,20,000+) and handheld smart canes (₹4,000–₹6,000).
- **Subsidized Distribution**: Tailored for integration into the Assistance to Disabled Persons for Purchase/Fitting of Aids and Appliances (ADIP) scheme and ALIMCO.

---

## Implementation Roadmap (6 Months)

- **Phase 1 (Months 1–2) — Benchtop Validation & Crosstalk Quantification**:
  - Breadboard integration of 8x ToF sensors + TCA9548A mux.
  - Optical surface bench tests (wood, glass, cloth) and interleaved timing calibration.
  - *Deliverable*: Benchtop rig sustaining 15 Hz aggregate refresh with zero false dropouts.
- **Phase 2 (Months 3–4) — Custom Flex-PCB & Ergonomic Pod Enclosure**:
  - Fabricate 2-layer polyimide flexible printed circuit (FPC) harness.
  - Tooling of modular IP54 silicone-lined TPU pods; tune LRA resonance (205 Hz).
  - *Deliverable*: Populated wearable flex-belt prototype with thermal profile <34.5°C.
- **Phase 3 (Month 5) — Firmware Refinement & BLE Companion App**:
  - Implement distance-to-cadence mapping, spatial haptic interpolation, and TalkBack/VoiceOver BLE telemetry.
  - *Deliverable*: Feature-complete wearable belt; mobile app passing Google Accessibility Scanner.
- **Phase 4 (Month 6) — Pilot User Trials & EnAble India Validation**:
  - Structured indoor/outdoor obstacle navigation trials with blindfolded volunteers and institutional beta testers.
  - *Deliverable*: Formal pilot trial evaluation report documenting head-strike avoidance and transit speed improvements.

---

## Presentation Deck

The official 14-slide Stage 2 competition submission deck matching the visual design language of Theme 7 is located at:
- PowerPoint: [`docs/presentation/SPATIAL_SENSE_Theme2_Vishwakarma_2026_27.pptx`](docs/presentation/SPATIAL_SENSE_Theme2_Vishwakarma_2026_27.pptx)
- PDF Export: [`docs/presentation/SPATIAL_SENSE_Theme2_Presentation.pdf`](docs/presentation/SPATIAL_SENSE_Theme2_Presentation.pdf)
- Slide Previews: [`docs/presentation/slides/`](docs/presentation/slides/)

---

## Team & Institutional Attribution

- **Team Name**: TEAM TECHTONICS
- **Project Title**: SPATIAL-SENSE
- **Competition**: Vishwakarma Awards 2026–27 (Stage 2)
- **Theme**: Theme 2 — Assistive Solutions (EnAble India), IIT Indore
- **Mentor Institution**: Indian Institute of Technology Indore (IIT Indore) & EnAble India
- **Author / Lead**: [Ashwinkumar-k10](https://github.com/Ashwinkumar-k10)
