# attempt to read the value written by write.py
# run this program after a hard reset

import machine
import os

def read():
    os.chdir("/")
    file = open("config.txt")
    result = file.read()
    file.close()
    return result

print(read())
