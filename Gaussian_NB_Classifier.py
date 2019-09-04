# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:19:28 2019

@author: SHAMS UR REHMAN
"""

from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

from sklearn.naive_bayes import GaussianNB

X = [[173,67,8],[167,40,8],[162,55,6],[169,60,8],[172,68,7],[162,44,7],[150,30,8],[163,76,10],[140,38,6],[159,60,6]]

Y = ['male','male','female','male','male','female','male','male','female','female']

test_data = [[162, 44, 7]]

gnb_clf = GaussianNB()
gnb_clf.fit(X,Y)
gnb_prediction = gnb_clf.predict(test_data)
print (gnb_prediction)