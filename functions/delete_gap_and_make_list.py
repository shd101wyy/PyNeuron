'''
Created on 2012-6-1

@author: shd101wyy
'''

'''
for example the string is 1,3,5,3
so gap is ','
so this function return [1,3,5,3]


'''
def deleteGapAndMakeList(inputString,gap):
    inputString=inputString.split(gap)
    output=[]
    for elem in inputString:
        output.append(float(elem))
    return output
        