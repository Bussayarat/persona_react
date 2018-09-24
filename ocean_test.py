# -*- coding: utf-8 -*-

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

def emotion_value(sum_emo):
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

def o_ocean(emo_set):
    # emotions_set = ['anger','sadness','joy','disgust','surprise','trust','fear','anticipation'] #0.25
    # amount = len(message)
    if anticipation > anger+sadness+joy+disgust+surprise+trust+fear:
        openness = 100/(joy + surprise + trust + (anticipation*2))
    else:
        openness = 'low'
    return openness

def c_ocean(message, emo_set):
    amount = len(message)
    # พิสัยระหว่างความีระเบียบ กับความไร้กังวล โน้มเอียงที่จะเป็นคนเจ้าระเบียบที่เชื่อถือได้ 
    # มีวินัย ชอบใจพฤติกรรมตามแผนมากกว่าจะทำอะไรแบบทันทีทันใด 
    # ดื้อและหมกมุ่น 
    # และคนที่มีลักษณะเช่นนี้ต่ำแม้จะยืดหยุ่นได้และทำอะไรได้โดยไม่ต้องคิด แต่ก็อาจมองได้ว่าเป็นคนไม่เอาใจใส่และเชื่อถือไม่ได้
    if surprise+anticipation < trust:
        if 100/(joy+trust/amount) > 0.5:
            # high > 70
            conscientiousness = 100/((joy+trust)-(surprise+anticipation))
        else:
            # medium < 70, > 50 --> 0.7
            conscientiousness = (100/(joy+trust))-0.5
    else:
        conscientiousness = 'low'
    return conscientiousness

def e_ocean(message, mo_set):
    amount = len(message)
    # โดยเป็นพิสัยระหว่างคนเปิดรับสังคม-คนกระตือรือร้น 
    # กับคนชอบอยู่คนเดียว-คนสงวนท่าที เป็นพลัง อารมณ์เชิงบวก surgency 
    # ความมั่นใจในตน ความชอบเข้าสังคม และความโน้มเอียงที่จะสืบหาสิ่งเร้าร่วมกับผู้อื่น และชอบพูด 
    # ลักษณะนี้ต่ำ เป็นคนคิดเยอะ
    
    if joy+trust+anticipation > sadness+fear+anger:
        anticipation/amount
        if anticipation > 0.5:
            # high > 70
            extraversion = 100/(joy+anticipation))
        else:
            # medium < 70, > 50 --> 0.7
            extraversion = (100/(joy+anticipation+surprise)) - 0.25
    else:
        extraversion = 'low'
    return extraversion

test = ['แต่ละวันดูแย่มากโคตรแย่ของแย่', 'กระหายชัยชนะเกินไปก็เสียอารมณ์']

sum_emo = get_emotion_summary(test, emo_dict_2)
print("\n\n* sum emo is ",sum_emo)
print("\n\n+ count",Counter(sum_emo) )
print("\n\n+++++++++++++++++++ sum on sum is +++++++++++++++++++ \n\n", sum_emo)
