import os
import sys
import pypreg
from distutils.dir_util import copy_tree

args = sys.argv[1:]
arg = ""
for a in args:
    arg += a
    arg += " "

live = os.getcwd()

# Stackoverflow
import shutil
folder = pypreg.buildtmp
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

copy_tree(".", pypreg.buildtmp)
os.chdir(pypreg.buildtmp)

os.system(".\\.venv\\Scripts\\pyinstaller.exe main.py" + arg + " --onefile")
os.system("copy dist\\main.exe " + live)