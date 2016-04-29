import csv
import random
import math
import operator
from loadDataset.py import loadDataset 
from euclideanDistance.py import euclideanDistance  
from getNeighbors.py import getNeighbors   
from getResponse.py import getResponse   
from getAccuracy.py import getAccuracy  
 
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = .80
	loadDataset('finaldata-data01.csv', split, trainingSet, testSet)
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
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


