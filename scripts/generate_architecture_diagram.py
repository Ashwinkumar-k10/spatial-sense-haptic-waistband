import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys

sys.stdout.reconfigure(encoding='utf-8')

fig, ax = plt.subplots(figsize=(15, 8.5), dpi=300)
ax.set_facecolor('#F8FAFC')
fig.patch.set_facecolor('#F8FAFC')

# Title & Subtitle inside diagram
ax.text(7.5, 8.1, 'SPATIAL-SENSE: HARDWARE & FIRMWARE SYSTEM ARCHITECTURE', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
ax.text(7.5, 7.75, 'Distributed Optical Sensing (0° & +25°), Deterministic Dual-Core DSP (<15ms Latency) & 360° Tactile Actuation', 
        ha='center', va='center', fontsize=9.5, color='#475569', fontstyle='italic')

# SECTION 1: OPTICAL PERCEPTION (Top-Left)
ax.add_patch(patches.FancyBboxPatch((0.4, 3.8), 3.4, 3.6, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#0284C7', lw=2))
ax.add_patch(patches.FancyBboxPatch((0.4, 7.0), 3.4, 0.4, boxstyle="round,pad=0.05", fc='#0284C7', ec='#0284C7', lw=1))
ax.text(2.1, 7.2, '1. OPTICAL PERCEPTION PATH', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')

ax.text(0.6, 6.7, '4x Horizontal ToF (0° Waist Plane)', fontweight='bold', fontsize=8, color='#0369A1')
ax.text(0.6, 6.4, '• ST VL53L1X (940nm Class-1 Eye Safe)\n• 27° FoV | Front, Rear, Left, Right', fontsize=7, color='#334155')

ax.text(0.6, 5.8, '4x Upward ToF (+25° Head Plane)', fontweight='bold', fontsize=8, color='#D97706')
ax.text(0.6, 5.5, '• F-Left, F-Right, R-Left, R-Right\n• 2.1m Protective Cone for Overhangs', fontsize=7, color='#334155')

ax.text(0.6, 4.9, 'TCA9548A 8-Ch I²C Multiplexer', fontweight='bold', fontsize=8, color='#0F766E')
ax.text(0.6, 4.6, '• Interleaved sequence: 1→5→2→6→3→7→4→8\n• 4 ms phase offsets (zero optical crosstalk)\n• 15 Hz aggregate refresh rate', fontsize=7, color='#334155')
ax.text(0.6, 4.0, '• Fast-Mode I²C Bus (400 kHz)', fontsize=7, color='#0284C7', fontweight='bold')


# SECTION 2: CENTRAL PROCESSING (Top-Center)
ax.add_patch(patches.FancyBboxPatch((4.1, 3.8), 3.9, 3.6, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#1D4ED8', lw=2))
ax.add_patch(patches.FancyBboxPatch((4.1, 7.0), 3.9, 0.4, boxstyle="round,pad=0.05", fc='#1D4ED8', ec='#1D4ED8', lw=1))
ax.text(6.05, 7.2, '2. CENTRAL PROCESSING (ESP32-S3)', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')

ax.text(4.3, 6.7, 'Core 0 — Sensor DSP Engine', fontweight='bold', fontsize=8, color='#1E40AF')
ax.text(4.3, 6.35, '• Non-blocking Fast-Mode I²C polling\n• MUX channel switching & timing sync\n• Median distance filtering & validity check\n• End-to-end processing latency < 15 ms', fontsize=7, color='#334155')

ax.text(4.3, 5.55, 'Core 1 — Haptic Cadence Engine', fontweight='bold', fontsize=8, color='#7C3AED')
ax.text(4.3, 5.2, '• Distance-to-cadence mapping (1.2s to 12Hz)\n• Directional radial node assignment\n• Spatial haptic interpolation between nodes\n• 3-second alert decay window (anti-fatigue)', fontsize=7, color='#334155')

ax.text(4.3, 4.4, 'ULP Coprocessor — Power Control', fontweight='bold', fontsize=8, color='#B91C1C')
ax.text(4.3, 4.05, '• Reads BMI160 6-DOF IMU continuously\n• 15 µA light sleep during stationary states\n• Fast 5 ms wake-up upon step detection', fontsize=7, color='#334155')


# SECTION 3: HAPTIC ACTUATION (Top-Right)
ax.add_patch(patches.FancyBboxPatch((8.3, 3.8), 3.4, 3.6, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#7C3AED', lw=2))
ax.add_patch(patches.FancyBboxPatch((8.3, 7.0), 3.4, 0.4, boxstyle="round,pad=0.05", fc='#7C3AED', ec='#7C3AED', lw=1))
ax.text(10.0, 7.2, '3. HAPTIC ACTUATION PATH', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#FFFFFF')

ax.text(8.5, 6.7, '8x TI DRV2605L Haptic Drivers', fontweight='bold', fontsize=8, color='#5B21B6')
ax.text(8.5, 6.4, '• Independent I²C bus interface\n• Hardware current limit: 150 mA\n• Real-time auto-resonance tracking\n• 5 ms rapid acceleration rise time', fontsize=7, color='#334155')

ax.text(8.5, 5.6, '8x Linear Resonant Actuators (LRAs)', fontweight='bold', fontsize=8, color='#991B1B')
ax.text(8.5, 5.25, '• Resonant frequency: 205 Hz ± 3 Hz\n• Up to 2.2 G peak tactile acceleration\n• Distributed at 45° intervals around waist\n• Crisp tactile transients on abdominal wall', fontsize=7, color='#334155')

ax.text(8.5, 4.4, 'Tactile Perception Mapping', fontweight='bold', fontsize=8, color='#047857')
ax.text(8.5, 4.05, '• Far (2.5m): 1.2s gentle pulse rhythm\n• Near (0.4m): Urgent 12 Hz vibration burst\n• 100% Non-Visual & Non-Auditory Alerts', fontsize=7, color='#334155')


# SECTION 4: POWER & BATTERY (Bottom-Left)
ax.add_patch(patches.FancyBboxPatch((0.4, 1.4), 5.7, 2.1, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#D97706', lw=1.8))
ax.add_patch(patches.FancyBboxPatch((0.4, 3.1), 5.7, 0.4, boxstyle="round,pad=0.05", fc='#D97706', ec='#D97706', lw=1))
ax.text(3.25, 3.3, '4. POWER MANAGEMENT SUBSYSTEM', ha='center', va='center', fontsize=9, fontweight='bold', color='#FFFFFF')

ax.text(0.6, 2.7, '3.7V 2500 mAh Li-ion Cell', fontweight='bold', fontsize=8, color='#92400E')
ax.text(0.6, 2.4, '• IEC 62133 safety compliant reference\n• Hardware BMS: 4.25V OVP, 2.8V UVP, 2A OCP', fontsize=7, color='#334155')

ax.text(3.4, 2.7, 'DC-DC & Regulated Rails', fontweight='bold', fontsize=8, color='#B45309')
ax.text(3.4, 2.4, '• High-efficiency 3.3V low-noise rail\n• USB-C charge port & programming', fontsize=7, color='#334155')

ax.text(0.6, 1.8, 'Thermal Target: < 34.5°C skin contact under continuous 60-min resonance actuation', fontsize=7, color='#1E293B', fontstyle='italic')


# SECTION 5: ACCESSIBILITY & TRAINER PLATFORM (Bottom-Right)
ax.add_patch(patches.FancyBboxPatch((6.4, 1.4), 5.3, 2.1, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#059669', lw=1.8))
ax.add_patch(patches.FancyBboxPatch((6.4, 3.1), 5.3, 0.4, boxstyle="round,pad=0.05", fc='#059669', ec='#059669', lw=1))
ax.text(9.05, 3.3, '5. ACCESSIBLE COMPANION PLATFORM', ha='center', va='center', fontsize=9, fontweight='bold', color='#FFFFFF')

ax.text(6.6, 2.7, 'Offline-First BLE 5.0 Interface', fontweight='bold', fontsize=8, color='#065F46')
ax.text(6.6, 2.4, '• Zero cloud/internet dependency\n• 100% TalkBack & VoiceOver compliant', fontsize=7, color='#334155')

ax.text(9.2, 2.7, 'Deaf-Blind Self-Test', fontweight='bold', fontsize=8, color='#047857')
ax.text(9.2, 2.4, '• Double-tap belt button\n• Clockwise haptic sweep', fontsize=7, color='#334155')

ax.text(6.6, 1.8, 'O&M Trainer Mode: Real-time 360° radar display, obstacle vectors & telemetry mirror', fontsize=7, color='#1E293B', fontstyle='italic')


# SYSTEM WORKING FLOW (Along the very bottom)
flow_steps = [
    ('1. SENSE', '8x ToF LiDARs\nDual Elevation'),
    ('2. SCHEDULE', 'TCA9548A MUX\n4ms Phase Shift'),
    ('3. FILTER', 'Core 0 DSP\nMedian Reject'),
    ('4. LOCALIZE', 'Radial Azimuth\n0° vs +25° Plane'),
    ('5. MAP CADENCE', 'Core 1 Cadence\n205Hz Resonance'),
    ('6. ACTUATE', '8x LRAs Deliver\nTactile Vectors')
]

for idx, (title, sub) in enumerate(flow_steps):
    x = 0.4 + idx * 1.9
    ax.add_patch(patches.FancyBboxPatch((x, 0.2), 1.6, 0.85, boxstyle="round,pad=0.06", fc='#1E293B', ec='#0F172A', lw=1.2))
    ax.text(x + 0.8, 0.75, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#38BDF8')
    ax.text(x + 0.8, 0.45, sub, ha='center', va='center', fontsize=6.5, color='#F8FAFC')
    if idx < len(flow_steps) - 1:
        ax.annotate('', xy=(x + 1.85, 0.62), xytext=(x + 1.62, 0.62), 
                    arrowprops=dict(arrowstyle="->", lw=2, color='#0284C7'))

# Connectors between blocks
# Perception to Processing
ax.annotate('', xy=(4.1, 5.6), xytext=(3.8, 5.6), arrowprops=dict(arrowstyle="->", lw=2.5, color='#0284C7'))
ax.text(3.95, 5.85, 'I²C', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0284C7')

# Processing to Actuation
ax.annotate('', xy=(8.3, 5.6), xytext=(8.0, 5.6), arrowprops=dict(arrowstyle="->", lw=2.5, color='#7C3AED'))
ax.text(8.15, 5.85, 'I²C/PWM', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#7C3AED')

# Processing to Power & Platform
ax.annotate('', xy=(6.05, 3.8), xytext=(6.05, 3.5), arrowprops=dict(arrowstyle="<->", lw=1.5, color='#D97706', ls='--'))
ax.annotate('', xy=(8.5, 3.5), xytext=(8.0, 3.8), arrowprops=dict(arrowstyle="<->", lw=1.5, color='#059669', ls=':'))

# LEGEND (Right-most panel)
ax.add_patch(patches.FancyBboxPatch((12.0, 1.4), 2.6, 6.0, boxstyle="round,pad=0.08", fc='#FFFFFF', ec='#CBD5E1', lw=1.5))
ax.text(13.3, 7.15, 'SYSTEM LEGEND', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0F172A')

legend_items = [
    ('→ Optical Data (I²C 400kHz)', '#0284C7'),
    ('→ Haptic Command / PWM', '#7C3AED'),
    ('→ Power 3.3V / BMS Rail', '#D97706'),
    ('⋯ BLE Wireless Telemetry', '#059669'),
    ('■ Waist-Level Plane (0°)', '#0284C7'),
    ('■ Overhead Plane (+25°)', '#D97706'),
    ('■ Resonant Tactile Node', '#991B1B')
]

for l_idx, (l_txt, l_col) in enumerate(legend_items):
    y_l = 6.6 - l_idx * 0.7
    ax.text(12.2, y_l, l_txt, fontsize=7.5, color=l_col, fontweight='bold')

ax.set_xlim(0, 14.8)
ax.set_ylim(0, 8.5)
ax.axis('off')
plt.tight_layout()
plt.savefig('assets/system_architecture_diagram.png', dpi=300, bbox_inches='tight')
plt.close()
print("Generated assets/system_architecture_diagram.png")
