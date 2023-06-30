import numpy as np
import os

class Flights:
    def __init__(self, filepaths):
        self.flight_data = [Flight(filepaths[i]) for i in range(len(filepaths))]
        
        
    def write_load_cycles(self, flts_per_block, block, log, sel, comp, label, load):
        
        folder_name = "results"
        os.makedirs("results", exist_ok=True)

        filepath = os.path.join(folder_name, 'load_cycles_' + str(comp) + '_' + str(load) + '_' + str(label) + '.txt')
        
        for i in range(int(flts_per_block)):
            
            if int(log) == 1:
                print('Printing Flight #' + str(i) + " Type: " + str(block[i]))
            
            self.flight_data[int(block[i])].write_flights(filepath, sel)   
            

    def flight_to_th(self, flts_per_block, block, log, sel):
        
        th = []
        
        for i in range(int(flts_per_block)):
            
            if int(log) == 1:
                print(' Setting Time history - Flight #' + str(i) + " Type: " + str(block[i]))
            
            self.flight_data[int(block[i])].write_th(th, sel)       
            
        return th


class Flight:
    def __init__(self, filepath):
        self.np = 0
        self.npars = 0
        
        self.filepath = filepath
        self.component = None
        self.segments = []
        self.level = []
        self.cycles = []
        self.pars = []

        self.load = None
        self.cases = None
        self.th = None
        
        self.read_flight()


    def read_flight(self):
        i = 0
        with open(self.filepath, 'r') as file:
            for line in file:
                i = i + 1
                if i == 1:
                    temp = line.split()
                    self.np = int(temp[0])
                    self.component = temp[1]
                    self.npars = int(temp[2])
                    
                    for j in range(self.npars):
                        self.pars.append(temp[3+j])
                    
                    self.load = np.empty((self.np, self.npars, 2)) # lines, parameters, maximum and minimum loads
                    self.cases = np.chararray((self.np, self.npars, 2)) # lines, parameters, maximum and minimum loads
                    self.th = np.empty((self.np * 2, self.npars))
                    
                if i > 1:
                    temp = line.split()
                    
                    # basic information
                    self.segments.append(temp[0])
                    self.level.append(temp[1])
                    self.cycles.append(temp[2])
                    
                    # loads
                    for j in range(self.npars):
                        self.load[i - 2, j, 0] = float(temp[3 + 4 * j])
                        self.load[i - 2, j, 1] = float(temp[5 + 4 * j])
                        self.cases[i - 2, j, 0] = temp[4 + 4 * j]
                        self.cases[i - 2, j, 1] = temp[6 + 4 * j]
                        self.th[2 * (i - 2), j] = float(temp[3 + 4 * j])
                        self.th[2 * (i - 2) - 1, j] = float(temp[5 + 4 * j])                        

                    
    
    # Data from fatigue and damage tolerance analysis                
    def write_flights(self, filepath, sel):
        
        # Appending data to result file containing the combination of flights in a block
        file = open(filepath, 'a')
        
        for i in range(int(self.np)):
            
            formatted_data = "{:8d}  {:12.3f}  {:8s}  {:12.3f}  {:8s}\n".format(int(self.cycles[i]), self.load[i, int(sel), 0], str(self.cases[i, int(sel), 0]), self.load[i, int(sel), 1], str(self.cases[i, int(sel), 1]))
            file.write(formatted_data)
        
        file.close()
        
    # Function that writes the time history from each flight into a time history comprising all blocks   
    def write_th(self, th, sel):
        
        for i in range(int(self.np)):
            th.append(self.th[2 * i], int(sel))
            th.append(self.th[2 * i - 1], int(sel))
            
        return th