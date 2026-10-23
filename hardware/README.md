# SPATIAL-SENSE — Electrical Hardware & Schematics

This directory contains the electrical architecture, schematic sheets, flexible printed circuit (FPC) layout, and complete itemized Bill of Materials (BOM) for **SPATIAL-SENSE**.

---

## Schematic Sheets (`/schematics`)

| Sheet Number | Title | Key Components |
|---|---|---|
| **Sheet 1** | *Optical Sensing & I²C Multiplexing* | ESP32-S3 Core 0, TCA9548A 8-channel multiplexer (0x70), 8x ST VL53L1X ToF sensors, XSHUT GPIO lines, Fast-Mode I²C (400 kHz). |
| **Sheet 2** | *Resonant Haptic Actuation Subsystem* | ESP32-S3 Core 1, dedicated I²C Bus 1, 8x TI DRV2605L motor controllers (auto-resonance tracking), 8x 205 Hz coin LRAs, 150 mA hardware current limit. |
| **Sheet 3** | *Power Distribution & BMS Protection* | 3.7V 2500 mAh 1S Li-ion cell (IEC 62133 compliance reference), Seiko hardware BMS (4.25V OVP, 2.8V UVP, 2A OCP), ultra-low-noise 3.3V buck-boost DC-DC, USB-C charge controller. |
| **Sheet 4** | *Motion Sensing & Wireless Interface* | Bosch BMI160 6-DOF IMU (accelerometer + gyroscope), ULP coprocessor interrupt line, 15 µA light sleep / 5 ms fast wake, BLE 5.0 radio stack. |
| **Block Diagram** | *System Architecture* | Unified signal flow diagram covering perception, processing, actuation, power rails, and offline telemetry. |
| **Geometry** | *Dual-Plane Ray-Trace* | Side-view optical geometry illustrating 0° waist plane and +25° head-level protective cone (up to 2.1 m). |

---

## Bill of Materials (`/eda/BOM_SPATIAL_SENSE_Vishwakarma_Stage2.csv`)

| Subsystem Group | Part Designation | Prototype Qty | Estimated Cost (INR) |
|---|---|:---:|:---:|
| **Core Processing & Power** | ESP32-S3-WROOM-1 + BMS + 2500 mAh Li-ion | 1 Set | ₹1,450 |
| **Optical Sensing Array** | ST VL53L1X ToF Sensors + Protective Optics | 8 Units | ₹3,200 |
| **Multiplexed Haptic Drivers** | TI DRV2605L Drivers + TCA9548A Multiplexer PCB | 8 Drivers + Mux | ₹2,100 |
| **Resonant Actuators** | Precision 205 Hz LRA Coin Actuators | 8 Units | ₹1,250 |
| **Harness, Enclosure & Belt** | Modular TPU Pods, Neoprene Belt & Polyimide FPC | 1 Assembly | ₹1,500 |
| **TOTAL FUNCTIONAL PROTOTYPE BOM** | **Source-Stated Prototype Estimate** | — | **₹9,500** |

### Unit Economics & Commercial Projections
- **Volume Manufacturing (1,000+ units)**: Projected to scale down to **₹3,650 per unit** via bulk reel SMT sourcing and injection tooling.
- **Target Retail Price**: **₹4,500**, benchmarked against imported haptic vests (₹1,20,000+) and commercial smart canes (₹4,000–₹6,000).
- **Subsidized Distribution**: Designed for distribution through government assistive schemes (ADIP / ALIMCO) and partnerships with EnAble India.
