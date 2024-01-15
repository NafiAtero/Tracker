

class Part:
    def __init__(self) -> None:
        
        self.notes = []

    def add_note(self, note_id, note_length, v, a, d, s, r, hp, hpm, lp, lpm):
        self.notes.append((note_id, note_length, v, a, d, s, r, hp, hpm, lp, lpm))
        
