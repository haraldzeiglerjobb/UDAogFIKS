"""
Ledetekst inn til bått laget 16.03.2025 kalt:
Realfag programmering naturfag 01

Innstillinger: 
- Naturfag fag/årstrinn/studieretning og aldersgruppe
- Programmeringsspråk (Python, javascript, C++, pseudokode/for microbit/Arduino)

Valgte "Studiespes 5 timer" og "Python"

Ledetekst: Lag et program som modellerer et naturfaglig fenomen.
"""
import matplotlib.pyplot as plt

class Plant:
    def __init__(self, water, light):
        self.water = water  # Mengde vann i liter
        self.light = light  # Lysstyrke (0-100)
        self.growth_rate = 0.0  # Vekstrate
        self.size = 0.0  # Plante størrelse i cm

    def update_growth(self):
        # Enkel modell der veksten påvirkes av både vann og lys
        self.growth_rate = (self.water * 0.5) + (self.light * 0.5)
        self.size += self.growth_rate

def simulate_growth(steps, initial_water, initial_light):
    plant = Plant(initial_water, initial_light)
    sizes = []

    for _ in range(steps):
        plant.update_growth()
        sizes.append(plant.size)

        # For enkelhets skyld, vi kan anta mengden vann og lys endres over tid
        plant.water -= 0.1  # Vann avtar
        plant.light += 0.1  # Lys øker, opp til 100
        plant.light = min(100, plant.light)  # Ikke la lyset gå over 100

    return sizes

# Parametre
steps = 50
initial_water = 20  # starten med 20 liter vann
initial_light = 50  # starten med 50 lys

# Kjør simuleringen
growth_sizes = simulate_growth(steps, initial_water, initial_light)

# Plott resultatet
plt.plot(growth_sizes)
plt.title('Plantevekst over tid')
plt.xlabel('Tid (dager)')
plt.ylabel('Plante størrelse (cm)')
plt.grid()
plt.show()