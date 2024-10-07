import numpy as np
import time

# Generate a random 1000x1000 matrix filled with random numbers
A = np.random.rand(1000, 1000)

# Method 1: Using Einstein summation notation via np.einsum
# Einsum allows you to specify the summation over indices explicitly.
# 'ii' indicates summing along the diagonal, i.e., where row index = column index.
start_time = time.time()  # Start timing
trace_einsum = np.einsum('ii', A)
einsum_time = time.time() - start_time  # Calculate the time taken
print(f"Trace using Einstein notation: {trace_einsum} (Time: {einsum_time:.6f} seconds)")

# Method 2: Using numpy's built-in trace function
# Numpy provides a direct way to compute the trace of an array via np.trace.
start_time = time.time()  # Start timing
trace_np = np.trace(A)
np_time = time.time() - start_time  # Calculate the time taken
print(f"Trace using numpy.trace: {trace_np} (Time: {np_time:.6f} seconds)")

# Method 3: Manual loop over diagonal elements
# Here we manually sum the diagonal elements by iterating over the matrix.
start_time = time.time()  # Start timing
trace_manual = sum(A[i, i] for i in range(A.shape[0]))
manual_time = time.time() - start_time  # Calculate the time taken
print(f"Trace using manual loop: {trace_manual} (Time: {manual_time:.6f} seconds)")

# The output will display the trace computed by each method and the time it took to compute.
# This helps compare the efficiency of using Einstein summation, numpy's built-in function,
# and a manual method using loops.