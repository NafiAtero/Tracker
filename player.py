import pyaudio
from tone import generate_tone
from mixer import combine_tracks


def play_samples(samples, volume=0.2, sample_rate=44100):
    p = pyaudio.PyAudio()
    sample_rate = 44100  # sampling rate, Hz, must be integer

    # per @yahweh comment explicitly convert to bytes sequence
    output_bytes = (volume * samples).tobytes()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    stream.write(output_bytes)
    
    stream.stop_stream()
    stream.close()

    p.terminate()

print("generating tones")
a = generate_tone(69, 2, a=0.1, d=0.2, r=0.5, wave="square")
b = generate_tone(71, 1, a=0.1, d=0.2, r=0.5)
c = generate_tone(72, 1, a=0.1, d=0.2, r=0.5)
d = generate_tone(74, 1, a=0.1, d=0.2, r=0.5)
e = generate_tone(76, 2, a=0.1, d=0.2, r=0.5)
print("tones generated")

print("combining tracks")
#master = combine_tracks([a, c, e])
print("tracks combined")

print("playing")
play_samples(a)
print("finished playing")