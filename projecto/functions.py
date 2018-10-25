def permutation(lst, i = 0, j = 0):
	if len(lst) == 0:
		return []
	elif ((len(lst) == 1) or (i == j)):
		return lst
	else:
		temp = lst[i]
		lst[i] = lst[j]
		lst[j] = temp
		return lst


def partition(data, left , right , pivot):
	pivotValue = data[pivot]
	data = permutation(data,pivot,right)
	index = left
	for i in range(left,right - 1):
		if data[i] < pivotValue:
			data = permutation(data,index,i)
			index += 1
	data = permutation(data,right,index)
	return index

def select(data, left , right, k):