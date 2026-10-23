# SPATIAL-SENSE: User Manual & Accessibility Protocol

### Non-Visual Operating Guide and Orientation & Mobility (O&M) Protocol

**Target Users:** Deaf-Blind Individuals, Visually Impaired Users, O&M Specialists, and Assistive Caregivers  
**System:** SPATIAL-SENSE 360° Wearable Haptic-Sonar Waistband  
**Revision:** Stage 2 Production Engineering Reference  

---

## 1. Tactile Anatomy & Orientation Guide

SPATIAL-SENSE is designed from the ground up for **100% blind and deaf-blind tactile operation**. The user can orient, wear, test, and adjust the device entirely through tactile landmarks without visual inspection or audio cues.

```
                      FRONT BUCKLE (Tactile Triangle Arrow ▲ Facing Up)
                                     [QUICK CLASP]
                               /                       \
        [Pod 1: Front 0°]                                 [Pod 5: Front-Left +25°]
                 |                                                 |
        [Pod 8: Front-Right +25°]                         [Pod 2: Left 0°]
                 \                                                 /
        [Pod 4: Right 0°]                                 [Pod 6: Rear-Left +25°]
                 \                                                 /
        [Pod 7: Rear-Right +25°]                          [Pod 3: Rear 0°]
                               \                       /
                                [REAR CONTROLLER HUB]
                          (Raised Braille Dot 'S' ⠎ on Top)
                          (Tactile Concave Power/Test Button)
                          (Reversible Magnetic USB-C Port)
```

### Tactile Identifying Features
1. **Rear Hub Housing**:
   - The central electronics pod features a **raised tactile Braille symbol 'S' (⠎)** molded into the top edge to signify the rear-facing position.
   - The underside of the rear hub has a soft, breathable neoprene contact pad that rests against the lower lumbar spine.
2. **Front Quick-Release Clasp**:
   - The magnetic mechanical buckle features a **recessed tactile arrow (▲)** indicating the "Up" orientation. The two buckle halves snap together effortlessly when aligned within 15 mm.
3. **Sensor Pod Geometry**:
   - **Horizontal (0°) Pods**: Feature flat front faces with smooth vertical grip ridges on both flanks.
   - **Overhead (+25°) Pods**: Feature a distinct, upward-slanted beveled roof ($25^\circ$ slope) that can be immediately identified with the fingertip.

---

## 2. Donning and Fit Adjustment

1. **Step 1: Orient the Waistband**:
   - Hold the rear central housing with the raised Braille dot facing **upwards** and towards your spine.
2. **Step 2: Position on the Iliac Crest**:
   - Position the waistband securely just above your hip bones (iliac crest), aligned with your navel in front.
   - *Crucial*: Ensure the waistband is snug and level around your torso. An unlevel waistband tilts the optical cones downward or excessively upward.
3. **Step 3: Fasten the Magnetic Clasp**:
   - Bring the two front buckle halves together until the internal neodymium magnets snap them into mechanical lock.
   - Pull the lateral elastic nylon cinch straps until the waistband feels firmly anchored to your waist without constricting breathing.
4. **Step 4: Tactile Check of Sensor Clearances**:
   - Lightly glide your fingers along the outer circumference of the 8 pods.
   - Ensure shirts, jackets, or scarves are tucked inside or cleared away from the optical aperture windows.

---

## 3. Non-Visual Operation & Tactile Self-Test

SPATIAL-SENSE features a single **Tactile Concave Button** located on the top ridge of the rear central housing.

```
       +--------------------------------------------------------------+
       |                  TACTILE BUTTON INTERACTION                  |
       +--------------------------------------------------------------+
       | Press & Hold (2 seconds)  --> Power ON (Sequential Thump)    |
       | Double-Tap (within 0.5s)  --> 360° Clockwise Self-Test Sweep |
       | Press & Hold (4 seconds)  --> Power OFF (Descending Rumble)  |
       +--------------------------------------------------------------+
```

### Powering On
- Press and hold the concave button for **2.0 seconds**.
- The device confirms startup by delivering a crisp, high-amplitude **dual-pulse thump** across all 8 haptic nodes simultaneously ($205\text{ Hz}$, $150\text{ ms}$).

### Zero-Sight Hardware Self-Test (Double-Tap)
To verify that all 8 sensors, multiplexers, and haptic drivers are operational before embarking on travel:
- Quickly **double-tap** the concave button.
- The system executes a **clockwise tactile sweep**:
  - Node 1 (Front) vibrates $\to$ Node 5 (Front-Left) $\to$ Node 2 (Left) $\to$ Node 6 (Rear-Left) $\to$ Node 3 (Rear) $\to$ Node 7 (Rear-Right) $\to$ Node 4 (Right) $\to$ Node 8 (Front-Right).
  - Each node pulses for $100\text{ ms}$ with a $50\text{ ms}$ transition.
- **Diagnostics Confirmation**:
  - *All Clear*: Complete 8-node sweep finishes with a synchronized dual confirmation pulse.
  - *Sensor Fault*: If any sensor channel fails I²C acknowledge, its corresponding node delivers a rapid triple-jitter buzz ($40\text{ ms}$ on/off), pinpointing the exact pod requiring inspection.

### Powering Off
- Press and hold the concave button for **4.0 seconds**.
- The device emits a **descending haptic frequency rumble** ($205\text{ Hz} \to 120\text{ Hz}$) before transitioning the ESP32-S3 into deep sleep.

---

## 4. The Haptic Language: Cadence, Direction & Decay

SPATIAL-SENSE communicates obstacle distance and bearing through pure mechanoreceptor vibration against the epidermal skin of the waistline.

### Directional Localization
Vibration is felt precisely at the anatomical location corresponding to the obstacle:
- **Navel (Front)**: Obstacle directly ahead at waist level.
- **Left Hip Bone**: Pedestrian, wall, or vehicle on your left flank.
- **Right Hip Bone**: Barrier or bollard on your right flank.
- **Lower Spine (Rear)**: Person or bicycle approaching from behind.
- **Upper Diagonal Pods (+25°)**: Overhead hazard (tree limb, open shutter, truck bed) in that respective diagonal quadrant.

### Distance-to-Cadence Curve
Vibration amplitude is held at an optimal resonant displacement ($2.2\text{ G}$ peak) while **pulse cadence varies dynamically**:

| Distance Zone | Target Range | Tactile Cadence | Sensation Character | Action Recommended |
| :--- | :--- | :--- | :--- | :--- |
| **Clear Zone** | $> 2.5\text{ m}$ | 0 pulses / sec (Silent) | Zero tactile sensation | Normal uninhibited stride. |
| **Notice Zone** | $1.8\text{ m} - 2.5\text{ m}$ | 1 pulse every $1.2\text{ s}$ | Gentle, slow tapping rhythm | Prepare to navigate around barrier. |
| **Caution Zone**| $1.0\text{ m} - 1.8\text{ m}$ | 3 to 5 pulses / sec ($4\text{ Hz}$) | Distinct, rhythmic pulsing | Slow walking pace; locate with cane. |
| **Hazard Zone** | $0.4\text{ m} - 1.0\text{ m}$ | 8 to 10 pulses / sec ($10\text{ Hz}$)| Urgent rapid vibration | Stop or alter heading immediately. |
| **Critical Collision** | $< 0.4\text{ m}$ | Continuous burst ($12\text{ Hz}$) | Intense, unmistakable buzz | Emergency halt; raise cane/hand guard.|

### Anti-Fatigue 3.0-Second Decay
To prevent tactile sensory adaptation (where skin receptors become numb from prolonged steady stimulation):
- If the user stops walking in front of a counter, wall, or doorway, the obstacle distance remains constant.
- After **3.0 seconds** of static proximity, the firmware reduces vibration duty cycle to **35% of baseline**.
- The user remains conscious of the wall's location without experiencing sensory fatigue or irritation. Moving closer or stepping away immediately restores full dynamic response.

---

## 5. Battery Charging & Power Management

```
               [Central Electronics Housing]
               +---------------------------+
               | (o) Power/Self-Test Button|
               |                           |
               | [====] Magnetic USB-C Port| <--- Snap Magnetic Pogo Cable
               +---------------------------+
```

1. **Reversible Magnetic USB-C Connector**:
   - The charging port utilizes a magnetic break-away coupler. The blind user simply holds the magnetic charging cable near the rear hub connector; it automatically aligns and snaps into place.
   - Reverse polarity protection prevents electrical short-circuiting regardless of cable orientation.
2. **Charging Tactile Status**:
   - *Connecting Charger*: Single long vibration pulse ($500\text{ ms}$) confirms charging initiated.
   - *Full Charge Reached*: Two short pulses confirm $100\%$ charge ($4.2\text{ V}$).
3. **Low-Battery Warning**:
   - When battery capacity drops below $15\%$ (~$3.5\text{ V}$), the device issues a distinct **triple slow vibration** every 5 minutes.
4. **Intelligent Inactivity Auto-Sleep**:
   - If the waistband is placed on a table or hung on a hook, the on-board Bosch BMI160 IMU detects zero acceleration for **60 seconds** and commands the system into ultra-low-power sleep ($15\text{ µA}$).
   - Picking up the waistband instantly awakens the system via IMU any-motion interrupt within **5 milliseconds**.

---

## 6. Companion BLE App & O&M Trainer Mirror Mode

While SPATIAL-SENSE is 100% autonomous and operates offline without any smartphone requirement, an optional BLE companion app is provided for accessibility configuration and O&M trainer guidance.

### Accessibility Standards Compliance
- Built with standard native accessibility hooks, fully compatible with:
  - **Android TalkBack** (Screen Reader & BrailleBack display via BLE).
  - **iOS VoiceOver**.
  - High-contrast visual modes and scalable dynamic type.

### O&M Trainer Mirror Display
- During indoor and outdoor orientation sessions, the O&M trainer can connect to the student's SPATIAL-SENSE unit up to a range of **15 meters**.
- The app displays a **360° Real-Time Polar Radar**:
  - 8 radial vectors display real-time millimeter distances.
  - Color-coded hazard arcs (Green >2.5m, Amber 1.0-2.5m, Red <0.8m).
  - Allows the instructor to evaluate whether the student is correctly perceiving and responding to overhead vs. waist hazards before physical contact occurs.

---

## 7. Cleaning, Maintenance & IP54 Care

- **Enclosure Care**: Wipe the TPU sensor pods and central housing with a damp cloth moistened with mild soap solution or 70% isopropyl alcohol. Do not submerge in water.
- **Optical Lens Windows**: Keep the 8 sensor apertures free of heavy mud or grease. Clean with a soft microfiber cloth or cotton swab.
- **Belt Strap Washing**: The neoprene belt band can be unclipped from the modular electronics and hand-washed in lukewarm water with mild detergent. Air dry thoroughly before reattaching pods.
- **Storage**: Store in a dry environment between $-10^\circ\text{C}$ and $+45^\circ\text{C}$. Avoid storing in direct sunlight on vehicle dashboards.
