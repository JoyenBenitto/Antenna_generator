import os
import shutil

def clean_dir(directory):
    '''
    Cleans the directory recursively if the directory exists
    Args: directory -> directory to be cleaned
    '''

    # Cleaning the directory
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    else:
        pass