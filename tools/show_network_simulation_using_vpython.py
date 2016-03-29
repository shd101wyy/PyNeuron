'''
Created on 2012-6-8

@author: shd101wyy
'''
from neuron_build.neuron_build import NeuronBuilder
import threading
class ShowNetworkSimulation(threading.Thread):
    def __init__(self,net):
        #self.net=NeuronBuilder(net)
        threading.Thread.__init__(self)
        self.net=net
         
    def designPosition(self):
        y_distance=4
        x_distance=4
        
        input_layer=self.net.input_layer
        hidden_layers=self.net.hidden_layers
        output_layer=self.net.output_layer
        self.input_neuron_position={}
        self.hidden_neuron_position={}
        self.output_neuron_position={}
        self.neuron_position={}
        

        middle=(input_layer[0]-1)/2.0
        for neuron in self.net.neuron_in_layer['in']:
            index=int(neuron[neuron.find('in')+2:])
            self.input_neuron_position[neuron]=(-5,(middle-index)*y_distance,0)
            self.neuron_position[neuron]=(-5,(middle-index)*y_distance,0)
            
        for i in range(len(hidden_layers)):
            middle=(hidden_layers[i]-1)/2.0
            for neuron in self.net.neuron_in_layer['hid'+str(i)]:
                index=int(neuron[neuron.find('_')+1:])
                self.hidden_neuron_position[neuron]=(-5+(i+1)*x_distance,(middle-index)*y_distance,0)
                self.neuron_position[neuron]=(-5+(i+1)*x_distance,(middle-index)*y_distance,0)
                
        middle=(output_layer[0]-1)/2.0              
        for neuron in self.net.neuron_in_layer['out']:
            index=int(neuron[neuron.find('out')+3:])
            self.output_neuron_position[neuron]=(-5+(1+len(hidden_layers))*x_distance,(middle-index)*y_distance,0)    
            self.neuron_position[neuron]=(-5+(1+len(hidden_layers))*x_distance,(middle-index)*y_distance,0)    
      
      
      
    def showNeurons(self):
        import visual
        def showArrow():
            for key in self.net.neuron_to_neuron_weight:
                from_neuron=key[:key.find('_to_')]
                to_neuron=key[key.find('to_')+3:]
                if self.net.neuron_to_neuron_weight[key]!=None:
                    delta_x=self.neuron_position[to_neuron][0]-self.neuron_position[from_neuron][0]
                    delta_y=self.neuron_position[to_neuron][1]-self.neuron_position[from_neuron][1]                   
                    delta_z=self.neuron_position[to_neuron][2]-self.neuron_position[from_neuron][2]                    
                    pointer=visual.arrow(pos=self.neuron_position[from_neuron], axis=(delta_x,delta_y,delta_z), shaftwidth=0.1)
            
            for key in self.net.neuron_in_layer['in']:
                x=self.neuron_position[key][0]-3
                y=self.neuron_position[key][1]
                z=self.neuron_position[key][2]
                pointer=visual.arrow(pos=(x,y,z), axis=(3,0,0), shaftwidth=0.1)
                
            for key in self.net.neuron_in_layer['out']:
                pointer=visual.arrow(pos=self.neuron_position[key], axis=(3,0,0), shaftwidth=0.1)
        #import visual
        input_layer=self.net.input_layer
        hidden_layers=self.net.hidden_layers
        output_layer=self.net.output_layer
        
        conditioned_neuron=self.net.conditionedNeuron
        
        for neuron in self.net.neuron_in_layer['in']:
            has_conditioned_neuron=False
            for conditioned_neuron in self.net.conditionedNeuron:
                if conditioned_neuron==neuron:
                    has_conditioned_neuron=True
                    break
            if has_conditioned_neuron:
                neuron=visual.sphere(pos=self.input_neuron_position[neuron],radius=0.6,color=visual.color.orange)
            else:
                neuron=visual.sphere(pos=self.input_neuron_position[neuron],radius=0.6,color=visual.color.yellow)
        
        for neuron in self.net.neuron_in_layer['out']:
            neuron=visual.sphere(pos=self.output_neuron_position[neuron],radius=0.6,color=visual.color.red)
          
        if self.net.has_hidden_layer:
            for i in range(len(self.net.hidden_layers)):
                for neuron in self.net.neuron_in_layer['hid'+str(i)]:
                    neuron=visual.sphere(pos=self.hidden_neuron_position[neuron],radius=0.6,color=visual.color.blue)
        showArrow()
        
    def run(self):
        self.designPosition()
        self.showNeurons()