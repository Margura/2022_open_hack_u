import os

from src.image import read_image, resize_image, split_image
from src.convert import h_img2melody_li, s_img2base_li, v_img2len_li
from src.make import song_make, mp3_make

def main(directory, filename) :
    midipath = os.path.join(directory, "out.midi")
    img = read_image(directory, filename)
    img = resize_image(img)
    h_img, s_img, v_img = split_image(img)
    melody_li = h_img2melody_li(h_img)
    base_li = s_img2base_li(s_img)
    len_li = v_img2len_li(v_img)
    song_make(melody_li, base_li, len_li, midipath)
    mp3_make(directory, midipath)