print('Online Script Loaded\n')

"""
https://raw.githubusercontent.com/burasate/test/master/SetupSystem/main.py
TESTING ZONE
"""
from maya import cmds
from maya import mel
import urllib2
import shutil
import zipfile
import os


def formatPath(path):
    path = path.replace("/", os.sep)
    path = path.replace("\\", os.sep)
    return path

mayaAppDir = formatPath(mel.eval('getenv MAYA_APP_DIR'))
scriptsDir = formatPath(mayaAppDir + os.sep + 'scripts')
projectDir = formatPath(scriptsDir+os.sep+'BRSLocDelay')
userFile = formatPath(projectDir + os.sep + "user")

print ('mayaAppDir = ' + mayaAppDir)
print ('scriptsDir = ' + scriptsDir)
print ('projectDir = ' + projectDir)
print ('userSetupFile = ' + userFile)
