# in a binary prediction case when we have so much data, we can make prediction simply 
# by observing trend in the data

import numpy as np
import pandas as pd

filename = 'titanic_data.csv'
full_data = pd.read_csv(filename)

outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

def accuracy_score(truth, pred):
    if len(truth) == len(pred): 
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"


def prediction(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger.Sex == 'female':
            if passenger.Pclass == 1 or passenger.Pclass == 2 :
                predictions.append(1)
                continue
            if passenger.Age >= 40 :
                predictions.append(0)
                continue
            predictions.append(1)
            continue
        if passenger.Age < 10:
            if passenger.SibSp  <= 1:
                predictions.append(1)
                continue
            predictions.append(0)
            continue
        if passenger.Age < 18:
            if passenger.Pclass <=2 :
                predictions.append(1)
                continue
            predictions.append(0)
            continue
        predictions.append(0)
    
    return pd.Series(predictions)

if __name__ == "__main__":
	print accuracy_score(outcomes, prediction(data))

# without any statistic method, this simple func acchive 82% accuracy
# can improve it easily just by make decision tree more complicate