import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from common import euler, mps

plt.style.use(["science", "grid", "bright"])

v0mph = 110
v0 = v0mph * mps
dt = 0.001
angles = np.arange(10, 60 + 1, 1)

def anglerange(deg):
    theta = np.radians(deg)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    x = 0
    y = 1

    while y > 0:
        x, y, vx, vy = euler(x, y, vx, vy, dt, wind=0.0)

    return x

ranges = []

for ang in angles:
    R = anglerange(ang)
    ranges.append(R)

maxidx = np.argmax(ranges)
bestangle = angles[maxidx]
bestrange = ranges[maxidx]

print(f"Best angle = {bestangle} degrees")
print(f"Range = {bestrange:.2f} m")

plt.figure(figsize=(10,5))
plt.plot(angles, ranges)
plt.xlabel("Launch Angle (°)")
plt.ylabel("Range (m)")
plt.title("Range vs Angle\nNo wind at 110 mph")
plt.show()
