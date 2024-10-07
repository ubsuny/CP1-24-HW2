import numpy as np

def is_square(matrix):
    """
    Accepts a 2d matrix, and returns whether or not the two dimensions have the
    same number of elements.

    Parameters:
    matrix (ndarray): Input array (2D matrix)

    Returns:
    boolean: Whether or not the matrix is square
    """
    return matrix.shape[0] == matrix.shape[1]   # check axes size

# TODO: Implement operation 1: compute_trace()


# Implement operation 2: get_diagonal()
# Function to return the diagonal elements of an array
# TODO: unit testing and exception handling
def get_diagonal(matrix, use_custom = False):
    """
    Accepts a matrix parameter as well as an optional boolean value to select
    a specific implementation of the get_diagonal(). The default behavior is to
    compute the diagonal elements of a matrix using the numpy diagonal()
    built-in method.

    Parameters:
    matrix (ndarray): Input array (2D matrix)
    use_custom (boolean): Selects if the custom implementation should be used.

    Returns:
    ndarray: Diagonal elements of the matrix
    """
    if use_custom == True:                              # if True was passed,
        diagonal = get_diagonal_custom(matrix)          # use the custom method
    else:                                               # otherwise,
        diagonal = get_diagonal_numpy(matrix)   # use the one in numpy

    return diagonal                                     # send it home

def get_diagonal_custom(matrix):
    """
    Returns the diagonal elements of a matrix using the numpy diagonal() method.

    Currently limited to 2-dimensional arrays.

    Parameters:
    matrix (ndarray): Input array (2D matrix)

    Returns:
    ndarray: Diagonal elements of the matrix
    """
    print("get_diagonal_custom() invoked.")     # announce the routine

    if is_square(matrix):                       # if the matrix is square
        size = matrix.shape[0]                  # get the matrix size
        indices = np.arange(size)              # make a list of indices
        diagonal = matrix[indices, indices]     # extract the diagonal

    else:                                       # otherwise
        n0 = matrix.shape[0]                    # get the size of 0th dim
        n1 = matrix.shape[1]                    # get the size of 1st dim
        min_size = min(n0, n1)                  # get the smaller of the two

        indices = np.arange(min_size)          # set the diagonal indices
        diagonal = matrix[indices, indices]     # extract the diagonal

    print("Diagonal elements (as numpy array):", diagonal)
    return diagonal

def get_diagonal_numpy(matrix):
    """
    Returns the diagonal elements of a matrix using the numpy diagonal() method.

    Parameters:
    matrix (ndarray): Input array (2D matrix)

    Returns:
    ndarray: Diagonal elements of the matrix
    """
    print("get_diagonal_numpy() invoked.")
    # use the included np method for computing a matrix diagonal
    return np.diagonal(matrix)

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
