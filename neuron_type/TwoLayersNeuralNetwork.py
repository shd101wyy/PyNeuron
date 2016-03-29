'''
Created on 2012-6-1

@author: shd101wyy
'''

'''
old version two layer neural network

class TwoLayersNeuralNetwork(object):

    def __init__(self,input_num,output_num,function_name='hardlim',weight=None,bias=None,data_set=None):
        
        self.neural_network_type=None
   
        self.function_name=function_name
        self.input_num=input_num
        self.output_num=output_num
        if weight==None:
            self.weight=[[0 for column in range(self.input_num)] for row in range(self.output_num)]
            self.weight=initialize(self.weight)
        else:
            self.weight=weight
        if bias==None:
            self.bias=[[0]for row in range(len(self.weight))]
            self.bias=initialize(self.bias)
        else:
            self.weight=weight
        self.data_set=data_set
        
    def activate(self,input_data):
        output=act(self.weight,input_data,self.bias,self.function_name)
        return output
        
    def setDataSet(self,data_set):
        self.data_set=data_set
        [self.input_data,self.output_data]=data_set.returnDataSet()
        
    def train(self):
        if self.data_set==None:
            print("Please set data sets")
        else:
            self.supervised_train=trainer(self.weight,self.input_data,self.bias,self.output_data,self.function_name)
            self.supervised_train.perceptronTrain()
            [self.weight,self.bias]=self.supervised_train.returnWeightAndBias()
    
    def plotFigure(self):
        self.supervised_train.plotFigure()
        

'''
'''
from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.trainer.LMSTrainer import LMSTrainer
class TwoLayersNeuralNetwork(object):

    def __init__(self,input_num,output_num,function_name='hardlim',weight=None,bias=None,data_set=None,learning_rate=0.2):
        self.function_name=function_name
        self.input_num=input_num
        self.output_num=output_num
        self.data_set=data_set
        self.learning_rate=learning_rate
        
        self.net=NeuronBuilder([self.input_num],[0],[self.output_num])
        self.net.connectTwoLayers('in', 'out')
        if weight!=None:
            self.net.setLayerToLayerWeight('in', 'out', weight)
        if bias!=None:
            self.net.setBiasToLayer('out', bias)
        
            
    def activate(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        return output
        
    def setDataSet(self,data_set):
        self.input_data=None
        self.output_data=None
        self.data_set=data_set
        [self.input_data,self.output_data]=data_set.returnDataSet()
        
    def train(self):
        if self.data_set==None:
            print("Please set data sets")
        else:
            self.trainer=LMSTrainer(self.net.layer_to_layer_weight['in_to_out'],self.input_data,self.net.bias_to_layer['out'],self.output_data,self.function_name,self.learning_rate)
            self.trainer.setDefaultLearningRate()
            self.trainer.LMSTrain()
            [weight,bias]=self.trainer.returnWeightAndBias()
            self.net.setLayerToLayerWeight('in', 'out', weight)
            self.net.setBiasToLayer('out', bias)
    def plotFigure(self):
        self.trainer.plotFigure()
        
  #  def setLearningRate(self,learning_rate):
  #      self.learning_rate=learning_rate
'''  
from neuron_build.neuron_build import NeuronBuilder
from trainer.LMSTrainer import LMSTrainer
class TwoLayersNeuralNetwork(object):

    def __init__(self,input_num,output_num,function_name='hardlim',weight=None,bias=None,data_set=None,learning_rate=0.2,max_error=0,max_epoch=-1):
        self.function_name=function_name
        self.input_num=input_num
        self.output_num=output_num
        self.learning_rate=learning_rate
        self.max_error=max_error
        self.max_epoch=max_epoch
        
        
        self.net=NeuronBuilder([self.input_num],[0],[self.output_num])
        self.net.connectTwoLayers('in', 'out')
        self.net.setLayerFunction('out', self.function_name)
        
        if data_set!=None:
            self.net.setDataSet(data_set)
        self.net.connectTwoLayers('in', 'out')
        if weight!=None:
            self.net.setLayerToLayerWeight('in', 'out', weight)
        if bias!=None:
            self.net.setBiasToLayer('out', bias)
           
    def activate(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        return output
        
    def setDataSet(self,data_set):
        self.net.input_data=None
        self.net.output_data=None
        self.net.setDataSet(data_set)

    def train(self):
        if self.net.data_set==None:
            print("Please set data sets")
        else:
            self.trainer=LMSTrainer(self.net,self.learning_rate,self.max_error,self.max_epoch)
            #self.trainer.setDefaultLearningRate()
            self.trainer.LMSTrain()
            [self.net.layer_to_layer_weight,self.net.bias_to_layer]=self.trainer.returnTrainedLayerToLayerWeightAndBias()
            self.net.updateNeuronToNeuronWeightByLayerToLayerWeight()
            self.net.updateBiasToNeuronByBiasToLayer()
            
    def plotFigure(self):
        self.trainer.plotFigure()
        
    def setLearningRate(self,learning_rate):
        self.learning_rate=learning_rate
        
    def setMaxError(self,max_error):
        self.max_error=max_error
        
    def setMaxEpoch(self,max_epoch):
        self.max_epoch=max_epoch
        
    def returnNeuronBuilder(self):
        return self.net
    
    def setNeuronBuilder(self,net):
        self.net=net
        
    def showNetworkSimulation(self):
        self.net.showNetworkSimulation()