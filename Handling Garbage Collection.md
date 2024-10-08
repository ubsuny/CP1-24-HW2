# Garbage Collection

Garbage collection is a performance optimization technique used in Python. Specifically, it identifies objects that are not in use and deletes them from memory. 

## Reclaiming memory and how it affects our project

Garbage collection "reclaims" memory taken up by objects that are no longer in use. It doesn't run continuously but is activated when certain criteria are met.

This directly affects our project since we're timing how long certain matrix operations take to run. If we are running our matrix operations in a loop and calculating their run time, as is often the case, then garbage collection will occasionally run during instances of the loop, increasing the calculation time for that instance.


## Mitigating the impact (Solutions)
There are several methods we may implement to mitigate the impact of garbage collection. 

1. Disabling garbage collection 
- We can disable garbage collection entirely during the runtime of our operations using something like
```Python
import gc

gc.disable()  #Disables automatic garbage collection
#Run the matrix operation
gc.enable()  #Reenables automatic garbage collection
```
- This will ensure that garbage collection has no impact on time calculations. Keep in mind that this may lead to inefficient code. Since garbage collection is used for memory optimization, disabling it can slow the code down dramatically. This is especially true if we are doing the matrix operation many times. 

2. Using timeit
- We can, instead of simply timing one run of the matrix operation, time multiple runs using timeit.timeit and average the output. This is precisely what we do in Array-axis-summations/Array Axis Summation.ipynb

```Python
for n in range(1, N):
    E, O = generate_matrices(n)
    
    #Use timeit to time the matrix multiplication
    t_n_rows = timeit.timeit(lambda: axis_summation(E,1), number=500) / 500  # Averaging over 500 runs
    t_n_columns = timeit.timeit(lambda: axis_summation(E,0), number = 50) / 50 
 
    #Append the calculation time to the list
    t_N_rows.append(t_n_rows)
    t_N_columns.append(t_n_columns)
```

- Here, we see that we time the calculation for the sum of the rows 500 times and the sum of the columns 50 times before appending the times to their respective arrays. This limits the impact of the garbage collection since the instances in which garbage collection is run are simply outliers in a large, averaged, set.
