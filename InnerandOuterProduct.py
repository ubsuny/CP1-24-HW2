#Python code for inner and outer product
#import time library to calculate time
import time
#import numpy library for scientific calculations
import numpy as np
# Define two vectors
vector_a = np.array([1, 5, 8])
vector_b = np.array([4, 9, 6])
#assign starting time
start=time.time()
# Inner product using np.dot
inner_product = np.dot(vector_a, vector_b)
outer_product = np.outer(vector_a, vector_b)
# assign ending time
end=time.time()
#print the execution time
print("execution time using numpy= ",end-start)
#print the result
print("Inner product:", inner_product)
print("Outer product:")
print(outer_product)




#Einsum Numpy
import numpy as np

# Define two vectors
vector_a = np.array([1, 5, 8])
vector_b = np.array([4, 9, 6])
#assign starting time
start=time.time()
# Calculate the inner product using np.einsum
inner_product = np.einsum('i,i->', vector_a, vector_b)

# Print the result
print("Inner Product (using np.einsum):", inner_product)

# Calculate the outer product using np.einsum
outer_product = np.einsum('i,j->ij', vector_a, vector_b)
#assign ending time
end=time.time()
#print the execution time
print("execution time using einsum= ",end-start)
# Print the result
print("Outer Product (using np.einsum):\n", outer_product)
