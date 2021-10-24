# Import the module nitk
import nltk

def detectLang():
    # We define our lengaujes
    languages = ["spanish","english","dutch", "italian","portuguese","turkish","danish","french", "russian"]
    
    # We write the message to decrypt
    message = input("Type the decrypted message: ")
    
    # Now we divide the text into single words
    tokens = nltk.tokenize.word_tokenize(message)
    
    # We make all the text lowercase
    tokens = [t.strip().lower() for t in tokens]
    
    langCount = {} # Define dict
    
    for lang in languages:
        stop_words = nltk.corpus.stopwords.words(lang)
        langCount[lang] = 0
    
    # Scroll through the words of our message
    for word in tokens:
        if word in stop_words:
            langCount[lang] += 1
    
    # Detect language
    detect = max(langCount, key = langCount.get)
    print ("El lenguaje utilizado es:", detect)

if __name__ == "__main__":
    detectLang()