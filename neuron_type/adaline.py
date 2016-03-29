'''
Created on 2012-6-7

@author: shd101wyy
'''
from neuron_type.TwoLayersNeuralNetwork import TwoLayersNeuralNetwork
class Adaline(TwoLayersNeuralNetwork):
    def __init__(self,input_num=2,output_num=2,function_name='purelin',weight=None,bias=None,data_set=None,learning_rate=0.2,max_error=0,max_epoch=-1):
        TwoLayersNeuralNetwork.__init__(self, input_num, output_num, function_name, weight, bias, data_set,learning_rate,max_error,max_epoch)
        
        
    def activate(self,input_list):
        return TwoLayersNeuralNetwork.activate(self, input_list)
        
    def setDataSet(self,data_set):
        TwoLayersNeuralNetwork.setDataSet(self, data_set)
        
    def train(self):
        TwoLayersNeuralNetwork.train(self)
    
    def plotFigure(self):
        TwoLayersNeuralNetwork.plotFigure(self)
    
    def setLearningRate(self,learning_rate):
        TwoLayersNeuralNetwork.setLearningRate(self, learning_rate)

    def setMaxError(self,max_error):
        TwoLayersNeuralNetwork.setMaxError(self, max_error)
        
    def setMaxEpoch(self,max_epoch):
        TwoLayersNeuralNetwork.setMaxEpoch(self, max_epoch)
        
    def returnNeuronBuilder(self):
        return TwoLayersNeuralNetwork.returnNeuronBuilder(self)
    
    def setNeuronBuilder(self,net):
        self.net=net
        
    def showNetworkSimulation(self):
        TwoLayersNeuralNetwork.showNetworkSimulation(self)