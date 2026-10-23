# SPATIAL-SENSE — 3D Mechanical CAD & Enclosure Design

This directory contains the 3D computer-aided design (CAD) models, exploded assembly geometry, and ergonomic packaging specifications for **SPATIAL-SENSE**: a 360° wearable haptic-sonar waistband designed for upper-torso and head-level collision protection in deaf-blind mobility.

---

## 3D Models (`/models`)

| File Name | Format | Description | Target Material |
|---|---|---|---|
| `spatial_sense_waistband_assembly.stl` | Binary STL | Complete 3D wearable assembly including contoured belt, 8 radial pods, and central rear housing. | Assembly Reference |
| `spatial_sense_waistband_assembly.obj` | Wavefront OBJ | Textured 3D mesh model with vertex normals and multi-part hierarchy. | 3D Visualization / Web |
| `modular_sensor_pod_waist_0deg.stl` | Binary STL | Parametric pod shell with 0° horizontal aperture, internal LRA cavity, and silicone isolation ring. | TPU 95A / SLS Nylon |
| `modular_sensor_pod_overhead_25deg.stl` | Binary STL | Parametric pod shell with +25° tilted upward optical cone protecting head level up to 2.1 m. | TPU 95A / SLS Nylon |
| `central_controller_battery_enclosure.stl` | Binary STL | Ergonomic curved rear housing for ESP32-S3, 2500 mAh Li-ion cell, hardware BMS, and USB-C port. | Polycarbonate-ABS Blend |
| `lra_haptic_coin_holder.stl` | Binary STL | Snap-fit vibration motor bracket providing mechanical coupling to skin while isolating optics. | Silicone 40A / TPU |
| `buckle_magnetic_clasp.stl` | Binary STL | Quick-release magnetic breakaway clasp for one-handed and zero-sight tactile donning. | Anodized Aluminum / PA12 |

---

## Fabrication & 3D Printing Recommendations

- **Modular Pods (Waist & Overhead)**:
  - **Material**: Thermoplastic Polyurethane (TPU 95A) or Selective Laser Sintered (SLS) Nylon PA12.
  - **Infill**: 100% solid infill around optical lens mount to prevent infrared light bleed.
  - **Layer Height**: 0.12 mm – 0.16 mm for precision sensor snap-fits.
  - **Gaskets**: Internal 1.0 mm food-grade silicone O-ring to achieve IP54 dust and water splash resistance.
- **Central Electronics Enclosure**:
  - **Material**: Injection-molded PC-ABS or high-temperature SLA resin.
  - **Wall Thickness**: Nominal 2.2 mm with internal structural ribs for impact protection.
  - **Thermal Performance**: Tested skin-facing surface temperature target below 34.5°C during continuous actuation.
- **Belt Harness**:
  - **Fabric**: 3.0 mm breathable perforated neoprene with soft-touch inner microfiber lining.
  - **Adjustment Range**: 26 inches (66 cm) to 44 inches (112 cm) waist circumferences.
  - **Total System Weight**: Under 320 grams (distributed evenly around the waist perimeter).

---

## Renders & Visualizations (`/renders`)

- `spatial_sense_exploded_cad_assembly.jpg`: Layered exploded assembly render showing belt, pods, sensors, LRAs, and FPC harness.
- `spatial_sense_assembled_concept.jpg`: Full product concept render of the waistband fitted around a user's torso.
- `spatial_sense_cad_ui_parametric_modeling.jpg`: Parametric CAD software UI showing feature tree, sketches, and toolpaths.
