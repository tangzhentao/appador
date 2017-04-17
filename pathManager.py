#! /usr/bin/env python

import os
import time
import classtools

class PathManager (classtools.AttrDisplay):
    '''
    manager the paths appador used.
    '''
    def __init__(self):
        pass

    def exportOptionsPath(self):
        '''
        return export Options path:~/Documents/appador/exportOptions/
        create it, if appador does not exist.
        '''
        appadorHomePath = self.appadorHomePath()
        exportOptionsPath = os.path.join(appadorHomePath, 'exportOptions')

        # check if exists
        if not os.path.exists(exportOptionsPath):
            os.makedirs(exportOptionsPath)
         
        return exportOptionsPath

    def appadorHomePath(self):
        '''
        return appad home path:~/Documents/appador
        create it, if appador does not exist.
        '''
        documentsPath = self.documentsPath()
        appadorHomePath = os.path.join(documentsPath, 'appador')

        # check if exists
        if not os.path.exists(appadorHomePath):
            os.makedirs(appadorHomePath)

        return appadorHomePath

    def documentsPath(self):
        homePath = os.path.expandvars('$HOME')
        documentsPath = os.path.join(homePath, 'Documents')
        return documentsPath 

    def currentTime(self):
        currentTime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        return currentTime


    @classmethod 
    def testAppadorHomePath(cls):
        appadorHomePath = PathManager().appadorHomePath()
        print appadorHomePath

    @classmethod 
    def testExportOptionsPath(cls):
        exportOptionsPath = PathManager().exportOptionsPath()
        print exportOptionsPath

if __name__ == '__main__':
    PathManager.testAppadorHomePath()
    PathManager.testExportOptionsPath()
