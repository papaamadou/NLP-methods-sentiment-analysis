# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from nltk import wordpunct_tokenize


def ratio_calculator(text):
    # Input : a text wich is a caracter string
    # Output : a dictionary with in key the language and in values the ratio of words in this language
     myRatio = {}
    
    #NLP first treatement : tokenize the text, get a list of words
     tokens = wordpunct_tokenize(text)
     words = [word.lower() for word in tokens]
    
     for language in stopwords.fileids():
         # we have a list of language and for this list of language we have a ratio
         stopwords_set = set(stopwords.words(language))
         words_set = set(words) 
         common_words = words_set.intersection(stopwords_set)
    
         myRatio[language] = len(common_words)
    
     return myRatio

def probability_calculator(most, secode_most) :
    # Input : 2 int
    # Output : a int
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba) 


def language_detector(text):
    # Input : a text which is a string of caracter
    # Output : nothing
    # Goals : find the language of a the text it's a prediction
     ratios = ratio_calculator(text)
    
     most_rated_language = max(ratios, key=ratios.get)
     most_common_words = ratios[most_rated_language]
     del ratios[most_rated_language]
     second_most_rated_language = max(ratios, key=ratios.get)
     second_most_common_words = ratios[second_most_rated_language]
    
     print("there is %s%% chances for this text to be writen in %s" %(probability_calculator(most_common_words, second_most_common_words), most_rated_language))

text = "It's was fun this years"