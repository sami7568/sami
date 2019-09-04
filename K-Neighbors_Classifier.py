# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:28:04 2019

@author: SHAMS UR REHMAN
"""

from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

from sklearn.neighbors import KNeighborsClassifier

X = [[173,67,8],[167,40,8],[162,55,6],[169,60,8],[172,68,7],[162,44,7],[150,30,8],[163,76,10],[140,38,6],[159,60,6]]

Y = ['male','male','female','male','male','female','male','male','female','female']

test_data = [[169, 60, 8]]

kn_clf = KNeighborsClassifier()
kn_clf.fit(X,Y)
kn_prediction = kn_clf.predict(test_data)
print (kn_prediction)