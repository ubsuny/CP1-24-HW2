#Import Statements
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import time

import timeit #This one is particularly important

#Define functions used in various matrix operation methods

def generate_matrices(n):
    '''Generates two nxn matrices, E and O. E contains the first n^2 even numbers (0, 2, 4, etc...)
      ordered from least to greatest across rows and down columns and O contains the first n^2 odd numbers ordered in the same way.
      
      n = size of matrix. Input of n produces two nxn matrices.'''
    #Create an array with even numbers from 0 to 2*n^2-2
    E = np.arange(0, 2*n**2, 2).reshape(n, n) #makes an array ranging from 0 to 2n^2 in steps of 2, then reshapes into n rows on length n, making an nxn matrix.
    
    #Create an array with odd numbers from 1 to 2*n**2-1
    O = np.arange(1, 2*n**2 + 1, 2).reshape(n, n)
    
    return E, O


#Each of the next four functions depends on an input array predefined and named arr.
# Function to sum the array elements along the specified axis
def axisSummation(arr, axis=None):
    """
    Computes the sum of array elements along a specified axis.
    
    Parameters:
    arr (ndarray): The input array.
    axis (int, optional): The axis along which the summation is performed. 
                          If None, sums over the entire array.
    
    Returns:
    float or ndarray: The sum of the array elements along the specified axis.
    """
    return np.sum(arr, axis=axis)

# Define functions to time the summation for rows and columns
def sum_array():
    """
    Computes the sum of all elements in the array.
    
    Returns:
    float: The sum of all elements in the array.
    """
    return axisSummation(arr, axis=None) # Summing all elements in the array

def sum_rows():
    """
    Computes the sum of elements along each row of the array.
    
    Returns:
    ndarray: The sum of each row in the array.
    """
    return axisSummation(arr, axis=1)  # Summing along rows (axis=1)

def sum_columns():
    """
    Computes the sum of elements along each column of the array.
    
    Returns:
    ndarray: The sum of each column in the array.
    """
    return axisSummation(arr, axis=0)  # Summing along columns (axis=0)


# TODO: Implement operation 1: compute_trace()


# Implement operation 2: get_diagonal()
# Function to return the diagonal elements of an array
# TODO: unit testing and exception handling
def get_diagonal(matrix):
    """
    Returns the diagonal elements of a matrix using the numpy diagonal() method.

    Parameters:
    matrix (ndarray): Input array (2D matrix)

    Returns:
    ndarray: Diagonal elements of the matrix
    """
    # use the included np method for computing a matrix diagonal
    return np.diagonal(matrix) # could attempt to optimize this to try and beat np..


# TODO: Implement operation 2: axis_summation()
# Computes the summation along specified axes


# TODO: Implement operation 3: transpose_array()
# Performs the transposition of an array


# TODO: Implement operation 4: purmute_axes()
# Permutes the axes of an array


# TODO: Implement operation 5: matrix_multiplication() and dot_product()
# Computes matrix multiplication and dot products


# TODO: Implement operation 6: vector_inner_product() and vector_outer_product()
# Functions that compute the inner and outer product for 2 vectors


# TODO: Implement operation 7: Broadcasting, element-wise and scalar multiplication
# Implement: elementwise_multiplication() and scalar_multiplication()


# TODO: Operation 8: tensor_contraction()
# Pairs a vector space and its dual


# TODO: Implement operation 9: Chained arrays in effecient calcluation order
# Implment the chained_operations() function to efficiently compute chained operations,
# providing multiple array  objects and a specified operation (maybe start
# with a single operation)
