## MATRICES

## The essence of Mathematics lies in its freedom. - CANTOR

### 3.1 Introduction

The knowledge of matrices is necessary in various branches of mathematics. Matrices are one of the most powerful tools in mathematics. This mathematical tool simplifies our work to a great extent when compared with other straight forward methods. The evolution of concept of matrices is the result of an attempt to obtain compact and simple methods of solving system of linear equations. Matrices are not only used as a representation of the coefficients in system of linear equations, but utility of matrices far exceeds that use. Matrix notation and operations are used in electronic spreadsheet programs for personal computer, which in turn is used in different areas of business and science like budgeting, sales projection, cost estimation, analysing the results of an experiment etc. Also, many physical operations such as magnification, rotation and reflection through a plane can be represented mathematically by matrices. Matrices are also used in cryptography. This mathematical tool is not only used in certain branches of sciences, but also in genetics, economics, sociology, modern psychology and industrial management.

In this chapter, we shall find it interesting to become acquainted with the fundamentals of matrix and matrix algebra.

### 3.2 Matrix

Suppose we wish to express the information that Radha has 15 notebooks. We may express it as [15] with the understanding that the number inside [ ] is the number of notebooks that Radha has. Now, if we have to express that Radha has 15 notebooks and 6 pens. We may express it as [15 6 ] with the understanding that first number inside [ ] is the number of notebooks while the other one is the number of pens possessed by Radha. Let us now suppose that we wish to express the information of possession
of notebooks and pens by Radha and her two friends Fauzia and Simran which is as follows:

| Radha | has | 15 | notebooks | and | 6 pens, |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fauzia | has | 10 | notebooks | and | 2 pens, |
| Simran | has | 13 | notebooks | and | 5 pens. |

Now this could be arranged in the tabular form as follows:

|  | Notebooks | Pens |
| :--- | :---: | :---: |
| Radha | 15 | 6 |
| Fauzia | 10 | 2 |
| Simran | 13 | 5 |

and this can be expressed as
![](https://cdn.mathpix.com/cropped/2025_07_21_a374a9ab152c8b061e73g-02.jpg?height=396&width=623&top_left_y=957&top_left_x=535)
or

|  | Radha | Fauzia | Simran |
| :--- | :---: | :---: | :---: |
| Notebooks | 15 | 10 | 13 |
| Pens | 6 | 2 | 5 |

which can be expressed as:
![](https://cdn.mathpix.com/cropped/2025_07_21_a374a9ab152c8b061e73g-02.jpg?height=300&width=780&top_left_y=1673&top_left_x=454)

In the first arrangement the entries in the first column represent the number of note books possessed by Radha, Fauzia and Simran, respectively and the entries in the second column represent the number of pens possessed by Radha, Fauzia and Simran,
respectively. Similarly, in the second arrangement, the entries in the first row represent the number of notebooks possessed by Radha, Fauzia and Simran, respectively. The entries in the second row represent the number of pens possessed by Radha, Fauzia and Simran, respectively. An arrangement or display of the above kind is called a matrix. Formally, we define matrix as:
Definition 1 A matrix is an ordered rectangular array of numbers or functions. The numbers or functions are called the elements or the entries of the matrix.

We denote matrices by capital letters. The following are some examples of matrices:

$$
\mathrm{A}=\left[\begin{array}{cc}
-2 & 5 \\
0 & \sqrt{5} \\
3 & 6
\end{array}\right], \mathrm{B}=\left[\begin{array}{ccc}
2+i & 3 & -\frac{1}{2} \\
3.5 & -1 & 2 \\
\sqrt{3} & 5 & \frac{5}{7}
\end{array}\right], \mathrm{C}=\left[\begin{array}{ccc}
1+x & x^{3} & 3 \\
\cos x & \sin x+2 & \tan x
\end{array}\right]
$$

In the above examples, the horizontal lines of elements are said to constitute, rows of the matrix and the vertical lines of elements are said to constitute, columns of the matrix. Thus $A$ has 3 rows and 2 columns, $B$ has 3 rows and 3 columns while $C$ has 2 rows and 3 columns.

### 3.2.1 Order of a matrix

A matrix having $m$ rows and $n$ columns is called a matrix of order $m \times n$ or simply $m \times n$ matrix (read as an $m$ by $n$ matrix). So referring to the above examples of matrices, we have A as $3 \times 2$ matrix, B as $3 \times 3$ matrix and C as $2 \times 3$ matrix. We observe that A has $3 \times 2=6$ elements, B and C have 9 and 6 elements, respectively.

In general, an $m \times n$ matrix has the following rectangular array:

$$
\left[\begin{array}{cccccc}
a_{11} & a_{12} & a_{13} & \cdots & a_{1 j} & \cdots \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2 j} & \cdots \\
\dot{\vdots}_{i 1} & \vdots_{i 2} & \vdots_{i 3} & \cdots & \vdots_{i j} & \cdots \\
\dot{a}_{i 1} & \vdots & \vdots & & \vdots \\
\dot{a}_{m 1} & \dot{a}_{m 2} & \dot{a}_{m 3} & \cdots & \dot{a}_{m j} & \cdots
\end{array} \dot{a}_{m n}\right]_{m \times n}
$$

or $\quad \mathrm{A}=\left[a_{i j}\right]_{m \times n}, 1 \leq i \leq m, 1 \leq j \leq n \quad i, j \in \mathrm{~N}$
Thus the $i^{\text {th }}$ row consists of the elements $a_{i 1}, a_{i 2}, a_{i 3}, \ldots, a_{i n}$, while the $j^{\text {th }}$ column consists of the elements $a_{1 j}, a_{2 j}, a_{3 j}, \ldots, a_{m j}$,

In general $a_{i j}$, is an element lying in the $i^{\text {th }}$ row and $j^{\text {th }}$ column. We can also call it as the $(i, j)^{\text {th }}$ element of A . The number of elements in an $m \times n$ matrix will be equal to $m n$.

## Note In this chapter

1. We shall follow the notation, namely $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ to indicate that A is a matrix of order $m \times n$.
2. We shall consider only those matrices whose elements are real numbers or functions taking real values.

We can also represent any point $(x, y)$ in a plane by a matrix (column or row) as $\left[\begin{array}{l}x \\ y\end{array}\right]$ (or $[x, y]$ ). For example point $\mathrm{P}(0,1)$ as a matrix representation may be given as

$$
\mathbf{P}=\left[\begin{array}{l}
0 \\
1
\end{array}\right] \text { or }\left[\begin{array}{ll}
0 & 1
\end{array}\right] .
$$

Observe that in this way we can also express the vertices of a closed rectilinear figure in the form of a matrix. For example, consider a quadrilateral $A B C D$ with vertices $\mathrm{A}(1,0), \mathrm{B}(3,2), \mathrm{C}(1,3), \mathrm{D}(-1,2)$.

Now, quadrilateral ABCD in the matrix form, can be represented as

$$
\mathrm{X}=\left[\begin{array}{cccc}
\mathrm{A} & \mathrm{~B} & \mathrm{C} & \mathrm{D} \\
1 & 3 & 1 & -1 \\
0 & 2 & 3 & 2
\end{array}\right]_{2 \times 4} \quad \text { or } \quad \mathrm{Y}=\begin{gathered}
\mathrm{A} \\
\mathrm{~B} \\
\mathrm{C} \\
\mathrm{D}
\end{gathered}\left[\begin{array}{cc}
1 & 0 \\
3 & 2 \\
1 & 3 \\
-1 & 2
\end{array}\right]_{4 \times 2}
$$

Thus, matrices can be used as representation of vertices of geometrical figures in a plane.

Now, let us consider some examples.
Example 1 Consider the following information regarding the number of men and women workers in three factories I, II and III

|  | Men workers | Women workers |
| :--- | :---: | :---: |
| I | 30 | 25 |
| II | 25 | 31 |
| III | 27 | 26 |

Represent the above information in the form of a $3 \times 2$ matrix. What does the entry in the third row and second column represent?

Solution The information is represented in the form of a $3 \times 2$ matrix as follows:

$$
A=\left[\begin{array}{ll}
30 & 25 \\
25 & 31 \\
27 & 26
\end{array}\right]
$$

The entry in the third row and second column represents the number of women workers in factory III.

Example 2 If a matrix has 8 elements, what are the possible orders it can have?
Solution We know that if a matrix is of order $m \times n$, it has $m n$ elements. Thus, to find all possible orders of a matrix with 8 elements, we will find all ordered pairs of natural numbers, whose product is 8 .
Thus, all possible ordered pairs are $(1,8),(8,1),(4,2),(2,4)$
Hence, possible orders are $1 \times 8,8 \times 1,4 \times 2,2 \times 4$
Example 3 Construct a $3 \times 2$ matrix whose elements are given by $a_{i j}=\frac{1}{2}|i-3 j|$.
Solution In general a $3 \times 2$ matrix is given by $\mathrm{A}=\left[\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32}\end{array}\right]$.
Now

$$
a_{i j}=\frac{1}{2}|i-3 j|, i=1,2,3 \text { and } j=1,2
$$

Therefore $\quad a_{11}=\frac{1}{2}|1-3 \times 1|=1 \quad a_{12}=\frac{1}{2}|1-3 \times 2|=\frac{5}{2}$

$$
\begin{array}{ll}
a_{21}=\frac{1}{2}|2-3 \times 1|=\frac{1}{2} & a_{22}=\frac{1}{2}|2-3 \times 2|=2 \\
a_{31}=\frac{1}{2}|3-3 \times 1|=0 & a_{32}=\frac{1}{2}|3-3 \times 2|=\frac{3}{2}
\end{array}
$$

Hence the required matrix is given by $\mathrm{A}=\left[\begin{array}{cc}1 & \frac{5}{2} \\ \frac{1}{2} & 2 \\ 0 & \frac{3}{2}\end{array}\right]$.

### 3.3 Types of Matrices

In this section, we shall discuss different types of matrices.
(i) Column matrix

A matrix is said to be a column matrix if it has only one column.
For example, $\mathrm{A}=\left[\begin{array}{c}0 \\ \sqrt{3} \\ -1 \\ 1 / 2\end{array}\right]$ is a column matrix of order $4 \times 1$.
In general, $\mathrm{A}=\left[a_{i j}\right]_{m \times 1}$ is a column matrix of order $m \times 1$.
(ii) Row matrix

A matrix is said to be a row matrix if it has only one row.
For example, $\mathrm{B}=\left[\begin{array}{llll}-\frac{1}{2} & \sqrt{5} & 2 & 3\end{array}\right]_{1 \times 4}$ is a row matrix.
In general, $\mathrm{B}=\left[b_{i j}\right]_{1 \times n}$ is a row matrix of order $1 \times n$.
(iii) Square matrix

A matrix in which the number of rows are equal to the number of columns, is said to be a square matrix. Thus an $m \times n$ matrix is said to be a square matrix if $m=n$ and is known as a square matrix of order ' $n$ '.

For example $A=\left[\begin{array}{ccc}3 & -1 & 0 \\ \frac{3}{2} & 3 \sqrt{2} & 1 \\ 4 & 3 & -1\end{array}\right]$ is a square matrix of order 3 .
In general, $\mathrm{A}=\left[a_{i j}\right]_{m \times m}$ is a square matrix of order $m$.
Note If $\mathrm{A}=\left[a_{i j}\right]$ is a square matrix of order $n$, then elements (entries) $a_{11}, a_{22}, \ldots, a_{n n}$ are said to constitute the diagonal, of the matrix $A$. Thus, if $A=\left[\begin{array}{ccc}1 & -3 & 1 \\ 2 & 4 & -1 \\ 3 & 5 & 6\end{array}\right]$. Then the elements of the diagonal of $A$ are $1,4,6$.
(iv) Diagonal matrix

A square matrix $\mathrm{B}=\left[b_{i j}\right]_{m \times m}$ is said to be a diagonal matrix if all its non diagonal elements are zero, that is a matrix $\mathrm{B}=\left[b_{i j}\right]_{m \times m}$ is said to be a diagonal matrix if $b_{i j}=0$, when $i \neq j$.
For example, $\mathrm{A}=[4], \mathrm{B}=\left[\begin{array}{cc}-1 & 0 \\ 0 & 2\end{array}\right], \mathrm{C}=\left[\begin{array}{ccc}-1.1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3\end{array}\right]$, are diagonal matrices of order 1,2,3, respectively.
(v) Scalar matrix

A diagonal matrix is said to be a scalar matrix if its diagonal elements are equal, that is, a square matrix $\mathrm{B}=\left[b_{i j}\right]_{n \times n}$ is said to be a scalar matrix if

$$
\begin{aligned}
& b_{i j}=0, \quad \text { when } i \neq j \\
& b_{i j}=k, \quad \text { when } i=j, \text { for some constant } k .
\end{aligned}
$$

For example
$\mathrm{A}=[3], \quad \mathrm{B}=\left[\begin{array}{cc}-1 & 0 \\ 0 & -1\end{array}\right], \quad \mathrm{C}=\left[\begin{array}{ccc}\sqrt{3} & 0 & 0 \\ 0 & \sqrt{3} & 0 \\ 0 & 0 & \sqrt{3}\end{array}\right]$
are scalar matrices of order 1, 2 and 3, respectively.
(vi) Identity matrix

A square matrix in which elements in the diagonal are all 1 and rest are all zero is called an identity matrix. In other words, the square matrix $\mathrm{A}=\left[a_{i j}\right]_{n \times n}$ is an identity matrix, if $a_{i j}=\left\{\begin{array}{lll}1 & \text { if } & i=j \\ 0 & \text { if } & i \neq j\end{array}\right.$.
We denote the identity matrix of order $n$ by $\mathrm{I}_{n}$. When order is clear from the context, we simply write it as I.

For example [1], $\left[\begin{array}{cc}1 & 0 \\ 0 & 1\end{array}\right],\left[\begin{array}{ccc}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$ are identity matrices of order 1, 2 and 3, respectively.
Observe that a scalar matrix is an identity matrix when $k=1$. But every identity matrix is clearly a scalar matrix.

## (vii) Zero matrix

A matrix is said to be zero matrix or null matrix if all its elements are zero.
For example, [0], $\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right],\left[\begin{array}{lll}0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right],[0,0]$ are all zero matrices. We denote zero matrix by O . Its order will be clear from the context.

### 3.3.1 Equality of matrices

Definition 2 Two matrices $\mathrm{A}=\left[a_{i j}\right]$ and $\mathrm{B}=\left[b_{i j}\right]$ are said to be equal if
(i) they are of the same order
(ii) each element of A is equal to the corresponding element of B , that is $a_{i j}=b_{i j}$ for all $i$ and $j$.
For example, $\left[\begin{array}{ll}2 & 3 \\ 0 & 1\end{array}\right]$ and $\left[\begin{array}{ll}2 & 3 \\ 0 & 1\end{array}\right]$ are equal matrices but $\left[\begin{array}{ll}3 & 2 \\ 0 & 1\end{array}\right]$ and $\left[\begin{array}{ll}2 & 3 \\ 0 & 1\end{array}\right]$ are not equal matrices. Symbolically, if two matrices A and B are equal, we write $\mathrm{A}=\mathrm{B}$.

If $\left[\begin{array}{ll}x & y \\ z & a \\ b & c\end{array}\right]=\left[\begin{array}{cc}-1.5 & 0 \\ 2 & \sqrt{6} \\ 3 & 2\end{array}\right]$, then $x=-1.5, y=0, z=2, a=\sqrt{6}, b=3, c=2$
Example 4 If $\left[\begin{array}{ccc}x+3 & z+4 & 2 y-7 \\ -6 & a-1 & 0 \\ b-3 & -21 & 0\end{array}\right]=\left[\begin{array}{ccc}0 & 6 & 3 y-2 \\ -6 & -3 & 2 c+2 \\ 2 b+4 & -21 & 0\end{array}\right]$
Find the values of $a, b, c, x, y$ and $z$.
Solution As the given matrices are equal, therefore, their corresponding elements must be equal. Comparing the corresponding elements, we get

$$
\begin{array}{rlrl}
x+3 & =0, & z+4 & =6, \\
a-1 & =-3, & 0 & =2 c+2 \\
a-3 & =3 y-2 \\
& & b-3 & =2 b+4
\end{array}
$$

Simplifying, we get

$$
a=-2, b=-7, c=-1, x=-3, y=-5, z=2
$$

Example 5 Find the values of $a, b, c$, and $d$ from the following equation:

$$
\left[\begin{array}{cc}
2 a+b & a-2 b \\
5 c-d & 4 c+3 d
\end{array}\right]=\left[\begin{array}{cc}
4 & -3 \\
11 & 24
\end{array}\right]
$$

Solution By equality of two matrices, equating the corresponding elements, we get

$$
\begin{array}{rlrl}
2 a+b & =4 & 5 c-d & =11 \\
a-2 b & =-3 & 4 c+3 d & =24
\end{array}
$$

Solving these equations, we get

$$
a=1, b=2, c=3 \text { and } d=4
$$

## EXERCISE 3.1

1. In the matrix $A=\left[\begin{array}{cccc}2 & 5 & 19 & -7 \\ 35 & -2 & \frac{5}{2} & 12 \\ \sqrt{3} & 1 & -5 & 17\end{array}\right]$, write:
(i) The order of the matrix,
(ii) The number of elements,
(iii) Write the elements $a_{13}, a_{21}, a_{33}, a_{24}, a_{23}$.
2. If a matrix has 24 elements, what are the possible orders it can have? What, if it has 13 elements?
3. If a matrix has 18 elements, what are the possible orders it can have? What, if it has 5 elements?
4. Construct a $2 \times 2$ matrix, $\mathrm{A}=\left[a_{i j}\right]$, whose elements are given by:
(i) $a_{i j}=\frac{(i+j)^{2}}{2}$
(ii) $a_{i j}=\frac{i}{j}$
(iii) $a_{i j}=\frac{(i+2 j)^{2}}{2}$
5. Construct a $3 \times 4$ matrix, whose elements are given by:
(i) $a_{i j}=\frac{1}{2}|-3 i+j|$
(ii) $a_{i j}=2 i-j$
6. Find the values of $x, y$ and $z$ from the following equations:
(i) $\left[\begin{array}{ll}4 & 3 \\ x & 5\end{array}\right]=\left[\begin{array}{ll}y & z \\ 1 & 5\end{array}\right]$
(ii) $\left[\begin{array}{cc}x+y & 2 \\ 5+z & x y\end{array}\right]=\left[\begin{array}{ll}6 & 2 \\ 5 & 8\end{array}\right]$ (iii)
(iii) $\left[\begin{array}{c}x+y+z \\ x+z \\ y+z\end{array}\right]=\left[\begin{array}{l}9 \\ 5 \\ 7\end{array}\right]$
7. Find the value of $a, b, c$ and $d$ from the equation:

$$
\left[\begin{array}{cc}
a-b & 2 a+c \\
2 a-b & 3 c+d
\end{array}\right]=\left[\begin{array}{cc}
-1 & 5 \\
0 & 13
\end{array}\right]
$$

8. $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ is a square matrix, if
(A) $m<n$
(B) $m>n$
(C) $m=n$
(D) None of these
9. Which of the given values of $x$ and $y$ make the following pair of matrices equal $\left[\begin{array}{cc}3 x+7 & 5 \\ y+1 & 2-3 x\end{array}\right],\left[\begin{array}{cc}0 & y-2 \\ 8 & 4\end{array}\right]$
(A) $x=\frac{-1}{3}, y=7$
(B) Not possible to find
(C) $y=7, \quad x=\frac{-2}{3}$
(D) $x=\frac{-1}{3}, y=\frac{-2}{3}$
10. The number of all possible matrices of order $3 \times 3$ with each entry 0 or 1 is:
(A) 27
(B) 18
(C) 81
(D) 512

### 3.4 Operations on Matrices

In this section, we shall introduce certain operations on matrices, namely, addition of matrices, multiplication of a matrix by a scalar, difference and multiplication of matrices.

### 3.4.1 Addition of matrices

Suppose Fatima has two factories at places A and B. Each factory produces sport shoes for boys and girls in three different price categories labelled 1, 2 and 3. The quantities produced by each factory are represented as matrices given below:
![](https://cdn.mathpix.com/cropped/2025_07_21_a374a9ab152c8b061e73g-10.jpg?height=293&width=766&top_left_y=1324&top_left_x=431)

Suppose Fatima wants to know the total production of sport shoes in each price category. Then the total production

In category 1 : for boys $(80+90)$, for girls $(60+50)$
In category 2 : for boys ( $75+70$ ), for girls ( $65+55$ )
In category 3 : for boys $(90+75)$, for girls $(85+75)$
This can be represented in the matrix form as $\left[\begin{array}{ll}80+90 & 60+50 \\ 75+70 & 65+55 \\ 90+75 & 85+75\end{array}\right]$.

This new matrix is the sum of the above two matrices. We observe that the sum of two matrices is a matrix obtained by adding the corresponding elements of the given matrices. Furthermore, the two matrices have to be of the same order.

Thus, if $\mathrm{A}=\left[\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23}\end{array}\right]$ is a $2 \times 3$ matrix and $\mathrm{B}=\left[\begin{array}{lll}b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23}\end{array}\right]$ is another $2 \times 3$ matrix. Then, we define $\mathrm{A}+\mathrm{B}=\left[\begin{array}{lll}a_{11}+b_{11} & a_{12}+b_{12} & a_{13}+b_{13} \\ a_{21}+b_{21} & a_{22}+b_{22} & a_{23}+b_{23}\end{array}\right]$.

In general, if $\mathrm{A}=\left[a_{i j}\right]$ and $\mathrm{B}=\left[b_{i j}\right]$ are two matrices of the same order, say $m \times n$. Then, the sum of the two matrices A and B is defined as a matrix $\mathrm{C}=\left[c_{i j}\right]_{m \times n}$, where $c_{i j}=a_{i j}+b_{i j}$, for all possible values of $i$ and $j$.

Example 6 Given $\mathrm{A}=\left[\begin{array}{ccc}\sqrt{3} & 1 & -1 \\ 2 & 3 & 0\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}2 & \sqrt{5} & 1 \\ -2 & 3 & \frac{1}{2}\end{array}\right]$, find $\mathrm{A}+\mathrm{B}$
Since A, B are of the same order $2 \times 3$. Therefore, addition of A and B is defined and is given by

$$
\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
2+\sqrt{3} & 1+\sqrt{5} & 1-1 \\
2-2 & 3+3 & 0+\frac{1}{2}
\end{array}\right]=\left[\begin{array}{ccc}
2+\sqrt{3} & 1+\sqrt{5} & 0 \\
0 & 6 & \frac{1}{2}
\end{array}\right]
$$

Note

1. We emphasise that if $A$ and $B$ are not of the same order, then $A+B$ is not defined. For example if $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 0\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 2 & 3 \\ 1 & 0 & 1\end{array}\right]$, then $\mathrm{A}+\mathrm{B}$ is not defined.
2. We may observe that addition of matrices is an example of binary operation on the set of matrices of the same order.

### 3.4.2 Multiplication of a matrix by a scalar

Now suppose that Fatima has doubled the production at a factory A in all categories (refer to 3.4.1).

Previously quantities (in standard units) produced by factory A were
1
2

3 | Boys | Girls |
| :---: | :---: |
| $\left[\begin{array}{c}80 \\ 75 \\ 90\end{array}\right.$ | $\left.\begin{array}{c}60 \\ 65 \\ 85\end{array}\right]$ |

Revised quantities produced by factory A are as given below:
Boys Girls
1
2
3 $\left[\begin{array}{ll}2 \times 80 & 2 \times 60 \\ 2 \times 75 & 2 \times 65 \\ 2 \times 90 & 2 \times 85\end{array}\right]$

This can be represented in the matrix form as $\left[\begin{array}{ll}160 & 120 \\ 150 & 130 \\ 180 & 170\end{array}\right]$. We observe that the new matrix is obtained by multiplying each element of the previous matrix by 2 .

In general, we may define multiplication of a matrix by a scalar as follows: if $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ is a matrix and $k$ is a scalar, then $k \mathrm{~A}$ is another matrix which is obtained by multiplying each element of A by the scalar $k$.

In other words, $k \mathrm{~A}=k\left[a_{i j}\right]_{m \times n}=\left[k\left(a_{i j}\right)\right]_{m \times n}$, that is, $(i, j)^{\text {th }}$ element of $k \mathrm{~A}$ is $k a_{i j}$ for all possible values of $i$ and $j$.

For example, if $\quad A=\left[\begin{array}{ccc}3 & 1 & 1.5 \\ \sqrt{5} & 7 & -3 \\ 2 & 0 & 5\end{array}\right]$, then

$$
3 \mathrm{~A}=3\left[\begin{array}{ccc}
3 & 1 & 1.5 \\
\sqrt{5} & 7 & -3 \\
2 & 0 & 5
\end{array}\right]=\left[\begin{array}{ccc}
9 & 3 & 4.5 \\
3 \sqrt{5} & 21 & -9 \\
6 & 0 & 15
\end{array}\right]
$$

Negative of a matrix The negative of a matrix is denoted by -A . We define $-\mathrm{A}=(-1) \mathrm{A}$.

For example, let

$$
\begin{aligned}
A & =\left[\begin{array}{cc}
3 & 1 \\
-5 & x
\end{array}\right], \text { then }-A \text { is given by } \\
-A & =(-1) A=(-1)\left[\begin{array}{cc}
3 & 1 \\
-5 & x
\end{array}\right]=\left[\begin{array}{cc}
-3 & -1 \\
5 & -x
\end{array}\right]
\end{aligned}
$$

Difference of matrices If $\mathrm{A}=\left[a_{i j}\right], \mathrm{B}=\left[b_{i j}\right]$ are two matrices of the same order, say $m \times n$, then difference $\mathrm{A}-\mathrm{B}$ is defined as a matrix $\mathrm{D}=\left[d_{i j}\right]$, where $d_{i j}=a_{i j}-b_{i j}$, for all value of $i$ and $j$. In other words, $\mathrm{D}=\mathrm{A}-\mathrm{B}=\mathrm{A}+(-1) \mathrm{B}$, that is sum of the matrix A and the matrix -B .
Example 7 If $\mathrm{A}=\left[\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}3 & -1 & 3 \\ -1 & 0 & 2\end{array}\right]$, then find $2 \mathrm{~A}-\mathrm{B}$.
Solution We have

$$
\begin{aligned}
2 \mathrm{~A}-\mathrm{B} & =2 \begin{array}{ccc}
1 & 2 & 3 \\
2 & 3 & 1
\end{array}-\begin{array}{rrr}
3 & -1 & 3 \\
-1 & 0 & 2
\end{array} \\
& =\left[\begin{array}{lll}
2 & 4 & 6 \\
4 & 6 & 2
\end{array}\right]+\left[\begin{array}{ccc}
-3 & 1 & -3 \\
1 & 0 & -2
\end{array}\right] \\
& =\left[\begin{array}{ccc}
2-3 & 4+1 & 6-3 \\
4+1 & 6+0 & 2-2
\end{array}\right]=\left[\begin{array}{ccc}
-1 & 5 & 3 \\
5 & 6 & 0
\end{array}\right]
\end{aligned}
$$

### 3.4.3 Properties of matrix addition

The addition of matrices satisfy the following properties:
(i) Commutative Law If $\mathrm{A}=\left[a_{i j}\right], \mathrm{B}=\left[b_{i j}\right]$ are matrices of the same order, say $m \times n$, then $\mathrm{A}+\mathrm{B}=\mathrm{B}+\mathrm{A}$.
Now

$$
\begin{aligned}
\mathrm{A}+\mathrm{B} & =\left[a_{i j}\right]+\left[b_{i j}\right]=\left[a_{i j}+b_{i j}\right] \\
& =\left[b_{i j}+a_{i j}\right] \text { (addition of numbers is commutative) } \\
& =\left(\left[b_{i j}\right]+\left[a_{i j}\right]\right)=\mathrm{B}+\mathrm{A}
\end{aligned}
$$

(ii) Associative Law For any three matrices $\mathrm{A}=\left[a_{i j}\right], \mathrm{B}=\left[b_{i j}\right], \mathrm{C}=\left[c_{i j}\right]$ of the same order, say $m \times n,(\mathrm{~A}+\mathrm{B})+\mathrm{C}=\mathrm{A}+(\mathrm{B}+\mathrm{C})$.
Now

$$
\begin{aligned}
(\mathrm{A}+\mathrm{B})+\mathrm{C} & =\left(\left[a_{i j}\right]+\left[b_{i j}\right]\right)+\left[c_{i j}\right] \\
& =\left[a_{i j}+b_{i j}\right]+\left[c_{i j}\right]=\left[\left(a_{i j}+b_{i j}\right)+c_{i j}\right] \\
& =\left[a_{i j}+\left(b_{i j}+c_{i j}\right)\right] \quad(\text { Why? }) \\
& =\left[a_{i j}\right]+\left[\left(b_{i j}+c_{i j}\right)\right]=\left[a_{i j}\right]+\left(\left[b_{i j}\right]+\left[c_{i j}\right]\right)=\mathrm{A}+(\mathrm{B}+\mathrm{C})
\end{aligned}
$$

(iii) Existence of additive identity Let $\mathrm{A}=\left[a_{i j}\right]$ be an $m \times n$ matrix and O be an $m \times n$ zero matrix, then $\mathrm{A}+\mathrm{O}=\mathrm{O}+\mathrm{A}=\mathrm{A}$. In other words, O is the additive identity for matrix addition.
(iv) The existence of additive inverse Let $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ be any matrix, then we have another matrix as $-\mathrm{A}=\left[-a_{i j}\right]_{m \times n}$ such that $\mathrm{A}+(-\mathrm{A})=(-\mathrm{A})+\mathrm{A}=\mathrm{O}$. So - A is the additive inverse of A or negative of A .

### 3.4.4 Properties of scalar multiplication of a matrix

If $\mathrm{A}=\left[a_{i j}\right]$ and $\mathrm{B}=\left[b_{i j}\right]$ be two matrices of the same order, say $m \times n$, and $k$ and $l$ are scalars, then
(i) $k(\mathrm{~A}+\mathrm{B})=k \mathrm{~A}+k \mathrm{~B},($ ii) $(k+l) \mathrm{A}=k \mathrm{~A}+l \mathrm{~A}$
(ii) $k(\mathrm{~A}+\mathrm{B})=k\left(\left[a_{i j}\right]+\left[b_{i j}\right]\right)$

$$
\begin{aligned}
& =k\left[a_{i j}+b_{i j}\right]=\left[k\left(a_{i j}+b_{i j}\right)\right]=\left[\left(k a_{i j}\right)+\left(k b_{i j}\right)\right] \\
& =\left[\begin{array}{ll}
k & a_{i j}
\end{array}\right]+\left[\begin{array}{ll}
k & b_{i j}
\end{array}\right]=k\left[a_{i j}\right]+k\left[b_{i j}\right]=k \mathrm{~A}+k \mathrm{~B}
\end{aligned}
$$

(iii) $(k+l) \mathrm{A}=(k+l)\left[a_{i j}\right]$

$$
=\left[(k+l) a_{i j}\right]+\left[\begin{array}{ll}
k & a_{i j}
\end{array}\right]+\left[l a_{i j}\right]=k\left[a_{i j}\right]+l\left[a_{i j}\right]=k \mathrm{~A}+l \mathrm{~A}
$$

Example 8 If $\mathrm{A}=\left[\begin{array}{cc}8 & 0 \\ 4 & -2 \\ 3 & 6\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{cc}2 & -2 \\ 4 & 2 \\ -5 & 1\end{array}\right]$, then find the matrix X , such that $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$.

Solution We have $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$
or
or $\quad 2 \mathrm{~A}-2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}-2 \mathrm{~A} \quad$ (Matrix addition is commutative)
or $\quad \mathrm{O}+3 \mathrm{X}=5 \mathrm{~B}-2 \mathrm{~A} \quad(-2 \mathrm{~A}$ is the additive inverse of 2A)
or $\quad 3 \mathrm{X}=5 \mathrm{~B}-2 \mathrm{~A} \quad$ ( O is the additive identity)
or

$$
X=\frac{1}{3}(5 B-2 A)
$$

or

$$
\mathrm{X}=\frac{1}{3}\left(5\left[\begin{array}{cc}
2 & -2 \\
4 & 2 \\
-5 & 1
\end{array}\right]-2\left[\begin{array}{cc}
8 & 0 \\
4 & -2 \\
3 & 6
\end{array}\right]\right)=\frac{1}{3}\left(\left[\begin{array}{cc}
10 & -10 \\
20 & 10 \\
-25 & 5
\end{array}\right]+\left[\begin{array}{cc}
-16 & 0 \\
-8 & 4 \\
-6 & -12
\end{array}\right]\right)
$$

$$
=\frac{1}{3}\left[\begin{array}{cc}
10-16 & -10+0 \\
20-8 & 10+4 \\
-25-6 & 5-12
\end{array}\right]=\frac{1}{3}\left[\begin{array}{cc}
-6 & -10 \\
12 & 14 \\
-31 & -7
\end{array}\right]=\left[\begin{array}{cc}
-2 & \frac{-10}{3} \\
4 & \frac{14}{3} \\
\frac{-31}{3} & \frac{-7}{3}
\end{array}\right]
$$

Example 9 Find X and Y , if $\mathrm{X}+\mathrm{Y}=\left[\begin{array}{cc}5 & 2 \\ 0 & 9\end{array}\right]$ and $\mathrm{X}-\mathrm{Y}=\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$.
Solution We have $(\mathrm{X}+\mathrm{Y})+(\mathrm{X}-\mathrm{Y})=\left[\begin{array}{cc}5 & 2 \\ 0 & 9\end{array}\right]+\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$.
or

$$
\begin{gathered}
(\mathrm{X}+\mathrm{X})+(\mathrm{Y}-\mathrm{Y})=\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right] \Rightarrow 2 \mathrm{X}=\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right] \\
\mathrm{X}=\frac{1}{2}\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right]=\left[\begin{array}{ll}
4 & 4 \\
0 & 4
\end{array}\right]
\end{gathered}
$$

or

$$
(\mathrm{X}+\mathrm{Y})-(\mathrm{X}-\mathrm{Y})=\left[\begin{array}{ll}
5 & 2 \\
0 & 9
\end{array}\right]-\left[\begin{array}{rr}
3 & 6 \\
0 & -1
\end{array}\right]
$$

or

$$
(\mathrm{X}-\mathrm{X})+(\mathrm{Y}+\mathrm{Y})=\left[\begin{array}{cc}
5-3 & 2-6 \\
0 & 9+1
\end{array}\right] \Rightarrow 2 \mathrm{Y}=\left[\begin{array}{cc}
2 & -4 \\
0 & 10
\end{array}\right]
$$

or

$$
\mathrm{Y}=\frac{1}{2}\left[\begin{array}{rr}
2 & -4 \\
0 & 10
\end{array}\right]=\left[\begin{array}{rr}
1 & -2 \\
0 & 5
\end{array}\right]
$$

Example 10 Find the values of $x$ and $y$ from the following equation:

$$
2\left[\begin{array}{cc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{rr}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

Solution We have

$$
2\left[\begin{array}{cc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right] \Rightarrow\left[\begin{array}{cc}
2 x & 10 \\
14 & 2 y-6
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

$$
\begin{array}{lc}
\text { or } & {\left[\begin{array}{cc}
2 x+3 & 10-4 \\
14+1 & 2 y-6+2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right] \Rightarrow\left[\begin{array}{cc}
2 x+3 & 6 \\
15 & 2 y-4
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]} \\
\text { or } & 2 x+3=7 \\
\text { or } & 2 x=7-3 \\
\text { or } & \text { and } \\
\text { i.e. } & \begin{aligned}
x=\frac{4}{2} & \text { and }
\end{aligned}
\end{array} \begin{array}{cc}
2 y-4=14 & 2 y=18 \\
\text { (Why?) } & \text { and }
\end{array} \quad \begin{aligned}
& y=\frac{18}{2} \\
& x=2 \text { and }
\end{aligned} \quad y=9 . \quad \text { y }=9 .
$$

Example 11 Two farmers Ramkishan and Gurcharan Singh cultivates only three varieties of rice namely Basmati, Permal and Naura. The sale (in Rupees) of these varieties of rice by both the farmers in the month of September and October are given by the following matrices A and B.

$$
\begin{aligned}
& \text { September Sales (in Rupees) } \\
& \left.\mathrm{A}=\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
10,000 & 20,000 & 30,000 \\
50,000 & 30,000 & 10,000
\end{array}\right] \text { Ramkishan } \\
& \text { October Sales (in Rupees) } \\
& \mathrm{B}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 6000 \\
20,000 & 10,000 & 10,000
\end{array}\right] \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$

(i) Find the combined sales in September and October for each farmer in each variety.
(ii) Find the decrease in sales from September to October.
(iii) If both farmers receive $2 \%$ profit on gross sales, compute the profit for each farmer and for each variety sold in October.

## Solution

(i) Combined sales in September and October for each farmer in each variety is given by

$$
\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
15,000 & 30,000 & 36,000 \\
70,000 & 40,000 & 20,000
\end{array}\right] \text { Ramkishan } \begin{aligned}
& \text { Gurcharan Singh } \\
& \text { Guron }
\end{aligned}
$$

(ii) Change in sales from September to October is given by

$$
\mathrm{A}-\mathrm{B}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 24,000 \\
30,000 & 20,000 & 0
\end{array}\right] \text { Ramkishan } \begin{aligned}
& \text { Gurcharan Singh } \\
& \hline
\end{aligned}
$$

(iii) $2 \%$ of $\mathrm{B}=\frac{2}{100} \times \mathrm{B}=0.02 \times \mathrm{B}$

$$
\begin{aligned}
& =0.02\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 6000 \\
20,000 & 10,000 & 10,000
\end{array}\right] \text { Ramkishan } \\
& \text { Gurcharan Singh } \\
& =\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
100 & 200 & 120 \\
400 & 200 & 200
\end{array}\right] \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$

Thus, in October Ramkishan receives ₹ 100, ₹ 200 and ₹ 120 as profit in the sale of each variety of rice, respectively, and Grucharan Singh receives profit of ₹ 400 , ₹ 200 and ₹ 200 in the sale of each variety of rice, respectively.

### 3.4.5 Multiplication of matrices

Suppose Meera and Nadeem are two friends. Meera wants to buy 2 pens and 5 story books, while Nadeem needs 8 pens and 10 story books. They both go to a shop to enquire about the rates which are quoted as follows:

Pen - ₹ 5 each, story book - ₹ 50 each.
How much money does each need to spend? Clearly, Meera needs $₹(5 \times 2+50 \times 5)$ that is ₹ 260, while Nadeem needs ( $8 \times 5+50 \times 10$ ) ₹, that is ₹ 540 . In terms of matrix representation, we can write the above information as follows:

## Requirements Prices per piece (in Rupees) Money needed (in Rupees)

$$
\left[\begin{array}{cc}
2 & 5 \\
8 & 10
\end{array}\right] \quad\left[\begin{array}{c}
5 \\
50
\end{array}\right] \quad\left[\begin{array}{c}
5 \times 2+5 \times 50 \\
8 \times 5+10 \times 50
\end{array}\right]=\left[\begin{array}{c}
260 \\
540
\end{array}\right]
$$

Suppose that they enquire about the rates from another shop, quoted as follows:
pen - ₹ 4 each, story book - ₹ 40 each.
Now, the money required by Meera and Nadeem to make purchases will be respectively $₹(4 \times 2+40 \times 5)=₹ 208$ and $₹(8 \times 4+10 \times 40)=₹ 432$

Again, the above information can be represented as follows:

## Requirements Prices per piece (in Rupees) Money needed (in Rupees)

$$
\left[\begin{array}{cc}
2 & 5 \\
8 & 10
\end{array}\right]
$$

$$
\left[\begin{array}{c}
4 \\
40
\end{array}\right]
$$

$$
\left[\begin{array}{c}
4 \times 2+40 \times 5 \\
8 \times 4+10 \times 40
\end{array}\right]=\left[\begin{array}{c}
208 \\
432
\end{array}\right]
$$

Now, the information in both the cases can be combined and expressed in terms of matrices as follows:

## Requirements Prices per piece (in Rupees)

Money needed (in Rupees)

$$
\left.\begin{array}{cc}
{\left[\begin{array}{cc}
2 & 5 \\
8 & 10
\end{array}\right]} & {\left[\begin{array}{cc}
5 & 4 \\
50 & 40
\end{array}\right]} \\
& =\left[\begin{array}{cc}
5 \times 2+5 \times 50 & 4 \times 2+40 \times 5 \\
8 \times 5+10 \times 50 & 8 \times 4+10 \times 40
\end{array}\right] \\
540 & 432
\end{array}\right]=
$$

The above is an example of multiplication of matrices. We observe that, for multiplication of two matrices A and B , the number of columns in A should be equal to the number of rows in B . Furthermore for getting the elements of the product matrix, we take rows of A and columns of B , multiply them element-wise and take the sum. Formally, we define multiplication of matrices as follows:

The product of two matrices A and B is defined if the number of columns of A is equal to the number of rows of B . Let $\mathrm{A}=\left[a_{i j}\right]$ be an $m \times n$ matrix and $\mathrm{B}=\left[b_{j k}\right]$ be an $n \times p$ matrix. Then the product of the matrices A and B is the matrix C of order $m \times p$. To get the $(i, k)^{\text {th }}$ element $c_{i k}$ of the matrix C , we take the $i^{\text {th }}$ row of A and $k^{\text {th }}$ column of B , multiply them elementwise and take the sum of all these products. In other words, if $\mathrm{A}=\left[a_{i j}\right]_{m \times n}, \mathrm{~B}=\left[b_{j k}\right]_{n \times p}$, then the $i^{\text {th }}$ row of A is $\left[a_{i 1} a_{i 2} \ldots a_{i n}\right]$ and the $k^{\text {th }}$ column of B is $\left[\begin{array}{c}b_{1 k} \\ b_{2 k} \\ \vdots \\ b_{n k}\end{array}\right]$, then $c_{i k}=a_{i 1} b_{1 k}+a_{i 2} b_{2 k}+a_{i 3} b_{3 k}+\ldots+a_{i n} b_{n k}=\sum_{j=1}^{n} a_{i j} b_{j k}$.

The matrix $\mathrm{C}=\left[c_{i k}\right]_{m \times p}$ is the product of A and B .
For example, if $\mathrm{C}=\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]$ and $\mathrm{D}=\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]$, then the product CD is defined
and is given by $\mathrm{CD}=\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]$. This is a $2 \times 2$ matrix in which each entry is the sum of the products across some row of C with the corresponding entries down some column of D . These four computations are
$\begin{aligned} & \text { Entry in } \\ & \text { first row } \\ & \text { first column }\end{aligned}\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{cc}(1)(2)+(-1)(-1)+(2)(5) & ? \\ ? & ?\end{array}\right]$
$\begin{aligned} & \text { Entry in } \\ & \text { first row } \\ & \text { second column }\end{aligned}\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{cc}13 & (1)(7)+(-1)(1)+2(-4) \\ ? & ?\end{array}\right]$
$\begin{aligned} & \text { Entry in } \\ & \text { second row } \\ & \text { first column }\end{aligned}\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{ll}13 & -2 \\ 0(2)+3(-1)+4(5) & ?\end{array}\right]$
$\begin{aligned} & \text { Entry in } \\ & \text { second row } \\ & \text { second column }\end{aligned}\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{ll}13 & -2 \\ 17 & 0(7)+3(1)+4(-4)\end{array}\right]$
Thus $\mathrm{CD}=\left[\begin{array}{ll}13 & -2 \\ 17 & -13\end{array}\right]$
Example 12 Find AB , if $\mathrm{A}=\left[\begin{array}{ll}6 & 9 \\ 2 & 3\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{lll}2 & 6 & 0 \\ 7 & 9 & 8\end{array}\right]$.
Solution The matrix A has 2 columns which is equal to the number of rows of B. Hence $A B$ is defined. Now

$$
\begin{aligned}
\mathrm{AB} & =\left[\begin{array}{lll}
6(2)+9(7) & 6(6)+9(9) & 6(0)+9(8) \\
2(2)+3(7) & 2(6)+3(9) & 2(0)+3(8)
\end{array}\right] \\
& =\left[\begin{array}{ccc}
12+63 & 36+81 & 0+72 \\
4+21 & 12+27 & 0+24
\end{array}\right]=\left[\begin{array}{ccc}
75 & 117 & 72 \\
25 & 39 & 24
\end{array}\right]
\end{aligned}
$$

Remark If AB is defined, then BA need not be defined. In the above example, AB is defined but BA is not defined because B has 3 column while A has only 2 (and not 3 ) rows. If $\mathrm{A}, \mathrm{B}$ are, respectively $m \times n, k \times l$ matrices, then both AB and BA are defined if and only if $n=k$ and $l=m$. In particular, if both A and B are square matrices of the same order, then both AB and BA are defined.

## Non-commutativity of multiplication of matrices

Now, we shall see by an example that even if AB and BA are both defined, it is not necessary that $\mathrm{AB}=\mathrm{BA}$.

Example 13 If $\mathrm{A}=\left[\begin{array}{ccc}1 & -2 & 3 \\ -4 & 2 & 5\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}2 & 3 \\ 4 & 5 \\ 2 & 1\end{array}\right]$, then find $\mathrm{AB}, \mathrm{BA}$. Show that $\mathrm{AB} \neq \mathrm{BA}$.

Solution Since A is a $2 \times 3$ matrix and B is $3 \times 2$ matrix. Hence AB and BA are both defined and are matrices of order $2 \times 2$ and $3 \times 3$, respectively. Note that

$$
\mathrm{AB}=\left[\begin{array}{rrr}
1 & -2 & 3 \\
-4 & 2 & 5
\end{array}\right]\left[\begin{array}{ll}
2 & 3 \\
4 & 5 \\
2 & 1
\end{array}\right]=\left[\begin{array}{cc}
2-8+6 & 3-10+3 \\
-8+8+10 & -12+10+5
\end{array}\right]=\left[\begin{array}{cr}
0 & -4 \\
10 & 3
\end{array}\right]
$$

and $\quad \mathrm{BA}=\left[\begin{array}{cc}2 & 3 \\ 4 & 5 \\ 2 & 1\end{array}\right]\left[\begin{array}{ccc}1 & -2 & 3 \\ -4 & 2 & 5\end{array}\right]=\left[\begin{array}{ccc}2-12 & -4+6 & 6+15 \\ 4-20 & -8+10 & 12+25 \\ 2-4 & -4+2 & 6+5\end{array}\right]=\left[\begin{array}{ccc}-10 & 2 & 21 \\ -16 & 2 & 37 \\ -2 & -2 & 11\end{array}\right]$
Clearly $\mathrm{AB} \neq \mathrm{BA}$
In the above example both AB and BA are of different order and so $\mathrm{AB} \neq \mathrm{BA}$. But one may think that perhaps $A B$ and $B A$ could be the same if they were of the same order. But it is not so, here we give an example to show that even if AB and BA are of same order they may not be same.

Example 14 If $\mathrm{A}=\left[\begin{array}{rr}1 & 0 \\ 0 & -1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$, then $\mathrm{AB}=\left[\begin{array}{rr}0 & 1 \\ -1 & 0\end{array}\right]$.
and

$$
\mathrm{BA}=\left[\begin{array}{rr}
0 & -1 \\
1 & 0
\end{array}\right] . \text { Clearly } \mathrm{AB} \neq \mathrm{BA} .
$$

Thus matrix multiplication is not commutative.
$\square$ Note This does not mean that $\mathrm{AB} \neq \mathrm{BA}$ for every pair of matrices $\mathrm{A}, \mathrm{B}$ for which AB and BA , are defined. For instance,
If $\mathrm{A}=\left[\begin{array}{ll}1 & 0 \\ 0 & 2\end{array}\right], \mathrm{B}=\left[\begin{array}{ll}3 & 0 \\ 0 & 4\end{array}\right]$, then $\mathrm{AB}=\mathrm{BA}=\left[\begin{array}{ll}3 & 0 \\ 0 & 8\end{array}\right]$
Observe that multiplication of diagonal matrices of same order will be commutative.

## Zero matrix as the product of two non zero matrices

We know that, for real numbers $a, b$ if $a b=0$, then either $a=0$ or $b=0$. This need not be true for matrices, we will observe this through an example.

Example 15 Find AB , if $\mathrm{A}=\left[\begin{array}{rr}0 & -1 \\ 0 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}3 & 5 \\ 0 & 0\end{array}\right]$.
Solution We have $\mathrm{AB}=\left[\begin{array}{rr}0 & -1 \\ 0 & 2\end{array}\right]\left[\begin{array}{ll}3 & 5 \\ 0 & 0\end{array}\right]=\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right]$.
Thus, if the product of two matrices is a zero matrix, it is not necessary that one of the matrices is a zero matrix.

### 3.4.6 Properties of multiplication of matrices

The multiplication of matrices possesses the following properties, which we state without proof.

1. The associative law For any three matrices $A, B$ and $C$. We have
$(\mathrm{AB}) \mathrm{C}=\mathrm{A}(\mathrm{BC})$, whenever both sides of the equality are defined.
2. The distributive law For three matrices $\mathrm{A}, \mathrm{B}$ and C .
(i) $\mathrm{A}(\mathrm{B}+\mathrm{C})=\mathrm{AB}+\mathrm{AC}$
(ii) $(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}$, whenever both sides of equality are defined.
3. The existence of multiplicative identity For every square matrix $A$, there exist an identity matrix of same order such that $I A=A I=A$.
Now, we shall verify these properties by examples.
Example 16 If $\mathrm{A}=\left[\begin{array}{rcr}1 & 1 & -1 \\ 2 & 0 & 3 \\ 3 & -1 & 2\end{array}\right], \mathrm{B}=\left[\begin{array}{rr}1 & 3 \\ 0 & 2 \\ -1 & 4\end{array}\right]$ and $\mathrm{C}=\left[\begin{array}{lllr}1 & 2 & 3 & -4 \\ 2 & 0 & -2 & 1\end{array}\right]$, find $\mathrm{A}(\mathrm{BC}),(\mathrm{AB}) \mathrm{C}$ and show that $(\mathrm{AB}) \mathrm{C}=\mathrm{A}(\mathrm{BC})$.

Solution We have $\mathrm{AB}=\left[\begin{array}{ccc}1 & 1 & -1 \\ 2 & 0 & 3 \\ 3 & -1 & 2\end{array}\right]\left[\begin{array}{rr}1 & 3 \\ 0 & 2 \\ -1 & 4\end{array}\right]=\left[\begin{array}{ll}1+0+1 & 3+2-4 \\ 2+0-3 & 6+0+12 \\ 3+0-2 & 9-2+8\end{array}\right]=\left[\begin{array}{rc}2 & 1 \\ -1 & 18 \\ 1 & 15\end{array}\right]$

$$
\begin{aligned}
(\mathrm{AB})(\mathrm{C}) & =\left[\begin{array}{rr}
2 & 1 \\
-1 & 18 \\
1 & 15
\end{array}\right]\left[\begin{array}{cccc}
1 & 2 & 3 & -4 \\
2 & 0 & -2 & 1
\end{array}\right]=\left[\begin{array}{cccc}
2+2 & 4+0 & 6-2 & -8+1 \\
-1+36 & -2+0 & -3-36 & 4+18 \\
1+30 & 2+0 & 3-30 & -4+15
\end{array}\right] \\
& =\left[\begin{array}{cccc}
4 & 4 & 4 & -7 \\
35 & -2 & -39 & 22 \\
31 & 2 & -27 & 11
\end{array}\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
\mathrm{BC} & =\left[\begin{array}{rr}
1 & 3 \\
0 & 2 \\
-1 & 4
\end{array}\right]\left[\begin{array}{rrrr}
1 & 2 & 3 & -4 \\
2 & 0 & -2 & 1
\end{array}\right]=\left[\begin{array}{rrrr}
1+6 & 2+0 & 3-6 & -4+3 \\
0+4 & 0+0 & 0-4 & 0+2 \\
-1+8 & -2+0 & -3-8 & 4+4
\end{array}\right] \\
& =\left[\begin{array}{rrrr}
7 & 2 & -3 & -1 \\
4 & 0 & -4 & 2 \\
7 & -2 & -11 & 8
\end{array}\right]
\end{aligned}
$$

Therefore

$$
\begin{aligned}
\mathrm{A}(\mathrm{BC}) & =\left[\begin{array}{rrr}
1 & 1 & -1 \\
2 & 0 & 3 \\
3 & -1 & 2
\end{array}\right]\left[\begin{array}{cccc}
7 & 2 & -3 & -1 \\
4 & 0 & -4 & 2 \\
7 & -2 & -11 & 8
\end{array}\right] \\
& =\left[\begin{array}{cccc}
7+4-7 & 2+0+2 & -3-4+11 & -1+2-8 \\
14+0+21 & 4+0-6 & -6+0-33 & -2+0+24 \\
21-4+14 & 6+0-4 & -9+4-22 & -3-2+16
\end{array}\right] \\
& =\left[\begin{array}{cccc}
4 & 4 & 4 & -7 \\
35 & -2 & -39 & 22 \\
31 & 2 & -27 & 11
\end{array}\right] . \text { Clearly, }(\mathrm{AB}) \mathrm{C}=\mathrm{A}(\mathrm{BC})
\end{aligned}
$$

Example 17 If $\mathrm{A}=\left[\begin{array}{rrr}0 & 6 & 7 \\ -6 & 0 & 8 \\ 7 & -8 & 0\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}0 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 2 & 0\end{array}\right], \mathrm{C}=\left[\begin{array}{r}2 \\ -2 \\ 3\end{array}\right]$
Calculate $\mathrm{AC}, \mathrm{BC}$ and $(\mathrm{A}+\mathrm{B}) \mathrm{C}$. Also, verify that $(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}$
Solution Now, $A+B=\left[\begin{array}{ccc}0 & 7 & 8 \\ -5 & 0 & 10 \\ 8 & -6 & 0\end{array}\right]$

So

$$
(A+B) C=\left[\begin{array}{rrr}
0 & 7 & 8 \\
-5 & 0 & 10 \\
8 & -6 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{r}
0-14+24 \\
-10+0+30 \\
16+12+0
\end{array}\right]=\left[\begin{array}{l}
10 \\
20 \\
28
\end{array}\right]
$$

Further

$$
\mathrm{AC}=\left[\begin{array}{ccc}
0 & 6 & 7 \\
-6 & 0 & 8 \\
7 & -8 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{r}
0-12+21 \\
-12+0+24 \\
14+16+0
\end{array}\right]=\left[\begin{array}{c}
9 \\
12 \\
30
\end{array}\right]
$$

and

$$
\mathrm{BC}=\left[\begin{array}{lll}
0 & 1 & 1 \\
1 & 0 & 2 \\
1 & 2 & 0
\end{array}\right]\left[\begin{array}{r}
2 \\
-2 \\
3
\end{array}\right]=\left[\begin{array}{l}
0-2+3 \\
2+0+6 \\
2-4+0
\end{array}\right]=\left[\begin{array}{c}
1 \\
8 \\
-2
\end{array}\right]
$$

So

$$
\mathrm{AC}+\mathrm{BC}=\left[\begin{array}{l}
9 \\
12 \\
30
\end{array}\right]+\left[\begin{array}{c}
1 \\
8 \\
-2
\end{array}\right]=\left[\begin{array}{l}
10 \\
20 \\
28
\end{array}\right]
$$

Clearly,

$$
(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}
$$

Example 18 If $A=\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]$, then show that $A^{3}-23 A-40 I=O$

Solution We have $A^{2}=A \cdot A=\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]\left[\begin{array}{rrr}1 & 2 & 3 \\ 3 & -2 & 1 \\ 4 & 2 & 1\end{array}\right]=\left[\begin{array}{lll}19 & 4 & 8 \\ 1 & 12 & 8 \\ 14 & 6 & 15\end{array}\right]$

So

$$
A^{3}=A A^{2}=\left[\begin{array}{rrr}
1 & 2 & 3 \\
3 & -2 & 1 \\
4 & 2 & 1
\end{array}\right]\left[\begin{array}{lcr}
19 & 4 & 8 \\
1 & 12 & 8 \\
14 & 6 & 15
\end{array}\right]=\left[\begin{array}{ccc}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]
$$

Now

$$
\begin{aligned}
\mathrm{A}^{3}-23 \mathrm{~A}-40 \mathrm{I} & =\left[\begin{array}{ccc}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]-23\left[\begin{array}{ccc}
1 & 2 & 3 \\
3 & -2 & 1 \\
4 & 2 & 1
\end{array}\right]-40\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
63 & 46 & 69 \\
69 & -6 & 23 \\
92 & 46 & 63
\end{array}\right]+\left[\begin{array}{ccc}
-23 & -46 & -69 \\
-69 & 46 & -23 \\
-92 & -46 & -23
\end{array}\right]+\left[\begin{array}{ccc}
-40 & 0 & 0 \\
0 & -40 & 0 \\
0 & 0 & -40
\end{array}\right] \\
& =\left[\begin{array}{ccc}
63-23-40 & 46-46+0 & 69-69+0 \\
69-69+0 & -6+46-40 & 23-23+0 \\
92-92+0 & 46-46+0 & 63-23-40
\end{array}\right] \\
& =\left[\begin{array}{lll}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right]=\mathrm{O}
\end{aligned}
$$

Example 19 In a legislative assembly election, a political group hired a public relations firm to promote its candidate in three ways: telephone, house calls, and letters. The cost per contact (in paise) is given in matrix A as

$$
\mathrm{A}=\left[\begin{array}{c}
\text { Cost per contact } \\
40 \\
100 \\
50
\end{array}\right] \begin{aligned}
& \text { Telephone } \\
& \text { Housecall } \\
& \text { Letter }
\end{aligned}
$$

The number of contacts of each type made in two cities X and Y is given by $\mathrm{B}=\left[\begin{array}{ccc}\text { Telephone } & \text { Housecall } & \text { Letter } \\ 1000 & 500 & 5000 \\ 3000 & 1000 & 10,000\end{array}\right] \rightarrow \mathrm{X}$. Find the total amount spent by the group in the two cities X and Y .

Solution We have

$$
\begin{aligned}
\mathrm{BA} & =\left[\begin{array}{c}
40,000+50,000+250,000 \\
120,000+100,000+500,000
\end{array}\right] \rightarrow \mathrm{X} \\
& =\left[\begin{array}{l}
340,000 \\
720,000
\end{array}\right] \rightarrow \mathrm{Y}
\end{aligned}
$$

So the total amount spent by the group in the two cities is 340,000 paise and 720,000 paise, i.e., ₹ 3400 and ₹ 7200 , respectively.

## EXERCISE 3.2

1. Let $\mathrm{A}=\left[\begin{array}{ll}2 & 4 \\ 3 & 2\end{array}\right], \mathrm{B}=\left[\begin{array}{rr}1 & 3 \\ -2 & 5\end{array}\right], \mathrm{C}=\left[\begin{array}{rr}-2 & 5 \\ 3 & 4\end{array}\right]$

Find each of the following:
(i) $\mathrm{A}+\mathrm{B}$
(ii) $\mathrm{A}-\mathrm{B}$
(iii) $3 \mathrm{~A}-\mathrm{C}$
(iv) AB
(v) BA
2. Compute the following:
(i) $\left[\begin{array}{cc}a & b \\ -b & a\end{array}\right]+\left[\begin{array}{ll}a & b \\ b & a\end{array}\right]$
(ii) $\left[\begin{array}{ll}a^{2}+b^{2} & b^{2}+c^{2} \\ a^{2}+c^{2} & a^{2}+b^{2}\end{array}\right]+\left[\begin{array}{cc}2 a b & 2 b c \\ -2 a c & -2 a b\end{array}\right]$
(iii) $\left[\begin{array}{rrr}-1 & 4 & -6 \\ 8 & 5 & 16 \\ 2 & 8 & 5\end{array}\right]+\left[\begin{array}{ccc}12 & 7 & 6 \\ 8 & 0 & 5 \\ 3 & 2 & 4\end{array}\right]$
(iv) $\left[\begin{array}{cc}\cos ^{2} x & \sin ^{2} x \\ \sin ^{2} x & \cos ^{2} x\end{array}\right]+\left[\begin{array}{cc}\sin ^{2} x & \cos ^{2} x \\ \cos ^{2} x & \sin ^{2} x\end{array}\right]$
3. Compute the indicated products.
(i) $\left[\begin{array}{rr}a & b \\ -b & a\end{array}\right]\left[\begin{array}{rr}a & -b \\ b & a\end{array}\right]$
(ii) $\left[\begin{array}{l}1 \\ 2 \\ 3\end{array}\right]\left[\begin{array}{lll}2 & 3 & 4\end{array}\right]$
(iii) $\left[\begin{array}{rr}1 & -2 \\ 2 & 3\end{array}\right]\left[\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right]$
(iv) $\left[\begin{array}{lll}2 & 3 & 4 \\ 3 & 4 & 5 \\ 4 & 5 & 6\end{array}\right]\left[\begin{array}{rrr}1 & -3 & 5 \\ 0 & 2 & 4 \\ 3 & 0 & 5\end{array}\right]$
(v) $\left[\begin{array}{rr}2 & 1 \\ 3 & 2 \\ -1 & 1\end{array}\right]\left[\begin{array}{rrr}1 & 0 & 1 \\ -1 & 2 & 1\end{array}\right]$
(vi) $\left[\begin{array}{rrr}3 & -1 & 3 \\ -1 & 0 & 2\end{array}\right]\left[\begin{array}{rr}2 & -3 \\ 1 & 0 \\ 3 & 1\end{array}\right]$
4. If $\mathrm{A}=\left[\begin{array}{rrr}1 & 2 & -3 \\ 5 & 0 & 2 \\ 1 & -1 & 1\end{array}\right], \mathrm{B}=\left[\begin{array}{rrr}3 & -1 & 2 \\ 4 & 2 & 5 \\ 2 & 0 & 3\end{array}\right]$ and $\mathrm{C}=\left[\begin{array}{rrr}4 & 1 & 2 \\ 0 & 3 & 2 \\ 1 & -2 & 3\end{array}\right]$, then compute $(\mathrm{A}+\mathrm{B})$ and $(\mathrm{B}-\mathrm{C})$. Also, verify that $\mathrm{A}+(\mathrm{B}-\mathrm{C})=(\mathrm{A}+\mathrm{B})-\mathrm{C}$.
5. If $\mathrm{A}=\left[\begin{array}{ccc}\frac{2}{3} & 1 & \frac{5}{3} \\ \frac{1}{3} & \frac{2}{3} & \frac{4}{3} \\ \frac{7}{3} & 2 & \frac{2}{3}\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}\frac{2}{5} & \frac{3}{5} & 1 \\ \frac{1}{5} & \frac{2}{5} & \frac{4}{5} \\ \frac{7}{5} & \frac{6}{5} & \frac{2}{5}\end{array}\right]$, then compute $3 A-5 B$.
6. Simplify $\cos \theta\left[\begin{array}{rr}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]+\sin \theta\left[\begin{array}{rr}\sin \theta & -\cos \theta \\ \cos \theta & \sin \theta\end{array}\right]$
7. Find X and Y , if
(i) $\mathrm{X}+\mathrm{Y}=\left[\begin{array}{ll}7 & 0 \\ 2 & 5\end{array}\right]$ and $\mathrm{X}-\mathrm{Y}=\left[\begin{array}{ll}3 & 0 \\ 0 & 3\end{array}\right]$
(ii) $2 \mathrm{X}+3 \mathrm{Y}=\left[\begin{array}{ll}2 & 3 \\ 4 & 0\end{array}\right]$ and $3 \mathrm{X}+2 \mathrm{Y}=\left[\begin{array}{rr}2 & -2 \\ -1 & 5\end{array}\right]$
8. Find X , if $\mathrm{Y}=\left[\begin{array}{ll}3 & 2 \\ 1 & 4\end{array}\right]$ and $2 \mathrm{X}+\mathrm{Y}=\left[\begin{array}{rr}1 & 0 \\ -3 & 2\end{array}\right]$
9. Find $x$ and $y$, if $2\left[\begin{array}{cc}1 & 3 \\ 0 & x\end{array}\right]+\left[\begin{array}{ll}y & 0 \\ 1 & 2\end{array}\right]=\left[\begin{array}{ll}5 & 6 \\ 1 & 8\end{array}\right]$
10. Solve the equation for $x, y, z$ and $t$, if $2\left[\begin{array}{ll}x & z \\ y & t\end{array}\right]+3\left[\begin{array}{rr}1 & -1 \\ 0 & 2\end{array}\right]=3\left[\begin{array}{ll}3 & 5 \\ 4 & 6\end{array}\right]$
11. If $x\left[\begin{array}{l}2 \\ 3\end{array}\right]+y\left[\begin{array}{c}-1 \\ 1\end{array}\right]=\left[\begin{array}{l}10 \\ 5\end{array}\right]$, find the values of $x$ and $y$.
12. Given $3\left[\begin{array}{ll}x & y \\ z & w\end{array}\right]=\left[\begin{array}{cc}x & 6 \\ -1 & 2 w\end{array}\right]+\left[\begin{array}{cc}4 & x+y \\ z+w & 3\end{array}\right]$, find the values of $x, y, z$ and $w$.
13. If $\mathrm{F}(x)=\left[\begin{array}{ccc}\cos x & -\sin x & 0 \\ \sin x & \cos x & 0 \\ 0 & 0 & 1\end{array}\right]$, show that $\mathrm{F}(x) \mathrm{F}(y)=\mathrm{F}(x+y)$.
14. Show that
(i) $\left[\begin{array}{rr}5 & -1 \\ 6 & 7\end{array}\right]\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right] \neq\left[\begin{array}{ll}2 & 1 \\ 3 & 4\end{array}\right]\left[\begin{array}{rr}5 & -1 \\ 6 & 7\end{array}\right]$
(ii) $\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]\left[\begin{array}{rrr}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right] \neq\left[\begin{array}{rrr}-1 & 1 & 0 \\ 0 & -1 & 1 \\ 2 & 3 & 4\end{array}\right]\left[\begin{array}{lll}1 & 2 & 3 \\ 0 & 1 & 0 \\ 1 & 1 & 0\end{array}\right]$
15. Find $A^{2}-5 A+6 I$, if $A=\left[\begin{array}{rrr}2 & 0 & 1 \\ 2 & 1 & 3 \\ 1 & -1 & 0\end{array}\right]$
16. If $\mathrm{A}=\left[\begin{array}{lll}1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3\end{array}\right]$, prove that $\mathrm{A}^{3}-6 \mathrm{~A}^{2}+7 \mathrm{~A}+2 \mathrm{I}=0$
17. If $\mathrm{A}=\left[\begin{array}{ll}3 & -2 \\ 4 & -2\end{array}\right]$ and $\mathrm{I}=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$, find $k$ so that $\mathrm{A}^{2}=k \mathrm{~A}-2 \mathrm{I}$
18. If $\mathrm{A}=\left[\begin{array}{cc}0 & -\tan \frac{\alpha}{2} \\ \tan \frac{\alpha}{2} & 0\end{array}\right]$ and I is the identity matrix of order 2 , show that

$$
I+A=(I-A)\left[\begin{array}{rr}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{array}\right]
$$

19. A trust fund has ₹ 30,000 that must be invested in two different types of bonds. The first bond pays $5 \%$ interest per year, and the second bond pays $7 \%$ interest per year. Using matrix multiplication, determine how to divide ₹ 30,000 among the two types of bonds. If the trust fund must obtain an annual total interest of:
(a) ₹ 1800
(b) ₹2000
20. The bookshop of a particular school has 10 dozen chemistry books, 8 dozen physics books, 10 dozen economics books. Their selling prices are ₹ 80 , ₹ 60 and ₹ 40 each respectively. Find the total amount the bookshop will receive from selling all the books using matrix algebra.
Assume X, Y, Z, W and P are matrices of order $2 \times n, 3 \times k, 2 \times p, n \times 3$ and $p \times k$, respectively. Choose the correct answer in Exercises 21 and 22.
21. The restriction on $n, k$ and $p$ so that $\mathrm{PY}+\mathrm{WY}$ will be defined are:
(A) $k=3, p=n$
(B) $k$ is arbitrary, $p=2$
(C) $p$ is arbitrary, $k=3$
(D) $k=2, p=3$
22. If $n=p$, then the order of the matrix $7 \mathrm{X}-5 \mathrm{Z}$ is:
(A) $p \times 2$
(B) $2 \times n$
(C) $n \times 3$
(D) $p \times n$

### 3.5. Transpose of a Matrix

In this section, we shall learn about transpose of a matrix and special types of matrices such as symmetric and skew symmetric matrices.

Definition 3 If $\mathrm{A}=\left[a_{i j}\right]$ be an $m \times n$ matrix, then the matrix obtained by interchanging the rows and columns of A is called the transpose of A . Transpose of the matrix A is denoted by $\mathrm{A}^{\prime}$ or $\left(\mathrm{A}^{\mathrm{T}}\right)$. In other words, if $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$, then $\mathrm{A}^{\prime}=\left[a_{j i}\right]_{n \times m}$. For example, if $\mathrm{A}=\left[\begin{array}{cc}3 & 5 \\ \sqrt{3} & 1 \\ 0 & \frac{-1}{5}\end{array}\right]_{3 \times 2}$, then $\mathrm{A}^{\prime}=\left[\begin{array}{ccc}3 & \sqrt{3} & 0 \\ 5 & 1 & \frac{-1}{5}\end{array}\right]_{2 \times 3}$

### 3.5.1 Properties of transpose of the matrices

We now state the following properties of transpose of matrices without proof. These may be verified by taking suitable examples.

For any matrices A and B of suitable orders, we have
(i) $\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$,
(ii) $(k \mathrm{~A})^{\prime}=k \mathrm{~A}^{\prime}$ (where $k$ is any constant)
(iii) $(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$
(iv) $(\mathrm{A} \mathrm{B})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$

Example 20 If $\mathrm{A}=\left[\begin{array}{lll}3 & \sqrt{3} & 2 \\ 4 & 2 & 0\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}2 & -1 & 2 \\ 1 & 2 & 4\end{array}\right]$, verify that
(i) $\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$,
(ii) $(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$,
(iii) $(k \mathrm{~B})^{\prime}=k \mathrm{~B}^{\prime}$, where $k$ is any constant.

## Solution

(i) We have

$$
\mathrm{A}=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right] \Rightarrow \mathrm{A}^{\prime}=\left[\begin{array}{cc}
3 & 4 \\
\sqrt{3} & 2 \\
2 & 0
\end{array}\right] \Rightarrow\left(\mathrm{A}^{\prime}\right)^{\prime}=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right]=\mathrm{A}
$$

Thus $\quad\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$
(ii) We have

$$
\mathrm{A}=\left[\begin{array}{lll}
3 & \sqrt{3} & 2 \\
4 & 2 & 0
\end{array}\right], \mathrm{B}=\left[\begin{array}{rrr}
2 & -1 & 2 \\
1 & 2 & 4
\end{array}\right] \Rightarrow \mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
5 & \sqrt{3}-1 & 4 \\
5 & 4 & 4
\end{array}\right]
$$

Therefore

$$
\begin{aligned}
(\mathrm{A}+\mathrm{B})^{\prime} & =\left[\begin{array}{cc}
5 & 5 \\
\sqrt{3}-1 & 4 \\
4 & 4
\end{array}\right] \\
\mathrm{A}^{\prime} & =\left[\begin{array}{cc}
3 & 4 \\
\sqrt{3} & 2 \\
2 & 0
\end{array}\right], \mathrm{B}^{\prime}=\left[\begin{array}{rr}
2 & 1 \\
-1 & 2 \\
2 & 4
\end{array}\right],
\end{aligned}
$$

Now

$$
A^{\prime}+B^{\prime}=\left[\begin{array}{cr}
5 & 5 \\
\sqrt{3}-1 & 4 \\
4 & 4
\end{array}\right]
$$

Thus

$$
(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}
$$

(iii) We have

Then

$$
k \mathrm{~B}=k\left[\begin{array}{rrr}
2 & -1 & 2 \\
1 & 2 & 4
\end{array}\right]=\left[\begin{array}{lrr}
2 k & -k & 2 k \\
k & 2 k & 4 k
\end{array}\right]
$$

$(k \mathrm{~B})^{\prime}=\left[\begin{array}{cc}2 k & k \\ -k & 2 k \\ 2 k & 4 k\end{array}\right]=k\left[\begin{array}{rr}2 & 1 \\ -1 & 2 \\ 2 & 4\end{array}\right]=k \mathrm{~B}^{\prime}$
Thus

$$
(k \mathrm{~B})^{\prime}=k \mathrm{~B}^{\prime}
$$

Example 21 If $\mathrm{A}=\left[\begin{array}{r}-2 \\ 4 \\ 5\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 3 & -6\end{array}\right]$, verify that $(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$.
Solution We have
then

$$
\begin{aligned}
\mathrm{A} & =\left[\begin{array}{r}
-2 \\
4 \\
5
\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}
1 & 3 & -6
\end{array}\right] \\
\mathrm{AB} & =\left[\begin{array}{r}
-2 \\
4 \\
5
\end{array}\right]\left[\begin{array}{lll}
1 & 3 & -6
\end{array}\right]=\left[\begin{array}{rrr}
-2 & -6 & 12 \\
4 & 12 & -24 \\
5 & 15 & -30
\end{array}\right]
\end{aligned}
$$

Now

$$
A^{\prime}=\left[\begin{array}{lll}
-2 & 4 & 5
\end{array}\right], B^{\prime}=\left[\begin{array}{r}
1 \\
3 \\
-6
\end{array}\right]
$$

$$
\mathrm{B}^{\prime} \mathrm{A}^{\prime}=\left[\begin{array}{r}
1 \\
3 \\
-6
\end{array}\right]\left[\begin{array}{lll}
-2 & 4 & 5
\end{array}\right]=\left[\begin{array}{ccc}
-2 & 4 & 5 \\
-6 & 12 & 15 \\
12 & -24 & -30
\end{array}\right]=(\mathrm{AB})^{\prime}
$$

Clearly
$(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$

### 3.6 Symmetric and Skew Symmetric Matrices

Definition 4 A square matrix $\mathrm{A}=\left[a_{i j}\right]$ is said to be symmetric if $\mathrm{A}^{\prime}=\mathrm{A}$, that is, $\left[a_{i j}\right]=\left[a_{j i}\right]$ for all possible values of $i$ and $j$.

For example $\mathrm{A}=\left[\begin{array}{ccr}\sqrt{3} & 2 & 3 \\ 2 & -1.5 & -1 \\ 3 & -1 & 1\end{array}\right]$ is a symmetric matrix as $\mathrm{A}^{\prime}=\mathrm{A}$
Definition 5 A square matrix $\mathrm{A}=\left[a_{i j}\right]$ is said to be skew symmetric matrix if $\mathrm{A}^{\prime}=-\mathrm{A}$, that is $a_{j i}=-a_{i j}$ for all possible values of $i$ and $j$. Now, if we put $i=j$, we have $a_{i i}=-a_{i i}$. Therefore $2 a_{i i}=0$ or $a_{i i}=0$ for all $i$ 's.

This means that all the diagonal elements of a skew symmetric matrix are zero.

For example, the matrix $\mathrm{B}=\left[\begin{array}{ccc}0 & e & f \\ -e & 0 & g \\ -f & -g & 0\end{array}\right]$ is a skew symmetric matrix as $\mathrm{B}^{\prime}=-\mathrm{B}$
Now, we are going to prove some results of symmetric and skew-symmetric matrices.

Theorem 1 For any square matrix A with real number entries, $\mathrm{A}+\mathrm{A}^{\prime}$ is a symmetric matrix and $A-A^{\prime}$ is a skew symmetric matrix.
Proof Let $\mathrm{B}=\mathrm{A}+\mathrm{A}^{\prime}$, then

$$
\begin{aligned}
\mathrm{B}^{\prime} & =\left(\mathrm{A}+\mathrm{A}^{\prime}\right)^{\prime} \\
& =\mathrm{A}^{\prime}+\left(\mathrm{A}^{\prime}\right)^{\prime}\left(\text { as }(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}\right) \\
& =\mathrm{A}^{\prime}+\mathrm{A}\left(\text { as }\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}\right) \\
& =\mathrm{A}+\mathrm{A}^{\prime}(\text { as } \mathrm{A}+\mathrm{B}=\mathrm{B}+\mathrm{A}) \\
& =\mathrm{B}
\end{aligned}
$$

Therefore

$$
\mathrm{B}=\mathrm{A}+\mathrm{A}^{\prime} \text { is a symmetric matrix }
$$

Now let

$$
\begin{aligned}
\mathrm{C} & =\mathrm{A}-\mathrm{A}^{\prime} \\
\mathrm{C}^{\prime} & =\left(\mathrm{A}-\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}^{\prime}-\left(\mathrm{A}^{\prime}\right)^{\prime} \quad(\text { Why? }) \\
& =\mathrm{A}^{\prime}-\mathrm{A} \quad(\text { Why? }) \\
& =-\left(\mathrm{A}-\mathrm{A}^{\prime}\right)=-\mathrm{C}
\end{aligned}
$$

Therefore
$\mathrm{C}=\mathrm{A}-\mathrm{A}^{\prime}$ is a skew symmetric matrix.
Theorem 2 Any square matrix can be expressed as the sum of a symmetric and a skew symmetric matrix.
Proof Let A be a square matrix, then we can write

$$
\mathrm{A}=\frac{1}{2}\left(\mathrm{~A}+\mathrm{A}^{\prime}\right)+\frac{1}{2}\left(\mathrm{~A}-\mathrm{A}^{\prime}\right)
$$

From the Theorem 1, we know that $\left(\mathrm{A}+\mathrm{A}^{\prime}\right)$ is a symmetric matrix and $\left(\mathrm{A}-\mathrm{A}^{\prime}\right)$ is a skew symmetric matrix. Since for any matrix $\mathrm{A},(k \mathrm{~A})^{\prime}=k \mathrm{~A}^{\prime}$, it follows that $\frac{1}{2}\left(\mathrm{~A}+\mathrm{A}^{\prime}\right)$
is symmetric matrix and $\frac{1}{2}\left(A-A^{\prime}\right)$ is skew symmetric matrix. Thus, any square matrix can be expressed as the sum of a symmetric and a skew symmetric matrix.
Example 22 Express the matrix $B=\left[\begin{array}{rrr}2 & -2 & -4 \\ -1 & 3 & 4 \\ 1 & -2 & -3\end{array}\right]$ as the sum of a symmetric and a skew symmetric matrix.
Solution Here

$$
\mathrm{B}^{\prime}=\left[\begin{array}{rrr}
2 & -1 & 1 \\
-2 & 3 & -2 \\
-4 & 4 & -3
\end{array}\right]
$$

Let

$$
\begin{aligned}
& \mathrm{P}=\frac{1}{2}\left(\mathrm{~B}+\mathrm{B}^{\prime}\right)=\frac{1}{2}\left[\begin{array}{rrr}
4 & -3 & -3 \\
-3 & 6 & 2 \\
-3 & 2 & -6
\end{array}\right]=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right], \\
& \mathrm{P}^{\prime}=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right]=\mathrm{P}
\end{aligned}
$$

Thus $\mathrm{P}=\frac{1}{2}\left(\mathrm{~B}+\mathrm{B}^{\prime}\right)$ is a symmetric matrix.

Also, let

$$
Q=\frac{1}{2}\left(B-B^{\prime}\right)=\frac{1}{2}\left[\begin{array}{rrr}
0 & -1 & -5 \\
1 & 0 & 6 \\
5 & -6 & 0
\end{array}\right]=\left[\begin{array}{ccc}
0 & \frac{-1}{2} & \frac{-5}{2} \\
\frac{1}{2} & 0 & 3 \\
\frac{5}{2} & -3 & 0
\end{array}\right]
$$

Then

$$
\mathrm{Q}^{\prime}=\left[\begin{array}{ccc}
0 & \frac{1}{2} & \frac{5}{3} \\
\frac{-1}{2} & 0 & -3 \\
\frac{-5}{2} & 3 & 0
\end{array}\right]=-\mathrm{Q}
$$

Thus $\mathrm{Q}=\frac{1}{2}\left(\mathrm{~B}-\mathrm{B}^{\prime}\right)$ is a skew symmetric matrix.

Now

$$
\mathrm{P}+\mathrm{Q}=\left[\begin{array}{ccc}
2 & \frac{-3}{2} & \frac{-3}{2} \\
\frac{-3}{2} & 3 & 1 \\
\frac{-3}{2} & 1 & -3
\end{array}\right]+\left[\begin{array}{ccc}
0 & \frac{-1}{2} & \frac{-5}{2} \\
\frac{1}{2} & 0 & 3 \\
\frac{5}{2} & -3 & 0
\end{array}\right]=\left[\begin{array}{rrr}
2 & -2 & -4 \\
-1 & 3 & 4 \\
1 & -2 & -3
\end{array}\right]=\mathrm{B}
$$

Thus, B is represented as the sum of a symmetric and a skew symmetric matrix.

## EXERCISE 3.3

1. Find the transpose of each of the following matrices:
(i) $\left[\begin{array}{c}5 \\ \frac{1}{2} \\ -1\end{array}\right]$
(ii) $\left[\begin{array}{rr}1 & -1 \\ 2 & 3\end{array}\right]$
(iii) $\left[\begin{array}{ccc}-1 & 5 & 6 \\ \sqrt{3} & 5 & 6 \\ 2 & 3 & -1\end{array}\right]$
2. If $\mathrm{A}=\left[\begin{array}{rrr}-1 & 2 & 3 \\ 5 & 7 & 9 \\ -2 & 1 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}-4 & 1 & -5 \\ 1 & 2 & 0 \\ 1 & 3 & 1\end{array}\right]$, then verify that
(i) $(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$,
(ii) $(\mathrm{A}-\mathrm{B})^{\prime}=\mathrm{A}^{\prime}-\mathrm{B}^{\prime}$
3. If $\mathrm{A}^{\prime}=\left[\begin{array}{rr}3 & 4 \\ -1 & 2 \\ 0 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}-1 & 2 & 1 \\ 1 & 2 & 3\end{array}\right]$, then verify that
(i) $(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$
(ii) $(\mathrm{A}-\mathrm{B})^{\prime}=\mathrm{A}^{\prime}-\mathrm{B}^{\prime}$
4. If $\mathrm{A}^{\prime}=\left[\begin{array}{cc}-2 & 3 \\ 1 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rr}-1 & 0 \\ 1 & 2\end{array}\right]$, then find $(\mathrm{A}+2 \mathrm{~B})^{\prime}$
5. For the matrices $A$ and $B$, verify that $(A B)^{\prime}=B^{\prime} A^{\prime}$, where
(i) $\mathrm{A}=\left[\begin{array}{r}1 \\ -4 \\ 3\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}-1 & 2 & 1\end{array}\right]$
(ii) $\mathrm{A}=\left[\begin{array}{l}0 \\ 1 \\ 2\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 5 & 7\end{array}\right]$
6. If (i) $\mathrm{A}=\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right]$, then verify that $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$
(ii) If $\mathrm{A}=\left[\begin{array}{cc}\sin \alpha & \cos \alpha \\ -\cos \alpha & \sin \alpha\end{array}\right]$, then verify that $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$
7. (i) Show that the matrix $A=\left[\begin{array}{rrr}1 & -1 & 5 \\ -1 & 2 & 1 \\ 5 & 1 & 3\end{array}\right]$ is a symmetric matrix.
(ii) Show that the matrix $\mathrm{A}=\left[\begin{array}{rrr}0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{array}\right]$ is a skew symmetric matrix.
8. For the matrix $\mathrm{A}=\left[\begin{array}{ll}1 & 5 \\ 6 & 7\end{array}\right]$, verify that
(i) $\left(\mathrm{A}+\mathrm{A}^{\prime}\right)$ is a symmetric matrix
(ii) $\left(\mathrm{A}-\mathrm{A}^{\prime}\right)$ is a skew symmetric matrix
9. Find $\frac{1}{2}\left(\mathrm{~A}+\mathrm{A}^{\prime}\right)$ and $\frac{1}{2}\left(\mathrm{~A}-\mathrm{A}^{\prime}\right)$, when $\mathrm{A}=\left[\begin{array}{rrr}0 & a & b \\ -a & 0 & c \\ -b & -c & 0\end{array}\right]$
10. Express the following matrices as the sum of a symmetric and a skew symmetric matrix:
(i) $\left[\begin{array}{rr}3 & 5 \\ 1 & -1\end{array}\right]$
(ii) $\left[\begin{array}{rrr}6 & -2 & 2 \\ -2 & 3 & -1 \\ 2 & -1 & 3\end{array}\right]$
(iii) $\left[\begin{array}{rrr}3 & 3 & -1 \\ -2 & -2 & 1 \\ -4 & -5 & 2\end{array}\right]$
(iv) $\left[\begin{array}{rr}1 & 5 \\ -1 & 2\end{array}\right]$

Choose the correct answer in the Exercises 11 and 12.
11. If $\mathrm{A}, \mathrm{B}$ are symmetric matrices of same order, then $\mathrm{AB}-\mathrm{BA}$ is a
(A) Skew symmetric matrix
(B) Symmetric matrix
(C) Zero matrix
(D) Identity matrix
12. If $A=\left[\begin{array}{cc}\cos \alpha & -\sin \alpha \\ \sin \alpha & \cos \alpha\end{array}\right]$, and $A+A^{\prime}=I$, then the value of $\alpha$ is
(A) $\frac{\pi}{6}$
(B) $\frac{\pi}{3}$
(C) $\pi$
(D) $\frac{3 \pi}{2}$

### 3.7 Invertible Matrices

Definition 6 If A is a square matrix of order $m$, and if there exists another square matrix B of the same order $m$, such that $\mathrm{AB}=\mathrm{BA}=\mathrm{I}$, then B is called the inverse matrix of A and it is denoted by $\mathrm{A}^{-1}$. In that case A is said to be invertible.

For example, let

$$
\mathrm{A}=\left[\begin{array}{ll}
2 & 3 \\
1 & 2
\end{array}\right] \text { and } \mathrm{B}=\left[\begin{array}{rr}
2 & -3 \\
-1 & 2
\end{array}\right] \text { be two matrices. }
$$

Now

$$
\begin{aligned}
\mathrm{AB} & =\left[\begin{array}{ll}
2 & 3 \\
1 & 2
\end{array}\right]\left[\begin{array}{rr}
2 & -3 \\
-1 & 2
\end{array}\right] \\
& =\left[\begin{array}{ll}
4-3 & -6+6 \\
2-2 & -3+4
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\mathrm{I}
\end{aligned}
$$

Also

$$
\mathrm{BA}=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\mathrm{I} \text {. Thus } \mathrm{B} \text { is the inverse of } \mathrm{A} \text {, in other }
$$

words $\mathrm{B}=\mathrm{A}^{-1}$ and A is inverse of B , i.e., $\mathrm{A}=\mathrm{B}^{-1}$

## Note

1. A rectangular matrix does not possess inverse matrix, since for products $B A$ and AB to be defined and to be equal, it is necessary that matrices A and B should be square matrices of the same order.
2. If B is the inverse of A , then A is also the inverse of B .

Theorem 3 (Uniqueness of inverse) Inverse of a square matrix, if it exists, is unique. Proof Let $\mathrm{A}=\left[a_{i j}\right]$ be a square matrix of order $m$. If possible, let B and C be two inverses of A . We shall show that $\mathrm{B}=\mathrm{C}$.

Since B is the inverse of A

$$
\begin{equation*}
A B=B A=I \tag{1}
\end{equation*}
$$

Since C is also the inverse of A

Thus
Theorem 4 If $A$ and $B$ are invertible matrices of the same order, then $(A B)^{-1}=B^{-1} A^{-1}$. Proof From the definition of inverse of a matrix, we have

$$
(\mathrm{AB})(\mathrm{AB})^{-1}=1
$$

or

$$
\mathrm{A}^{-1}(\mathrm{AB})(\mathrm{AB})^{-1}=\mathrm{A}^{-1} \mathrm{I}
$$

(Pre multiplying both sides by $\mathrm{A}^{-1}$ )
or

$$
\left(A^{-1} A\right) B(A B)^{-1}=A^{-1} \quad\left(\text { Since } A^{-1} I=A^{-1}\right)
$$

or

$$
\mathrm{IB}(\mathrm{AB})^{-1}=\mathrm{A}^{-1}
$$

or

$$
\mathrm{B}(\mathrm{AB})^{-1}=\mathrm{A}^{-1}
$$

or

$$
B^{-1} B(A B)^{-1}=B^{-1} A^{-1}
$$

or

$$
\mathrm{I}(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}
$$

Hence

$$
(\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1}
$$

## EXERCISE 3.4

1. Matrices $A$ and $B$ will be inverse of each other only if
(A) $\mathrm{AB}=\mathrm{BA}(\mathrm{B}) \mathrm{AB}=\mathrm{BA}=0$
(C) $\mathrm{AB}=0, \mathrm{BA}=\mathrm{I}(\mathrm{D}) \mathrm{AB}=\mathrm{BA}=\mathrm{I}$

## Miscellaneous Examples

Example 23 If $\mathrm{A}=\left[\begin{array}{cc}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$, then prove that $\mathrm{A}^{n}=\left[\begin{array}{cc}\cos n \theta & \sin n \theta \\ -\sin n \theta & \cos n \theta\end{array}\right], n \in \mathbf{N}$.
Solution We shall prove the result by using principle of mathematical induction.
We have $\quad \mathrm{P}(n)$ : If $\mathrm{A}=\left[\begin{array}{cc}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$, then $\mathrm{A}^{n}=\left[\begin{array}{cc}\cos n \theta & \sin n \theta \\ -\sin n \theta & \cos n \theta\end{array}\right], n \in \mathbf{N}$

$$
P(1): A=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right] \text {, so } A^{1}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right]
$$

Therefore, the result is true for $n=1$.
Let the result be true for $n=k$. So

$$
\mathrm{P}(k): \mathrm{A}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right], \text { then } \mathrm{A}^{k}=\left[\begin{array}{cc}
\cos k \theta & \sin k \theta \\
-\sin k \theta & \cos k \theta
\end{array}\right]
$$

Now, we prove that the result holds for $n=k+1$

Now

$$
\begin{aligned}
\mathrm{A}^{k+1} & =\mathrm{A} \cdot \mathrm{~A}^{k}=\left[\begin{array}{cc}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right]\left[\begin{array}{cc}
\cos k \theta & \sin k \theta \\
-\sin k \theta & \cos k \theta
\end{array}\right] \\
& =\left[\begin{array}{cc}
\cos \theta \cos k \theta-\sin \theta \sin k \theta & \cos \theta \sin k \theta+\sin \theta \cos k \theta \\
-\sin \theta \cos k \theta+\cos \theta \sin k \theta & -\sin \theta \sin k \theta+\cos \theta \cos k \theta
\end{array}\right] \\
& =\left[\begin{array}{cc}
\cos (\theta+k \theta) & \sin (\theta+k \theta) \\
-\sin (\theta+k \theta) & \cos (\theta+k \theta)
\end{array}\right]=\left[\begin{array}{cc}
\cos (k+1) \theta & \sin (k+1) \theta \\
-\sin (k+1) \theta & \cos (k+1) \theta
\end{array}\right]
\end{aligned}
$$

Therefore, the result is true for $n=k+1$. Thus by principle of mathematical induction, we have $A^{n}=\left[\begin{array}{cc}\cos n \theta & \sin n \theta \\ -\sin n \theta & \cos n \theta\end{array}\right]$, holds for all natural numbers.

Example 24 If A and B are symmetric matrices of the same order, then show that AB is symmetric if and only if A and B commute, that is $\mathrm{AB}=\mathrm{BA}$.

Solution Since A and B are both symmetric matrices, therefore $\mathrm{A}^{\prime}=\mathrm{A}$ and $\mathrm{B}^{\prime}=\mathrm{B}$.

Let $\quad \mathrm{AB}$ be symmetric, then $(\mathrm{AB})^{\prime}=\mathrm{AB}$
But
$(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}=\mathrm{BA}$ (Why?)
Therefore
$\mathrm{BA}=\mathrm{AB}$
Conversely, if $A B=B A$, then we shall show that $A B$ is symmetric.
Now

$$
\begin{aligned}
(\mathrm{AB})^{\prime} & =\mathrm{B}^{\prime} \mathrm{A}^{\prime} \\
& =\mathrm{BA}(\text { as } \mathrm{A} \text { and } \mathrm{B} \text { are symmetric }) \\
& =\mathrm{AB}
\end{aligned}
$$

Hence AB is symmetric.
Example 25 Let $\mathrm{A}=\left[\begin{array}{rr}2 & -1 \\ 3 & 4\end{array}\right], \mathrm{B}=\left[\begin{array}{ll}5 & 2 \\ 7 & 4\end{array}\right], \mathrm{C}=\left[\begin{array}{ll}2 & 5 \\ 3 & 8\end{array}\right]$. Find a matrix D such that $\mathrm{CD}-\mathrm{AB}=\mathrm{O}$.

Solution Since A, B, C are all square matrices of order 2, and CD - AB is well defined, D must be a square matrix of order 2 .

Let

$$
\begin{aligned}
& \mathrm{D}=\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right] \text {. Then } \mathrm{CD}-\mathrm{AB}=0 \text { gives } \\
& {\left[\begin{array}{ll}
2 & 5 \\
3 & 8
\end{array}\right]\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]-\left[\begin{array}{rr}
2 & -1 \\
3 & 4
\end{array}\right]\left[\begin{array}{ll}
5 & 2 \\
7 & 4
\end{array}\right]=\mathrm{O}}
\end{aligned}
$$

or

$$
\left[\begin{array}{ll}
2 a+5 c & 2 b+5 d \\
3 a+8 c & 3 b+8 d
\end{array}\right]-\left[\begin{array}{ll}
3 & 0 \\
43 & 22
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]
$$

or

$$
\left[\begin{array}{cc}
2 a+5 c-3 & 2 b+5 d \\
3 a+8 c-43 & 3 b+8 d-22
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]
$$

By equality of matrices, we get

$$
\begin{array}{r}
2 a+5 c-3=0 \\
3 a+8 c-43=0 \\
2 b+5 d=0 \\
3 b+8 d-22=0 \tag{4}
\end{array}
$$

and
Solving (1) and (2), we get $a=-191, c=77$. Solving (3) and (4), we get $b=-110$, $d=44$.

Therefore

$$
\mathrm{D}=\left[\begin{array}{ll}
a & b \\
c & d
\end{array}\right]=\left[\begin{array}{cc}
-191 & -110 \\
77 & 44
\end{array}\right]
$$

## Miscellaneous Exercise on Chapter 3

1. If A and B are symmetric matrices, prove that $\mathrm{AB}-\mathrm{BA}$ is a skew symmetric matrix.
2. Show that the matrix $B^{\prime} A B$ is symmetric or skew symmetric according as $A$ is symmetric or skew symmetric.
3. Find the values of $x, y, z$ if the matrix $\mathrm{A}=\left[\begin{array}{ccc}0 & 2 y & z \\ x & y & -z \\ x & -y & z\end{array}\right]$ satisfy the equation $\mathrm{A}^{\prime} \mathrm{A}=\mathrm{I}$.
4. For what values of $x$ : $\left[\begin{array}{lll}1 & 2 & 1\end{array}\right]\left[\begin{array}{lll}1 & 2 & 0 \\ 2 & 0 & 1 \\ 1 & 0 & 2\end{array}\right]\left[\begin{array}{l}0 \\ 2 \\ x\end{array}\right]=\mathrm{O}$ ?
5. If $A=\left[\begin{array}{rr}3 & 1 \\ -1 & 2\end{array}\right]$, show that $A^{2}-5 A+7 I=0$.
6. Find $x$, if $\left[\begin{array}{lll}x & -5 & -1\end{array}\right]\left[\begin{array}{lll}1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 0 & 3\end{array}\right]\left[\begin{array}{l}x \\ 4 \\ 1\end{array}\right]=\mathrm{O}$
7. A manufacturer produces three products $x, y, z$ which he sells in two markets. Annual sales are indicated below:

| Market | Products |  |  |
| :---: | :--- | :--- | :--- |
| I | 10,000 | 2,000 | 18,000 |
| II | 6,000 | 20,000 | 8,000 |

(a) If unit sale prices of $x, y$ and $z$ are $₹ 2.50$, $₹ 1.50$ and $₹ 1.00$, respectively, find the total revenue in each market with the help of matrix algebra.
(b) If the unit costs of the above three commodities are ₹ 2.00, ₹ 1.00 and 50 paise respectively. Find the gross profit.
8. Find the matrix $X$ so that $X\left[\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6\end{array}\right]=\left[\begin{array}{rrr}-7 & -8 & -9 \\ 2 & 4 & 6\end{array}\right]$

Choose the correct answer in the following questions:
9. If $\mathrm{A}=\begin{array}{cc}\alpha & \beta \\ \gamma & -\alpha\end{array}$ is such that $\mathrm{A}^{2}=\mathrm{I}$, then
(A) $1+\alpha^{2}+\beta \gamma=0$
(B) $1-\alpha^{2}+\beta \gamma=0$
(C) $1-\alpha^{2}-\beta \gamma=0$
(D) $1+\alpha^{2}-\beta \gamma=0$
10. If the matrix A is both symmetric and skew symmetric, then
(A) A is a diagonal matrix
(B) A is a zero matrix
(C) A is a square matrix
(D) None of these
11. If $A$ is square matrix such that $A^{2}=A$, then $(I+A)^{3}-7 A$ is equal to
(A) A
(B) $\mathrm{I}-\mathrm{A}$
(C) I
(D) 3 A

## Summary

- A matrix is an ordered rectangular array of numbers or functions.
- A matrix having $m$ rows and $n$ columns is called a matrix of order $m \times n$.
- $\left[a_{i j}\right]_{m \times 1}$ is a column matrix.
- $\left[a_{i j}\right]_{1 \times n}$ is a row matrix.
- An $m \times n$ matrix is a square matrix if $m=n$.
- $\mathrm{A}=\left[a_{i j}\right]_{m \times m}$ is a diagonal matrix if $a_{i j}=0$, when $i \neq j$.
- $\mathrm{A}=\left[a_{i j}\right]_{n \times n}$ is a scalar matrix if $a_{i j}=0$, when $i \neq j, a_{i j}=k$, ( $k$ is some constant), when $i=j$.
- $\mathrm{A}=\left[a_{i j}\right]_{n \times n}$ is an identity matrix, if $a_{i j}=1$, when $i=j, a_{i j}=0$, when $i \neq j$.
- A zero matrix has all its elements as zero.
- $\mathrm{A}=\left[a_{i j}\right]=\left[b_{i j}\right]=\mathrm{B}$ if (i) A and B are of same order, (ii) $a_{i j}=b_{i j}$ for all possible values of $i$ and $j$.
- $k \mathrm{~A}=k\left[a_{i j}\right]_{m \times n}=\left[k\left(a_{i j}\right)\right]_{m \times n}$
- $-\mathrm{A}=(-1) \mathrm{A}$
- $\mathrm{A}-\mathrm{B}=\mathrm{A}+(-1) \mathrm{B}$
- $\mathrm{A}+\mathrm{B}=\mathrm{B}+\mathrm{A}$
- $(\mathrm{A}+\mathrm{B})+\mathrm{C}=\mathrm{A}+(\mathrm{B}+\mathrm{C})$, where $\mathrm{A}, \mathrm{B}$ and C are of same order.
- $k(\mathrm{~A}+\mathrm{B})=k \mathrm{~A}+k \mathrm{~B}$, where A and B are of same order, $k$ is constant.
- $(k+l) \mathrm{A}=k \mathrm{~A}+l \mathrm{~A}$, where $k$ and $l$ are constant.
- If $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ and $\mathrm{B}=\left[b_{j k}\right]_{n \times p}$, then $\mathrm{AB}=\mathrm{C}=\left[c_{i k}\right]_{m \times p}$, where $c_{i k}=\sum_{j=1}^{n} a_{i j} b_{j k}$
- (i) $\mathrm{A}(\mathrm{BC})=(\mathrm{AB}) \mathrm{C}$, (ii) $\mathrm{A}(\mathrm{B}+\mathrm{C})=\mathrm{AB}+\mathrm{AC}$, (iii) $(\mathrm{A}+\mathrm{B}) \mathrm{C}=\mathrm{AC}+\mathrm{BC}$
- If $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$, then $\mathrm{A}^{\prime}$ or $\mathrm{A}^{\mathrm{T}}=\left[a_{j i}\right]_{n \times m}$
- (i) $\left(\mathrm{A}^{\prime}\right)^{\prime}=\mathrm{A}$, (ii) $(k \mathrm{~A})^{\prime}=k \mathrm{~A}^{\prime}$, (iii) $(\mathrm{A}+\mathrm{B})^{\prime}=\mathrm{A}^{\prime}+\mathrm{B}^{\prime}$, (iv) $(\mathrm{AB})^{\prime}=\mathrm{B}^{\prime} \mathrm{A}^{\prime}$
- A is a symmetric matrix if $\mathrm{A}^{\prime}=\mathrm{A}$.
- A is a skew symmetric matrix if $\mathrm{A}^{\prime}=-\mathrm{A}$.
- Any square matrix can be represented as the sum of a symmetric and a skew symmetric matrix.
- If $A$ and $B$ are two square matrices such that $A B=B A=I$, then $B$ is the inverse matrix of $A$ and is denoted by $A^{-1}$ and $A$ is the inverse of $B$.
- Inverse of a square matrix, if it exists, is unique.

