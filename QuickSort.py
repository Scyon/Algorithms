
def quickSort(array, low, high):
    
	if low >= high:
		return
		
	pivot = partition(array, low, high)
	quickSort(array, low, pivot-1)
	quickSort(array, pivot+1, high)
	return array
	
	
def partition(array, low, high):
	# set pivot to the middle index (discarding remainder)
	pivot = (low + high)//2
	# swap the pivot with the high index
	swap(array, pivot, high)
	# set i --> low index
	i = low
	# code below ensures that values higher than pivot are on the right
	# and values lower than pivor are on the left
	# iterate from low index to high index
	for j in range(low, high):
		# if the current value is less than the high index
		if array[j] <= array[high]:
			# swap i and the current index
			swap(array, i, j)
			# increment i
			i = i + 1
	# swap i with the high index to get pivot
	swap(array, i, high)
	# return pivot index
	return i
	
def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp


if __name__ == '__main__':
	a = [9, 8, 7, 6, 5, 7, 2, 3, 4, 5]
	print(a)
	print(quickSort(a, 0, len(a)-1))
