import spacy
import os
import re


def classify_model(text):
    pwd = os.getcwd()
    nlp_model = spacy.load(f"{pwd}/data/textcat_roberta_output/model-best")
    output = nlp_model(text)

    return max([(value, key) for key, value in output.cats.items()])[1]


if __name__ == '__main__':
    text = 'COVID-19 is the most common cause of law enforcement duty-related deaths in 2020 and 2021'
    print(classify_model(text))