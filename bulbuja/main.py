from datos import *
from functions import *
import time
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

initDatos()

data = arreglo

timeStamp = {}

for i in range(len(arreglo)):
	t0 = time.perf_counter()
	tri_bullbuja(data[i])
	t1 = time.perf_counter()
	timeStamp[sizes[i]] =  t1 - t0

plt.plot(sizes,timeStamp.values(),label='tiempos')
plt.xlabel('Tamanio Arreglo')
plt.ylabel('Tiempo ordenamiento')
plt.title('Ordenamiento')
plt.legend()
plt.show()

with open('timeStamp.csv','w') as f:
    w = csv.writer(f)
    w.writerows(timeStamp.items())

os.system('pause')
