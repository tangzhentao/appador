#! /usr/bin/env python

import os
import time
import classtools

class ExportOption(classtools.AttrDisplay):
    '''
    export archive file options

    '''
    def __init__(self):
        pass

    def generatePlist(self):
        pass

    def generateDefaultAdHocPlist(self):
        pass

    def generateDefaultAppStorePlist(self):
        pass


    @classmethod 
    def testExport(cls):
        archivePath = '/Users/tang/Documents/appador/PublishScriptDemo/archive/PublishScriptDemo_2017-04-15_18-28-24.xcarchive'
        exportPath = '/Users/tang/Documents/appador/PublishScriptDemo/ipa'
        plistPath = '/Users/tang/exportOptionPlist/AppStoreExportOptions.plist'

        exporter1 =  Exporter(archivePath, exportPath, plistPath)
        exporter1.export()

if __name__ == '__main__':
    Exporter.testExport()

