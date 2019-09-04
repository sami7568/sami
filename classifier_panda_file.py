# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:56:34 2019

@author: leveno
"""

import pandas as pd
from sklearn import tree
 
fl=pd.read_csv('file.csv') 
#print(fl)

gender=list(fl['gender'])
height=list(fl['height'])
weight=list(fl['weight'])
shoe_size=list(fl['shoe_size'])

my_list=[gender,height,weight,shoe_size]
 
values=[]
x=my_list[0]

height=my_list[1]
weight=my_list[2]
shoe_size=my_list[3]

for i in range(len(x)):
    new_list=[height[i],weight[i],shoe_size[i]]
    values.append(new_list)
    
clf=tree.DecisionTreeClassifier()
clf=clf.fit(values,x)
prediction=clf.predict([[180,69,9]]) 

print (prediction)  
    
    


