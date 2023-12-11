import string

def loadStopWords():
    file = open("stopwords.txt", "r", encoding="utf-8")

    stopwords = [] 
    for word in file:
        stopwords.append(word)

    return stopwords

def wordFilter(word: str, stopwords: list, links: bool, hash: bool, at: bool, empty: bool):
    if len(stopwords) != 0:
        if word in stopwords:
            return False

    if links:
        if word.startswith("http"):
            return False

    if hash:
        if word.startswith("#"):
            return False
    if at:
        if word.startswith("@"):
            return False

    if empty:
        if len(word) == 0: 
            return False

    return True

def wordTransform(word: str, caps: bool, punc: bool):
    if caps:
        word = word.lower()

    if punc:
        word = word.replace(string.punctuation, "")

    return word

def initLexique(filePath, wordDict):
    global stopwords, links, caps, hash, at, punc, empty

    file = open(filePath, "r")

    for line in file:
        lineContent = line.split("\t")[2]

        for word in lineContent.split(" "):

            word = wordTransform(caps, punc)

            if not(wordFilter(stopwords, links, hash, at, empty)):
                continue

            wordDict.update({word : len(wordDict)+1})

    file.close()

    return wordDict

stopwords, links, caps, hash, at, punc, empty


wordDict = {}
wordDict = initLexique("donnees_tp1/twitter-2013train-A.txt", wordDict)
wordDict = initLexique("donnees_tp1/twitter-2013dev-A.txt", wordDict)
wordDict = initLexique("donnees_tp1/twitter-2013test-A.txt", wordDict)



print(len(wordDict))