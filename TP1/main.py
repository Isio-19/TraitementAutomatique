import sys

# index of word is index+1 (so no 0)
def addWord(wordList: list, wordToAdd: str):
    if wordToAdd in wordList:
        return wordList, findWord(wordList, wordToAdd)

    wordList.append(wordToAdd)
    return wordList, len(wordList)

def findWord(wordList: list, wordToFind: str):
    return wordList.index(wordToFind)+1

def initList(content, lexique, indexList, occurrenceList, stopwords):
    for word in content:
        if word in stopwords:
            continue

        if word.startswith("http") or word.startswith("#") or word.startswith("@"):
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

def createClassificator(filePath):
    file = open(filePath, "r")

    stopwords = loadStopwords()
    lexique = []
    tweetList = []

    for line in file:
        split = line.split("\t")

        sentiment = split[1]
        content = split[2].split(" ")

        tweet = str(translateSentiment(sentiment))
        indexList = []
        occurrenceList = []

        # initialise indexList and occurrenceList
        lexique, indexList, occurrenceList = initList(content, lexique, indexList, occurrenceList, stopwords)

        # build the tweet line to add to the file
        while len(indexList) != 0:
            # find the lowest index in list
            lowestIndex = indexList[0]
            index = 0

            for i in range(len(indexList)):
                if lowestIndex > indexList[i]:
                    lowestIndex = indexList[i]
                    index = i

            tweet += " " + str(lowestIndex) + ":" + str(occurrenceList[index])
            
            del indexList[index]
            del occurrenceList[index]

        tweetList.append(tweet)

    file.close()

    print(len(lexique))

    return tweetList

def createFile(fileName, list):
    file = open(fileName+".svm", "w")
    for line in list:
        file.write(line)
        file.write("\n")

    file.close()

list = createClassificator("donnees_tp1/twitter-2013train-A.txt")
createFile("train", list)