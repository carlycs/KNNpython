import csv
import random
import math
import operator
#append directories to python path
import sys
sys.path.append("/home/fixinthis/Documents/git/KNNpython")

from loadDataset import loadDataset 
from euclideanDistance import euclideanDistance  
from getNeighbors import getNeighbors   
from getResponse import getResponse   
from getAccuracy import getAccuracy  
 
def main():
    # prepare data
    trainingSet=[]
    testSet=[]
    split = 0.80
    loadDataset('crime.csv', split, trainingSet, testSet)
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    # generate predictions
    predictions=[]
    k = 3
    for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
            print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))

    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
main()


