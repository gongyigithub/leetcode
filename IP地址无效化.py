#coding:utf-8
'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
test:
input:address = "1.1.1.1"
output:"1[.]1[.]1[.]1"
'''

def defangIPaddr(address:str):
    '''
    将输入的IP地址里的.转换成[.]
    字符串替换，replace，re模块，format
    '''
    result = address.replace('.','[.]')
    import re
    result1 = re.sub(r'\.','[.]',address)
    print(result,'\n',result1)

address = "111.2.3.4"
defangIPaddr(address)