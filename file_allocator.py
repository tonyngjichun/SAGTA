import os
import numpy as np
from load_files import fileWalker

class GTA(object):
    def __init__(self, gtaName: str):
        self.name = gtaName
        self.ownList = []
        self.crossCheckList = []

def allocate(args):
    rawDownloadsWalker = fileWalker(args.file_path)
    rawFileNames = rawDownloadsWalker.walk()

    #Slice all raw file names evenly across n GTAs
    if args.split_evenly:
        rawFileChunks = np.array_split(np.array(rawFileNames),args.num_GTA)

    for i, gtaName in enumerate(args.GTA_names):
        #Create class:GTA object on the fly:
        vars()[gtaName] = GTA(gtaName)
        exec(gtaName+'.ownList.append(list(rawFileChunks[i]))')

