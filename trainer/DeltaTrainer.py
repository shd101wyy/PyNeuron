'''
Created on 2012-6-4

@author: shd101wyy
'''
'''

This version of delta trainer makes some mistakes, the algorithm was wrong and I improved it.
Now the new version of delta trainer is right

import pylab as py
from pyneuron.functions.from_function_fire_output import *
from pyneuron.functions.convert_matrix_to_list import convertMatrixToList
from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.functions.functions import diff_function

class DeltaTrainer(object):

    def __init__(self,net,learning_rate=0.2,max_error=0,max_epoch=-1):
       
        #self.net=NeuronBuilder(net)
        self.net=net

       
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
        print error
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
    
    def DeltaTrain(self):
        self.epoch=0
        while not self.testAllDataPass():
            for i in range(len(self.net.input_data)):
                self.input_to_input_layer=self.net.input_data[i]
                self.target=self.net.output_data[i]
                self.net.setInputToInputLayer(self.input_to_input_layer)
                for keys in self.net.neuron_to_neuron_weight.keys():
                    if self.net.neuron_to_neuron_weight[keys]==None:
                        continue
                    from_neuron=keys[:keys.find('_to_')]
                    to_neuron=keys[keys.find('to_')+3:]
                    sensitivity=self.getSensitivityFromOneNeuron(to_neuron)
                    
                    self.net.neuron_to_neuron_weight[keys]+=self.learning_rate*sensitivity*self.net.getOutputFromOneNeuron(from_neuron)
                    #self.net.bias_to_neuron[to_neuron]+=self.learning_rate*sensitivity
                    self.net.setNeuronToNeuronWeight(from_neuron, to_neuron, self.net.neuron_to_neuron_weight[keys])
                    
                    if self.net.has_bias:
                        self.net.bias_to_neuron[to_neuron]+=self.learning_rate*sensitivity
                        self.net.setBiasToNeuron(to_neuron, self.net.bias_to_neuron[to_neuron])
                    
            self.epoch+=1
            #print self.net.layer_to_layer_weight
            print self.net.neuron_to_neuron_weight
        print("Finish Training")
        print("Epoches"+str(self.epoch))
        
    def getSensitivityFromOneNeuron(self,neuron_key):
        if neuron_key.find('out')!=-1:
            sensitivity=self.getErrorFromOneOutputNeuron(self.input_to_input_layer, self.target, neuron_key)*diff_function(self.net.neuron_function[neuron_key],self.net.getTheInputToOneNeuron(neuron_key))
        else:
            sensitivity=1
            sum_of_weight_and_former_sensitivitiy=0
            #for keys in self.net.neuron_to_neuron_weight:  The same
            for keys in self.net.neuron_to_neuron_weight.keys():
                from_neuron=keys[:keys.find('_to_')]
                to_neuron=keys[keys.find('to_')+3:]
                if from_neuron==neuron_key and self.net.neuron_to_neuron_weight[keys]!=None:
                    sum_of_weight_and_former_sensitivitiy+=self.net.neuron_to_neuron_weight[keys]*self.getSensitivityFromOneNeuron(to_neuron)
            #diff_function(self.net.neuron_function[neuron_key],self.net.getTheInputToOneNeuron(neuron_key))
            sensitivity=diff_function(self.net.neuron_function[neuron_key],self.net.getTheInputToOneNeuron(neuron_key))*sum_of_weight_and_former_sensitivitiy
        return sensitivity
    
    def getErrorFromOneOutputNeuron(self,input_list,output_list,neuron_key):
        if neuron_key.find('out')==-1:
            print("Mistake occurred, the error you want to get is not from output layer")
            return None
        else:
            self.net.setInputToInputLayer(input_list)
            output=self.net.getOutputFromOneNeuron(neuron_key)
            index=neuron_key[neuron_key.find('out')+3:]
            target=output_list[int(index)]
            return target-output
        
    def plotFigure(self):
        epoch_arange=py.arange(0,self.epoch+1,1)
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
'''      

# New version of delta trainer
'''
Created on 2012-6-9

@author: shd101wyy
'''

#This is an experiment version whose algorithm is recently developed

import pylab as py
from pyneuron.functions.from_function_fire_output import *
from pyneuron.functions.convert_matrix_to_list import convertMatrixToList
from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.functions.functions import diff_function

class DeltaTrainer(object):

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
        print error
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
    
    def DeltaTrain(self):
        import copy
        self.epoch=0
        while not self.testAllDataPass():
            for i in range(len(self.net.input_data)):
                self.input_to_input_layer=self.net.input_data[i]
                self.target=self.net.output_data[i]
                self.net.setInputToInputLayer(self.input_to_input_layer)
                
                self.neuron_to_neuron_weight_clone=copy.deepcopy(self.net.neuron_to_neuron_weight)
                self.bias_to_neuron_clone=copy.deepcopy(self.net.bias_to_neuron)
                
                for keys in self.net.neuron_to_neuron_weight.keys():
                    if self.net.neuron_to_neuron_weight[keys]==None:
                        continue
                    from_neuron=keys[:keys.find('_to_')]
                    to_neuron=keys[keys.find('to_')+3:]
                    sensitivity=self.getSensitivityFromOneNeuron(to_neuron)
                    
                    self.neuron_to_neuron_weight_clone[keys]+=self.learning_rate*sensitivity*self.net.getOutputFromOneNeuron(from_neuron)
                    #self.net.neuron_to_neuron_weight[keys]+=self.learning_rate*sensitivity*self.net.getOutputFromOneNeuron(from_neuron)
                    #self.net.bias_to_neuron[to_neuron]+=self.learning_rate*sensitivity
                    #self.net.setNeuronToNeuronWeight(from_neuron, to_neuron, self.net.neuron_to_neuron_weight[keys])
                    
                    if self.net.has_bias:
                        #self.net.bias_to_neuron[to_neuron]+=self.learning_rate*sensitivity
                        #self.net.setBiasToNeuron(to_neuron, self.net.bias_to_neuron[to_neuron])
                        self.bias_to_neuron_clone[to_neuron]+=self.learning_rate*sensitivity
                        
                self.net.neuron_to_neuron_weight=copy.deepcopy(self.neuron_to_neuron_weight_clone)
                self.net.bias_to_neuron=copy.deepcopy(self.bias_to_neuron_clone)
            
            self.epoch+=1
            #print self.net.layer_to_layer_weight
            print self.net.neuron_to_neuron_weight
        print("Finish Training")
        print("Epoches"+str(self.epoch))
        self.net.updateBiasToLayerByBiasToNeuron()
        self.net.updateLayerToLayerWeightByNeuronToNeuronWeight()
        
        
    def getSensitivityFromOneNeuron(self,neuron_key):
        if neuron_key.find('out')!=-1:
            sensitivity=self.getErrorFromOneOutputNeuron(self.input_to_input_layer, self.target, neuron_key)*diff_function(self.net.neuron_function[neuron_key],self.net.getTheInputToOneNeuron(neuron_key))
        else:
            sensitivity=1
            sum_of_weight_and_former_sensitivitiy=0
            #for keys in self.net.neuron_to_neuron_weight:  The same
            for keys in self.net.neuron_to_neuron_weight.keys():
                from_neuron=keys[:keys.find('_to_')]
                to_neuron=keys[keys.find('to_')+3:]
                if from_neuron==neuron_key and self.net.neuron_to_neuron_weight[keys]!=None:
                    sum_of_weight_and_former_sensitivitiy+=self.net.neuron_to_neuron_weight[keys]*self.getSensitivityFromOneNeuron(to_neuron)
            #diff_function(self.net.neuron_function[neuron_key],self.net.getTheInputToOneNeuron(neuron_key))
            sensitivity=diff_function(self.net.neuron_function[neuron_key],self.net.getTheInputToOneNeuron(neuron_key))*sum_of_weight_and_former_sensitivitiy
        return sensitivity
    
    def getErrorFromOneOutputNeuron(self,input_list,output_list,neuron_key):
        if neuron_key.find('out')==-1:
            print("Mistake occurred, the error you want to get is not from output layer")
            return None
        else:
            self.net.setInputToInputLayer(input_list)
            output=self.net.getOutputFromOneNeuron(neuron_key)
            index=neuron_key[neuron_key.find('out')+3:]
            target=output_list[int(index)]
            return target-output
        
    def plotFigure(self):
        epoch_arange=py.arange(0,self.epoch+1,1)
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
       

    
    
    
