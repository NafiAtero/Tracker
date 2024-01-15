from Track import Track
from Part import Part
from utils import combine_tracks

class Music:
    def __init__(self) -> None:
        self.tracks = []
        self.tracks.append(Track("sine"))
        self.tracks.append(Track("sine"))
        self.tracks.append(Track("square"))
        self.tracks.append(Track("square"))
        self.tracks.append(Track("tri"))
        self.tracks.append(Track("saw"))
        self.tracks.append(Track("noise"))
        self.tracks.append(Track("noise"))
        
        self.parts = []
        self.sequences = []
        
    # todo
    def add_part(self):
        new_part = Part()
        self.parts.append(new_part)
        
    def add_sequence(self, bpm, cells_per_beat, length, t1p, t1v, t2p, t2v, t3p, t3v, t4p, t4v, t5p, t5v, t6p, t6v, t7p, t7v, t8p, t8v):
        self.sequences.append(bpm, cells_per_beat, length, [t1p, t1v, t2p, t2v, t3p, t3v, t4p, t4v, t5p, t5v, t6p, t6v, t7p, t7v, t8p, t8v])
        
    def get_music_samples(self):
        for sequence in self.sequences:
            for i in range(len(self.tracks)):
                track = self.tracks[i]
                track.add_part(sequence[0], sequence[1], sequence[2], sequence[3][i*2], sequence[3][i*2+1])
        
        track_samples = []
        for track in self.tracks:
            track_samples.append(track.get_track_samples())
        
        return combine_tracks(track_samples)
        