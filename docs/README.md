# SPATIAL-SENSE Technical Documentation Suite

### Engineering Specifications, Accessibility Guidelines & Clinical Validation Manuals

**Project:** SPATIAL-SENSE: A 360° Wearable Haptic-Sonar Waistband for Upper-Torso and Head-Level Collision Protection in Deaf-Blind Mobility  
**Competition:** Vishwakarma Awards 2026–27  
**Track:** Theme 2 — Assistive Solutions (EnAble India), IIT Indore  
**Team:** TEAM TECHTONICS  

---

## Documentation Index

This directory contains the complete technical engineering, mechanical fabrication, accessibility, and validation documentation for the SPATIAL-SENSE Stage 2 submission.

### 1. [Project Proposal & Problem Analysis](file:///a:/Projects/Vishwakarma%20awards/docs/Project_Proposal_Theme2.md)
- **File:** `docs/Project_Proposal_Theme2.md`
- **Scope:** Detailed epidemiological problem definition (450,000 deaf-blind individuals in India), white cane ground-sweep blindspots, overhead collision risks, proposed technical solution, dual-elevation innovation, target population, and multi-tier economic cost breakdown (₹9,500 prototype BOM vs ₹3,650 volume manufacturing target).

### 2. [User Manual & Accessibility Protocol](file:///a:/Projects/Vishwakarma%20awards/docs/User_Manual_and_Accessibility_Guide.md)
- **File:** `docs/User_Manual_and_Accessibility_Guide.md`
- **Scope:** Complete non-visual operating guide. Tactile orientation features, raised Braille markers, double-tap non-visual hardware self-test sweep, wearing and fit guidelines, distance-to-cadence haptic vocabulary, magnetic USB-C charging, TalkBack/VoiceOver companion app operation, and O&M trainer 360° radar mirror display.

### 3. [Hardware Design & Assembly Manual](file:///a:/Projects/Vishwakarma%20awards/docs/Hardware_Design_and_Assembly_Manual.md)
- **File:** `docs/Hardware_Design_and_Assembly_Manual.md`
- **Scope:** Mechanical CAD fabrication parameters (TPU 95A / PETG 3D printing), 2-layer polyimide FPC ribbon harness routing, mechanical vibration decoupling ribs for LRA motors, TP4056/BMS power regulation, thermal isolation (<34.5°C skin safety), step-by-step assembly procedure, and quality assurance checklists.

### 4. [Firmware Architecture & DSP Algorithms](file:///a:/Projects/Vishwakarma%20awards/docs/Firmware_and_DSP_Algorithms.md)
- **File:** `docs/Firmware_and_DSP_Algorithms.md`
- **Scope:** FreeRTOS dual-core task scheduling (Core 0 I/O vs Core 1 DSP), interleaved round-robin multiplexer firing timing with 4.0 ms phase offsets, 3-tap temporal median filtering mathematical formulation, distance-to-cadence exponential compression equation, anti-fatigue 3.0-second decay model, closed-loop auto-resonance tracking (205 Hz), and IMU motion-sleep state machine.

### 5. [Testing & Clinical Validation Protocol](file:///a:/Projects/Vishwakarma%20awards/docs/Testing_and_Validation_Protocol.md)
- **File:** `docs/Testing_and_Validation_Protocol.md`
- **Scope:** Laboratory verification standards (IEC 60825-1:2014 Class 1 laser eye safety, IEC 62368-1 thermal limits, IP54 dust/water testing), optical crosstalk quantification, <15 ms latency benchtop oscilloscopy, and a 50-meter dual-elevation obstacle course mobility trial protocol in collaboration with EnAble India.

### 6. [System Architecture Specification](file:///a:/Projects/Vishwakarma%20awards/docs/specs/System_Architecture.md)
- **File:** `docs/specs/System_Architecture.md`
- **Scope:** Technical component interconnects, bus speeds (400 kHz Fast-Mode I²C), pin assignments, and power tree parameters.

### 7. [Failure Mode and Effects Analysis (FMEA)](file:///a:/Projects/Vishwakarma%20awards/docs/specs/FMEA_Analysis.md)
- **File:** `docs/specs/FMEA_Analysis.md`
- **Scope:** Comprehensive FMEA risk matrix covering optical obstruction, battery exhaustion, skin chafing, tactile desensitization, and bus lockups with deterministic hardware/firmware mitigations.
