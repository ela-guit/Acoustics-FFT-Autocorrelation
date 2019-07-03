# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:52:09 2017

@author: adamq
"""

"""
Summary:

This code serves to import .wave sound files into a single place. The description
of each sound file is given. All sound files are real recorded noises.
"""

import scipy.io.wavfile
import numpy as np
import pylab as plt

"""
Open files:

The sound files beginning with the name 'speech' are the same speech samples recorded
in rooms of different reverbations. The number at the end of the file name refers to reverb
time. I.e. 'speech reverb 2.0.wav' has reverb time of 2.0 seconds.
"""

speechdry = scipy.io.wavfile.read("speech dry.wav")
speechdry_rate, speechdry_sound = speechdry[0], speechdry[1]

speech20 = scipy.io.wavfile.read("speech reverb 2.0.wav")
speech20_rate, speech20_sound = speech20[0], speech20[1][:,0]