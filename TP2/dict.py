import torch
import numpy 

device = ("cuda")

class NeuralNetwork(torch.nn.Module):
    def __init__(self, dictSize):
        super(NeuralNetwork, self).__init__()
        self.linear1 = torch.nn.Linear(dictSize, 1024)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(1024, 3)
        self.softmax = torch.nn.Softmax(dim=1)
        self.double()

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu1(x)
        x = self.linear2(x)
        x = self.softmax(x)

        return x
    
class SVMDataset(torch.utils.data.Dataset):
    def __init__(self, svmFile, sizeDict):
        self.svmFile = svmFile

        # list of tensor 
        self.data = []

        # list of int 
        self.sentiment = []

        file = open(self.svmFile)
        for line in file:
            line = line.replace("\n", "")
            content = line.split(" ")

            self.sentiment.append(int(content[0]))
            del content[0]

            tweetTensor = numpy.zeros(sizeDict)

            for wordAndOccurrence in content: 
                temp = wordAndOccurrence.split(":")
                # correspond to the word id, -1 because it starts at 1
                tweetTensor[int(temp[0])-1] = int(temp[1])

            self.data.append(torch.from_numpy(tweetTensor).to(device))

        file.close()

        self.sentiment = torch.from_numpy(numpy.array(self.sentiment)).to(device)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.sentiment[idx]

def train_loop(dataloader, model, loss_fn, optimizer):
    for batch, (X, y) in enumerate(dataloader):
        # rajout
        X, y = X.to(device), y.to(device)
        
        # Compute prediction and loss
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def test_model(dataloader, model):
    errorRate = 0
    numberLine = 0

    confusionMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for batch, (X, y) in enumerate(dataloader):
        predictedY = model(X)

        for i in range(len(X)):
            numberLine += 1

            predictedLabel = numpy.argmax(predictedY[i].tolist())

            confusionMatrix[predictedLabel][y[i]] += 1

            if predictedLabel != y[i]:
                errorRate += 1

    precision = 100 - (errorRate/numberLine)*100

    print(f'Prediction rate of the model: {precision}%')
    return confusionMatrix

def loadStopWords():
    file = open("donnees_tp2/stopwords.txt", "r", encoding="utf-8")

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
            
            # ignore the words that are not in the training set
            if word not in wordDict:
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
links = False
caps = False
hash = False
at = False
punc = False
empty = False

wordDict = {}
wordDict = initLexique("donnees_tp2/twitter-2013train-A.txt", wordDict)

createFile("train", createList("donnees_tp2/twitter-2013train-A.txt", wordDict))
# createFile("dev", createList("donnees_tp2/twitter-2013dev-A.txt", wordDict))
createFile("test", createList("donnees_tp2/twitter-2013test-A.txt", wordDict))

averagePrecision = 0

svm = SVMDataset("svm/train.svm", len(wordDict))
dataloader = torch.utils.data.DataLoader(svm, batch_size=4)
model = NeuralNetwork(len(wordDict)).to(device)
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

confusionMatrix = []

for i in range(5):
    train_loop(dataloader, model, loss_fn, optimizer)

    svm = SVMDataset("svm/test.svm", len(wordDict))
    dataloader = torch.utils.data.DataLoader(svm, batch_size=4)

    confusionMatrix = test_model(dataloader, model)

print(f"Confusion matrix: {confusionMatrix}")