#!/usr/bin/env python
'''
'''

class foo:
    def __init__(self):
        self._name = 'tang'
        print '__init__'
    
    def display(self):
        print self.name()

    def name(self):
        print 'call name func'
        return self._name
    def setName(self, name):
        self.name = name


if __name__ == '__main__':
    f = foo()
    f.display()
