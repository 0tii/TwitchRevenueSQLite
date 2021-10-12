import os

def checkPath(path):
    if os.path.exists(path):
        if os.path.exists(path+os.sep+'2019'+os.sep+'08'+os.sep+'28'+os.sep+'all_revenues.csv.gz'):
            return True
        print('\033[91mThe path is valid, however the subsequent folder structure could not be validated.\033[0m')
        return False
    print('\033[91mThe path specified does not exist.\033[0m')
    return False
