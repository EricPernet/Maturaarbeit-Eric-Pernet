import numpy as np
import matplotlib.pyplot as plt
 
# Define your data: True Wind Angle (TWA) and Boat Speed for different True Wind Speeds (TWS)
# Example data:
twa = np.arange(0, 190, 10)  # True Wind Angle in degrees
tws = np.array([5, 10, 15])   # True Wind Speeds in knots (fuer 20 Knoten Graph nach "15" 20 einfuegen)
boat_speeds = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)], #Blauer Graph 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)], #Oranger Graph 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)], #Gruener Graph 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)]]) #Roter Graph 
 
# Polardiagramm erstellen
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
 
for i in range(len(tws)):
    ax.plot(np.radians(twa), boat_speeds[i], label=f" {tws[i]} Knoten")
 
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rticks([2, 4, 6, 8, 10, 12, 14, 16, 18]) #Werte fuer Geschwindigkeiten im Diagramm
ax.set_rlabel_position(0)
ax.set_title('Polardiagramm') #Titel setzen
ax.legend(loc='lower left', title = 'Windgeschwindigkeit') #Legende unten links
 
 
plt.show()
