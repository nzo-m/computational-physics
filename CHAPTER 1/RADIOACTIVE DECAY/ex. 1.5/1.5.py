from nzo import plot

tau = 1.0
dt = 0.001
t_max = 10

initial = [
    (100, 0),
    (0, 100),
    (50, 50)]

for NA0, NB0 in initial:
    NA = NA0
    NB = NB0
    time = 0

    ts = []
    NAs = []
    NBs = []

    # Euler method
    while time <= t_max:
        ts.append(time)
        NAs.append(NA)
        NBs.append(NB)

        dNA = (NB - NA) / tau
        dNB = (NA - NB) / tau

        NA += dNA * dt
        NB += dNB * dt

        time += dt

    plot(
        ts, NAs, ts, NBs,
        title=f"A ↔ B, tau={tau}s, NA0={NA0}, NB0={NB0}",
        xlabel="Time [s]",
        ylabel="Number of Nuclei",
        labels=["NA(t)", "NB(t)"]
    )
