import binascii  

def to_bytes(inputString):
    bin=lambda n:(n > 0) and (bin(n/2) + str(n%2)) or ''  
    s = inputString
    s_16 = binascii.b2a_hex(s)  
    s_10 = int(s_16,16)  
    s_2 = bin(s_10)  
    return s_2
