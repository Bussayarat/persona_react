# -*- coding: utf-8 -*-
import tweepy, json, csv, gspread, re, string, wordlists
# import collections
import numpy as np
from collections import Counter
from tweepy import Stream, OAuthHandler
# from pythainlp import word_tokenize
from pythainlp.word_vector import thai2vec
from pythainlp.rank import rank
from oauth2client.service_account import ServiceAccountCredentials
from tweepy.streaming import StreamListener
from pythainlp.collation import collation
from pythainlp.sentiment import sentiment
from pythainlp.tokenize import word_tokenize, WhitespaceTokenizer, sent_tokenize

emo_dict = {
'anger' : ['แย่'], 'anger' : ['โคตร'],
'sadness' : ['แต่ละวัน'], 'sad' : ['แต่'],
'joy' : ['ดู'], 'joy' : ['มาก'],
'disgust' : ['แหวะ'], 'disgust' : ['ไม่'],
'surprise' : ['เอ']}
# 'น่ากลัว' : 'fear', 'อึมครึม' : 'fear',
# 'เชื่อดิ' : 'trust', 'แน่นอน' : 'trust',
# 'พยายาม' : 'anticipation', 'อีกนิดเดียว' : 'anticipation'
# }
emo_dict_2 = {
'anger' : ['แย่','โคตร'],
'sadness' : ['แต่ละวัน','แต่'],
'joy' : ['ดู','มาก'],
'disgust' : ['แหวะ','ไม่'],
'surprise' : ['เอ']
}

# emo_sict_3 = {}
# def search(name):
#     for p in myDict:
#         if p['name'] == name:
#             return p
#
# search("ไม่")
# ตัดคำไม่มี mood ออกแล้วหา emotions
def search_emotoins(dict, lookup):
    for key, value in dict.items():
        for word in value: #for ตัวแปรหนึ่งที่สร้างขึ้นมาเพื่อนวนลูป
            if lookup in word: #สำหรับคำ
                return key
#             else:
#                 return lookup

# def search(myDict, lookup):
#     for key, value in myDict.items():
#         for v in value:
#             if lookup in v:
#                 return key


# def search(values, searchFor):
#     for k in values:
#         for v in values[k]:
#             if searchFor in v:
#                 return k
#     return Noner
#
# def search_dictionary(emodict, lookup):
#     for emotion, word in emodict.items():
#         if word == lookup:
#             return  emotion
#
#
# def search(myDict, lookup):
#     for key, value in myDict.items():
#         for v in value:
#             if lookup in v:
#                 return key

# dictionary = {'george' : 16, 'amber' : 19}
# search_age = raw_input("Provide age")
# for age in dictionary.values():
#     if age == search_age:
#         name = dictionary[age]
#         print name

#แก้เป็นอันล่าง
# for name, age in list.iteritems():    # for name, age in list.items():  (for Python 3.x)
#     if age == search_age:
#         print name


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
    # emotion = search(emo_dict, word)
    print(emotion)
    # e0 =search(word,)
    # def search_emotoins(emo_dict, lookup)
    sum_emo.append(emotion)
    print(word)
# def check_e_set
print (sum_emo)

def emo_set(sum_emo):
    cou
