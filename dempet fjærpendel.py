import numpy as np
import matplotlib.pyplot as plt

# Parametere
m = 0.245
mu = 0.01
k1 = 3.34
k2 = 6.83
x0 = 0.05
g = 9.81
dt = 0.001
t = 0
k = k1 + k2

# Startverdier
x = [x0]
v = 0  # startfart
# Akselerasjonsfunksjon
def aksel(pos, vel):
    friksjon = -mu * m * g * np.sign(vel)   # friksjonskraft
    fjærkraft = -k * pos                    # fjærkraft
    return (fjærkraft + friksjon) / m       # total akselerasjon

# Simulasjonsløkke
while t < 7:
    a = aksel(x[-1], v)     # beregn akselerasjon
    v += a * dt             # oppdater fart
    ny_x = x[-1] + v * dt   # oppdater posisjon
    # Lagre ny posisjon
    x.append(ny_x)
    t += dt

# Juster tidslisten basert på lengden av x
t_list = np.arange(0, len(x) * dt, dt)

# Plotting av resultatene
plt.figure(figsize=(12, 6))
plt.plot(t_list, x, label='Amplitude (m)')
plt.title('Kloss Amplitude')
plt.xlabel('Tid (s)')
plt.ylabel('Amplitude (m)')
plt.legend()
plt.grid()
plt.show()
