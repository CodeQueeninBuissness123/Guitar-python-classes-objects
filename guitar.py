class Guitar:
    def __init__(self, chords):
        self.chords = chords

    def play_chords(self):
        for chord in self.chords:
            print(f"Playing chord: {chord}")

class BluesGuitar(Guitar):
    def __init__(self):
        super().__init__(["C", "E", "G", "A#", "D", "G"])

class JazzGuitar(Guitar):
    def __init__(self):
        super().__init__(["C", "C#", "D", "E", "F", "F#", "G", "G#", "A", "A#", "B"])

class RockGuitar(Guitar):
    def __init__(self):
        super().__init__(["C", "D", "E", "F", "G", "A", "B"])

# Usage example:
blues_guitar = BluesGuitar()
blues_guitar.play_chords()

jazz_guitar = JazzGuitar()
jazz_guitar.play_chords()

rock_guitar = RockGuitar()
rock_guitar.play_chords()
