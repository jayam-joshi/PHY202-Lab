import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

# -----------------------------------------------------------------
# DO NOT RUN THIS CODE THROUGH COLAB CHECK HOW THINGS ARE DONE HERE
# -----------------------------------------------------------------

''' 
   Random_Walk.py

1. On the night of new year's eve, a person got drunk and trying to reach home.
He is in a road (consider one dimension) and takes random steps (either +1.0
step or -1.0 step) in every 15 sec. Each step corresponds to one meter of
distance. His home is 100 meters away.
(a) If he takes a total of N steps how much distance he travel on average?
(b) How the average distance as above depends on N?
(c) Plot the histogram of the displacement.
'''


'''
PSUDO CODE:
==========
Take it as an exercise to write the PSUDO code here..
'''

Nreal  = 4096
MNstep = 1024

mean_disp = []
for Nstep in range(MNstep):

    dispR = []
    for real in range(Nreal):

        steps = nr.randint(0, 2, Nstep)
        steps[np.where(steps==0)] = -1
        disp  = np.sum(steps)
        dispR.append(disp)

    mean_disp.append(np.mean(dispR))
    print ("\tAt Iteration %5d/%5d [ %3.2f %%]" %(Nstep,MNstep, 100.*Nstep/MNstep), end="\r")

plt.clf()
plt.show()
plt.ion()

plt.figure(1)
plt.loglog(np.abs(mean_disp))

plt.figure(2)
plt.hist(mean_disp, bins=16)
