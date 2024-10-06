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

