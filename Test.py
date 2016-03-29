'''
Created on 2012-5-31

@author: shd101wyy
'''

'''
from neuron_type.perceptron import Perceptron
from data.DataSet import DataSet

p=Perceptron(2,1)
data=DataSet(2,1)
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
'''

'''
from data.DataSet import DataSet
from neuron_type.hopfield_network import HopfieldNetwork
from tools.save_load_tools import NeuralTools
   
hop=HopfieldNetwork(4,function_name='hardlim')
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
from neuron_type.hopfield_network import HopfieldNetwork
from neuron_type.perceptron import Perceptron
from data.DataSet import DataSet
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
from neuron_build.neuron_build import NeuronBuilder
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
from neuron_build.neuron_build import NeuronBuilder
from data.DataSet import DataSet
from trainer.DeltaTrainer import DeltaTrainer
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
from neuron_type.simple_associative_network_hebb import SimpleAssociativeNetwork
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



# Instar Network
'''
from neuron_type.instar_network import InstarNetwork
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
from neuron_type.out_star_network import OutstarNetwork
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
from neuron_type.backpropagation_neural_network import Backpropagation
from data.DataSet import DataSet
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
from neuron_type.perceptron import Perceptron
from data.DataSet import DataSet
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
from neuron_type.backpropagation_neural_network import Backpropagation
from data.DataSet import DataSet
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
from neuron_type.instar_network import InstarNetwork
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
'''
from neuron_build.neuron_build import NeuronBuilder
from trainer.Kohonen import KohonenTrainer
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
'''