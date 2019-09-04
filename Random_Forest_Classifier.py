# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:47:33 2019

@author: SHAMS UR REHMAN
"""

from sklearn.ensemble import RandomForestClassifier

X = [[173,67,8],[167,40,8],[162,55,6],[169,60,8],[172,68,7],[162,44,7],[150,30,8],[163,76,10],[140,38,6],[159,60,6]]

Y = ['male','male','female','male','male','female','male','male','female','female']

test_data = [[159, 60, 6]]

rfc_clf = RandomForestClassifier(n_estimators=100)
rfc_clf.fit(X,Y)
rfc_prediction = rfc_clf.predict(test_data)
print (rfc_prediction)