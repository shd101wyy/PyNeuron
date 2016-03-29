'''
Created on 2012-6-4

@author: shd101wyy
'''
'''
import pylab as py
from sympy import Matrix
from pyneuron.functions.from_function_fire_output import *
from pyneuron.functions.convert_matrix_to_list import convertMatrixToList
class LMSTrainer(object):

    def __init__(self,weight,input_data,bias,output_data,function_name,learning_rate=0.2):

        self.weight=weight
        self.input_data=input_data
        self.bias=bias
        self.output_data=output_data
        self.function_name=function_name
        
        self.plot_error=[]
        self.plot_target=[]
        self.plot_output=[]
        
        self.learning_rate=learning_rate
        
    def setDefaultLearningRate(self):
        num=len(self.input_data)
        sum=Matrix([[0 for column in range(len(self.input_data[0]))]for row in range(len(self.input_data[0]))])
        for elem in self.input_data:
            mat=Matrix([elem])
            mat=mat.transpose()*mat/num
            sum=sum+mat
        eigenvalue=sum.eigenvals()
        max=0
    # print 'sum'
    #print sum
    # print eigenvalue
        for keys in eigenvalue:
            if keys>max:
                max=keys
        self.learning_rate=1/max
    def setLearningRate(self,learn_rate):
        self.learning_rate=learn_rate   

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
            #print 'output_matrix'+str(output_matrix)
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
    
    def LMSTrain(self):
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
                
                
                
                weight_matrix=weight_matrix+2*self.learning_rate*error*input_matrix.transpose()
                bias_matrix=bias_matrix+2*self.learning_rate*error
                self.weight=convertMatrixToList(weight_matrix)
                self.bias=convertMatrixToList(bias_matrix)
                #print bias_matrix
                #print self.bias
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
'''
        
        
import matplotlib.pyplot as py
import numpy as np

class LMSTrainer(object):

    def __init__(self,net,learning_rate=0.2,max_error=0,max_epoch=-1):
        '''
        Constructor
        '''
        #self.net=NeuronBuilder(net)
        self.net=net
        '''purelin
        self.weight=weight
        self.input_data=input_data
        self.bias=bias
        self.output_data=output_data
        self.function_name=function_name
        '''
        
        self.plot_error=[]
        self.plot_target=[]
        self.plot_output=[]
        
        self.learning_rate=learning_rate
        self.max_error=max_error
        self.max_epoch=max_epoch

        
    def setLearningRate(self,learn_rate):
        self.learning_rate=learn_rate   

    def testAllDataPass(self):
        def averageTheList(input_list):
            sum=0
            num=len(input_list)
            for elem in input_list:
                sum+=elem
            return sum/num
        
        all_pass=True
        could_break=False
        error=0.5
        sum=0
        for i in range(len(self.net.input_data)):
            self.net.setInputToInputLayer(self.net.input_data[i])
            output=self.net.getOutputFromLayer('out')
            for j in range(len(self.net.output_data[i])):
                sum+=(self.net.output_data[i][j]-output[j][0])**2
                if self.net.output_data[i][j]!=output[j][0]:
                    all_pass=False
                    could_break=True
            if could_break:
                break
        error=error*sum
        #print 'error is '+str(error)
        self.plot_error.append(error)
        
        if error<=self.max_error:
            all_pass=True
            print('after train the error is '+str(error))
            print('the max error you required is'+str(self.max_error))
            
        if self.max_epoch==-1:
            pass
        else:
            if self.epoch>=self.max_epoch:
                all_pass=True
                print('max epoch is'+str(self.max_epoch))
                print('error is '+str(error))
        return all_pass
    
    def LMSTrain(self):
        self.epoch=0
        while not self.testAllDataPass():
            for i in range(len(self.net.input_data)):
                self.input_to_input_layer=self.net.input_data[i]
                self.target=self.net.output_data[i]
                self.net.setInputToInputLayer(self.input_to_input_layer)
                for out_neuron in self.net.neuron_in_layer['out']:
                    index=int(out_neuron[out_neuron.find('t')+1:])
                    output=self.net.getOutputFromOneNeuron(out_neuron)
                    error=self.target[index]-output
                    for key in self.net.neuron_to_neuron_weight:
                        from_neuron=key[:key.find('_to_')]
                        to_neuron=key[key.find('to_')+3:]
                        if to_neuron==out_neuron:
                            self.net.neuron_to_neuron_weight[key]+=2*self.learning_rate*error*self.net.getOutputFromOneNeuron(from_neuron)
                            self.net.setNeuronToNeuronWeight(from_neuron, to_neuron, self.net.neuron_to_neuron_weight[key])
                            if self.net.has_bias:
                                self.net.bias_to_neuron[to_neuron]+=2*self.learning_rate*error
                                self.net.setBiasToNeuron(to_neuron, self.net.bias_to_neuron[to_neuron])

            self.epoch+=1
            #print self.net.layer_to_layer_weight
            #print self.net.neuron_to_neuron_weight
            #print self.net.bias_to_layer
        print("Finish Training")
        print("Epoches"+str(self.epoch))
        

        
    def plotFigure(self):
        epoch_arange=np.arange(0,self.epoch+1,1)
        #py.title("Target--Output--Error")
        py.plot(epoch_arange,self.plot_error,'bo',label='error')
        #py.plot(epoch_arange,self.plot_target,'ro',label='target')
        #py.plot(epoch_arange,self.plot_output,'yo',label='output')
        #py.xlabel('Epochs*'+str(len(self.input_data)))
        py.xlabel('Epochs')
        py.ylabel('Error')
        py.grid(True)
        py.legend(loc='lower left', numpoints=1)
        py.show()
    
    def setMaxError(self,max_error):
        self.max_error=max_error
        
    def setMaxEpoch(self,max_epoch):
        self.max_epoch=max_epoch
        
        
    def returnTrainedLayerToLayerWeightAndBias(self):
        return [self.net.layer_to_layer_weight,self.net.bias_to_layer]
       
    def setDefaultLearningRate(self):
        from sympy import Matrix
        num=len(self.net.input_data)
        sum=Matrix([[0 for column in range(len(self.net.input_data[0]))]for row in range(len(self.net.input_data[0]))])
        for elem in self.net.input_data:
            mat=Matrix([elem])
            mat=mat.transpose()*mat/num
            sum=sum+mat
        eigenvalue=sum.eigenvals()
        max=0
    # print 'sum'
    #print sum
    # print eigenvalue
        for keys in eigenvalue:
            if keys>max:
                max=keys
        self.learning_rate=1/max
    
    

        