# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:25:33 2017

@author: adamq
"""

"""
Summary:

    The following code serves to analyze the following characteristics of the
    imported waveforms using auto-correlation and fourier transform techniques:
        
        Frame-wise power spectrum
        Frame-wise auto-correlation
    
"""

import Waveforms2 as wv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

"""
Define function to convert the time domains from sample number to seconds:

    Pseudocode:
        Define a function which returns a domain with units in seconds
            Get input sequence and sample rate
            Define a domain sequence with length equal to the input sequence length
            The domain sequence is to be filled with integers from 0 to the sequence length
            Divide the values in the domain sequence by the sample rate
            Return the domain sequence

Then get the time domains in seconds for each sound sequence.

Each sound sequence may be plotted with respect to the new converted time domains.

"""

def get_domain_s(sequence_raw, sample_rate):
    #raw domain
    domain_raw = np.linspace(0, len(sequence_raw), len(sequence_raw))
    #new domain in seconds
    domain_s = domain_raw/sample_rate
    
    return domain_s

#Get new domains in seconds
speechdry_domain_s = get_domain_s(wv2.speechdry_sound, wv2.speechdry_rate)
speech20_domain_s = get_domain_s(wv2.speech20_sound, wv2.speech20_rate)


"""
Define frames of the raw sound as sequences as follows:
    
    Define a 2 dimensional list of frame intervals:
        The 1st dimension [:] determines the frame
        The 2nd dimension [:][:] determines the frame boundaries as integer numbers
    Define new sequences for each frame of the original imported sounds
"""

#Define list of frame intervals
speechdry_frames = [[int(.150E4), int(.165E4)], [int(3E4),int(3.015E4)], [int(2E4),int(2.015E4)]]
speech20_frames = [[int(.150E4), int(.165E4)], [int(3E4),int(3.015E4)], [int(2E4),int(2.015E4)]]

#Define frames for dry speech
speechdry_1=wv2.speechdry_sound[speechdry_frames[0][0]:speechdry_frames[0][1]]
speechdry_2=wv2.speechdry_sound[speechdry_frames[1][0]:speechdry_frames[1][1]]
speechdry_3=wv2.speechdry_sound[speechdry_frames[2][0]:speechdry_frames[2][1]]

#Define frames for speech with 2.0 second reverb
speech20_1=wv2.speech20_sound[speech20_frames[0][0]:speech20_frames[0][1]]
speech20_2=wv2.speech20_sound[speech20_frames[1][0]:speech20_frames[1][1]]
speech20_3=wv2.speech20_sound[speech20_frames[2][0]:speech20_frames[2][1]]

"""
Define auto-correlation sequences of each frame.
These are direct frame-wise auto-correlations.

Also get the domains of the auto-correlation sequences in seconds.
"""

#Get auto-correlation of each frame:
    
#Dry speech:
speechdry_1_auto = np.correlate(speechdry_1, speechdry_1, "full")
speechdry_2_auto = np.correlate(speechdry_2, speechdry_2, "full")
speechdry_3_auto = np.correlate(speechdry_3, speechdry_3, "full")

#2.0 second reverb speech
speech20_1_auto = np.correlate(speech20_1, speech20_1, "full")
speech20_2_auto = np.correlate(speech20_2, speech20_2, "full")
speech20_3_auto = np.correlate(speech20_3, speech20_3, "full")

#Define raw domains in seconds:
    
#Dry speech:
speechdry_1_auto_domain_s = get_domain_s(speechdry_1_auto, wv2.speechdry_rate)
speechdry_2_auto_domain_s = get_domain_s(speechdry_2_auto, wv2.speechdry_rate)
speechdry_3_auto_domain_s = get_domain_s(speechdry_3_auto, wv2.speechdry_rate)

#2.0 second reverb speech:
speech20_1_auto_domain_s = get_domain_s(speech20_1_auto, wv2.speech20_rate)
speech20_2_auto_domain_s = get_domain_s(speech20_2_auto, wv2.speech20_rate)
speech20_3_auto_domain_s = get_domain_s(speech20_3_auto, wv2.speech20_rate)

"""
Triangularize the frames of the raw sound as follows:
    Define new triangularized frames of sequences as equal to:
        The original sequence multiplied by a triangle window of equal length
        
Then, take the auto-correlation sequences of the triangularized frames. The domains
for these auto-correlations of triangularized sequences are the same as for the auto-correlations
of non-triangularized sequences.
"""

#triangularized sequences:

#Dry speech
speechdry_1_tr = signal.triang(len(speechdry_1))*speechdry_1
speechdry_2_tr = signal.triang(len(speechdry_2))*speechdry_2
speechdry_3_tr = signal.triang(len(speechdry_3))*speechdry_3

#2.0 second reverb speech:
speech20_1_tr = signal.triang(len(speech20_1))*speech20_1
speech20_2_tr = signal.triang(len(speech20_2))*speech20_2
speech20_3_tr = signal.triang(len(speech20_3))*speech20_3
    
#Auto-correlation sequences:

#Dry speech
speechdry_1_tr_auto = np.correlate(speechdry_1_tr, speechdry_1_tr, "full")
speechdry_2_tr_auto = np.correlate(speechdry_2_tr, speechdry_2_tr, "full")
speechdry_3_tr_auto = np.correlate(speechdry_3_tr, speechdry_3_tr, "full")

#2.0 second reverb speech:

speech20_1_tr_auto = np.correlate(speech20_1_tr, speech20_1_tr, "full")
speech20_2_tr_auto = np.correlate(speech20_2_tr, speech20_2_tr, "full")
speech20_3_tr_auto = np.correlate(speech20_3_tr, speech20_3_tr, "full")

"""
Define the power spectra of each frame.
These are using direct frame-wise fourier transforms.
"""

def get_domain_Hz(fft_sequence, sample_rate):
    #raw domain
    domain_raw = np.linspace(0, len(fft_sequence), len(fft_sequence))
    #domain in Hz
    domain_Hz = domain_raw*sample_rate/(np.pi*2)
    
    return domain_Hz
    

#get fft of the sample frame
speechdry_1_fft = np.fft.rfft(speechdry_1)
speechdry_2_fft = np.fft.rfft(speechdry_2)
speechdry_3_fft = np.fft.rfft(speechdry_3)

speech20_1_fft = np.fft.rfft(speech20_1)
speech20_2_fft = np.fft.rfft(speech20_2)
speech20_3_fft = np.fft.rfft(speech20_3)

#get power spectra
speechdry_1_spect = abs(speechdry_1_fft**2)
speechdry_2_spect = abs(speechdry_2_fft**2)
speechdry_3_spect = abs(speechdry_3_fft**2)

speech20_1_spect = abs(speech20_1_fft**2)
speech20_2_spect = abs(speech20_2_fft**2)
speech20_3_spect = abs(speech20_3_fft**2)

#get frequency domain in hz (cycles per second)
speechdry_1_Hz = get_domain_Hz(speechdry_1_spect, wv2.speechdry_rate)
speechdry_2_Hz = get_domain_Hz(speechdry_2_spect, wv2.speechdry_rate)
speechdry_3_Hz = get_domain_Hz(speechdry_3_spect, wv2.speechdry_rate)

speech20_1_Hz = get_domain_Hz(speech20_1_spect, wv2.speech20_rate)
speech20_2_Hz = get_domain_Hz(speech20_2_spect, wv2.speech20_rate)
speech20_3_Hz = get_domain_Hz(speech20_3_spect, wv2.speech20_rate)
"""
Define the fourier transfomr sequence of the auto-correlation of each frame.
These are the spectra of the frame-wise auto-correlations.
"""
#get fft of the auto correlation
speechdry_1_auto_fft = np.fft.rfft(speechdry_1_auto[int(len(speechdry_1_auto)/2):len(speechdry_1_auto)])
speechdry_2_auto_fft = np.fft.rfft(speechdry_2_auto)
speechdry_3_auto_fft = np.fft.rfft(speechdry_3_auto)
#get power spectra
speechdry_1_auto_spect = abs(speechdry_1_auto_fft**2)
speechdry_2_auto_spect = abs(speechdry_2_auto_fft**2)
speechdry_3_auto_spect = abs(speechdry_3_auto_fft**2)
#get frequency domain in hz (cycles per second)
speechdry_1_auto_Hz = get_domain_Hz(speechdry_1_auto_spect, wv2.speech20_rate)
speechdry_2_auto_Hz = get_domain_Hz(speechdry_2_auto_spect, wv2.speech20_rate)
speechdry_3_auto_Hz = get_domain_Hz(speechdry_3_auto_spect, wv2.speech20_rate)

"""
______________________+++++++++Plots begin below+++++++++++____________________
"""

"""
########### Plot the raw sounds ############
"""

plt.figure()
plt.plot(speechdry_domain_s, wv2.speechdry_sound)
plt.plot(speechdry_domain_s[speechdry_frames[0][0]:speechdry_frames[0][1]],
         speechdry_1, label="frame 1")
plt.plot(speechdry_domain_s[speechdry_frames[1][0]:speechdry_frames[1][1]],
         speechdry_2, label="frame 2")
plt.plot(speechdry_domain_s[speechdry_frames[2][0]:speechdry_frames[2][1]],
         speechdry_3, label="frame 3")
plt.xlabel("time domain (seconds)")
plt.ylabel("sound pressure")
plt.title("Dry speech sample")
plt.legend(loc = "upper right")

plt.figure()
plt.plot(speech20_domain_s, wv2.speech20_sound)
plt.plot(speech20_domain_s[speech20_frames[0][0]:speech20_frames[0][1]],
         speech20_1, label="frame 1")
plt.plot(speech20_domain_s[speech20_frames[1][0]:speech20_frames[1][1]],
         speech20_2, label="frame 2")
plt.plot(speech20_domain_s[speech20_frames[2][0]:speech20_frames[2][1]],
         speech20_3, label="frame 3")
plt.xlabel("time domain (seconds)")
plt.ylabel("sound pressure")
plt.title("Reverbated speech sample")
plt.legend(loc = "upper right")

#plt.figure()
#plt.plot()
#plt.xlabel()
#plt.ylabel()
#plt.title()

"""
########## Plot the raw frames and their triangularized forms ##########

note: This is for demonstration purposed, not for finding fundamental frequency information,
    so one frame should suffice
"""
plt.figure()
plt.plot(get_domain_s(speechdry_1, wv2.speechdry_rate), speechdry_1, label = "nontriangularized")
plt.plot(get_domain_s(speechdry_1, wv2.speechdry_rate), speechdry_1_tr, label = "triangularized")
plt.title("Triangularized vs non-Triangularized frame 1 for Dry speech")
plt.legend(loc = "upper right")
plt.xlabel("time domain (seconds)")
plt.ylabel("Sound pressure")

"""
########## Plot the autocorrelation of each frame ##########
"""

#nontriangularized:
plt.figure()
plt.plot(speechdry_1_auto_domain_s, speechdry_1_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Dry speech sample: Frame 1")

plt.figure()
plt.plot(speechdry_2_auto_domain_s, speechdry_2_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Dry speech sample: Frame 2")

plt.figure()
plt.plot(speechdry_3_auto_domain_s, speechdry_3_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Dry speech sample: Frame 3")

plt.figure()
plt.plot(speech20_1_auto_domain_s, speech20_1_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Reverbated speech sample: Frame 1")

plt.figure()
plt.plot(speech20_2_auto_domain_s, speech20_2_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Reverbated speech sample: Frame 2")

plt.figure()
plt.plot(speech20_3_auto_domain_s, speech20_3_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Reverbated speech sample: Frame 3")

#triangularized:

plt.figure()
plt.plot(speechdry_1_auto_domain_s, speechdry_1_tr_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Dry speech sample: Frame 1, triangularized")

plt.figure()
plt.plot(speechdry_2_auto_domain_s, speechdry_2_tr_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Dry speech sample: Frame 2, triangularized")

plt.figure()
plt.plot(speechdry_3_auto_domain_s, speechdry_3_tr_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Dry speech sample: Frame 3, triangularized")

plt.figure()
plt.plot(speech20_1_auto_domain_s, speech20_1_tr_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Reverbated speech sample: Frame 1, triangularized")

plt.figure()
plt.plot(speech20_2_auto_domain_s, speech20_2_tr_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Reverbated speech sample: Frame 2, triangularized")

plt.figure()
plt.plot(speech20_3_auto_domain_s, speech20_3_tr_auto)
plt.xlabel("time domain (seconds)")
plt.ylabel("Autocorrelation amplitude")
plt.title("Autocorrelation of Reverbated speech sample: Frame 3, triangularized")

"""
########## Plot the spectra ################
"""

plt.figure()
plt.plot(speechdry_1_Hz, speechdry_1_spect)
plt.xlabel("frequency domain (hertz)")
plt.ylabel("Frequency amplitude")
plt.title("Frequency spectrum of Dry speech sample: Frame 1")

plt.figure()
plt.plot(speechdry_2_Hz, speechdry_2_spect)
plt.xlabel("frequency domain (hertz)")
plt.ylabel("Frequency amplitude")
plt.title("Frequency spectrum of Dry speech sample: Frame 2")

plt.figure()
plt.plot(speechdry_3_Hz, speechdry_3_spect)
plt.xlabel("frequency domain (hertz)")
plt.ylabel("Frequency amplitude")
plt.title("Frequency spectrum of Dry speech sample: Frame 3")

plt.figure()
plt.plot(speech20_1_Hz, speech20_1_spect)
plt.xlabel("frequency domain (hertz)")
plt.ylabel("Frequency amplitude")
plt.title("Frequency spectrum of Reverbated speech sample: Frame 1")

plt.figure()
plt.plot(speech20_2_Hz, speech20_2_spect)
plt.xlabel("frequency domain (hertz)")
plt.ylabel("Frequency amplitude")
plt.title("Frequency spectrum of Reverbated speech sample: Frame 2")

plt.figure()
plt.plot(speech20_3_Hz, speech20_3_spect)
plt.xlabel("frequency domain (hertz)")
plt.ylabel("Frequency amplitude")
plt.title("Frequency spectrum of Reverbated speech sample: Frame 3")