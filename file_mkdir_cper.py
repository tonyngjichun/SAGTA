import os
import shutil

def writeTxt(gtaDict, save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    for gtaName, gtaObj in gtaDict.items():
        eachSavePath = save_path + '/' + gtaName
        if not os.path.exists(eachSavePath):
            os.mkdir(eachSavePath)

        f = open(eachSavePath + '/' + gtaName + '_own_list.txt', 'w+')
        gtaObj.ownList.sort()
        for fileName in gtaObj.ownList:
            f.write(fileName + '\n')
        f.close()
    
        f = open(eachSavePath + '/' + gtaName + '_cross_check_list.txt', 'w+')
        gtaObj.crossCheckList.sort()
        for fileName in gtaObj.crossCheckList:
            f.write(fileName + '\n')
        f.close()

def copyFiles(gtaDict, file_path, save_path):
    for gtaName, gtaObj in gtaDict.items():
        eachOwnPath = save_path + '/' + gtaName + '/own'
        if not os.path.exists(eachOwnPath):
            os.mkdir(eachOwnPath)
     
        for fileName in gtaObj.ownList:  
            shutil.copy2(file_path + '/' + fileName, eachOwnPath)
  
        eachCrossCheckPath = save_path + '/' + gtaName + '/cross_check'
        if not os.path.exists(eachCrossCheckPath):
            os.mkdir(eachCrossCheckPath)
