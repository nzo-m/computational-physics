from nzo import plot

v0 = 0
t0 = 0
g = 9.8
dt = 0.1
tmax = 10

vs = []
ts = []
v = v0
t = t0

while t <= tmax:
    ts.append(t)
    vs.append(v)
    v -= g * dt
    t += dt

plot(ts, vs,
    title="Euler Method: Free Fall",
    xlabel="Time (s)",
    ylabel="Velocity (m/s)",
    labels=["v(t)"])


