import os, fnmatch
import numpy as np 
import argparse

class fileWalker(object):
    def __init__(self, file_path, pdf_only=True):
        self.filePath = file_path
        self.pdf_only = pdf_only
        self.fileNames = []
        if self.pdf_only:
            print("Reading (pdf files only) from: "+self.filePath)
        else:
            print("Reading (all file types) from: "+self.filePath)
    
    def walk(self)
        listOfFiles = os.listdir(self.filePath)
        
        pattern = '*'
        if self.pdf_only:
            pattern += '.pdf'
        
        print('=='*20)
        print('Walking...')    
        for entry in self.listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                print(entry)
                self.fileNames.append(entry)
        print('=='*20)
        print("Directory walking complete. Filenames saved.")
        
        return self.fileNames