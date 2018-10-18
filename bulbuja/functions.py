def tri_bullbuja(arreglo):
	permutation = True
	passage = 0
	while permutation == True:
		permutation = False
		passage = passage + 1
		for en_cours in range(0, len(arreglo) - passage):
			if arreglo[en_cours] > arreglo[en_cours + 1]:
				permutation = True
				arreglo[en_cours], arreglo[en_cours + 1] = \
				arreglo[en_cours + 1], arreglo[en_cours]
	return arreglo			