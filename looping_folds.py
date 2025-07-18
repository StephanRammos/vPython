
from vpython import *

# Set up expanded scene
scene.background = color.white
scene.range = 2
scene.forward = vector(-1, -1, -1)

# Define triangle vertices
A = vector(0, 0, 0)
B = vector(1, 0, 0)
C = vector(0.5, sqrt(3)/2, 0)

# Triangle 1 (center)
tri1 = triangle(v0=vertex(pos=A, color=color.red),
                v1=vertex(pos=B, color=color.red),
                v2=vertex(pos=C, color=color.red))

# Triangle 2 (attached to B)
D = B
E = vector(1.5, sqrt(3)/2, 0)
F = C
tri2_vs = [vertex(pos=D, color=color.orange),
           vertex(pos=E, color=color.orange),
           vertex(pos=F, color=color.orange)]
tri2 = triangle(v0=tri2_vs[0], v1=tri2_vs[1], v2=tri2_vs[2])

# Triangle 3 (attached to A)
G = A
H = vector(-0.5, sqrt(3)/2, 0)
I = C
tri3_vs = [vertex(pos=G, color=color.green),
           vertex(pos=H, color=color.green),
           vertex(pos=I, color=color.green)]
tri3 = triangle(v0=tri3_vs[0], v1=tri3_vs[1], v2=tri3_vs[2])

# Continuous folding loop
while True:
    for angle in range(0, 91, 1):  # Fold up
        rate(30)
        theta = radians(angle)
        for i, v in enumerate(tri2_vs):
            if i != 0:
                v.pos = rotate(v.pos - B, angle=radians(1), axis=vector(1, 0, 0)) + B
        for i, v in enumerate(tri3_vs):
            if i != 0:
                v.pos = rotate(v.pos - A, angle=radians(1), axis=vector(1, 0, 0)) + A

    for angle in range(90, -1, -1):  # Fold down
        rate(30)
        theta = radians(angle)
        for i, v in enumerate(tri2_vs):
            if i != 0:
                v.pos = rotate(v.pos - B, angle=radians(-1), axis=vector(1, 0, 0)) + B
        for i, v in enumerate(tri3_vs):
            if i != 0:
                v.pos = rotate(v.pos - A, angle=radians(-1), axis=vector(1, 0, 0)) + A
