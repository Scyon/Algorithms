
def selectionSort(array):
	for i in range(len(array)-1):
		index = i
		for j in range(i+1, len(array)):
			if array[j] < array[index]:
				index = j
		if index != i:
			swap(array, index, i)
	return array

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp


if __name__ == '__main__':
	a = [9, 8, 7, 6, 5, 7, 2, 3, 4, 5]
	print(a)
	print(selectionSort(a))
