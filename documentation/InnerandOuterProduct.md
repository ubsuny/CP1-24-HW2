# Documentation
## Inner Product:
For two vectors $\vec{a}$ and $\vec{b}$ in n-dimensional space, the inner product is defined as :
$\vec{a} \cdot \vec{b}=\sum_{i=1}^n a_i b_i$

In Einstein's notation, this can be written as:
$\vec{a} \cdot \vec{b}= a_i b^i$

Expanded Form:  
$C = \vec{a} \cdot \vec{b} = a_i b^i = a_1 b^1 + a_2 b^2 + \dots + a_n b^n$

## Outer Product: 
For two vectors $\vec{u}$ and $\vec{v}$, 

$$
\mathbf{u} = \begin{pmatrix} 
u_1 \\ 
u_2 \\ 
\vdots \\ 
u_m 
\end{pmatrix}, \quad
\mathbf{v} = \begin{pmatrix} 
v_1 \\ 
v_2 \\ 
\vdots \\ 
v_n 
\end{pmatrix}, \quad
\mathbf{v}^T = \begin{pmatrix} 
v_1 & v_2 & \cdots & v_n 
\end{pmatrix}
$$

the outer product results in a matrix:

$$\mathbf{u} \otimes \mathbf{v} = \begin{pmatrix} 
u_1 \\ 
u_2 \\ 
\vdots \\ 
u_m 
\end{pmatrix} \quad \begin{pmatrix} 
v_1 & v_2 & \cdots & v_n 
\end{pmatrix}$$


$$ =
\begin{pmatrix}
u_1 v_1 & u_1 v_2 & \cdots & u_1 v_n \\
u_2 v_1 & u_2 v_2 & \cdots & u_2 v_n \\
\vdots   & \vdots   & \ddots & \vdots \\
u_m v_1 & u_m v_2 & \cdots & u_m v_n
\end{pmatrix}
$$


In Einstein's notation, this can be written as:

$$\left( \vec{a} \otimes \vec{b} \right)_{ij} = a_i b_j$$
