'''
Created on 2012-5-31

@author: shd101wyy
'''
'''
input_data=[[data1],[data2]]
output_data=[[data1],[data2]]

'''
class DataSet(object):
    def __init__(self,input_num,output_num):
        self.input_num=input_num
        self.output_num=output_num
        self.input_data=[[]]
        self.output_data=[[]]
        
    def addItem(self,input_data,output_data):
        def autoSave():
            createFile=open('temp_dataSet.dat','w')
            inputString=''
            for i in range(len(self.input_data)):
                inputString=inputString+'input:'+str(self.input_data[i])+'\n'
                inputString=inputString+'output:'+str(self.output_data[i])+'\n'
            createFile.write(inputString)
            createFile.close()
                
        if len(input_data)!=self.input_num or len(output_data)!=self.output_num:
            print("mistakes occurred when adding input or output ")
            print("mistake input data"+str(input_data))
            print("mistake output data"+str(output_data))
        self.input_data.append(input_data)
        self.output_data.append(output_data)
        if self.input_data[0]==[]:
            self.input_data.remove([])
            self.output_data.remove([])
        autoSave()
    def returnDataSet(self):
        return [self.input_data,self.output_data]
        
    
