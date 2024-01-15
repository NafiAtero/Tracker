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
#a = generate_tone(69, 2, a=0.01, d=0.02, r=0.1, wave="sine")
b = generate_tone(69, 2, a=0.01, d=0.02, r=0.1, wave="square")
#c = generate_tone(69, 2, a=0.01, d=0.02, r=0.1, wave="tri")
#d = generate_tone(69, 2, a=0.01, d=0.02, r=0.1, wave="saw")
e = generate_tone(20, 2, a=0.01, d=0.02, r=0.1, wave="noise")
print("tones generated")

print("combining tracks")
#master = combine_tracks([a, c, e])
print("tracks combined")

print("playing")
#play_samples(a)
#play_samples(b)
#play_samples(c)
#play_samples(d)
play_samples(e)
print("finished playing")