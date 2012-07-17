'''
Created on 2012-5-31

@author: shd101wyy
'''
from sympy import Matrix
'''
def convertMatrixToList(matrix):
    rows=matrix.rows
    columns=matrix.cols
    if matrix.cols!=1:
        list=[[0 for column in range(columns)]for row in range(rows)]
        for i in range(rows):
            for j in range(columns):
                list[i][j]=matrix[i,j]
    else: #when column =1, avoid[[1],[2]]kind of data
        list=[]
        for i in range(rows):
            list.append(matrix[i,0])
    return list
        
'''
def convertMatrixToList(matrix):
    rows=matrix.rows
    columns=matrix.cols
    list=[[0 for column in range(columns)]for row in range(rows)]
    for i in range(rows):
        for j in range(columns):
            list[i][j]=matrix[i,j]
    return list
        
