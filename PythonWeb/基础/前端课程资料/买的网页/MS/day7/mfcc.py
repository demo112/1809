# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import python_speech_features as sf  # 语音提取器
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

sample_rate, sigs, = wf.read('speeches/training/banana/banana04.wav')

mfcc = sf.mfcc(sigs, sample_rate)


print(mfcc)
mp.matshow(mfcc.T, cmap='jet', fignum="MFCC")
mp.title('MCFF')
mp.xlabel('Samle')
mp.ylabel('Feature')

mp.tick_params(which='both', top='False', labeltop='False',
               labelbottom='True', labelsize=10)

mp.show()
