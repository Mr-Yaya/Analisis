import random

# def permutation(lst, i = 0, j = 0):
# 	if len(lst) == 0:
# 		return []
# 	elif ((len(lst) == 1) or (i == j)):
# 		return lst
# 	else:
# 		temp = lst[i]
# 		lst[i] = lst[j]
# 		lst[j] = temp
# 		return lst


def partition(data, left , right , pivot):
	pivotValue = data[pivot]
	data[pivot], data[right] = data[right], data[pivot]
	index = left
	for i in range(left,right):
		if data[i] < pivotValue:
			data[index], data[i] = data[i], data[index]
			index += 1
	data[right], data[index] = data[index], data[right]	
	return index

def rec_select(data,k,left,right):
	if left == right:
		return data[left]
	pivot = random.randint(left,right)
	pivot = partition(data,left,right,pivot)
	if k == pivot:
		return data[k]
	elif k < pivot:
		return rec_select(data,k,left,pivot -1)
	else:
		return rec_select(data,k,pivot + 1, right)

def _select(data,k, left, right):
	while True:
		pivot = random.randint(left,right)
		newPivot = partition(data, left, right, pivot)
		pivotDist = newPivot - left
		if pivotDist == k:
			return data[newPivot]
		elif k < pivotDist:
			right = newPivot - 1
		else:
			k -= pivotDist + 1
			left = newPivot + 1

def select(data,k, left=None, right=None):
	if left is None:
		left = 0
	lv1 = len(data) - 1
	if right is None:
		right = lv1
	assert data and k >= 0
	assert 0 <= left <= lv1
	assert left <= right <= lv1
	return _select(data,k,left,right)
		