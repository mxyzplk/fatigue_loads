import signal_analysis
import numpy as np
import math

time = np.empty(1000)
th = np.empty(1000)

for t in range(1000):
    th[t] = 3 * math.sin(t) + math.exp(-2*t)

Test = signal_analysis.Th("label", th)

