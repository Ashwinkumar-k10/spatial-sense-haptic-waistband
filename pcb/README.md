# SPATIAL-SENSE — PCB Engineering & Hardware Design

### Mixed-Signal Wearable Controller & Power Management Hardware

**Project Identifier:** `SPATIAL-SENSE — Prototype PCB Design`  
**Competition:** Vishwakarma Awards 2026–27 (Theme 2: Assistive Solutions, EnAble India, IIT Indore)  
**Team:** TEAM TECHTONICS  
**EDA Suite:** KiCad 10.0.7 / Windows 11  

---

## Overview

This directory contains the electrical architecture validation, KiCad schematics, PCB layout, manufacturing outputs, and design-rule verification reports for the **SPATIAL-SENSE central controller PCB**.

The PCB is an ultra-compact, 4-layer mixed-signal board that integrates:
- **Espressif ESP32-S3-WROOM-1** dual-core microcontroller (240 MHz).
- **Dual Texas Instruments TCA9548A** I²C bus multiplexers providing hard electrical isolation between optical perception and haptic actuation.
- **Bosch Sensortec BMI160** 6-DoF inertial measurement unit for motion-triggered autonomous sleep and wake-up.
- **Eight Texas Instruments DRV2605L** haptic driver ICs with closed-loop back-EMF auto-resonance tracking (205 Hz).
- **Comprehensive Lithium Power Subsystem**: Microchip MCP73831T CC/CV autonomous charger, DW01A/FS8205A hardware BMS protection, P-MOSFET automatic load-sharing circuit, and dual TI TLV75733P 1.0 A low-dropout regulators (`+3V3_DIGITAL` & `+3V3_HAPTIC`).
- **Standardized Interconnects**: 8x JST-SH 4-pin optical sensor headers, 8x JST-SH 2-pin LRA motor drive headers, 1x JST-PH 2-pin battery header, and 16-pin USB Type-C receptacle.

---

## Engineering Documentation

1. [**Component & Architecture Validation Report (Stage A & B)**](Component_and_Architecture_Validation_Report.md)  
   Comprehensive datasheet verification table, I²C addressing conflict resolution, ESP32-S3 pin mapping, worst-case power consumption and thermal calculations, load-sharing schematic analysis, and distinction between verified design elements vs. pending physical tests.

---

## Design Stages Workflow

* **[x] Stage A — Validate Architecture & Components**: Complete component validation table, datasheet verification, and IC vs module selection.
* **[x] Stage B — Resolve I²C Addressing, Pin Mapping & Power**: Dual TCA9548A bus topology (`0x70` & `0x71`), strapping pin isolation, power-path circuit, and connector pinouts.
* **[ ] Stage C — Generate & Validate KiCad Schematic**: 6-sheet hierarchical schematic in native KiCad format.
* **[ ] Stage D — Assign Footprints & Produce PCB Layout**: 4-layer stackup ($65 \times 48\text{ mm}$), thermal relief, and controlled-impedance routing.
* **[ ] Stage E — Run ERC / DRC Verification**: Automated rules verification via `kicad-cli 10.0.7`.
* **[ ] Stage F — Manufacturing Deliverables**: Schematic PDF, BOM CSV, netlists, Gerber, and drill files.
