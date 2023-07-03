#
class Flight_statistics:
    def __init__(self, filepath, times, life, flts, nms):
        self.nsegs = 0
        self.segs = []
        self.idist = 0
        self.dists = []
        self.ilimit = 0
        self.limits = []       
        self.nps = 0
        self.itype = 0                        # 0: Statistics based on time 1: Statistics based on range
        self.vtype = 0                        # Base of the Statistics
        
        self.read_cases(filepath)
    
    def read_cases(self, filepath):
        
        with open(self.filepath, 'r') as file:
            line = file.readline()
            temp = line.split() 
            self.itype = int(temp[0])         # Statistics type
            self.vtype = int(temp[1])         # Statistics base (like 1000 hrs, 100 nm, etc)            
            
            ##############################################    # Number of load cases
            line = file.readline()
            temp = line.split() 
            self.nsegs = int(temp[0])         

            for i in range(self.ncases):
                line = file.readline()
                temp = line.split()
                self.segs.append(float(temp[i]))
            ##############################################    # Distribution based on time or input
            line = file.readline()
            temp = line.split() 
            self.idists = int(temp[0])        
           
            if self.idists == 0:
                pass
            else:
                line = file.readline()
                temp = line.split()                  
                for i in range(len(self.segs)):
                    self.dists.append(temp[i])
            #############################################    # Limitations   
            line = file.readline()
            temp = line.split() 
            self.ilimit = int(temp[0])       
           
            if self.ilimit == 0:
                for i in range(len(self.segs)):
                    self.limits.append(0)
            else:
                line = file.readline()
                temp = line.split()                  
                for i in range(len(self.segs)):
                    self.limits.append(temp[i])
                    
    
class Taxi_statistics:
    def __init__(self, filename):
        pass