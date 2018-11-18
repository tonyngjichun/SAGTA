import os
import numpy as np
import inspect
from random import shuffle
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

    def distribute(self, others):
        #others = list(others)
        nOthers = len(others)
        crossCheckChunksNP = np.array_split(np.array(self.ownList),nOthers)
        for i, each in enumerate(others):
            each.crossCheckList.extend(list(crossCheckChunksNP[i]))


def allocate(args):
    rawDownloadsWalker = fileWalker(args.file_path, args.save_path, args.pdf_only)
    rawFileNames = rawDownloadsWalker.walk()
    shuffle(rawFileNames)

    # slice all raw file names evenly across n GTAs
    if args.split_evenly:
        rawFileChunks = np.array_split(np.array(rawFileNames),args.num_GTA)

    # prepares dict of class objects:GTA
    gtaDict = {gtaName: GTA(gtaName) for gtaName in args.GTA_names}

    for i, gtaName in enumerate(args.GTA_names):
        gtaDict[gtaName].assign(rawFileChunks[i])

        # for evenly spreading cross check list, queue = 'others'
        if 'others' not in locals():
            others = [gtaDict[name] for name in args.GTA_names if name != gtaName]
        else:
            others[others.index(gtaDict[gtaName])] = gtaDict[insertNameNext]
        
        gtaDict[gtaName].distribute(others)

        # for next iteration
        insertNameNext = gtaName # insert name back into queue
        others.append(others.pop(0)) # shift queue by one index
    
    return gtaDict