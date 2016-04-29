trainingSet=[]
testSet=[]
loadDataset('finaldata-data01.csv', 0.66, trainingSet, testSet)
print 'Train: ' + repr(len(trainingSet))
print 'Test: ' + repr(len(testSet))
