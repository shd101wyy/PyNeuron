'''
Created on 2012-5-31

@author: shd101wyy
'''
from functions import *
from convert_matrix_to_list import convertMatrixToList
from sympy import Matrix
#output is list
def fireForList(function_name,output):
    for i in range(len(output)):
        if function_name=='hardlim':
            output[i]=hardlim(output[i])
        elif function_name=='hardlims':
            output[i]=hardlims(output[i])
        elif function_name=='purelin':
            output[i]=purelin(output[i])
        elif function_name=='satlin':
            output[i]=satlin(output[i])
        elif function_name=='satlins':
            output[i]=satlins(output[i])
        elif function_name=='logsig':
            output[i]=logsig(output[i])
        elif function_name=='tansig':
            output[i]=tansig(output[i])
        elif function_name=='poslin':
            output[i]=poslin(output[i])
        else:
            print("there is no such kind function called"+function_name)
    return output



#output is matrix
def fireForMatrix(function_name,matrix):
    row=matrix.rows
    col=matrix.cols
    for i in range(row):
        for j in range(col):
            matrix[i,j]=fireForOneValue(function_name,matrix[i,j])
    return matrix

def fireForOneValue(function_name,value):
    #print 'value'+str(value)
    if value!=None:
        if function_name=='hardlim':
            value=hardlim(value)
        elif function_name=='hardlims':
            value=hardlims(value)
        elif function_name=='purelin':
            value=purelin(value)
        elif function_name=='satlin':
            value=satlin(value)
        elif function_name=='satlins':
            value=satlins(value)
        elif function_name=='logsig':
            value=logsig(value)
        elif function_name=='tansig':
            value=tansig(value)
        elif function_name=='poslin':
            value=poslin(value)
        else:
            print("there is no such kind function called"+function_name)
    else:
        pass
    return value
