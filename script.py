#data preprations
import csv 
with open('finaldata-data01.csv', 'rb') as csvfile:
zipcodereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in zipcodereader:
		print ', '.join(row)

#building the training and the testing sets (80-20)
