import numpy as np
#
# This module will collect load cases data (load factors, station, forces and moments and generate a multiplying factor to the stress case)
#
# The transfer function will use data from the component and apply a polynomial
#
#


class Tf:
    def __init__(self, filepath):
        self.ntfs = 0
        self.nstations = 0
        self.tfs = None
        self.id = []

        self.read_tfs(filepath)

    def read_tfs(self, filepath):

        with open(filepath, 'r') as file:
            line = file.readline()
            temp = line.split()
            self.ntfs = int(temp[0])

            line = file.readline()
            temp = line.split()
            self.nstations = int(temp[0])

            self.tfs = np.empty((self.ntfs, self.nstations, 2))

            for i in range(self.ntfs):
                line = file.readline()
                temp = line.split()
                self.id.append(temp[0])
                for j in range(self.nstations):
                    line = file.readline()
                    temp = line.split()
                    self.tfs[i, j, 0] = float(temp[0])
                    self.tfs[i, j, 1] = float(temp[1])

    def eval_tf(self, val, case, station):

        for i in range(self.ntfs):
            if self.id[i] == case:
                res = self.tfs[i, station, 0] * val + self.tfs[i, station, 1]
                break

        return res
