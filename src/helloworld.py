import os

import torch
import torchaudio
import numpy as np

A = 0.5    # 振幅
f = 1000.0    # 周波数 Hz
sec = 3.0  # 信号の長さ s
sf = 44100 # サンプリング周波数 Hz
FOLDER = "/tmp"

def helloworld():
    t = torch.arange(0, sec, 1/sf) #サンプリング点の生成
    y = A*torch.sin(2*np.pi*f*t) # 正弦波の生成
    y = y.reshape(1,len(t))
    torchaudio.save(filepath=os.path.join(FOLDER, "helloworld.mp3"), src=y, sample_rate=sf, format='mp3')

if __name__ == "__main__" :
    helloworld()