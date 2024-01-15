import numpy as np

sample_rate = 44100

class Track:
    def __init__(self, wave) -> None:
        self.wave = wave
        self.parts = []
        
    def add_part(self, bpm, cells_per_beat, length, part, volume):
        self.parts.append((part, bpm, cells_per_beat, length))
        
        
    def get_track_samples(self):
        pass
        #cell_length = 60 / (bpm  * cells_per_beat)
        #sample_count = cell_length * length * sample_rate
        #samples = np.zeros(sample_count, dtype=np.float32)
    