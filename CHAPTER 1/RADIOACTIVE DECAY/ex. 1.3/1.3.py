from nzo import plot

v, t = 0, 0
a = 10
b = 1
dt = 0.01
tmax = 10
ts = []
vs = []

while t <= tmax:
    ts.append(t)
    vs.append(v)
    v += (a - b * v) * dt
    t += dt

plot(ts, vs,
    title="Terminal Velocity",
    xlabel="Time (s)",
    ylabel="Horizontal Distance x (m)",
    labels=["x(t)"])