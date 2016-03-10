UECM3033 Assignment #2 Report
========================================================

- Prepared by: ** OOI HUI PING**
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/OoiHp/UECM3033_assign2](https://github.com/OoiHp/UECM3033_assign2)

Explain your selection criteria here.

For an iterative method to succeed or converge, the linear system of equations needs to be diagonally dominant. This could be compute by the formula: |ai,i| > $\Sigma$ |ai,j|, for all j not equal i. Since SOR is an iterative method, the formula will be used to select SOR to solve the linear system if it is TRUE.

Explain how you implement your `task1.py` here.

For the two linear system given in this assignment will be solve by LU factorization method.
The solution for 3x3 matrix is [ 1.  1.  1.] and for the 6x6 matrix is [ 1.  -1.   4.  -3.5  7.  -1. ]
The answers are checked by A*sol, it is correct if the result of multiplication is equal to b.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (eco-pot.jpg)

![eco-pot.jpg](eco-pot.jpg)

How many non zero element in $\Sigma$?

800

Put here your lower and better resolution pictures. Explain how you generate these pictures from `task2.py`.

n=30, ![figure_2.png](figure-2.png)

n=200,  ![figure_3.png](figure-3.png)

First, each of the matrices r, g and b are decomposed into another 3 matrices $\Sigma, U$ and $V$ by $sp.linalg.svd()$. 3 new $\Sigma$ are then created from original $\Sigma$ by keeping the first n(30 and 200) none zero elements , and all other none zero elements are set to zero. The new $\Sigma$ is then convert to diagonal matrix by sp.linalg.diagsvd(), with the dimensions of 800 x 1000. New r, g, b matrices are created by $ U \Sigma_{n} V^T$, where the $\Sigma_{n}$ is the new sigma. The new r, g, b are compiled back to img to form the lower and better resolution pictures.

What is a sparse matrix?

A sparse matrix is a matrix in which most of the elements are zero.
In the assignment, the diagonalize $\Sigma$ matrix are sparse matrix with dimension 800 x 1000.

-----------------------------------

<sup>last modified: 11.03.2016</sup>