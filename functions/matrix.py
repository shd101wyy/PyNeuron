'''
Created on 2012-6-4

@author: shd101wyy

multiplyTwoListMatrix(list1,list2)is no the same as multiplyTwoListMatrix(list2,list1)
'''

class Matrix(object):
    def __init__(self):
        pass
    def multiply(self,list1,list2):
        output=[[0 for column in range(len(list2[0]))]for row in range(len(list1))]
        for i in range(len(output)):
            for j in range(len(output[0])):
                output[i][j]=0
                count=0
                for a in range(len(list1[0])):
                    if list1[i][a]==None or list2[a][j]==None:
                        output[i][j]+=0
                        count+=1
                    else:
                        output[i][j]+=list1[i][a]*list2[a][j]
                    if count==len(list1[0]):
                        output[i][j]=None
                    
        #print output
        return output
    
    def plus(self,list1,list2):
        output=[[0 for column in range(len(list1[0]))]for row in range(len(list1))]
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                output[i][j]=list1[i][j]+list2[i][j]
        return output
    def transpose(self,list1):
        list2=[[0 for column in range(len(list1))]for row in range(len(list1[0]))]
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                list2[j][i]=list1[i][j]
                
        return list2
    

    

    
    
    
