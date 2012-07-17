'''
Created on 2012-5-31

@author: shd101wyy
'''
#input_data is [1,2,3] alike
from sympy import Matrix
from from_function_fire_output import fireForList
def activate(weight,input_data,bias,function_name):
    weight_matrix=Matrix(weight)
    #print weight_matrix
    input2=[[0]for row in range(len(input_data))]
    for i in range(len(input_data)):
        input2[i][0]=input_data[i]
    input_matrix=Matrix(input2)
    #print input_matrix
    
    bias_matrix=Matrix(bias)
    #print bias_matrix
    #print weight_matrix*input_matrix
    
    output_matrix=weight_matrix*input_matrix+bias_matrix
    output=[]
    for i in range(len(weight)):
        output.append(output_matrix[i,0])
    
    output=fireForList(function_name,output)
    return output


