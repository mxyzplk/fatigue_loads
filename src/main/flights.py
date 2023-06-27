class Flight:
    def __init__(self, filepath, label):
        self.np = 0
        self.filepath = filepath
        self.label = label
        self.segments = []
        self.level = []
        self.cycles = []
        self.ref1 = []
        self.ref2 = []
        self.load1 = []
        self.load2 = []
        
        self.read_flight()


    def read_flight(self):
        i = 0
        with open(self.filepath, 'r') as file:
            for line in file:
                i = i + 1
                if i == 1:
                    temp = line.split()
                    self.np = int(temp[0])
                if i > 1:
                    temp = line.split()
                    self.segments.append(temp[0])
                    self.level.append(temp[1])
                    self.cycles.append(temp[2])
                    self.ref1.append(temp[3])
                    self.ref2.append(temp[4])
                    self.load1.append(temp[5])
                    self.load2.append(temp[6])
                    
                    
    def write_flights(self, filepath):
        
        file = open(filepath, 'a')
        
        for i in len(int(self.np)):
            file.write()
        
        
            
