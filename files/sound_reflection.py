# -*- coding: utf-8 -*-
"""
Author: Adam Gao
"""

"""
Code Summary:
The following code calculates and prints characteristics of a sequence
in the temporal domain.

The imported sequences are in the temporal domain. Time
should have been discretized.

Cross-correlation and autocorrelation sequences are calculated using np.correlated
from the numpy package.
"""
#import modules
import numpy as np
import pylab as plt
import Waveforms as wv

#define or import sound source sequence, sequence should be an array:
a_n = wv.sinewave_r1[500:3500]

#define or import reflection of sound source:
a_n_m = wv.sinewave_r1[700:3700]

#Plot the two sequences:
plt.figure()
plt.title("Sound sequences")
plt.plot(a_n, label = "direct sound")
plt.plot(a_n_m, label = "reflected sound")
plt.legend(loc = "upper right")

"""
First, do the most naiive thing:
Plot the auto-correlation sequence of the direct sound source

Pseudocode:
    
    Take the autocorrelation sequence of a_n
    Plot the autocorrelation sequence
"""
a_n_auto = np.correlate(a_n, a_n, mode = "same")
plt.figure()
plt.title("Auto-correlation sequence of direct sound source")
plt.plot(a_n_auto)

"""
The square sum of a sound a_n and its reflection is calculated and then
compared with an expression including autocorrelation of a_n. Assuming a perfectly
reflected sound, the two expressions should theoretically be equal.

For ease of reading, variables with name E denote the ensemble average terms.
Note that the ensemble average of a single sequence a_n is just a_n.

Pseudocode:

    Define L.H.S of the equation, E_sq
    Define R.H.S of the equation, E_auto
    Plot E_sq and E_auto to be compared with eachother
"""
#Square average:
E_sq = (a_n + a_n_m)**2

#Auto-correlation term:
E_auto = a_n**2 + a_n_m**2 + 2*np.correlate(a_n, a_n, "same")

#Plot the two sequences
plt.figure()
plt.plot(E_sq, label = "L.H.S: Squared sum")
plt.plot(E_auto, label = "R.H.S: Sum of squared averages and Auto-Correlation")
plt.legend(loc = "upper right")