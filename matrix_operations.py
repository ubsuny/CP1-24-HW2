import numpy as np

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


# Performs the transposition of an array
def get_transpose(matrix):
    """
    Retruns the transpose of the given matrix usning the numpy transpose() method

    Parameters:
    
    a : array_like
        Input array.

    axes : tuple or list of ints, optional
        If specified, it must be a tuple or list which contains a permutation of [0,1,…,N-1] where N is the number of axes of a. 
        The i’th axis of the returned array will correspond to the axis numbered axes[i] of the input. 
        If not specified, defaults to range(a.ndim)[::-1], which reverses the order of the axes.

    Returns:

    p : ndarray
        a with its axes permuted. A view is returned whenever possible.
    """
    # uses the numpy method to return the transpose of a matrix
    return np.transpose(matrix)


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
