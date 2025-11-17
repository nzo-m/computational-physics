import numpy as np
from common import euler, mps

dt = 0.001
deg = 35
theta = np.radians(deg)

vmph = [100, 110, 120]
results = {}

def range(v0):
    vx = v0*np.cos(theta)
    vy = v0*np.sin(theta)
    x, y = 0.0, 1.0
    while y > 0:
        x, y, vx, vy = euler(x, y, vx, vy, dt)
    return x

for s in vmph:
    R = range(s * mps)
    results[s] = R

print("Launch angle =", deg)

for s in vmph:
    print(f"{s} mph  →  range = {results[s]:.2f} m")

