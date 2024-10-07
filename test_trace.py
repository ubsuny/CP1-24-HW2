import unittest
import numpy as np

class TestTraceMethods(unittest.TestCase):
    
    # The setUp method runs before each test method. We use it to define a matrix 
    # that will be used in the test cases.
    def setUp(self):
        # A simple 3x3 matrix for testing
        self.A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Test for the Einstein summation method using np.einsum
    def test_einsum_trace(self):
        # Einsum notation 'ii' sums the diagonal elements (1 + 5 + 9 = 15)
        trace = np.einsum('ii', self.A)
        self.assertEqual(trace, 15, "Einstein summation trace did not match expected value")
    
    # Test for numpy's built-in trace method np.trace
    def test_numpy_trace(self):
        # Numpy's trace method should also give 1 + 5 + 9 = 15
        trace = np.trace(self.A)
        self.assertEqual(trace, 15, "Numpy trace did not match expected value")
    
    # Test for the manual method using a loop to calculate the trace
    def test_manual_trace(self):
        # Summing the diagonal manually using a loop should result in 15
        trace = sum(self.A[i, i] for i in range(self.A.shape[0]))
        self.assertEqual(trace, 15, "Manual trace calculation did not match expected value")

# This check ensures that the test cases only run if this file is executed directly.
# It won't run during imports (e.g., if you're using this as part of a larger test suite).
if __name__ == '__main__':
    unittest.main()