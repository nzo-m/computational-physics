import numpy as np
from common import euler, mps

distance = 60.5 * 0.3048
v0 = 100 * mps
dt = 0.0005

x = 0.0
vx = v0
vy = 0.0
y = 1.8

while x < distance:
    x, y, vx, vy = euler(x, y, vx, vy, dt)

vf = np.sqrt(vx**2 + vy**2)

print(f"Initial: 100 mph")
print(f"Final speed at plate: {vf/mps:.2f} mph")
