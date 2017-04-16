#! /usr/bin/env python

import os
import time
import classtools

class Exporter(classtools.AttrDisplay):
    '''
    export archive file to ipa file

    '''
    def __init__(self, archivePath, exportPath, exportOptionsPlist):
        self.archivePath = archivePath
        self.exportPath = exportPath
        self.exportOptionsPlist = exportOptionsPlist


    def export(self):
        '''
        exportPath is the directory path. we can decide where put ipa file. 
        but we cannot decide the name of ipa file. the name of ipa file is scheme name.
        xcodebuild will make the directories, if no exist at exportPath.
        if already exists same name ipa file, xcodebuild will override it.
        '''
        print ('\n{0} export {1}\n'.format(10 * '-', 10 * '-'))

        # print export info 
        print ('archive path: %s' % self.archivePath)
        print ('export path: %s' % self.exportPath)
        print ('exportOptionsPlist path: %s' % self.exportOptionsPlist)

         #check path
        self.checkPath()

        # '%s': to handle white space in path
        command = "xcodebuild -exportArchive -archivePath '%s' -exportPath '%s' -exportOptionsPlist '%s' " % (self.archivePath, self.exportPath, self.exportOptionsPlist)

        print ''
        print 'command:'
        print command
        print ''
        status = os.system(command)
        print ('status = %d' % status)

    def checkPath(self):
        self.checkArchivePath()
        self.checkExportOptionsPlist()

    def checkArchivePath(self):
        '''
        check path:
        1. does exist ?
        2. is directory ?
        3. is archive file?
        '''
        if os.path.exists(self.archivePath):
            if os.path.isdir(self.archivePath):
                root, ext = os.path.splitext(self.archivePath)
                if ext != '.xcarchive':
                    print ('%s: is not archive file!' % self.archivePath)
                    os._exit(0)
            else:
                print ('%s: is not archive file!' % self.archivePath)
                os._exit(0)
        else:
            print ('%s: does not exist!' % self.archivePath)
            os._exit(0)


    def checkExportOptionsPlist(self):
        '''
        check path:
        1. does exist ?
        2. is file ?
        3. is plist file?
        '''
        if os.path.exists(self.exportOptionsPlist):
            if os.path.isfile(self.exportOptionsPlist):
                root, ext = os.path.splitext(self.exportOptionsPlist)
                if ext != '.plist':
                    print ('%s: is not plist file!' % self.exportOptionsPlist)
                    os._exit(0)
            else:
                print ('%s: is not plist file!' % self.exportOptionsPlist)
                os._exit(0)
        else:
            print ('%s: does not exist!' % self.exportOptionsPlist)
            os._exit(0)

    @classmethod 
    def testExport(cls):
        archivePath = '/Users/tang/Documents/appador/PublishScriptDemo/archive/PublishScriptDemo_2017-04-15_18-28-24.xcarchive'
        exportPath = '/Users/tang/Documents/appador/PublishScriptDemo/ipa'
        plistPath = '/Users/tang/exportOptionPlist/AppStoreExportOptions.plist'

        exporter1 =  Exporter(archivePath, exportPath, plistPath)
        exporter1.export()

if __name__ == '__main__':
    Exporter.testExport()

