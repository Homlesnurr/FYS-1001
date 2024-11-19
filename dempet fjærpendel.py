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
def aksel(pos, v):
    friksjon = -mu * m * g * np.sign(v) # np.sign(v) bestemmer retningen, og får ingen del på 0 feil
    fjærkraft = -k * pos
    return (fjærkraft + friksjon) / m

# Simulasjonsløkke
while t < 7:
    a = aksel(x[-1], v)
    v += a * dt
    ny_x = x[-1] + v * dt
    x.append(ny_x)
    t += dt

# Plotting av posisjonen
t_list = np.arange(0, len(x) * dt, dt)

plt.figure(figsize=(12, 6))
plt.plot(t_list, x, label='Amplitude (m)')
plt.title('Kloss Amplitude')
plt.xlabel('Tid (s)')
plt.ylabel('Amplitude (m)')
plt.legend()
plt.grid()
plt.show()