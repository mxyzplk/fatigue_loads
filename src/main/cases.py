import numpy as np
#
class Cases:
    def __init__(self, filepath):
        self.ncases = 0
        self.nloads = 0
        self.cnames = []
        self.labels = []
        self.loads = None
        
        self.read_cases(filepath)
    
    def read_cases(self, filepath):
        
        with open(self.filepath, 'r') as file:
            line = file.readline()
            temp = line.split()
            self.ncases = int(temp[0])       # Number of load cases
            self.nloads = int(temp[1])       # Number of load parameters
            
            self.loads = np.empty((self.ncases, self.nloads))
            
            for i in range(self.ncases):
                line = file.readline()
                temp = line.split()
                self.cname.append(temp[0])    
                self.labels.append(temp[1])
                self.loads[i, 0:self.nloads] = float(temp[2:self.nloads+2])
            
    