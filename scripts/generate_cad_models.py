import struct
import math
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("cad/models", exist_ok=True)
os.makedirs("cad/renders", exist_ok=True)

def write_binary_stl(filename, facets):
    """
    facets is a list of ((nx, ny, nz), (v1x, v1y, v1z), (v2x, v2y, v2z), (v3x, v3y, v3z))
    """
    with open(filename, 'wb') as f:
        header = b'SPATIAL-SENSE CAD Model - Team Techtonics Vishwakarma Awards 2026-27'
        header = header.ljust(80, b'\0')
        f.write(header)
        f.write(struct.pack('<I', len(facets)))
        for normal, v1, v2, v3 in facets:
            f.write(struct.pack('<fff', *normal))
            f.write(struct.pack('<fff', *v1))
            f.write(struct.pack('<fff', *v2))
            f.write(struct.pack('<fff', *v3))
            f.write(struct.pack('<H', 0)) # attribute byte count

def write_obj(filename, vertices, faces):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# SPATIAL-SENSE CAD Assembly - Team Techtonics\n")
        f.write(f"o {os.path.splitext(os.path.basename(filename))[0]}\n")
        for v in vertices:
            f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
        for face in faces:
            # 1-indexed
            f.write("f " + " ".join(str(idx + 1) for idx in face) + "\n")

# Geometry helpers to build parametric boxes and cylinders
def add_box_facets(facets, cx, cy, cz, dx, dy, dz):
    hx, hy, hz = dx/2, dy/2, dz/2
    # 8 corners
    c = [
        (cx - hx, cy - hy, cz - hz),
        (cx + hx, cy - hy, cz - hz),
        (cx + hx, cy + hy, cz - hz),
        (cx - hx, cy + hy, cz - hz),
        (cx - hx, cy - hy, cz + hz),
        (cx + hx, cy - hy, cz + hz),
        (cx + hx, cy + hy, cz + hz),
        (cx - hx, cy + hy, cz + hz)
    ]
    # 6 faces * 2 triangles = 12 triangles
    faces = [
        # bottom (-z)
        ((0, 0, -1), c[0], c[2], c[1]),
        ((0, 0, -1), c[0], c[3], c[2]),
        # top (+z)
        ((0, 0, 1), c[4], c[5], c[6]),
        ((0, 0, 1), c[4], c[6], c[7]),
        # front (-y)
        ((0, -1, 0), c[0], c[1], c[5]),
        ((0, -1, 0), c[0], c[5], c[4]),
        # back (+y)
        ((0, 1, 0), c[2], c[3], c[7]),
        ((0, 1, 0), c[2], c[7], c[6]),
        # left (-x)
        ((-1, 0, 0), c[0], c[4], c[7]),
        ((-1, 0, 0), c[0], c[7], c[3]),
        # right (+x)
        ((1, 0, 0), c[1], c[2], c[6]),
        ((1, 0, 0), c[1], c[6], c[5]),
    ]
    facets.extend(faces)

def add_cylinder_facets(facets, cx, cy, cz, r, h, axis='z', segments=24):
    angles = [2 * math.pi * i / segments for i in range(segments)]
    if axis == 'z':
        # Top and bottom centers
        b_c = (cx, cy, cz - h/2)
        t_c = (cx, cy, cz + h/2)
        for i in range(segments):
            a1 = angles[i]
            a2 = angles[(i + 1) % segments]
            p1_b = (cx + r * math.cos(a1), cy + r * math.sin(a1), cz - h/2)
            p2_b = (cx + r * math.cos(a2), cy + r * math.sin(a2), cz - h/2)
            p1_t = (cx + r * math.cos(a1), cy + r * math.sin(a1), cz + h/2)
            p2_t = (cx + r * math.cos(a2), cy + r * math.sin(a2), cz + h/2)
            
            # Bottom cap
            facets.append(((0, 0, -1), b_c, p2_b, p1_b))
            # Top cap
            facets.append(((0, 0, 1), t_c, p1_t, p2_t))
            # Sides
            norm = (math.cos((a1+a2)/2), math.sin((a1+a2)/2), 0)
            facets.append((norm, p1_b, p2_t, p1_t))
            facets.append((norm, p1_b, p2_b, p2_t))
    elif axis == 'y':
        b_c = (cx, cy - h/2, cz)
        t_c = (cx, cy + h/2, cz)
        for i in range(segments):
            a1 = angles[i]
            a2 = angles[(i + 1) % segments]
            p1_b = (cx + r * math.cos(a1), cy - h/2, cz + r * math.sin(a1))
            p2_b = (cx + r * math.cos(a2), cy - h/2, cz + r * math.sin(a2))
            p1_t = (cx + r * math.cos(a1), cy + h/2, cz + r * math.sin(a1))
            p2_t = (cx + r * math.cos(a2), cy + h/2, cz + r * math.sin(a2))
            
            facets.append(((0, -1, 0), b_c, p1_b, p2_b))
            facets.append(((0, 1, 0), t_c, p2_t, p1_t))
            norm = (math.cos((a1+a2)/2), 0, math.sin((a1+a2)/2))
            facets.append((norm, p1_b, p1_t, p2_t))
            facets.append((norm, p1_b, p2_t, p2_b))

# 1. MODEL: Modular Sensor Pod Waist (0 degree)
print("Generating 3D models...")
pod0_facets = []
# Outer shell: 42mm wide x 35mm high x 22mm deep
add_box_facets(pod0_facets, 0, 0, 0, 42, 35, 22)
# Optical lens aperture bezel: cylindrical protrusion on front (+y)
add_cylinder_facets(pod0_facets, 0, 12, 0, 6.5, 4, axis='y')
# Belt slot clips (left and right)
add_box_facets(pod0_facets, -23, 0, -2, 5, 30, 4)
add_box_facets(pod0_facets, 23, 0, -2, 5, 30, 4)
# Internal LRA coin retention cavity (indicated by rear tactile bulge)
add_cylinder_facets(pod0_facets, 0, -11, 0, 7.5, 2.5, axis='y')
write_binary_stl("cad/models/modular_sensor_pod_waist_0deg.stl", pod0_facets)
print("Created cad/models/modular_sensor_pod_waist_0deg.stl")

# 2. MODEL: Modular Sensor Pod Overhead (+25 degree tilted aperture)
pod25_facets = []
# Base shell: 42mm x 38mm x 24mm
add_box_facets(pod25_facets, 0, 0, 0, 42, 38, 24)
# Tilted optical hood: wedged box and tilted aperture
add_box_facets(pod25_facets, 0, 8, 8, 28, 18, 14)
# Belt clips
add_box_facets(pod25_facets, -23, 0, -2, 5, 30, 4)
add_box_facets(pod25_facets, 23, 0, -2, 5, 30, 4)
# Rear tactile contact dome
add_cylinder_facets(pod25_facets, 0, -12, 0, 7.5, 2.5, axis='y')
write_binary_stl("cad/models/modular_sensor_pod_overhead_25deg.stl", pod25_facets)
print("Created cad/models/modular_sensor_pod_overhead_25deg.stl")

# 3. MODEL: Central Controller & Battery Enclosure
ctrl_facets = []
# Ergonomic curved housing: 95mm wide x 65mm high x 26mm deep
add_box_facets(ctrl_facets, 0, 0, 0, 95, 65, 26)
# Battery compartment lid
add_box_facets(ctrl_facets, 0, 0, 13.5, 88, 58, 3)
# Raised tactile self-test button on top (+z)
add_cylinder_facets(ctrl_facets, 25, 0, 15, 6, 4, axis='z')
# Recessed USB-C charging port bezel at bottom (-z)
add_box_facets(ctrl_facets, 0, 0, -14, 14, 8, 3)
# Belt passage anchors
add_box_facets(ctrl_facets, -52, 0, 0, 10, 45, 6)
add_box_facets(ctrl_facets, 52, 0, 0, 10, 45, 6)
write_binary_stl("cad/models/central_controller_battery_enclosure.stl", ctrl_facets)
print("Created cad/models/central_controller_battery_enclosure.stl")

# 4. MODEL: LRA Haptic Coin Holder
lra_facets = []
# Coin mount diameter 14mm, height 4.5mm
add_cylinder_facets(lra_facets, 0, 0, 0, 7.2, 4.5, axis='z')
# Outer silicone dampening ring
add_cylinder_facets(lra_facets, 0, 0, 0, 9.5, 2.0, axis='z')
write_binary_stl("cad/models/lra_haptic_coin_holder.stl", lra_facets)
print("Created cad/models/lra_haptic_coin_holder.stl")

# 5. MODEL: Belt Buckle Magnetic Clasp
buckle_facets = []
add_box_facets(buckle_facets, -18, 0, 0, 32, 40, 8)
add_box_facets(buckle_facets, 18, 0, 0, 32, 40, 8)
add_cylinder_facets(buckle_facets, 0, 0, 0, 6, 9, axis='z')
write_binary_stl("cad/models/buckle_magnetic_clasp.stl", buckle_facets)
print("Created cad/models/buckle_magnetic_clasp.stl")

# 6. FULL ASSEMBLY MODEL: SPATIAL-SENSE Waistband Assembly (STL & OBJ)
assembly_facets = []
# Waistband ring: Torus approximated by circular segments
belt_r = 160 # mm radius (~32 inch waist)
segments = 32
for i in range(segments):
    a1 = 2 * math.pi * i / segments
    a2 = 2 * math.pi * (i + 1) / segments
    x1, y1 = belt_r * math.cos(a1), belt_r * math.sin(a1)
    x2, y2 = belt_r * math.cos(a2), belt_r * math.sin(a2)
    mid_x, mid_y = (x1 + x2)/2, (y1 + y2)/2
    len_seg = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # Belt strap segment
    add_box_facets(assembly_facets, mid_x, mid_y, 0, len_seg, 4, 38)

# Add 8 pods around perimeter (every 45 degrees)
for idx in range(8):
    ang = 2 * math.pi * idx / 8
    px = (belt_r + 14) * math.cos(ang)
    py = (belt_r + 14) * math.sin(ang)
    # Alternate 0 deg (even) and +25 deg (odd)
    if idx % 2 == 0:
        add_box_facets(assembly_facets, px, py, 0, 24, 24, 22)
        add_cylinder_facets(assembly_facets, px * 1.05, py * 1.05, 0, 5, 4, axis='z')
    else:
        add_box_facets(assembly_facets, px, py, 4, 24, 24, 24)
        add_cylinder_facets(assembly_facets, px * 1.05, py * 1.05, 8, 5, 4, axis='z')

# Central controller at rear (idx = 4, ang = pi)
add_box_facets(assembly_facets, 0, -(belt_r + 18), 0, 75, 24, 45)

write_binary_stl("cad/models/spatial_sense_waistband_assembly.stl", assembly_facets)
print("Created cad/models/spatial_sense_waistband_assembly.stl")

# Also write Wavefront OBJ for easy viewing
vertices = []
faces = []
v_map = {}

def get_v_idx(v):
    v_rounded = (round(v[0], 3), round(v[1], 3), round(v[2], 3))
    if v_rounded not in v_map:
        v_map[v_rounded] = len(vertices)
        vertices.append(v_rounded)
    return v_map[v_rounded]

for normal, v1, v2, v3 in assembly_facets:
    i1 = get_v_idx(v1)
    i2 = get_v_idx(v2)
    i3 = get_v_idx(v3)
    if i1 != i2 and i2 != i3 and i3 != i1:
        faces.append((i1, i2, i3))

write_obj("cad/models/spatial_sense_waistband_assembly.obj", vertices, faces)
print("Created cad/models/spatial_sense_waistband_assembly.obj")
