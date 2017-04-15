#! /usr/bin/env python

import os
import time
import classtools

class Archiver(classtools.AttrDisplay):
    '''
    archive project/workspace specified to archive path by scheme

    '''
    def __init__(self, path, scheme, archivePath=None):
        self.path = path
        self.fileType = self.fileType()
        self.scheme = scheme
        self.archivePath = archivePath

    def fileType(self):
        '''
        return -project, -workspace or None by self.path
        '''
        fileType = None
        root, ext = os.path.splitext(self.path)
        if ext == '.xcodeproj':
            fileType  = '-project'
        elif ext == '.xcworkspace':
            fileType= '-workspace'
        else:
            pass
        return fileType

    def archive(self):
        print ('\n{0} archive {1}\n'.format(10 * '-', 10 * '-'))

        # generate default archive path ,if no exists
        if self.archivePath is None:
            self.archivePath = self.defaultArchivePath()

        # print archive info 
        print ('project/workspace path: %s' % self.path)
        print ('file type: %s' % self.fileType)
        print ('scheme: %s' % self.scheme)
        print ('archive path: %s' % self.archivePath)

        # check path
        self.checkPath()

        # '%s': to handle white space in path
        command = "xcodebuild %s '%s' -scheme %s -archivePath '%s' archive " % (self.fileType, self.path, self.scheme, self.archivePath)
        print command
        status = os.system(command)
        print ('status = %d' % status)

    def checkPath(self):
        '''
        check path:
        1. does exist ?
        2. is directory ?
        3. is project or workspace file?
        '''
        if os.path.exists(self.path):
            if os.path.isdir(self.path):
                if self.fileType is None:
                    print ('%s: is not project or workspace file!' % self.path)
                    os._exit(0)
            else:
                print ('%s: is not project or workspace file!' % self.path)
                os._exit(0)
        else:
            print ('%s: does not exist!' % self.path)
            os._exit(0)

    def defaultArchivePath(self):
        '''
        Xcode product archive name format: schemeName + date + .xcarchive.
        when we pass -archivePath to xcodebuild archive, extension(.xcarchive) is auto generated.
        so archivePath passed  need not include extension(.xcarchive)
        we put archive file to user Documets, that is,
        ~/Document/appador/archive/archiveName
        '''
        archiveDirectoryPath = self.archiveDirectoryPath()
        archiveName = self.archiveName()
        archivePath = os.path.join(archiveDirectoryPath, archiveName)

        return archivePath

    def archiveDirectoryPath(self):
        documentsPath = self.documentsPath()
        archiveDirectoryPath = os.path.join(documentsPath, 'appador', self.scheme, 'archive')
        if not os.path.exists(archiveDirectoryPath):
            os.makedirs(archiveDirectoryPath)
        
        return archiveDirectoryPath

    def archiveName(self):
        currentTime = self.currentTime()
        name = self.scheme + '_' + currentTime

        return name

    def documentsPath(self):
        homePath = os.path.expandvars('$HOME')
        documentsPath = os.path.join(homePath, 'Documents')
        return documentsPath 

    def currentTime(self):
        currentTime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        return currentTime


    @classmethod 
    def testInit(cls):
        path1 = '/Volumes/Data/svn_projects/PublishScript/PublishScriptDemo/PublishScriptDemo.xcodeproj'
        path2 = '/Volumes/Data/svn_projects/PublishScript/PublishScriptDemo/PublishScriptDemo.xcworkspace'
        path3 = '/Volumes/Data/svn_projects/PublishScript/PublishScriptDemo'
        path4 = '/Volumes/Data/svn_projects/PublishScript/PublishScriptDemo/noExist'
        scheme = 'PublishScriptDemo'
        archiver1 = Archiver(path1, scheme)
        print (archiver1)
        archiver2 = Archiver(path2, scheme)
        print (archiver2)
        archiver3 = Archiver(path3, scheme)
        print (archiver3)
        archiver4 = Archiver(path4, scheme)
        print (archiver4)
    
    @classmethod
    def testArchive(cls):
        path1 = '/Volumes/Data/svn_projects/PublishScript/PublishScriptDemo/PublishScriptDemo.xcodeproj1'
        scheme = 'PublishScriptDemo'
        archiver1 = Archiver(path1, scheme)
        archiver1.archive()





if __name__ == '__main__':
    #Archiver.testInit()
    Archiver.testArchive()

