'''
Created on 2012-6-7

@author: shd101wyy
'''

from neuron_build.neuron_build import NeuronBuilder
from trainer.InstarTrainer import InstarTrainer
class InstarNetwork(object):

    def __init__(self,input_num,output_num,unconditioned_input_num,function_name='hardlim',learning_rate=0.2):
        self.function_name=function_name
        self.input_num=input_num
        self.output_num=output_num
        self.learning_rate=learning_rate
        
        self.net=NeuronBuilder([self.input_num],[0],[self.output_num])
        self.net.connectTwoLayers('in', 'out')
        self.net.setLayerFunction('out', self.function_name)
        self.net.setUnconditionedNeuronNum(unconditioned_input_num)
        
           
    def activate(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        return output
        
    def train(self,input_list):
        self.trainer=InstarTrainer(self.net,self.learning_rate)
        self.trainer.InstarTrainForOnce(input_list)
        
    def setLearningRate(self,learning_rate):
        self.learning_rate=learning_rate
        
    def returnNeuronBuilder(self):
        return self.net
    
    def setNeuronBuilder(self,net):
        self.net=net
    
    def showNetworkSimulation(self):
        self.net.showNetworkSimulation()