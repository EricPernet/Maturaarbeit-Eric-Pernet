import numpy as np
import matplotlib.pyplot as plt
 
# Define your data: True Wind Angle (TWA) and Boat Speed for different True Wind Speeds (TWS)
# Example data:
twa = np.arange(0, 190, 10)  # True Wind Angle in degrees
tws = np.array([5, 10, 15])   # True Wind Speeds in knots (fuer 20 Knoten Graph nach "15" 20 einfuegen)
boat_speeds = np.array([[ 0, 15.31, 17, 19.46, 20.5, 21.7, 23.17, 24.49, 24.97, 24.07, 26, 26.19, 26.21, 26.99, 27.15, 27.04, 25.98, 26.68, 22.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)], #Blauer Graph (3.)
                        [0, 4.53, 9.75, 13.02, 13.83, 14.53, 14.99, 14.99, 13.37, 14.36, 15.41, 15.84, 15.45, 14.86, 14.22, 9.22, 11.91, 8.52, 5.92, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)], #Oranger Graph (1.)
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)], #Grüner Graph (2.)
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][:len(twa)]]) #Roter Graph (4.)
 
# Create a polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
 
for i in range(len(tws)):
    ax.plot(np.radians(twa), boat_speeds[i], label=f" {tws[i]} Knoten")
 
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rticks([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
ax.set_rlabel_position(0)
ax.set_title('')
#ax.legend(loc='lower left', title = 'Windgeschwindigkeit')
 
 
plt.show()