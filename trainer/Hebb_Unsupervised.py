'''
Created on 2012-6-7

@author: shd101wyy
'''
#Only two layers neural network supported
from pyneuron.neuron_build.neuron_build import NeuronBuilder     
import pylab as py   
class HebbUnsupervisedTrainer(object):

    def __init__(self,net,learning_rate=0.2,decay_rate=0.1):
        '''
        Constructor
        '''
        #self.net=NeuronBuilder(net)
        self.net=net

        self.plot_error=[]
        self.plot_target=[]
        self.plot_output=[]
        
        self.learning_rate=learning_rate
        #self.max_error=max_error
        self.decay_rate=decay_rate
    
    
    def HebbTrainForOnce(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        for key in self.net.neuron_to_neuron_weight:
            from_neuron=key[:key.find('_to_')]
            to_neuron=key[key.find('to_')+3:]  
            for i in range(len(self.net.conditionedNeuron)):
                if self.net.conditionedNeuron[i]==from_neuron:
                    index=to_neuron[3:]
                    input_from_input_layer=self.net.getTheInputToOneNeuron(from_neuron)
                    self.net.neuron_to_neuron_weight[key]=(1-self.decay_rate)*self.net.neuron_to_neuron_weight[key]+self.learning_rate*output[int(index)][0]*input_from_input_layer
        self.net.updateLayerToLayerWeightByNeuronToNeuronWeight()
        print("Finish Training")

        
    def setLearningRate(self,learn_rate):
        self.learning_rate=learn_rate   
    
    def setDecayRate(self,decay_rate):
        self.decay_rate=decay_rate
        
        
    def returnTrainedLayerToLayerWeightAndBias(self):
        return [self.net.layer_to_layer_weight,self.net.bias_to_layer]
       

    
    

        