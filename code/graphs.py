import matplotlib.pyplot as plt
import numpy as np

""""
Code for computing a basic graph. The statistics from the 'loss versus cycle' graph is used (see in report graph 3).
The values can be changed in the variables 'Cycle' and system1/2/3.
""""

Cycle = [1, 2, 3, 4]
system1 = [0.0544625, 0.0934372, 0.0333609, 0.0531672]
system2 = [0.0840725, 0.1488623, 0.0701313, 0.0884721]
system3 = [0.0679019, 0.0388342, 0.0408674, 0.0466386]
  
plt.plot(Cycle, system1, color='grey', marker='o', label='System 1')
plt.plot(Cycle, system2, color='blue', marker='o', label = 'System 2')
plt.plot(Cycle, system3, color='green', marker='o', label = 'System 3')
plt.title('Loss versus cycle', fontsize=14)
plt.xlabel('Cycle', fontsize=14)
plt.ylabel('Loss score', fontsize=14)
plt.xticks(np.arange(min(Cycle), max(Cycle)+1, 1.0))
#plt.grid(True)
plt.legend()
plt.show()
