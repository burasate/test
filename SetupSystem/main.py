print('Online Script Loaded')

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
  
mayaAppDir = mel.eval('getenv MAYA_APP_DIR')
#scriptsDir = "%s%sscripts"%(mayaAppDir, os.sep)
scriptsDir = mayaAppDir+os.sep+'scripts'
userSetupFile = scriptsDir + os.sep + "userSetup.py" 

print ('mayaAppDir = '+mayaAppDir)
print ('scriptsDir = '+scriptsDir)
print ('userSetupFile = '+userSetupFile)
