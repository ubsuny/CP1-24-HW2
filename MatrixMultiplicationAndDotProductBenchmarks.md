# Matrix Multiplication and Dot Product Execution time

We compare the execution time for implementing Matrix Multiplication and Dot Product operations using different Pyhton algorithms with Einstein Summation. 
The reults thus obtained are provided in form of an exponential reltionship between execution time and matrix size ($N \times N$) as follows:

The computation time ($t$) is related to matrix size ($N$) as:

$$ t = A N^p$$

1. Matrix Multiplication using numpy.dot() function: $p = 3.0132837768634517 \pm 0.04459185897819507$;  $A = 8.156539602154813 \times 10^{-8}$


2. Matrix Multiplication using numpy.matmul() function: $p = 3.2645666900495707 \pm 0.04515499035536509$;  $A = 1.7775493484025162 \times 10^{-10}$


3. Matrix Multiplication using for loops: $p = 2.9446176592860307 \pm 0.06068289679981572$;  $A = 6.688786592447885 \times 10^{-7}$


4. Matrix Multiplication using Einstein Summation: $p = 2.8245754130387843 \pm 0.10256293864649399$;  $A = 1.1628851426155198 \times 10^{-9}$


5. Matrix Dot Product using numpy.dot() and numpy.trace() functions: $p = 1.7232033016352866 \pm 0.030687484250679593$;  $A = 1.893648329851737 \times 10^{-9}$


6. Matrix Dot Product using Einstein Summation: $p = 2.1538684855486787 \pm 0.06073369383635453$;  $A = 1.3540215797646266 \times 10^{-10}$


7. Matrix Dot Product using for loops: $p = -0.050622328426910654 \pm 0.0975347645791423;  A: 7.8932421200591 \times 10^{-8}$
(Note: for loop execution time appears nearly constant, however, it is significantly higher than the more prominent exponential algorithms in magnitude)
