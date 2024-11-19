from vpython import sphere, vec, rate, mag2, norm, pi, sqrt

G = 39.42  # Newton's gravitation konstant


# 2 simulasjoner under

# 2 Massive stjerner i midten med planet i bane
m1 = 0.005 # Planet masse
m2 = 10  # Stjerne masse
m3 = 10  # Stjerne masse
r_planet = 0.05
r_stjerne = 0.03
d_planet = 2
v_planet = 20
v_star = 40

# 2 planeter i midten med planet i bane
# m1 = 1 # Planet masse
# m2 = 1  # Stjerne masse
# m3 = 1  # Stjerne masse
# r_planet = 0.03
# r_stjerne = 0.03
# d_planet = 0.5
# v_planet = 2
# v_star = 3


M = m1 + m2 + m3


# Himmellegemer
bodies = [
    {
        'sphere': sphere(pos=vec(d_planet, 0, 0), radius=r_planet, color=vec(1, 0, 0), make_trail=True),
        'mass': m1,
        'vel': vec(0, v_planet, 0),
        'force': vec(0, 0, 0)
    },
    
    # Fjern disse for simulasjon med 3 planeter
    ########################################################################################################
    {
        'sphere': sphere(pos=vec(d_planet*1.5, 0, 0), radius=r_planet, color=vec(1, 0, 0), make_trail=True),
        'mass': m1,
        'vel': vec(0, v_planet*0.8, 0),
        'force': vec(0, 0, 0)
    },
    {
        'sphere': sphere(pos=vec(d_planet*2, 0, 0), radius=r_planet, color=vec(1, 0, 0), make_trail=True),
        'mass': m1,
        'vel': vec(0, v_planet*0.7, 0),
        'force': vec(0, 0, 0)
    },
    ########################################################################################################
    
    {
        'sphere': sphere(pos=vec(0.05, 0, 0), radius=r_stjerne, color=vec(1, 1, 0), make_trail=True, retain=16),
        'mass': m2,
        'vel': vec(0, v_star, 0),
        'force': vec(0, 0, 0)
    },
    {
        'sphere': sphere(pos=vec(-0.05, 0, 0), radius=r_stjerne, color=vec(1, 1, 0), make_trail=True, retain=16),
        'mass': m3,
        'vel': vec(0, -v_star, 0),
        'force': vec(0, 0, 0)
    }
]

# Senter av masse
CM = sphere(pos=vec(0, 0, 0), radius=0.01, color=vec(1, 1, 1))

# Tidssteg (veldig lav er nødvendig så de massive stjernene ikke går amok)
dt = 0.0000006

while True:
    rate(1 / dt)
    
    # Reset kraften på hver av himmellegeme'ene
    for body in bodies:
        body['force'] = vec(0, 0, 0)
    
    # Finn kraften mellom hver av planetene
    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies):
            if i < j:
                r = body1['sphere'].pos - body2['sphere'].pos
                r = r if r.mag > 0.2 else r * (0.1 / r.mag)
                F = - G * body1['mass'] * body2['mass'] / r.mag2 * r.hat
                body1['force'] += F
                body2['force'] -= F
    
    # Oppdater fart og posisjon
    for body in bodies:
        body['vel'] += body['force'] / body['mass'] * dt
        body['sphere'].pos += body['vel'] * dt
    
    # Oppdater senter av masse posisjon
    CM.pos = sum((body['mass'] * body['sphere'].pos for body in bodies), vec(0, 0, 0)) / M
