from vpython import *
import time

scene.title = "Triangles Folding from Center Vertices"
scene.background = color.white
scene.width = 1000
scene.height = 700
scene.range = 2  # expand visible area
scene.forward = vector(-1.5, -1.2, -1)

# Define center triangle base points
A = vector(0, 0, 0)
B = vector(1, 0, 0)
C = vector(0.5, 0.87, 0)

# Draw central triangle (blue)
tri1 = triangle(vs=[vertex(pos=A, color=color.blue),
                    vertex(pos=B, color=color.blue),
                    vertex(pos=C, color=color.blue)])

# Triangle 2 folds from vertex B (orange)
D = vector(1.5, 0.87, 0)
tri2_vs = [vertex(pos=B, color=color.orange),
           vertex(pos=D, color=color.orange),
           vertex(pos=C, color=color.orange)]
tri2 = triangle(vs=tri2_vs)

# Triangle 3 folds from vertex A (green)
E = vector(-0.5, 0.87, 0)
tri3_vs = [vertex(pos=A, color=color.green),
           vertex(pos=E, color=color.green),
           vertex(pos=C, color=color.green)]
tri3 = triangle(vs=tri3_vs)

# Hold flat layout for 5 seconds
t_start = time.time()
while time.time() - t_start < 5:
    rate(10)

# Animate folding both triangles upward around their own vertex
for angle in range(0, 91):
    rate(15)
    for v in tri2_vs:
        v.pos = rotate(v.pos - B, angle=radians(1), axis=vector(1, 0, 0)) + B
    for v in tri3_vs:
        v.pos = rotate(v.pos - A, angle=radians(1), axis=vector(1, 0, 0)) + A

# Keep window open
while True:
    rate(10)
