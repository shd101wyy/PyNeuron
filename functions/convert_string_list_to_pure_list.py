'''
Created on 2012-6-1

@author: shd101wyy
'''
'''
for example:
    for string kind of list [[1,2],[3,4]]
    this function will return list [[1,2],[3,4]]
    for string kind of list [1,2,3,4]
    this functions will return list [1,2,3,4]



'''
def convertStringListToList(inputString):
    
    if inputString.count("[")==1:
        output=[]
        inputString=inputString.replace('[','')
        inputString=inputString.replace(']','')
        if inputString.find(' ')!=-1:
            inputString=inputString.replace(' ','')
        inputString=inputString.split(',')
        for elem in inputString:
            #output.append(int(elem))
            output.append(float(elem))
    
    else:
        row=inputString.count('[')-1
        column= inputString[inputString.find('[',inputString.find('[')+1):inputString.find(']')].count(',')+1
        output=[[0 for j in range(column)]for i in range(row)]
        
        inputString=inputString[1:len(inputString)-1]
        inputString=inputString.replace('[','')
        inputString=inputString.replace(']','')
        if inputString.find(' ')!=-1:
            inputString=inputString.replace(' ','')
        inputString=inputString.split(",")
        for i in range(row):
            for j in range(column):
                output[i][j]=float(inputString[i*column+j])
    return output


