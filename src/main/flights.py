class Flight:
    def __init__(self, filepath, label):
        self.np = 0
        self.filepath = filepath
        self.label = label
        self.segments = []
        self.cycles = []
        self.ref1 = []
        self.ref2 = []
        self.load1 = []
        self.load2 = []


    def read_flight(self):
        i = 0
        with open(self.filepath, 'r') as file:
            for line in file:
                i = i + 1
                if i > 2:
                    temp = line.split()
                    self.segments.append(temp[0])
                    self.cycles.append(temp[1])
                    self.ref1.append(temp[3])
                    self.ref2.append(temp[5])
                    self.load1.append(temp[2])
                    self.load2.append(temp[4])
