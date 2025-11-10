from nzo import plot

NA = 10000
NB = 10000
TB = 100
ta_tb = float(input("TA/TB Ratio: "))
TA = TB * ta_tb

t = 1
dt = 0.01
tmax = 1000
T = []
na = []
nb = []

while t <= tmax:
    T.append(t)
    na.append(NA)
    nb.append(NB)

    dNA = -NA / TA * dt
    dNB = (NA / TA - NB / TB) * dt
    NA += dNA
    NB += dNB
    t += dt

plot(T, na, T, nb,
     title="Radioactive Decay with TA/TB = %.4f" % ta_tb,
     xlabel="Time (s)",
     ylabel="Number of atoms",
     labels=["NA(t)", "NB(t)"])
