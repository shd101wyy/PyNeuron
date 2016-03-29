'''
from pyneuron.neuron_build.neuron_build import NeuronBuilder
net=NeuronBuilder([2],[3,4],[2],has_bias=True)
net.connectTwoLayers('in', 'hid0')
net.connectTwoLayers('hid0', 'hid1')
net.connectTwoLayers('hid1', 'out')
print net.neuron_to_neuron_weight
print net.bias_to_neuron
net.setLayerFunction('hid0', 'logsig')
net.setLayerFunction('hid1', 'logsig')
net.setLayerFunction('out', 'purelin')
net.setNeuronFunction('hid0_2', 'hardlim')
print net.neuron_function
net.setInputToInputLayer([1,0.6])
print net.getOutputFromLayer('hid1')
print net.getOutputFromLayer('out')
print net.getOutputFromOneNeuron('out0')
net.showNetworkSimulation()
'''

from neuron_build.neuron_build import NeuronBuilder
net=NeuronBuilder([2],[3],[2],has_bias=True)
net.connectTwoLayers('in', 'hid0')
net.connectTwoLayers('hid0','out')
from data.DataSet import DataSet
data=DataSet(2,2)
data.addItem([1,1], [-1,-1])
data.addItem([1,-1],[-1,1])
data.addItem([-1,1],[1,-1])
data.addItem([-1,-1],[1,1])
net.setDataSet(data)
net.setLayerFunction('hid0', 'logsig')
net.setLayerFunction('out','purelin')
net.setInputToInputLayer([1,1])
print net.getOutputFromLayer('out')
print net.neuron_function
from trainer.DeltaTrainer import DeltaTrainer
trainer=DeltaTrainer(net)
trainer.setMaxError(0.001)
trainer.DeltaTrain()
#trainer.plotFigure()
net.setInputToInputLayer([1,1])
print net.getOutputFromLayer('out')
print net.activate([1,-1])
print net.activate([1,1,1])
print net.getOutputFromLayer('out')
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
#b.showNetworkSimulation()
b.setLearningRate(0.5)
b.setMaxError(0.00000001)
b.train()
b.plotFigure()
print b.net.neuron_to_neuron_weight
print b.activate([0.5,0.6])
'''


