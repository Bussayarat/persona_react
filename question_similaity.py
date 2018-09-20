from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, manhattan_distances

import numpy as np
from pythainlp import word_tokenize

STOP_WORD = open("stopwords.txt", "r").read().splitlines()


def tokenizer(text):
    #  TODO : cleansing
    text = word_tokenize(text)
    return text


class similarity:
    def __init__(self, questions):
        self.questions = questions
        self.count_vector = TfidfVectorizer(
            tokenizer=tokenizer, lowercase=False, stop_words=STOP_WORD
        )

        self.questions_count_vector = self.count_vector.fit_transform(questions)

    def get_similarity(self, message, theshold=0.0, returns="max"):

        message_count_vector = self.count_vector.transform([message])

        if self.questions_count_vector == None:
            return False

        distance = cosine_similarity(message_count_vector, self.questions_count_vector)[0]
        
        if min(distance) <= theshold:
            return False
        elif returns == "max":
            index = np.argmax(distance)
            similarity_question = self.questions[index]
            return similarity_question

        elif returns == 'all':
            return {self.questions[i] : distance[i]  for i in range(len(distance))}

