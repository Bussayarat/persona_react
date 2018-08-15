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

#
# def set_value(count):
#     for key,value in count.items():
#         print(key)
#         print(value)
#         if not (key is None):
#             exec("%s = %d" % (key,value))

def search_dict(dict, lookup):
    for label, words in dict.items():
        for word in words:
            if lookup in word:
                return label

def o_ocean(all_emo, amount_tweet): # all_emo = sum_emo (array of emotions)
    emotions = ['anger','sadness','joy','disgust','surprise','trust','fear','anticipation']
    cnt = Counter(all_emo) #จากทุก tweet หาค่าที่ซ้ำกันเพื่อดูว่าแต่ละอารมณ์มีค่าเท่าไหร่ 2 3 4 5 6
    emo_set = [] #เก็บค่าจาก append
    # all_emo = ['sadness', 'joy', None, 'anger', 'anger', None, 'anger']

    for nunb in range(0,7):
        if not (all_emo is None):
            # for key,value in count.items():
            #     print(key)
            #     print(value)
            #     if not (key is None):
            #         exec("%s = %d" % (key,value))
            # x='buffalo'
            # exec("%s = %d" % (x,2))
            x = (cnt[emotions[nunb]])
            emo_set.append(exec("%s = %d" % (x,(cnt[emotions[nunb]]))))
            # ดึงเรื่อง emo เข้ามาคำนวณ อารมณ์หลากหลายเมื่อเทียบจากคำพูดทั้งหมดตัดเป็น %
            emo_set[nunb] = (100 * emo_set[nunb]) / amount_tweet
    openness = joy + surprise + trust + (anticipation*2)
    # # ดูว่าอารมณ์หลากหลายไหม
    #
    # # ตรวจว่าอารมณ์หลากหลายมั้ย + หา openness
    # if state == 'stable' :
    #     # พิสัยระหว่าง anticipation กับ อารมณ์ที่ไม่หลากหลาย(ตรงข้ามกับข้อแรก)
    #     openness = abs(anticipation + ) / 2
    #     return(openness)
    # else:
    #     openness =
    #     return(openness)
    return(openness)

# def c_ocean():
#     # พิสัยระหว่างความมีประสิทธิภาพ-ความเป็นคนมีระเบียบ กับความเป็นคนสบาย ๆ-ความเป็นคนไร้กังวล
#     return(range)
#
# def e_ocean():
#     # พิสัยระหว่างคนเปิดรับสังคม-คนกระตือรือร้น กับคนชอบอยู่คนเดียว-คนสงวนท่าที
#     return(range)
#
# def a_ocean():
#     # พิสัยระหว่างความเป็นมิตร-เห็นอกเห็นใจผู้อื่น กับความเป็นคนช่างวิเคราะห์-ไม่ค่อยยุ่งกับผู้อื่น
#     return(range)
#
# def n_ocean(emo, behavr_dict):
#     # ความไม่เสถียรทางอารมณ์ ดึงเรื่อง อารมณ์เข้ามาคำนวณหาความถี่
#     # เช็คค่าความแปรผันทางอารมณ์
#
# def behaviour_analysis(emotions):
#     # กลัว ปกป้อง
#     # โกรธ ทำลาย
#     # รื่นเริง ให้ความร่วมมมือ
#     # รังเกียจ ปฏิเสธ
#     # เศร้า พยายามรักษาความรู้สึก
#     #  ประหลาดใจ พยายามปรับตัวเข้ากับสภาพแวดล้อมใหม่
#     # คาดหวัง(อยากรู้อยากเห็น) สำรวจค้นหา

# just for debug
emo_dict_2 = {
'anger' : ['แย่','โคตร','กระหาย','ซ้ำเติม'],
'sadness' : ['แต่ละวัน','แต่','น้ำตา'],
'joy' : ['ดู','มาก','สนุก','ชอบ'],
'disgust' : ['แหวะ','ไม่','เกลียด','เสือก'],
'surprise' : ['เอ'],
'trust' : ['ดี'],
'fear' : ['ตาย'],
'anticipation' : ['อร่อย','คาดหวัง']
}
test = ['แต่ละวันดูแย่มากโคตรแย่ของแย่','กระหายชัยชนะเกินไปก็เสียอารมณ์ ทำอะไรเอาแค่สนุกๆก็โอเคละ']


# example = 'แต่ละวันดูแย่มากโคตรแย่ของแย่'
# # ex2 = 'ทำอะไรแบบนี้.......มันดูแย่นะ'
# example = word_tokenize(example, engine='newmm')
# # ex2 = word_tokenize(ex2, engine='newmm')
# # print(example)
# # print(ex2)
# len_word = len(example)
# cnt = Counter(example)
# sum_emo = []

sum_emo = []
# ข้อความแบบ array [as,sd,fs]
for sent in range (0,32):
    example = word_t[sent]
    example = word_tokenize(example, engine='newmm')
    len_word = len(example)
    cnt = Counter(example)

    for count in range (0, len_word):
        word = example[count]
        emotion = search_dict(emo_dict_2, word)
        sum_emo.append(emotion)
count = Counter(sum_emo)
dict(count)
list(count)
set(count)
print(sum_emo)
print(count)
o_ocean(sum_emo,33)

# behavr_dict = {
# 'anger' : 'ทำลาย',
# 'sadness' : 'รักษาความรู้สึก',
# 'joy' : 'ให้ความร่วมมือ',
# 'disgust' : 'ปฏิเสธ',
# 'surprise' : 'ปรับตัว',
# 'anticipation' : 'หาคำตอบ',
# 'fear' : 'ปกป้อง',
# 'trust' : 'ยอมรับ',
# }

# anger , sad, anger, joy, anticipation
# list(collections.Counter(('5', '5', '4', '5')).items())
# example = 'แต่ละวันดูแย่มากโคตรแย่ของแย่'
# ex2 = 'ทำอะไรแบบนี้.......มันดูแย่นะ'
# example = word_tokenize(example, engine='newmm')
# ex2 = word_tokenize(ex2, engine='newmm')
# print(example)
# print(ex2)
# len_word = len(example)
# cnt = Counter(example)
# print(cnt)
# sum_emo = []

# print(cnt)
# for count in range (0, len_word):
#     word = example[count]
#     emotion = search_dict(emo_dict_2, word)
#     sum_emo.append(emotion)
# count = Counter(sum_emo)
# dict(count)
# list(count)
# set(count)
# print(set(count))
# print(x)
# print('sum_emo is',sum_emo)
# print('count is',count)
# print('dict is',c)
# print(o_ocean(sum_emo,2))

# for key,value in count.items():
#     print(key)
#     print(value)
#     if not (key is None):
#         exec("%s = %d" % (key,value))
# print('anger =', anger)
# persona_react
