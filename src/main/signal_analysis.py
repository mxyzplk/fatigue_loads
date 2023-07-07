import rainflow
import matplotlib.pyplot as plt
import os
from tf import Tf


class Th:
    def __init__(self, label, time_history):
        self.time_history = []
        self.reduced_time_history = []
        self.range = []
        self.mean = []
        self.cycles = []
        self.peak1 = []
        self.peak2 = []
        self.label = label
        self.np = 0

        self.set_time_history(time_history)
        self.calculate_rainflow()
        self.spectra_peaks()
        self.spectra_range()
        

    def set_time_history(self, time_history):
        self.np = len(time_history)
        for i in range(self.np):
            self.time_history.append(time_history[i])
            

    def calculate_rainflow(self):
        cycles_object = rainflow.extract_cycles(self.time_history)
        for range, mean, count, i_start, i_end in cycles_object:
            self.range.append(range)
            self.mean.append(mean)
            self.cycles.append(count)
            self.reduced_time_history.append(i_start)
            self.peak1.append(float(mean) + float(range))
            self.peak2.append(float(mean) - float(range))
        self.reduced_time_history.append(i_end)
        

    def spectra_peaks(self):
        sorted_indices1 = sorted(range(len(self.peak1)), key=lambda i: self.peak1[i], reverse=True)
        sorted_indices2 = sorted(range(len(self.peak2)), key=lambda i: self.peak2[i], reverse=True)

        exceedances1 = []
        exceedances2 = []

        load1 = []
        load2 = []
        sum1 = 0
        sum2 = 0
        for i in range(len(self.peak1)):
            sum1 = sum1 + self.cycles[sorted_indices1[i]]
            sum2 = sum2 + self.cycles[sorted_indices2[i]]

            if self.range[sorted_indices1[i]] < self.range[sorted_indices2[i]]:
                break
            else:
                exceedances1.append(sum1)
                exceedances2.append(sum2)
                load1.append(self.range[sorted_indices1[i]])
                load2.append(self.range[sorted_indices2[i]])

        fig, ax = plt.subplots()
        ax.plot(exceedances1, load1, color='black')
        ax.plot(exceedances2, load2, color='black')
        ax.set_xlabel('Exceedances')
        ax.set_ylabel(self.label)
        ax.set_title('Load Exceedances - ' + self.label)
        ax.grid(color='0.8', linestyle='dashed', which='both', linewidth=0.5)
        plt.figure(figsize=(10, 6))

        folder_name = "results"
        os.makedirs("results", exist_ok=True)

        filepath = os.path.join(folder_name, 'load_exc_' + str(self.label) + '.png')

        fig.savefig(filepath, dpi=600, bbox_inches='tight')


    def spectra_range(self):
        sorted_indices = sorted(range(len(self.range)), key=lambda i: self.range[i], reverse=True)
        exceedances = []
        load1 = []
        load2 = []
        sum = 0
        for i in range(len(self.range)):
            sum = sum + self.cycles[sorted_indices[i]]
            exceedances.append(sum)
            load1.append(float(self.range[sorted_indices[i]]))
            load2.append(-1.0*float(self.range[sorted_indices[i]]))

        fig, ax = plt.subplots()
        ax.plot(exceedances, load1, color='black')
        ax.plot(exceedances, load2, color='black')
        ax.set_xlabel('Exceedances')
        ax.set_ylabel(self.label)
        ax.set_title('Amplitude Exceedances - ' + self.label)
        ax.grid(color='0.8', linestyle='dashed', which='both', linewidth=0.5)
        plt.figure(figsize=(10, 6))

        folder_name = "results"
        os.makedirs("results", exist_ok=True)

        filepath = os.path.join(folder_name, 'amplitude_exc_' + str(self.label) + '.png')

        fig.savefig(filepath, dpi=600, bbox_inches='tight', pad_inches=0.1)


