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
