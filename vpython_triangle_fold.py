from vpython import *

# Setup scene
scene.title = "Vertex-Based Triangle Fold"
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

# Define second triangle sharing vertex C (top point)
D = vector(1.5, 0.87, 0)
tri2_vs = [vertex(pos=B, color=color.orange),
           vertex(pos=D, color=color.orange),
           vertex(pos=C, color=color.orange)]
tri2 = triangle(vs=tri2_vs)

# Animate fold: rotate second triangle around vertex C
for angle in range(0, 91, 1):
    rate(30)
    for v in tri2_vs:
        v.pos = rotate(v.pos - C, angle=radians(1), axis=vector(1, 0, 0)) + C

# Keep window open so user can view final result
while True:
    rate(10)
