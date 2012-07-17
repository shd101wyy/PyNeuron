'''
Created on 2012-5-31

@author: shd101wyy
'''
'''



from pyneuron.neuron_type.perceptron import Perceptron
from pyneuron.data.DataSet import DataSet

p=Perceptron(2,1)
data=DataSet(2,1)first_layer_key
data.addItem([1,1],[0])
data.addItem([0,0],[1])
data.addItem([0,1],[1])
data.addItem([1,0],[0])
data.addItem([0.5,0.5],[0])
p.setDataSet(data)
p.train()
p.plotFigure()
print p.activate([1,1])
print p.activate([0.5,0.5])

from pyneuron.data.DataSet import DataSet
from pyneuron.neuron_type.perceptron import perceptron     
p=perceptron(2,2)
data1=DataSet(2,2)
data1.addItem([-2,1],[0,1])
data1.addItem([-1,2],[0,1])
data1.addItem([1,1],[0,0])
data1.addItem([1,2],[0,0])
data1.addItem([2,0],[1,0])
data1.addItem([2,-1],[1,0])
data1.addItem([-1,-1],[1,1])
data1.addItem([-2,-2],[1,1])
p.setDataSet(data1)
p.train()
print p.weight
print p.bias
print p.activate([-2,1])
print p.activate([-1,2])
print p.activate([1,1])
print p.activate([1,2])
print p.activate([2,0])
print p.activate([2,-1])
print p.activate([-1,-1])
print p.activate([-2,-2])


#   This is quick and dirty, but it will show the results
subplot(3, 1, 1)
plot([i[1] for i in population])
title("Population")
grid(True)

subplot(3, 1, 2)
plot(test_positions, all_targets1, 'bo', label='targets')
plot(test_positions, allactuals, 'ro', label='actuals')
grid(True)
legend(loc='lower left', numpoints=1)
title("Test Target Points vs Actual Points")

subplot(3, 1, 3)
plot(range(1, len(net.accum_mse) + 1, 1), net.accum_mse)
xlabel('epochs')
ylabel('mean squared error')
grid(True)
title("Mean Squared Error by Epoch")

show()
'''
'''
from pyneuron.data.DataSet import DataSet
from pyneuron.neuron_type.hopfield_network import hopfield_network
from pyneuron.tools.save_load_tools import NeuralTools

   
hop=hopfield_network(4,function_name='hardlim')
data=DataSet(4,4)
data.addItem([1,1,0,0],[0,0,1,1])
data.addItem([0,0,1,1],[1,1,0,0])
data.addItem([1,0,1,0],[0,1,0,1])
data.addItem([0,1,0,1],[1,0,1,0])
hop.setDataSet(data)
hop.train()
print hop.activate([1,1,0,0])
hop.plotFigure()
tools=NeuralTools()
tools.saveNetwork(hop, 'SavedHopfield.nnt')
'''
'''
import os
print os.path.exists('SavedHopfield.nnt')
file=open('SavedHopfield.nnt','r')
output=[]
for lines in file:
    output.append(lines)
print output
dic={}
for line in output:
    print line
    dic[line[0:line.find(':')]]=line[line.find(':')+1:line.find('\\')]
print dic

print dic['weight']


def changeStringListToList(inputString,row,column):
    output=[[0 for j in range(column)]for i in range(row)]
    
    inputString=inputString[1:len(inputString)-1]
    inputString=inputString.replace('[','')
    inputString=inputString.replace(']','')
    inputString=inputString.replace(',','')
    inputString=inputString.split(" ")
    for i in range(row):
        for j in range(column):
            output[i][j]=float(inputString[i*column+j])
   
    return output
    
    
print changeStringListToList(dic['weight'],int(dic['output_num']),int(dic['input_num']))

'''
'''
from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.data.DataSet import DataSet
from pyneuron.trainer.LMSTrainer import LMSTrainer
class ExperimentPerceptron(object):
    def __init__(self,input_num,output_num,function_name='hardlim'):
        self.input_num=input_num
        self.output_num=output_num
        self.function_name=function_name
        self.net=NeuronBuilder([self.input_num],[0],[self.output_num])
        self.net.connectTwoLayers('in', 'out')
        self.net.setLayerFunction('out', self.function_name)
        self.weight=self.net.layer_to_layer_weight['in_to_out']
        self.bias=self.net.bias_to_layer['out']
    def setDataSet(self,data_set):
        self.input_data=None
        self.output_data=None
        self.data_set=data_set
        [self.input_data,self.output_data]=self.data_set.returnDataSet()
    def train(self):
        self.trainer=LMSTrainer(self.weight,self.input_data,self.bias,self.output_data,'hardlim')
        self.trainer.setDefaultLearningRate()
        self.trainer.LMSTrain()
        [self.weight,self.bias]=self.trainer.returnWeightAndBias()
        self.net.setLayerToLayerWeight('in', 'out', self.weight)
        self.net.setBiasToLayer('out', self.bias)
    def plotFigure(self):
        self.plotFigure()
    def activate(self,input_list):
        self.net.setInputToInputLayer(input_list)
        return self.net.getOutputFromLayer('out')
p=ExperimentPerceptron(2,2)
data=DataSet(2,2)
data.addItem([1,1], [1,1])
data.addItem([1,0], [0,0])
data.addItem([0,1], [0,0])
data.addItem([0,0], [0,0])
p.setDataSet(data)
p.train()
print p.activate([1,1])
#print p.net.neuron_to_neuron_weight
'''
'''
from pyneuron.neuron_type.hopfield_network import HopfieldNetwork
from pyneuron.neuron_type.perceptron import Perceptron
from pyneuron.data.DataSet import DataSet
h=Perceptron(4,4,'hardlim')
data=DataSet(4,4)
data.addItem([1,1,1,1],[0,0,0,0])
data.addItem([1,0,1,0],[0,1,0,1])
data.addItem([1,0,0,1],[0,1,1,0])
data.addItem([1,1,0,0],[0,0,1,1])
data.addItem([1,1,0,1],[0,0,1,0])
data.addItem([1,0,1,1],[0,1,0,0])
data.addItem([0,1,1,1],[1,0,0,0])
data.addItem([0,0,1,1],[1,1,0,0])
data.addItem([0,0,0,1],[1,1,1,0])
data.addItem([0,1,0,1],[1,0,1,0])
data.addItem([0,1,1,0],[1,0,0,1])
h.setDataSet(data)
h.train()
h.plotFigure()

'''
'''
from pyneuron.neuron_build.neuron_build import NeuronBuilder
neuron=NeuronBuilder([2],[3],[2])
neuron.connectTwoLayers('in', 'hid0')
neuron.connectTwoLayers('hid0','out')
neuron.setLayerFunction('hid0', 'logsig')
neuron.setLayerFunction('out','purelin')
neuron.setInputToInputLayer([1,1])
print neuron.getOutputFromLayer('hid0')
print neuron.getOutputFromLayer('out')
'''
'''
from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.data.DataSet import DataSet
from pyneuron.trainer.DeltaTrainer import DeltaTrainer
net=NeuronBuilder([2],[3],[1])
net.connectTwoLayers('in', 'hid0')
net.connectTwoLayers('hid0', 'out')
net.setLayerFunction('hid0', 'logsig')
net.setLayerFunction('out', 'purelin')
data=DataSet(2,1)

data.addItem([0.5,0.5], [1])
data.addItem([1,0.5], [1])
data.addItem([0.75,1], [1])
data.addItem([0.75,0.75], [0])
data.addItem([1,1],[0])

net.setDataSet(data)


delta=DeltaTrainer(net,0.2)
delta.setMaxError(0.01)
delta.DeltaTrain()
delta.plotFigure()

'''
'''
#Associative Simple Network
from pyneuron.neuron_type.simple_associative_network_hebb import SimpleAssociativeNetwork
san=SimpleAssociativeNetwork(2,1,1)
san.setDecayRate(0.3)
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,0])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron
san.train([1,1])
print san.activate([0,1])
print san.net.layer_to_layer_weight
print san.net.neuron_to_neuron_weight
print san.net.conditionedNeuron
print san.net.unconditionedNeuron
print san.net.bias_to_neuron

'''

'''
# Instar Network

from pyneuron.neuron_type.instar_network import InstarNetwork
instar=InstarNetwork(4,1,1)
print instar.activate([0,1,-1,1])
print instar.net.layer_to_layer_weight
print instar.net.bias_to_layer
instar.train([0,1,-1,-1])
print instar.activate([0,1,-1,1])
print instar.net.layer_to_layer_weight
print instar.net.bias_to_layer              
instar.train([1,1,-1,-1])
print instar.activate([0,1,-1,1])
print instar.net.layer_to_layer_weight
print instar.net.bias_to_layer    
instar.train([1,1,-1,-1])
print instar.activate([0,1,-1,1])
print instar.net.layer_to_layer_weight
print instar.net.bias_to_layer    
instar.train([1,1,-1,-1])
print instar.activate([0,1,-1,1])
print instar.net.layer_to_layer_weight
print instar.net.bias_to_layer    
instar.train([1,1,-1,-1])
print instar.activate([0,1,-1,1])
print instar.net.layer_to_layer_weight
print instar.net.bias_to_layer    
instar.train([1,1,-1,-1])
print instar.activate([0,1,-1,1])
print instar.net.layer_to_layer_weight
print instar.net.bias_to_layer    
'''
'''
# Outstar network
from pyneuron.neuron_type.out_star_network import OutstarNetwork
outstar=OutstarNetwork(4,3)
print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight
print outstar.net.bias_to_layer
outstar.train([0,1,-1,-1])
print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight
            
outstar.train([1,1,-1,-1])
print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight
  
outstar.train([1,1,-1,-1])
print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight
  
outstar.train([1,1,-1,-1])
print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight
  
outstar.train([1,1,-1,-1])
print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight
  
outstar.train([1,1,-1,-1])
print outstar.activate([0,1,-1,1])
print outstar.net.layer_to_layer_weight
'''

'''
from pyneuron.neuron_type.backpropagation_neural_network import Backpropagation
from pyneuron.data.DataSet import DataSet
b=Backpropagation([2],[3,2],[1])
print b.net.layer_to_layer_weight
print b.net.neuron_to_neuron_weight
data=DataSet(2,1)
data.addItem([0,0],[1])
data.addItem([1,1],[1])
data.addItem([1,0],[0])
data.addItem([0,1],[0])
data.addItem([0.5,0.6],[0.7])
b.setDataSet(data)
b.showNetworkSimulation()
b.setLearningRate(0.5)
b.setMaxError(0.00000001)
b.train()
b.plotFigure()
print b.net.neuron_to_neuron_weight
print b.activate([0.5,0.6])

'''


'''

from pyneuron.neuron_type.perceptron import Perceptron
from pyneuron.data.DataSet import DataSet
p=Perceptron(2,1)
data=DataSet(2,1)
data.addItem([0,0], [0])
data.addItem([1,0], [0])
data.addItem([0,1], [1])
data.addItem([1,1], [1])
data.addItem([0.75,0.75],[1])
data.addItem([0.5,0.5],[1])
p.setDataSet(data)
p.showNetworkSimulation()
p.train()
p.plotFigure()
print p.activate([0,0])
print p.activate([1,0])
print p.activate([0,1])
print p.activate([1,1])
print p.activate([0.75,0.75])
print p.activate([0.5,0.5])
'''
'''
from pyneuron.neuron_type.backpropagation_neural_network import Backpropagation
from pyneuron.data.DataSet import DataSet
b=Backpropagation([2],[3],[2])
print b.net.layer_to_layer_weight
print b.net.neuron_to_neuron_weight
data=DataSet(2,2)
data.addItem([0,0],[1,1])
data.addItem([1,1],[1,1])
data.addItem([1,0],[0,0])
data.addItem([0,1],[0,1])
data.addItem([0.5,0.6],[0.7,0.7])
b.setDataSet(data)
b.setLearningRate(0.2)
#b.showNetworkSimulation()
b.setMaxError(0.0001)
b.train()
#b.plotFigure()
#.net.updateBiasToNeuronByBiasToLayer()
print b.net.neuron_to_neuron_weight
print b.activate([0.5,0.6])
print b.activate([0,0])
print b.activate([1,1])
print b.activate([1,0])
print b.activate([0,1])
print b.activate([9,9])
'''
'''
from pyneuron.neuron_type.instar_network import InstarNetwork
i=InstarNetwork(2,1,1)
i.showNetworkSimulation()
i.setLearningRate(0.5)
i.train([0,1])
print i.activate([0,1])
i.train([1,1])
print i.activate([1,1])
i.train([1,1])
print i.activate([0,1])
i.train([1,1])
print i.activate([0,1])
i.train([1,1])
print i.activate([0,1])
'''

from pyneuron.neuron_build.neuron_build import NeuronBuilder
from pyneuron.trainer.Kohonen import KohonenTrainer
net=NeuronBuilder([2],[0],[5])
net.connectTwoLayers('in', 'out')
net.setLayerFunction('out', 'compet')
net.setInputToInputLayer([1,1])
net.showNetworkSimulation()
k=KohonenTrainer(net)
k.KohonenTrainForWinnerNeuron([1,1],'out')
print net.neuron_to_neuron_weight
k.KohonenTrainForWinnerNeuron([1,1],'out')
print net.neuron_to_neuron_weight
k.KohonenTrainForWinnerNeuron([1,1],'out')
print net.neuron_to_neuron_weight