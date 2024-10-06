# Ricci Scalar Calculation Using Tensor Contractions

## Overview

The Ricci scalar is a key quantity in General Relativity, representing the average curvature of spacetime. It is derived from the Ricci tensor by contracting it with the inverse metric tensor in General Relativity.

## Mathematical Explanation

1. The Ricci tensor is obtained by contracting the Riemann curvature tensor:

   $$
   R_{\mu \nu} = R^\lambda_{\mu \lambda \nu}
   $$

3. **Ricci Scalar Calculation:**
   The Ricci scalar is computed by contracting the Ricci tensor with the inverse metric tensor:

   $$
   R = g^{\mu \nu} R_{\mu \nu}
   $$

### Comparison of Execution Times for Ricci Scalar Calculation and the Explanation of code which compares the execution time of two different methods for calculating the Ricci scalar using tensor contraction in Python.

#### Overview

This document compares the execution times of two different methods for calculating the Ricci scalar using tensor contractions in Python. This comparison highlights the performance benefits of using optimized contraction paths for tensor calculations.

#### Methods Compared

##### 1. **NumPy's `einsum` Function**

- **Description**: `einsum` is a function that performs tensor contractions using Einstein summation notation. A direct implemenatation of einsum specifying how indices are summed results in a contraction between the inverse metric and the Ricci Tensor.
- **Advantages**:
  - Simple and direct implementation of tensor contractions.
  - Widely used in scientific computing due to its readability and ease of use.
- **Limitations**:
  - Not optimized for performance; may not find the most efficient path for complex or large-scale contractions like, calculating the Reimann Curvature Tensor, which can lead to slower execution times.

##### 2. **Opt-Einsum**

- **Description**: An optimized version of `einsum` which finds the most efficient contraction path for tensor operations. It works on the order of operations to provide the most efficient output.
- **Advantages**:
  - It finds the optimal contraction path, which reduces the number of operations.
  - Complex contractions are easily done with opt einsum.
- **Limitations**:
  - It is slightly more complex due to additional steps for path optimization.

#### Performance Comparison

##### **Setup**

- Both methods were tested on a sample metric tensor which represents a flat spacetime metric and a Ricci tensor is calculated.
- The execution times were measured using Python’s `timeit` module over 1000 iterations for each method.

##### **Findings**

- **Performance Gain**: Opt-Einsum showed faster execution times compared to NumPy's `einsum`.
- **Efficiency**: Path optimization is extremeley important in tensor contractions to increase the running efficiency.
- **Impact on Large-Scale Computations**: For larger tensors or more complex tensor operations, the performance benefits of Opt-Einsum are even more pronounced, making it a preferred choice for high-performance computing tasks.

##### **Conclusion**

The comparison of execution times between NumPy's `einsum` and Opt-Einsum highlights the crucial role of optimization in tensor calculations. While NumPy’s `einsum` provides a straightforward approach, Opt-Einsum’s ability to determine and use the most efficient contraction path offers substantial performance improvements. This is particularly valuable in fields like physics, machine learning, and other areas requiring large-scale tensor computations.

Opt-Einsum's optimizations can lead to faster calculations and reduced computational resources, making it an essential tool for anyone working with tensor contractions in scientific computing.

###### **Explanation of code**

import numpy as np
import opt_einsum as oe
import timeit

The above are the neccessary libraries and packagaes. numpy is a fundamental package for numerical computing in Python. The contraction and taking inverse of tensors are being done using numpy. opt_einsum is an optimized version of numpy.einsum, used to perform Einstein summation with improved performance, especially on larger tensors. And timeit is a Python module that measures the execution time. This is used here to compare the execution time of both methods of calculating Ricci scalar.


def calculate_ricci_scalar_numpy(g, R):
    Calculate the Ricci scalar using NumPy's einsum function.
    
    Parameters:
    - g: Metric tensor (numpy array).
    - R: Ricci tensor (numpy array).

    g_inv = np.linalg.inv(g)
    ricci_scalar = np.einsum('ij,ij->', g_inv, R)
    return ricci_scalar

Starting from the beginning I give two inputs; the metric tensor 'g' and the Ricci Tensor 'R'. The inverse of the metric tensor is calculated first using np.linalg.inv(). 
np.einsum() is used to perform tensor contraction using Einstein notation. The function returns the Ricci scalar. 

def calculate_ricci_scalar_opt_einsum(g, R):

    Calculate the Ricci scalar using Opt-Einsum with an optimized contraction path.
    optimized_path, _ = oe.contract_path('ij,ij->', g_inv, R)
    ricci_scalar = oe.contract('ij,ij->', g_inv, R, optimize=optimized_path)
    return ricci_scalar

This return function is the same, the difference is the way we are calculating the Ricci scalar. This function opt_einsum.contract_path() calculates the Ricci scalar using the inverse of the metric tensor g and the Ricci tensor R. This is really beneficial for large tensors, as it looks for the most efficient path of calculating the Ricci scalar as it involves contraction with metric tensor. The optimized_path parameter in oe.contract() tells Opt-Einsum to use the optimized path found earlier,to speed up the computation process and returns the Ricci scalar with the more optimized version.

Now that we have calculated the Ricci scalar via two methods, let us compare them.

def compare_execution_times():
    
    #Define a metric tensor (4x4) representing flat spacetime (Minkowski metric)
    g = np.array([[1, 0, 0, 0],
                  [0, -1, 0, 0],
                  [0, 0, -1, 0],
                  [0, 0, 0, -1]])

    # Define a hypothetical Ricci tensor (4x4) with arbitrary values for demonstration
    R = np.array([[1, 0.1, 0.2, 0.3],
                  [0.1, 0.5, 0.1, 0.2],
                  [0.2, 0.1, 0.4, 0.1],
                  [0.3, 0.2, 0.1, 0.3]])

    # Timing NumPy's einsum implementation
    numpy_time = timeit.timeit(lambda: calculate_ricci_scalar_numpy(g, R), number=1000)
    print(f"Execution time using NumPy einsum: {numpy_time:.6f} seconds for 1000 iterations.")

    # Timing Opt-Einsum implementation
    opt_einsum_time = timeit.timeit(lambda: calculate_ricci_scalar_opt_einsum(g, R), number=1000)
    print(f"Execution time using Opt-Einsum: {opt_einsum_time:.6f} seconds for 1000 iterations.")

    # Comparison of execution times
    if numpy_time > opt_einsum_time:
        print(f"Opt-Einsum is faster by {(numpy_time - opt_einsum_time):.6f} seconds.")
    else:
        print(f"NumPy einsum is faster by {(opt_einsum_time - numpy_time):.6f} seconds.")

Define Metric Tensor (flat spacetime metric) and Ricci tensor (with arbitraty values). The timeit() function is used to measure the execution time of the two methods over 1000 iterations. NumPy einsum Time measures how long it takes to calculate the Ricci scalar using np.einsum(). Opt-Einsum Time measures the time taken using opt_einsum with the optimized contraction path. The code compares the execution times of the two methods and prints which one is faster.

if __name__ == "__main__":
    compare_execution_times()

This ensures that the compare_execution_times() function runs only when the script is executed directly.

#### References

- [NumPy Documentation](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Opt-Einsum Documentation](https://optimized-einsum.readthedocs.io/en/stable/)


