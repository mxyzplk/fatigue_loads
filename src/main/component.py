#
# Component Data contains:
#
# 1) Component name
# 2) Load Types  (e.i. BMX, SLZ, TMY, HM, FN, etc)
# 3) Load Labels (e.i. Stations, load factors, etc)
# 4) Source (loads are read from load cases files or created by transfer function)
class Component:
    def __init__(self):
        self.name = None
        self.loads = []
        self.nloads = 0
        self.stations = []
        self.nstations = 0
        self.source = []
        
        
    def read_component(self, filepath):
        # reading component data
        with open(filepath, 'r') as file:
            line = file.readline()
            temp = line.split()
            self.name = temp[0]            # Component name
            
            line = file.readline()
            temp = line.split()
            self.nloads = int(temp[0])     # Load Types
            
            for i in range(self.nloads):
                self.loads.append(temp[i+1])
                
            line = file.readline()
            temp = line.split()
            self.nstations = int(temp[0])  # Load Labels
            
            for i in range(self.nstations):
                self.stations.append(temp[i+1])


            line = file.readline()
            temp = line.split()
            
            for i in range(self.stations):   # Source 
                self.source.append(temp[i])                   
            


    