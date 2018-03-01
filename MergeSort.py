
def mergeSort(array):
    
	if len(array) == 1:                                  
		return
		
	middleIndex = len(array) // 2
	# left --> up to middleIndex inclusive
	leftHalf = array[:middleIndex]
	# right --> from middleIndex non inclusive
	rightHalf = array[middleIndex:]
	
	mergeSort(leftHalf)
	mergeSort(rightHalf)
	
	i = 0
	j = 0
	k = 0
	
	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] < rightHalf[j]:
			array[k] = leftHalf[i]
			i = i + 1
		else:
			array[k] = rightHalf[j]
			j = j + 1
			
		k = k + 1
	
	# if we have items left over in left or right sub arrays
	while i < len(leftHalf):
		array[k] = leftHalf[i]
		k = k + 1
		i = i + 1

	while j < len(rightHalf):
		array[k] = rightHalf[j]
		k = k + 1
		j = j + 1

	return array	

if __name__ == '__main__':
	a = [9, 8, 7, 6, 5, 7, 2, 3, 4, 5]
	print(a)
	print(mergeSort(a))