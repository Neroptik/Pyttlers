'''
Created on 22 nov. 2012

@author: VJLT0530
'''

import pyamf.remoting

class Test():
    def __init__(self, a, b, c):
        '''
        Test class initialization
        :param a:toto
        :param b:tata
        :param c:titi
        '''
        self.a = a
        self.b = b
        self.c = c
    
if __name__ == '__main__':
    envelope = pyamf.remoting.Envelope(3)
    print envelope