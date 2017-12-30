# -*- coding: utf-8 -*-
"""
Author: Adam Gao
"""

"""
Summary:
The following code serves to generate waveforms as sequences in time domains.
The code can be imported as a module so that the sequences may be analyzed.
"""

#import modules:
import numpy as np
import pylab as plt

"""
Single Sine Wave:
    
Generate a sequence containing a sinewave at 5<t<15
    sequence length: 4000
    sequence domain: 0<t<20
"""
#Generate discretized time domain x_n:
x_n = np.linspace(0,40,4001)

#Generate array to fill with sinewave:
sinewave = np.zeros((4001))
#Add a sine wave in a frame:
sinewave[1000:3000] = np.sin(x_n[0:2000])

"""
Single Sine Wave with one reflection:

Generate a single sine wave with a single reflection

"""

#Generate sinewave as was done before
sinewave_r1 = np.zeros((4001))
sinewave_r1[1000:3000] = np.sin(x_n[0:2000])
#Add reflection
sinewave_r1[1200:3200] += np.sin(x_n[0:2000])

"""
Saw wave:

Generate a sawtooth wave
"""

#Generate discretized time domain x_n:
x_n = np.linspace(0,40,4001)
sawtooth_width = 1.
sawtooth_height = 1.
sawtooth = sawtooth_height*x_n%sawtooth_width
