# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:44:59 2017

@author: adamq
"""

"""
Code Summary:
This code serves to build waveforms from the ground up using harmonics. As applied to
auto-correlation, one can remove harmonics one by one and see if/how the auto-correlation
is affected.

"""

import numpy as np

def sineharmonics(harmonics, amplitudes, length, steps):
    """
    Function description:
    Take a list of different harmonics and return a sum of sinewaves, one sinewave
    corresponding to each harmonic, over the time domain
    
    harmonics: array, list of harmonics
    amplitudes: array, list of coefficient values for each sine wave, should have
                same length as harmonics
    length: maximum value of time of signal
    steps: number of steps in signal
    
    Pseudocode:
        
        Define a time domain with length "length" and step amount "steps
        Define an empty array with lenght "steps to fill with signal information
        Define a loop to iterate through each harmonic:
            Add a sequence equivalent to a sine wave of the harmonic, with respect to the time domain
        Return the signal value
    
    """
    
    t_domain = np.linspace(0, length, steps)
    signal = np.zeros(steps)
    for i in range(0, len(harmonics)):
        signal += amplitudes[i]*np.sin(np.pi*2*harmonics[i]*t_domain)
    return signal