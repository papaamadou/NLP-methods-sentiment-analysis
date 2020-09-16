# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from nltk import wordpunct_tokenize

test = wordpunct_tokenize("tout d'abord, nous allons commencer par découper notre text en mots. C'est ce qu'on appelle la tokenisation ou tokenizer en anglais")
print(test)

language = stopwords.fileids()
print(language)

frStopword = stopwords.words('french')[0:10]
print(frStopword)

def _calc_ratios(text):
     ratios = {}
    
     tokens = wordpunct_tokenize(text)
     words = [word.lower() for word in tokens]
    
     for lang in stopwords.fileids():
         stopwords_set = set(stopwords.words(lang))
         words_set = set(words)
         common_words = words_set.intersection(stopwords_set)
    
         ratios[lang] = len(common_words)
    
     return ratios

def _calc_probability(most, secode_most) :
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba)


def detect_language(text):

     ratios = _calc_ratios(text)
    
     most_rated_language = max(ratios, key=ratios.get)
     most_common_words = ratios[most_rated_language]
     del ratios[most_rated_language]
     second_most_rated_language = max(ratios, key=ratios.get)
     second_most_common_words = ratios[second_most_rated_language]
    
     print("there is %s%% chances for this text to be writen in %s" %(_calc_probability(most_common_words, second_most_common_words), most_rated_language))

text = "It's was fun this years"
test3 = _calc_ratios(text)
print(test3)
detect_language(text)

