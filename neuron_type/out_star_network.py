'''
Created on 2012-6-7

@author: shd101wyy
'''
from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.trainer.OutstarTrainer import OutstarTrainer
class OutstarNetwork(object):

    def __init__(self,input_num,unconditioned_input_num,function_name='satlins',learning_rate=0.2):
        self.function_name=function_name
        self.input_num=input_num
        self.output_num=unconditioned_input_num
        self.learning_rate=learning_rate
        
        self.net=NeuronBuilder([self.input_num],[0],[self.output_num],has_bias=False)
        for i in range(unconditioned_input_num):
            self.net.connectTwoNeurons('in'+str(i), 'out'+str(i))
        for i in range(input_num-unconditioned_input_num):
            for neuron in self.net.neuron_in_layer['out']:
                self.net.connectTwoNeurons('in'+str(i+unconditioned_input_num),neuron)
        print self.net.neuron_to_neuron_weight
        print self.net.layer_to_layer_weight
        self.net.setLayerFunction('out', self.function_name)
        self.net.setUnconditionedNeuronNum(unconditioned_input_num)
        
           
    def activate(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        return output
        
    def train(self,input_list):
        self.trainer=OutstarTrainer(self.net,self.learning_rate)
        self.trainer.OutstarTrainForOnce(input_list)
        
    def setLearningRate(self,learning_rate):
        self.learning_rate=learning_rate
        
    def returnNeuronBuilder(self):
        return self.net
    
    def setNeuronBuilder(self,net):
        self.net=net
        
    def showNetworkSimulation(self):
        self.net.showNetworkSimulation()