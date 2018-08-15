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

    for nunb in range(0,7):
        if not (all_emo is None):
            # for key,value in count.items():
            #     print(key)
            #     print(value)
            #     if not (key is None):
            #         exec("%s = %d" % (key,value))
            # x='buffalo'
            # exec("%s = %d" % (x,2))
            x = (cnt[emotions[count]])
            emo_set.append(exec("%s = %d" % (x,(cnt[emotions[count]]))))
            # ดึงเรื่อง emo เข้ามาคำนวณ อารมณ์หลากหลายเมื่อเทียบจากคำพูดทั้งหมดตัดเป็น %
            emo_set[count] = (100 * emo_set[count]) / amount_tweet
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

# word_t = [
# 'กระหายชัยชนะเกินไปก็เสียอารมณ์ ทำอะไรเอาแค่สนุกๆก็โอเคละ',
# 'เกลียดกว่าการปลุกแบบปิดแอร์ คือเร่งแอร์ แล้วขโมยผ้าห่ม น้ำตาตะไหล',
# 'ของเทคของทุกคนในทีมอร่อยโคตร ถถถถถถ',
# 'ความบังเอิญสร้างได้ ถ้าเนียนพอ',
# 'คุณคาดหวังว่าจะได้อะไร ?',
# 'ชอบความเท่เวลาคอรัส เพิ่งรู้ว่าโมบายร้องเพราะโคตร',
# 'ชอบความเนื้อเพลงประชดประชันแบบเหงาๆ 5555',
# 'ชีวิตที่เลือกอะไรไม่ได้เลยนี่เศร้าเน้อ',
# 'ตอนเด็กๆมีแมวมีสามสี เลยตั้งชื่อว่าอีเหมียว',
# 'นานๆจะฝันร้ายซักที',
# 'เป็นประโยคเดียวจริงๆที่เราเชื่อมาจนถึงทุกวันนี้',
# 'ผมจะชวนเธอไปร้านหนังสือ',
# 'เพื่อนบอกมันต้องเป็นคนที่ให้ความรู้สึกเหมือนครอบครัว พร้อมให้อภัยกัน ไม่ใช่ซ้ำเติม',
# 'มันไม่มีประตูไหนที่เปิดแล้วมีความสุขเท่าประตูตู้เย็นที่บ้านละ',
# 'มึงให้เกียรติชีวิตมึงที่ใช้มาหน่อยดิว่ะ',
# 'เมื่อคุณชอบกินอาหารญี่ปุ่น แต่เพื่อนคุณเสือกแพ้แซลม่อน',
# 'รู้ว่ามันเป็นอะไรที่เจ็บ แต่ก็รู้ว่ามันยังเจ็บกว่านี้ได้อีก',
# 'เรื่องมันช่างน่าเศร้า',
# 'โลกความจริงมันเหนื่อยแท้',
# 'วันนี้มันดี เราเลยเลือกอยู่กับวันนี้มากกว่าเมื่อวาน หรือวันไหนๆในอนาคต',
# 'สมองจะแตก',
# 'เหมือนกูจะตายเร็วๆนี้ไงก็ไม่รู้',
# 'แก ยีนส์ไม่ได้ใส่สบายอะ555555555555555555555555555555',
# 'ความเด็กเปรตไม่เข้าใครออกใคร',
# 'คอมเม้นก็เสือกตลก 5555555555555',
# 'เครื่องรางความรักคงต้องเหมาเป็นกระสอบ',
# 'งงในงง',
# 'ชั้ลวัลเน้เห็นเม่กหม่อกรั้ยเข้ามาปวกคุมหัวจึย',
# 'เดี๋ยวจะหาว่าหล่อไม่เตือน 555555555555',
# 'แต่เพื่อนอยู่ยังอยู่กับเรา',
# 'แต่มีคนทำได้จริงๆนะ จำได้',
# 'แต่มึงดันไปโฟกัสจุดดำบนชีวิตมึงแค่จุดเดียวเองเนี่ยนะ',
# 'แต่แม่เราก็ซ้ำเติมพ่ออยู่บ่อยๆ ถถถถถถ']

# example = 'แต่ละวันดูแย่มากโคตรแย่ของแย่'
# # ex2 = 'ทำอะไรแบบนี้.......มันดูแย่นะ'
# example = word_tokenize(example, engine='newmm')
# # ex2 = word_tokenize(ex2, engine='newmm')
# # print(example)
# # print(ex2)
# len_word = len(example)
# cnt = Counter(example)
# sum_emo = []

# sum_emo = []
# # ข้อความแบบ array [as,sd,fs]
# for sent in range (0,32):
#     example = word_t[sent]
#     example = word_tokenize(example, engine='newmm')
#     len_word = len(example)
#     cnt = Counter(example)
#
#     for count in range (0, len_word):
#         word = example[count]
#         emotion = search_dict(emo_dict_2, word)
#         sum_emo.append(emotion)
# count = Counter(sum_emo)
# print(sum_emo)
# print(count)
# o_ocean(sum_emo,33)

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
example = 'แต่ละวันดูแย่มากโคตรแย่ของแย่'
ex2 = 'ทำอะไรแบบนี้.......มันดูแย่นะ'
example = word_tokenize(example, engine='newmm')
ex2 = word_tokenize(ex2, engine='newmm')
# print(example)
# print(ex2)
len_word = len(example)
cnt = Counter(example)
print(cnt)
sum_emo = []

# print(cnt)
for count in range (0, len_word):
    word = example[count]
    emotion = search_dict(emo_dict_2, word)
    sum_emo.append(emotion)
count = Counter(sum_emo)
c = dict(count)
x=list(count)
print(set(count))
print(x)
print('sum_emo is',sum_emo)
print('count is',count)
print('dict is',c)

for key,value in count.items():
    print(key)
    print(value)
    if not (key is None):
        exec("%s = %d" % (key,value))
print('anger =', anger)
