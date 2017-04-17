#! /usr/bin/env python

import os
import pathManager


AdHocOptions = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>compileBitcode</key>
    <false/>
    <key>method</key>
    <string>ad-hoc</string>
</dict>
</plist>
'''

AppStoreOptions = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>uploadSymbols</key>
    <true/>
    <key>uploadBitcode</key>
    <true/>
    <key>method</key>
    <string>app-store</string>
</dict>
</plist>
'''

class ExportOptions(pathManager.PathManager):
    '''
    export archive file options

    '''
    def __init__(self):
        pass

    def generateAdHocPlist(self):
        plistPath = self.AdHocExportOptionsPlistPath()
        f = open(plistPath, 'w')
        f.write(AdHocOptions)
        f.close()

    def generateAppStorePlist(self):
        plistPath = self.AppStoreExportOptionsPlistPath()
        f = open(plistPath, 'w')
        f.write(AppStoreOptions)
        f.close()
        pass

    def AdHocExportOptionsPlistPath(self):
        exportOptionsPath = self.exportOptionsPath()
        AdHocExportOptionsPlistPath = os.path.join(exportOptionsPath, 'AdHocExportOptions.plist')

        return AdHocExportOptionsPlistPath

    def AppStoreExportOptionsPlistPath(self):
        exportOptionsPath = self.exportOptionsPath()
        AppStoreExportOptionsPlistPath = os.path.join(exportOptionsPath, 'AppStoreExportOptions.plist')

        return AppStoreExportOptionsPlistPath


    @classmethod 
    def testGeneratePlists(cls):
        exportOptions = ExportOptions()
        exportOptions.generateAdHocPlist()
        exportOptions.generateAppStorePlist()

if __name__ == '__main__':

    ExportOptions.testGeneratePlists()
