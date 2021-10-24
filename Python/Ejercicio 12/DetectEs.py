import os
from main import message

UPPERLETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ¨ÁÉÍÓÚ´'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    path = os.path.split(os.path.realpath(__file__), encoding = "utf-8")
    dictionaryFile = open(path[0] + '/dictEsp.txt')
    spanishWords = {}
    for word in dictionaryFile.read().split('\n'):
        spanishWords[word] = None
    dictionaryFile.close()
    return spanishWords

SPANISH_WORDS = loadDictionary()

def SpanishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in SPANISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isSpanish(message, wordPercentage = 20, letterPercentage = 85):
    wordsMatch = SpanishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messPort = (float(numLetters) / len(message)) * 100
    lettersMatch = messPort >= letterPercentage
    return wordsMatch and lettersMatch

def Detect(message):
    print("\n")
    isenglish = isSpanish(message)
    engliscount = int(SpanishCount(message))
    print("Español: %s \n" % (isenglish))
