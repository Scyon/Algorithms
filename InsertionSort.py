
def insertionSort(array):
	for i in range(len(array)):
		j = i
		while j > 0 and array[j-1] > array[j]:
			swap(array, j, j-1)
			j = j-1
	return array


def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp


if __name__ == '__main__':
	a = [9, 8, 7, 6, 5, 7, 2, 3, 4, 5]
	print(a)
	print(insertionSort(a))
