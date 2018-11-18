import os

def writeTxt(gtaDict, save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    for gtaName, gtaObj in gtaDict.items():
        f = open(save_path + '/' + gtaName + '_own_list.txt', 'w+')
        for fileName in gtaObj.ownList:
            f.write(fileName + '\n')
        f.close()
    
        f = open(save_path + '/' + gtaName + '_cross_check_list.txt', 'w+')
        for fileName in gtaObj.crossCheckList:
            f.write(fileName + '\n')
        f.close()