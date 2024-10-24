#Imported Libraries

import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from sklearn.externals import joblib

#This function to read the messages leaving the header from each of the files and suming it
#to list for classification

def reading_Files(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


#Below function to append the message and their particular classification

def dffromdirectory(path, classification): #dataframefromdirectory
    rows = []
    index = []
    for filename, message in reading_Files(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)


#Main to call above functions
data1 = DataFrame({'message': [], 'class': []})

data1 = data1.append(dffromdirectory(r'/workspaces/spam/emails/spam', 'spam'))
data1 = data1.append(dffromdirectory(r'/workspaces/spam/emails/ham', 'ham'))


#Here we're reading Data Frame
data1.head()



#training data using MultinomialNB classifier
vector = CountVectorizer()
counts = vector.fit_transform(data1['message'].values)

classifier = MultinomialNB()
targets = data1['class'].values
classifier.fit(counts, targets)

# saved model 
#joblib.dump(classifier, 'spam.pkl')

#Load pickle file
class_from_joblib = joblib.load('spam.pkl')

#Predicting the Spam Emails

examples = ['Free Viagra available!!!', "Hi Neil, how about a game of squash tomorrow?"]
def prediction(example):
    class_from_joblib = joblib.load('spam.pkl')
    example_counts = vector.transform(example)
    prediction = class_from_joblib.predict(example_counts)
    return prediction

#prediction(examples)
#print(prediction)
