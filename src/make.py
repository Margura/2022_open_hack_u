import os

from music21 import note, stream
from midi2audio import FluidSynth

def song_make(melody_li, base_li, len_li, midipath):
    s = stream.Score()
    melody_s = stream.Part()
    base_s = stream.Part()
    length = len(melody_li)
    for i in range(length) :
        melody_n = note.Note(melody_li[i])
        base_n = note.Note(base_li[i])
        melody_n.quarterLength = len_li[i]
        base_n.quarterLength = len_li[length - i - 1]
        melody_n.volume = 50
        base_n.volume = 30
        melody_s.append(melody_n)
        base_s.append(base_n)
    l1 = note.Note(melody_li[i], quarterLength=3)
    l2 = note.Note(base_li[i], quarterLength=3)
    l1.volume = 50
    l2.volume = 30
    melody_s.append(l1)
    base_s.append(l2)
    s.append(melody_s)
    s.append(base_s)
    s.write("midi", fp=midipath)
    
def mp3_make(directory, midipath) :
    fs = FluidSynth(sound_font='static/sound/piano.sf2')
    fs.midi_to_audio(midipath, os.path.join(directory, 'out.mp3'))