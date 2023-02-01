import zipfile
import os
from MyFunctions import *
dc = get_vars()
class Zip:
    def myzip(it1, it2):
        filenames = [it1+"\\"+f for f in os.listdir(it1) if os.path.isfile(os.path.join(it1, f))] + [it2+"\\"+f for f in os.listdir(it2) if os.path.isfile(os.path.join(it2, f))]
        zip_filename=dc["PATH_ZIP_FILE"]
        with zipfile.ZipFile(zip_filename, 'w') as zip_file:
            for filename in filenames:
                zip_file.write(filename)
