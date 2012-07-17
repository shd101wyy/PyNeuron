'''
Created on 2012-6-6

@author: shd101wyy

for example: this function will convert 
{'out0': 'hardlim', 'out1': 'hardlim', 'out2': 'hardlim', 'out3': 'hardlim'}
from string to dict

however this function will only convert
{'apple':1,'peach':2}
to
{'apple':'1', 'peach':'2'}
'''
'''
def convertStringDictToDict(string_dict):
    #print string_dict
    string_dict=string_dict.replace('{','')
    #print string_dict
    string_dict=string_dict.replace('}','')
    #print string_dict
    string_dict=string_dict.replace('\'','')
    #print string_dict
    string_dict=string_dict.replace(' ','')
    #print string_dict
    string_dict=string_dict.replace(':',' ')
    #print string_dict
    a=string_dict.split(',')
    dict={}
    for elem in a:
        key=elem[:elem.find(' ')]
        responce=elem[elem.find(' ')+1:]
        dict[key]=responce
    #print dict
    return dict
'''
def convertStringDictToDict(string_dict):
    #print string_dict
    string_dict=string_dict.replace('{','')
    #print string_dict
    string_dict=string_dict.replace('}','')
    #print string_dict
    string_dict=string_dict.replace('\'','')
    #print string_dict
    string_dict=string_dict.replace(' ','')
    #print string_dict
    
    
    index_of_colon=string_dict.find(':') #:
    index_of_comma=-1 #,
    dict={}
    while index_of_colon!=-1:
        key=string_dict[index_of_comma+1:index_of_colon]
        old_index_of_colon=index_of_colon
        index_of_colon=string_dict.find(':',index_of_colon+1)
        if index_of_colon==-1:
            responce=string_dict[old_index_of_colon+1:]
            dict[key]=responce
            break
        index_of_comma=string_dict.find(',',index_of_comma+1,index_of_colon)
        if index_of_comma!=-1:
            temp=string_dict.find(',',index_of_comma+1,index_of_colon)
        else:
            temp=-1
        while temp!=-1:
            index_of_comma=string_dict.find(',', index_of_comma+1,index_of_colon)
            temp=string_dict.find(',',index_of_comma+1,index_of_colon)
        responce=string_dict[old_index_of_colon+1:index_of_comma]
        dict[key]=responce
    return dict

