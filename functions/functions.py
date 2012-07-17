# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="shd101wyy"
__date__ ="$2012-5-31 16:22:26$"
from math import *
def hardlim(input_value):
    if input_value<0:
        #return output=0
        return 0
    else:
        #return output=1
        return 1
    
def hardlims(input_value):
    if input_value<0:
        #return output=-1
        return -1
    else:
        #return output=1
        return 1

def purelin(input_value):
    #return output=input_value
    return input_value

def satlin(input_value):
    if input_value<0:
        #return output=0
        return 0
    elif input_value>=0 and input_value<=1:
        #return output=input_value
        return input_value
    else:
        #return output=1
        return 1

def satlins(input_value):
    if input_value<-1:
    # return output=-1
       return -1 
    elif input_value>=-1 and input_value<=1:
       # return output=input_value
       return input_value
    else:
       # return output=1
       return 1

def logsig(input_value):
    return 1/(1+exp(-input_value))

def tansig(input_value):
    return (exp(input_value)-exp(-input_value))/(exp(input_value)+exp(-input_value))

def poslin(input_value):
    if input_value<0:
        return 0
    else:
        return input_value
    
#def compet
def compet(neuron_key,net):
    #from pyneuron.neuron_build.neuron_build import NeuronBuilder
    #a=NeuronBuilder(net)
  
    if neuron_key.find('in')!=-1:
        layer_key='in'
    elif neuron_key.find('out')!=-1:
        layer_key='out'
    elif neuron_key.find('hid')!=-1:
        layer_key=neuron_key[:neuron_key.find('_')]
    else:
        print('the neuron key you entered is wrong')
        
    max=net.getTheInputToOneNeuron(neuron_key)
    

    for neuron in net.neuron_in_layer[layer_key]:
        if net.neuron_function[neuron]=='compet':
            input_to_neuron=net.getTheInputToOneNeuron(neuron)
            #output=purelin(input_to_neuron)
            output=input_to_neuron
            if output>max:
                return 0
                break
    return 1

def diff_purelin(x):
    return 1

def diff_logsig(x):
    return (1-logsig(x))*(logsig(x))

def diff_function(function_name,input_value):
    if function_name=='hardlim':
        #print("hardlim has no derivative ")
        #return 0
        if input_value<0:
        #return output=0
            return 0
        else:
        #return output=1
            return 1
    elif function_name=='purelin':
        return diff_purelin(input_value)
    elif function_name=='logsig':
        return diff_logsig(input_value)
    else:
        print("I have not make "+function_name)
        return None

