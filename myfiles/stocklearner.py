import pandas as pd
import quandl as qd
import numpy as np
from sklearn.model_selection import train_test_split
import math
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
import csv

def predict(symbol):
    result=[]
    symbol='NSE/'+symbol
    print(symbol)
    df=qd.get(symbol)
    df['beta']=((df['High']-df['Low'])/df['High'])*100
    df['diff']=((df['Close']-df['Open'])/df['Open'])*100
    print(df.tail())
    df=df[['diff','Close']]
    forecast_col = 'Close'
    df.fillna(value=-99999, inplace=True)
    forecast_out = int(1)
    xpredict=df[-5:]
    print(xpredict)
    df['target']=df[forecast_col].shift(-forecast_out)
    df.fillna(9999,inplace=True)
    print(df.tail(10))
    X = np.array(df.drop(['target'], 1))
    xpredict=np.array(xpredict)
    X = preprocessing.scale(X)
    xpredict=preprocessing.scale(xpredict)
    X_lately = X[-(2*forecast_out):]
    X = X[:-(2*forecast_out)]
    df.dropna(inplace=True)
    y = np.array(df['target'])
    ylately=y[-(2*forecast_out):]
    y=y[:-(2*forecast_out)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    result.append(symbol)
    result.append(confidence)
    result.append(ylately)
    result.append(clf.predict(X_lately))
    

mypredictions=[]

with open('symbol.txt','r')  as f:
    line=f.readline()
    while(len(line)>0):
        mypredictions.append(predict(line))
        line=f.readline().strip(' ')

print(mypredictions)
with open('predict.csv','wb') as filer:
    for x in mypredictions:
        for y in x:
            filer.write(y)
            filer.write(',')
        file.write('\n')
        
with open('predict.csv','wb') as filer:
    writer=csv.writer(filer,lineterminator='\n')
    writer.writerow(['SYMBOL','ACCURACY','4/17(A)','4/18(D)','4/17(P)','4/18(P)'])
    for x in mypredictions:
        writer.writerow(x)
    
