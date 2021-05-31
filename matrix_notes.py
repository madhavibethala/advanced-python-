# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
a=np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
print(a)
print("no of rows:")
print(a.shape[0])
print("no of column:")
print(a.shape[1])

# insert a column to a matrix

col_new=np.matrix("2,3,4")
print(col_new)

a=np.insert(a,0,col_new,axis=1)
print(a)
row_new=np.matrix("1,2,3,4,6")
print(row_new)

#
a=np.insert(a,3,row_new,axis=0)
print(a)
print(a.size)
#modifing matrix elements
a[0,1]=-3
print(a)
print("first row data",a[1,:])
print("sec column",a[:,2])
