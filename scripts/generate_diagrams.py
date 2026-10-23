import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs("assets", exist_ok=True)

# Set global styles
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. DUAL PLANE RAY-TRACE GEOMETRY
def create_dual_plane_geometry():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#F8FAFC')

    # Ground plane
    ax.plot([-1, 4.5], [0, 0], color='#64748B', lw=3)
    ax.text(3.5, 0.08, 'Ground Level (0.0 m)', color='#475569', fontsize=9, fontweight='bold')

    # Human silhouette schematic
    # Head, torso, legs
    ax.add_patch(patches.Circle((0, 1.7), 0.12, facecolor='#1E293B', edgecolor='#0F172A', lw=1.5))
    ax.plot([0, 0], [1.58, 0.95], color='#1E293B', lw=8, solid_capstyle='round') # Torso
    ax.plot([0, -0.15], [0.95, 0], color='#1E293B', lw=5, solid_capstyle='round') # Leg 1
    ax.plot([0, 0.15], [0.95, 0], color='#1E293B', lw=5, solid_capstyle='round') # Leg 2

    # Waistband position
    ax.add_patch(patches.Rectangle((-0.12, 0.92), 0.24, 0.12, facecolor='#0284C7', edgecolor='#0369A1', lw=2, zorder=5))
    ax.text(-0.15, 1.1, 'SPATIAL-SENSE\nWaistband (1.0 m)', color='#0369A1', fontsize=9, fontweight='bold', ha='right')

    # Horizontal plane beam (0 deg)
    ax.plot([0.1, 4.0], [0.98, 0.98], color='#0284C7', lw=2.5, ls='--')
    ax.fill_between([0.1, 4.0], [0.98, 0.98 - 0.9], [0.98, 0.98 + 0.9], color='#0284C7', alpha=0.1)
    ax.text(2.5, 0.82, '0° Waist-Level Optical Plane\n(Walls, pedestrians, waist obstacles)', color='#0369A1', fontsize=8.5, fontweight='bold')

    # Upward tilted plane beam (+25 deg)
    x_end = 3.5
    y_end = 0.98 + x_end * np.tan(np.radians(25))
    ax.plot([0.1, x_end], [0.98, y_end], color='#D97706', lw=2.5, ls='--')
    ax.fill_between([0.1, x_end], [0.98, y_end - 0.7], [0.98, y_end + 0.7], color='#D97706', alpha=0.12)
    ax.text(2.1, 2.15, '+25° Upward Optical Plane (2.1 m Protective Cone)\n(Tree limbs, store awnings, open windows)', color='#B45309', fontsize=8.5, fontweight='bold')

    # Overhead Hazard (Awning / Branch)
    ax.add_patch(patches.Rectangle((2.8, 1.45), 1.2, 0.25, facecolor='#EF4444', edgecolor='#B91C1C', lw=1.5, hatch='//'))
    ax.text(3.4, 1.8, 'HAZARD: Iron Awning / Branch\n(Height: 1.45 m – 1.8 m)', color='#B91C1C', fontsize=9, fontweight='bold', ha='center')

    # Cane path (ground only)
    ax.plot([0.05, 1.3], [1.0, 0.05], color='#94A3B8', lw=2.5, ls=':')
    ax.plot([1.3, 1.6], [0.05, 0.05], color='#DC2626', lw=3)
    ax.text(0.8, 0.35, 'Standard Cane Sweep Path\n(Ground obstacles only - MISSED!)', color='#64748B', fontsize=8, fontstyle='italic')

    ax.set_xlim(-0.8, 4.3)
    ax.set_ylim(-0.1, 2.6)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('SPATIAL-SENSE: Dual-Elevation Ray-Trace Geometry (0° & +25° Planes)', fontsize=12, fontweight='bold', pad=10, color='#0F172A')
    plt.tight_layout()
    plt.savefig('assets/dual_plane_geometry.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated assets/dual_plane_geometry.png")

# 2. ELECTRICAL SCHEMATICS (4 SHEETS IN ONE COMBO OR SEPARATE)
def create_schematic_sheets():
    # Sheet 1: Optical Sensing & I2C Multiplexing
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    # ESP32-S3 block
    ax.add_patch(patches.FancyBboxPatch((0.5, 3.0), 2.2, 3.5, boxstyle="round,pad=0.1", fc='#EFF6FF', ec='#1D4ED8', lw=2))
    ax.text(1.6, 6.1, 'ESP32-S3 MCU\n(Dual Core @ 240MHz)', ha='center', va='center', fontweight='bold', color='#1E3A8A', fontsize=10)
    ax.text(1.6, 5.2, 'Core 0: Sensor DSP\nFast-Mode I2C (400kHz)\nInterleaved Scheduler\n(4 ms Phase Offsets)', ha='center', va='center', color='#1E40AF', fontsize=8)
    ax.text(1.6, 3.8, 'GPIO 1/2: SDA/SCL\nGPIO 4-11: XSHUT [0..7]\nGPIO 12: MUX_RST', ha='center', va='center', color='#3B82F6', fontsize=7.5, fontfamily='monospace')

    # TCA9548A MUX block
    ax.add_patch(patches.FancyBboxPatch((3.8, 3.2), 2.0, 3.1, boxstyle="round,pad=0.1", fc='#F0FDF4', ec='#15803D', lw=2))
    ax.text(4.8, 5.9, 'TCA9548A\nI2C Multiplexer', ha='center', va='center', fontweight='bold', color='#14532D', fontsize=10)
    ax.text(4.8, 4.8, 'Address: 0x70\n8 Independent Busses\n(Ch 0..7 Channels)\nPrevents Address Conflict', ha='center', va='center', color='#166534', fontsize=8)
    ax.text(4.8, 3.7, 'SDA/SCL In -> Out 0..7\nHardware Reset Pin', ha='center', va='center', color='#15803D', fontsize=7.5, fontfamily='monospace')

    # Connecting bus MCU -> MUX
    ax.annotate('', xy=(3.8, 5.0), xytext=(2.7, 5.0), arrowprops=dict(arrowstyle="<->", lw=2, color='#1D4ED8'))
    ax.text(3.25, 5.2, 'I2C Bus 0\n(SDA/SCL)', ha='center', va='bottom', fontsize=7.5, color='#1D4ED8', fontweight='bold')

    # 8x VL53L1X Sensors
    sensors = [
        ('S0 (Front, 0°)', 6.2),
        ('S1 (F-Right, +25°)', 5.4),
        ('S2 (Right, 0°)', 4.6),
        ('S3 (R-Right, +25°)', 3.8),
        ('S4 (Rear, 0°)', 3.0),
        ('S5 (R-Left, +25°)', 2.2),
        ('S6 (Left, 0°)', 1.4),
        ('S7 (F-Left, +25°)', 0.6)
    ]

    for label, y in sensors:
        color = '#0284C7' if '0°' in label else '#D97706'
        bg = '#E0F2FE' if '0°' in label else '#FEF3C7'
        ax.add_patch(patches.FancyBboxPatch((7.0, y - 0.25), 2.4, 0.6, boxstyle="round,pad=0.05", fc=bg, ec=color, lw=1.5))
        ax.text(8.2, y + 0.05, label, ha='center', va='center', fontweight='bold', color='#0F172A', fontsize=7.5)
        ax.text(8.2, y - 0.15, 'ST VL53L1X ToF (940nm Class-1)', ha='center', va='center', color='#475569', fontsize=6.5)

        # Connection lines from MUX
        ax.annotate('', xy=(7.0, y + 0.05), xytext=(5.8, 4.8), arrowprops=dict(arrowstyle="->", lw=1, color='#15803D', connectionstyle="arc3,rad=0.1"))

    # Power rail
    ax.plot([0.5, 9.4], [6.8, 6.8], color='#DC2626', lw=2, ls='--')
    ax.text(0.6, 6.95, '3.3V Regulated Power Rail (Decoupled with 0.1uF + 10uF caps)', color='#DC2626', fontsize=8, fontweight='bold')

    ax.set_xlim(0, 9.8)
    ax.set_ylim(0, 7.2)
    ax.axis('off')
    plt.title('SHEET 1: Optical Sensing & I²C Multiplexing Subsystem', fontsize=11, fontweight='bold', color='#1E293B', pad=10)
    plt.tight_layout()
    plt.savefig('assets/schematic_sheet1.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Sheet 2: Haptic Actuation Subsystem
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    # ESP32-S3 Core 1 block
    ax.add_patch(patches.FancyBboxPatch((0.5, 2.5), 2.2, 3.8, boxstyle="round,pad=0.1", fc='#EFF6FF', ec='#1D4ED8', lw=2))
    ax.text(1.6, 5.8, 'ESP32-S3 MCU\nCore 1: Haptic DSP', ha='center', va='center', fontweight='bold', color='#1E3A8A', fontsize=10)
    ax.text(1.6, 4.6, 'Distance-to-Cadence\nMapping Engine\n(1.2s to 12Hz Cadence)\nSpatial Interpolation\nAlert Decay (3s Window)', ha='center', va='center', color='#1E40AF', fontsize=7.5)
    ax.text(1.6, 3.2, 'Dedicated I2C Bus 1\n(SDA: GPIO 15, SCL: 16)\nHardware EN / TRIG Pins', ha='center', va='center', color='#3B82F6', fontsize=7.5, fontfamily='monospace')

    # 8x DRV2605L Drivers & 8x LRAs
    drivers = [
        ('DRV2605L #1', 'LRA 1 (Front)', 6.0),
        ('DRV2605L #2', 'LRA 2 (Front-R)', 5.2),
        ('DRV2605L #3', 'LRA 3 (Right)', 4.4),
        ('DRV2605L #4', 'LRA 4 (Rear-R)', 3.6),
        ('DRV2605L #5', 'LRA 5 (Rear)', 2.8),
        ('DRV2605L #6', 'LRA 6 (Rear-L)', 2.0),
        ('DRV2605L #7', 'LRA 7 (Left)', 1.2),
        ('DRV2605L #8', 'LRA 8 (Front-L)', 0.4)
    ]

    for drv_name, lra_name, y in drivers:
        # Driver IC box
        ax.add_patch(patches.FancyBboxPatch((3.8, y - 0.25), 2.2, 0.65, boxstyle="round,pad=0.05", fc='#F5F3FF', ec='#7C3AED', lw=1.5))
        ax.text(4.9, y + 0.1, drv_name, ha='center', va='center', fontweight='bold', color='#5B21B6', fontsize=8)
        ax.text(4.9, y - 0.12, 'Auto-Resonance 205Hz', ha='center', va='center', color='#6D28D9', fontsize=6.5)

        # LRA box
        ax.add_patch(patches.Circle((7.8, y + 0.05), 0.3, facecolor='#FEF2F2', edgecolor='#DC2626', lw=1.8))
        ax.text(7.8, y + 0.05, 'LRA', ha='center', va='center', fontweight='bold', color='#991B1B', fontsize=7.5)
        ax.text(8.7, y + 0.05, lra_name, ha='left', va='center', fontweight='bold', color='#1E293B', fontsize=7.5)

        # Connecting arrows
        ax.annotate('', xy=(3.8, y + 0.05), xytext=(2.7, 4.5), arrowprops=dict(arrowstyle="->", lw=1, color='#1D4ED8', connectionstyle="arc3,rad=-0.05"))
        ax.annotate('', xy=(7.5, y + 0.05), xytext=(6.0, y + 0.05), arrowprops=dict(arrowstyle="->", lw=1.5, color='#7C3AED'))

    ax.set_xlim(0, 9.8)
    ax.set_ylim(0, 6.8)
    ax.axis('off')
    plt.title('SHEET 2: Resonant Haptic Actuation Subsystem (DRV2605L + 205Hz LRAs)', fontsize=11, fontweight='bold', color='#1E293B', pad=10)
    plt.tight_layout()
    plt.savefig('assets/schematic_sheet2.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Sheet 3: Power Management, Charging & BMS
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    # Battery
    ax.add_patch(patches.FancyBboxPatch((0.5, 1.5), 1.8, 2.0, boxstyle="round,pad=0.1", fc='#FEF3C7', ec='#D97706', lw=2))
    ax.text(1.4, 2.8, 'Li-ion Battery\n3.7V 2500mAh', ha='center', va='center', fontweight='bold', color='#92400E', fontsize=9)
    ax.text(1.4, 1.9, '1S Pack\nIEC 62133 Cert Ref\nHardware Fuse 2A', ha='center', va='center', color='#B45309', fontsize=7.5)

    # BMS Protection IC
    ax.add_patch(patches.FancyBboxPatch((2.9, 1.5), 1.8, 2.0, boxstyle="round,pad=0.1", fc='#FEE2E2', ec='#DC2626', lw=2))
    ax.text(3.8, 2.8, 'Hardware BMS\nProtection', ha='center', va='center', fontweight='bold', color='#991B1B', fontsize=9)
    ax.text(3.8, 1.9, 'OVP: 4.25 V cutoff\nUVP: 2.80 V cutoff\nOCP: 2.0 A limit', ha='center', va='center', color='#B91C1C', fontsize=7.5)

    # USB-C Charger IC
    ax.add_patch(patches.FancyBboxPatch((1.7, 0.2), 1.8, 0.9, boxstyle="round,pad=0.08", fc='#F1F5F9', ec='#475569', lw=1.5))
    ax.text(2.6, 0.65, 'USB-C Interface (5V)\nCharge Controller', ha='center', va='center', fontweight='bold', color='#334155', fontsize=8)

    # 3.3V Buck-Boost DC-DC
    ax.add_patch(patches.FancyBboxPatch((5.3, 1.5), 1.8, 2.0, boxstyle="round,pad=0.1", fc='#EFF6FF', ec='#2563EB', lw=2))
    ax.text(6.2, 2.8, 'High-Efficiency\nDC-DC Buck-Boost', ha='center', va='center', fontweight='bold', color='#1E40AF', fontsize=9)
    ax.text(6.2, 1.9, '3.3V Output Rail\nLow Ripple (<15mV)\nUltra-low Iq Sleep', ha='center', va='center', color='#2563EB', fontsize=7.5)

    # Power Distribution Rails
    ax.add_patch(patches.FancyBboxPatch((7.7, 2.6), 1.8, 1.1, boxstyle="round,pad=0.08", fc='#F0FDF4', ec='#16A34A', lw=1.5))
    ax.text(8.6, 3.15, 'Sensors & MUX Rail\n(3.3V @ 150mA max)', ha='center', va='center', fontweight='bold', color='#15803D', fontsize=8)

    ax.add_patch(patches.FancyBboxPatch((7.7, 1.1), 1.8, 1.1, boxstyle="round,pad=0.08", fc='#FAF5FF', ec='#9333EA', lw=1.5))
    ax.text(8.6, 1.65, 'Haptic Drivers Rail\n(Hardware Limit 150mA)', ha='center', va='center', fontweight='bold', color='#7E22CE', fontsize=8)

    # Arrows
    ax.annotate('', xy=(2.9, 2.5), xytext=(2.3, 2.5), arrowprops=dict(arrowstyle="->", lw=2, color='#D97706'))
    ax.annotate('', xy=(5.3, 2.5), xytext=(4.7, 2.5), arrowprops=dict(arrowstyle="->", lw=2, color='#DC2626'))
    ax.annotate('', xy=(7.7, 3.15), xytext=(7.1, 2.8), arrowprops=dict(arrowstyle="->", lw=1.8, color='#2563EB'))
    ax.annotate('', xy=(7.7, 1.65), xytext=(7.1, 2.2), arrowprops=dict(arrowstyle="->", lw=1.8, color='#2563EB'))
    ax.annotate('', xy=(2.6, 1.5), xytext=(2.6, 1.1), arrowprops=dict(arrowstyle="->", lw=1.8, color='#475569'))

    ax.set_xlim(0, 9.8)
    ax.set_ylim(0, 4.2)
    ax.axis('off')
    plt.title('SHEET 3: Power Distribution, Battery Management & Safety Protection', fontsize=11, fontweight='bold', color='#1E293B', pad=10)
    plt.tight_layout()
    plt.savefig('assets/schematic_sheet3.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Sheet 4: Motion Sensing (BMI160) & BLE Companion Interface
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    # BMI160 IMU
    ax.add_patch(patches.FancyBboxPatch((0.6, 1.4), 2.2, 2.2, boxstyle="round,pad=0.1", fc='#FEF2F2', ec='#EF4444', lw=2))
    ax.text(1.7, 2.8, 'BMI160 6-DOF IMU\n(Accel + Gyro)', ha='center', va='center', fontweight='bold', color='#991B1B', fontsize=9.5)
    ax.text(1.7, 1.9, 'Step Detection / Motion\nStationary Recognition\nInterrupt Trigger to ULP', ha='center', va='center', color='#B91C1C', fontsize=8)

    # ESP32 ULP & BLE
    ax.add_patch(patches.FancyBboxPatch((3.7, 1.2), 2.5, 2.6, boxstyle="round,pad=0.1", fc='#EFF6FF', ec='#2563EB', lw=2))
    ax.text(4.95, 3.2, 'ESP32-S3 Dual-Core\nULP Coprocessor', ha='center', va='center', fontweight='bold', color='#1E40AF', fontsize=9.5)
    ax.text(4.95, 2.3, '15 uA Light Sleep Mode\n5 ms Fast Wake on Motion\nBLE 5.0 Radio Stack\n(Zero Internet Dependency)', ha='center', va='center', color='#1D4ED8', fontsize=8)
    ax.text(4.95, 1.45, 'Offline-First BLE Telemetry', ha='center', va='center', color='#3B82F6', fontsize=7.5, fontstyle='italic')

    # Accessible Companion App
    ax.add_patch(patches.FancyBboxPatch((7.1, 2.4), 2.3, 1.5, boxstyle="round,pad=0.1", fc='#F0FDF4', ec='#16A34A', lw=1.8))
    ax.text(8.25, 3.3, 'Deaf-Blind End User\nTalkBack / VoiceOver', ha='center', va='center', fontweight='bold', color='#14532D', fontsize=8.5)
    ax.text(8.25, 2.7, 'Zero-Sight Self-Test\nHaptic Verification Mirror', ha='center', va='center', color='#166534', fontsize=7.5)

    # O&M Trainer App
    ax.add_patch(patches.FancyBboxPatch((7.1, 0.6), 2.3, 1.5, boxstyle="round,pad=0.1", fc='#FAF5FF', ec='#9333EA', lw=1.8))
    ax.text(8.25, 1.5, 'O&M Trainer Mode\nEnAble India Mirror', ha='center', va='center', fontweight='bold', color='#581C87', fontsize=8.5)
    ax.text(8.25, 0.9, 'Real-time 360° Radar View\nBattery & Sensor Telemetry', ha='center', va='center', color='#6B21A8', fontsize=7.5)

    # Connectors
    ax.annotate('', xy=(3.7, 2.5), xytext=(2.8, 2.5), arrowprops=dict(arrowstyle="->", lw=2, color='#DC2626'))
    ax.text(3.25, 2.7, 'INT Pin\nWakeup', ha='center', va='bottom', fontsize=7.5, color='#DC2626', fontweight='bold')

    ax.annotate('', xy=(7.1, 3.15), xytext=(6.2, 2.8), arrowprops=dict(arrowstyle="<->", lw=1.8, color='#2563EB', ls='--'))
    ax.annotate('', xy=(7.1, 1.35), xytext=(6.2, 2.2), arrowprops=dict(arrowstyle="<->", lw=1.8, color='#2563EB', ls='--'))
    ax.text(6.65, 3.1, 'BLE Link', ha='center', va='bottom', fontsize=7.5, color='#2563EB', fontweight='bold')

    ax.set_xlim(0, 9.8)
    ax.set_ylim(0, 4.2)
    ax.axis('off')
    plt.title('SHEET 4: Motion Sensing (BMI160), Low-Power ULP & BLE Companion Interface', fontsize=11, fontweight='bold', color='#1E293B', pad=10)
    plt.tight_layout()
    plt.savefig('assets/schematic_sheet4.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated all 4 schematic sheets.")

create_dual_plane_geometry()
create_schematic_sheets()
