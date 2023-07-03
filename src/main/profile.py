#
class Profile:
    def __init__(self, filepath):
        self.nsegs = 0
        self.stype = []      # 0: Events    1: Segments
        self.id = []
        self.time = []
        self.name = []
        
        self.read_profile(filepath)
        
    def read_profile(self, filepath):
        
        with open(self.filepath, 'r') as file:
            line = file.readline()
            temp = line.split()
            self.nsegs = int(temp[0])
            
            for i in range(self.nsegs):
                line = file.readline()
                temp = line.split()
                self.stype.append(temp[0])
                self.id.append(temp[1])
                self.time.append(temp[2])
                self.name  .append(temp[3])
               
                
    