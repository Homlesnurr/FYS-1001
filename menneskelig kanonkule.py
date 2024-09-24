import numpy as np
import matplotlib.pyplot as plt

# Definer verdiene
M = 70              # kg
g = 9.81            # m/s^2
theta = np.pi / 4   # 45 grader
distanse = 50       # m
b = 0.076           # kg/s
dt = 0.0001         # s

def utskytning(v, final=False):
    x, y = 0, 10 * np.sin(theta)  # Start posisjon
    vx, vy = v * np.cos(theta), v * np.sin(theta)  # Startfart

    # Løkke som går mens personen er over bakken
    while y > 0:
        x += vx * dt
        y += vy * dt
        ax = -b * vx * abs(vx) / M  # Luftmotstand i x-retning
        ay = -b * vy * abs(vy) / M - g  # Luftmotstand i y-retning + gravitasjon
        vx += ax * dt
        vy += ay * dt

        if final:
            xlist.append(x)
            ylist.append(y)

    return x

# Binær søk for utgangshastighet
v_lav, v_høy = 0, 100  # m/s
xlist, ylist = [], []  # Lister for posisjoner

while True:
    v = (v_lav + v_høy) / 2
    test = utskytning(v)
    if abs(test - distanse) < 0.001: # Avslutter søket når testen er nær nok
        break
    if test < distanse:
        v_lav = v
    else:
        v_høy = v

# Lagrer verdiene så de kan plottes
utskytning(v, True)

print(f'Utgangshastigheten er ca. {v:.3f} m/s')

# Plotting
plt.plot(xlist, ylist)
plt.title("Menneskelig kanon")
plt.xlabel("Distanse (m)")
plt.ylabel("Høyde (m)")
plt.grid(True)
plt.show()