import numpy as np
import timeit as tm


# Functions to multiply an array by a scalar and return the resulting array

# using direct multiplication with the scalar getting implicitly broadcasted
def scalarMultiplication1(arr, scalar = 0.0):
    """
    Returns the multipliction of an array by a scalar.
    Parameters:
    arr (ndarray): Input array
    Returns:
    ndarray: The result of multiplying the scalar with each element of the array
    """
    result = arr * scalar
    return result

# using a for loop
def scalarMultiplication2(arr, scalar = 0.0):
    """
    Returns the multipliction of an array by a scalar.
    Parameters:
    arr (ndarray): Input array
    Returns:
    ndarray: The result of multiplying the scalar with each element of the array
    """
    result = []
    for i in range(len(arr)):
        result.append(arr[i]*scalar)
    return result

# using np.einsum
def scalarMultiplication3(arr, scalar = 0.0):
    """
    Returns the multipliction of an array by a scalar.
    Parameters:
    arr (ndarray): Input array
    Returns:
    ndarray: The result of multiplying the scalar with each element of the array
    """
    result = np.einsum(',...', scalar, arr)
    return result

# Function to multiply two arrays and return the resulting array

# using direct multiplication after broadcasting one of the arrays for its shape to match that of the other
def arrayMultiplication1(arr1, arr2):
    """
    Returns the element-wise multipliction of two arrays.
    Parameters:
    arr1 (ndarray), arr2 (ndarray): Input arrays
    Returns:
    ndarray: An array of the elements that each of them result from multiplying an element from the first array by an element from the second array
    """

    broadcasted_arr2 = np.broadcast_to(arr1,arr2.shape)


    result = arr1 * broadcasted_arr2 # instead of arr2
    return result

# using for loops
# The issue here is that I'm not able to implement the exact functionality of the broadcasting process
def arrayMultiplication2(arr1, arr2):
    """
    Returns the element-wise multipliction of two arrays.
    Parameters:
    arr1 (ndarray), arr2 (ndarray): Input arrays
    Returns:
    ndarray: An array of the elements that each of them result from multiplying an element from the first array by an element from the second array
    """

    # broadcasted_arr2 = np.broadcast_to(arr1,arr2.shape) (no broadcasting took place)

    result = []
    for i in range(len(arr1)):
        result.append(arr1[i]*arr2) # that's normal broadcasting directly multiplying a scalar by an array, which means it can be optimized
    return result

# using np.einsum
def arrayMultiplication3(arr1, arr2):
    """
    Returns the element-wise multipliction of two arrays.
    Parameters:
    arr1 (ndarray), arr2 (ndarray): Input arrays
    Returns:
    ndarray: An array of the elements that each of them result from multiplying an element from the first array by an element from the second array
    """

    result = np.einsum(arr2, [Ellipsis], arr1, [Ellipsis])
    return result

# testing
arr1 = np.array([7, 8, 9])
arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
scalar = 6.0
# Scalar Multiplication test
print(scalarMultiplication1(arr1,scalar))
print("The best time taken to multiply the first array by the scalar is roughly: ", tm.timeit(lambda: scalarMultiplication1(arr1,scalar), number = 1000), " sec")

print(scalarMultiplication1(arr2,scalar))
print("The best time taken to multiply the second array by the scalar is roughly: ", tm.timeit(lambda: scalarMultiplication1(arr2,scalar), number = 1000), " sec")

# Array Multiplication test
print(arrayMultiplication1(arr1,arr2))
print("The best time taken to multiply the first array by the second array is roughly: ", tm.timeit(lambda: arrayMultiplication1(arr1,arr2), number = 1000), " sec")

"""
1. There's no problem with the multiplication of an array by a scalar
2. Not all the arrays can be broadcasted to match each other
"""
# TODO: An exception handling is needed to deal with the "unmatchable" scenarios