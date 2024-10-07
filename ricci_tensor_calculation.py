# ricci_scalar_timing.py
import numpy as np
import opt_einsum as oe
import timeit

def calculate_ricci_scalar_numpy(g, R):
    """
    Calculate the Ricci scalar using NumPy's einsum function.
    """
    g_inv = np.linalg.inv(g)
    ricci_scalar = np.einsum('ij,ij->', g_inv, R)
    return ricci_scalar

def calculate_ricci_scalar_opt_einsum(g, R):
    """
    Calculate the Ricci scalar using Opt-Einsum with an optimized contraction path.
    """
    g_inv = np.linalg.inv(g)
    optimized_path, _ = oe.contract_path('ij,ij->', g_inv, R)
    ricci_scalar = oe.contract('ij,ij->', g_inv, R, optimize=optimized_path)
    return ricci_scalar

def compare_execution_times():
    # Define a metric tensor (4x4) representing flat spacetime (Minkowski metric)
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

if __name__ == "__main__":
    compare_execution_times()
