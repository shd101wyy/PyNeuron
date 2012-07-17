'''
Created on 2012-6-7

@author: shd101wyy

I just find that decay_rate can be understood as how well you often forget something
'''
from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.trainer.Hebb_Unsupervised import HebbUnsupervisedTrainer
class SimpleAssociativeNetwork(object):

    def __init__(self,input_num,output_num,unconditioned_input_num,function_name='hardlim',learning_rate=0.2,decay_rate=0.1):
        self.function_name=function_name
        self.input_num=input_num
        self.output_num=output_num
        self.learning_rate=learning_rate
        self.decay_rate=decay_rate
        
        self.net=NeuronBuilder([self.input_num],[0],[self.output_num])
        self.net.connectTwoLayers('in', 'out')
        self.net.setLayerFunction('out', self.function_name)
        self.net.setUnconditionedNeuronNum(unconditioned_input_num)
        
           
    def activate(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        return output
        
    def train(self,input_list):
        self.trainer=HebbUnsupervisedTrainer(self.net,self.learning_rate,self.decay_rate)
        self.trainer.HebbTrainForOnce(input_list)
        
    def setLearningRate(self,learning_rate):
        self.learning_rate=learning_rate
        
    def setDecayRate(self,decay_rate):
        self.decay_rate=decay_rate
        
    def returnNeuronBuilder(self):
        return self.net
    
    def setNeuronBuilder(self,net):
        self.net=net
        
    def showNetworkSimulation(self):
        self.net.showNetworkSimulation()