#function that returns the maximum sum of products of two arrays
#by multiplying each number in one array by one number in the other
def largest_dot_product(arr1, arr2) : 

	# Variable to store the sum of 
	# products of array elements 
	sop = 0

	# finding the length of the arrays 
	arr_len = len(arr1) 

	# Sorting the elements of both the arrays 
	arr1.sort() 
	arr2.sort() 

	# Iterating through the arrays 
	# and calculating sum of product 
	for i in range(arr_len) : 
		sop += arr1[i] * arr2[i]
	return sop 

# Main driver code and passing array values
if __name__ == "__main__" : 

	A = [1, 2, 3] 
	B = [4, 5, 1]
	print('largest_dot_product',A,B)
	print(largest_dot_product(A, B)) 

