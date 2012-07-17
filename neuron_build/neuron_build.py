'''
Back up

    def updateBiasToLayerByBiasToNeuron(self):
        for key in self.bias_to_neuron:
            if key.find('hid')!=-1:
                layer_key='hid'
                i=key[key.find('hid')+3:]
            elif key.find('in')!=-1:
                layer_key='in'
                i=key[key.find('in')+2:]
            elif key.find('out')!=-1:
                layer_key='out'
                i=key[key.find('out')+3:]
            else:
                print('mistake occurred when updating biasToLayer by biasToNeuron, key is'+key)
            
            self.bias_to_layer[layer_key][int(i)]=self.bias_to_neuron[key]

 def createWeightAndBiasAndFunctionName(input_layer,hidden_layer,output_layer):
            weight={}
            neuron_to_neuron_weight={}
            bias={}
            neuron_function={}
            if len(hidden_layer)==1 and hidden_layer[0]==0:
                weight['in_to_out']=[[0 for column in range(input_layer[0])]for row in range(output_layer[0])]
                bias['in_to_out']=[[0]for row in range(output_layer[0])]
                for i in range(len(weight['in_to_out'])):
                    neuron_function['out'+str(i)]='purelin'
                    for j in range(len(weight['in_to_out'][0])):
                        neuron_to_neuron_weight['in'+str(j)+'_to_out'+str(i)]=0
  
            else:
                
                #connect layer in to hid1
                weight['in_to_hid0']=[[0 for column in range(input_layer[0])]for row in range(hidden_layer[0])]
                bias['in_to_hid0']=[[0]for row in range(hidden_layer[0])]
                #connect layer hid last to out
                weight['hid'+str(len(hidden_layer)-1)+'_to_out']=[[0 for column in range(hidden_layer[len(hidden_layer)-1])]for row in range(output_layer[0])]
                bias['hid'+str(len(hidden_layer)-1)+'_to_out']=[[0]for row in range(output_layer[0])]
                #connect layer between hid
                for i in range(len(hidden_layer)-1):
                    weight['hid'+str(i)+'_to_hid'+str(i+1)]=[[0 for column in range(hidden_layer[i])]for row in range(hidden_layer[i+1])]
                    bias['hid'+str(i)+'_to_hid'+str(i+1)]=[[0]for row in range(hidden_layer[i+1])]
                #connect neuron in in to hid1
                for i in range(len(weight['in_to_hid0'])):
                    neuron_function['hid0_'+str(i)]='purelin'
                    for j in range(len(weight['in_to_hid0'][0])):
                        neuron_to_neuron_weight['in'+str(j)+'_to_hid0_'+str(i)]=weight['in_to_hid0'][i][j]
                #connect neuron in  hid last to out
                for i in range(len(weight['hid'+str(len(hidden_layer)-1)+'_to_out'])):
                    neuron_function['out'+str(i)]='purelin'
                    for j in range(len(weight['hid'+str(len(hidden_layer)-1)+'_to_out'][0])):
                        neuron_to_neuron_weight['hid'+str(len(hidden_layer)-1)+str(j)+'_to_out'+str(i)]=weight['hid'+str(len(hidden_layer)-1)+'_to_out'][i][j]
                #connect neuron in  hid to hid
                for a in range(len(hidden_layer)-1):
                    for i in range(len(weight['hid'+str(a)+'_to_hid'+str(a+1)])):
                        neuron_function['hid'+str(a+1)+'_'+str(i)]='purelin'
                        for j in range(len(weight['hid'+str(a)+'_to_hid'+str(a+1)][0])):
                            neuron_to_neuron_weight['hid'+str(a)+"_"+str(j)+"_to_hid"+str(a+1)+"_"+str(i)]=weight['hid'+str(a)+'_to_hid'+str(a+1)][i][j]
                #  weight['hid'+str(a)+'_to_hid'+str(a+1)]
                
                
            return [weight,neuron_to_neuron_weight,bias,neuron_function]

'''






'''
It can only be used for feedforward now
Created on 2012-6-2

@author: shd101wyy
'''
'''
for example:
    look at rows to determine the amount of layers
    input:[[0,0,0,0]] has one layers
    hidden:[[0,0],[0,0]] has two layers
This Neural Builder is mainly for Supervised Neural Network
n=NeuronBuilder([2],[2,3],[4])
create a network with 2 neurons for one input layer,
                     2,3 neurons for each 2 hidden layer
                    and 4 neuron for one output layer 
                    
                    
                    
# three noun:
    1) layer key:
        for example:
            input layer:in
            hidden layer:hid0 hid1 hid2 hid3 .......
            output layer:out
    2)neuron key:
        for example:
            the third neuron in input layer:
                in2
            the second neuron in the third hidden layer:
                hi2_1
            the fourth neuron in output layer:
                out3
    3)neuron name:
        the name of one neuron in one specific position:
            for example:
                the name of the second neuron in the first hidden layer:
                    neuron_dic[neuron_key]=neuron_name
                    neuron_dict['hid0_1']="Hi this is the name of the neuron you appoint"
                    
# connect between two specific neurons:
    connect fist neuron in input layer and second neuron in the third hidden layer
    in0_to_hi2_1
    and then give weight['in_to_hi2'][1][0]=a random value
'''




class NeuronBuilder(object):

    def __init__(self,input_layer,hidden_layers,output_layer,has_bias=True):
        self.input_num=input_layer[0]
        self.input_layer=input_layer
        self.output_num=output_layer[0]
        self.output_layer=output_layer
        self.hidden_layers=hidden_layers
        self.hidden_list=[]
        self.has_bias=has_bias
        self.winner_neuron=None
        self.input_list_to_input_layer=None
        '''
        if type(hidden_layers)==type([]):
            self.hidden_layers_num=len(hidden_layers)
            for neuron_num_of_each_layer in self.hidden_layers:
                self.hidden_list.append([0 for num in range(neuron_num_of_each_layer)])
        else:
            if hidden_layers[0]==0:
                self.hidden_layers_num=0
                self.hidden_list=[[]]
            else:
                self.hidden_layers_num=1
                self.hidden_list.append([0 for num in range(hidden_layers)])
        '''
        self.hidden_dict=None
        if len(hidden_layers) and hidden_layers[0]==0:
            self.has_hidden_layer=False
        else:
            self.has_hidden_layer=True
            for elem in hidden_layers:
                self.hidden_list.append([0 for num in range(elem)])
                self.hidden_dict={}
            for i in range(len(self.hidden_list)):
                for j in range(len(self.hidden_list[i])):
                    self.hidden_dict['hid'+str(i)+"_"+str(j)]=str(i)+"_hidden_layer_neuron_"+str(j)   

        #self.input_list=[[0 for num in range(self.input_num)]]
        #self.output_list=[[0 for num in range(self.output_num)]]            
        self.input_layer_list=[[0 for num in range(self.input_num)]]
        self.output_layer_list=[[0 for num in range(self.output_num)]]
        
        self.input_dict={}
        self.output_dict={}
        #self.hidden_dict={}
        for i in range(self.input_num):
            self.input_dict['in'+str(i)]="input_neuron_"+str(i)
        for i in range(self.output_num):
            self.output_dict['out'+str(i)]="output_neuron_"+str(i)
        #for i in range(len(self.hidden_list)):
        #    for j in range(len(self.hidden_list[i])):
        #        self.hidden_dict['hid'+str(i)+"_"+str(j)]=str(i)+"_hidden_layer_neuron_"+str(j)
        self.neuron_dict={}
        for keys in self.input_dict.keys():
            self.neuron_dict[keys]=self.input_dict[keys]
        for keys in self.output_dict.keys():
            self.neuron_dict[keys]=self.output_dict[keys]
        if self.has_hidden_layer:
            for keys in self.hidden_dict.keys():
                self.neuron_dict[keys]=self.hidden_dict[keys]
        #print self.input_list
        #print self.output_list
        #print self.hidden_list
        #print self.input_dict
        #print self.output_dict
       # if self.has_hidden_layer:
         #   print self.hidden_dict
        #print self.neuron_dict
        
        #define name_dict :the reverse of the neuron_dict
        self.name_dict={}
        for key in self.neuron_dict.keys():
            self.name_dict[self.neuron_dict[key]]=key
        

        self.layer_to_layer_weight=None
        self.neuron_to_neuron_weight=None
        self.bias_to_layer=None
        self.neuron_function=None
        
        # create neuron_in_layer to get neuron key in one layer 
        self.neuron_in_layer={}
        self.neuron_in_layer['in']=[]
        self.neuron_in_layer['out']=[]
        for i in range(len(self.hidden_layers)):
            self.neuron_in_layer['hid'+str(i)]=[]
        for i in range(self.input_num):
            self.neuron_in_layer['in'].append('in'+str(i))
        for i in range(self.output_num):
            self.neuron_in_layer['out'].append('out'+str(i))
        if self.has_hidden_layer:
            for i in range(len(self.hidden_layers)):
                self.neuron_in_layer['hid'+str(i)]=[]
            for i in range(len(self.hidden_layers)):
                for j in range(self.hidden_layers[i]):
                    self.neuron_in_layer['hid'+str(i)].append('hid'+str(i)+'_'+str(j))
        #set up weight bias and one neuron's function name
        def createWeightAndBiasAndFunctionName(input_layer,hidden_layer,output_layer):
            from random import uniform
            weight={}
            neuron_to_neuron_weight={}
            bias={}
            neuron_function={}
            if len(hidden_layer)==1 and hidden_layer[0]==0:
                weight['in_to_out']=[[None for column in range(input_layer[0])]for row in range(output_layer[0])]
                #bias['in_to_out']=[[None]for row in range(output_layer[0])]
                bias['out']=[[uniform(-1,1)]for row in range(output_layer[0])]
                for i in range(len(weight['in_to_out'])):
                    neuron_function['out'+str(i)]='purelin'
                    for j in range(len(weight['in_to_out'][0])):
                        neuron_to_neuron_weight['in'+str(j)+'_to_out'+str(i)]=None
  
            else:
                
                #connect layer in to hid1
                weight['in_to_hid0']=[[None for column in range(input_layer[0])]for row in range(hidden_layer[0])]
                #bias['in_to_hid0']=[[None]for row in range(hidden_layer[0])]
                bias['hid0']=[[uniform(-1,1)]for row in range(hidden_layer[0])]
                #connect layer hid last to out
                weight['hid'+str(len(hidden_layer)-1)+'_to_out']=[[None for column in range(hidden_layer[len(hidden_layer)-1])]for row in range(output_layer[0])]
                #bias['hid'+str(len(hidden_layer)-1)+'_to_out']=[[None]for row in range(output_layer[0])]
                bias['out']=[[uniform(-1,1)]for row in range(output_layer[0])]
                #connect layer between hid
                for i in range(len(hidden_layer)-1):
                    weight['hid'+str(i)+'_to_hid'+str(i+1)]=[[None for column in range(hidden_layer[i])]for row in range(hidden_layer[i+1])]
                    #bias['hid'+str(i)+'_to_hid'+str(i+1)]=[[None]for row in range(hidden_layer[i+1])]
                    bias['hid'+str(i+1)]=[[uniform(-1,1)]for row in range(hidden_layer[i+1])]
                #connect neuron in in to hid1
                for i in range(len(weight['in_to_hid0'])):
                    neuron_function['hid0_'+str(i)]='purelin'
                    for j in range(len(weight['in_to_hid0'][0])):
                        neuron_to_neuron_weight['in'+str(j)+'_to_hid0_'+str(i)]=weight['in_to_hid0'][i][j]
                #connect neuron in  hid last to out
                for i in range(len(weight['hid'+str(len(hidden_layer)-1)+'_to_out'])):
                    neuron_function['out'+str(i)]='purelin'
                    for j in range(len(weight['hid'+str(len(hidden_layer)-1)+'_to_out'][0])):
                        # neuron_to_neuron_weight['hid'+str(len(hidden_layer)-1)+str(j)+'_to_out'+str(i)]=weight['hid'+str(len(hidden_layer)-1)+'_to_out'][i][j]
                        neuron_to_neuron_weight['hid'+str(len(hidden_layer)-1)+'_'+str(j)+'_to_out'+str(i)]=weight['hid'+str(len(hidden_layer)-1)+'_to_out'][i][j]
                #connect neuron in  hid to hid
                for a in range(len(hidden_layer)-1):
                    for i in range(len(weight['hid'+str(a)+'_to_hid'+str(a+1)])):
                        neuron_function['hid'+str(a+1)+'_'+str(i)]='purelin'
                        for j in range(len(weight['hid'+str(a)+'_to_hid'+str(a+1)][0])):
                            neuron_to_neuron_weight['hid'+str(a)+"_"+str(j)+"_to_hid"+str(a+1)+"_"+str(i)]=weight['hid'+str(a)+'_to_hid'+str(a+1)][i][j]
                #  weight['hid'+str(a)+'_to_hid'+str(a+1)]
                              
            return [weight,neuron_to_neuron_weight,bias,neuron_function]
        [self.layer_to_layer_weight,self.neuron_to_neuron_weight,self.bias_to_layer,self.neuron_function]=createWeightAndBiasAndFunctionName(self.input_layer,self.hidden_layers,self.output_layer)
        self.bias_to_neuron={}
        if not self.has_bias:
            self.bias_to_layer=None
            self.bias_to_neuron=None
        else:
            for keys in self.bias_to_layer:
                target_neuron=keys
                #print 'target layer'+str(target_neuron)
                for i in range(len(self.bias_to_layer[keys])):
                    if target_neuron.find('in')!=-1 or target_neuron.find('out')!=-1:
                        self.bias_to_neuron[target_neuron+str(i)]=self.bias_to_layer[keys][i][0]
                    if target_neuron.find('hid')!=-1:
                        self.bias_to_neuron[target_neuron+"_"+str(i)]=self.bias_to_layer[keys][i][0]
        
        self.conditionedNeuron=[]
        self.unconditionedNeuron=[]
                
    def connectTwoNeurons(self,first_neuron_key,second_neuron_key):
        '''    
        Connect two neurons:
        for example:
            connectTwoNeurons('in0','hid0_2') will connect the first neuron in input layer
            to the third neuron in the first hidden layer

        '''      

        from random import uniform
        self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]=uniform(-1,1)
        if first_neuron_key.find('in')!=-1:
            first_layer='in'
            j=first_neuron_key[first_neuron_key.find('in')+2:]
        elif first_neuron_key.find('out')!=-1:
            first_layer='out'
            j=first_neuron_key[first_neuron_key.find('out')+3:]
        else:
            first_layer=first_neuron_key[:first_neuron_key.find('_')]
            j=first_neuron_key[first_neuron_key.find('_')+1:]

        if second_neuron_key.find('in')!=-1:
            second_layer='in'
            i=second_neuron_key[second_neuron_key.find('in')+2:]
        elif second_neuron_key.find('out')!=-1:
            second_layer='out'
            i=second_neuron_key[second_neuron_key.find('out')+3:]
        else:
            second_layer=second_neuron_key[:second_neuron_key.find('_')]
            i=second_neuron_key[second_neuron_key.find('_')+1:]
        try:
            self.layer_to_layer_weight[first_layer+'_to_'+second_layer][int(i)][int(j)]=self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]    
        except:
            print('except occurred when connect two neurons')
            self.layer_to_layer_weight[first_layer+'_to_'+second_layer]=[[None for column in range(len(self.neuron_in_layer[first_layer]))]for row in range(len(self.neuron_in_layer[second_layer]))]
            self.layer_to_layer_weight[first_layer+'_to_'+second_layer][int(i)][int(j)]=self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]    
    def connectTwoLayers(self,first_layer_key,second_layer_key):
        from random import uniform
        if self.layer_to_layer_weight.has_key(first_layer_key+'_to_'+second_layer_key):
            pass
        else:
            print "do not has key"
            self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key]=[[uniform(-1,1) for column in range(len(self.neuron_in_layer[first_layer_key]))]for row in range(len(self.neuron_in_layer[second_layer_key]))]
            
        for i in range(len(self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key])):
            for j in range(len(self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][0])):
                self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]=uniform(-1,1)
                if first_layer_key.find('hid')!=-1 and second_layer_key.find('hid')!=-1:
                #    print "go 0"
                #    print first_layer_key+'_'+str(j)+'_to_'+second_layer_key+"_"+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+'_'+str(j)+'_to_'+second_layer_key+"_"+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                elif first_layer_key.find('hid')!=-1 and second_layer_key.find('hid')==-1:
                #    print "go 1"
                #    print first_layer_key+'_'+str(j)+'_to_'+second_layer_key+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+'_'+str(j)+'_to_'+second_layer_key+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                elif first_layer_key.find('hid')==-1 and second_layer_key.find('hid')==-1:
                #   print "go 2"
                #    print first_layer_key+str(j)+'_to_'+second_layer_key+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+str(j)+'_to_'+second_layer_key+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                else:
                #    print "go 3"
                #    print first_layer_key+str(j)+'_to_'+second_layer_key+"_"+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+str(j)+'_to_'+second_layer_key+"_"+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
    def setNeuronToNeuronWeight(self,first_neuron_key,second_neuron_key,weight):
        self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]=weight 
        if first_neuron_key.find('in')!=-1:
            first_layer='in'
            j=first_neuron_key[first_neuron_key.find('in')+2:]
        elif first_neuron_key.find('out')!=-1:
            first_layer='out'
            j=first_neuron_key[first_neuron_key.find('out')+3:]
        else:
            first_layer=first_neuron_key[:first_neuron_key.find('_')]
            j=first_neuron_key[first_neuron_key.find('_')+1:]

        if second_neuron_key.find('in')!=-1:
            second_layer='in'
            i=second_neuron_key[second_neuron_key.find('in')+2:]
        elif second_neuron_key.find('out')!=-1:
            second_layer='out'
            i=second_neuron_key[second_neuron_key.find('out')+3:]
        else:
            second_layer=second_neuron_key[:second_neuron_key.find('_')]
            i=second_neuron_key[second_neuron_key.find('_')+1:]
        try:
            self.layer_to_layer_weight[first_layer+'_to_'+second_layer][int(i)][int(j)]=self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]    
        except:
            self.layer_to_layer_weight[first_layer+'_to_'+second_layer]=[[None for column in range(len(self.neuron_in_layer[first_layer]))]for row in range(len(self.neuron_in_layer[second_layer]))]
            self.layer_to_layer_weight[first_layer+'_to_'+second_layer][int(i)][int(j)]=self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]       
    
    def setLayerToLayerWeight(self,first_layer_key,second_layer_key,weight):
        self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key]=weight
        for i in range(len(self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key])):
            for j in range(len(self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][0])):
                if first_layer_key.find('hid')!=-1 and second_layer_key.find('hid')!=-1:
                #    print "go 0"
                #    print first_layer_key+'_'+str(j)+'_to_'+second_layer_key+"_"+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+'_'+str(j)+'_to_'+second_layer_key+"_"+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                elif first_layer_key.find('hid')!=-1 and second_layer_key.find('hid')==-1:
                #    print "go 1"
                #    print first_layer_key+'_'+str(j)+'_to_'+second_layer_key+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+'_'+str(j)+'_to_'+second_layer_key+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                elif first_layer_key.find('hid')==-1 and second_layer_key.find('hid')==-1:
                #   print "go 2"
                #    print first_layer_key+str(j)+'_to_'+second_layer_key+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+str(j)+'_to_'+second_layer_key+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                else:
                #    print "go 3"
                #    print first_layer_key+str(j)+'_to_'+second_layer_key+"_"+str(i)
                    self.neuron_to_neuron_weight[first_layer_key+str(j)+'_to_'+second_layer_key+"_"+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
          
    def setLayerFunction(self,layer_key,function_name):  
        '''
        set all neurons in the specific layer to a specific function name
        '''
        for keys in self.neuron_function:
            if keys.find(layer_key)!=-1:
                self.neuron_function[keys]=function_name
    def setNeuronFunction(self,neuron_key,function_name):
        self.neuron_function[neuron_key]=function_name
        
    def disconnectTwoNeurons(self,first_neuron_key,second_neuron_key):
        #from random import uniform
        self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]=None
        if first_neuron_key.find('in')!=-1:
            first_layer='in'
            j=first_neuron_key[first_neuron_key.find('in')+2:]
        elif first_neuron_key.find('out')!=-1:
            first_layer='out'
            j=first_neuron_key[first_neuron_key.find('out')+3:]
        else:
            first_layer=first_neuron_key[:first_neuron_key.find('_')]
            j=first_neuron_key[first_neuron_key.find('_')+1:]

        if second_neuron_key.find('in')!=-1:
            second_layer='in'
            i=second_neuron_key[second_neuron_key.find('in')+2:]
        elif second_neuron_key.find('out')!=-1:
            second_layer='out'
            i=second_neuron_key[second_neuron_key.find('out')+3:]
        else:
            second_layer=second_neuron_key[:second_neuron_key.find('_')]
            i=second_neuron_key[second_neuron_key.find('_')+1:]    
        self.layer_to_layer_weight[first_layer+'_to_'+second_layer][int(i)][int(j)]=self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]    
        
        
    def disconnectTwoLayers(self,first_layer_key,second_layer_key):
        #from random import uniform
        for i in range(len(self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key])):
            for j in range(len(self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][0])):
                self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]=None
                if first_layer_key.find('hid')!=-1 and second_layer_key.find('hid')!=-1:
                    self.neuron_to_neuron_weight[first_layer_key+'_'+str(j)+'_to_'+second_layer_key+"_"+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                elif first_layer_key.find('hid')!=-1 and second_layer_key.find('hid')==-1:
                    self.neuron_to_neuron_weight[first_layer_key+'_'+str(j)+'_to_'+second_layer_key+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                elif first_layer_key.find('hid')==-1 and second_layer_key.find('hid')==-1:
                    self.neuron_to_neuron_weight[first_layer_key+str(j)+'_to_'+second_layer_key+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
                else:
                    self.neuron_to_neuron_weight[first_layer_key+str(j)+'_to_'+second_layer_key+"_"+str(i)]=self.layer_to_layer_weight[first_layer_key+'_to_'+second_layer_key][i][j]
    
    
    
    def getInputToNeuronFromTwoConnectedNeurons(self,first_neuron_key,second_neuron_key,input_from_first_neuron):
        '''
        from first_neuron to second_neuron
        '''
        #from pyneuron.functions.from_function_fire_output import fireForOneValue
        if self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]!=None:
            #print first_neuron_key+"_to_"+second_neuron_key
            #print self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]
            #print input_from_first_neuron
            return self.neuron_to_neuron_weight[first_neuron_key+"_to_"+second_neuron_key]*input_from_first_neuron
        else:
            return None
    def getOutputFromOneNeuron(self,output_from_neuron_key):
        from pyneuron.functions.from_function_fire_output import fireForOneValue
        from pyneuron.functions.functions import compet
        if output_from_neuron_key.find('in')!=-1:
            return self.get_output_from_input_layer[output_from_neuron_key]
        else:
            input_to_neuron=None
            for keys in self.neuron_to_neuron_weight:
                target_neuron=keys[keys.find('to_')+3:]
                from_neuron=keys[:keys.find('_to')]
                if target_neuron==output_from_neuron_key and self.neuron_to_neuron_weight[keys]!=None:
                    #recursion
                    if input_to_neuron==None:
                        input_to_neuron=0
                    input_to_neuron+=self.getInputToNeuronFromTwoConnectedNeurons(from_neuron, target_neuron,self.getOutputFromOneNeuron(from_neuron))
            if self.has_bias:
                if input_to_neuron!=None:
                    input_to_neuron+=self.bias_to_neuron[output_from_neuron_key]
                else:
                    pass
            #print output_from_neuron_key
            #print input_to_neuron
            if self.neuron_function[output_from_neuron_key]=='compet':
                output=compet(output_from_neuron_key,self)
            #      if auto_train_competitive_neuron:
            #          from pyneuron.trainer.Kohonen import KohonenTrainer
            #        t=KohonenTrainer(self)
            #        if output_from_neuron_key.find('out')!=-1:
            #            competitive_layer_key='out'
            #        elif output_from_neuron_key.find('hid')!=-1:
            #            competitive_layer_key=output_from_neuron_key[:output_from_neuron_key.find('_')]
            #        else:
            #            print("competitive layer key error")
            #        t.KohonenTrainForWinnerNeuron(self.input_list_to_input_layer, competitive_layer_key)
            else:
                output=fireForOneValue(self.neuron_function[output_from_neuron_key],input_to_neuron)
            return output
        
    def getTheInputToOneNeuron(self,neuron_key):
        from pyneuron.functions.from_function_fire_output import fireForOneValue
        if neuron_key.find('in')!=-1:
            return self.get_output_from_input_layer[neuron_key]
        else:
            input_to_neuron=None
            for keys in self.neuron_to_neuron_weight:
                target_neuron=keys[keys.find('to_')+3:]
                from_neuron=keys[:keys.find('_to')]
                if target_neuron==neuron_key and self.neuron_to_neuron_weight[keys]!=None:
                    #recursion
                    if input_to_neuron==None:
                        input_to_neuron=0
                    input_to_neuron+=self.getInputToNeuronFromTwoConnectedNeurons(from_neuron, target_neuron,self.getOutputFromOneNeuron(from_neuron))
            if self.has_bias:
                if input_to_neuron!=None:
                    input_to_neuron+=self.bias_to_neuron[neuron_key]
                else:
                    pass
            #print output_from_neuron_key
            #print input_to_neuron
            output=fireForOneValue('purelin',input_to_neuron)
            return output
        
    def getOutputFromLayer(self,layer_key):
        output=[]
        for neuron in self.neuron_in_layer[layer_key]:
#            output.append(self.getOutputFromOneNeuron(neuron))
            output.append([self.getOutputFromOneNeuron(neuron)])
        return output
    def getTheInputToOneLayer(self,layer_key):
        output=[]
        for neuron in self.neuron_in_layer[layer_key]:
#            output.append(self.getTheInputToOneNeuron(neuron))
            output.append([self.getTheInputToOneNeuron(neuron)])
        return output       
    
    def setInputToInputLayer(self,input_list):
        self.get_output_from_input_layer={}
        self.input_list_to_input_layer=input_list
        if len(input_list)!=self.input_num:
            print("Input num is wrong")
        else:
            for i in range(self.input_num):
                self.get_output_from_input_layer['in'+str(i)]=input_list[i]
        
    def setDataSet(self,data_set):
        self.input_data=None
        self.output_data=None
        self.data_set=data_set
        [self.input_data,self.output_data]=data_set.returnDataSet()
    def setBiasToLayer(self,target_layer_key,bias_value):
        self.bias_to_layer[target_layer_key]=bias_value
        for i in range(len(bias_value)):
            if target_layer_key.find('hid')!=-1:
                self.bias_to_neuron[target_layer_key+"_"+str(i)]=bias_value[i][0]
            else:
                self.bias_to_neuron[target_layer_key+str(i)]=bias_value[i][0]
    def setBiasToNeuron(self,neuron_key,bias_value):
        self.bias_to_neuron[neuron_key]=bias_value
        if neuron_key.find('hid')!=-1:
            index=int(neuron_key[neuron_key.find('_')+1:])
            self.bias_to_layer[neuron_key[:neuron_key.find('_')]][index][0]=bias_value
        elif neuron_key.find('in')!=-1:
            index=int(neuron_key[neuron_key.find('in')+2:])
            self.bias_to_layer['in'][index][0]=bias_value
        elif neuron_key.find('out')!=-1:
            index=int(neuron_key[neuron_key.find('out')+3:])
            self.bias_to_layer['out'][index][0]=bias_value
        else:
            print("neuron key error")
        
    def getFunctionNameOfOneNeuron(self,neuron_key):
        return self.neuron_function[neuron_key]


    def updateNeuronToNeuronWeightByLayerToLayerWeight(self):
        if not self.has_hidden_layer:
            for i in range(len(self.layer_to_layer_weight['in_to_out'])):
                for j in range(len(self.layer_to_layer_weight['in_to_out'][0])):
                    self.neuron_to_neuron_weight['in'+str(j)+'_to_out'+str(i)]=self.layer_to_layer_weight['in_to_out'][i][j]
        else:
            for i in range(len(self.layer_to_layer_weight['in_to_hid0'])):
                for j in range(len(self.layer_to_layer_weight['in_to_hid0'][0])):
                    self.neuron_to_neuron_weight['in'+str(j)+'_to_hid0_'+str(i)]=self.layer_to_layer_weight['in_to_hid0'][i][j]
            for i in range(len(self.layer_to_layer_weight['hid'+str(len(self.hidden_layers)-1)+'_to_out'])):
                for j in range(len(self.layer_to_layer_weight['hid'+str(len(self.hidden_layers)-1)+'_to_out'][0])):
                    self.neuron_to_neuron_weight['hid'+str(len(self.hidden_layers)-1)+'_'+str(j)+'_to_out'+str(i)]=self.layer_to_layer_weight['hid'+str(len(self.hidden_layers)-1)+'_to_out'][i][j]
            for a in range(len(self.hidden_layers)-1):
                for i in range(len(self.layer_to_layer_weight['hid'+str(a)+'_to_hid'+str(a+1)])):
                    for j in range(len(self.layer_to_layer_weight['hid'+str(a)+'_to_hid'+str(a+1)][0])):
                        self.neuron_to_neuron_weight['hid'+str(a)+'_'+str(j)+'_to_hid'+str(a+1)+'_'+str(i)]=self.layer_to_layer_weight['hid'+str(a)+'_to_hid'+str(a+1)][i][j]
                        
    def updateBiasToNeuronByBiasToLayer(self):
        for keys in self.bias_to_layer:
            target_neuron=keys
            #print 'target layer'+str(target_neuron)
            for i in range(len(self.bias_to_layer[keys])):
                if target_neuron.find('in')!=-1 or target_neuron.find('out')!=-1:
                    self.bias_to_neuron[target_neuron+str(i)]=self.bias_to_layer[keys][i][0]
                if target_neuron.find('hid')!=-1:
                    #print target_neuron+"_"+str(i)
                    #print self.bias_to_layer[keys]
                    self.bias_to_neuron[target_neuron+"_"+str(i)]=float(self.bias_to_layer[keys][i][0])
    
    def setNeuronNameToNeuronKey(self,neuron_name,neuron_key):
        self.neuron_dict[neuron_key]=neuron_name
        self.name_dict[neuron_name]=neuron_key
        
    def updateLayerToLayerWeightByNeuronToNeuronWeight(self):
        for key in self.neuron_to_neuron_weight:
            from_neuron=key[:key.find('_to')]
            to_neuron=key[key.find('to_')+3:]
            if from_neuron.find('hid')!=-1:
                from_layer=from_neuron[:from_neuron.find('_')]
                i=from_neuron[from_neuron.find('_')+1:]
            elif from_neuron.find('in')!=-1:
                from_layer='in'
                i=from_neuron[from_neuron.find('in')+2:]
            elif from_neuron.find('out')!=-1:
                from_layer='out'
                i=from_neuron[from_neuron.find('out')+3:]
            else:
                print('from_neuron mistake')

            if to_neuron.find('hid')!=-1:
                to_layer=to_neuron[:to_neuron.find('_')]
                j=to_neuron[to_neuron.find('_')+1:]
            elif to_neuron.find('in')!=-1:
                to_layer='in'
                j=to_neuron[to_neuron.find('in')+2:]
            elif to_neuron.find('out')!=-1:
                to_layer='out'
                j=to_neuron[to_neuron.find('out')+3:]
            else:
                print('in_neuron mistake')
                
            self.layer_to_layer_weight[from_layer+'_to_'+to_layer][int(j)][int(i)]=self.neuron_to_neuron_weight[key]                

    def updateBiasToLayerByBiasToNeuron(self):
        for key in self.bias_to_neuron:
            if key.find('hid')!=-1:
                #layer_key='hid'
                layer_key=key[:key.find('_')]
                i=key[key.find('_')+1:]
            elif key.find('in')!=-1:
                layer_key='in'
                i=key[key.find('in')+2:]
            elif key.find('out')!=-1:
                layer_key='out'
                i=key[key.find('out')+3:]
            else:
                print('mistake occurred when updating biasToLayer by biasToNeuron, key is'+key)
            
            self.bias_to_layer[layer_key][int(i)][0]=self.bias_to_neuron[key]            
    def setUnconditionedNeuron(self,neuron_key):  #food for dog
        from random import uniform
        if neuron_key.find('in')==-1:
                    print('mistake occurred, you can only appoint a input neuron to unconditioned neuron')
        else:
            self.unconditionedNeuron.append(neuron_key)
            for key in self.neuron_to_neuron_weight:
                from_neuron=key[:key.find('_to_')]
                to_neuron=key[key.find('to_')+3:]  
                if self.has_bias: 
                    bias=self.bias_to_neuron[to_neuron]
                    if bias<0:
                        bias=-bias
                    else:
                        self.bias_to_neuron[to_neuron]=-self.bias_to_neuron[to_neuron]
                    #while True:
                    #    if self.neuron_to_neuron_weight[key]<bias:
                    #        self.neuron_to_neuron_weight[key]=uniform(-1,1)
                    #    else:
                    #        break
                    if self.neuron_to_neuron_weight[key]!=None:
                        self.neuron_to_neuron_weight[key]=1
                #else:
                #    if self.neuron_to_neuron_weight[key]<0 and self.neuron_to_neuron_weight[key]!=None:
                #        #print self.neuron_to_neuron_weight[key]
                #        self.neuron_to_neuron_weight[key]=-self.neuron_to_neuron_weight[key]
                else:
                    if self.neuron_to_neuron_weight[key]!=None:
                        #print self.neuron_to_neuron_weight[key]
                        self.neuron_to_neuron_weight[key]=1
        self.updateLayerToLayerWeightByNeuronToNeuronWeight()  
                    

        
        
    def setConditionedNeuron(self,neuron_key):    #bell for dog
        if neuron_key.find('in')==-1:
            print('mistake occurred, you can only appoint a input neuron to conditioned neuron')
        else:
            self.conditionedNeuron.append(neuron_key)
            for key in self.neuron_to_neuron_weight:
                from_neuron=key[:key.find('_to_')]
                to_neuron=key[key.find('to_')+3:]
                if from_neuron==neuron_key and self.neuron_to_neuron_weight[key]!=None:
                    self.neuron_to_neuron_weight[key]=0
        self.updateLayerToLayerWeightByNeuronToNeuronWeight()
            
    def setRestOfInputNeuronToConditionedNeuronByKnownUnconditionedNeuron(self):
        for neuron in self.neuron_in_layer['in']:
            has_neuron=False
            for un_neuron in self.unconditionedNeuron:
                if un_neuron ==neuron:
                    #print 'go here'
                    has_neuron=True
                    break
            if not has_neuron:
                self.setConditionedNeuron(neuron)
                
    def setRestOfInputNeuronToUnconditionedNeuronByKnownConditionedNeuron(self):
        for neuron in self.neuron_in_layer['in']:
            has_neuron=False
            for un_neuron in self.conditionedNeuron:
                if un_neuron ==neuron:
                    has_neuron=True
                    break
            if not has_neuron:
                self.setUnconditionedNeuron(neuron)
                
    def setUnconditionedNeuronNum(self,num):
        for i in range(num):
            self.setUnconditionedNeuron(self.neuron_in_layer['in'][i])
        self.setRestOfInputNeuronToConditionedNeuronByKnownUnconditionedNeuron()
        
    def showNetworkSimulation(self):
        from pyneuron.tools.show_network_simulation_using_vpython import ShowNetworkSimulation
        show=ShowNetworkSimulation(self)
        #show.designPosition()
        #show.showNeurons()
        show.start()
        
    def setCompetitiveLayer(self,layer_key):
        for neuron in self.neuron_in_layer[layer_key]:
            self.setNeuronFunction(neuron, 'compet')
        
    def getWinnerNeuronFromCompetitiveLayer(self,layer_key):
        for neuron in self.neuron_in_layer[layer_key]:
            if self.neuron_function[neuron]=='compet':
                output=self.getOutputFromOneNeuron(neuron)
                if output==1:
                    winner_neuron=neuron
                    break
        self.winner_neuron=winner_neuron
        return winner_neuron
