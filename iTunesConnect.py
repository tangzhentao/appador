#!/usr/bin/env python
'''
iTunes Connect account
used for distributing app to AppStore
'''

class iTunesConnect:
    def __init__(self, tag, username, password):
        self.tag = tag
        self.username = username
        self.password = password
    
    def display(self):
        print (self.__class__.__name__)
        print ('\ttag: %s\n \tusername: %s\n \tpassword: %s'% (self.tag, self.username, self.password))


if __name__ == '__main__':
    emama = iTunesConnect('emama', 'zhonghelida', 'zhonghelida123')
    emama.display()
