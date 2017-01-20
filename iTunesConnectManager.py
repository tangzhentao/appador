#!/usr/bin/env python
'''
iTunes Connect account manager
manager multiple accounts and select one account
used for distributing app to AppStore
'''

import shelve
import os
import iTunesConnect

class iTunesConnectManager:
    def __init__(self, iTunesConnects=None):
        self.iTunesConnects = iTunesConnects
        self._dbPath = '~/.appador/iTunesConnectsdb'

    def getDb(self):
        db = shelve.open(self.dbPath())
        return db

    def dbPath(self):
        # check whether directory exists
        print ('db path: {0}'.format(self._dbPath))
        dirPath = os.path.dirname(self._dbPath)
        print ('db directory: {0}'.format(dirPath))
        if os.path.exists(dirPath):
            print ('db directory[{0}] exists'.format(dirPath))
        else:
            print ('db directory[{0}] does not  exist'.format(dirPath))
            # create db directory
            os.makedirs(dirPath)
            print ('created directory: {0}'.format(dirPath))

        return self._dbPath;
    
    def addiTunesConnect(self, iTunesConnect):
        print ('call addiTunesConnect')
        # get db
        db = self.getDb()
        # add record to db
        db[iTunesConnect.tag] = iTunesConnect
        # close db
        db.close()

    def removeiTunesConnect(self, iTunesConnect):
        print ('removeiTunesConnect')
        # get db
        db = self.getDb()
        # remove record from db
        del db[iTunesConnect.tag]
        # close db
        db.close()

        
    def display(self):
        print (self.__class__.__name__)
        print(self.iTunesConnects)

if __name__ == '__main__':
    emama = iTunesConnect('emama', 'zhonghelida', 'zhonghelida123')
    emama.display()
