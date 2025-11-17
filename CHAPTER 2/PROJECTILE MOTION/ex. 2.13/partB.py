import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from common import euler, mps

plt.style.use(["science", "grid", "bright"])

v0 = 110 * mps
dt = 0.001
angles = np.arange(10, 60+1, 1)

wind_head = 25 * mps
wind_tail = -25 * mps

def anglereg(deg, wind):
    theta = np.radians(deg)
    vx = v0*np.cos(theta)
    vy = v0*np.sin(theta)
    x, y = 0, 1

    while y > 0:
        x, y, vx, vy = euler(x, y, vx, vy, dt, wind = wind)

    return x

def scan(wind):
    ranges = [anglereg(a, wind) for a in angles]
    idx = np.argmax(ranges)

    return angles[idx], ranges[idx], ranges

angleh, rangeh, Rh = scan(wind_head)
anglet, ranget, Rt = scan(wind_tail)

print("HEADWIND:")
print(f"  Best angle = {angleh}°")
print(f"  Max range = {rangeh:.2f} m")

print("\nTAILWIND:")
print(f"  Best angle = {anglet}°")
print(f"  Max range = {ranget:.2f} m")

plt.figure(figsize=(10,5))
plt.plot(angles, Rh, label="25 mph headwind")
plt.plot(angles, Rt, label="25 mph tailwind")
plt.xlabel("Launch Angle (°)")
plt.ylabel("Range (m)")
plt.legend()
plt.title("Range vs Angle with Wind (110 mph)")
plt.savefig("partBb", dpi=300, bbox_inches='tight')
plt.show()
