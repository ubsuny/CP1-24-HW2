## Trace of a Matrix
The trace of a matrix is the sum of the diagonal elements. For a square matrix 𝐴, the trace is mathematically represented as:

$$\displaystyle{T}{r}{\left({A}\right)}={\sum_{{{i}={1}}}^{{n}}}{A}_{{{i}{i}}}$$

Where:

$\displaystyle{A}\ \text{ is an }\ {n}\times{n}\ \text{ matrix}.$
$\displaystyle{A}_{{{i}{i}}}\ \text{ refers to the diagonal elements.}$


In Einstein notation, this operation can be written as:

$$\displaystyle{T}{r}{\left({A}\right)}={A}_{{{i}{i}}}​$$


Implementations:
Methods for calculating the trace:
- Using NumPy's built-in function **numpy.trace()**.
- Using Einstein summation with **numpy.einsum()**.
