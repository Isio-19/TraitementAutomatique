import string

# index of word is index+1 (so no 0)
def addWord(wordList: list, wordToAdd: str):
    if wordToAdd in wordList:
        return wordList, findWord(wordList, wordToAdd)

    wordList.append(wordToAdd)
    return wordList, len(wordList)

def findWord(wordList: list, wordToFind: str):
    return wordList.index(wordToFind)+1

def findLowestIndex(indexList):
    lowestIndex = indexList[0]
    index = 0

    for i in range(len(indexList)):
        if lowestIndex > indexList[i]:
            lowestIndex = indexList[i]
            index = i

    return lowestIndex, index


def initList(content, lexique, indexList, occurrenceList, caps, stopword, links, hash, at, punc, empty):
    if stopword:
        stopwords = loadStopwords()
    
    for word in content:
        # uncaps the words        
        if caps:
            word = word.lower()

        # gets rid of stopwords
        if stopword:
            if word in stopwords:
                continue

        # gets rid of links
        if links:
            if word.startswith("http"):
                continue 

        # gets rid of hashtags
        if hash:
            if word.startswith("#"):
                continue

        # gets ried of mentions
        if at:
            if word.startswith("@"):
                continue

        # delete punctuation
        if punc: 
            word = word.replace(string.punctuation, "")
            word = word.replace(" ", "")

        # gets rid of empty words
        if empty:
            if word == "":
                continue

        lexique, index = addWord(lexique, word)

        if not(index in indexList):
            indexList.append(index)
            occurrenceList.append(content.count(word))

    return lexique, indexList, occurrenceList

def translateSentiment(sentiment):
    sentimentList = ["neutral", "positive", "negative"]
    return sentimentList.index(sentiment)

def loadStopwords():
    file = open("stopwords.txt", "r", encoding="utf-8")
    list = []

    for line in file: 
        list.append(line)

    file.close()
    
    return list

def buildLexique(filePath, lexique, caps, stopword, links, hash, at, punc, empty):
    file = open(filePath, "r")

    if stopword:
        stopwords = loadStopwords()

    for line in file:
        content = line.split('\t')[2].split(" ")
     
        for word in content:
            word = word.replace(" ", "")

            # filters
            if caps: 
                word = word.lower()

            if stopword:
                if word in stopwords:
                    continue

            if links:
                if word.startswith("http"):
                    continue

            if hash:
                if word.startswith("#"):
                    continue

            if at:
                if word.startswith("@"):
                    continue

            if punc:
                word = word.replace(string.punctuation, "")
            
            if empty:
                if len(word) == 0:  
                    continue
    
            lexique, _ = addWord(lexique, word)
    
    file.close()

    return lexique

def createClassificator(filePath, lexique, stopword, links, caps, hash, at, punc, empty):
    file = open(filePath, "r")

    tweetList = []

    for line in file:
        split = line.split("\t")

        sentiment = split[1]
        content = split[2].split(" ")

        tweet = str(translateSentiment(sentiment))
        indexList = []
        occurrenceList = []

        # initialise indexList and occurrenceList
        lexique, indexList, occurrenceList = initList(content, indexList, occurrenceList, stopword, links, caps, hash, at, punc, empty)

        # build the tweet line to add to the file
        while len(indexList) != 0:
            # find the lowest index in list
            lowestIndex, index = findLowestIndex(indexList)

            tweet += " " + str(lowestIndex) + ":" + str(occurrenceList[index])
            
            del indexList[index]
            del occurrenceList[index]

        tweetList.append(tweet)

    file.close()

    print(len(lexique))

    return tweetList

def createFile(fileName, list):
    file = open("svm/"+fileName+".svm", "w")
    for line in list:
        file.write(line)
        file.write("\n")

    file.close()

caps=False
stopword=True
links=False
hash=False
at=False
punc=False
empty=False

wordList = []
wordList = buildLexique("donnees_tp1/twitter-2013train-A.txt", wordList)
wordList = buildLexique("donnees_tp1/twitter-2013dev-A.txt", wordList)
wordList = buildLexique("donnees_tp1/twitter-2013test-A.txt", wordList)
print(len(wordList))
# createClassificator("donnees_tp1/twitter-2013train-A.txt", wordList, caps, stopword, links, hash, at, punc, empty)
# createFile("train", list)

# list = createClassificator("donnees_tp1/twitter-2013dev-A.txt", caps, stopword, links, hash, at, punc, empty)
# createFile("dev", list)

# list = createClassificator("donnees_tp1/twitter-2013test-A.txt", caps, stopword, links, hash, at, punc, empty)
# createFile("test", list)