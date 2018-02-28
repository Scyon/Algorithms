
def bubbleSort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				swap(arr, j, j+1)
	return arr

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


if __name__ == '__main__':
	a = [9, 8, 7, 6, 5, 7, 2, 3, 4, 5]
	print(a)
	print(bubbleSort(a))
