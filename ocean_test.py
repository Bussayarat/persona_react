# -*- coding: utf-8 -*-

# connect google spreadsheet 
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# api_key = '***'
# api_secret = '***'
# access_token = '***'
# access_secret = '***'

# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']
# credentials = ServiceAccountCredentials.from_json_keyfile_name('XXX.json', scope)
# # client = gspread.authorize(credentials)
# gc = gspread.authorize(credentials)
# sh = gc.open_by_url('xxxxxxx.com')
# esponse = sh.sheet_name.cell(x,y)
# d_solve = sh.sheet_name.get_all_values()

from collections import Counter
from pythainlp.tokenize import word_tokenize, WhitespaceTokenizer, sent_tokenize

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


def emotion_dict_transform(emo_dict):    
    return {text: key  for key, values in emo_dict.items() for text in values}


def get_emotion_in_text(text, emotion_dict):
    text = word_tokenize(text, engine='newmm')
    emotion = [emotion_dict[word] for word in text if word in emotion_dict.keys()]
    return emotion

def get_emotion_summary(message_list, emotion_dict):
    emotion_dict = emotion_dict_transform(emotion_dict)
    summary = []
    for text in message_list:
        summary += get_emotion_in_text(text, emotion_dict)
    return summary

def value_emotion(sum_emo):
    emotions_set = ['anger','sadness','joy','disgust','surprise','trust','fear','anticipation']
    emo_set = []
    or numb in range(0,7): #innitial = anger emotion_set[0]
        if not (sum_emo is None): #if in sum_emo have None ,will pass None
            if emotions_set[numb] in str(sum_emo):
                emo = emotions_set[numb]
                count = Counter(sum_emo)
                no_emo = count[emo]
                exec("%s = %d" % (emo, no_emo))
                emo_set.append(emo)
            else:
                emo = emotions_set[numb]
                no_emo = 0
                exec("%s = %d" % (emo, no_emo))
                emo_set.append(emo)
    del sum_emo
    return(emo_set)

# def o_ocean(sum_emo, message):
#     emotion_set = ['anger','sadness', 'joy','disgust','surprise','trust','fear','anticipation']
#     cnt = Counter(sum_emo)
#     #print(cnt)
#     emo_set = []
#     for nunb in range(0,7):
#         if not (sum_emo is None):
#             # for key,value in count.items():
#             #     print(key)
#             #     print(value)
#             #     if not (key is None):
#             #         exec("%s = %d" % (key,value))
#             # x='buffalo'
#             # exec("%s = %d" % (x,2))
#             if x == sum_emo:
#                 exec(emo % sum_emo)
#             else:
#                 x = sum_emo[emotions[nunb]]
#         # emo_set.append(exec("%s = %d" % ((emotions[nunb],x))))
#         # ดึงเรื่อง emo เข้ามาคำนวณ อารมณ์หลากหลายเมื่อเทียบจากคำพูดทั้งหมดตัดเป็น %
#         # emo_set[nunb] = (100 * emo_set[nunb]) / message
#     #openness = joy + surprise + trust + sum_set

#     # ดูว่าอารมณ์หลากหลายไหม
#     # ตรวจว่าอารมณ์หลากหลายมั้ย + หา openness
#     # if state == 'stable' :
#     #     # พิสัยระหว่าง anticipation กับ อารมณ์ที่ไม่หลากหลาย(ตรงข้ามกับข้อแรก)
#     openness = abs(anticipation + x) / 2
#     return(openness)

test = ['แต่ละวันดูแย่มากโคตรแย่ของแย่', 'กระหายชัยชนะเกินไปก็เสียอารมณ์']

sum_emo = get_emotion_summary(test, emo_dict_2)
print("\n\n* sum emo is ",sum_emo)
print("\n\n+ count",Counter(sum_emo) )
print("\n\n+++++++++++++++++++ sum on sum is +++++++++++++++++++ \n\n", sum_emo)

# o_ocean(sum_emo)


# print(dict(count))
# print(dict(count)['anger'])
# print(list(count))
# print(set(count))

# print(sum_emo)
# x = sum_emo[emotions[nunb]] #เฉพาะคำที่ emotions[x] สมมติว่าเป็น anger = x
# print(x)
# print(sum_emo)
# print(count)
# x = count['anger']
# print(x)
# o_ocean(sum_emo,2)
# o_ocean(count,2)

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



