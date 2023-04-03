from os import *
import sys
import pypreg
from distutils.dir_util import copy_tree

class clrs:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

cargoName = sys.argv[1]

print(clrs.OKGREEN + "Generating a project called " + clrs.HEADER + cargoName)
system("cls")

mkdir(cargoName)
chdir(cargoName)
print(clrs.OKGREEN + "30%")

system("echo print('Hello, world!') >> main.py")
system("cls")
print(clrs.OKGREEN + "40%")

# Copy venv
mkdir(".venv")
copy_tree(pypreg.venvtmp, ".venv")
system("cls")
print(clrs.OKGREEN + "100%, Done!")
print(clrs.ENDC)