## DETERMINANTS

## All Mathematical truths are relative and conditional. - C.P. STEINMETZ

### 4.1 Introduction

In the previous chapter, we have studied about matrices and algebra of matrices. We have also learnt that a system of algebraic equations can be expressed in the form of matrices. This means, a system of linear equations like

$$
\begin{aligned}
& a_{1} x+b_{1} y=c_{1} \\
& a_{2} x+b_{2} y=c_{2}
\end{aligned}
$$

can be represented as $\left[\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2}\end{array}\right]\left[\begin{array}{l}x \\ y\end{array}\right]=\left[\begin{array}{l}c_{1} \\ c_{2}\end{array}\right]$. Now, this system of equations has a unique solution or not, is determined by the number $a_{1} b_{2}-a_{2} b_{1}$. (Recall that if $\frac{a_{1}}{a_{2}} \neq \frac{b_{1}}{b_{2}}$ or, $a_{1} b_{2}-a_{2} b_{1} \neq 0$, then the system of linear
![](https://cdn.mathpix.com/cropped/2025_07_21_87c5502490a156e1f0f9g-01.jpg?height=535&width=410&top_left_y=834&top_left_x=1059)
P.S. Laplace (1749-1827) equations has a unique solution). The number $a_{1} b_{2}-a_{2} b_{1}$ which determines uniqueness of solution is associated with the matrix $\mathrm{A}=\left[\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2}\end{array}\right]$ and is called the determinant of A or det A. Determinants have wide applications in Engineering, Science, Economics, Social Science, etc.

In this chapter, we shall study determinants up to order three only with real entries. Also, we will study various properties of determinants, minors, cofactors and applications of determinants in finding the area of a triangle, adjoint and inverse of a square matrix, consistency and inconsistency of system of linear equations and solution of linear equations in two or three variables using inverse of a matrix.

### 4.2 Determinant

To every square matrix $\mathrm{A}=\left[a_{i j}\right]$ of order $n$, we can associate a number (real or complex) called determinant of the square matrix A, where $a_{i j}=(i, j)^{\text {th }}$ element of A.

This may be thought of as a function which associates each square matrix with a unique number (real or complex). If M is the set of square matrices, K is the set of numbers (real or complex) and $f: \mathrm{M} \rightarrow \mathrm{K}$ is defined by $f(\mathrm{~A})=k$, where $\mathrm{A} \in \mathrm{M}$ and $k \in \mathrm{~K}$, then $f(\mathrm{~A})$ is called the determinant of A . It is also denoted by $|\mathrm{A}|$ or $\operatorname{det} \mathrm{A}$ or $\Delta$.

If $\mathrm{A}=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$, then determinant of A is written as $|\mathrm{A}|=\left|\begin{array}{ll}a & b \\ c & d\end{array}\right|=\operatorname{det}(\mathrm{A})$
Remarks
(i) For matrix $\mathrm{A},|\mathrm{A}|$ is read as determinant of A and not modulus of A .
(ii) Only square matrices have determinants.

### 4.2.1 Determinant of a matrix of order one

Let $\mathrm{A}=[a]$ be the matrix of order 1, then determinant of A is defined to be equal to $a$

### 4.2.2 Determinant of a matrix of order two

Let

$$
\mathrm{A}=\left[\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right] \text { be a matrix of order } 2 \times 2
$$

then the determinant of A is defined as:

$$
\operatorname{det}(\mathrm{A})=|\mathrm{A}|=\Delta=\left|\begin{array}{lll}
a_{11} & & a_{12} \\
& \ddots & \\
a_{21} & & a_{22}
\end{array}\right|=a_{11} a_{22}-a_{21} a_{12}
$$

Example 1 Evaluate $\left|\begin{array}{rr}2 & 4 \\ -1 & 2\end{array}\right|$.
Solution We have $\left|\begin{array}{cc}2 & 4 \\ -1 & 2\end{array}\right|=2(2)-4(-1)=4+4=8$.
Example 2 Evaluate $\left|\begin{array}{cc}x & x+1 \\ x-1 & x\end{array}\right|$
Solution We have

$$
\left|\begin{array}{cc}
x & x+1 \\
x-1 & x
\end{array}\right|=x(x)-(x+1)(x-1)=x^{2}-\left(x^{2}-1\right)=x^{2}-x^{2}+1=1
$$

### 4.2.3 Determinant of a matrix of order $3 \times 3$

Determinant of a matrix of order three can be determined by expressing it in terms of second order determinants. This is known as expansion of a determinant along a row (or a column). There are six ways of expanding a determinant of order

3 corresponding to each of three rows ( $\mathrm{R}_{1}, \mathrm{R}_{2}$ and $\mathrm{R}_{3}$ ) and three columns ( $\mathrm{C}_{1}, \mathrm{C}_{2}$ and $\mathrm{C}_{3}$ ) giving the same value as shown below.

Consider the determinant of square matrix $\mathrm{A}=\left[a_{i j}\right]_{3 \times 3}$
i.e.,

$$
|\mathrm{A}|=\left|\begin{array}{lll}
\boldsymbol{a}_{\mathbf{1 1}} & \boldsymbol{a}_{\mathbf{1 2}} & \boldsymbol{a}_{\mathbf{1 3}} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|
$$

## Expansion along first $\operatorname{Row}\left(\mathbf{R}_{\mathbf{1}}\right)$

Step 1 Multiply first element $a_{11}$ of $\mathrm{R}_{1}$ by $(-1)^{(1+1)}\left[(-1)^{\text {sum of suffixes in } a_{11}}\right]$ and with the second order determinant obtained by deleting the elements of first row $\left(R_{1}\right)$ and first column $\left(\mathrm{C}_{1}\right)$ of $|\mathrm{A}|$ as $a_{11}$ lies in $\mathrm{R}_{1}$ and $\mathrm{C}_{1}$,
i.e.,

$$
(-1)^{1+1} a_{11}\left|\begin{array}{ll}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{array}\right|
$$

Step 2 Multiply 2nd element $a_{12}$ of $\mathrm{R}_{1}$ by $(-1)^{1+2}\left[(-1)^{\text {sum of suffixes in } a_{12}}\right]$ and the second order determinant obtained by deleting elements of first row ( $\mathrm{R}_{1}$ ) and 2nd column ( $\mathrm{C}_{2}$ ) of | A | as $a_{12}$ lies in $\mathrm{R}_{1}$ and $\mathrm{C}_{2}$,
i.e.,

$$
(-1)^{1+2} a_{12}\left|\begin{array}{ll}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{array}\right|
$$

Step 3 Multiply third element $a_{13}$ of $\mathrm{R}_{1}$ by $(-1)^{1+3}\left[(-1)^{\text {sum of suffixes in } a_{13}}\right]$ and the second order determinant obtained by deleting elements of first row $\left(\mathrm{R}_{1}\right)$ and third column $\left(\mathrm{C}_{3}\right)$ of | A | as $a_{13}$ lies in $\mathrm{R}_{1}$ and $\mathrm{C}_{3}$,
i.e.,

$$
(-1)^{1+3} a_{13}\left|\begin{array}{ll}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}\right|
$$

Step 4 Now the expansion of determinant of A, that is, $|\mathrm{A}|$ written as sum of all three terms obtained in steps 1, 2 and 3 above is given by

$$
\begin{aligned}
\operatorname{det} \mathrm{A}=|\mathrm{A}|= & (-1)^{1+1} a_{11}\left|\begin{array}{ll}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{array}\right|+(-1)^{1+2} a_{12}\left|\begin{array}{ll}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{array}\right| \\
& +(-1)^{1+3} a_{13}\left|\begin{array}{ll}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}\right|
\end{aligned}
$$

or

$$
\begin{aligned}
|\mathrm{A}|= & a_{11}\left(a_{22} a_{33}-a_{32} a_{23}\right)-a_{12}\left(a_{21} a_{33}-a_{31} a_{23}\right) \\
& +a_{13}\left(a_{21} a_{32}-a_{31} a_{22}\right)
\end{aligned}
$$

$$
\begin{align*}
= & a_{11} a_{22} a_{33}-a_{11} a_{32} a_{23}-a_{12} a_{21} a_{33}+a_{12} a_{31} a_{23}+a_{13} a_{21} a_{32} \\
& -a_{13} a_{31} a_{22} \tag{1}
\end{align*}
$$

Note We shall apply all four steps together.

## Expansion along second row ( $\mathbf{R}_{\mathbf{2}}$ )

$$
|\mathrm{A}|=\left|\begin{array}{lll}
\mathrm{a}_{11} & \mathrm{a}_{12} & \mathrm{a}_{13} \\
\boldsymbol{a}_{21} & \boldsymbol{a}_{22} & \boldsymbol{a}_{23} \\
\mathrm{a}_{31} & \mathrm{a}_{32} & \mathrm{a}_{33}
\end{array}\right|
$$

Expanding along $\mathrm{R}_{2}$, we get

$$
\begin{align*}
|\mathrm{A}|= & (-1)^{2+1} a_{21}\left|\begin{array}{ll}
a_{12} & a_{13} \\
a_{32} & a_{33}
\end{array}\right|+(-1)^{2+2} a_{22}\left|\begin{array}{ll}
a_{11} & a_{13} \\
a_{31} & a_{33}
\end{array}\right| \\
& +(-1)^{2+3} a_{23}\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{31} & a_{32}
\end{array}\right| \\
= & -a_{21}\left(a_{12} a_{33}-a_{32} a_{13}\right)+a_{22}\left(a_{11} a_{33}-a_{31} a_{13}\right) \\
& -a_{23}\left(a_{11} a_{32}-a_{31} a_{12}\right) \\
|\mathrm{A}|= & -a_{21} a_{12} a_{33}+a_{21} a_{32} a_{13}+a_{22} a_{11} a_{33}-a_{22} a_{31} a_{13}-a_{23} a_{11} a_{32} \\
& +a_{23} a_{31} a_{12} \\
= & a_{11} a_{22} a_{33}-a_{11} a_{23} a_{32}-a_{12} a_{21} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32} \\
& -a_{13} a_{31} a_{22} \tag{2}
\end{align*}
$$

## Expansion along first Column ( $\mathrm{C}_{1}$ )

$$
|\mathrm{A}|=\left|\begin{array}{lll}
\boldsymbol{a}_{\mathbf{1 1}} & a_{12} & a_{13} \\
\boldsymbol{a}_{\mathbf{2 1}} & a_{22} & a_{23} \\
\boldsymbol{a}_{\mathbf{3 1}} & a_{32} & a_{33}
\end{array}\right|
$$

By expanding along $\mathrm{C}_{1}$, we get

$$
\begin{aligned}
|\mathrm{A}|= & a_{11}(-1)^{1+1}\left|\begin{array}{ll}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{array}\right|+a_{21}(-1)^{2+1}\left|\begin{array}{ll}
a_{12} & a_{13} \\
a_{32} & a_{33}
\end{array}\right| \\
& +a_{31}(-1)^{3+1}\left|\begin{array}{ll}
a_{12} & a_{13} \\
a_{22} & a_{23}
\end{array}\right| \\
= & a_{11}\left(a_{22} a_{33}-a_{23} a_{32}\right)-a_{21}\left(a_{12} a_{33}-a_{13} a_{32}\right)+a_{31}\left(a_{12} a_{23}-a_{13} a_{22}\right)
\end{aligned}
$$

$$
\begin{align*}
\mathrm{A} \mid= & a_{11} a_{22} a_{33}-a_{11} a_{23} a_{32}-a_{21} a_{12} a_{33}+a_{21} a_{13} a_{32}+a_{31} a_{12} a_{23} \\
& -a_{31} a_{13} a_{22} \\
= & a_{11} a_{22} a_{33}-a_{11} a_{23} a_{32}-a_{12} a_{21} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32} \\
& -a_{13} a_{31} a_{22} \tag{3}
\end{align*}
$$

Clearly, values of $|\mathrm{A}|$ in (1), (2) and (3) are equal. It is left as an exercise to the reader to verify that the values of $|\mathrm{A}|$ by expanding along $\mathrm{R}_{3}, \mathrm{C}_{2}$ and $\mathrm{C}_{3}$ are equal to the value of $|\mathrm{A}|$ obtained in (1), (2) or (3).

Hence, expanding a determinant along any row or column gives same value.

## Remarks

(i) For easier calculations, we shall expand the determinant along that row or column which contains maximum number of zeros.
(ii) While expanding, instead of multiplying by $(-1)^{i+j}$, we can multiply by +1 or -1 according as $(i+j)$ is even or odd.
(iii) Let $\mathrm{A}=\left[\begin{array}{ll}2 & 2 \\ 4 & 0\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}1 & 1 \\ 2 & 0\end{array}\right]$. Then, it is easy to verify that $\mathrm{A}=2 \mathrm{~B}$. Also $|\mathrm{A}|=0-8=-8$ and $|\mathrm{B}|=0-2=-2$.
Observe that, $|\mathrm{A}|=4(-2)=2^{2}|\mathrm{~B}|$ or $|\mathrm{A}|=2^{n}|\mathrm{~B}|$, where $n=2$ is the order of square matrices A and B .

In general, if $\mathrm{A}=k \mathrm{~B}$ where A and B are square matrices of order $n$, then $|\mathrm{A}|=k^{n}$ $|\mathrm{B}|$, where $n=1,2,3$
Example 3 Evaluate the determinant $\Delta=\left|\begin{array}{rrr}1 & 2 & 4 \\ -1 & 3 & 0 \\ 4 & 1 & 0\end{array}\right|$.
Solution Note that in the third column, two entries are zero. So expanding along third column ( $\mathrm{C}_{3}$ ), we get

$$
\begin{aligned}
\Delta & =4\left|\begin{array}{rr}
-1 & 3 \\
4 & 1
\end{array}\right|-0\left|\begin{array}{ll}
1 & 2 \\
4 & 1
\end{array}\right|+0\left|\begin{array}{rr}
1 & 2 \\
-1 & 3
\end{array}\right| \\
& =4(-1-12)-0+0=-52
\end{aligned}
$$

Example 4 Evaluate $\Delta=\left|\begin{array}{ccc}0 & \sin \alpha & -\cos \alpha \\ -\sin \alpha & 0 & \sin \beta \\ \cos \alpha & -\sin \beta & 0\end{array}\right|$.

Solution Expanding along $\mathrm{R}_{1}$, we get

$$
\begin{aligned}
\Delta & =0\left|\begin{array}{cc}
0 & \sin \beta \\
-\sin \beta & 0
\end{array}\right|-\sin \alpha\left|\begin{array}{cc}
-\sin \alpha & \sin \beta \\
\cos \alpha & 0
\end{array}\right|-\cos \alpha\left|\begin{array}{cc}
-\sin \alpha & 0 \\
\cos \alpha & -\sin \beta
\end{array}\right| \\
& =0-\sin \alpha(0-\sin \beta \cos \alpha)-\cos \alpha(\sin \alpha \sin \beta-0) \\
& =\sin \alpha \sin \beta \cos \alpha-\cos \alpha \sin \alpha \sin \beta=0
\end{aligned}
$$

Example 5 Find values of $x$ for which $\left|\begin{array}{ll}3 & x \\ x & 1\end{array}\right|=\left|\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right|$.
Solution We have $\left|\begin{array}{cc}3 & x \\ x & 1\end{array}\right|=\left|\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right|$
i.e.

$$
\begin{aligned}
3-x^{2} & =3-8 \\
x^{2} & =8
\end{aligned}
$$

i.e.

Hence

$$
x= \pm 2 \sqrt{2}
$$

## EXERCISE 4.1

Evaluate the determinants in Exercises 1 and 2.

1. $\left|\begin{array}{rr}2 & 4 \\ -5 & -1\end{array}\right|$
2. 

(i) $\left|\begin{array}{cc}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right|$
(ii) $\left|\begin{array}{cc}x^{2}-x+1 & x-1 \\ x+1 & x+1\end{array}\right|$
3. If $\mathrm{A}=\left[\begin{array}{ll}1 & 2 \\ 4 & 2\end{array}\right]$, then show that $|2 \mathrm{~A}|=4|\mathrm{~A}|$
4. If $\mathrm{A}=\left[\begin{array}{lll}1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 4\end{array}\right]$, then show that $|3 \mathrm{~A}|=27|\mathrm{~A}|$
5. Evaluate the determinants
(i) $\left|\begin{array}{rrr}3 & -1 & -2 \\ 0 & 0 & -1 \\ 3 & -5 & 0\end{array}\right|$
(ii) $\left|\begin{array}{rrr}3 & -4 & 5 \\ 1 & 1 & -2 \\ 2 & 3 & 1\end{array}\right|$
(iii) $\left|\begin{array}{ccc}0 & 1 & 2 \\ -1 & 0 & -3 \\ -2 & 3 & 0\end{array}\right|$
(iv) $\left|\begin{array}{rrr}2 & -1 & -2 \\ 0 & 2 & -1 \\ 3 & -5 & 0\end{array}\right|$
6. If $\mathrm{A}=\left[\begin{array}{lll}1 & 1 & -2 \\ 2 & 1 & -3 \\ 5 & 4 & -9\end{array}\right]$, find $|\mathrm{A}|$
7. Find values of $x$, if
(i) $\left|\begin{array}{ll}2 & 4 \\ 5 & 1\end{array}\right|=\left|\begin{array}{cc}2 x & 4 \\ 6 & x\end{array}\right|$
(ii) $\left|\begin{array}{ll}2 & 3 \\ 4 & 5\end{array}\right|=\left|\begin{array}{cc}x & 3 \\ 2 x & 5\end{array}\right|$
8. If $\left|\begin{array}{cc}x & 2 \\ 18 & x\end{array}\right|=\left|\begin{array}{cc}6 & 2 \\ 18 & 6\end{array}\right|$, then $x$ is equal to
(A) 6
(B) $\pm 6$
(C) -6
(D) 0

### 4.3 Area of a Triangle

In earlier classes, we have studied that the area of a triangle whose vertices are $\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right)$ and $\left(x_{3}, y_{3}\right)$, is given by the expression $\frac{1}{2}\left[x_{1}\left(y_{2}-y_{3}\right)+x_{2}\left(y_{3}-y_{1}\right)+\right.$ $\left.x_{3}\left(y_{1}-y_{2}\right)\right]$. Now this expression can be written in the form of a determinant as

$$
\Delta=\frac{1}{2}\left|\begin{array}{lll}
x_{1} & y_{1} & 1  \tag{1}\\
x_{2} & y_{2} & 1 \\
x_{3} & y_{3} & 1
\end{array}\right|
$$

## Remarks

(i) Since area is a positive quantity, we always take the absolute value of the determinant in (1).
(ii) If area is given, use both positive and negative values of the determinant for calculation.
(iii) The area of the triangle formed by three collinear points is zero.

Example 6 Find the area of the triangle whose vertices are $(3,8),(-4,2)$ and $(5,1)$. Solution The area of triangle is given by

$$
\Delta=\frac{1}{2}\left|\begin{array}{rrr}
3 & 8 & 1 \\
-4 & 2 & 1 \\
5 & 1 & 1
\end{array}\right|
$$

$$
\begin{aligned}
& =\frac{1}{2}[3(2-1)-8(-4-5)+1(-4-10)] \\
& =\frac{1}{2}(3+72-14)=\frac{61}{2}
\end{aligned}
$$

Example 7 Find the equation of the line joining $\mathrm{A}(1,3)$ and $\mathrm{B}(0,0)$ using determinants and find $k$ if $\mathrm{D}(k, 0)$ is a point such that area of triangle ABD is 3 sq units.
Solution Let $\mathrm{P}(x, y)$ be any point on AB . Then, area of triangle ABP is zero (Why?). So

$$
\frac{1}{2}\left|\begin{array}{lll}
0 & 0 & 1 \\
1 & 3 & 1 \\
x & y & 1
\end{array}\right|=0
$$

This gives

$$
\frac{1}{2}(y-3 x)=0 \text { or } y=3 x
$$

which is the equation of required line AB .
Also, since the area of the triangle ABD is 3 sq. units, we have

$$
\frac{1}{2}\left|\begin{array}{ccc}
1 & 3 & 1 \\
0 & 0 & 1 \\
k & 0 & 1
\end{array}\right|= \pm 3
$$

This gives, $\frac{-3 k}{2}= \pm 3$, i.e., $k=\mp 2$.

## EXERCISE 4.2

1. Find area of the triangle with vertices at the point given in each of the following:
(i) $(1,0),(6,0),(4,3)$
(ii) $(2,7),(1,1),(10,8)$
(iii) $(-2,-3),(3,2),(-1,-8)$
2. Show that points
$\mathrm{A}(a, b+c), \mathrm{B}(b, c+a), \mathrm{C}(c, a+b)$ are collinear.
3. Find values of $k$ if area of triangle is 4 sq. units and vertices are
(i) $(k, 0),(4,0),(0,2)$
(ii) $(-2,0),(0,4),(0, k)$
4. (i) Find equation of line joining $(1,2)$ and $(3,6)$ using determinants.
(ii) Find equation of line joining $(3,1)$ and $(9,3)$ using determinants.
5. If area of triangle is 35 sq units with vertices $(2,-6),(5,4)$ and $(k, 4)$. Then $k$ is
(A) 12
(B) -2
(C) $-12,-2$
(D) $12,-2$

### 4.4 Minors and Cofactors

In this section, we will learn to write the expansion of a determinant in compact form using minors and cofactors.

Definition 1 Minor of an element $a_{i j}$ of a determinant is the determinant obtained by deleting its $i$ th row and $j$ th column in which element $a_{i j}$ lies. Minor of an element $a_{i j}$ is denoted by $\mathrm{M}_{i j}$.

Remark Minor of an element of a determinant of order $n(n \geq 2)$ is a determinant of order $n-1$.

Example 8 Find the minor of element 6 in the determinant $\Delta=\left|\begin{array}{lll}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{array}\right|$
Solution Since 6 lies in the second row and third column, its minor $\mathrm{M}_{23}$ is given by

$$
\mathrm{M}_{23}=\left|\begin{array}{ll}
1 & 2 \\
7 & 8
\end{array}\right|=8-14=-6\left(\text { obtained by deleting } \mathrm{R}_{2} \text { and } \mathrm{C}_{3} \text { in } \Delta\right) .
$$

Definition 2 Cofactor of an element $a_{i j}$, denoted by $\mathrm{A}_{i j}$ is defined by $\mathrm{A}_{i j}=(-1)^{i+j} \mathrm{M}_{i j}$, where $\mathrm{M}_{i j}$ is minor of $a_{i j}$.

Example 9 Find minors and cofactors of all the elements of the determinant $\left|\begin{array}{rr}1 & -2 \\ 4 & 3\end{array}\right|$
Solution Minor of the element $a_{i j}$ is $\mathrm{M}_{i j}$
Here $a_{11}=1$. So $\mathrm{M}_{11}=$ Minor of $a_{11}=3$
$\mathrm{M}_{12}=$ Minor of the element $a_{12}=4$
$\mathrm{M}_{21}=$ Minor of the element $a_{21}=-2$
$\mathrm{M}_{22}=$ Minor of the element $a_{22}=1$
Now, cofactor of $a_{i j}$ is $\mathrm{A}_{i j}$. So

$$
\begin{aligned}
& A_{11}=(-1)^{1+1} \quad M_{11}=(-1)^{2}(3)=3 \\
& A_{12}=(-1)^{1+2} \quad M_{12}=(-1)^{3}(4)=-4 \\
& A_{21}=(-1)^{2+1} \quad M_{21}=(-1)^{3}(-2)=2 \\
& A_{22}=(-1)^{2+2} \quad M_{22}=(-1)^{4}(1)=1
\end{aligned}
$$

Example 10 Find minors and cofactors of the elements $a_{11}, a_{21}$ in the determinant

$$
\Delta=\left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|
$$

Solution By definition of minors and cofactors, we have
Minor of $a_{11}=\mathrm{M}_{11}=\left|\begin{array}{ll}a_{22} & a_{23} \\ a_{32} & a_{33}\end{array}\right|=a_{22} a_{33}-a_{23} a_{32}$
Cofactor of $a_{11}=\mathrm{A}_{11}=(-1)^{1+1} \quad \mathrm{M}_{11}=a_{22} a_{33}-a_{23} a_{32}$
Minor of $a_{21}=\mathrm{M}_{21}=\left|\begin{array}{ll}a_{12} & a_{13} \\ a_{32} & a_{33}\end{array}\right|=a_{12} a_{33}-a_{13} a_{32}$
Cofactor of $a_{21}=\mathrm{A}_{21}=(-1)^{2+1} \quad \mathrm{M}_{21}=(-1)\left(a_{12} a_{33}-a_{13} a_{32}\right)=-a_{12} a_{33}+a_{13} a_{32}$
Remark Expanding the determinant $\Delta$, in Example 21, along $\mathrm{R}_{1}$, we have

$$
\begin{aligned}
\Delta & =(-1)^{1+1} a_{11}\left|\begin{array}{ll}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{array}\right|+(-1)^{1+2} a_{12}\left|\begin{array}{ll}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{array}\right|+(-1)^{1+3} a_{13}\left|\begin{array}{ll}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}\right| \\
& =a_{11} \mathrm{~A}_{11}+a_{12} \mathrm{~A}_{12}+a_{13} \mathrm{~A}_{13}, \text { where } \mathrm{A}_{i j} \text { is cofactor of } a_{i j} \\
& =\text { sum of product of elements of } \mathrm{R}_{1} \text { with their corresponding cofactors }
\end{aligned}
$$

Similarly, $\Delta$ can be calculated by other five ways of expansion that is along $R_{2}, R_{3}$, $\mathrm{C}_{1}, \mathrm{C}_{2}$ and $\mathrm{C}_{3}$.

Hence $\Delta=$ sum of the product of elements of any row (or column) with their corresponding cofactors.

Note If elements of a row (or column) are multiplied with cofactors of any other row (or column), then their sum is zero. For example,

$$
\begin{aligned}
\Delta & =a_{11} \mathrm{~A}_{21}+a_{12} \mathrm{~A}_{22}+a_{13} \mathrm{~A}_{23} \\
& =a_{11}(-1)^{1+1}\left|\begin{array}{ll}
a_{12} & a_{13} \\
a_{32} & a_{33}
\end{array}\right|+a_{12}(-1)^{1+2}\left|\begin{array}{ll}
a_{11} & a_{13} \\
a_{31} & a_{33}
\end{array}\right|+a_{13}(-1)^{1+3}\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{31} & a_{32}
\end{array}\right| \\
& =\left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{11} & a_{12} & a_{13} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|=0 \text { (since } \mathrm{R}_{1} \text { and } \mathrm{R}_{2} \text { are identical) }
\end{aligned}
$$

Similarly, we can try for other rows and columns.

Example 11 Find minors and cofactors of the elements of the determinant

$$
\left|\begin{array}{ccc}
2 & -3 & 5 \\
6 & 0 & 4 \\
1 & 5 & -7
\end{array}\right| \text { and verify that } a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33}=0
$$

Solution We have $M_{11}=\left|\begin{array}{cc}0 & 4 \\ 5 & -7\end{array}\right|=0-20=-20 ; \quad A_{11}=(-1)^{1+1}(-20)=-20$

$$
\begin{array}{ll}
\mathrm{M}_{12}=\left|\begin{array}{cc}
6 & 4 \\
1 & -7
\end{array}\right|=-42-4=-46 ; & \mathrm{A}_{12}=(-1)^{1+2}(-46)=46 \\
\mathrm{M}_{13}=\left|\begin{array}{cc}
6 & 0 \\
1 & 5
\end{array}\right|=30-0=30 ; & \mathrm{A}_{13}=(-1)^{1+3}(30)=30 \\
\mathrm{M}_{21}=\left|\begin{array}{cc}
-3 & 5 \\
5 & -7
\end{array}\right|=21-25=-4 ; & \mathrm{A}_{21}=(-1)^{2+1}(-4)=4 \\
\mathrm{M}_{22}=\left|\begin{array}{cc}
2 & 5 \\
1 & -7
\end{array}\right|=-14-5=-19 ; & \mathrm{A}_{22}=(-1)^{2+2}(-19)=-19 \\
\mathrm{M}_{23}=\left|\begin{array}{cc}
2 & -3 \\
1 & 5
\end{array}\right|=10+3=13 ; & \mathrm{A}_{23}=(-1)^{2+3}(13)=-13 \\
\mathrm{M}_{31}=\left|\begin{array}{cc}
-3 & 5 \\
0 & 4
\end{array}\right|=-12-0=-12 ; & \mathrm{A}_{31}=(-1)^{3+1}(-12)=-12 \\
\mathrm{M}_{32}=\left|\begin{array}{cc}
2 & 5 \\
6 & 4
\end{array}\right|=8-30=-22 ; & \mathrm{A}_{32}=(-1)^{3+2}(-22)=22 \\
\mathrm{M}_{33}=\left|\begin{array}{cc}
2 & -3 \\
6 & 0
\end{array}\right|=0+18=18 ; & \mathrm{A}_{33}=(-1)^{3+3}(18)=18 \\
a_{11}=2, a_{12}=-3, a_{13}=5 ; \mathrm{A}_{31}=-12, \mathrm{~A}_{32}=22, \mathrm{~A}_{33}=18 \\
a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33} \\
=2(-12)+(-3)(22)+5(18)=-24-66+90=0
\end{array}
$$

## EXERCISE 4.3

Write Minors and Cofactors of the elements of following determinants:
1.
(i) $\left|\begin{array}{rr}2 & -4 \\ 0 & 3\end{array}\right|$
(ii) $\left|\begin{array}{ll}a & c \\ b & d\end{array}\right|$
2.
(i) $\left|\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right|$
(ii) $\left|\begin{array}{rrr}1 & 0 & 4 \\ 3 & 5 & -1 \\ 0 & 1 & 2\end{array}\right|$
3. Using Cofactors of elements of second row, evaluate $\Delta=\left|\begin{array}{lll}5 & 3 & 8 \\ 2 & 0 & 1 \\ 1 & 2 & 3\end{array}\right|$.
4. Using Cofactors of elements of third column, evaluate $\Delta=\left|\begin{array}{lll}1 & x & y z \\ 1 & y & z x \\ 1 & z & x y\end{array}\right|$.
5. If $\Delta=\left|\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right|$ and $\mathrm{A}_{i j}$ is Cofactors of $a_{i j}$, then value of $\Delta$ is given by
(A) $a_{11} \mathrm{~A}_{31}+a_{12} \mathrm{~A}_{32}+a_{13} \mathrm{~A}_{33}$
(B) $a_{11} \mathrm{~A}_{11}+a_{12} \mathrm{~A}_{21}+a_{13} \mathrm{~A}_{31}$
(C) $a_{21} \mathrm{~A}_{11}+a_{22} \mathrm{~A}_{12}+a_{23} \mathrm{~A}_{13}$
(D) $a_{11} \mathrm{~A}_{11}+a_{21} \mathrm{~A}_{21}+a_{31} \mathrm{~A}_{31}$

### 4.5 Adjoint and Inverse of a Matrix

In the previous chapter, we have studied inverse of a matrix. In this section, we shall discuss the condition for existence of inverse of a matrix.

To find inverse of a matrix A , i.e., $\mathrm{A}^{-1}$ we shall first define adjoint of a matrix.

### 4.5.1 Adjoint of a matrix

Definition 3 The adjoint of a square matrix $\mathrm{A}=\left[a_{i j}\right]_{n \times n}$ is defined as the transpose of the matrix $\left[\mathrm{A}_{i j}\right]_{n \times n}$, where $\mathrm{A}_{i j}$ is the cofactor of the element $a_{i j}$. Adjoint of the matrix A is denoted by adj A .

Let

$$
\mathrm{A}=\left[\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right]
$$

Then $\quad \operatorname{adj} \mathrm{A}=$ Transpose of $\left[\begin{array}{lll}\mathrm{A}_{11} & \mathrm{~A}_{12} & \mathrm{~A}_{13} \\ \mathrm{~A}_{21} & \mathrm{~A}_{22} & \mathrm{~A}_{23} \\ \mathrm{~A}_{31} & \mathrm{~A}_{32} & \mathrm{~A}_{33}\end{array}\right]=\left[\begin{array}{lll}\mathrm{A}_{11} & \mathrm{~A}_{21} & \mathrm{~A}_{31} \\ \mathrm{~A}_{12} & \mathrm{~A}_{22} & \mathrm{~A}_{32} \\ \mathrm{~A}_{13} & \mathrm{~A}_{23} & \mathrm{~A}_{33}\end{array}\right]$
Example 12 Find $\operatorname{adj} \mathrm{A}$ for $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 4\end{array}\right]$
Solution We have $\mathrm{A}_{11}=4, \mathrm{~A}_{12}=-1, \mathrm{~A}_{21}=-3, \mathrm{~A}_{22}=2$

Hence

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{ll}
\mathrm{A}_{11} & \mathrm{~A}_{21} \\
\mathrm{~A}_{12} & \mathrm{~A}_{22}
\end{array}\right]=\left[\begin{array}{cc}
4 & -3 \\
-1 & 2
\end{array}\right]
$$

Remark For a square matrix of order 2, given by

$$
\mathrm{A}=\left[\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right]
$$

The adj A can also be obtained by interchanging $a_{11}$ and $a_{22}$ and by changing signs of $a_{12}$ and $a_{21}$, i.e.,
$\operatorname{adj} \mathrm{A}=$
![](https://cdn.mathpix.com/cropped/2025_07_21_87c5502490a156e1f0f9g-13.jpg?height=207&width=454&top_left_y=1177&top_left_x=673)

Change sign Interchange
We state the following theorem without proof.
Theorem 1 If A be any given square matrix of order $n$, then

$$
\mathrm{A}(\operatorname{adj} \mathrm{~A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}
$$

where I is the identity matrix of order $n$

## Verification

Let

$$
\mathrm{A}=\left[\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right] \text {, then } \operatorname{adj} \mathrm{A}=\left[\begin{array}{lll}
\mathrm{A}_{11} & \mathrm{~A}_{21} & \mathrm{~A}_{31} \\
\mathrm{~A}_{12} & \mathrm{~A}_{22} & \mathrm{~A}_{32} \\
\mathrm{~A}_{13} & \mathrm{~A}_{23} & \mathrm{~A}_{33}
\end{array}\right]
$$

Since sum of product of elements of a row (or a column) with corresponding cofactors is equal to $|\mathrm{A}|$ and otherwise zero, we have

$$
\mathrm{A}(\operatorname{adj} \mathrm{~A})=\left[\begin{array}{ccc}
|\mathrm{A}| & 0 & 0 \\
0 & |\mathrm{~A}| & 0 \\
0 & 0 & |\mathrm{~A}|
\end{array}\right]=|\mathrm{A}|\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=|\mathrm{A}| \mathrm{I}
$$

Similarly, we can show $(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$
Hence $\mathrm{A}(\operatorname{adj} \mathrm{A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$
Definition 4 A square matrix A is said to be singular if $|\mathrm{A}|=0$.
For example, the determinant of matrix $\mathrm{A}=\begin{array}{ll}1 & 2 \\ 4 & 8\end{array}$ is zero
Hence A is a singular matrix.
Definition 5 A square matrix $A$ is said to be non-singular if $|A| \neq 0$

Let

$$
A=\left[\begin{array}{ll}
1 & 2 \\
3 & 4
\end{array}\right] . \text { Then }|A|=\left|\begin{array}{ll}
1 & 2 \\
3 & 4
\end{array}\right|=4-6=-2 \neq 0 .
$$

Hence A is a nonsingular matrix
We state the following theorems without proof.
Theorem 2 If A and B are nonsingular matrices of the same order, then AB and BA are also nonsingular matrices of the same order.
Theorem 3 The determinant of the product of matrices is equal to product of their respective determinants, that is, $|\mathrm{AB}|=|\mathrm{A}||\mathrm{B}|$, where A and B are square matrices of the same order

$$
|\mathrm{A}| \quad 0 \quad 0
$$

Remark We know that $(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}=0 \quad|\mathrm{~A}| \quad 0 \quad,|\mathrm{~A}| \neq 0$

$$
\begin{array}{lll}
0 & 0 & |\mathrm{~A}|
\end{array}
$$

Writing determinants of matrices on both sides, we have

$$
|(\operatorname{adj} \mathrm{A}) \mathrm{A}|=\left|\begin{array}{ccc}
|\mathrm{A}| & 0 & 0 \\
0 & |\mathrm{~A}| & 0 \\
0 & 0 & |\mathrm{~A}|
\end{array}\right|
$$

i.e.

$$
|(\operatorname{adj} \mathrm{A})||\mathrm{A}|=|\mathrm{A}|^{3}\left|\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right|
$$

(Why?)
i.e.

$$
|(\operatorname{adj} \mathrm{A})||\mathrm{A}|=|\mathrm{A}|^{3}(1)
$$

i.e.

$$
|(\operatorname{adj} \mathrm{A})|=|\mathrm{A}|^{2}
$$

In general, if A is $a$ square matrix of order $n$, then $|\operatorname{adj}(\mathrm{A})|=|\mathrm{A}|^{n-1}$.
Theorem 4 A square matrix $A$ is invertible if and only if $A$ is nonsingular matrix.
Proof Let A be invertible matrix of order $n$ and I be the identity matrix of order $n$. Then, there exists a square matrix B of order $n$ such that $\mathrm{AB}=\mathrm{BA}=\mathrm{I}$

Now

$$
\mathrm{AB}=\mathrm{I} . \text { So }|\mathrm{AB}|=|\mathrm{I}| \quad \text { or } \quad|\mathrm{A}| \quad|\mathrm{B}|=1 \quad(\text { since }|\mathrm{I}|=1,|\mathrm{AB}|=|\mathrm{A}||\mathrm{B}|)
$$

This gives

$$
|\mathrm{A}| \neq 0 \text {. Hence } \mathrm{A} \text { is nonsingular. }
$$

Conversely, let A be nonsingular. Then $|\mathrm{A}| \neq 0$
Now

$$
\mathrm{A}(\operatorname{adj} \mathrm{~A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}
$$

(Theorem 1)
or

$$
\mathrm{A}\left(\frac{1}{|\mathrm{~A}|} \operatorname{adj} \mathrm{A}\right)=\left(\frac{1}{|\mathrm{~A}|} \operatorname{adj} \mathrm{A}\right) \mathrm{A}=\mathrm{I}
$$

or

$$
\mathrm{AB}=\mathrm{BA}=\mathrm{I}, \text { where } \mathrm{B}=\frac{1}{|\mathrm{~A}|} \text { adj } \mathrm{A}
$$

Thus

$$
\mathrm{A} \text { is invertible and } \mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \operatorname{adj} \mathrm{A}
$$

Example 13 If $\mathrm{A}=\begin{array}{lll}1 & 3 & 3 \\ 1 & 4 & 3\end{array}$, then verify that A adj $\mathrm{A}=|\mathrm{A}|$ I. Also find $\mathrm{A}^{-1}$.

$$
134
$$

Solution We have $|\mathrm{A}|=1(16-9)-3(4-3)+3(3-4)=1 \neq 0$
Now $\mathrm{A}_{11}=7, \mathrm{~A}_{12}=-1, \mathrm{~A}_{13}=-1, \mathrm{~A}_{21}=-3, \mathrm{~A}_{22}=1, \mathrm{~A}_{23}=0, \mathrm{~A}_{31}=-3, \mathrm{~A}_{32}=0$, $A_{33}=1$

Therefore

$$
\operatorname{adj} \mathrm{A}=\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]
$$

Now

$$
\begin{aligned}
\mathrm{A}(\operatorname{adj} \mathrm{~A}) & =\left[\begin{array}{lll}
1 & 3 & 3 \\
1 & 4 & 3 \\
1 & 3 & 4
\end{array}\right]\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{lll}
7-3-3 & -3+3+0 & -3+0+3 \\
7-4-3 & -3+4+0 & -3+0+3 \\
7-3-4 & -3+3+0 & -3+0+4
\end{array}\right] \\
& =\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=(1)\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=|\mathrm{A}| . \mathrm{I}
\end{aligned}
$$

Also

$$
\mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \text { adj } \mathrm{A}=\frac{1}{1}\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]=\left[\begin{array}{rrr}
7 & -3 & -3 \\
-1 & 1 & 0 \\
-1 & 0 & 1
\end{array}\right]
$$

Example 14 If $\mathrm{A}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]$, then verify that $(A B)^{-1}=B^{-1} A^{-1}$.
Solution We have $\mathrm{AB}=\left[\begin{array}{cc}2 & 3 \\ 1 & -4\end{array}\right]\left[\begin{array}{cc}1 & -2 \\ -1 & 3\end{array}\right]=\left[\begin{array}{cc}-1 & 5 \\ 5 & -14\end{array}\right]$
Since, $|\mathrm{AB}|=-11 \neq 0,(\mathrm{AB})^{-1}$ exists and is given by

$$
(\mathrm{AB})^{-1}=\frac{1}{|\mathrm{AB}|} \operatorname{adj}(\mathrm{AB})=-\frac{1}{11}\left[\begin{array}{cc}
-14 & -5 \\
-5 & -1
\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

Further, $|\mathrm{A}|=-11 \neq 0$ and $|\mathrm{B}|=1 \neq 0$. Therefore, $\mathrm{A}^{-1}$ and $\mathrm{B}^{-1}$ both exist and are given by

$$
\mathrm{A}^{-1}=-\frac{1}{11} \quad-4 \quad-3, \quad \mathrm{~B}^{-1}=\begin{array}{cc}
3 & 2 \\
1 & 1
\end{array}
$$

Therefore

$$
\mathrm{B}^{-1} \mathrm{~A}^{-1}=-\frac{1}{11} \quad 3 \quad 2 \quad-4 \quad-3 \quad 1 \quad 1 \quad-1 \quad 2 \quad=-\frac{1}{11} \quad-14 \quad-5 \quad-1 \quad=\frac{1}{11}\left[\begin{array}{cc}
14 & 5 \\
5 & 1
\end{array}\right]
$$

Hence $(A B)^{-1}=B^{-1} A^{-1}$

Example 15 Show that the matrix $A=\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}$ satisfies the equation $A^{2}-4 A+I=O$, where I is $2 \times 2$ identity matrix and O is $2 \times 2$ zero matrix. Using this equation, find $\mathrm{A}^{-1}$.

Solution We have $A^{2}=A \cdot A=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]=\left[\begin{array}{cc}7 & 12 \\ 4 & 7\end{array}\right]$

Hence

$$
\mathrm{A}^{2}-4 \mathrm{~A}+\mathrm{I}=\left[\begin{array}{cc}
7 & 12 \\
4 & 7
\end{array}\right]-\left[\begin{array}{cc}
8 & 12 \\
4 & 8
\end{array}\right]+\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right]=\mathrm{O}
$$

Now

$$
A^{2}-4 A+I=O
$$

Therefore

$$
A A-4 A=-I
$$

or

$$
\text { A } \mathrm{A}\left(\mathrm{~A}^{-1}\right)-4 \mathrm{AA}^{-1}=-\mathrm{IA}^{-1} \text { (Post multiplying by } \mathrm{A}^{-1} \text { because }|\mathrm{A}| \neq 0 \text { ) }
$$

or

$$
\mathrm{A}\left(\mathrm{~A} \mathrm{~A}^{-1}\right)-4 \mathrm{I}=-\mathrm{A}^{-1}
$$

or

$$
A I-4 I=-A^{-1}
$$

or

$$
\mathrm{A}^{-1}=4 \mathrm{I}-\mathrm{A}=\left[\begin{array}{ll}
4 & 0 \\
0 & 4
\end{array}\right]-\left[\begin{array}{ll}
2 & 3 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right]
$$

Hence

$$
A^{-1}=\left[\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right]
$$

## EXERCISE 4.4

Find adjoint of each of the matrices in Exercises 1 and 2.

1. $\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}$
$1 \quad-1 \quad 2$
2. 235
$\begin{array}{lll}-2 & 0 & 1\end{array}$

Verify $\mathrm{A}(\operatorname{adj} \mathrm{A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$ in Exercises 3 and 4
3. $\begin{array}{cc}2 & 3 \\ -4 & -6\end{array}$
4. $\begin{array}{ccc}1 & -1 & 2 \\ 3 & 0 & -2 \\ 1 & 0 & 3\end{array}$

Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.
5. $\begin{array}{cc}2 & -2 \\ 4 & 3\end{array}$
6. $\begin{array}{rr}-1 & 5 \\ -3 & 2\end{array}$
7. $\begin{array}{lll}1 & 2 & 3 \\ 0 & 2 & 4 \\ 0 & 0 & 5\end{array}$
8. $\begin{array}{ccc}1 & 0 & 0 \\ 3 & 3 & 0 \\ 5 & 2 & -1\end{array}$
9. $\begin{array}{ccc}2 & 1 & 3 \\ 4 & -1 & 0 \\ -7 & 2 & 1\end{array}$
10. $\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}$
11. $\left[\begin{array}{ccc}1 & 0 & 0 \\ 0 & \cos \alpha & \sin \alpha \\ 0 & \sin \alpha & -\cos \alpha\end{array}\right]$
12. Let $A=\begin{array}{ll}3 & 7 \\ 2 & 5\end{array}$ and $B=\begin{array}{ll}6 & 8 \\ 7 & 9\end{array}$. Verify that $(A B)^{-1}=B^{-1} A^{-1}$.
13. If $\mathrm{A}=\begin{array}{cc}3 & 1 \\ -1 & 2\end{array}$, show that $\mathrm{A}^{2}-5 \mathrm{~A}+7 \mathrm{I}=\mathrm{O}$. Hence find $\mathrm{A}^{-1}$.
14. For the matrix $\mathrm{A}=\begin{array}{ll}3 & 2 \\ 1 & 1\end{array}$, find the numbers $a$ and $b$ such that $\mathrm{A}^{2}+a \mathrm{~A}+b \mathrm{I}=\mathrm{O}$.
15. For the matrix $A=\begin{array}{ccc}1 & 1 & 1 \\ 1 & 2 & -3 \\ 2 & -1 & 3\end{array}$

Show that $A^{3}-6 A^{2}+5 A+11 I=O$. Hence, find $A^{-1}$.

$$
\begin{array}{lll}
2 & -1 & 1
\end{array}
$$

16. If $\mathrm{A}=-1 \quad 2 \quad-1$

$$
\begin{array}{lll}
1 & -1 & 2
\end{array}
$$

Verify that $A^{3}-6 A^{2}+9 A-4 I=O$ and hence find $A^{-1}$
17. Let A be a nonsingular square matrix of order $3 \times 3$. Then $|\operatorname{adj} \mathrm{A}|$ is equal to
(A) $|\mathrm{A}|$
(B) $|\mathrm{A}|^{2}$
(C) $|\mathrm{A}|^{3}$
(D) $3|\mathrm{~A}|$
18. If $A$ is an invertible matrix of order 2 , then $\operatorname{det}\left(A^{-1}\right)$ is equal to
(A) $\operatorname{det}(\mathrm{A})$
(B) $\frac{1}{\operatorname{det}(\mathrm{~A})}$
(C) 1
(D) 0

### 4.6 Applications of Determinants and Matrices

In this section, we shall discuss application of determinants and matrices for solving the system of linear equations in two or three variables and for checking the consistency of the system of linear equations.

Consistent system A system of equations is said to be consistent if its solution (one or more) exists.
Inconsistent system A system of equations is said to be inconsistent if its solution does not exist.

Note In this chapter, we restrict ourselves to the system of linear equations having unique solutions only.
4.6.1 Solution of system of linear equations using inverse of a matrix

Let us express the system of linear equations as matrix equations and solve them using inverse of the coefficient matrix.

Consider the system of equations

$$
\begin{aligned}
& a_{1} x+b_{1} y+c_{1} z=d_{1} \\
& a_{2} x+b_{2} y+c_{2} z=d_{2} \\
& a_{3} x+b_{3} y+c_{3} z=d_{3}
\end{aligned}
$$

Let $\quad \mathrm{A}=\left[\begin{array}{lll}a_{1} & b_{1} & c_{1} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3}\end{array}\right], \mathrm{X}=\left[\begin{array}{c}x \\ y \\ z\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{l}d_{1} \\ d_{2} \\ d_{3}\end{array}\right]$
Then, the system of equations can be written as, $\mathrm{AX}=\mathrm{B}$, i.e.,

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
d_{1} \\
d_{2} \\
d_{3}
\end{array}\right]
$$

Case I If A is a nonsingular matrix, then its inverse exists. Now
or

$$
\begin{array}{rlr}
\mathrm{A}^{-1}(\mathrm{AX}) & =\mathrm{A}^{-1} \mathrm{~B} & \left(\text { premultiplying by } \mathrm{A}^{-1}\right) \\
\left(\mathrm{A}^{-1} \mathrm{~A}\right) \mathrm{X} & =\mathrm{A}^{-1} \mathrm{~B} & (\text { by associative property }) \\
\mathrm{IX} & =\mathrm{A}^{-1} \mathrm{~B} & \\
\mathrm{X} & =\mathrm{A}^{-1} \mathrm{~B} &
\end{array}
$$

This matrix equation provides unique solution for the given system of equations as inverse of a matrix is unique. This method of solving system of equations is known as Matrix Method.
Case II If A is a singular matrix, then $|\mathrm{A}|=0$.
In this case, we calculate ( $\operatorname{adj} \mathrm{A}$ ) B.
If $(\operatorname{adj} \mathrm{A}) \mathrm{B} \neq \mathrm{O}$, ( O being zero matrix), then solution does not exist and the system of equations is called inconsistent.

If ( $\operatorname{adj} \mathrm{A}$ ) $\mathrm{B}=\mathrm{O}$, then system may be either consistent or inconsistent according as the system have either infinitely many solutions or no solution.

Example 16 Solve the system of equations

$$
\begin{aligned}
& 2 x+5 y=1 \\
& 3 x+2 y=7
\end{aligned}
$$

Solution The system of equations can be written in the form $\mathrm{AX}=\mathrm{B}$, where

$$
\mathrm{A}=\left[\begin{array}{ll}
2 & 5 \\
3 & 2
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y
\end{array}\right] \text { and } \mathrm{B}=\left[\begin{array}{l}
1 \\
7
\end{array}\right]
$$

Now, $|\mathrm{A}|=-11 \neq 0$, Hence, A is nonsingular matrix and so has a unique solution.

Note that

$$
\mathrm{A}^{-1}=-\frac{1}{11} \quad \begin{array}{cc}
2 & -5 \\
-3 & 2
\end{array}
$$

Therefore

$$
\mathrm{X}=\mathrm{A}^{-1} \mathrm{~B}=-\frac{1}{11} \quad 2 \quad \begin{array}{ccc}
-5 & 1 \\
-3 & 2 & 7
\end{array}
$$

i.e.

$$
\begin{gathered}
{\left[\begin{array}{l}
x \\
y
\end{array}\right]=-\frac{1}{11} \quad-33=3} \\
x=3, y=-1
\end{gathered}
$$

Hence
Example 17 Solve the following system of equations by matrix method.

$$
\begin{array}{r}
3 x-2 y+3 z=8 \\
2 x+y-z=1 \\
4 x-3 y+2 z=4
\end{array}
$$

Solution The system of equations can be written in the form $\mathrm{AX}=\mathrm{B}$, where

$$
\mathrm{A}=\left[\begin{array}{ccc}
3 & -2 & 3 \\
2 & 1 & -1 \\
4 & -3 & 2
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } \mathrm{B}=\left[\begin{array}{l}
8 \\
1 \\
4
\end{array}\right]
$$

We see that

$$
|A|=3(2-3)+2(4+4)+3(-6-4)=-17 \neq 0
$$

Hence, A is nonsingular and so its inverse exists. Now
$\mathrm{A}_{11}=-1$,
$\mathrm{A}_{12}=-8$,
$\mathrm{A}_{13}=-10$
$\mathrm{A}_{21}=-5$,
$\mathrm{A}_{22}=-6$,
$\mathrm{A}_{23}=1$
$\mathrm{A}_{31}=-1$,
$\mathrm{A}_{32}=9$,
$\mathrm{A}_{33}=7$

Therefore

$$
\begin{aligned}
\mathrm{A}^{-1} & =-\frac{1}{17}\left[\begin{array}{ccc}
-1 & -5 & -1 \\
-8 & -6 & 9 \\
-10 & 1 & 7
\end{array}\right] \\
\mathrm{X} & =\mathrm{A}^{-1} \mathrm{~B}=-\frac{1}{17}\left[\begin{array}{ccc}
-1 & -5 & -1 \\
-8 & -6 & 9 \\
-10 & 1 & 7
\end{array}\right]\left[\begin{array}{l}
8 \\
1 \\
4
\end{array}\right]
\end{aligned}
$$

So
i.e.

$$
\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=-\frac{1}{17}\left[\begin{array}{l}
-17 \\
-34 \\
-51
\end{array}\right]=\left[\begin{array}{l}
1 \\
2 \\
3
\end{array}\right]
$$

Hence

$$
x=1, y=2 \text { and } z=3
$$

Example 18 The sum of three numbers is 6 . If we multiply third number by 3 and add second number to it, we get 11 . By adding first and third numbers, we get double of the second number. Represent it algebraically and find the numbers using matrix method.

Solution Let first, second and third numbers be denoted by $x, y$ and $z$, respectively. Then, according to given conditions, we have

$$
\begin{aligned}
x+y+z & =6 \\
y+3 z & =11 \\
x+z & =2 y \text { or } x-2 y+z=0
\end{aligned}
$$

This system can be written as $\mathrm{A} \mathrm{X}=\mathrm{B}$, where

$$
\mathrm{A}=\begin{array}{lll}
1 & 1 & 1 \\
0 & 1 & 3 \\
1 & 2 & 1
\end{array}, \mathrm{X}=\begin{gathered}
x \\
y \\
z
\end{gathered} \text { and } \mathrm{B}=\begin{gathered}
6 \\
11 \\
0
\end{gathered}
$$

Here $|\mathrm{A}|=1(1+6)-(0-3)+(0-1)=9 \neq 0$. Now we find adj A

$$
\begin{array}{lll}
A_{11}=1(1+6)=7, & A_{12}=-(0-3)=3, & A_{13}=-1 \\
A_{21}=-(1+2)=-3, & A_{22}=0, & A_{23}=-(-2-1)=3 \\
A_{31}=(3-1)=2, & A_{32}=-(3-0)=-3, & A_{33}=(1-0)=1
\end{array}
$$

Hence $\operatorname{adj} \mathrm{A}=\left[\begin{array}{ccc}7 & -3 & 2 \\ 3 & 0 & -3 \\ -1 & 3 & 1\end{array}\right]$

Thus

$$
\mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|} \operatorname{adj}(\mathrm{A})=\frac{1}{9}\left[\begin{array}{ccc}
7 & -3 & 2 \\
3 & 0 & -3 \\
-1 & 3 & 1
\end{array}\right]
$$

Since

$$
\mathrm{X}=\mathrm{A}^{-1} \mathrm{~B}
$$

$$
\mathrm{X}=\frac{1}{9}\left[\begin{array}{ccc}
7 & -3 & 2 \\
3 & 0 & -3 \\
-1 & 3 & 1
\end{array}\right]\left[\begin{array}{c}
6 \\
11 \\
0
\end{array}\right]
$$

or

$$
\begin{aligned}
& x \\
& y \\
& z
\end{aligned}=\frac{1}{9}\left[\begin{array}{l}
42-33+0 \\
18+0+0 \\
-6+33+0
\end{array}\right]=\frac{1}{9} \begin{gathered}
9 \\
18 \\
27
\end{gathered}=\begin{aligned}
& 1 \\
& 2 \\
& 3
\end{aligned}
$$

Thus

$$
x=1, y=2, z=3
$$

## EXERCISE 4.5

Examine the consistency of the system of equations in Exercises 1 to 6.

1. $x+2 y=2$
$2 x+3 y=3$
2. $2 x-y=5$
$x+y=4$
3. $x+3 y=5$
$2 x+6 y=8$
4. $x+y+z=1$
$2 x+3 y+2 z=2$
$a x+a y+2 a z=4$
5. $3 x-y-2 z=2$
$2 y-z=-1$
$3 x-5 y=3$
6. $5 x-y+4 z=5$
$2 x+3 y+5 z=2$
$5 x-2 y+6 z=-1$

Solve system of linear equations, using matrix method, in Exercises 7 to 14 .
7. $5 x+2 y=4$
$7 x+3 y=5$
8. $2 x-y=-2$
$3 x+4 y=3$
9. $4 x-3 y=3$
$3 x-5 y=7$
10. $5 x+2 y=3$
11. $2 x+y+z=1$
12. $x-y+z=4$
$3 x+2 y=5$
$x-2 y-z=\frac{3}{2}$
$3 y-5 z=9$
$2 x+y-3 z=0$
$3 y-5 z=9$
$x+y+z=2$
13. $2 x+3 y+3 z=5$
$x-2 y+z=-4$
$3 x-y-2 z=3$
14. $x-y+2 z=7$
$3 x+4 y-5 z=-5$
$2 x-y+3 z=12$
15. If $A=\left[\begin{array}{rrr}2 & -3 & 5 \\ 3 & 2 & -4 \\ 1 & 1 & -2\end{array}\right]$, find $A^{-1}$. Using $A^{-1}$ solve the system of equations

$$
\begin{aligned}
2 x-3 y+5 z & =11 \\
3 x+2 y-4 z & =-5 \\
x+y-2 z & =-3
\end{aligned}
$$

16. The cost of 4 kg onion, 3 kg wheat and 2 kg rice is $₹ 60$. The cost of 2 kg onion, 4 kg wheat and 6 kg rice is ₹ 90 . The cost of 6 kg onion 2 kg wheat and 3 kg rice is ₹ 70 . Find cost of each item per kg by matrix method.

## Miscellaneous Examples

$\begin{array}{llllll}1 & 1 & 2 & 2 & 0 & 1\end{array}$
Example 19 Use product $\begin{array}{llllll}0 & 2 & 3 & 9 & 2 & 3\end{array}$ to solve the system of equations $\begin{array}{llllll}3 & 2 & 4 & 6 & 1 & 2\end{array}$

$$
\begin{array}{r}
x-y+2 z=1 \\
2 y-3 z=1 \\
3 x-2 y+4 z=2
\end{array}
$$

Solution Consider the product $\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right]\left[\begin{array}{ccc}-2 & 0 & 1 \\ 9 & 2 & -3 \\ 6 & 1 & -2\end{array}\right]$

$$
\begin{gathered}
=\left[\begin{array}{ccc}
-2-9+12 & 0-2+2 & 1+3-4 \\
0+18-18 & 0+4-3 & 0-6+6 \\
-6-18+24 & 0-4+4 & 3+6-8
\end{array}\right]=\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array} \\
\begin{array}{ccccc}
1 & -1 & 2^{-1} & -2 & 0 \\
0 & 2 & -3 & 1 \\
3 & -2 & 4 & -9 & 2
\end{array} \\
6
\end{gathered}
$$

Now, given system of equations can be written, in matrix form, as follows

$$
\left[\begin{array}{ccc}
1 & -1 & 2 \\
0 & 2 & -3 \\
3 & -2 & 4
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right]
$$

or

$$
\begin{aligned}
x & =\left[\begin{array}{rrr}
1 & -1 & 2 \\
y & 2 & -3 \\
z & -2 & 4
\end{array}\right]^{-1}\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right]=\left[\begin{array}{cccc}
2 & 0 & 1 & 1 \\
9 & 2 & 3 & 1 \\
6 & 1 & 2 & 2
\end{array}\right. \\
& =\left[\begin{array}{r}
-2+0+2 \\
9+2-6 \\
6+1-4
\end{array}\right]=\left[\begin{array}{l}
0 \\
5 \\
3
\end{array}\right] \\
x & =0, y=5 \text { and } z=3
\end{aligned}
$$

Hence

## Miscellaneous Exercises on Chapter 4

1. Prove that the determinant $\left|\begin{array}{ccc}x & \sin \theta & \cos \theta \\ -\sin \theta & -x & 1 \\ \cos \theta & 1 & x\end{array}\right|$ is independent of $\theta$.
2. Evaluate $\left|\begin{array}{ccc}\cos \alpha \cos \beta & \cos \alpha \sin \beta & -\sin \alpha \\ -\sin \beta & \cos \beta & 0 \\ \sin \alpha \cos \beta & \sin \alpha \sin \beta & \cos \alpha\end{array}\right|$.
3. If $\mathrm{A}^{-1}=\left[\begin{array}{ccc}3 & -1 & 1 \\ -15 & 6 & -5 \\ 5 & -2 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}1 & 2 & -2 \\ -1 & 3 & 0 \\ 0 & -2 & 1\end{array}\right]$, find $(\mathrm{AB})^{-1}$
4. Let $\mathrm{A}=\begin{array}{cccc}2 & 3 & 1 \\ 1 & 1 & 5\end{array}$. Verify that
(i) $[\operatorname{adj} \mathrm{A}]^{-1}=\operatorname{adj}\left(\mathrm{A}^{-1}\right)$
(ii) $\left(\mathrm{A}^{-1}\right)^{-1}=\mathrm{A}$
5. Evaluate $\left|\begin{array}{ccc}x & y & x+y \\ y & x+y & x \\ x+y & x & y\end{array}\right|$
6. Evaluate $\left|\begin{array}{ccc}1 & x & y \\ 1 & x+y & y \\ 1 & x & x+y\end{array}\right|$

Using properties of determinants in Exercises 11 to 15, prove that:
7. Solve the system of equations

$$
\begin{aligned}
& \frac{2}{x}+\frac{3}{y}+\frac{10}{z}=4 \\
& \frac{4}{x}-\frac{6}{y}+\frac{5}{z}=1 \\
& \frac{6}{x}+\frac{9}{y}-\frac{20}{z}=2
\end{aligned}
$$

Choose the correct answer in Exercise 17 to 19.
8. If $x, y, z$ are nonzero real numbers, then the inverse of matrix $\mathrm{A}=\left[\begin{array}{ccc}x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z\end{array}\right]$ is
(A) $\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
(B) $x y z\left[\begin{array}{ccc}x^{-1} & 0 & 0 \\ 0 & y^{-1} & 0 \\ 0 & 0 & z^{-1}\end{array}\right]$
(C) $\frac{1}{x y z}\left[\begin{array}{ccc}x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z\end{array}\right]$
(D) $\frac{1}{x y z}\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$
9. Let $\mathrm{A}=\left[\begin{array}{ccc}1 & \sin \theta & 1 \\ -\sin \theta & 1 & \sin \theta \\ -1 & -\sin \theta & 1\end{array}\right]$, where $0 \leq \theta \leq 2 \pi$. Then
(A) $\operatorname{Det}(\mathrm{A})=0$
(B) $\operatorname{Det}(A) \in(2, \infty)$
(C) $\operatorname{Det}(\mathrm{A}) \in(2,4)$
(D) $\operatorname{Det}(\mathrm{A}) \in[2,4]$

## Summary

- Determinant of a matrix $\mathrm{A}=\left[a_{11}\right]_{1 \times 1}$ is given by $\left|a_{11}\right|=a_{11}$
- Determinant of a matrix $\mathrm{A}=\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22}\end{array}$ is given by

$$
|\mathrm{A}|=\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|=a_{11} a_{22}-a_{12} a_{21}
$$

$$
a_{1} \quad b_{1} \quad c_{1}
$$

- Determinant of a matrix $\mathrm{A}=a_{2} \quad b_{2} \quad c_{2}$ is given by (expanding along $\mathrm{R}_{1}$ )

$$
|\mathrm{A}|=\left|\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right|=a_{1}\left|\begin{array}{cc}
b_{2} & c_{2} \\
b_{3} & c_{3}
\end{array}\right|-b_{1}\left|\begin{array}{cc}
a_{2} & c_{2} \\
a_{3} & c_{3}
\end{array}\right|+c_{1}\left|\begin{array}{cc}
a_{2} & b_{2} \\
a_{3} & b_{3}
\end{array}\right|
$$

## For any square matrix $A$, the $|A|$ satisfy following properties.

- Area of a triangle with vertices $\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right)$ and $\left(x_{3}, y_{3}\right)$ is given by

$$
\Delta=\frac{1}{2}\left|\begin{array}{lll}
x_{1} & y_{1} & 1 \\
x_{2} & y_{2} & 1 \\
x_{3} & y_{3} & 1
\end{array}\right|
$$

- Minor of an element $a_{i j}$ of the determinant of matrix A is the determinant obtained by deleting $i^{\text {th }}$ row and $j^{\text {th }}$ column and denoted by $\mathrm{M}_{i j}$.
- Cofactor of $a_{i j}$ of given by $\mathrm{A}_{i j}=(-1)^{i+j} \mathrm{M}_{i j}$
- Value of determinant of a matrix A is obtained by sum of product of elements of a row (or a column) with corresponding cofactors. For example,

$$
|\mathrm{A}|=a_{11} \mathrm{~A}_{11}+a_{12} \mathrm{~A}_{12}+a_{13} \mathrm{~A}_{13} .
$$

- If elements of one row (or column) are multiplied with cofactors of elements of any other row (or column), then their sum is zero. For example, $a_{11} \mathrm{~A}_{21}+a_{12}$ $\mathrm{A}_{22}+a_{13} \mathrm{~A}_{23}=0$

If $\mathrm{A}=\left[\begin{array}{lll}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}\end{array}\right]$, then $\operatorname{adj} \mathrm{A}=\left[\begin{array}{lll}\mathrm{A}_{11} & \mathrm{~A}_{21} & \mathrm{~A}_{31} \\ \mathrm{~A}_{12} & \mathrm{~A}_{22} & \mathrm{~A}_{32} \\ \mathrm{~A}_{13} & \mathrm{~A}_{23} & \mathrm{~A}_{33}\end{array}\right]$, where $\mathrm{A}_{i j}$ is cofactor of $a_{i j}$

- $\mathrm{A}(\operatorname{adj} \mathrm{A})=(\operatorname{adj} \mathrm{A}) \mathrm{A}=|\mathrm{A}| \mathrm{I}$, where A is square matrix of order $n$.
- A square matrix A is said to be singular or non-singular according as $|\mathrm{A}|=0$ or $|\mathrm{A}| \neq 0$.
- If $\mathrm{AB}=\mathrm{BA}=\mathrm{I}$, where B is square matrix, then B is called inverse of A . Also $\mathrm{A}^{-1}=\mathrm{B}$ or $\mathrm{B}^{-1}=\mathrm{A}$ and hence $\left(\mathrm{A}^{-1}\right)^{-1}=\mathrm{A}$.
- A square matrix A has inverse if and only if A is non-singular.
- $\mathrm{A}^{-1}=\frac{1}{|\mathrm{~A}|}(\operatorname{adj} \mathrm{A})$
- If $a_{1} x+b_{1} y+c_{1} z=d_{1}$
$a_{2} x+b_{2} y+c_{2} z=d_{2}$
$a_{3} x+b_{3} y+c_{3} z=d_{3}$,
then these equations can be written as $\mathrm{AX}=\mathrm{B}$, where

$$
\mathrm{A}=\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right], \mathrm{X}=\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right] \text { and } \mathrm{B}=\left[\begin{array}{l}
d_{1} \\
d_{2} \\
d_{3}
\end{array}\right]
$$

- Unique solution of equation $A X=B$ is given by $X=A^{-1} B$, where $|A| \neq 0$.
- A system of equation is consistent or inconsistent according as its solution exists or not.
- For a square matrix A in matrix equation $\mathrm{AX}=\mathrm{B}$
(i) $|\mathrm{A}| \neq 0$, there exists unique solution
(ii) $|\mathrm{A}|=0$ and $(\operatorname{adj} \mathrm{A}) \mathrm{B} \neq 0$, then there exists no solution
(iii) $|\mathrm{A}|=0$ and $(\operatorname{adj} \mathrm{A}) \mathrm{B}=0$, then system may or may not be consistent.


## Historical Note

The Chinese method of representing the coefficients of the unknowns of several linear equations by using rods on a calculating board naturally led to the discovery of simple method of elimination. The arrangement of rods was precisely that of the numbers in a determinant. The Chinese, therefore, early developed the idea of subtracting columns and rows as in simplification of a determinant Mikami, China, pp 30, 93.

Seki Kowa, the greatest of the Japanese Mathematicians of seventeenth century in his work 'Kai Fukudai no Ho' in 1683 showed that he had the idea of determinants and of their expansion. But he used this device only in eliminating a quantity from two equations and not directly in the solution of a set of simultaneous linear equations. T. Hayashi, "The Fakudoi and Determinants in Japanese Mathematics," in the proc. of the Tokyo Math. Soc., V.

Vendermonde was the first to recognise determinants as independent functions. He may be called the formal founder. Laplace (1772), gave general method of expanding a determinant in terms of its complementary minors. In 1773 Lagrange treated determinants of the second and third orders and used them for purpose other than the solution of equations. In 1801, Gauss used determinants in his theory of numbers.

The next great contributor was Jacques - Philippe - Marie Binet, (1812) who stated the theorem relating to the product of two matrices of $m$-columns and $n$ rows, which for the special case of $m=n$ reduces to the multiplication theorem.

Also on the same day, Cauchy (1812) presented one on the same subject. He used the word 'determinant' in its present sense. He gave the proof of multiplication theorem more satisfactory than Binet's.

The greatest contributor to the theory was Carl Gustav Jacob Jacobi, after this the word determinant received its final acceptance.

