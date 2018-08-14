# -*- coding: utf-8 -*-
from collections import Counter
from pythainlp.tokenize import word_tokenize, WhitespaceTokenizer, sent_tokenize

# for chart
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.path import Path
# from matplotlib.spines import Spine
# from matplotlib.projections.polar import PolarAxes
# from matplotlib.projections import register_projection

# cpltd
# def set2initial_value():
#
# def set_value(count):
#     for key,value in count.items():
#         print(key)
#         print(value)
#         if not (key is None):
#             exec("%s = %d" % (key,value))


def search_dict(dict, lookup):
    for key, value in dict.items():
        for word in value:
            if lookup in word:
                return key

# just for debug
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
    emotion = search_dict(emo_dict_2, word)
    sum_emo.append(emotion)
count = Counter(sum_emo)


for key,value in count.items():
    print(key)
    print(value)
    if not (key is None):
        exec("%s = %d" % (key,value))
# test_react
# persona_react
