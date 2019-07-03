# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:17:13 2017

@author: adamq
"""

"""

Code Summary:

Test and confirm properties of waves and auto-correlation usage.
"""

#imported modules
import numpy as np
import pylab as plt
import Waveforms3 as wv3

"""
Compare the convolution between a sine wave of one cyle and a unit comb
with a sine wave of multiple cycles, with cycle number equal to the number of
spikes in the unit comb.

Pseudocode:
    Define period length of the sine wave
    Define an empty array to be turned into a unit pulse train
    Begin a loop to iterate through each index of the empty pulse train array:
        If the index is a multiple of the period length, fill the index with the unit value 1
    Define a domain for the sine function of multiple cycles, with length equal to unit pulse train length
    Define a domain for a single sine wave cycle using period length
    Define a single cycle sinewave over the period length domain
    Get the convolution between the unit pulse train and the single cycle sine wave
    Define  domain for convolution
"""
N = 10 #length of one cycle, i.e period length

#Define a unit impulse train as a sequence:
    
#Create an array:
unit_comb = np.zeros(N*100)
#Fill the array with the unit value at different spacings N
for i in range(0, len(unit_comb)):
    if i%int(N*10) == 0: #if the array index is not a multiple of N:
        unit_comb[i] = 1 #fill the index with the unit value 1
        
#domain for the sine function of multiple cycles
x_domain_long = np.linspace(0, len(unit_comb)/10, len(unit_comb))

#domain for the sinewave of one cycle.
x_domain_single = np.linspace(0, N, N*10)
#define the sine wave of one cycle as a sequence.
a_n = np.sin(x_domain_single*(2*np.pi)/N)
#Take the convolution between the single cycle sinewave and the impulse train.
a_n_convolve = np.convolve(a_n, unit_comb, "same")
#Define the domain for the convolution sequence
x_domain_convolve =np.linspace(0, len(a_n_convolve)/10, len(a_n_convolve))

"""
Get the convolution between a more complex waveform and the same unit pulse train as well.
Pseudocode:
    
    Define signal using the harmonics signal generator I built:
        The lowest harmonic should be such that its sine wave has the same period
        as the previously defined sine wave
    (the signal should have array length equal to that of the previous single cycle sine wave)
    Define same signal but with same length as unit pulse train (to be compared with convolution)
    Get convolution of the signal and unit pulse train

"""

b_n = wv3.sineharmonics(np.linspace(1/N,20/N,20), np.linspace(1,0,20), len(a_n)/10, len(a_n))
b_n_full = wv3.sineharmonics(np.linspace(1/N,20/N,20), np.linspace(1,0,20), len(unit_comb)/10, len(unit_comb))
b_n_convolve = np.convolve(b_n, unit_comb, "same")

"""
############ Plots below #####################
"""
plt.figure()
plt.plot(x_domain_single, a_n)
plt.title("Single Cycle Sine wave")
plt.xlabel("Arbitrary domain")
plt.ylabel("Wave amplitude")

plt.figure()
plt.plot(x_domain_long, unit_comb)
plt.title("unit pulse-train")
plt.xlabel("Arbitrary domain")
plt.ylabel("Wave amplitude")

plt.figure()
plt.plot(x_domain_convolve, a_n_convolve, label = "convolution")
plt.plot(x_domain_convolve, np.sin(x_domain_convolve*(np.pi*2/N)), label = "full sequence")
plt.title("Convolution vs Full sequence 1")
plt.xlabel("Arbitrary domain")
plt.ylabel("Wave amplitude")
plt.legend(loc="upper right")

plt.figure()
plt.plot(x_domain_single, b_n)
plt.title("Single Cycle Multiple Harmonics")
plt.xlabel("Arbitrary domain")
plt.ylabel("Wave amplitude")

plt.figure()
plt.plot(x_domain_long, b_n_convolve, label = "convolution")
plt.plot(x_domain_long, b_n_full, label = "full sequence")
plt.title("Convolution vs Full sequence 2")
plt.xlabel("Arbitrary domain")
plt.ylabel("Wave amplitude")
plt.legend(loc = "upper right")