import numpy as np
import matplotlib.pyplot as plt

# %% Startverdier
d = -10  # Sammentrekning av fjær (m)
dt = 1e-4# Tidsteg (s)
Theta = np.pi/4  # Vinkel på kanon (rad)
m = 70  # Masse på person (kg)
c = 0.7  # Luftmotstands koeffisient hode først
A = 0.18  # Areal tversnitt menneske hode først (m^2)
rho = 1.2  # Ca. luftdensitet i Tromsø ved 15 grader 85% luftfuktighet (kg/m^3)
g = 9.81  # Gravitasjonskonstant (m/s^2)
n = 0

# %% Startposisjoner etter utskytning
x = 0  # Startposisjon i x etter utskytning (m)
y = np.sin(Theta)*10  # Startposisjon i y etter utskytning (m)

# Lister for å oppbevare posisjoner, fart og akselerasjon
x_list = []
y_list = []
v_list = []
a_list = []


# Starter med en større økning for 'k'
klow = 0
khigh = 1000
k = (khigh + klow)/2  # Startverdi for fjærkonstant (N/m)
k_øker = 50  # Justering av fjærkonstanten

# %% Simuleringer utskytning
while True:  # Itererer helt til den treffer 50 meter
    # Resetter posisjoner, fart og akselerasjon for hver iterasjon
    x = 0
    y = np.sin(Theta)*10
    v_x = 0
    v_y = 0
    a = 0
    v = 0
    d = -10
    F = 1
    x_list = [x]
    y_list = [y]
    v_list = [v]
    a_list = [a]

    # %% Akselerasjon inni kanon
    while d < 0:
        F = -k*d - m*g*np.sin(Theta) if F > 0 else 0
        a = F/m
        v = v + a*dt
        d = d + v*dt

        # Ser på endring av fart og akselerasjon
        v_list.append(v)
        a_list.append(a)

    # Startfart etter utskytning
    v_x = v*np.cos(Theta)
    v_y = v*np.sin(Theta)

    # %% Posisjon i lufta
    while y >= 0:  # Stopper når den treffer bakken
        angle = np.arctan(v_y/v_x)
        Luftmotstand = 1/2*rho*np.sqrt(v_x**2 + v_y**2)**2*c*A
        a_y = (-m*g - Luftmotstand*np.sin(angle))/m
        a_x = -Luftmotstand*np.cos(angle)/m
        v_x = v_x + a_x*dt
        v_y = v_y + a_y*dt
        x = x + v_x*dt
        y = y + v_y*dt

        # Oppbevarer posisjoner for plotting
        x_list.append(x)
        y_list.append(y)

    # Juster k basert på hvor langt fra 50 meter vi er
    if x > 50:
        khigh = k
    else:
        klow = k
    # Avslutt hvis vi er svært nær 50 meter og feil margin er liten
    if abs(x - 50) < 0.001:
        print(f"Fant en utgangsfart på {v:.2f}m/s og en fjærkonstant. Sist kjente k: {k:.2f}N/m")
        break

    # Tester hvor mange iterasjoner man gjør
    n += 1
    print(f"Iterasjon {n}: k = {k:.2f}, x = {x:.2f}")

# Høyeste g kraft
g_kraft = a_list[1]/9.81
print(f'høyeste g kraften er {g_kraft:.2f} som er helt overlevbart')
# Farten personen treffer madrassen med
Theta_treff = np.arctan(v_y/v_x)
v_treff = v_y/np.sin(Theta_treff)
print(f'Personen treffer madrassen med en fart på {v_treff:.2f} m/s som også er overlevbart, men kommer an på madrassen')

# %% Plotter siste utkast
plt.plot(x_list, y_list)
plt.title('Menneske i kanon med luftmotstand')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.show()
