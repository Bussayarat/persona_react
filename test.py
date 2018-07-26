# -*- coding: utf-8 -*-
# import tweepy, json, csv, gspread, re, string, wordlists
# import collections
# import numpy as np
from collections import Counter
from pythainlp.tokenize import word_tokenize, WhitespaceTokenizer, sent_tokenize

# for radar chart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection

# for testing
emo_dict = {
'anger' : ['แย่'], 'anger' : ['โคตร'],
'sadness' : ['แต่ละวัน'], 'sad' : ['แต่'],
'joy' : ['ดู'], 'joy' : ['มาก'],
'disgust' : ['แหวะ'], 'disgust' : ['ไม่'],
'surprise' : ['เอ']}

emo_dict_2 = {
'anger' : ['แย่','โคตร'],
'sadness' : ['แต่ละวัน','แต่'],
'joy' : ['ดู','มาก'],
'disgust' : ['แหวะ','ไม่'],
'surprise' : ['เอ']
}

def search_emotoins(dict, lookup):
    for key, value in dict.items():
        for word in value: #for ตัวแปรหนึ่งที่สร้างขึ้นมาเพื่อนวนลูป
            if lookup in word: #สำหรับคำ
                return key

example = 'แต่ละวันดูแย่มากโคตรแย่ของแย่' #ทดลองแยกอารมณ์จาก 1 ประโยค
example = word_tokenize(example, engine='newmm') # ['แต่ละ','วัน','ดู','แย่','มาก']
print(example)
len_word = len(example) # len_word = 5
print(len_word)
sum_emo = []
print (emo_dict_2)

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
