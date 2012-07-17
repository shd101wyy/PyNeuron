'''
Created on 2012-5-31

@author: shd101wyy
'''
'''
Hopfield Network
Recurrent Layer:
    function:
        satlins
'''
from pyneuron.neuron_type.TwoLayersNeuralNetwork import TwoLayersNeuralNetwork
class HopfieldNetwork(TwoLayersNeuralNetwork):
    def __init__(self,input_num=2,function_name='hardlim',weight=None,bias=None,data_set=None,learning_rate=0.2,max_error=0,max_epoch=-1):
        
        TwoLayersNeuralNetwork.__init__(self, input_num, input_num, function_name, weight, bias, data_set,learning_rate,max_error,max_epoch)
        
        for i in range(len(self.net.layer_to_layer_weight['in_to_out'])):
            self.net.layer_to_layer_weight['in_to_out'][i][i]=0
        for i in range(len(self.net.layer_to_layer_weight['in_to_out'])):
            for j in range(len(self.net.layer_to_layer_weight['in_to_out'][0])):
                self.net.layer_to_layer_weight['in_to_out'][i][j]=self.net.layer_to_layer_weight['in_to_out'][j][i]
        self.net.updateNeuronToNeuronWeightByLayerToLayerWeight()
    
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
'''
BackUp
from pyneuron.functions.initialize_weight_bias import initialize
from pyneuron.functions.activate import activate as act
from pyneuron.trainer.trainer import trainer
class HopfieldNetwork(object):
    def __init__(self,input_num,function_name='satlins',weight=None,bias=None,data_set=None):
        
        self.neural_network_type="Hopfield"
        
        self.function_name=function_name
        self.input_num=input_num
        self.output_num=input_num
        self.data_set=data_set

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

        for i in range(len(self.weight)):
            self.weight[i][i]=0
        
        
        
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
            self.supervised_train.train()
            [self.weight,self.bias]=self.supervised_train.returnWeightAndBias()
    
    def plotFigure(self):
        self.supervised_train.plotFigure()
        


'''      