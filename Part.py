

class Part:
    def __init__(self, bpm, cells_per_beat, part_length) -> None:
        self.bpm = bpm
        self.cells_per_beat = cells_per_beat
        self.part_length = part_length
        
        self.notes = []

    def add_note(self, note_id, note_length, v, a, d, s, r, hp, hpm, lp, lpm):
        self.notes.append((note_id, note_length, v, a, d, s, r, hp, hpm, lp, lpm))
        
