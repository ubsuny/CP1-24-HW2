import numpy as np
import time

# Generate a random 5x5 matrix with values between 0 and 25
np.random.seed(0) 
A = np.random.randint(0, 26, size=(5, 5))

# Function to time trace calculation
def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time, result

# Test and time standard trace calculation using numpy.trace()
trace_time, trace_result = time_function(np.trace, A)

# Test and time trace calculation using Einstein summation with numpy.einsum()
einsum_trace_time, einsum_trace_result = time_function(np.einsum, 'ii->', A)

# Print the matrix and the results
print("Matrix A:")
print(A)

print("\nTrace Calculation Results:")
print(f"Standard Trace (np.trace): {trace_result}, Time: {trace_time:.10f} seconds")
print(f"Einstein Summation Trace (np.einsum): {einsum_trace_result}, Time: {einsum_trace_time:.10f} seconds")
