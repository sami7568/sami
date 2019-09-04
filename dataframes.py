# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:40:47 2019

@author: leveno
"""
 
import pandas as pd

dtf ={'A': pd.Series([100.,200.,300.], index=['apple','pear','orange']),
      'B':pd.Series([111.,222.,333.,4444.], index=['apple','pear','orange','melon'])}

df=pd.DataFrame(dtf)
print(df)

