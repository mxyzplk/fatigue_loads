# -*- coding: utf-8 -*-
import os
from component import Component


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
        self.config_dir = None
        self.flights_dir = None
        self.statistics_dir = None
        self.twist_dir = None
        self.flt_path = []
        self.flight_types = 0
        self.flight_time = 0
        self.flight_range = 0
        self.nblocks = 0
        self.flts_per_block = 0
        self.logs = 0
        self.component = Component()
        
        self.set_config()
        

    def get_dirs(self):
        # Get the current file's directory
        self.main_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the resources folder
        self.resources_dir = os.path.join(self.main_dir, '../resources')
        self.config_dir = os.path.join(self.resources_dir, './config')
        self.flights_dir = os.path.join(self.resources_dir, './flights')
        self.statistics_dir = os.path.join(self.resources_dir, './statistics')
        self.twist_dir = os.path.join(self.resources_dir, './twist')       
        
        print(self.main_dir)
        print(self.resources_dir)
        print(self.config_dir)
        

    def set_config(self):

        self.get_dirs()

        # Setting paths to various input files
        flt_occ_path = os.path.join(self.config_dir, 'flt_occurrence.txt')
        config_path = os.path.join(self.config_dir, 'ac_data.txt')
        flt_disp_path = os.path.join(self.config_dir, 'flt_distribution.txt')
        

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
            for i in range(int(self.flight_types)):
                line = file.readline()
                temp = line.split()
                self.flight_occ.append(temp[0])
                self.flight_filenames.append(temp[1])
                self.flight_labels.append(temp[2])
                self.flt_path.append(os.path.join(self.flights_dir, self.flight_filenames[i]))

        
        # Reading flights distribution in a block
        with open(flt_disp_path, 'r') as file:
            for i in range(self.flts_per_block):
                line = file.readline()
                temp = line.split()                
                self.block.append(temp[0])

                
                

            

            