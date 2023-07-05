import numpy as np
import math
from scipy.interpolate import interp1d

#
#  Maneuver and Gust Statistic 
#  
class Flight_statistics:
    def __init__(self, filepath, seg_times, airborne_time, multiplier, twistpath, nblocks):
        self.nsegs = 0
        self.segs = []
        self.idist = 0
        self.dists = []
        self.ilimit = 0
        self.limits = []       
        self.nps = 0
        self.sfactor = 0                        # Base of the Statistics
        self.airborne_time = float(airborne_time)
        self.seg_time = []
        self.inclf = 0
        self.meanlf = 0
        self.statistics = None
        self.levels = np.empty((10, 2))
        
        self.read_cases(filepath, seg_times, multiplier)
        self.discrete = Twist(twistpath, nblocks)
        self.get_discrete_load_levels(self.discrete.exc)
        
    
    def read_cases(self, filepath, times, multiplier):
        
        with open(filepath, 'r') as file:
            line = file.readline()
            temp = line.split() 
            self.inclf = float(temp[0])           # Maximum value (e.i. limit maneuvering load factor, limit gust, etc)
            self.meanlf = float(temp[1])
            
            line = file.readline()
            temp = line.split()
            self.sfactor = int(temp[0])         # Statistics base (like 1000 hrs, 100 nm, etc)            
            
            ##############################################    
            line = file.readline()
            temp = line.split() 
            self.nsegs = int(temp[0])           # Number of segments

            line = file.readline()
            temp = line.split()
            for i in range(self.nsegs):         # Segments Ids
                self.segs.append(float(temp[i]))
                self.seg_time.append(times[int(temp[i])])
                
            line = file.readline()
            temp = line.split()     
            for i in range(self.nsegs):          # Load factors Limitations
                self.limits.append(0)            
           
            ##############################################    # Distribution based on time or input
            line = file.readline()
            temp = line.split() 
            self.idists = int(temp[0])        
           
            if self.idists == 0:
                for i in range(self.nsegs):
                    self.dists.append(float(self.seg_time[i]) / float(self.airborne_time))
            else:
                line = file.readline()
                temp = line.split()                  
                for i in range(self.nsegs):
                    self.dists.append(temp[i])

            ############################################   # Statistics
            line = file.readline()
            temp = line.split() 
            self.nps = int(temp[0])
            self.statistics = np.empty((self.nps, 6))       # Upper LF, Exc, Lower LF, Exc
            
            for i in range(self.nps):
                line = file.readline()
                temp = line.split()
                self.statistics[i, 0] = float(self.meanlf) + float(temp[0]) * float(self.inclf)
                self.statistics[i, 1] = float(temp[1]) * float(self.sfactor) * float(multiplier)
                self.statistics[i, 2] = math.log10(float(temp[1]) * float(multiplier))
                self.statistics[i, 3] = float(self.meanlf) + float(temp[2]) * float(self.inclf)
                self.statistics[i, 4] = float(temp[3]) * float(self.sfactor) * float(multiplier)
                self.statistics[i, 5] = math.log10(float(self.sfactor) * float(temp[3]) * float(multiplier))                 


    def get_discrete_load_levels(self, exc):
        
        # Input Exceedances in life per load level
        for i in range(10):
            f1 = interp1d(self.statistics[:, 2], self.statistics[:, 0], fill_value='extrapolate')
            f2 = interp1d(self.statistics[:, 5], self.statistics[:, 3], fill_value='extrapolate')
            self.levels[i, 0] = f1(math.log10(exc[i]))
            self.levels[i, 1] = f2(math.log10(exc[i]))

                    
#
#  Taxi Statistic
#   
class Taxi_statistics:
    def __init__(self, filepath):
        pass
    
    
#
#  Landing Statistic
#       
class Landing_statistics:
    def __init__(self, filepath):
        pass
    
#
#  TWIST Table which contains the occurrences per flight levels
#    
class Twist:
    def __init__(self, filepath, nblocks):
        self.nlvls = 0
        self.twist = None
        self.sum_occ = None
        self.exc = None
        self.discrete = None
        self.read_cases(filepath)
        self.nblocks = nblocks
        
        
    def read_cases(self, filepath):
        with open(filepath, 'r') as file:
            line = file.readline()
            temp = line.split() 
            self.nlvls = int(temp[0])
            self.twist = np.empty((10, self.nlvls))  # 10 Flights , N Levels
            self.sum_occ = np.empty(10)
            self.exc = np.empty(10)
            
            for i in range(10):
                line = file.readline()
                temp = line.split()
                for j in range(self.nlvls):
                    self.twist[i, j] = int(temp[j])

            line = file.readline()
            temp = line.split()
            for i in range(self.nlvls):
                self.sum_occ[i] = int(temp[i])  
                
            line = file.readline()
            temp = line.split()
            for i in range(self.nlvls):
                self.exc[i] = int(temp[i])                  