import numpy as num
import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

def token(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return PorterStemmer().stem(word.lower())


def bag_of_words(TokenizeSentence, AllWords):
    sentence_words = [stem(word) for word in TokenizeSentence]
    # initialize bag with 0 for each word
    bag = num.zeros(len(AllWords), dtype=num.float32)
    for i, w in enumerate(AllWords):
        if w in sentence_words: 
            bag[i] = 1
    return bag

