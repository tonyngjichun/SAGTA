import os

def writeTxt(gtaDict):
    for gtaName, gtaObj in gtaDict.items():
        f = open(gtaName + '_own_list.txt', 'w+')
        for fileName in gtaObj.ownList:
            f.write(fileName + '\n')
        f.close()
    
        f = open(gtaName + '_cross_check_list.txt', 'w+')
        for fileName in gtaObj.crossCheckList:
            f.write(fileName + '\n')
        f.close()