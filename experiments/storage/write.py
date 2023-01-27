# a simple test of writing to non-volatile storage on the Pico

import machine
import os
import utime

def write(value):
    print("chdir")
    os.chdir("/")
    print("opening file")
    file = open("config.txt", "w")
    print(f'writing value "{value}"')
    file.write(value)
    print("closing file")
    file.close()
    

write("This is the string I want to write - "+str(utime.localtime()))