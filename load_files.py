import os, fnmatch

class fileWalker(object):
    def __init__(self, file_path, save_path, pdf_only):
        self.filePath = file_path
        self.savePath = save_path
        self.pdf_only = pdf_only
        self.fileNames = []
        if self.pdf_only:
            print("Reading (pdf files only) from: "+self.filePath)
        else:
            print("Reading (all file types) from: "+self.filePath)
    
    def walk(self):
        listOfFiles = os.listdir(self.filePath)
        pattern = '*'
        if self.pdf_only:
            pattern += '.pdf'
        
        print('=='*40)
        print('Walking...')    
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                print('Entry: '+entry)
                self.fileNames.append(entry)
                
        print('=='*40)
        print("Directory walking complete. Filenames saved.")
        
        if not os.path.exists(self.savePath):
            os.mkdir(self.savePath)

        self.fileNames.sort()
        f = open(self.savePath + '/' + 'list_all.txt', 'w+')
        for fileName in self.fileNames:
            f.write(fileName + '\n')
        f.close()

        return self.fileNames 