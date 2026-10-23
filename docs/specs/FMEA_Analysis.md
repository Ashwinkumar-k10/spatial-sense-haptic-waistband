# SPATIAL-SENSE — Failure Mode and Effects Analysis (FMEA)

## Vishwakarma Awards 2026–27 | Team TECHTONICS
**Theme 2: Assistive Solutions (EnAble India), IIT Indore**

---

### Failure Modes, Effects & Mitigation Matrix

| Failure Mode | Potential Hazard / Effect | Severity (1-10) | Root Cause | Proposed Fail-Safe / Mitigation Strategy | Detection / Verification |
|---|---|:---:|---|---|---|
| **Optical Sensor Crosstalk** | False obstacle alerts or missed hazards leading to hesitation or collision. | 7 | Concurrent 940 nm laser firing across adjacent ToF sensors. | Deterministic interleaved firing sequence (`1->5->2->6->3->7->4->8`) with 4 ms phase offsets. Temporal 3-tap median filter. | Benchtop rig achieving 15 Hz aggregate rate with zero false dropouts across varied materials. |
| **Optical Lens Contamination / Dirt** | Reduced detection sensitivity in a specific angular sector without user awareness. | 8 | Environmental dust, sweat, or physical smudging on sensor apertures. | Per-channel signal-to-noise ratio (SNR) monitoring; consecutive dropout detection triggers accessible non-visual fault pulse. | Startup optical diagnostics and ambient photon baseline evaluation. |
| **Incorrect Directional Mapping** | Misleading tactile direction communicated, prompting user to veer toward hazard. | 9 | Firmware azimuth misalignment or sensor-to-actuator channel mismatch. | Strict immutable radial mapping table in flash; factory calibration verification; real-time O&M trainer radar mirror checks. | Multi-direction obstacle test track with blindfolded volunteer trials. |
| **Haptic Actuator / Driver Failure** | Hazard detected optically but warning not perceived physically by user. | 9 | Mechanical disconnection of LRA or DRV2605L driver IC stall. | Automatic startup self-test (clockwise tactile sweep); DRV2605L fault register monitoring; adjacent-node fallback alerting. | Power-on self-test (POST) and tactile verification button double-tap. |
| **Battery Depletion / Cutoff** | Sudden loss of collision protection while navigating unfamiliar outdoor areas. | 8 | Undetected battery discharge below cutoff threshold. | Early 15% low-battery warning via distinctive triple-pulse tactile cadence; power-saving light sleep; graceful shutdown at 2.8 V. | ADC voltage divider monitoring with hardware BMS cutoff. |
| **Microcontroller Firmware Stall** | Frozen sensor readings or locked continuous vibration causing confusion. | 9 | FreeRTOS task deadlock or I²C bus lockup. | Hardware Watchdog Timer (WDT) with auto-reset; I²C bus timeout clear routines; normally-quiescent actuator fail-safe. | Benchtop fault-injection stress testing over 48 hours. |
| **Actuator Overheating on Skin** | Thermal discomfort or skin tissue irritation under prolonged warning bursts. | 6 | Continuous resonant operation in confined wearable space. | Skin-facing thermal dissipation target <34.5°C; internal silicone thermal isolation; driver current limited to 150 mA. | Thermocouple profiling under continuous 100% duty cycle for 60 minutes. |
