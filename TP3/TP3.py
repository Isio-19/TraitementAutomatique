import numpy as np
from numpy import linalg

def init():
    vectors = {}
    
    file = open("vectors400.txt")
    for line in file:
        line = line.strip()
        split = line.split(" ")
        
        word = split[0]
        del split[0]

        vector = []
        for value in split:
            vector.append(float(value))
        
        vectors.update({word : vector})
    return vectors

#4 - Fonction qui permet de calculer la similarité cosine de deux mots 
def cosineSimilarity(word1, word2, vectors):
    firstVector = np.array(vectors.get(word1))
    secondVector = np.array(vectors.get(word2))

    print(firstVector)
    print(secondVector)

    return np.dot(firstVector, secondVector)/(np.linalg.norm(firstVector)*np.linalg.norm(secondVector))

vectors = init()

words = str(input("Type two words to find the similarity of: "))
while True:
    words = words.split() 
    if len(words) == 2:
        break

    words = str(input("Please type two words to find the similarity of: "))
        
print(cosineSimilarity(words[0], words[1], vectors))
