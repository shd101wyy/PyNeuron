'''
Created on 2012-5-31

@author: shd101wyy
'''
'''
This is a perceptron learning rule


'''
from sympy import Matrix
from pyneuron.functions.from_function_fire_output import *
from pyneuron.functions.convert_matrix_to_list import convertMatrixToList
import pylab as py
class trainer(object):
    def __init__(self,weight,input_data,bias,output_data,function_name):
        self.weight=weight
        self.input_data=input_data
        self.bias=bias
        self.output_data=output_data
        self.function_name=function_name
        
        self.plot_error=[]
        self.plot_target=[]
        self.plot_output=[]
    def testAllDataPass(self):
        all_pass=True
        weight_matrix=Matrix(self.weight)
        bias_matrix=Matrix(self.bias)
        for i in range(len(self.input_data)):
            input_matrix=Matrix([self.input_data[i]])
            input_matrix=input_matrix.transpose()
            #target_matrix=Matrix([self.output_data[i]])
            #target_matrix=target_matrix.transpose()
            output_matrix=weight_matrix*input_matrix+bias_matrix
            output=[]
            for j in range(len(self.weight)):
                output.append(output_matrix[j,0])
            output=fireForList(self.function_name,output)
            if output!=self.output_data[i]:
                all_pass=False
                #print 'output'+str(output)
                #print 'target'+str(self.output_data[i])                
                break
            #print 'output'+str(output)
            #print 'target'+str(self.output_data[i])
        #print all_pass
        return all_pass
    
    def perceptronTrain(self):
        def meanSquare(matrix):
            rows=matrix.rows
            cols=matrix.cols
            a=0
            for i in range(rows):
                for j in range(cols):
                    a=a+matrix[i,j]**2
            a=a**0.5
            return a
        
        

        self.epoch=0
        while not self.testAllDataPass():
            for i in range(len(self.input_data)):
                weight_matrix=Matrix(self.weight)
                bias_matrix=Matrix(self.bias)
                input_matrix=Matrix([self.input_data[i]])
                input_matrix=input_matrix.transpose()
                target_matrix=Matrix([self.output_data[i]])
                target_matrix=target_matrix.transpose()     
                #print "target_matrix:"
                #print target_matrix
                #print 'output_matrix:'
                #print fireForMatrix(self.function_name,weight_matrix*input_matrix+bias_matrix)
                error=target_matrix-fireForMatrix(self.function_name,weight_matrix*input_matrix+bias_matrix)
                #print 'error'+str(error)
                #print 'output'+str(weight_matrix*input_matrix+bias_matrix)
                #print 'after fire output'+str(fireForMatrix(self.function_name,weight_matrix*input_matrix+bias_matrix))
                #print 'target'+str(target_matrix)
                
                #experiment
                self.plot_error.append(meanSquare(error))
                self.plot_target.append(meanSquare(target_matrix))
                self.plot_output.append(meanSquare(fireForMatrix(self.function_name,weight_matrix*input_matrix+bias_matrix)))
                
                
                
                weight_matrix=weight_matrix+error*input_matrix.transpose()
                bias_matrix=bias_matrix+error
                self.weight=convertMatrixToList(weight_matrix)
                self.bias=convertMatrixToList(bias_matrix)
                #print 'weight'+str(self.weight)
                #print 'bias'+str(self.bias)
            self.epoch+=1
        print("Finish Training")
        print("Epoches"+str(self.epoch))
        
        
        
    def returnWeightAndBias(self):
        return [self.weight,self.bias]
    def plotFigure(self):
        epoch_arange=py.arange(0,self.epoch*len(self.input_data),1)
        py.title("Target--Output--Error")
        py.plot(epoch_arange,self.plot_error,'bo',label='error')
        py.plot(epoch_arange,self.plot_target,'ro',label='target')
        py.plot(epoch_arange,self.plot_output,'yo',label='output')
        py.xlabel('Epochs*'+str(len(self.input_data)))
        py.grid(True)
        py.legend(loc='lower left', numpoints=1)
        py.show()
        