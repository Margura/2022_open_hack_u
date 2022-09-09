import os
import cv2

def read_image(directory, filename) :
    img = cv2.imread(os.path.join(directory, filename))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return img

def resize_image(img) :
    size = min(len(img), len(img[0]))
    img = cv2.resize(img, dsize=(size, size), interpolation=cv2.INTER_CUBIC)
    img = cv2.resize(img, dsize=(5, 5), interpolation=cv2.INTER_CUBIC)
    return img
    
def split_image(img) :
    h_img = []
    s_img = []
    v_img = []
    for row in img :
        for pixel in row :
            h_img.append(pixel[0])
            s_img.append(pixel[1])
            v_img.append(pixel[2])
    return h_img, s_img, v_img
