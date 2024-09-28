import numpy as np
import timeit as tm


# Function to multiply an array by a scalar and return the resulting array
def scalarMultiplication(arr, scalar = 0.0):
    """
    Returns the multipliction of an array by a scalar.
    Parameters:
    arr (ndarray): Input array
    Returns:
    ndarray: The result of multiplying the scalar with each element of the array
    """
    result = arr * scalar
    return result


# Function to multiply two arrays and return the resulting array
def arrayMultiplication(arr1, arr2):
    """
    Returns the element-wise multipliction of two arrays.
    Parameters:
    arr1 (ndarray), arr2 (ndarray): Input arrays
    Returns:
    ndarray: An array of the elements that each of them result from multiplying an element from the first array by an element from the second array
    """

    # just testing
    broadcasted_arr2 = np.broadcast_to(arr1,arr2.shape)


    result = arr1 * broadcasted_arr2 # instead of arr2
    return result


# testing
arr1 = np.array([7, 8, 9])
arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
scalar = 6.0
# Scalar Multiplication test
print(scalarMultiplication(arr1,scalar))
print("The best time taken to multiply the first array by the scalar is roughly: ", tm.timeit(lambda: scalarMultiplication(arr1,scalar)), " usec")

print(scalarMultiplication(arr2,scalar))
print("The best time taken to multiply the second array by the scalar is roughly: ", tm.timeit(lambda: scalarMultiplication(arr2,scalar)), " usec")

# Array Multiplication test
print(arrayMultiplication(arr1,arr2))
print("The best time taken to multiply the first array by the second array is roughly: ", tm.timeit(lambda: arrayMultiplication(arr1,arr2)), " usec")

"""
1. There's no problem with the multiplication of an array by a scalar
2. Not all the arrays can be broadcasted to match each other
"""
# TODO: An exception handling is needed to deal with the "unmatchable" scenarios