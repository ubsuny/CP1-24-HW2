import unittest
import numpy as np
from matrix_operations import get_diagonal

#TODO: Consider writing a test that times the execution of the operations
class TestNumpyDiagonalOperations(unittest.TestCase):
    """
    This class implements the unit tests for the numpy built-in diagonal-related
    matrix operations.

    In this class we test for a few different shapes of matrices, as well as the
    case of an empty matrix.

    For detailed info on how it works, check out the unittest package:
    https://docs.python.org/3/library/unittest.html
    """

    def test_get_diagonal_square_matrix(self):
        """
        Test get_diagonal on a square matrix.
        """
        # Create an arbitrary square matrix
        matrix = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

        # this is the value that we expect the function to return
        expected_output = np.array([1, 5, 9])

        # assert that the actual outcome matches the expected outcome
        np.testing.assert_array_equal(get_diagonal(matrix, False), expected_output)

    def test_get_diagonal_rectangular_matrix(self):
        """
        Test get_diagonal on a rectangular (non-square) matrix.
        """
        # Create a matrix
        matrix = np.array([[10, 20, 30],
                           [40, 50, 60]])
        # Define an execpted value
        expected_output = np.array([10, 50])

        # Assert that they are equivalent
        np.testing.assert_array_equal(get_diagonal(matrix, False), expected_output)

    def test_get_diagonal_empty_matrix(self):
        """
        Test get_diagonal on an empty matrix.
        """
        # Make an empty matrix (no elements)
        matrix = np.array([[]])

        # Create our expected output
        expected_output = np.array([])

        # Assert that they are equal
        np.testing.assert_array_equal(get_diagonal(matrix, False), expected_output)

    def test_get_diagonal_single_element_matrix(self):
        """
        Test get_diagonal on a 1x1 matrix.
        """
        # Create a matrix with a single value
        matrix = np.array([[42]])

        # Create an expectation value
        expected_output = np.array([42])

        # Assert their equality
        np.testing.assert_array_equal(get_diagonal(matrix, False), expected_output)

class TestCustomDiagonalOperations(unittest.TestCase):
    """
    This class implements the unit tests for the custom implementation of the
    diagonal-related matrix operations.

    In this class we test for a few different shapes of matrices, as well as the
    case of an empty matrix.

    For detailed info on how it works, check out the unittest package:
    https://docs.python.org/3/library/unittest.html
    """

    def test_get_diagonal_square_matrix(self):
        """
        Test get_diagonal on a square matrix.
        """
        # Create an arbitrary square matrix
        matrix = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

        # this is the value that we expect the function to return
        expected_output = np.array([1, 5, 9])

        # assert that the actual outcome matches the expected outcome
        np.testing.assert_array_equal(get_diagonal(matrix, True), expected_output)

    def test_get_diagonal_rectangular_matrix(self):
        """
        Test get_diagonal on a rectangular (non-square) matrix.
        """
        # Create a matrix
        matrix = np.array([[10, 20, 30],
                           [40, 50, 60]])
        # Define an execpted value
        expected_output = np.array([10, 50])

        # Assert that they are equivalent
        np.testing.assert_array_equal(get_diagonal(matrix, True), expected_output)

    def test_get_diagonal_empty_matrix(self):
        """
        Test get_diagonal on an empty matrix.
        """
        # Make an empty matrix (no elements)
        matrix = np.array([[]])

        # Create our expected output
        expected_output = np.array([])

        # Assert that they are equal
        np.testing.assert_array_equal(get_diagonal(matrix, True), expected_output)

    def test_get_diagonal_single_element_matrix(self):
        """
        Test get_diagonal on a 1x1 matrix.
        """
        # Create a matrix with a single value
        matrix = np.array([[42]])

        # Create an expectation value
        expected_output = np.array([42])

        # Assert their equality
        np.testing.assert_array_equal(get_diagonal(matrix, True), expected_output)


if __name__ == '__main__':          # if this file was executed directly
    unittest.main()                 # then run the unit tests defined
