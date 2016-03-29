'''
Created on 2012-6-7

@author: shd101wyy
'''
#Only two layers neural network supported
class KohonenTrainer(object):

    def __init__(self,net,learning_rate=0.2):
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
    
    #I do not make sure whether it is right or not   
    def KohonenTrainForOnce(self,input_list):
        self.net.setInputToInputLayer(input_list)
        output=self.net.getOutputFromLayer('out')
        for key in self.net.neuron_to_neuron_weight:
            from_neuron=key[:key.find('_to_')]
            to_neuron=key[key.find('to_')+3:]  
            for i in range(len(self.net.conditionedNeuron)):
                if self.net.conditionedNeuron[i]==from_neuron:
                    index=to_neuron[3:]
                    input_from_input_layer=self.net.getTheInputToOneNeuron(from_neuron)
                    #self.net.neuron_to_neuron_weight[key]=(1-self.decay_rate)*self.net.neuron_to_neuron_weight[key]+self.learning_rate*output[int(index)][0]*input_from_input_layer
                    self.net.neuron_to_neuron_weight[key]=self.net.neuron_to_neuron_weight[key]+self.learning_rate*(input_from_input_layer-self.net.neuron_to_neuron_weight[key])
        self.net.updateLayerToLayerWeightByNeuronToNeuronWeight()
        print("Finish Training")
    
    def KohonenTrainForWinnerNeuron(self,input_list,competitive_layer_key):
        self.net.setInputToInputLayer(input_list)
        #output=self.net.getOutputFromLayer('out')
        winner_neuron=self.net.getWinnerNeuronFromCompetitiveLayer(competitive_layer_key)
        for key in self.net.neuron_to_neuron_weight:
            from_neuron=key[:key.find('_to_')]
            to_neuron=key[key.find('to_')+3:]  
            if to_neuron==winner_neuron:
                input_from_from_neuron=self.net.getTheInputToOneNeuron(from_neuron)
                #self.net.neuron_to_neuron_weight[key]=(1-self.decay_rate)*self.net.neuron_to_neuron_weight[key]+self.learning_rate*output[int(index)][0]*input_from_input_layer
                self.net.neuron_to_neuron_weight[key]=self.net.neuron_to_neuron_weight[key]+self.learning_rate*(input_from_from_neuron-self.net.neuron_to_neuron_weight[key])
        self.net.updateLayerToLayerWeightByNeuronToNeuronWeight()
        print("Finish Training")
    
    def setLearningRate(self,learn_rate):
        self.learning_rate=learn_rate   
          
    def returnTrainedLayerToLayerWeightAndBias(self):
        return [self.net.layer_to_layer_weight,self.net.bias_to_layer]
       

    
    

        