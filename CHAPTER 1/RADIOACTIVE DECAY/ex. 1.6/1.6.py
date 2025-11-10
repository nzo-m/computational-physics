from nzo import plot
import numpy as np

N = 50
a = 0.2
b = float(input("Enter death coefficient b: "))
t = 0
dt = 0.1
t_max = 50

ts = []
Ns = []

while t <= t_max:
    ts.append(t)
    Ns.append(N)
    N += (a*N - b*N**2) * dt
    t += dt

if b == 0:
    Ns_exact = [Ns[0] * np.exp(a * t) for t in ts]
    plot(ts, Ns, ts, Ns_exact,
         title=f"Population Growth (a={a}, b={b})",
         xlabel="Time",
         ylabel="Population",
         labels=["Euler", "Exact"])
else:
    plot(ts, Ns,
         title=f"Population Growth (a={a}, b={b})",
         xlabel="Time",
         ylabel="Population",
         labels=["Euler"])
