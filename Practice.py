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

