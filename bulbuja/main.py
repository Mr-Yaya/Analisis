from datos import *
from functions import *
import time
import os

initDatos()

data = arreglo

timeStamp = {}

for i in range(len(arreglo)):
	t0 = time.process_time()
	tri_bullbuja(data[i])
	t1 = time.process_time()

	timeStamp[sizes[i]] =  t1 - t0

print(timeStamp)

os.system('pause')
