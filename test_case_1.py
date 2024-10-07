import numpy as np
import time

# Generate a random 500x500 matrix filled with random numbers
B = np.random.rand(500, 500)

# Method 1: Using Einstein summation notation via np.einsum
start_time = time.time()
trace_einsum = np.einsum('ii', B)
einsum_time = time.time() - start_time
print(f"Trace using Einstein notation (500x500): {trace_einsum} (Time: {einsum_time:.6f} seconds)")

# Method 2: Using numpy's built-in trace function
start_time = time.time()
trace_np = np.trace(B)
np_time = time.time() - start_time
print(f"Trace using numpy.trace (500x500): {trace_np} (Time: {np_time:.6f} seconds)")

# Method 3: Manual loop over diagonal elements
start_time = time.time()
trace_manual = sum(B[i, i] for i in range(B.shape[0]))
manual_time = time.time() - start_time
print(f"Trace using manual loop (500x500): {trace_manual} (Time: {manual_time:.6f} seconds)")