import os
def checkfile(file):
    for f in os.listdir():
        if file == f:
            return True
    return False
