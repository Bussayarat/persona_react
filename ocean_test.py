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
    cnt = Counter(emo_set)
    anger = cnt['anger']
    sadness = cnt['sadness']
    joy = cnt['joy']
    disgust = cnt['disgust']
    surprise = cnt['surprise']
    trust = cnt['trust']
    fear = cnt['fear']
    anticipation = cnt['anticipation']
    # emo_set = [0,1,2,3,4,5,6,7]
    # emotions_set = ['anger','sadness','joy','disgust','surprise','trust','fear','anticipation'] #0.25
    # amount = len(message)
    mood = anger + sadness + joy + disgust + surprise+trust + fear
    if anticipation > mood:
        openness = 100/(joy + surprise + trust + (anticipation*2))
    else:
        openness = 'low'
    return openness

def c_ocean(amount, emo_set):
    cnt = Counter(emo_set)
    anger = cnt['anger']
    sadness = cnt['sadness']
    joy = cnt['joy']
    disgust = cnt['disgust']
    surprise = cnt['surprise']
    trust = cnt['trust']
    fear = cnt['fear']
    anticipation = cnt['anticipation']
    # amount = len(message)

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

def e_ocean(amount, emo_set):
    # amount = len(message)
    cnt = Counter(emo_set)
    anger = cnt['anger']
    sadness = cnt['sadness']
    joy = cnt['joy']
    disgust = cnt['disgust']
    surprise = cnt['surprise']
    trust = cnt['trust']
    fear = cnt['fear']
    anticipation = cnt['anticipation']

    if joy+trust+anticipation > sadness+fear+anger:
        anticipation/amount
        if anticipation > 0.5:
            # high > 70
            extraversion = 100/(joy+anticipation)
        else:
            # medium < 70, > 50 --> 0.7
            extraversion = (100/(joy+anticipation+surprise)) - 0.25
    else:
        extraversion = 'low'
    return extraversion

def a_ocean(emo_set):
    cnt = Counter(emo_set)
    anger = cnt['anger']
    sadness = cnt['sadness']
    joy = cnt['joy']
    disgust = cnt['disgust']
    surprise = cnt['surprise']
    trust = cnt['trust']
    fear = cnt['fear']
    anticipation = cnt['anticipation']

    if joy > disgust+anger:
        if 100/(joy+surprise) >= 1:
            # high > 70
            agreeableness = 100/((joy+trust+surprise)-(anger+sadness))
        else:
            # medium < 70, > 50 --> 0.7
            agreeableness = 100/joy+trust+surprise
    else:
        agreeableness = 'low'

    return agreeableness

def n_ocean(amount, emo_set):
    # amount = len(message)
    cnt = Counter(emo_set)
    anger = cnt['anger']
    sadness = cnt['sadness']
    joy = cnt['joy']
    disgust = cnt['disgust']
    surprise = cnt['surprise']
    trust = cnt['trust']
    fear = cnt['fear']
    anticipation = cnt['anticipation']

    if 100/(anger+sadness+joy+disgust+surprise+trust+fear+anticipation) <= 1:
        negative = anger+sadness+fear+disgust
        positive = joy+trust+anticipation+surprise
        if negative > positive:
            neuroticism = (positive+negative)/amount
        else:
            neuroticism = 100/(positive-negative)+1
    else:
        neuroticism = 'low'
    return neuroticism

test = ['แต่ละวันดูแย่มากโคตรแย่ของแย่', 'กระหายชัยชนะเกินไปก็เสียอารมณ์']

sum_emo = get_emotion_summary(test, emo_dict_2)
print("\n\n* sum emo is ",sum_emo)
print("\n\n+ count",Counter(sum_emo) )
print("\n\n+++++++++++++++++++ sum on sum is +++++++++++++++++++ \n\n", sum_emo)
