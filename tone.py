import numpy as np
import math

sample_rate = 44100

def get_note_freq(n, base_freq=440, base_note=69):
    if n > 108 or n < 0: return base_freq
    return base_freq * (2 ** ((n - base_note) / 12))

def sine_wave(amp, freq, phase):
    return amp * math.sin(2 * math.pi * freq * phase)

def square_wave(amp, freq, phase):
    sine = sine_wave(amp, freq, phase)
    for i in range(3, 50, 2):
        sine += sine_wave(amp/i, freq*i, phase)
    return sine

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
            
        if wave == "sine":
            sample = sine_wave(amp, freq, t)
        elif wave == "square":
            sample = square_wave(amp, freq, t)
            
        if sample > 1: 
            clipping == True
            sample = 1
        elif sample < -1: 
            clipping == True
            sample = -1
        
        samples[i] = sample
    
    if clipping: print("clipping")
    return samples

