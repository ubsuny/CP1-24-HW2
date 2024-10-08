# Python code for matrix transposition and permutation
# Import time library to calculate time
import time
# Import numpy library for scientific calculations
import numpy as np

# Define a matrix
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Assign starting time
start = time.time()

# Transpose of the matrix using np.transpose
transpose_matrix = np.transpose(matrix)

# Permute axes of the matrix (just as an example)
# Here, we are permuting the matrix with the same shape
# This would typically be more complex for higher dimensional arrays
permuted_matrix = np.transpose(matrix, axes=(1, 0))

# Assign ending time
end = time.time()

# Print the execution time
print("Execution time using numpy transpose and permutation: ", end-start)

# Print the results
print("Original Matrix:")
print(matrix)

print("Transposed Matrix (using np.transpose):")
print(transpose_matrix)

print("Permuted Matrix (using np.transpose with axes):")
print(permuted_matrix)

# Now using np.einsum for transposing and permuting

# Assign starting time
start = time.time()

# Transpose matrix using np.einsum (equivalent to swapping axes)
einsum_transpose = np.einsum('ij->ji', matrix)

# For permutation, einsum can perform the same operation
einsum_permuted = np.einsum('ij->ji', matrix)

# Assign ending time
end = time.time()

# Print the execution time
print("Execution time using einsum for transpose and permutation: ", end-start)

# Print the results
print("Einsum Transposed Matrix:")
print(einsum_transpose)

print("Einsum Permuted Matrix:")
print(einsum_permuted)
