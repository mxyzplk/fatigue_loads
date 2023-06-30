import os
from signal_analysis import Th
import numpy as np

class Flights:
    def __init__(self, filepaths, labels, flight_types):
        self.flight_data = [Flight(filepaths[i], labels[i]) for i in range(int(flight_types))]


    def write_load_cycles(self, flts_per_block, block, logs):
        
        folder_name = "results"
        os.makedirs("results", exist_ok=True)

        filepath = os.path.join(folder_name, 'wing_fatigue_loads.txt')
        
        open(filepath, 'w').close()
        
        for i in range(flts_per_block):
            if logs == 1:
                print("Printing flight " + str(i+1) + " of 4000. Flight: " + str(block[i]))
            flt = int(block[i])-1
            self.flight_data[flt].write_flights(filepath)
            
                        
    def flights_to_th(self, flts_per_block, block, label, comp):
        
        th = []
        updated_th = th
        
        for i in range(flts_per_block):
            th = updated_th
            flt = int(block[i])-1
            updated_th = self.flight_data[flt].write_th(th, int(comp))
        
        th = Th(label, updated_th)
                    
            
class Flight:
    def __init__(self, filepath, label):
        self.np = 0
        self.filepath = filepath
        self.label = label
        self.segments = []
        self.level = []
        self.cycles = []
        self.ref = None
        self.load = None
        self.th = None
        self.npars = 0
        self.pars = []
        self.comp = None
        
        self.read_flight()


    def read_flight(self):
        i = 0
        with open(self.filepath, 'r') as file:
            for line in file:
                i = i + 1
                if i == 1:
                    temp = line.split()
                    self.np = int(temp[0])
                    self.comp = temp[1]
                    self.npars = int(temp[2])
                    self.load = np.empty(self.np, self.npars, 2) # number of lines, number of parameters, load 1 and load 2
                    self.ref = np.chararray(self.np, self.npars, 2) # number of lines, number of parameters, load 1 and load 2
                    self.th = np.empty(self.np * 2, self.npars)
                    
                    for j in range(self.npars):
                        self.pars.append(temp[2+j])
                        
                if i > 1:
                    temp = line.split()
                    # basic information
                    self.segments.append(temp[0])
                    self.level.append(temp[1])
                    self.cycles.append(temp[2])

                    for j in range(self.npars):
                        self.load[i, j, 1] = temp[3 + 4 * j]
                        self.load[i, j, 2] = temp[5 + 4 * j]
                        self.ref[i, j, 1] = temp[4 + 4 * j]
                        self.ref[i, j, 2] = temp[6 + 4 * j]                        
                        self.th[2 * i, j] = temp[3 + 4 * j]
                        self.th[2 * i - 1, j] = temp[5 + 4 * j]
                    
                    
    def write_flights(self, filepath):
        
        # Appeding data to result file containing the combination of flights in a block
        file = open(filepath, 'a')
        
        for i in range(int(self.np)):
            formatted_data = "{:8d}  {:12.3f}  {:8s}  {:12.3f}  {:8s}\n".format(int(self.cycles[i]), float(self.load1[i]), self.ref1[i], float(self.load2[i]), self.ref2[i])
            file.write(formatted_data)
        
        file.close()
        
        
    def write_th(self, th, comp):
        
        for i in range(int(self.np)):
            th.append(self.th[2 * i], int(comp))
            th.append(self.th[2 * i - 1], int(comp))
            
        return th
    
    
    def generate_sublists(lst):
        it = iter(lst)
        while True:
            sublist = [next(it), next(it)]
            yield sublist
        