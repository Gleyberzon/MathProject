import zipfile
import os
from MyFunctions import *
dc = get_vars()
class Zip:
    def myzip(it1, it2):
        """
        Name: Roman Gleyberzon
        Date: 01/02/2023
        Description: This creates zip file from 2 given folders
        Input: path to folder 1, path to folder 2
        Output: create zip file that contains folder 1 and folder 2
        """
        filenames = [it1+"\\"+f for f in os.listdir(it1) if os.path.isfile(os.path.join(it1, f))] + [it2+"\\"+f for f in os.listdir(it2) if os.path.isfile(os.path.join(it2, f))]
        zip_filename=dc["PATH_ZIP_FILE"]
        with zipfile.ZipFile(zip_filename, 'w') as zip_file:
            for filename in filenames:
                zip_file.write(filename)
