'''
Created on 2012-6-1

@author: shd101wyy


save and load neural network and data set
'''
from functions.convert_string_list_to_pure_list import convertStringListToList
from data.DataSet import DataSet
from neuron_build.neuron_build import NeuronBuilder
from functions.convert_string_dict_to_pure_dict import convertStringDictToDict
class NeuralTools(object):
    def __init__(self):
        pass
    
    def saveNeuronBuilder(self,neuron_builder,save_path):
        self.net=neuron_builder
        input_layer=self.net.input_layer
        hidden_layers=self.net.hidden_layers
        output_layer=self.net.output_layer
        has_bias=self.net.has_bias
        layer_to_layer_weight=self.net.layer_to_layer_weight
        bias_to_layer=self.net.bias_to_layer
        neuron_function=self.net.neuron_function
        neuron_dict=self.net.neuron_dict
        name_dict=self.net.name_dict
        input_data=self.net.input_data
        output_data=self.net.output_data
        
        
        inputString=''
        inputString=inputString+"input_layer:"+str(input_layer)+'\n'
        inputString=inputString+"hidden_layers:"+str(hidden_layers)+'\n'
        inputString=inputString+"output_layer:"+str(output_layer)+'\n'
        inputString=inputString+"has_bias:"+str(has_bias)+'\n'
        inputString=inputString+"layer_to_layer_weight:"+str(layer_to_layer_weight)+'\n'
        inputString=inputString+"bias_to_layer:"+str(bias_to_layer)+'\n'
        inputString=inputString+"neuron_function:"+str(neuron_function)+'\n'
        inputString=inputString+"neuron_dict:"+str(neuron_dict)+'\n'
        inputString=inputString+"name_dict:"+str(name_dict)+'\n'
        inputString=inputString+"input_data:"+str(input_data)+'\n'
        inputString=inputString+"output_data:"+str(output_data)+'\n'
        if save_path.find('.')==-1:
            save_path+='.nnet'
        createFile=open(save_path,'w')
        createFile.write(inputString)
        createFile.close()
        
        print('finish saving neuron builder in'+save_path)
           
    def saveDataSet(self,data_set,save_path):
        input_data=data_set.input_data
        output_data=data_set.output_data
        createFile=open(save_path,'w')
        inputString=''
        for i in range(len(input_data)):
            inputString=inputString+'input:'+str(input_data[i])+'\n'
            inputString=inputString+'output:'+str(output_data[i])+'\n'
        createFile.write(inputString)
        createFile.close()
        
    def loadNeuronBuilder(self,save_path):
        '''
        input_layer=self.net.input_layer
        hidden_layers=self.net.hidden_layers
        output_layer=self.net.output_layer
        has_bias=self.net.has_bias
        layer_to_layer_weight=self.net.layer_to_layer_weight
        bias_to_layer=self.net.bias_to_neuron
        neuron_function=self.net.neuron_function
        neuron_dict=self.net.neuron_dict
        name_dict=self.net.name_dict
        input_data=self.net.input_data
        output_data=self.net.output_data
        '''
        import os
        if save_path.find('.')==-1:
            save_path+='.nnet'
        if os.path.exists(save_path):
            file=open(save_path,'r')
            output=[]
            for lines in file:
                output.append(lines)
            #print output
            dic={}
            for line in output:
            #    print line
                dic[line[0:line.find(':')]]=line[line.find(':')+1:line.find('\\')]
            #print dic
            file.close()
            input_layer=convertStringListToList(dic['input_layer'])
            for i in range(len(input_layer)):
                input_layer[i]=int(input_layer[i])
                
            hidden_layers=convertStringListToList(dic['hidden_layers'])
            for i in range(len(hidden_layers)):
                hidden_layers[i]=int(hidden_layers[i])
                
            output_layer=convertStringListToList(dic['output_layer'])
            for i in range(len(output_layer)):
                output_layer[i]=int(output_layer[i])
            has_bias=dic['has_bias']
            if has_bias=='True':
                has_bias=True
            elif has_bias=='False':
                has_bias=False
            else:
                print("Mistake occurred when load has_bias:"+has_bias)
                
            layer_to_layer_weight=convertStringDictToDict(dic['layer_to_layer_weight'])
            print dic['layer_to_layer_weight']
            print layer_to_layer_weight
            for key in layer_to_layer_weight.keys():
                layer_to_layer_weight[key]=convertStringListToList(layer_to_layer_weight[key])
            
            bias_to_layer=convertStringDictToDict(dic['bias_to_layer'])
            print dic['bias_to_layer']
            print bias_to_layer
            for key in bias_to_layer:
                bias_to_layer[key]=convertStringListToList(bias_to_layer[key])
        
            neuron_function=convertStringDictToDict(dic['neuron_function'])
            neuron_dict=convertStringDictToDict(dic['neuron_dict'])
            name_dict=convertStringDictToDict(dic['name_dict'])
            input_data=convertStringListToList(dic['input_data'])
            output_data=convertStringListToList(dic['output_data'])
            
            net=NeuronBuilder(input_layer,hidden_layers,output_layer,has_bias)
            net.layer_to_layer_weight=layer_to_layer_weight
            net.updateNeuronToNeuronWeightByLayerToLayerWeight()
            net.bias_to_layer=bias_to_layer
            net.updateBiasToNeuronByBiasToLayer()
            net.neuron_function=neuron_function
            net.neuron_dict=neuron_dict
            net.name_dict=name_dict
            
            data=DataSet(len(input_data[0]),len(output_data[0]))
            for i in range(len(input_data)):
                data.addItem(input_data[i], output_data[i])
            net.setDataSet(data)
            
            #print neural_network_type
            #print input_num
            #print output_num
            #print weight
            #print bias
            #print function_name
            return net
        else:
            print(save_path+"does not exist")
            return None
    def loadDataSet(self,save_path):
        '''
        input_data
        output_data
        
        
        '''
        import os
        if os.path.exists(save_path):
            file=open(save_path,'r')
            output=[]
            num=0
            for line in file:
                inputString=line[line.find("["):line.find("\n")]
                output.append(inputString)
                num+=1
                #print line
            #print output
            input_data=[]
            output_data=[]
            for i in range(num/2):
                input_data.append(convertStringListToList(output[2*i]))
                output_data.append(convertStringListToList(output[2*i+1]))
            input_num=len(input_data[0])
            output_num=len(output_data[0])
            data=DataSet(input_num,output_num)
            for i in range(len(input_data)):
                data.addItem(input_data[i], output_data[i])
            return data
        else:
            print(save_path+"does not exist")
        
        
    


'''
    def saveNetwork(self,network,save_path):
        neural_network_type=network.neural_network_type
        input_num=network.input_num
        output_num=network.output_num
        weight=network.weight
        bias=network.bias
        function_name=network.function_name
        
        inputString=''
        inputString=inputString+"type:"+str(neural_network_type)+'\n'
        inputString=inputString+"input_num:"+str(input_num)+'\n'
        inputString=inputString+"output_num:"+str(output_num)+'\n'
        inputString=inputString+"weight:"+str(weight)+'\n'
        inputString=inputString+"bias:"+str(bias)+'\n'
        inputString=inputString+"function_name:"+str(function_name)+'\n'
        
        createFile=open(save_path,'w')
        createFile.write(inputString)
        createFile.close()
        
    def loadNetwork(self,save_path):
        neural_network_type
        input_num
        output_num
        weight
        bias
        function_name
    
        import os
        if os.path.exists(save_path):
            file=open(save_path,'r')
            output=[]
            for lines in file:
                output.append(lines)
            #print output
            dic={}
            for line in output:
            #    print line
                dic[line[0:line.find(':')]]=line[line.find(':')+1:line.find('\\')]
            #print dic
            neural_network_type=dic['type']
            input_num=int(dic['input_num'])
            output_num=int(dic['output_num'])
            weight=convertStringListToList(dic['weight'],output_num,input_num)
            bias=convertStringListToList(dic['bias'],output_num,1)
            function_name=dic['function_name']
            #print neural_network_type
            #print input_num
            #print output_num
            #print weight
            #print bias
            #print function_name
        else:
            print(save_path+"does not exist")
'''