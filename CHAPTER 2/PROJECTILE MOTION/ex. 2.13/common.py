import numpy as np

g = 9.8
B2 = 4e-5
mps = 0.44704

def euler(x, y, vx, vy, dt, wind=0.0):
    vrelx = vx - wind
    vrely = vy

    v = np.sqrt(vrelx**2 + vrely**2)

    ax = -B2 * v * vrelx
    ay = -g - B2 * v * vrely

    vx += ax * dt
    vy += ay * dt
    x  += vx * dt
    y  += vy * dt

    return x, y, vx, vy
