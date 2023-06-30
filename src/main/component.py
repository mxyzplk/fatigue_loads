class Component:
    def __init__(self):
        self.name = None
        self.loads = []
        self.nloads = 0
        self.stations = []
        self.nstations = 0
        
        
    def read_component(self, filepath):
        # reading component data
        with open(filepath, 'r') as file:
            line = file.readline()
            temp = line.split()
            self.name = temp[0]
            
            line = file.readline()
            temp = line.split()
            self.nloads = int(temp[0])
            
            for i in range(self.nloads):
                self.loads.append(temp[i+1])
                
            line = file.readline()
            temp = line.split()
            self.nstations = int(temp[0])
            
            for i in range(self.nloads):
                self.stations.append(temp[i+1])                
            


    