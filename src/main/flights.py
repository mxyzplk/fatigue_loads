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
        self.th = []
        
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
                    self.load1.append(temp[3])
                    self.ref1.append(temp[4])
                    self.load2.append(temp[5])                    
                    self.ref2.append(temp[6])
                    self.th.append(temp[3])
                    self.th.append(temp[5])
                    
                    
    def write_flights(self, filepath):
        
        # Appeding data to result file containing the combination of flights in a block
        file = open(filepath, 'a')
        
        for i in range(int(self.np)):
            formatted_data = "{:8d}  {:12.3f}  {:8s}  {:12.3f}  {:8s}\n".format(int(self.cycles[i]), float(self.load1[i]), self.ref1[i], float(self.load2[i]), self.ref2[i])
            file.write(formatted_data)
        
        file.close()
        
        
    def write_th(self, th):
        
        for i in range(int(self.np)):
            th.append(self.th[2 * i])
            th.append(self.th[2 * i - 1])
            
        return th