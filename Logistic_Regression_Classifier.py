# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:30:55 2019

@author: SHAMS UR REHMAN
"""

from sklearn.linear_model import LogisticRegression

# [height, weight, shoe_size]
X = [[173,67,8],[167,40,8],[162,55,6],[169,60,8],[172,68,7],[162,44,7],[150,30,8],[163,76,10],[140,38,6],[159,60,6]]

Y = ['male','male','female','male','male','female','male','male','female','female']

test_data = [[159, 60, 6]]

l_clf = LogisticRegression(solver='lbfgs')
l_clf.fit(X,Y)
l_prediction = l_clf.predict(test_data)
print (l_prediction)