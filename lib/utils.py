import os

class SimpleDirFileReader:
    def __init__(self, dir_path):
        self.filenames = os.listdir(dir_path)
        self.dir_path = dir_path

    def read(self):
        documents = []

        for filename in self.filenames:
            path = os.path.join(self.dir_path, filename)

            with open(path, "r") as f:
                data = f.read()
                documents.append(data)


        return documents



        
