# -*- coding: utf-8 -*-
from collections import Counter
from pythainlp.tokenize import word_tokenize, WhitespaceTokenizer, sent_tokenize

# for radar chart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection

# just for debug code
emo_dict_2 = {
'anger' : ['แย่','โคตร'],
'sadness' : ['แต่ละวัน','แต่'],
'joy' : ['ดู','มาก'],
'disgust' : ['แหวะ','ไม่'],
'surprise' : ['เอ']
}

example = 'แต่ละวันดูแย่มากโคตรแย่ของแย่'
example = word_tokenize(example, engine='newmm')
len_word = len(example)
sum_emo = []
for count in range (0, len_word):
    word = example[count]
    print(count)
    emotion = search_emotoins(emo_dict_2, word)
    print(emotion)
    sum_emo.append(emotion)
    print(word)

print (sum_emo) # ['sadness', 'joy', None, 'anger', 'anger', None, 'anger']
count = Counter(sum_emo)
print(count) #debug
print('anger = ',dict(count)['anger'])
# ใน 1% จะมีผลทางอารมณ์แต่ละด้านเป็นเท่าไหร่
# 100% คือทั้งหมดรวมกันเป็นคะแนนดิบ  5 6 7 8 ...
# ถ้ามี anger 5 sad 7 happy 6 trust 1 , 1% = 19 --> 5/19 = ?%


def search_emotoins(dict, lookup):
    for key, value in dict.items():
        for word in value:
            if lookup in word:
                return key

def cal_emo(emo_list):
    if anger = 0, fear =0 , glade = 0 :
        print (mood)
