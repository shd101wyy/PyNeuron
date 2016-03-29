'''
Created on 2012-6-5

@author: shd101wyy
'''
from neuron_build.neuron_build import NeuronBuilder
from trainer.DeltaTrainer import DeltaTrainer
class Backpropagation(object):
    def __init__(self,input_layer_list,hidden_layer_list,output_layer_list,learning_rate=0.2,max_error=0.01,max_epoch=-1):
        '''
        Constructor
        '''
        self.net=NeuronBuilder(input_layer_list,hidden_layer_list,output_layer_list)
        self.net.setLayerFunction('out', 'purelin')
        for i in range(len(self.net.hidden_layers)):
            self.net.setLayerFunction('hid'+str(i),'logsig')
        
        self.net.connectTwoLayers('in', 'hid0')
        if len(self.net.hidden_layers)!=1:
            for i in range(len(self.net.hidden_layers)-1):
                self.net.connectTwoLayers('hid'+str(i), 'hid'+str(i+1))
        self.net.connectTwoLayers('hid'+str(len(self.net.hidden_layers)-1), 'out')
        
        self.learning_rate=learning_rate
        self.max_error=max_error
        self.max_epoch=max_epoch
        
    def activate(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        return output
        
    def setDataSet(self,data_set):
        self.data_set=data_set
        [self.net.input_data,self.net.output_data]=data_set.returnDataSet()
        
    def train(self):
        if self.data_set==None:
            print("Please set data sets")
        else:
            self.trainer=DeltaTrainer(self.net)
            self.trainer.setLearningRate(self.learning_rate)
            self.trainer.setMaxError(self.max_error)
            self.trainer.setMaxEpoch(self.max_epoch)
            self.trainer.DeltaTrain()
            #[weight,bias]=self.trainer.returnTrainedLayerToLayerWeightAndBias()
            [self.net.layer_to_layer_weight,self.net.bias_to_layer]=self.trainer.returnTrainedLayerToLayerWeightAndBias()
            
            # print self.net.neuron_to_neuron_weight
            self.net.updateNeuronToNeuronWeightByLayerToLayerWeight()
            self.net.updateBiasToNeuronByBiasToLayer()
            # print self.net.neuron_to_neuron_weight

    def plotFigure(self):
        self.trainer.plotFigure()
        
    def setLearningRate(self,learning_rate):
        self.learning_rate=learning_rate
        
    def setMaxError(self,max_error):
        self.max_error=max_error
        
    def setMaxEpoch(self,max_epoch):
        self.max_epoch=max_epoch
        
    def showNetworkSimulation(self):
        self.net.showNetworkSimulation()
  
  
