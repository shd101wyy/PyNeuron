'''
Created on 2012-5-31

@author: shd101wyy
'''
import random
def initialize(weight_or_bias):
    for row in range(len(weight_or_bias)):
        for column in range(len(weight_or_bias[0])):
            weight_or_bias[row][column]=random.uniform(-1,1)
    return weight_or_bias