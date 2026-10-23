# SPATIAL-SENSE — Embedded Firmware Architecture

This directory contains the production-grade embedded C++/FreeRTOS firmware for the **SPATIAL-SENSE** wearable assistive device running on the **ESP32-S3 dual-core microcontroller** (240 MHz).

---

## Architectural Principles

1. **Deterministic Real-Time Processing**:
   - Replaces opaque, high-latency deep neural networks with deterministic digital signal processing (DSP).
   - Sustains an end-to-end sensor-to-actuation latency **under 15 ms**.
2. **Dual-Core Workload Partitioning**:
   - **Core 0 (`TaskCore0_SensorEngine`)**: Non-blocking Fast-Mode I²C (400 kHz) bus transactions, TCA9548A multiplexer channel selection, interleaved sensor firing schedule, and 3-tap temporal median filtering.
   - **Core 1 (`TaskCore1_HapticEngine`)**: Hard real-time distance-to-cadence mapping, resonant PWM pulse generation, spatial haptic interpolation across adjacent nodes, and anti-fatigue alert decay window.
   - **ULP Coprocessor**: Monitors the Bosch BMI160 6-DOF IMU; places main cores into 15 µA light sleep when stationary and triggers 5 ms rapid wake on step detection.

---

## Crosstalk Mitigation: Interleaved Firing Sequence

Simultaneous laser emission across 8 closely spaced 940 nm Time-of-Flight sensors causes severe optical crosstalk and false distance dropouts. SPATIAL-SENSE implements an interleaved firing schedule with **4 ms phase offsets**:

$$\text{Firing Sequence: } \text{Node } 1 \longrightarrow 5 \longrightarrow 2 \longrightarrow 6 \longrightarrow 3 \longrightarrow 7 \longrightarrow 4 \longrightarrow 8$$

- Opposite radial sensors fire consecutively to maximize angular and spatial separation.
- Total cycle time across all 8 nodes = $8 \times 4\text{ ms} = 32\text{ ms} \approx 66.6\text{ ms}$ complete refresh cycle ($\approx 15\text{ Hz}$ aggregate refresh rate).

---

## Resonant Haptic Cadence & Distance Mapping

- **Resonant Lock**: Actuators operate at their mechanical resonant frequency ($205\text{ Hz} \pm 3\text{ Hz}$) tracked dynamically by the TI DRV2605L to achieve up to 2.2 G peak tactile acceleration with minimal current draw.
- **Cadence Gradient**:
  - Distance $\ge 2.5\text{ m}$: Zero vibration (quiescent).
  - Distance $= 2.5\text{ m}$: Gentle rhythmic pulse every $1.2\text{ s}$ ($0.83\text{ Hz}$).
  - Distance $= 0.4\text{ m}$: Accelerates smoothly into an urgent $12\text{ Hz}$ tactile burst ($83\text{ ms}$ repetition).
- **Anti-Fatigue Alert Decay Window**:
  - Continuous tactile stimulation induces mechanoreceptor desensitization within 45 seconds.
  - If the user pauses before an obstacle, the firmware ramps down vibration intensity to $35\%$ after **3.0 seconds**, preserving tactile sensitivity.

---

## Build & Flash Instructions

### Prerequisites
- [PlatformIO Core](https://platformio.org/) or PlatformIO IDE (VS Code extension).

### Building
```bash
cd firmware
pio run
```

### Flashing via USB-C
```bash
pio run --target upload --upload-port COM_PORT
```

### Serial Monitoring
```bash
pio device monitor --speed 115200
```
