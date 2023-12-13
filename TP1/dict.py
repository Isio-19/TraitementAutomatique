def loadStopWords():
    file = open("donnees_tp1/stopwords.txt", "r", encoding="utf-8")

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
    word = word.replace("\n", "")

    if caps:
        word = word.lower()

    if punc:
        punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~'
        for i in punctuation:
            word = word.replace(i, "")
        

    return word

def translateSentiment(sentiment: str):
    sentimentTranslator = ["neutral", "positive", "negative"]

    return sentimentTranslator.index(sentiment)

def initLexique(filePath, wordDict):

    file = open(filePath, "r")

    for line in file:
        lineContent = line.split("\t")[2]

        # to get rid of the \u
        lineContent = lineContent.encode("utf-8", "strict")
        lineContent = lineContent.decode("utf-8", "strict")

        for word in lineContent.split(" "):
            word = wordTransform(word, caps, punc)

            if not(wordFilter(word, stopwords, links, hash, at, empty)):
                continue

            if (word not in wordDict):
                wordDict.update({word : len(wordDict)+1})

    file.close()

    return wordDict

def createList(fileName: str, wordDict: dict):
    global stopwords, links, caps, hash, at, punc, empty

    file = open(fileName, "r")

    listTweet = []

    for line in file:
        split = line.split("\t")

        lineTweet = str(translateSentiment(split[1]))
        lineContent = split[2]

        # to get rid of the \u
        lineContent = lineContent.encode("utf-8", "strict")
        lineContent = lineContent.decode("utf-8", "strict")

        indexToOccurrenceDict = {}

        for word in lineContent.split(" "):
            word = wordTransform(word, caps, punc)

            if not(wordFilter(word, stopwords, links, hash, at, empty)):
                continue
            
            if wordDict[word] not in indexToOccurrenceDict:
                indexToOccurrenceDict.update({wordDict[word] : 1})
            else:
                indexToOccurrenceDict.update({wordDict[word] : indexToOccurrenceDict[wordDict[word]]+1})

        indexToOccurrenceDict = dict(sorted(indexToOccurrenceDict.items()))

        for index, occurrence in indexToOccurrenceDict.items():
            lineTweet += " " + str(index) + ":" + str(occurrence)

        listTweet.append(lineTweet)

    file.close()

    return listTweet

def createFile(fileName: str, listTweet: list):
    file = open("svm/"+fileName+".svm", "w")
    
    for line in listTweet: 
        file.write(line)
        file.write("\n")
    
    file.close()

stopwords = []
stopwords = loadStopWords()
links = True
caps = False
hash = False
at = False
punc = True
empty = False

wordDict = {}
wordDict = initLexique("donnees_tp1/twitter-2013train-A.txt", wordDict)
wordDict = initLexique("donnees_tp1/twitter-2013dev-A.txt", wordDict)
wordDict = initLexique("donnees_tp1/twitter-2013test-A.txt", wordDict)

classificator = createList("donnees_tp1/twitter-2013train-A.txt", wordDict)
createFile("train", classificator)
classificator = createList("donnees_tp1/twitter-2013dev-A.txt", wordDict)
createFile("dev", classificator)
classificator = createList("donnees_tp1/twitter-2013test-A.txt", wordDict)
createFile("test", classificator)
