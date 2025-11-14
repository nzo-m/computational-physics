import numpy as np
import matplotlib.pyplot as plt
import scienceplots

tau = 1.0
dt = 0.001
t_max = 10
ts = np.arange(0, t_max + dt, dt)

initial = [
    (100, 0),
    (0, 100),
    (50, 50)]

plt.style.use(['science', 'grid', 'bright'])
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("A-B System for Different Initial Conditions")

for i, (NA0, NB0) in enumerate(initial):
    NA = np.zeros_like(ts)
    NB = np.zeros_like(ts)

    NA[0] = NA0
    NB[0] = NB0

    for j in range(len(ts) - 1):
        dNA = (NB[j] - NA[j]) / tau
        dNB = (NA[j] - NB[j]) / tau

        NA[j+1] = NA[j] + dNA * dt
        NB[j+1] = NB[j] + dNB * dt

    ax = axes[i]
    ax.plot(ts, NA, label="NA(t)")
    ax.plot(ts, NB, label="NB(t)")
    ax.set_title(f"NA0 = {NA0}, NB0 = {NB0}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Number of Nuclei")
    ax.legend(loc="best")

fig.savefig("varying-initial-conditions.png", dpi=300, bbox_inches='tight')
plt.show()
