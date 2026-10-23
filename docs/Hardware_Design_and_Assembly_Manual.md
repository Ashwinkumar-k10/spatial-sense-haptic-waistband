# SPATIAL-SENSE: Hardware Design & Assembly Manual

### Electro-Mechanical Architecture, Fabrication Guidelines & Assembly Protocol

**Project:** SPATIAL-SENSE (Stage 2 Technical Reference)  
**Track:** Theme 2 — Assistive Solutions, Vishwakarma Awards 2026–27  
**Team:** TEAM TECHTONICS  

---

## 1. Electro-Mechanical Overview

The SPATIAL-SENSE hardware platform distributes optical sensing and vibrotactile actuation uniformly around a human torso while centralizing processing, power regulation, and battery storage in a compact lumbar housing.

```
+---------------------------------------------------------------------------------------+
|                                    REAR HOUSING                                       |
|  - ESP32-S3 Dual-Core MCU (240MHz)        - 3.7V 2000mAh Li-Po Cell (103450)          |
|  - 2x TCA9548A I2C Multiplexers (0x70/0x71)- TP4056 Charger + DW01A/FS8205A BMS      |
|  - Bosch BMI160 6-DoF IMU                 - AP2112K-3.3 Ultra-Low Noise LDO (600mA)   |
|  - Magnetic USB-C Charging Port           - Tactile Power/Self-Test Button            |
+-------------------------------------------+-------------------------------------------+
                                            |
         +----------------------------------+----------------------------------+
         |                                                                     |
         v                                                                     v
  [LEFT BUS FPC]                                                        [RIGHT BUS FPC]
  - 3.3V Power & GND                                                    - 3.3V Power & GND
  - I2C Bus A (Multiplexer 1)                                           - I2C Bus B (Multiplexer 2)
  - 4x Discrete Sensor Pods                                             - 4x Discrete Sensor Pods
    * Pod 5 (FL, +25°): VL53L1X + DRV2605L + LRA                         * Pod 8 (FR, +25°): VL53L1X + DRV2605L + LRA
    * Pod 2 (L, 0°):   VL53L1X + DRV2605L + LRA                         * Pod 4 (R, 0°):   VL53L1X + DRV2605L + LRA
    * Pod 6 (RL, +25°): VL53L1X + DRV2605L + LRA                         * Pod 7 (RR, +25°): VL53L1X + DRV2605L + LRA
    * Pod 1 (F, 0° - Left Split): VL53L1X + DRV + LRA                   * Pod 3 (R, 0° - Rear Split): VL53L1X + DRV + LRA
```

---

## 2. Bill of Materials (BOM) & Key Component Sourcing

Itemized summary of the ₹9,500 Stage 2 functional prototype bill of materials:

| Subsystem | Part Description | Manufacturer / Part # | Qty | Unit Cost (₹) | Total (₹) | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Compute** | ESP32-S3-WROOM-1-N16R8 Dual Core 240MHz | Espressif Systems | 1 | 480 | 480 | Main processing, FreeRTOS, BLE 5.0 |
| **Sensors** | VL53L1X Time-of-Flight Ranging Sensor | STMicroelectronics | 8 | 420 | 3,360 | 940nm VCSEL ranging up to 4.0 m |
| **Multiplexing** | TCA9548A Low-Voltage 8-Ch I2C Switch | Texas Instruments | 2 | 140 | 280 | Sensor & actuator channel separation |
| **Actuation** | 10mm Coin LRA (205Hz, 2.2G peak) | Jinlong / Vybronics | 8 | 185 | 1,480 | Directional tactile stimulus |
| **Haptic Drivers**| DRV2605L Haptic Driver with Auto-Resonance| Texas Instruments | 8 | 195 | 1,560 | Closed-loop LRA resonant tracking |
| **IMU** | BMI160 6-DoF Accelerometer + Gyroscope | Bosch Sensortec | 1 | 240 | 240 | Inactivity sleep & step wake-up |
| **Power & BMS** | TP4056 + DW01A + FS8205A Protected BMS | Microchip / Generic | 1 | 120 | 120 | 1A CC/CV Li-ion charge management |
| **Power Cell** | 3.7V 2000mAh 103450 Li-Po Battery | PKCELL / EEMB | 1 | 450 | 450 | 12-hour continuous runtime |
| **Regulation** | AP2112K-3.3 600mA Low-Dropout Regulator | Diodes Inc. | 2 | 45 | 90 | Clean 3.3V analog/digital rails |
| **Interconnect** | 2-Layer Custom Polyimide FPC Ribbon Harness | JLCPCB / Custom | 2 | 350 | 700 | Flexible waist routing with gold fingers |
| **Enclosures** | 3D Printed TPU 95A Pods & PETG Hub Enclosure| In-house FDM | 10 | 45 | 450 | Ergonomic housings & pod brackets |
| **Textile & Clasp**| Elastic Neoprene Belt + Neodymium Buckle | YKK / Custom | 1 | 290 | 290 | Waistband foundation & magnetic clasp |
| **Hardware** | Brass Heat-Set Inserts, M2 Torx Screws, Gaskets| McMaster / Generic | Lot | — | — | Mechanical fastening & sealing |
| **TOTAL** | **Stage 2 Functional Prototype Bill of Materials** | — | — | — | **₹9,500** | Functional Verification Prototype |

---

## 3. Mechanical CAD & 3D Fabrication Parameters

The CAD suite comprises six modular parametric parts located in `cad/models/`:

### Enclosure Printing Specifications
```
+------------------------------------------------------------------------------------+
| Component                 | Material    | Infill | Layer Height | Wall Thickness    |
+------------------------------------------------------------------------------------+
| modular_sensor_pod_waist   | TPU 95A     | 30%    | 0.16 mm      | 3 perimeters (1.2mm)|
| modular_sensor_pod_overhead| TPU 95A     | 30%    | 0.16 mm      | 3 perimeters (1.2mm)|
| lra_haptic_coin_holder     | TPU 85A/95A | 100%   | 0.12 mm      | Solid elastomer    |
| central_controller_housing | PETG / ABS  | 40%    | 0.20 mm      | 4 perimeters (1.6mm)|
| buckle_magnetic_clasp      | PETG Carbon | 60%    | 0.16 mm      | High-tensile shear |
+------------------------------------------------------------------------------------+
```

### Vibration Isolation Architecture
A common failure mode in multi-point haptic wearables is **parasitic vibrotactile crosstalk**: vibration from one motor traveling through the belt chassis and triggering unintended skin sensations on adjacent sectors.
- **Solution**:
  1. Each LRA is housed inside an independent, high-durometer silicone rubber boot (`lra_haptic_coin_holder.stl`).
  2. The boot is suspended within the TPU outer pod via a **3-point decoupling rib geometry**, isolating vibrational energy from the main belt strap.
  3. The inner contact nub of the LRA extends directly through an aperture in the pod, pressing exclusively against the user's garment or skin with a contact force of $\approx 1.5\text{ N}$.

---

## 4. Flexible Printed Circuit (FPC) & Harness Routing

To ensure high mechanical fatigue life (>50,000 bending cycles around the human waist), wiring is routed via a **2-layer Polyimide Flexible PCB**:

```
                       FPC HARNESS CROSS-SECTION
  +-----------------------------------------------------------------+
  | Top Polyimide Coverlay (25 µm)                                  |
  +-----------------------------------------------------------------+
  | Layer 1: Power & Clock Traces (35 µm Cu, 0.35 mm width)         |
  +-----------------------------------------------------------------+
  | Polyimide Base Dielectric Core (50 µm)                          |
  +-----------------------------------------------------------------+
  | Layer 2: I2C Data & Actuation Lines (35 µm Cu, 0.25 mm width)   |
  +-----------------------------------------------------------------+
  | Bottom Polyimide Coverlay (25 µm)                               |
  +-----------------------------------------------------------------+
```

### Key FPC Design Rules
- **Minimum Bend Radius**: $R_{\text{min}} \ge 5\text{ mm}$ (no 90° sharp corners; all corners routed with 45° chamfers or 3 mm fillets).
- **Strain Relief Stiffeners**: 0.3 mm FR4 stiffeners are laminated beneath each sensor pod landing pad to prevent flex fatigue at solder joints.
- **Impedance & Shielding**: Ground planes sandwich the I2C Fast-Mode lines (`SDA`/`SCL`) to prevent cross-coupling between 400 kHz bus clock transitions and high-amplitude LRA PWM drive pulses.

---

## 5. Power Supply & Thermal Safety Subsystem

The power subsystem is designed for long battery runtime and thermal safety under direct skin contact:

### Circuit Topology
1. **Battery Cell**: Single-cell Li-ion (nominal $3.7\text{ V}$, $2000\text{ mAh}$, 103450 prismatic form factor).
2. **Charging Controller (TP4056)**: Set to $850\text{ mA}$ constant-current charging via a $1.5\text{ k}\Omega$ programming resistor (`R_PROG`). Recharges the battery from $0\%$ to $90\%$ in under 2.5 hours.
3. **BMS Protection IC (DW01A + FS8205A Dual MOSFET)**:
   - Overcharge Cutoff: $4.28\text{ V} \pm 0.05\text{ V}$
   - Overdischarge Cutoff: $2.40\text{ V} \pm 0.1\text{ V}$
   - Overcurrent Limit: $3.0\text{ A}$ instant trip.
4. **Thermal Monitoring (NTC Thermistor)**:
   - $10\text{ k}\Omega$ NTC thermistor positioned directly against the Li-ion cell casing and routed to the TP4056 temperature qualification pin.
   - Disables charging if cell temperature exceeds $+45^\circ\text{C}$ or falls below $0^\circ\text{C}$.
5. **Skin-Contact Temperature Management**:
   - The ESP32-S3 and AP2112K LDO regulators are thermally sinked to an internal 0.5 mm copper heat spreader isolated from the outer user-facing surface by a 3 mm air gap and neoprene insulator pad.
   - Measured skin-facing enclosure temperature remains strictly below **$34.5^\circ\text{C}$** under continuous maximum computational and haptic load (well below the $41.0^\circ\text{C}$ biological comfort threshold defined by IEC 62368-1).

---

## 6. Step-by-Step Assembly Instructions

```
  [Step 1: Board Prep]     [Step 2: Pod Assembly]     [Step 3: Harness Integration]
  Solder ToF & DRV2605L -> Insert into TPU Pods  -> Connect FPC Ribbon Harness
          |                         |                           |
          v                         v                           v
  [Step 4: LRA Dampening]  [Step 5: Rear Hub Mount]   [Step 6: Final IP54 Seal]
  Fit Silicone Dampeners-> Install ESP32-S3 & BMS -> Torque M2 Torx & Verify
```

1. **Step 1: Sub-Assembly of Sensor Pods**:
   - Solder the ST VL53L1X module and TI DRV2605L driver to the pod breakout board.
   - Solder the 10mm LRA motor leads to the DRV2605L differential output terminals (`OUT+`, `OUT-`).
   - Press the LRA into its silicone vibration-dampening boot.
2. **Step 2: Mechanical Pod Housing**:
   - Seat the sensor/driver assembly into the respective 0° or +25° TPU enclosure.
   - Secure the pod backing plate using two M2 × 6mm black oxide Torx screws threaded into brass heat-set inserts.
3. **Step 3: Central Controller Assembly**:
   - Install the ESP32-S3 mainboard, dual TCA9548A multiplexers, and power management board into the central PETG housing (`central_controller_battery_enclosure.stl`).
   - Place the 2000 mAh Li-ion battery into the lower insulated cell bay, applying high-temperature Kapton tape over all battery terminals.
4. **Step 4: FPC Harness Interconnection**:
   - Slide the FPC ribbon harness through the lateral cable glands of the central housing.
   - Insert the FPC gold fingers into the zero-insertion-force (ZIF) connectors on the mainboard and lock the retaining sliders.
5. **Step 5: Belt Webbing Integration**:
   - Thread the 40 mm high-tensile neoprene waistband through the integral belt loops on the rear housing and all 8 sensor pods.
   - Install the front magnetic quick-release buckle (`buckle_magnetic_clasp.stl`).
6. **Step 6: Sealing & Benchtop Verification**:
   - Apply a continuous bead of silicone RTV gasket around the perimeter mating lip of the rear housing lid.
   - Fasten the lid with four M2.5 × 8mm Torx screws.
   - Proceed to Quality Assurance and Benchtop Verification.

---

## 7. Quality Assurance Checklist

- [ ] **Continuity & Short Circuit Test**: Verify $>10\text{ M}\Omega$ resistance between 3.3V rail and GND before battery connection.
- [ ] **I2C Bus Address Scan**: Confirm all 8 VL53L1X sensors respond at default address `0x29` when switched via TCA9548A channels 0–7.
- [ ] **LRA Resonance Calibration**: Verify DRV2605L auto-resonance completes with zero diagnostic error flags; check resonant frequency reads $205\text{ Hz} \pm 3\text{ Hz}$.
- [ ] **Drop & Flex Verification**: Execute 1,000 cycles of dynamic waistband flexing; verify zero communication packet dropouts on Fast-Mode I2C bus.
