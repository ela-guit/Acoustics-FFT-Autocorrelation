# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 01:21:21 2017

@author: adamq
"""

"""
Code Summary:
    
    The following code serves to test the effectiveness of auto-correlation in
    detecting fundamental frequency(s).
    
"""

#import modules
import numpy as np
import scipy as sc
import pylab as plt
import Waveforms as wv
import Waveforms3 as wv3

"""
Pseudocode:
    Define a list of harmonic numbers for each signal
    Define a list of coefficiens for each harmonic number for each signal
    Define signals using the wv3.sineharmonics function
    Get the auto-correlation sequences
    Plot signals and their auto-correlation sequences and their fourier transforms
"""

#define harmonic numbers and their coefficients:
a_1n, a_1c = np.linspace(1, 20, 20), np.linspace(1, 0, 20)
a_2n, a_2c = np.linspace(2, 20, 19), np.linspace(19/20, 0, 19)
a_3n, a_3c = np.linspace(5, 20, 16), np.linspace(16/20, 0, 16)

#define or import sound sequence, sequence should be an array:

a_1 = wv3.sineharmonics(a_1n, a_1c, 15, 1500)
a_2 = wv3.sineharmonics(a_2n, a_2c, 15, 1500)
a_3 = wv3.sineharmonics(a_3n, a_3c, 15, 1500)

b_1 = a_1*np.random.rand(len(a_1))
b_2 = a_2*np.random.rand(len(a_2))
b_3 = a_3*np.random.rand(len(a_3))

#get auto-correlation sequences
a_1_auto = np.correlate(a_1, a_1, mode = "full")
a_2_auto = np.correlate(a_2, a_2, mode = "full")
a_3_auto = np.correlate(a_3, a_3, mode = "full")

b_1_auto = np.correlate(b_1, b_1, mode = "full")
b_2_auto = np.correlate(b_2, b_2, mode = "full")
b_3_auto = np.correlate(b_3, b_3, mode = "full")

"""
############## Harmonic number plots#####################
"""
plt.figure()
plt.plot(a_1n, a_1c, label = "Signal A1")
plt.plot(a_2n, a_2c, label = "Signal A2")
plt.plot(a_3n, a_3c, label = "Signal A3")
plt.title("Harmonic number amplitudes")
plt.ylabel("Harmonic number Coefficient value")
plt.xlabel("Harmonic number")
plt.legend(loc = "upper right")

"""
###############Signal plots#############################
"""

plt.figure()
plt.plot(a_1)
plt.title("Signal A1")
plt.ylabel("y axis, 'signal amplitude'")
plt.xlabel("'temporal domain' arbitrary units")


plt.figure()
plt.plot(a_2)
plt.title("Signal A2")
plt.ylabel("y axis, 'signal amplitude'")
plt.xlabel("'temporal domain' arbitrary units")



plt.figure()
plt.plot(a_3)
plt.title("Signal A3")
plt.ylabel("y axis, 'signal amplitude'")
plt.xlabel("'temporal domain' arbitrary units")

"""
#################Auto-correlation plots############################
"""

plt.figure()
plt.plot(a_1_auto)
plt.title("Signal A1 auto-correlation")
plt.ylabel("y axis, 'signal amplitude'")
plt.xlabel("'temporal domain' arbitrary units")

plt.figure()
plt.plot(a_2_auto)
plt.title("Signal A2 auto-correlation")
plt.ylabel("y axis, 'signal amplitude'")
plt.xlabel("'temporal domain' arbitrary units")

plt.figure()
plt.plot(a_3_auto)
plt.title("Signal A3 auto-correlation")
plt.ylabel("y axis, 'signal amplitude'")
plt.xlabel("'temporal domain' arbitrary units")

"""
##################Frequency Plots###############################
"""

plt.figure()
plt.plot(np.fft.rfft(a_1))
plt.title("Fourier Transform of signal A1")
plt.ylabel("'Frequency amplitude'")
plt.xlabel("'frequency domain' arbitrary units")

plt.figure()
plt.plot(np.fft.rfft(a_2))
plt.title("Fourier Transform of signal A2")
plt.ylabel("'Frequency amplitude'")
plt.xlabel("'frequency domain' arbitrary units")

plt.figure()
plt.plot(np.fft.rfft(a_3))
plt.title("Fourier Transform A3")
plt.ylabel("'Frequency amplitude'")
plt.xlabel("'Frequency domain' arbitrary units")