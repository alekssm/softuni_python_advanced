import os
from os import path


try:
    os.remove("test.txt")
except FileNotFoundError:
    print("File already deleted!")
