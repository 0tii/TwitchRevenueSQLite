import os

def _checkFileIntegrity(path):
    for root, dirs, files in os.walk(path):
        if files:
            if len(files) > 1: #may only have 1 file per subfolder
                return False
            if not files[0].endswith('.gz'):
                return False
    return True

def checkPath(path):
    if os.path.exists(path):
        if os.path.exists(path+os.sep+'2019'+os.sep+'08'+os.sep+'28'+os.sep+'all_revenues.csv.gz'): #sample path we know has to exist
            if _checkFileIntegrity(path):
                return True
            else:
                print('\033[91mPath and folder structure were validated, but one or more files have been touched. Please restore the original untouched file structure.\033[0m') #error file(s) have been touched
                return False
        print('\033[91mThe path is valid, however the subsequent folder structure could not be validated.\033[0m')
        return False
    print('\033[91mThe path specified does not exist.\033[0m')
    return False
