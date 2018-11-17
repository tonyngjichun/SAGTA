import os
import numpy as np
import inspect
from load_files import fileWalker

class GTA(object):
    def __init__(self, gtaName: str):
        self.name = gtaName
        self.ownList = []
        self.crossCheckList = []

    # legacy bit
    def getSignature(self, func):
        self.sig = inspect.signature(func)

    def assign(self, ownListNP: np.array):
        self.ownList.extend(list(ownListNP))

    def distribute(self, *others):
        nOthers = len(others)
        crossCheckChunksNP = np.array_split(np.array(self.ownList),nOthers)
        for i, each in enumerate(others):
            each.crossCheckList.extend(list(crossCheckChunksNP[i]))
    

def allocate(args):
    rawDownloadsWalker = fileWalker(args.file_path, args.pdf_only)
    rawFileNames = rawDownloadsWalker.walk()

    #Slice all raw file names evenly across n GTAs
    if args.split_evenly:
        rawFileChunks = np.array_split(np.array(rawFileNames),args.num_GTA)

    #Prepares dict of class objects:GTA
    gtaDict = {gtaName: GTA(gtaName) for gtaName in args.GTA_names}

    for i, gtaName in enumerate(args.GTA_names):
        gtaDict[gtaName].assign(rawFileChunks[i])
        gtaDict[gtaName].distribute(*[gtaDict[others] for others in args.GTA_names if others != gtaName])
        print(gtaName+'s own list:', gtaDict[gtaName].ownList)
    
    for i, gtaName in enumerate(args.GTA_names):
        print(gtaName+'s cross-check list:', gtaDict[gtaName].crossCheckList)
