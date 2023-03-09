#AUTHOR: ALLISON MURDOCK
#MCGIll ID: 261009978

class Note:
    OCTAVE_MIN = 1
    OCTAVE_MAX = 7
    
    def __init__(self, duration, pitch, octave=1, accidental_value="natural"):
    
        if type(duration)!= float or duration <= 0:
            raise AssertionError("Invalid duration.")
        
        valid_pitches = ("A", "B", "C", "D", "E", "F", "G", "R")
        if pitch not in valid_pitches:
            raise AssertionError("Invalid pitch.")
        
        if type(octave) != int or not (1 <= octave <= 7 ):
            raise AssertionError("Invalid octave.")
        
        valid_accidental_value = ("sharp", "flat", "natural")
        if accidental_value not in valid_accidental_value:
            raise AssertionError("Invalid accidental_value.")
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental_value
        
        
    def play(self, music_player):
        if self.pitch == "R":
            note = "pause"
        else:
            note = self.pitch + str(self.octave)
            
            if self.accidental == "sharp":
                note += "#"
            elif self.accidental == "flat":
                note += "b"
            
        music_player.play_note(note, self.duration)
        
    def __str__(self):
        return (str(self.duration) + " " + self.pitch + " " + str(self.octave) + " " + self.accidental) 