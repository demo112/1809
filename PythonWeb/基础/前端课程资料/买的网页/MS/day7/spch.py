# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import python_speech_features as sf  # 语音提取器
import scipy.io.wavfile as wf  # wav文件读取
import matplotlib.pyplot as mp
import os
import warnings
import hmmlearn.hmm as hl  # 用于记录
category = DeprecationWarning
warnings.fileterwarnings('ignore', category=DeprecationWarning)


def search_speeches(directory, speeches):
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        raise IOError("The directory" + directory + 'does not exist')
    for entry in os.listdir(directory):  # 迭代器
        label = directory[directory.rfind(os.path.sep) + 1:]
        print(label)
        path = os.path.join(directory, entry)
        print('------')
        print(path)
        if os.path.isdir(path):
            search_speeches(path, speeches)
        elif os.path.isfile(path) and path.endswith('.wav'):
            if label not in speeches:
                speeches[label] = []
            speeches[label].append(path)

train_speech = {}
search_speeches('speeches/training', train_speech)
print(train_speech)
