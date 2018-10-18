import random 

arreglo = []

sizes=[64,128,256,512,1024,2048,4096,8192]#16384,32768,65536]

def initDatos():
	for curr_sizes in sizes:
		arreglo.append([random.randint(0,200000) for i in range(curr_sizes)])