import numpy as np
import math
import random

sample_rate = 44100

def get_note_freq(n, base_freq=440, base_note=69):
    if n > 108 or n < 12: return base_freq
    return base_freq * (2 ** ((n - base_note) / 12))

def sine_wave(amp, freq, phase):
    return amp * math.sin(2 * math.pi * freq * phase)

def square_wave(amp, freq, phase):
    sample = sine_wave(amp, freq, phase)
    for i in range(3, 50, 2):
        sample += sine_wave(amp/i, freq*i, phase)
    return sample

def tri_wave(amp, freq, phase):
    sample = sine_wave(amp, freq, phase)
    for i in range(3, 50, 4):
        sample -= sine_wave(amp/(i**2), freq*i, phase)
        sample += sine_wave(amp/((i+2)**2), freq*(i+2), phase)
    return sample

def saw_wave(amp, freq, phase):
    sample = sine_wave(amp, freq, phase)
    for i in range(2, 50):
        sample += sine_wave(amp/i, freq*i, phase)
    return sample

def noise(amp):
    return random.randrange(-1, 1) * amp

def generate_tone(note, duration, a=0.005, d=0.005, s=0.8, r=0.010, wave="sine"):
    sample_count = int(round((duration + r) * sample_rate))
    samples = np.zeros(sample_count, dtype=np.float32)
    amp = 0
    freq = get_note_freq(note)
    clipping = False
    
    for i in range(sample_count):
        t = i / sample_rate
        
        if t < a:           # attack
            amp = t / a
        elif t < d:         # todo decay
            amp = (((a + d) - t) / d) * (1 - s) + s
        elif t > duration:  # release
            amp = (((duration + r) - t) / r) * s
        else:               # sustain
            amp = s
           
        sample = 0
        if wave == "sine":
            sample = sine_wave(amp, freq, t)
        elif wave == "square":
            sample = square_wave(amp, freq, t)
        elif wave == "tri":
            sample = tri_wave(amp, freq, t)
        elif wave == "saw":
            sample = saw_wave(amp, freq, t)
        elif wave == "noise":
            sample = noise(amp)
            
        if sample > 1: 
            clipping == True
            sample = 1
        elif sample < -1: 
            clipping == True
            sample = -1
        
        samples[i] = sample
    
    if clipping: print("clipping")
    return samples

