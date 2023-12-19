import torch
import numpy 

class NeuralNetwork(torch.nn.Module):
    def __init__(self, dictSize):
        super(NeuralNetwork, self).__init__()
        self.linear1 = torch.nn.Linear(dictSize, 512)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(512, 512)
        self.relu2 = torch.nn.ReLU()
        self.linear3 = torch.nn.Linear(512, 3)
        self.softmax = torch.nn.Softmax(dim=1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu1(x)
        x = self.linear2(x)
        x = self.relu2(x)
        x = self.linear3(x)
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

            self.sentiment.append(float(content[0]))
            del content[0]

            tweetTensor = torch.zeros(sizeDict)

            for wordAndOccurrence in content: 
                temp = wordAndOccurrence.split(":")
                # correspond to the word id, -1 because it starts at 1
                tweetTensor[int(temp[0])-1] = int(temp[1])

            self.data.append(tweetTensor)

        file.close()

        self.sentiment = torch.from_numpy(numpy.array(self.sentiment)).to(torch.float32)
        # print(self.sentiment)
        # print(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.sentiment[idx], self.data[idx]

def train_loop(dataloader, model, loss_fn, optimizer):
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction and loss
        print(X.tolist())

        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")

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
# classificator = createList("donnees_tp1/twitter-2013dev-A.txt", wordDict)
createFile("dev", classificator)
# classificator = createList("donnees_tp1/twitter-2013test-A.txt", wordDict)
createFile("test", classificator)

# svm = SVMDataset("svm/aaugh.svm", 6)

print(len(wordDict))

svm = SVMDataset("svm/train.svm", len(wordDict))
dataloader = torch.utils.data.DataLoader(svm, batch_size=64)
model = NeuralNetwork(len(wordDict))
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

train_loop(dataloader, model, loss_fn, optimizer)

# faire en sorte que les svm de dev et test soient écrits avec les mots de train