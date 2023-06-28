# -*- coding: utf-8 -*-
import os
from flights import Flight
from signal_analysis import Th


class Config:
    def __init__(self):
        self.flight_names = []
        self.flight_labels = []
        self.flight_filenames = []
        self.flight_occ = []
        self.life_cycles = []
        self.block = []
        self.nflights = 0
        self.resources_dir = None
        self.main_dir = None
        self.flight_types = 0
        self.flight_time = 0
        self.flight_range = 0
        self.flight_data = None
        self.nblocks = 0
        self.flts_per_block = 0
        self.logs = 0
        
        self.set_config()

    def get_dirs(self):
        # Get the current file's directory
        self.main_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the resources folder
        self.resources_dir = os.path.join(self.main_dir, '../resources')

    def set_config(self):

        self.get_dirs()

        # Setting paths to various input files
        flt_occ_path = os.path.join(self.resources_dir, 'flt_occurrence.txt')
        config_path = os.path.join(self.resources_dir, 'ac_data.txt')
        flt_disp_path = os.path.join(self.resources_dir, 'flt_distribution.txt')
        

        # Reading config file
        with open(config_path, 'r') as file:
            line = file.readline()
            temp = line.split()
            self.nflights = int(temp[0])       # Number of Flights in Life

            line = file.readline()
            temp = line.split()
            self.flight_time = int(temp[0])    # Flight time in minutes

            line = file.readline()
            temp = line.split()
            self.flight_range = int(temp[0])   # Flight range in nm
            

            line = file.readline()
            temp = line.split()
            self.nblocks = int(temp[0])        # Number of blocks
     

            line = file.readline()
            temp = line.split()
            self.flts_per_block = int(temp[0]) # Flights per block  


            line = file.readline()
            temp = line.split()
            self.flight_types = int(temp[0])   # flight Types
            

            line = file.readline()
            temp = line.split()
            self.logs = int(temp[0])          # logs           
            

        # Reading flight occurrences
        with open(flt_occ_path, 'r') as file:
            file_path = []
            for i in range(int(self.flight_types)):
                line = file.readline()
                temp = line.split()
                self.flight_occ.append(temp[0])
                self.flight_filenames.append(temp[1])
                self.flight_labels.append(temp[2])
                file_path.append(os.path.join(self.resources_dir, self.flight_filenames[i]))

        # Initializing Flight array
        self.flight_data = [Flight(file_path[i], self.flight_labels[i]) for i in range(int(self.flight_types))]
        
        # Reading flights distribution in a block
        with open(flt_disp_path, 'r') as file:
            for i in range(self.flts_per_block):
                line = file.readline()
                temp = line.split()                
                self.block.append(temp[0])
                
                
    def write_load_cycles(self):
        
        folder_name = "results"
        os.makedirs("results", exist_ok=True)

        filepath = os.path.join(folder_name, 'wing_fatigue_loads.txt')
        
        open(filepath, 'w').close()
        
        for i in range(self.flts_per_block):
            if self.logs == 1:
                print("Printing flight " + str(i+1) + " of 4000. Flight: " + str(self.block[i]))
            flt = int(self.block[i])-1
            self.flight_data[flt].write_flights(filepath)
            
            
    def flights_to_th(self):
        
        th = []
        updated_th = th
        
        for i in range(self.flts_per_block):
            th = updated_th
            flt = int(self.block[i])-1
            updated_th = self.flight_data[flt].write_th(th)
        
        th = Th("teste", updated_th)
        
            