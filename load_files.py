import os, re, fnmatch

class fileWalker(object):
    def __init__(self, file_path, save_path, pdf_only, imperial_id):
        self.filePath = file_path
        self.savePath = save_path
        self.pdf_only = pdf_only
        self.fileNames = []
        self.imperial_id = imperial_id

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
        with open(self.savePath + '/' + 'list_all.txt', 'w+') as f1:
            for fileName in self.fileNames:
                f1.write(fileName + '\n')
                if self.imperial_id:
                    with open(self.savePath + '/' + 'all_IDs.txt', 'w+') as f2:
                        p = re.compile('[a-z]{2,3}\d{2,5}')
                        print(p.findall(fileName)[0])
                        f2.write(p.findall(fileName)[0] + '\n')

        return self.fileNames
