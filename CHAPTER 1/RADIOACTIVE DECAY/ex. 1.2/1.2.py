from nzo import plot

x0 = 0
t0 = 0
dt = 0.01
tmax = 10
ts = []
xs = []

while t0 <= tmax:
    v = 40.0
    xs.append(x0)
    ts.append(t0)
    x0 += v * dt
    t0 += dt

plot(ts, xs,
    title="Euler Method: Horizontal Motion",
    xlabel="Time (s)",
    ylabel="Horizontal Distance x (m)",
    labels=["x(t)"])