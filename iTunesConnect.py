#!/usr/bin/env python
'''
iTunes Connect account
used for distributing app to AppStore
'''

import classtools

class iTunesConnect:
    def __init__(self, username, password, tag=''):
        # if no specific tag, use username as tag
        if tag == '':
            tag = username

        self.tag = tag
        self.username = username
        self.password = password
        self.selected = False

    def __str__(self):
        selected_flag = ''
        if self.selected:
            selected_flag = '*'
        des = '[%s: username: %s, password: %s, tag: %s]%s' % (self.__class__.__name__, self.username, self.password, self.tag, selected_flag)
        return des
    
if __name__ == '__main__':
    emama = iTunesConnect('zhonghelida', 'zhonghelida123')
    print emama
