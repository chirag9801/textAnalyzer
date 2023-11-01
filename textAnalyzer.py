
from tokenize import String


sentence = str(input("Enter a String: "))

class TextAnalyzer(object):
    def __init__(self, text):
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')

        formattedText = formattedText.lower()

        self.fmttext = formattedText

    
    def freqall(self):
        wordlist = self.fmttext.split(' ')
        wordmapr = {}
        for word in set(wordlist):
            wordmapr[word] = wordlist.count(word)

        return wordmapr
    

    def wordfreq(self, word):
        freqdict = self.freqall()

        if word in freqdict:
            return freqdict[word]
        else:
            return 0
        

#define object instance

analyzer = TextAnalyzer(sentence)

print("formatted text : ",analyzer.fmttext)

wordmapr = analyzer.freqall()
print(wordmapr)

wordinput = str(input("enter word from above dictionary: "))
frequency = analyzer.wordfreq(wordinput)
print('frequency of word ',wordinput,'is ',frequency)