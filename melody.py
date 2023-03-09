#AUTHOR: ALLISON MURDOCK
#MCGIll ID: 261009978

from note import Note

class Melody:
    
    def __init__(self, filename_song):
        
        f = open(filename_song, "r")
        
        f_contents = f.read().split("\n")
        self.title = f_contents[0]
        self.author = f_contents[1]
        self.notes = []
        
        repeat = False
        repeat_notes = []
        
        for note_str in f_contents[2:]:
            note_list = note_str.split()
            
            duration = float(note_list[0])
            pitch = note_list[1]
            octave = int(note_list[2])
            accidental = note_list[3].lower()
            repeat_value = note_list[4]
            
            if repeat_value == "true":
                
                if repeat == True: # repeat sequence is over
                    repeat = False
                    repeat_notes.append(Note(duration, pitch, octave, accidental))
                    self.notes += (repeat_notes * 2)
                    repeat_notes = []
                
                else: # begin a repeat sequence
                    repeat = True
                    repeat_notes.append(Note(duration, pitch, octave, accidental))
            
            elif repeat == True:
                repeat_notes.append(Note(duration, pitch, octave, accidental))
            
            else:
                self.notes.append(Note(duration, pitch, octave, accidental))
    
        f.close()
        
    def play(self, music_player):
        for note in self.notes:
            note.play(music_player)
            
    def get_total_duration(self):
        total_duration = 0.0
        
        for note in self.notes:
            total_duration += note.duration
        
        return total_duration
    
    def lower_octave(self):
        octaves_lowered = []
        
        for note in self.notes:
            octave_low = note.octave - 1
              
            if octave_low >= Note.OCTAVE_MIN:
                lowered_note = Note(note.duration, note.pitch, octave_low, note.accidental)
                octaves_lowered.append(lowered_note)
            else:
                return False
             
        self.notes = octaves_lowered
        return True
    
    def upper_octave(self):
        octaves_raised = []
        
        for note in self.notes:
            octave_high = note.octave + 1
              
            if octave_high <= Note.OCTAVE_MAX:
                raised_note = Note(note.duration, note.pitch, octave_high, note.accidental)
                octaves_raised.append(raised_note)
            else:
                return False
             
        self.notes = octaves_raised
        return True
    
    
    def change_tempo(self, speed):
        for note in self.notes:
            note.duration = note.duration * speed
        
        
            
            
            
        
    