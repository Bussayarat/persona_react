

# import ocean_test
import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import Counter
import question_similaity
from pythainlp.tokenize import word_tokenize
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "cred.json", scope
)
gc = gspread.authorize(credentials)

emotion_default_url = "https://docs.google.com/spreadsheets/d/12ZvHgNWWPwf3kQ2HkZUO4edlGWvjjirrbICqVQ_mDaA/edit?usp=sharing"
q_ans_default_url = "https://docs.google.com/spreadsheets/d/1jT32XCs2xedvMvnVZZrHiBSbxWaJzlYNndK40udcQW8/edit?usp=sharing_eip&ts=5ba0b116"


question_answer = None
emotion_dict = None
find_similar = None


def get_question_answer(q_ans_link=q_ans_default_url):
    q_ans = gc.open_by_url(q_ans_link)
    q_ans_sheet = q_ans.worksheet("ZOCIAL EYE")
    q_ans = [q_ans_sheet.col_values(columns + 1)[1:] for columns in range(8)]
    question = [question for question in q_ans[1] if question != ""]
    faq = {}
    for num in range(len(question)):
        faq[question[num]] = {
            "x": q_ans[2][num],
            "o": q_ans[3][num],
            "c": q_ans[4][num],
            "e": q_ans[5][num],
            "a": q_ans[6][num],
            "n": q_ans[7][num],
        }
    return faq


def get_emotion_dict(dict_link=emotion_default_url):
    emotion_file = gc.open_by_url(dict_link)
    emotion_sheet = emotion_file.worksheet("emo")
    emotion_dict = {
        emotion[0]: emotion[1:]
        for emotion in [emotion_sheet.col_values(columns + 1) for columns in range(8)]
    }
    return {text: key for key, values in emotion_dict.items() for text in values}


def get_emotion_in_text(text, emotion_dict):
    text = word_tokenize(text, engine="newmm")
    emotion = [emotion_dict[word] for word in text if word in emotion_dict.keys()]
    return emotion


def get_emotion_summary(message_list, emotion_dict):
    summary = []
    for text in message_list:
        summary += get_emotion_in_text(text, emotion_dict)
    return summary


def get_ocean(emo_set):
    cnt = Counter(emo_set)
    anger = cnt["anger"]
    sadness = cnt["sadness"]
    joy = cnt["joy"]
    disgust = cnt["disgust"]
    surprise = cnt["surprise"]
    trust = cnt["trust"]
    fear = cnt["fear"]
    anticipation = cnt["anticipation"]

    amount = len(emo_set)

    sum_mood = anger + sadness + joy + disgust + surprise + trust + fear + anticipation

    if anticipation > sum_mood - anticipation:
        openness = 100 / (joy + surprise + trust + (anticipation * 2))
    else:
        openness = 0

    if surprise + anticipation < trust:
        if 100 / (joy + trust / amount) > 0.5:
            # high > 70
            conscientiousness = 100 / ((joy + trust) - (surprise + anticipation))
        else:
            # medium < 70, > 50 --> 0.7
            conscientiousness = (100 / (joy + trust)) - 0.5
    else:
        conscientiousness = 0

    if joy + trust + anticipation > sadness + fear + anger:
        anticipation / amount
        if anticipation > 0.5:
            # high > 70
            extraversion = 100 / (joy + anticipation)
        else:
            # medium < 70, > 50 --> 0.7
            extraversion = (100 / (joy + anticipation + surprise)) - 0.25
    else:
        extraversion = 0

    if joy > disgust + anger:
        if 100 / (joy + surprise) >= 1:
            # high > 70
            agreeableness = 100 / ((joy + trust + surprise) - (anger + sadness))
        else:
            # medium < 70, > 50 --> 0.7
            agreeableness = 100 / joy + trust + surprise
    else:
        agreeableness = 0

    if 100 / (sum_mood) <= 1:
        negative = anger + sadness + fear + disgust
        positive = joy + trust + anticipation + surprise
        if negative > positive:
            neuroticism = (positive + negative) / amount
        else:
            neuroticism = 100 / (positive - negative) + 1
    else:
        neuroticism = 0

    return openness, conscientiousness, extraversion, agreeableness, neuroticism


def personality(o, c, e, a, n):
    max_ocean = max([o, c, e, a, n])

    if o != 0 and e != 0:
        if any([max_ocean == o, max_ocean == e]):
            p_per = o + e
            e_per = o + e
            first_op = 'e'
        else:
            if all([max_ocean == c, a > o, a > e, a > n]):
                i_per = a + c
                first_op = 'i'
            else:
                if i_per - e_per > 0:
                    first_op = 'i'
                else:
                    first_op = 'e'
    else:
        first_op = 'i'

    # check T or F
    if all([max_ocean == c, a == 0]):
        second_op = 't'
    else:
        second_op = 'f'

    # check J or P
    if all([o != 0, e != 0, n == 0]):
        third_op = 'p'
    else:
        if max_ocean == c:
            third_op = 'j'
        else:
            if any([max_ocean == o, max_ocean == e]):
                third_op = 'p'
            else:
                third_op = 'j'

    # check S or N
    if all([max_ocean == c, o != 0, n == 0]):
        fourth_op = 's'
    else:
        fourth_op = 'n'

    return first_op, second_op, third_op, fourth_op


def get_response(message, ans_type):
    global question_answer
    global find_similar
    if question_answer == None:
        question_answer = get_question_answer()
        find_similar = question_similaity.similarity(list(question_answer.keys()))
    # print(message)
    question = find_similar.get_similarity(message, theshold=0.3)
    if question:
        response = question_answer[question][ans_type]
    else:
        question = "ไม่พบคำถามที่ใกล้เคียง"
        response = "ไม่ทราบจ้า"

    return question, response


def get_personality(message_list, persona_dict=get_emotion_dict()):
    emo_set = get_emotion_summary(message_list, persona_dict)
    emo_set = [i.lower() for i in emo_set]
    o, c, e, a, n = get_ocean(emo_set)
    persona = personality(o, c, e, a, n)
    return persona

test = ["แต่ละวันดูแย่มากโคตรแย่ของแย่", "กระหายชัยชนะเกินไปก็เสียอารมณ์","แต่ละวันดูแย่มากโคตรแย่ของแย่", "กระหายชัยชนะเกินไปก็เสียอารมณ์","แต่ละวันดูแย่มากโคตรแย่ของแย่", "กระหายชัยชนะเกินไปก็เสียอารมณ์"]

sum_emo = get_personality(test)
print("\n\n* sum emo is ", sum_emo)
print("\n\n+ count", Counter(sum_emo))
print("\n\n+++++++++++++++++++ sum on sum is +++++++++++++++++++ \n\n", sum_emo)
