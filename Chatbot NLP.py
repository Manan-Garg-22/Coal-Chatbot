import numpy as np
import random
import string
import nltk



file_path = file_path = r"C:\Users\Prateek Gupta\Desktop\C_programs 101\Prateek_Codes\data.txt"
f = open(file_path, 'r', errors='ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))


greet_inputs = ('hello', 'hi' , 'whassup', 'yo')
greet_responses = ('hi','hello', 'right back at you')
def greet(sentence):
    for word in sentence.split():
        return random.choice(greet_responses)
    

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo1_response = ''
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        robo1_response = robo1_response +  "I am sorry but I am unable to understand you"
        return robo1_response
    else:
        robo1_response = robo1_response + sentence_tokens[idx]
        return robo1_response
    
flag = True
print("Hello! I am the Retreival Learning Bot. Start typing your text after greeting to talk to me. For ending convo type bye!")

while(flag ==True):

    user_response = input()
    user_response = user_response.lower()
    if(user_response != "bye"):
        if(user_response == 'thank you' or user_response == 'thanks'):
            flag = False
            print("Bot: You are welcome..")
        else:
            if(greet(user_response) != None):
                print("Bot" + greet(user_response))
            else:
                sentence_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response) 
                final_words = list(set (word_tokens))
                print("Bot: ", end = "")
                print(response(user_response)) 
                sentence_tokens.remove(user_response)
    else:
        flag = False
        print('Bot: Goodbye!')
