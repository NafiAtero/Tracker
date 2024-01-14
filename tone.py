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

def all_pass_filter(input_sample, delayed_sample, target_freq):
    tan = np.tan(np.pi * target_freq / sample_rate)
    a1 = (tan - 1) / (tan + 1)
    output_sample = a1 * input_sample + delayed_sample
    delayed_sample = input_sample - a1 * output_sample
    return output_sample, delayed_sample
    

def generate_tone(note, duration, a=0.005, d=0.005, s=0.8, r=0.010, wave="sine"):
    sample_count = int(round((duration + r) * sample_rate))
    samples = np.zeros(sample_count, dtype=np.float32)
    amp = 0
    freq = get_note_freq(note)
    clipping = 0
    hpf_sample = 0
    lpf_sample = 0
    
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
            
        lpf_output, lpf_sample = all_pass_filter(sample, lpf_sample, freq*2)
        hpf_output, hpf_sample = all_pass_filter(sample, hpf_sample, freq*0.5)
        
        sample += lpf_output
        sample -= hpf_output
        sample /= 2
            
        if sample > 1: 
            clipping = max(clipping, sample - 1)
            sample = 1
        elif sample < -1: 
            clipping = max(clipping, -(1 + sample))
            sample = -1
        
        samples[i] = sample
    
    if clipping != 0: print("!!CLIPPING!!", clipping)
    return samples

