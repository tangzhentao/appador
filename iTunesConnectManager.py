#!/usr/bin/env python
'''
iTunes Connect account manager
manager multiple accounts and select one account
used for distributing app to AppStore
'''

import shelve
import os
import iTunesConnect
import copy 

class iTunesConnectManager:
    ''' 
    manager iTnues connect account
    '''

    def __init__(self, iTunesConnects=None):
        # get home path
        home = os.path.expandvars('$HOME')
        # config folder
        config_path = '.appador/iTunesConnectsdb'
        self._dbPath = os.path.join(home, config_path)

    def getDb(self):
        '''
        get loacl db that stores iTunes connect accounts
        '''
        db = shelve.open(self.dbPath())
        return db

    def dbPath(self):
        # check whether directory exists
        dirPath = os.path.dirname(self._dbPath)
        if os.path.exists(dirPath):
            pass
        else:
            # create db directory
            os.makedirs(dirPath)

        return self._dbPath;
    
    def addiTunesConnect(self, iTunesConnect):
        ''' 
        add iTunesConnect to local db
        '''
        # get db
        db = self.getDb()
        # add record to db
        db[iTunesConnect.tag] = iTunesConnect
        # close db
        db.close()

    def removeiTunesConnect(self, iTunesConnect):
        '''
        remove iTunes connect account from loacl db
        '''
        # get db
        db = self.getDb()
        # remove record from db
        del db[iTunesConnect.tag]
        # close db
        db.close()

    def selectiTunesConnect(self, iTunesConnect):
        '''
        select iTunes connect account from local db
        '''
        # make a deep copy of iTunesConnect and operate copy
        ic_copy = copy.deepcopy(iTunesConnect)
        # get db
        db = self.getDb()
        # get current selected iTunes connect
        selected_ic = None
        for tag in db:
            ic = db[tag]
            if ic.selected:
                selected_ic = ic
                break
        # check current selected iTunes connect and iTunesConnect, 
        # if same, do nothing, or deselect current iTunes connect and select iTunesConnect
        if selected_ic:
            if selected_ic.tag == ic_copy.tag:
                pass
            else:
                selected_ic.selected = False
                db[selected_ic.tag] = selected_ic
                
                ic_copy.selected = True
                db[ic_copy.tag] = ic_copy
        else:
            ic_copy.selected = True
            db[ic_copy.tag] = ic_copy


        # close db
        db.close()

    def selectiTunesConnectByTag(self, tag):
        '''
        select iTunes connect account from local db by tag
        '''

        # get db
        db = self.getDb()
        # chekc  iTunesConnect with tag if exists
        if db.has_key(tag):
            # exists and select it
            ic = db[tag]
            self.selectiTunesConnect(ic)
        else:
            print ('iTunesConnect with %s does not exist' % (tag))

    def removeiTunesConnectByTag(self, tag):
        '''
        remove iTunes connect account with tag from local db
        '''
        # get db
        db = self.getDb()
        # chekc  iTunesConnect with tag if exists
        if db.has_key(tag):
            # exists and select it
            ic = db[tag]
            self.removeiTunesConnect(ic)
        else:
            print ('iTunesConnect with %s does not exist' % (tag))

    def selectediTunesConnect(self):
        '''
        return seleced iTunes connect account
        '''
        # get db
        db = self.getDb()

        selected_ic = None
        for tag in db:
            ic = db[tag]
            if ic.selected:
                selected_ic = ic
                break

        return selected_ic

    def iTunesConnectWithTag(self, tag):
        '''
        return theiTunes connect account whose tag is passed tag
        '''
        # get db
        db = self.getDb()
        ic = db[tag]
        return ic
        
        
    def printDb(self):
        '''
        print all of local db recoard
        '''
        # get db
        db = self.getDb()
        # get number of db's recoard
        keys = db.keys()
        num = len(keys)

        if num == 0:
            print ('no iTunes connect!')
        else:
            print ('all iTunes connects:')
            for tag in db:
                ic = db[tag]
                print ic
# self test
if __name__ == '__main__':
    emama = iTunesConnect.iTunesConnect('emama', 'zhonghelida', 'zhonghelida123')
    yueke = iTunesConnect.iTunesConnect('yueke', 'yuekeusername', 'yueke123')

    # test iTunesConnectManager
    icm = iTunesConnectManager()
    icm.addiTunesConnect(emama)
    icm.addiTunesConnect(yueke)
    icm.printDb()
    # select emama
    icm.selectiTunesConnect(emama)
    icm.printDb()
    # select yueke
    icm.selectiTunesConnect(yueke)
    icm.printDb()
    # remove yueke
    icm.removeiTunesConnect(yueke)
    icm.removeiTunesConnect(emama)
    icm.printDb()
    # test select by tag
    print ('%s test select by tag %s' % (10 * '-', 10 * '-'))
    icm.addiTunesConnect(emama)
    icm.addiTunesConnect(yueke)
    print ('before select:')
    icm.printDb()
    icm.selectiTunesConnectByTag('eeeeeemama')
    icm.printDb()
    icm.selectiTunesConnectByTag('emama')
    icm.printDb()
    # test selected iTunes connect
    selected_ic = icm.selectediTunesConnect()
    print ('selected iTunes connect: %s' % (selected_ic))
