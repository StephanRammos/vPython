from vpython import *

scene.title = "Two Triangles Folding"
scene.background = color.white
scene.center = vector(0.5, 0.3, 0)
scene.forward = vector(-1, -1, -1)

# Define triangle base points
A = vector(0, 0, 0)
B = vector(1, 0, 0)
C = vector(0.5, 0.87, 0)

# Draw central triangle
tri1 = triangle(vs=[vertex(pos=A, color=color.blue),
                    vertex(pos=B, color=color.blue),
                    vertex(pos=C, color=color.blue)])

# Triangle 2 shares vertex C
D = vector(1.5, 0.87, 0)
tri2_vs = [vertex(pos=B, color=color.orange),
           vertex(pos=D, color=color.orange),
           vertex(pos=C, color=color.orange)]
tri2 = triangle(vs=tri2_vs)

# Triangle 3 shares vertex A
E = vector(-0.5, 0.87, 0)
tri3_vs = [vertex(pos=A, color=color.green),
           vertex(pos=E, color=color.green),
           vertex(pos=C, color=color.green)]
tri3 = triangle(vs=tri3_vs)

# Animate folding both triangles up
for angle in range(0, 91):
    rate(30)
    for v in tri2_vs:
        v.pos = rotate(v.pos - C, angle=radians(1), axis=vector(1, 0, 0)) + C
    for v in tri3_vs:
        v.pos = rotate(v.pos - C, angle=radians(1), axis=vector(1, 0, 0)) + C

# Keep window open
while True:
    rate(10)
