#! /usr/bin/env python

'distribute tool, distribute ipa to some server'

import os
import iTunesConnect
import subprocess

class Distributer:
    '''
    distribute base class
    '''
    def __init__(self, ipaPath):
        self.ipaPath = ipaPath
        # check ipa file 
        self.check_ipa();

    def check_ipa(self):
        '''
        check:
        1. whether ipa at ipaPath  exists
        2. whether ipa at ipaPath is directory
        3. whether ipa's extension at ipaPath is .ipa
        '''
        if os.path.exists(self.ipaPath):
            if os.path.isfile(self.ipaPath):
                root, ext = os.path.splitext(self.ipaPath)
                if ext == '.ipa':
                    pass
                else:
                    print ('"%s" is not ipa file!' % (self.ipaPath))
            else:
                print ('"%s" is not ipa file(not file)!' % (self.ipaPath))
        else:
            print ('"%s" does not exist!' % (self.ipaPath))

class AppStoreDistributer(Distributer):
    altool_path = '/Applications/Xcode.app/Contents/Applications/Application Loader.app/Contents/Frameworks/ITunesSoftwareService.framework/Versions/A/Support/altool'
    def __init__(self, ipaPath, iTunesConnect):
        self.check_altool()
        Distributer.__init__(self, ipaPath)
        self.iTunesConnect = iTunesConnect

    def check_altool(self):
        if os.path.exists(self.altool_path):
            pass
        else:
            errortext = 'altool(at path: %s) does not exist!' % self.altool_path
            print errortext
            os._exit(0)

    def distribute(self):
        print ('\n{0} distribute {1}\n'.format(10 * '-', 10 * '-'))
        print ('ipa path: %s' % self.ipaPath)
        print ('iTunesConnect: %s\n'% self.iTunesConnect.username)
        print ('will distribute...')
        # '%s': to handle white space in path
        command = "'%s' -f %s -t ios -u %s -p %s --upload-app" % (self.altool_path, self.ipaPath, self.iTunesConnect.username, self.iTunesConnect.password)
        print ('command: %s' % command)
        status = os.system(command)
        print ('status = %d' % status)
        #ps = subprocess.Popen(command)
        
        ''' status:
        256   Error: Unable to validate your application. Your Apple ID or password was entered incorrectly.
        '''


if __name__ == '__main__':
    p1 = '/no/exist'
    p2 = '/Users/tang/Documents/log.txt'
    p3 = '/Users/tang/Documents/testipa'
    p4 = '/Users/tang/Documents/CareerRelease.ipa'
    d1 = Distributer(p1)
    d2 = Distributer(p2)
    d3 = Distributer(p3)
    d4 = Distributer(p4)
    # test AppStoreDistributer 
    pushDemoPath = '/Users/tang/Desktop/PublishScriptDemo17-04-25/PublishScriptDemo.ipa'
    bole_ic= iTunesConnect.iTunesConnect(tag = 'bole', username = 'zhonghelida_apps@sina.com', password = 'zhldMIMA2')
    appstore_d = AppStoreDistributer(ipaPath = pushDemoPath, iTunesConnect = bole_ic)

    # distribute
    appstore_d.distribute()
