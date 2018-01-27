#-*- coding: GBK -*-
from selenium import webdriver
import codecs
import json


oulu = webdriver.Chrome()


class WordItem:
    def __init__(self, word, phonitic, exp, phrase):
        self.word = word
        self.phonitic = phonitic
        self.explain = exp
        self.phrase = phrase

    def word_print(self):
            print(self.word)
            print(self.phonitic)
            print(self.explain)
            print(self.phrase)

    
def search_word(words):
    for word in words:
        wordse = word
        base_url = 'http://dict.eudic.net/dicts/en'
        url = base_url+'/'+wordse
        oulu.get(url)
        oulu.implicitly_wait(30)
        word = oulu.find_element_by_xpath('//*[@id="exp-head"]/h1/span[1]').text
        phonitic = oulu.find_element_by_xpath('//*[@id="exp-head"]/div/span[1]').text
        exp=oulu.find_element_by_xpath('//*[@id="ExpFCChild"]').text
        phrase=''##oulu.find_element_by_xpath('//*[@id="ExpSPEC"]').text
        word1=worditem(word,phonitic,exp,phrase)
        word1.wprint()
    ## a=json.dumps([word,phonitic,exp,phrase])
    ## oulu.close()


f = open('word.txt','r')
words = f.readline()
nword = words.split(",")
print(nword)
search_word(nword)

