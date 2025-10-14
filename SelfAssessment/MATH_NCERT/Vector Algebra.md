## VECTOR ALGEBRA

In most sciences one generation tears down what another has built and what one has established another undoes. In Mathematics alone each generation builds a new story to the old structure. - HERMAN HANKEL

### 10.1 Introduction

In our day to day life, we come across many queries such as - What is your height? How should a football player hit the ball to give a pass to another player of his team? Observe that a possible answer to the first query may be 1.6 meters, a quantity that involves only one value (magnitude) which is a real number. Such quantities are called scalars. However, an answer to the second query is a quantity (called force) which involves muscular strength (magnitude) and direction (in which another player is positioned). Such quantities are called vectors. In mathematics, physics and engineering, we frequently come across with both types of quantities, namely, scalar quantities such as length, mass,
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-01.jpg?height=618&width=407&top_left_y=873&top_left_x=996) time, distance, speed, area, volume, temperature, work, money, voltage, density, resistance etc. and vector quantities like displacement, velocity, acceleration, force, weight, momentum, electric field intensity etc.

In this chapter, we will study some of the basic concepts about vectors, various operations on vectors, and their algebraic and geometric properties. These two type of properties, when considered together give a full realisation to the concept of vectors, and lead to their vital applicability in various areas as mentioned above.

### 10.2 Some Basic Concepts

Let ' $l$ ' be any straight line in plane or three dimensional space. This line can be given two directions by means of arrowheads. A line with one of these directions prescribed is called a directed line (Fig 10.1 (i), (ii)).
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-02.jpg?height=436&width=905&top_left_y=263&top_left_x=299)

Fig 10.1
Now observe that if we restrict the line $l$ to the line segment AB , then a magnitude is prescribed on the line $l$ with one of the two directions, so that we obtain a directed line segment (Fig 10.1(iii)). Thus, a directed line segment has magnitude as well as direction.
Definition 1 A quantity that has magnitude as well as direction is called a vector.
Notice that a directed line segment is a vector (Fig 10.1(iii)), denoted as $\overrightarrow{\mathrm{AB}}$ or simply as $\vec{a}$, and read as 'vector $\overrightarrow{\mathrm{AB}}$ ' or 'vector $\vec{a}$ '.

The point A from where the vector $\overrightarrow{\mathrm{AB}}$ starts is called its initial point, and the point B where it ends is called its terminal point. The distance between initial and terminal points of a vector is called the magnitude (or length) of the vector, denoted as $|\overrightarrow{\mathrm{AB}}|$, or $|\vec{a}|$, or $a$. The arrow indicates the direction of the vector.
$\approx$ Note Since the length is never negative, the notation $|\vec{a}|<0$ has no meaning.

## Position Vector

From Class XI, recall the three dimensional right handed rectangular coordinate system (Fig 10.2(i)). Consider a point P in space, having coordinates ( $x, y, z$ ) with respect to the origin $\mathrm{O}(0,0,0)$. Then, the vector $\overrightarrow{\mathrm{OP}}$ having O and P as its initial and terminal points, respectively, is called the position vector of the point P with respect to O . Using distance formula (from Class XI), the magnitude of $\overrightarrow{\mathrm{OP}}$ (or $\vec{r}$ ) is given by

$$
|\overrightarrow{\mathrm{OP}}|=\sqrt{x^{2}+y^{2}+z^{2}}
$$

In practice, the position vectors of points $\mathrm{A}, \mathrm{B}, \mathrm{C}$, etc., with respect to the origin O are denoted by $\vec{a}, \vec{b}, \vec{c}$, etc., respectively (Fig 10.2 (ii)).
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-03.jpg?height=498&width=918&top_left_y=254&top_left_x=288)

Fig 10.2

## Direction Cosines

Consider the position vector $\overrightarrow{\mathrm{OP}}$ (or $\vec{r}$ ) of a point $\mathrm{P}(x, y, z$ ) as in Fig 10.3. The angles $\alpha$, $\beta, \gamma$ made by the vector $\vec{r}$ with the positive directions of $x, y$ and $z$-axes respectively, are called its direction angles. The cosine values of these angles, i.e., $\cos \alpha, \cos \beta$ and $\cos \gamma$ are called direction cosines of the vector $\vec{r}$, and usually denoted by $l, m$ and $n$, respectively.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-03.jpg?height=715&width=922&top_left_y=1040&top_left_x=282)

From Fig 10.3, one may note that the triangle OAP is right angled, and in it, we have $\cos \alpha=\frac{x}{r}$ ( $r$ stands for $|\vec{r}|$ ). Similarly, from the right angled triangles OBP and OCP, we may write $\cos \beta=\frac{y}{r}$ and $\cos \gamma=\frac{z}{r}$. Thus, the coordinates of the point P may also be expressed as ( $l r, m r, n r$ ). The numbers $l r, m r$ and $n r$, proportional to the direction cosines are called as direction ratios of vector $\vec{r}$, and denoted as $a, b$ and $c$, respectively.
$\approx$ Note One may note that $l^{2}+m^{2}+n^{2}=1$ but $a^{2}+b^{2}+c^{2} \neq 1$, in general.

### 10.3 Types of Vectors

Zero Vector A vector whose initial and terminal points coincide, is called a zero vector (or null vector), and denoted as $\overrightarrow{0}$. Zero vector can not be assigned a definite direction as it has zero magnitude. Or, alternatively otherwise, it may be regarded as having any direction. The vectors $\overrightarrow{\mathrm{AA}}, \overrightarrow{\mathrm{BB}}$ represent the zero vector,

Unit Vector A vector whose magnitude is unity (i.e., 1 unit) is called a unit vector. The unit vector in the direction of a given vector $\vec{a}$ is denoted by $\hat{a}$.

Coinitial Vectors Two or more vectors having the same initial point are called coinitial vectors.

Collinear Vectors Two or more vectors are said to be collinear if they are parallel to the same line, irrespective of their magnitudes and directions.
Equal Vectors Two vectors $\vec{a}$ and $\vec{b}$ are said to be equal, if they have the same magnitude and direction regardless of the positions of their initial points, and written as $\vec{a}=\vec{b}$.

Negative of a Vector A vector whose magnitude is the same as that of a given vector (say, $\overrightarrow{A B}$ ), but direction is opposite to that of it, is called negative of the given vector. For example, vector $\overrightarrow{\mathrm{BA}}$ is negative of the vector $\overrightarrow{\mathrm{AB}}$, and written as $\overrightarrow{\mathrm{BA}}=-\overrightarrow{\mathrm{AB}}$.

Remark The vectors defined above are such that any of them may be subject to its parallel displacement without changing its magnitude and direction. Such vectors are called free vectors. Throughout this chapter, we will be dealing with free vectors only.

Example 1 Represent graphically a displacement of $40 \mathrm{~km}, 30^{\circ}$ west of south.

Solution The vector $\overrightarrow{\mathrm{OP}}$ represents the required displacement (Fig 10.4).

Example 2 Classify the following measures as scalars and vectors.
(i) 5 seconds
(ii) $1000 \mathrm{~cm}^{3}$
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-04.jpg?height=480&width=524&top_left_y=1551&top_left_x=878)
(iii) 10 Newton
(iv) $30 \mathrm{~km} / \mathrm{hr}$
(v) $10 \mathrm{~g} / \mathrm{cm}^{3}$
(vi) $20 \mathrm{~m} / \mathrm{s}$ towards north

## Solution

(i) Time-scalar
(ii) Volume-scalar
(iii) Force-vector
(iv) Speed-scalar
(v) Density-scalar
(vi) Velocity-vector

Example 3 In Fig 10.5, which of the vectors are:
(i) Collinear
(ii) Equal
(iii) Coinitial

## Solution

(i) Collinear vectors: $\vec{a}, \vec{c}$ and $\vec{d}$.
(ii) Equal vectors: $\vec{a}$ and $\vec{c}$.
(iii) Coinitial vectors: $\vec{b}, \vec{c}$ and $\vec{d}$.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-05.jpg?height=364&width=536&top_left_y=686&top_left_x=842)

## EXERCISE 10.1

1. Represent graphically a displacement of $40 \mathrm{~km}, 30^{\circ}$ east of north.
2. Classify the following measures as scalars and vectors.
(i) 10 kg
(ii) 2 meters north-west
(iii) $40^{\circ}$
(iv) 40 watt
(v) $10^{-19}$ coulomb
(vi) $20 \mathrm{~m} / \mathrm{s}^{2}$
3. Classify the following as scalar and vector quantities.
(i) time period
(ii) distance
(iii) force
(iv) velocity
(v) work done
4. In Fig 10.6 (a square), identify the following vectors.
(i) Coinitial
(ii) Equal
(iii) Collinear but not equal
5. Answer the following as true or false.
(i) $\vec{a}$ and $-\vec{a}$ are collinear.
(ii) Two collinear vectors are always equal in magnitude.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-05.jpg?height=423&width=421&top_left_y=1483&top_left_x=978)

Fig 10.6
(iii) Two vectors having same magnitude are collinear.
(iv) Two collinear vectors having the same magnitude are equal.

### 10.4 Addition of Vectors

A vector $\overrightarrow{\mathrm{AB}}$ simply means the displacement from a point A to the point B . Now consider a situation that a girl moves from A to B and then from B to C (Fig 10.7). The net displacement made by the girl from point A to the point C , is given by the vector $\overrightarrow{\mathrm{AC}}$ and expressed as
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-06.jpg?height=297&width=454&top_left_y=269&top_left_x=951)

Fig 10.7

$$
\overrightarrow{\mathrm{AC}}=\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}}
$$

This is known as the triangle law of vector addition.
In general, if we have two vectors $\vec{a}$ and $\vec{b}$ (Fig 10.8 (i)), then to add them, they are positioned so that the initial point of one coincides with the terminal point of the other (Fig 10.8(ii)).
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-06.jpg?height=450&width=1294&top_left_y=966&top_left_x=109)

Fig 10.8
For example, in Fig 10.8 (ii), we have shifted vector $\vec{b}$ without changing its magnitude and direction, so that it's initial point coincides with the terminal point of $\vec{a}$. Then, the vector $\vec{a}+\vec{b}$, represented by the third side AC of the triangle ABC , gives us the sum (or resultant) of the vectors $\vec{a}$ and $\vec{b}$ i.e., in triangle ABC (Fig 10.8 (ii)), we have

$$
\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}}=\overrightarrow{\mathrm{AC}}
$$

Now again, since $\overrightarrow{\mathrm{AC}}=-\overrightarrow{\mathrm{CA}}$, from the above equation, we have

$$
\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}}+\overrightarrow{\mathrm{CA}}=\overrightarrow{\mathrm{AA}}=\overrightarrow{0}
$$

This means that when the sides of a triangle are taken in order, it leads to zero resultant as the initial and terminal points get coincided (Fig 10.8(iii)).

Now, construct a vector $\overrightarrow{\mathrm{BC}^{\prime}}$ so that its magnitude is same as the vector $\overrightarrow{\mathrm{BC}}$, but the direction opposite to that of it (Fig 10.8 (iii)), i.e.,

$$
\overrightarrow{\mathrm{BC}^{\prime}}=-\overrightarrow{\mathrm{BC}}
$$

Then, on applying triangle law from the Fig 10.8 (iii), we have

$$
\overrightarrow{\mathrm{AC}^{\prime}}=\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}^{\prime}}=\overrightarrow{\mathrm{AB}}+(-\overrightarrow{\mathrm{BC}})=\vec{a}-\vec{b}
$$

The vector $\overrightarrow{\mathrm{AC}^{\prime}}$ is said to represent the difference of $\vec{a}$ and $\vec{b}$.
Now, consider a boat in a river going from one bank of the river to the other in a direction perpendicular to the flow of the river. Then, it is acted upon by two velocity vectors-one is the velocity imparted to the boat by its engine and other one is the velocity of the flow of river water. Under the simultaneous influence of these two velocities, the boat in actual starts travelling with a different velocity. To have a precise idea about the effective speed and direction (i.e., the resultant velocity) of the boat, we have the following law of vector addition.

If we have two vectors $\vec{a}$ and $\vec{b}$ represented by the two adjacent sides of a parallelogram in magnitude and direction (Fig 10.9), then their sum $\vec{a}+\vec{b}$ is represented in magnitude and direction by the diagonal of the parallelogram through their common point. This is known as the parallelogram law of vector addition.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-07.jpg?height=447&width=592&top_left_y=884&top_left_x=811)

Fig 10.9

Note From Fig 10.9, using the triangle law, one may note that

$$
\begin{aligned}
& \overrightarrow{\mathrm{OA}}+\overrightarrow{\mathrm{AC}}=\overrightarrow{\mathrm{OC}} \\
& \overrightarrow{\mathrm{OA}}+\overrightarrow{\mathrm{OB}}=\overrightarrow{\mathrm{OC}}
\end{aligned}
$$

(since $\overrightarrow{\mathrm{AC}}=\overrightarrow{\mathrm{OB}}$ )
which is parallelogram law. Thus, we may say that the two laws of vector addition are equivalent to each other.

## Properties of vector addition

Property 1 For any two vectors $\vec{a}$ and $\vec{b}$,

$$
\vec{a}+\vec{b}=\vec{b}+\vec{a}
$$

(Commutative property)

## Proof Consider the parallelogram ABCD

(Fig 10.10). Let $\overrightarrow{\mathrm{AB}}=\vec{a}$ and $\overrightarrow{\mathrm{BC}}=\vec{b}$, then using the triangle law, from triangle ABC , we have

$$
\overrightarrow{\mathrm{AC}}=\vec{a}+\vec{b}
$$

Now, since the opposite sides of a parallelogram are equal and parallel, from Fig 10.10 , we have, $\overrightarrow{\mathrm{AD}}=\overrightarrow{\mathrm{BC}}=\vec{b}$ and $\overrightarrow{\mathrm{DC}}=\overrightarrow{\mathrm{AB}}=\vec{a}$. Again using triangle law, from
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-08.jpg?height=443&width=587&top_left_y=264&top_left_x=816)

Fig 10.10 triangle ADC, we have

Hence

$$
\begin{aligned}
& \overrightarrow{\mathrm{AC}}=\overrightarrow{\mathrm{AD}}+\overrightarrow{\mathrm{DC}}=\vec{b}+\vec{a} \\
\vec{a}+\vec{b}=\vec{b}+\vec{a} &
\end{aligned}
$$

Property 2 For any three vectors $a, b$ and $c$

$$
(\vec{a}+\vec{b})+\vec{c}=\vec{a}+(\vec{b}+\vec{c})
$$

(Associative property)
Proof Let the vectors $\vec{a}, \vec{b}$ and $\vec{c}$ be represented by $\overrightarrow{\mathrm{PQ}}, \overrightarrow{\mathrm{QR}}$ and $\overrightarrow{\mathrm{RS}}$, respectively, as shown in Fig 10.11(i) and (ii).
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-08.jpg?height=484&width=1093&top_left_y=1252&top_left_x=205)

Fig 10.11
Then

$$
\vec{a}+\vec{b}=\overrightarrow{\mathrm{PQ}}+\overrightarrow{\mathrm{QR}}=\overrightarrow{\mathrm{PR}}
$$

and

$$
\vec{b}+\vec{c}=\overrightarrow{\mathrm{QR}}+\overrightarrow{\mathrm{RS}}=\overrightarrow{\mathrm{QS}}
$$

So

$$
(\vec{a}+\vec{b})+\vec{c}=\overrightarrow{\mathrm{PR}}+\overrightarrow{\mathrm{RS}}=\overrightarrow{\mathrm{PS}}
$$

and

$$
\begin{aligned}
& \vec{a}+(\vec{b}+\vec{c})=\overrightarrow{\mathrm{PQ}}+\overrightarrow{\mathrm{QS}}=\overrightarrow{\mathrm{PS}} \\
& (\vec{a}+\vec{b})+\vec{c}=\vec{a}+(\vec{b}+\vec{c})
\end{aligned}
$$

Hence
Remark The associative property of vector addition enables us to write the sum of three vectors $\vec{a}, \vec{b}, \vec{c}$ as $\vec{a}+\vec{b}+\vec{c}$ without using brackets.

Note that for any vector $a$, we have

$$
\vec{a}+\overrightarrow{0}=\overrightarrow{0}+\vec{a}=\vec{a}
$$

Here, the zero vector $\overrightarrow{0}$ is called the additive identity for the vector addition.

### 10.5 Multiplication of a Vector by a Scalar

Let $\vec{a}$ be a given vector and $\lambda$ a scalar. Then the product of the vector $\vec{a}$ by the scalar $\lambda$, denoted as $\lambda \vec{a}$, is called the multiplication of vector $\vec{a}$ by the scalar $\lambda$. Note that, $\lambda \vec{a}$ is also a vector, collinear to the vector $\vec{a}$. The vector $\lambda \vec{a}$ has the direction same (or opposite) to that of vector $\vec{a}$ according as the value of $\lambda$ is positive (or negative). Also, the magnitude of vector $\lambda \vec{a}$ is $|\lambda|$ times the magnitude of the vector $\vec{a}$, i.e.,

$$
|\lambda \vec{a}|=|\lambda||\vec{a}|
$$

A geometric visualisation of multiplication of a vector by a scalar is given in Fig 10.12.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-09.jpg?height=262&width=1277&top_left_y=1152&top_left_x=108)

Fig 10.12
When $\lambda=-1$, then $\lambda \vec{a}=-\vec{a}$, which is a vector having magnitude equal to the magnitude of $\vec{a}$ and direction opposite to that of the direction of $\vec{a}$. The vector $-\vec{a}$ is called the negative (or additive inverse) of vector $\vec{a}$ and we always have

$$
\vec{a}+(-\vec{a})=(-\vec{a})+\vec{a}=\overrightarrow{0}
$$

Also, if $\lambda=\frac{1}{|a|}$, provided $\vec{a} \neq 0$ i.e. $\vec{a}$ is not a null vector, then

$$
|\lambda \vec{a}|=|\lambda||\vec{a}|=\frac{1}{|\vec{a}|}|\vec{a}|=1
$$

So, $\lambda \vec{a}$ represents the unit vector in the direction of $\vec{a}$. We write it as

$$
\hat{a}=\frac{1}{|\vec{a}|} \vec{a}
$$

## Note For any scalar $k, k \overrightarrow{0}=\overrightarrow{0}$.

### 10.5.1 Components of a vector

Let us take the points $\mathrm{A}(1,0,0), \mathrm{B}(0,1,0)$ and $\mathrm{C}(0,0,1)$ on the $x$-axis, $y$-axis and $z$-axis, respectively. Then, clearly

$$
|\overrightarrow{\mathrm{OA}}|=1,|\overrightarrow{\mathrm{OB}}|=1 \text { and }|\overrightarrow{\mathrm{OC}}|=1
$$

The vectors $\overrightarrow{\mathrm{OA}}, \overrightarrow{\mathrm{OB}}$ and $\overrightarrow{\mathrm{OC}}$, each having magnitude 1 , are called unit vectors along the axes $\mathrm{OX}, \mathrm{OY}$ and OZ , respectively, and denoted by $\hat{i}, \hat{j}$ and $\hat{k}$, respectively (Fig 10.13).

Now, consider the position vector $\overrightarrow{\mathrm{OP}}$ of a point $\mathrm{P}(x, y, z)$
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-10.jpg?height=351&width=346&top_left_y=655&top_left_x=1057)

Fig 10.13 as in Fig 10.14. Let $\mathrm{P}_{1}$ be the foot of the perpendicular from P on the plane XOY.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-10.jpg?height=669&width=764&top_left_y=1155&top_left_x=387)

We, thus, see that $\mathrm{P}_{1} \mathrm{P}$ is parallel to $z$-axis. As $\hat{i}, \hat{j}$ and $\hat{k}$ are the unit vectors along the $x, y$ and $z$-axes, respectively, and by the definition of the coordinates of P , we have $\overrightarrow{\mathrm{P}_{1} \mathrm{P}}=\overrightarrow{\mathrm{OR}}=z \hat{k}$. Similarly, $\overrightarrow{\mathrm{QP}_{1}}=\overrightarrow{\mathrm{OS}}=y \hat{j}$ and $\overrightarrow{\mathrm{OQ}}=x \hat{i}$.

Therefore, it follows that and

$$
\begin{aligned}
& \overrightarrow{\mathrm{OP}_{1}}=\overrightarrow{\mathrm{OQ}}+\overrightarrow{\mathrm{QP}_{1}}=x \hat{i}+y \hat{j} \\
& \overrightarrow{\mathrm{OP}}=\overrightarrow{\mathrm{OP}_{1}}+\overrightarrow{\mathrm{P}_{1} \mathrm{P}}=x \hat{i}+y \hat{j}+z \hat{k}
\end{aligned}
$$

Hence, the position vector of P with reference to O is given by

$$
\overrightarrow{\mathrm{OP}}(\text { or } \vec{r})=x \hat{i}+y \hat{j}+z \hat{k}
$$

This form of any vector is called its component form. Here, $x, y$ and $z$ are called as the scalar components of $\vec{r}$, and $x \hat{i}, y \hat{j}$ and $z \hat{k}$ are called the vector components of $\vec{r}$ along the respective axes. Sometimes $x, y$ and $z$ are also termed as rectangular components.

The length of any vector $\vec{r}=x \hat{i}+y \hat{j}+z \hat{k}$, is readily determined by applying the Pythagoras theorem twice. We note that in the right angle triangle $\mathrm{OQP}_{1}$ (Fig 10.14)

$$
\left|\overrightarrow{\mathrm{OP}_{1}}\right|=\sqrt{|\overrightarrow{\mathrm{OQ}}|^{2}+\left|\overrightarrow{\mathrm{QP}_{1}}\right|^{2}}=\sqrt{x^{2}+y^{2}}
$$

and in the right angle triangle $\mathrm{OP}_{1} \mathrm{P}$, we have

$$
\overrightarrow{\mathrm{OP}}=\sqrt{\left|\overrightarrow{\mathrm{OP}_{1}}\right|^{2}+\left|\overrightarrow{\mathrm{P}_{1} \mathrm{P}}\right|^{2}}=\sqrt{\left(x^{2}+y^{2}\right)+z^{2}}
$$

Hence, the length of any vector $\vec{r}=x \hat{i}+y \hat{j}+z \hat{k}$ is given by

$$
|\vec{r}|=|x \hat{i}+y \hat{j}+z \hat{k}|=\sqrt{x^{2}+y^{2}+z^{2}}
$$

If $\vec{a}$ and $\vec{b}$ are any two vectors given in the component form $a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$ and $b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}$, respectively, then
(i) the sum (or resultant) of the vectors $\vec{a}$ and $\vec{b}$ is given by

$$
\vec{a}+\vec{b}=\left(a_{1}+b_{1}\right) \hat{i}+\left(a_{2}+b_{2}\right) \hat{j}+\left(a_{3}+b_{3}\right) \hat{k}
$$

(ii) the difference of the vector $\vec{a}$ and $\vec{b}$ is given by

$$
\vec{a}-\vec{b}=\left(a_{1}-b_{1}\right) \hat{i}+\left(a_{2}-b_{2}\right) \hat{j}+\left(a_{3}-b_{3}\right) \hat{k}
$$

(iii) the vectors $\vec{a}$ and $\vec{b}$ are equal if and only if

$$
a_{1}=b_{1}, a_{2}=b_{2} \quad \text { and } \quad a_{3}=b_{3}
$$

(iv) the multiplication of vector $\vec{a}$ by any scalar $\lambda$ is given by

$$
\lambda \vec{a}=\left(\lambda a_{1}\right) \hat{i}+\left(\lambda a_{2}\right) \hat{j}+\left(\lambda a_{3}\right) \hat{k}
$$

The addition of vectors and the multiplication of a vector by a scalar together give the following distributive laws:

Let $\vec{a}$ and $\vec{b}$ be any two vectors, and $k$ and $m$ be any scalars. Then
(i) $k \vec{a}+m \vec{a}=(k+m) \vec{a}$
(ii) $k(m \vec{a})=(k m) \vec{a}$
(iii) $k(\vec{a}+\vec{b})=k \vec{a}+k \vec{b}$

## Remarks

(i) One may observe that whatever be the value of $\lambda$, the vector $\lambda \vec{a}$ is always collinear to the vector $\vec{a}$. In fact, two vectors $\vec{a}$ and $\vec{b}$ are collinear if and only if there exists a nonzero scalar $\lambda$ such that $\vec{b}=\lambda \vec{a}$. If the vectors $\vec{a}$ and $\vec{b}$ are given in the component form, i.e. $\vec{a}=a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$ and $\vec{b}=b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}$, then the two vectors are collinear if and only if

$$
\begin{array}{ll} 
& b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}=\lambda\left(a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}\right) \\
\Leftrightarrow & b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}=\left(\lambda a_{1}\right) \hat{i}+\left(\lambda a_{2}\right) \hat{j}+\left(\lambda a_{3}\right) \hat{k} \\
\Leftrightarrow & b_{1}=\lambda a_{1}, b_{2}=\lambda a_{2}, b_{3}=\lambda a_{3} \\
\Leftrightarrow & \frac{b_{1}}{a_{1}}=\frac{b_{2}}{a_{2}}=\frac{b_{3}}{a_{3}}=\lambda
\end{array}
$$

(ii) If $\vec{a}=a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$, then $a_{1}, a_{2}, a_{3}$ are also called direction ratios of $\vec{a}$.
(iii) In case if it is given that $l, m, n$ are direction cosines of a vector, then $l \hat{i}+m \hat{j}+n \hat{k}$ $=(\cos \alpha) \hat{i}+(\cos \beta) \hat{j}+(\cos \gamma) \hat{k}$ is the unit vector in the direction of that vector, where $\alpha, \beta$ and $\gamma$ are the angles which the vector makes with $x, y$ and $z$ axes respectively.

Example 4 Find the values of $x, y$ and $z$ so that the vectors $\vec{a}=x \hat{i}+2 \hat{j}+z \hat{k}$ and $\vec{b}=2 \hat{i}+y \hat{j}+\hat{k}$ are equal.

Solution Note that two vectors are equal if and only if their corresponding components are equal. Thus, the given vectors $\vec{a}$ and $\vec{b}$ will be equal if and only if

$$
x=2, y=2, z=1
$$

Example 5 Let $\vec{a}=\hat{i}+2 \hat{j}$ and $\vec{b}=2 \hat{i}+\hat{j}$. Is $|\vec{a}|=|\vec{b}|$ ? Are the vectors $\vec{a}$ and $\vec{b}$ equal?
Solution We have $|\vec{a}|=\sqrt{1^{2}+2^{2}}=\sqrt{5}$ and $|\vec{b}|=\sqrt{2^{2}+1^{2}}=\sqrt{5}$
So, $|\vec{a}|=|\vec{b}|$. But, the two vectors are not equal since their corresponding components are distinct.

Example 6 Find unit vector in the direction of vector $\vec{a}=2 \hat{i}+3 \hat{j}+\hat{k}$
Solution The unit vector in the direction of a vector $\vec{a}$ is given by $\hat{a}=\frac{1}{|\vec{a}|} \vec{a}$.
Now

$$
|\vec{a}|=\sqrt{2^{2}+3^{2}+1^{2}}=\sqrt{14}
$$

Therefore

$$
\hat{a}=\frac{1}{\sqrt{14}}(2 \hat{i}+3 \hat{j}+\hat{k})=\frac{2}{\sqrt{14}} \hat{i}+\frac{3}{\sqrt{14}} \hat{j}+\frac{1}{\sqrt{14}} \hat{k}
$$

Example 7 Find a vector in the direction of vector $\vec{a}=\hat{i}-2 \hat{j}$ that has magnitude 7 units.

Solution The unit vector in the direction of the given vector $\vec{a}$ is

$$
\hat{a}=\frac{1}{|\vec{a}|} \vec{a}=\frac{1}{\sqrt{5}}(\hat{i}-2 \hat{j})=\frac{1}{\sqrt{5}} \hat{i}-\frac{2}{\sqrt{5}} \hat{j}
$$

Therefore, the vector having magnitude equal to 7 and in the direction of $\vec{a}$ is

$$
7 \hat{a}=7\left(\frac{1}{\sqrt{5}} \hat{i}-\frac{2}{\sqrt{5}} \hat{j}\right)=\frac{7}{\sqrt{5}} \hat{i}-\frac{14}{\sqrt{5}} \hat{j}
$$

Example 8 Find the unit vector in the direction of the sum of the vectors, $\vec{a}=2 \hat{i}+2 \hat{j}-5 \hat{k}$ and $\vec{b}=2 \hat{i}+\hat{j}+3 \hat{k}$.

Solution The sum of the given vectors is

$$
\vec{a}+\vec{b}(=\vec{c}, \text { say })=4 \hat{i}+3 \hat{j}-2 \hat{k}
$$

and

$$
|\vec{c}|=\sqrt{4^{2}+3^{2}+(-2)^{2}}=\sqrt{29}
$$

Thus, the required unit vector is

$$
\hat{c}=\frac{1}{|\vec{c}|} \vec{c}=\frac{1}{\sqrt{29}}(4 \hat{i}+3 \hat{j}-2 \hat{k})=\frac{4}{\sqrt{29}} \hat{i}+\frac{3}{\sqrt{29}} \hat{j}-\frac{2}{\sqrt{29}} \hat{k}
$$

Example 9 Write the direction ratio's of the vector $\vec{a}=\hat{i}+\hat{j}-2 \hat{k}$ and hence calculate its direction cosines.

Solution Note that the direction ratio's $a, b, c$ of a vector $\vec{r}=x \hat{i}+y \hat{j}+z \hat{k}$ are just the respective components $x, y$ and $z$ of the vector. So, for the given vector, we have $a=1, b=1$ and $c=-2$. Further, if $l, m$ and $n$ are the direction cosines of the given vector, then

$$
1=\frac{a}{|\vec{r}|}=\frac{1}{\sqrt{6}}, \quad m=\frac{b}{|\vec{r}|}=\frac{1}{\sqrt{6}}, \quad n=\frac{c}{|\vec{r}|}=\frac{-2}{\sqrt{6}} \text { as }|\vec{r}|=\sqrt{6}
$$

Thus, the direction cosines are $\left(\frac{1}{\sqrt{6}}, \frac{1}{\sqrt{6}},-\frac{2}{\sqrt{6}}\right)$.

### 10.5.2 Vector joining two points

If $\mathrm{P}_{1}\left(x_{1}, y_{1}, z_{1}\right)$ and $\mathrm{P}_{2}\left(x_{2}, y_{2}, z_{2}\right)$ are any two points, then the vector joining $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$ is the vector $\overrightarrow{\mathrm{P}_{1} \mathrm{P}_{2}}$ (Fig 10.15).

Joining the points $P_{1}$ and $P_{2}$ with the origin O , and applying triangle law, from the triangle $\mathrm{OP}_{1} \mathrm{P}_{2}$, we have

$$
\overrightarrow{\mathrm{OP}_{1}}+\overrightarrow{\mathrm{P}_{1} \mathrm{P}_{2}}=\overrightarrow{\mathrm{OP}_{2}}
$$

Using the properties of vector addition, the above equation becomes
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-14.jpg?height=447&width=579&top_left_y=1099&top_left_x=827)

$$
\overrightarrow{\mathrm{P}_{1} \mathrm{P}_{2}}=\overrightarrow{\mathrm{OP}_{2}}-\overrightarrow{\mathrm{OP}_{1}}
$$

i.e.

$$
\begin{aligned}
\overrightarrow{\mathrm{P}_{1} \mathrm{P}_{2}} & =\left(x_{2} \hat{i}+y_{2} \hat{j}+z_{2} \hat{k}\right)-\left(x_{1} \hat{i}+y_{1} \hat{j}+z_{1} \hat{k}\right) \\
& =\left(x_{2}-x_{1}\right) \hat{i}+\left(y_{2}-y_{1}\right) \hat{j}+\left(z_{2}-z_{1}\right) \hat{k}
\end{aligned}
$$

The magnitude of vector $\overrightarrow{\mathrm{P}_{1} \mathrm{P}_{2}}$ is given by

$$
\left|\overrightarrow{\mathrm{P}_{1} \mathrm{P}_{2}}\right|=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
$$

Example 10 Find the vector joining the points $\mathrm{P}(2,3,0)$ and $\mathrm{Q}(-1,-2,-4)$ directed from P to Q .

Solution Since the vector is to be directed from P to Q , clearly P is the initial point and Q is the terminal point. So, the required vector joining P and Q is the vector $\overrightarrow{\mathrm{PQ}}$, given by
i.e.

$$
\begin{aligned}
& \overrightarrow{\mathrm{PQ}}=(-1-2) \hat{i}+(-2-3) \hat{j}+(-4-0) \hat{k} \\
& \overrightarrow{\mathrm{PQ}}=-3 \hat{i}-5 \hat{j}-4 \hat{k} .
\end{aligned}
$$

### 10.5.3 Section formula

Let P and Q be two points represented by the position vectors $\overrightarrow{\mathrm{OP}}$ and $\overrightarrow{\mathrm{OQ}}$, respectively, with respect to the origin O . Then the line segment joining the points P and Q may be divided by a third point, say R, in two ways - internally (Fig 10.16) and externally (Fig 10.17). Here, we intend to find the position vector $\overrightarrow{\mathrm{OR}}$ for the point R with respect to the origin O . We take the two cases one by one.

Case I When R divides PQ internally (Fig 10.16). If R divides $\overrightarrow{\mathrm{PQ}}$ such that $m \overrightarrow{\mathrm{RQ}}=n \overrightarrow{\mathrm{PR}}$,
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-15.jpg?height=342&width=504&top_left_y=853&top_left_x=899)

Fig 10.16 where $m$ and $n$ are positive scalars, we say that the point R divides $\overrightarrow{\mathrm{PQ}}$ internally in the ratio of $m: n$. Now from triangles ORQ and OPR, we have
and

$$
\overrightarrow{\mathrm{RQ}}=\overrightarrow{\mathrm{OQ}}-\overrightarrow{\mathrm{OR}}=\vec{b}-\vec{r}
$$

Therefore, we have

$$
m(\vec{b}-\vec{r})=n(\vec{r}-\vec{a}) \quad \text { (Why?) }
$$

or

$$
\vec{r}=\frac{m \vec{b}+n \vec{a}}{m+n} \quad \text { (on simplification) }
$$

Hence, the position vector of the point R which divides P and Q internally in the ratio of $m: n$ is given by

$$
\overrightarrow{\mathrm{OR}}=\frac{m \vec{b}+n \vec{a}}{m+n}
$$

Case II When R divides PQ externally (Fig 10.17). We leave it to the reader as an exercise to verify that the position vector of the point R which divides the line segment PQ externally in the ratio $m: n$ i.e. $\frac{\mathrm{PR}}{\mathrm{QR}}=\frac{m}{n}$ is given by

$$
\overrightarrow{\mathrm{OR}}=\frac{m \vec{b}-n \vec{a}}{m-n}
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-16.jpg?height=390&width=504&top_left_y=262&top_left_x=895)

Fig 10.17

Remark If R is the midpoint of PQ , then $m=n$. And therefore, from Case I, the midpoint R of $\overrightarrow{\mathrm{PQ}}$, will have its position vector as

$$
\overrightarrow{\mathrm{OR}}=\frac{\vec{a}+\vec{b}}{2}
$$

Example 11 Consider two points P and Q with position vectors $\overrightarrow{\mathrm{OP}}=3 \vec{a}-2 \vec{b}$ and $\overrightarrow{\mathrm{OQ}}=\vec{a}+\vec{b}$. Find the position vector of a point R which divides the line joining P and Q in the ratio 2:1, (i) internally, and (ii) externally.

## Solution

(i) The position vector of the point R dividing the join of P and Q internally in the ratio 2:1 is

$$
\overrightarrow{\mathrm{OR}}=\frac{2(\vec{a}+\vec{b})+(3 \vec{a}-2 \vec{b})}{2+1}=\frac{5 \vec{a}}{3}
$$

(ii) The position vector of the point R dividing the join of P and Q externally in the ratio $2: 1$ is

$$
\overrightarrow{\mathrm{OR}}=\frac{2(\vec{a}+\vec{b})-(3 \vec{a}-2 \vec{b})}{2-1}=4 \vec{b}-\vec{a}
$$

Example 12 Show that the points $\mathrm{A}(2 \hat{i}-\hat{j}+\hat{k}), \mathrm{B}(\hat{i}-3 \hat{j}-5 \hat{k}), \mathrm{C}(3 \hat{i}-4 j-4 \hat{k})$ are the vertices of a right angled triangle.

Solution We have
and

$$
\begin{aligned}
& \overrightarrow{\mathrm{AB}}=(1-2) \hat{i}+(-3+1) \hat{j}+(-5-1) \hat{k}=-\hat{i}-2 \hat{j}-6 \hat{k} \\
& \overrightarrow{\mathrm{BC}}=(3-1) \hat{i}+(-4+3) \hat{j}+(-4+5) \hat{k}=2 \hat{i}-\hat{j}+\hat{k} \\
& \overrightarrow{\mathrm{CA}}=(2-3) \hat{i}+(-1+4) \hat{j}+(1+4) \hat{k}=-\hat{i}+3 \hat{j}+5 \hat{k}
\end{aligned}
$$

Further, note that

$$
|\overrightarrow{\mathrm{AB}}|^{2}=41=6+35=|\overrightarrow{\mathrm{BC}}|^{2}+|\overrightarrow{\mathrm{CA}}|^{2}
$$

Hence, the triangle is a right angled triangle.

## EXERCISE 10.2

1. Compute the magnitude of the following vectors:

$$
\vec{a}=\hat{i}+\hat{j}+k ; \quad \vec{b}=2 \hat{i}-7 \hat{j}-3 \hat{k} ; \quad \vec{c}=\frac{1}{\sqrt{3}} \hat{i}+\frac{1}{\sqrt{3}} \hat{j}-\frac{1}{\sqrt{3}} \hat{k}
$$

2. Write two different vectors having same magnitude.
3. Write two different vectors having same direction.
4. Find the values of $x$ and $y$ so that the vectors $2 \hat{i}+3 \hat{j}$ and $x \hat{i}+y \hat{j}$ are equal.
5. Find the scalar and vector components of the vector with initial point $(2,1)$ and terminal point $(-5,7)$.
6. Find the sum of the vectors $\vec{a}=\hat{i}-2 \hat{j}+\hat{k}, \vec{b}=-2 \hat{i}+4 \hat{j}+5 \hat{k}$ and $\vec{c}=\hat{i}-6 \hat{j}-7 \hat{k}$.
7. Find the unit vector in the direction of the vector $\vec{a}=\hat{i}+\hat{j}+2 \hat{k}$.
8. Find the unit vector in the direction of vector $\overrightarrow{\mathrm{PQ}}$, where P and Q are the points $(1,2,3)$ and (4, 5, 6), respectively.
9. For given vectors, $\vec{a}=2 \hat{i}-\hat{j}+2 \hat{k}$ and $\vec{b}=-\hat{i}+\hat{j}-\hat{k}$, find the unit vector in the direction of the vector $\vec{a}+\vec{b}$.
10. Find a vector in the direction of vector $5 \hat{i}-\hat{j}+2 \hat{k}$ which has magnitude 8 units.
11. Show that the vectors $2 \hat{i}-3 \hat{j}+4 \hat{k}$ and $-4 \hat{i}+6 \hat{j}-8 \hat{k}$ are collinear.
12. Find the direction cosines of the vector $\hat{i}+2 \hat{j}+3 \hat{k}$.
13. Find the direction cosines of the vector joining the points $A(1,2,-3)$ and $\mathrm{B}(-1,-2,1)$, directed from A to B .
14. Show that the vector $\hat{i}+\hat{j}+\hat{k}$ is equally inclined to the axes $\mathrm{OX}, \mathrm{OY}$ and OZ .
15. Find the position vector of a point $R$ which divides the line joining two points $P$ and Q whose position vectors are $\hat{i}+2 \hat{j}-\hat{k}$ and $-\hat{i}+\hat{j}+\hat{k}$ respectively, in the ratio 2 : 1
(i) internally
(ii) externally
16. Find the position vector of the mid point of the vector joining the points $\mathrm{P}(2,3,4)$ and $\mathrm{Q}(4,1,-2)$.
17. Show that the points $\mathrm{A}, \mathrm{B}$ and C with position vectors, $\vec{a}=3 \hat{i}-4 \hat{j}-4 \hat{k}$, $\vec{b}=2 \hat{i}-\hat{j}+\hat{k}$ and $\vec{c}=\hat{i}-3 \hat{j}-5 \hat{k}$, respectively form the vertices of a right angled triangle.
18. In triangle ABC (Fig 10.18), which of the following is not true:
(A) $\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}}+\overrightarrow{\mathrm{CA}}=\overrightarrow{0}$
(B) $\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}}-\overrightarrow{\mathrm{AC}}=\overrightarrow{0}$
(C) $\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}}-\overrightarrow{\mathrm{AC}}=\overrightarrow{0}$
(D) $\overrightarrow{\mathrm{AB}}-\overrightarrow{\mathrm{CB}}+\overrightarrow{\mathrm{CA}}=\overrightarrow{0}$
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-18.jpg?height=210&width=447&top_left_y=673&top_left_x=954)

Fig 10.18
19. If $\vec{a}$ and $\vec{b}$ are two collinear vectors, then which of the following are incorrect:
(A) $\vec{b}=\lambda \vec{a}$, for some scalar $\lambda$
(B) $\vec{a}= \pm \vec{b}$
(C) the respective components of $\vec{a}$ and $\vec{b}$ are not proportional
(D) both the vectors $\vec{a}$ and $\vec{b}$ have same direction, but different magnitudes.

### 10.6 Product of Two Vectors

So far we have studied about addition and subtraction of vectors. An other algebraic operation which we intend to discuss regarding vectors is their product. We may recall that product of two numbers is a number, product of two matrices is again a matrix. But in case of functions, we may multiply them in two ways, namely, multiplication of two functions pointwise and composition of two functions. Similarly, multiplication of two vectors is also defined in two ways, namely, scalar (or dot) product where the result is a scalar, and vector (or cross) product where the result is a vector. Based upon these two types of products for vectors, they have found various applications in geometry, mechanics and engineering. In this section, we will discuss these two types of products.

### 10.6.1 Scalar (or dot) product of two vectors

Definition 2 The scalar product of two nonzero vectors $\vec{a}$ and $\vec{b}$, denoted by $\vec{a} \cdot \vec{b}$, is
defined as

$$
\vec{a} \cdot \vec{b}=|\vec{a}||\vec{b}| \cos \theta,
$$

where, $\theta$ is the angle between $\vec{a}$ and $\vec{b}, 0 \leq \theta \leq \pi$ (Fig 10.19).
If either $\vec{a}=0$ or $\vec{b}=0$ then $\theta$ is not defined, and in this case, we
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-19.jpg?height=176&width=306&top_left_y=268&top_left_x=1095)

Fig 10.19 define $\vec{a} \cdot \vec{b}=0$

## Observations

1. $\vec{a} \cdot \vec{b}$ is a real number.
2. Let $\vec{a}$ and $\vec{b}$ be two nonzero vectors, then $\vec{a} \cdot \vec{b}=0$ if and only if $\vec{a}$ and $\vec{b}$ are perpendicular to each other. i.e.
$\vec{a} \cdot \vec{b}=0 \Leftrightarrow \vec{a} \perp \vec{b}$
3. If $\theta=0$, then $\vec{a} \cdot \vec{b}=|\vec{a}||\vec{b}|$

In particular, $\vec{a} \cdot \vec{a}=|\vec{a}|^{2}$, as $\theta$ in this case is 0 .
4. If $\theta=\pi$, then $\vec{a} \cdot \vec{b}=-|\vec{a}||\vec{b}|$

In particular, $\vec{a} \cdot \vec{b}=-|\vec{a}||\vec{b}|$, as $\theta$ in this case is $\pi$.
5. In view of the Observations 2 and 3 , for mutually perpendicular unit vectors $\hat{i}, \hat{j}$ and $\hat{k}$, we have

$$
\begin{aligned}
& \hat{i} \cdot \hat{i}=\hat{j} \cdot \hat{j}=\hat{k} \cdot \hat{k}=1 \\
& \hat{i} \cdot \hat{j}=\hat{j} \cdot \hat{k}=\hat{k} \cdot \hat{i}=0
\end{aligned}
$$

6. The angle between two nonzero vectors $\vec{a}$ and $\vec{b}$ is given by

$$
\cos \theta=\frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}, \text { or } \theta=\cos ^{-1}\left(\frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}\right)
$$

7. The scalar product is commutative. i.e.

$$
\vec{a} \cdot \vec{b}=\vec{b} \cdot \vec{a} \quad \text { (Why?) }
$$

## Two important properties of scalar product

Property 1 (Distributivity of scalar product over addition) Let $\vec{a}, \vec{b}$ and $\vec{c}$ be any three vectors, then

$$
\vec{a} \cdot(\vec{b}+\vec{c})=\vec{a} \cdot \vec{b}+\vec{a} \cdot \vec{c}
$$

Property 2 Let $\vec{a}$ and $\vec{b}$ be any two vectors, and 1 be any scalar. Then

$$
(\lambda \vec{a}) \cdot \vec{b}=(\lambda \vec{a}) \cdot \vec{b}=\lambda(\vec{a} \cdot \vec{b})=\vec{a} \cdot(\lambda \vec{b})
$$

If two vectors $\vec{a}$ and $\vec{b}$ are given in component form as $a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$ and $b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}$, then their scalar product is given as

$$
\begin{aligned}
\vec{a} \cdot \vec{b}= & \left(a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}\right) \cdot\left(b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}\right) \\
= & a_{1} \hat{i} \cdot\left(b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}\right)+a_{2} \hat{j} \cdot\left(b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}\right)+a_{3} \hat{k} \cdot\left(b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}\right) \\
= & a_{1} b_{1}(\hat{i} \cdot \hat{i})+a_{1} b_{2}(\hat{i} \cdot \hat{j})+a_{1} b_{3}(\hat{i} \cdot \hat{k})+a_{2} b_{1}(\hat{j} \cdot \hat{i})+a_{2} b_{2}(\hat{j} \cdot \hat{j})+a_{2} b_{3}(\hat{j} \cdot \hat{k}) \\
& +a_{3} b_{1}(\hat{k} \cdot \hat{i})+a_{3} b_{2}(\hat{k} \cdot \hat{j})+a_{3} b_{3}(\hat{k} \cdot \hat{k})(\text { Using the above Properties } 1 \text { and } 2) \\
= & a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3} \quad \text { (Using Observation 5) }
\end{aligned}
$$

Thus

$$
\vec{a} \cdot \vec{b}=a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3}
$$

### 10.6.2 Projection of a vector on a line

Suppose a vector $\overrightarrow{\mathrm{AB}}$ makes an angle $\theta$ with a given directed line $l$ (say), in the anticlockwise direction (Fig 10.20). Then the projection of $\overrightarrow{\mathrm{AB}}$ on $l$ is a vector $\vec{p}$ (say) with magnitude $|\overrightarrow{\mathrm{AB}}||\cos \theta|$, and the direction of $\vec{p}$ being the same (or opposite) to that of the line $l$, depending upon whether $\cos \theta$ is positive or negative. The vector $\vec{p}$
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-20.jpg?height=719&width=1210&top_left_y=1284&top_left_x=142)

Fig 10.20
is called the projection vector, and its magnitude $|\vec{p}|$ is simply called as the projection of the vector $\overrightarrow{\mathrm{AB}}$ on the directed line $l$.

For example, in each of the following figures (Fig 10.20 (i) to (iv)), projection vector of $\overrightarrow{\mathrm{AB}}$ along the line $l$ is vector $\overrightarrow{\mathrm{AC}}$.

## Observations

1. If $\hat{p}$ is the unit vector along a line $l$, then the projection of a vector $\vec{a}$ on the line $l$ is given by $\vec{a} \cdot \hat{p}$.
2. Projection of a vector $\vec{a}$ on other vector $\vec{b}$, is given by

$$
\vec{a} \cdot \hat{b}, \quad \text { or } \quad \vec{a} \cdot\left(\frac{\vec{b}}{|\vec{b}|}\right), \quad \text { or } \quad \frac{1}{|\vec{b}|}(\vec{a} \cdot \vec{b})
$$

3. If $\theta=0$, then the projection vector of $\overrightarrow{\mathrm{AB}}$ will be $\overrightarrow{\mathrm{AB}}$ itself and if $\theta=\pi$, then the projection vector of $\overrightarrow{\mathrm{AB}}$ will be $\overrightarrow{\mathrm{BA}}$.
4. If $\theta=\frac{\pi}{2}$ or $\theta=\frac{3 \pi}{2}$, then the projection vector of $\overrightarrow{\mathrm{AB}}$ will be zero vector.

Remark If $\alpha, \beta$ and $\gamma$ are the direction angles of vector $\vec{a}=a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$, then its direction cosines may be given as

$$
\cos \alpha=\frac{\vec{a} \cdot \hat{i}}{|\vec{a}||\hat{i}|}=\frac{a_{1}}{|\vec{a}|}, \quad \cos \beta=\frac{a_{2}}{|\vec{a}|}, \quad \text { and } \cos \gamma=\frac{a_{3}}{|\vec{a}|}
$$

Also, note that $|\vec{a}| \cos \alpha,|\vec{a}| \cos \beta$ and $|\vec{a}| \cos \gamma$ are respectively the projections of $\vec{a}$ along OX , OY and OZ . i.e., the scalar components $a_{1}, a_{2}$ and $a_{3}$ of the vector $\vec{a}$, are precisely the projections of $\vec{a}$ along $x$-axis, $y$-axis and $z$-axis, respectively. Further, if $\vec{a}$ is a unit vector, then it may be expressed in terms of its direction cosines as

$$
\vec{a}=\cos \alpha \hat{i}+\cos \beta \hat{j}+\cos \gamma \hat{k}
$$

Example 13 Find the angle between two vectors $\vec{a}$ and $\vec{b}$ with magnitudes 1 and 2 respectively and when $\vec{a} \cdot \vec{b}=1$.
Solution Given $\vec{a} \cdot \vec{b}=1,|\vec{a}|=1$ and $|\vec{b}|=2$. We have

$$
\theta=\cos ^{-1}\left(\frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}\right)=\cos ^{-1}\left(\frac{1}{2}\right)=\frac{\pi}{3}
$$

Example 14 Find angle ' $\theta$ ' between the vectors $\vec{a}=\hat{i}+\hat{j}-\hat{k}$ and $\vec{b}=\hat{i}-\hat{j}+\hat{k}$.
Solution The angle $\theta$ between two vectors $\vec{a}$ and $\vec{b}$ is given by

Now

$$
\begin{aligned}
\cos \theta & =\frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|} \\
\vec{a} \cdot \vec{b} & =(\hat{i}+\hat{j}-\hat{k}) \cdot(\hat{i}-\hat{j}+\hat{k})=1-1-1=-1
\end{aligned}
$$

Therefore, we have

$$
\cos \theta=\frac{-1}{3}
$$

hence the required angle is

$$
\theta=\cos ^{-1}\left(-\frac{1}{3}\right)
$$

Example 15 If $\vec{a}=5 \hat{i}-\hat{j}-3 \hat{k}$ and $\vec{b}=\hat{i}+3 \hat{j}-5 \hat{k}$, then show that the vectors $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ are perpendicular.

Solution We know that two nonzero vectors are perpendicular if their scalar product is zero.

Here

$$
\vec{a}+\vec{b}=(5 \hat{i}-\hat{j}-3 \hat{k})+(\hat{i}+3 \hat{j}-5 \hat{k})=6 \hat{i}+2 \hat{j}-8 \hat{k}
$$

and

$$
\vec{a}-\vec{b}=(5 \hat{i}-\hat{j}-3 \hat{k})-(\hat{i}+3 \hat{j}-5 \hat{k})=4 \hat{i}-4 \hat{j}+2 \hat{k}
$$

So

$$
(\vec{a}+\vec{b}) \cdot(\vec{a}-\vec{b})=(6 \hat{i}+2 \hat{j}-8 \hat{k}) \cdot(4 \hat{i}-4 \hat{j}+2 \hat{k})=24-8-16=0
$$

Hence $\quad \vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ are perpendicular vectors.
Example 16 Find the projection of the vector $\vec{a}=2 \hat{i}+3 \hat{j}+2 \hat{k}$ on the vector $\vec{b}=\hat{i}+2 \hat{j}+\hat{k}$.
Solution The projection of vector $\vec{a}$ on the vector $\vec{b}$ is given by

$$
\frac{1}{|\vec{b}|}(\vec{a} \cdot \vec{b})=\frac{(2 \times 1+3 \times 2+2 \times 1)}{\sqrt{(1)^{2}+(2)^{2}+(1)^{2}}}=\frac{10}{\sqrt{6}}=\frac{5}{3} \sqrt{6}
$$

Example 17 Find $|\vec{a}-\vec{b}|$, if two vectors $\vec{a}$ and $\vec{b}$ are such that $|\vec{a}|=2,|\vec{b}|=3$ and $\vec{a} \cdot \vec{b}=4$.

Solution We have

$$
\begin{aligned}
|\vec{a}-\vec{b}|^{2} & =(\vec{a}-\vec{b}) \cdot(\vec{a}-\vec{b}) \\
& =\vec{a} \cdot \vec{a}-\vec{a} \cdot \vec{b}-\vec{b} \cdot \vec{a}+\vec{b} \cdot \vec{b}
\end{aligned}
$$

$$
\begin{aligned}
& =|\vec{a}|^{2}-2(\vec{a} \cdot \vec{b})+|\vec{b}|^{2} \\
& =(2)^{2}-2(4)+(3)^{2}
\end{aligned}
$$

Therefore

$$
|\vec{a}-\vec{b}|=\sqrt{5}
$$

Example 18 If $\vec{a}$ is a unit vector and $(\vec{x}-\vec{a}) \cdot(\vec{x}+\vec{a})=8$, then find $|\vec{x}|$.
Solution Since $\vec{a}$ is a unit vector, $|\vec{a}|=1$. Also,

$$
(\vec{x}-\vec{a}) \cdot(\vec{x}+\vec{a})=8
$$

or

$$
\vec{x} \cdot \vec{x}+\vec{x} \cdot \vec{a}-\vec{a} \cdot \vec{x}-\vec{a} \cdot \vec{a}=8
$$

or

$$
|\vec{x}|^{2}-1=8 \text { i.e. }|\vec{x}|^{2}=9
$$

Therefore

$$
|\vec{x}|=3 \text { (as magnitude of a vector is non negative). }
$$

Example 19 For any two vectors $\vec{a}$ and $\vec{b}$, we always have $|\vec{a} \cdot \vec{b}| \leq|\vec{a}||\vec{b}|$ (CauchySchwartz inequality).
Solution The inequality holds trivially when either $\vec{a}=\overrightarrow{0}$ or $\vec{b}=\overrightarrow{0}$. Actually, in such a situation we have $|\vec{a} \cdot \vec{b}|=0=|\vec{a}||\vec{b}|$. So, let us assume that $|\vec{a}| \neq 0 \neq|\vec{b}|$. Then, we have

Therefore

$$
\begin{aligned}
& \frac{|\vec{a} \cdot \vec{b}|}{|\vec{a} \| \vec{b}|}=|\cos \theta| \leq 1 \\
& |\vec{a} \cdot \vec{b}| \leq|\vec{a}||\vec{b}|
\end{aligned}
$$

Example 20 For any two vectors $\vec{a}$ and $\vec{b}$, we always have $|\vec{a}+\vec{b}| \leq|\vec{a}|+|\vec{b}|$ (triangle inequality).

Solution The inequality holds trivially in case either $\vec{a}=\overrightarrow{0}$ or $\vec{b}=\overrightarrow{0}$ (How?). So, let $|\vec{a}| \neq \overrightarrow{0} \neq|\vec{b}|$. Then,
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-23.jpg?height=212&width=466&top_left_y=1379&top_left_x=936)

Fig 10.21

$$
\begin{aligned}
|\vec{a}+\vec{b}|^{2} & =(\vec{a}+\vec{b})^{2}=(\vec{a}+\vec{b}) \cdot(\vec{a}+\vec{b}) \\
& =\vec{a} \cdot \vec{a}+\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{a}+\vec{b} \cdot \vec{b} \\
& =|\vec{a}|^{2}+2 \vec{a} \cdot \vec{b}+|\vec{b}|^{2} \\
& \leq|\vec{a}|^{2}+2|\vec{a} \cdot \vec{b}|+|\vec{b}|^{2} \\
& \leq|\vec{a}|^{2}+2|\vec{a}||\vec{b}|+|\vec{b}|^{2} \\
& =(|\vec{a}|+|\vec{b}|)^{2}
\end{aligned}
$$

(scalar product is commutative) (since $x \leq|x| \forall x \in \mathbf{R}$ )
(from Example 19)

Hence

$$
|\vec{a}+\vec{b}| \leq|\vec{a}|+|\vec{b}|
$$

Remark If the equality holds in triangle inequality (in the above Example 20), i.e.
then

$$
\begin{aligned}
|\vec{a}+\vec{b}| & =|\vec{a}|+|\vec{b}|, \\
|\overrightarrow{\mathrm{AC}}| & =|\overrightarrow{\mathrm{AB}}|+|\overrightarrow{\mathrm{BC}}|
\end{aligned}
$$

showing that the points $\mathrm{A}, \mathrm{B}$ and C are collinear.
Example 21 Show that the points $\mathrm{A}(-2 \hat{i}+3 \hat{j}+5 \hat{k}), \mathrm{B}(\hat{i}+2 \hat{j}+3 \hat{k})$ and $\mathrm{C}(7 \hat{i}-\hat{k})$ are collinear.

Solution We have

Therefore

$$
\begin{aligned}
\overrightarrow{\mathrm{AB}} & =(1+2) \hat{i}+(2-3) \hat{j}+(3-5) \hat{k}=3 \hat{i}-\hat{j}-2 \hat{k} \\
\overrightarrow{\mathrm{BC}} & =(7-1) \hat{i}+(0-2) \hat{j}+(-1-3) \hat{k}=6 \hat{i}-2 \hat{j}-4 \hat{k} \\
\overrightarrow{\mathrm{AC}} & =(7+2) \hat{i}+(0-3) \hat{j}+(-1-5) \hat{k}=9 \hat{i}-3 \hat{j}-6 \hat{k} \\
|\overrightarrow{\mathrm{AB}}| & =\sqrt{14},|\overrightarrow{\mathrm{BC}}|=2 \sqrt{14} \text { and }|\overrightarrow{\mathrm{AC}}|=3 \sqrt{14}
\end{aligned}
$$

Hence the points $A, B$ and $C$ are collinear.
$\square$ Note In Example 21, one may note that although $\overrightarrow{\mathrm{AB}}+\overrightarrow{\mathrm{BC}}+\overrightarrow{\mathrm{CA}}=\overrightarrow{0}$ but the points $\mathrm{A}, \mathrm{B}$ and C do not form the vertices of a triangle.

## EXERCISE 10.3

1. Find the angle between two vectors $\vec{a}$ and $\vec{b}$ with magnitudes $\sqrt{3}$ and 2 , respectively having $\vec{a} \cdot \vec{b}=\sqrt{6}$.
2. Find the angle between the vectors $\hat{i}-2 \hat{j}+3 \hat{k}$ and $3 \hat{i}-2 \hat{j}+\hat{k}$
3. Find the projection of the vector $\hat{i}-\hat{j}$ on the vector $\hat{i}+\hat{j}$.
4. Find the projection of the vector $\hat{i}+3 \hat{j}+7 \hat{k}$ on the vector $7 \hat{i}-\hat{j}+8 \hat{k}$.
5. Show that each of the given three vectors is a unit vector:

$$
\frac{1}{7}(2 \hat{i}+3 \hat{j}+6 \hat{k}), \frac{1}{7}(3 \hat{i}-6 \hat{j}+2 \hat{k}), \quad \frac{1}{7}(6 \hat{i}+2 \hat{j}-3 \hat{k})
$$

Also, show that they are mutually perpendicular to each other.
6. Find $|\vec{a}|$ and $|\vec{b}|$, if $(\vec{a}+\vec{b}) \cdot(\vec{a}-\vec{b})=8$ and $|\vec{a}|=8|\vec{b}|$.
7. Evaluate the product $(3 \vec{a}-5 \vec{b}) \cdot(2 \vec{a}+7 \vec{b})$.
8. Find the magnitude of two vectors $\vec{a}$ and $\vec{b}$, having the same magnitude and such that the angle between them is $60^{\circ}$ and their scalar product is $\frac{1}{2}$.
9. Find $|\vec{x}|$, if for a unit vector $\vec{a},(\vec{x}-\vec{a}) \cdot(\vec{x}+\vec{a})=12$.
10. If $\vec{a}=2 \hat{i}+2 \hat{j}+3 \hat{k}, \vec{b}=-\hat{i}+2 \hat{j}+\hat{k}$ and $\vec{c}=3 \hat{i}+\hat{j}$ are such that $\vec{a}+\lambda \vec{b}$ is perpendicular to $\vec{c}$, then find the value of $\lambda$.
11. Show that $|\vec{a}| \vec{b}+|\vec{b}| \vec{a}$ is perpendicular to $|\vec{a}| \vec{b}-|\vec{b}| \vec{a}$, for any two nonzero vectors $\vec{a}$ and $\vec{b}$.
12. If $\vec{a} \cdot \vec{a}=0$ and $\vec{a} \cdot \vec{b}=0$, then what can be concluded about the vector $\vec{b}$ ?
13. If $\vec{a}, \vec{b}, \vec{c}$ are unit vectors such that $\vec{a}+\vec{b}+\vec{c}=\overrightarrow{0}$, find the value of $\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}$.
14. If either vector $\vec{a}=\overrightarrow{0}$ or $\vec{b}=\overrightarrow{0}$, then $\vec{a} \cdot \vec{b}=0$. But the converse need not be true. Justify your answer with an example.
15. If the vertices $\mathrm{A}, \mathrm{B}, \mathrm{C}$ of a triangle ABC are ( $1,2,3),(-1,0,0),(0,1,2)$, respectively, then find $\angle \mathrm{ABC}$. [ $\angle \mathrm{ABC}$ is the angle between the vectors $\overrightarrow{\mathrm{BA}}$ and $\overrightarrow{\mathrm{BC}}]$.
16. Show that the points $A(1,2,7), B(2,6,3)$ and $C(3,10,-1)$ are collinear.
17. Show that the vectors $2 \hat{i}-\hat{j}+\hat{k}, \hat{i}-3 \hat{j}-5 \hat{k}$ and $3 \hat{i}-4 \hat{j}-4 \hat{k}$ form the vertices of a right angled triangle.
18. If $\vec{a}$ is a nonzero vector of magnitude ' $a$ ' and $\lambda$ a nonzero scalar, then $\lambda \vec{a}$ is unit vector if
(A) $\lambda=1$
(B) $\lambda=-1$
(C) $a=|\lambda|$
(D) $a=1 /|\lambda|$

### 10.6.3 Vector (or cross) product of two vectors

In Section 10.2, we have discussed on the three dimensional right handed rectangular coordinate system. In this system, when the positive $x$-axis is rotated counterclockwise
into the positive $y$-axis, a right handed (standard) screw would advance in the direction of the positive $z$-axis (Fig 10.22(i)).

In a right handed coordinate system, the thumb of the right hand points in the direction of the positive $z$-axis when the fingers are curled in the direction away from the positive $x$-axis toward the positive $y$-axis (Fig 10.22(ii)).
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-26.jpg?height=502&width=1079&top_left_y=509&top_left_x=212)

Fig 10.22 (i), (ii)
Definition 3 The vector product of two nonzero vectors $\vec{a}$ and $\vec{b}$, is denoted by $\vec{a} \times \vec{b}$ and defined as

$$
\vec{a} \times \vec{b}=|\vec{a}||\vec{b}| \sin \theta \hat{n},
$$

where, $\theta$ is the angle between $\vec{a}$ and $\vec{b}, 0 \leq \theta \leq \pi$ and $\hat{n}$ is a unit vector perpendicular to both $\vec{a}$ and $\vec{b}$, such that $\vec{a}, \vec{b}$ and $\hat{n}$ form a right handed system (Fig 10.23). i.e., the right handed system rotated from $\vec{a}$ to $\vec{b}$ moves in the direction
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-26.jpg?height=320&width=313&top_left_y=1198&top_left_x=1089)

Fig 10.23 of $\hat{n}$.

If either $\vec{a}=\overrightarrow{0}$ or $\vec{b}=\overrightarrow{0}$, then $\theta$ is not defined and in this case, we define $\vec{a} \times \vec{b}=\overrightarrow{0}$.

## Observations

1. $\vec{a} \times \vec{b}$ is a vector.
2. Let $\vec{a}$ and $\vec{b}$ be two nonzero vectors. Then $\vec{a} \times \vec{b}=\overrightarrow{0}$ if and only if $\vec{a}$ and $\vec{b}$ are parallel (or collinear) to each other, i.e.,

$$
\vec{a} \times \vec{b}=\overrightarrow{0} \Leftrightarrow \vec{a} \| \vec{b}
$$

In particular, $\vec{a} \times \vec{a}=\overrightarrow{0}$ and $\vec{a} \times(-\vec{a})=\overrightarrow{0}$, since in the first situation, $\theta=0$ and in the second one, $\theta=\pi$, making the value of $\sin \theta$ to be 0 .
3. If $\theta=\frac{\pi}{2}$ then $\vec{a} \times \vec{b}=|\vec{a} \| \vec{b}|$.
4. In view of the Observations 2 and 3, for mutually perpendicular unit vectors $\hat{i}, \hat{j}$ and $\hat{k}$ (Fig 10.24), we have

$$
\begin{aligned}
& \hat{i} \times \hat{i}=\hat{j} \times \hat{j}=\hat{k} \times \hat{k}=\overrightarrow{0} \\
& \hat{i} \times \hat{j}=\hat{k}, \quad \hat{j} \times \hat{k}=\hat{i}, \quad \hat{k} \times \hat{i}=\hat{j}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-27.jpg?height=269&width=236&top_left_y=443&top_left_x=1163)

Fig 10.24
5. In terms of vector product, the angle between two vectors $\vec{a}$ and $\vec{b}$ may be given as

$$
\sin \theta=\frac{|\vec{a} \times \vec{b}|}{|\vec{a}||\vec{b}|}
$$

6. It is always true that the vector product is not commutative, as $\vec{a} \times \vec{b}=-\vec{b} \times \vec{a}$. Indeed, $\vec{a} \times \vec{b}=|\vec{a}||\vec{b}| \sin \theta \hat{n}$, where $\vec{a}, \vec{b}$ and $\hat{n}$ form a right handed system, i.e., $\theta$ is traversed from $\vec{a}$ to $\vec{b}$, Fig 10.25 (i). While, $\vec{b} \times \vec{a}=|\vec{a}||\vec{b}| \sin \theta \hat{n}_{1}$, where $\vec{b}, \vec{a}$ and $\hat{n}_{1}$ form a right handed system i.e. $\theta$ is traversed from $\vec{b}$ to $\vec{a}$, Fig 10.25(ii).
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-27.jpg?height=487&width=1182&top_left_y=1336&top_left_x=213)

Fig 10.25 (i), (ii)
Thus, if we assume $\vec{a}$ and $\vec{b}$ to lie in the plane of the paper, then $\hat{n}$ and $\hat{n}_{1}$ both will be perpendicular to the plane of the paper. But, $\hat{n}$ being directed above the paper while $\hat{n}_{1}$ directed below the paper. i.e. $\hat{n}_{1}=-\hat{n}$.

Hence

$$
\begin{aligned}
\vec{a} \times \vec{b} & =|\vec{a} \| \vec{b}| \sin \theta \hat{n} \\
& =-|\vec{a}||\vec{b}| \sin \theta \hat{n}_{1}=-\vec{b} \times \vec{a}
\end{aligned}
$$

7. In view of the Observations 4 and 6 , we have

$$
\hat{j} \times \hat{i}=-\hat{k}, \quad \hat{k} \times \hat{j}=-\hat{i} \text { and } \hat{i} \times \hat{k}=-\hat{j}
$$

8. If $\vec{a}$ and $\vec{b}$ represent the adjacent sides of a triangle then its area is given as $\frac{1}{2}|\vec{a} \times \vec{b}|$.
By definition of the area of a triangle, we have from Fig 10.26,

Area of triangle $\mathrm{ABC}=\frac{1}{2} \mathrm{AB} \cdot \mathrm{CD}$.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-28.jpg?height=249&width=416&top_left_y=662&top_left_x=987)

Fig 10.26

But $\mathrm{AB}=|\vec{b}|$ (as given), and $\mathrm{CD}=|\vec{a}| \sin \theta$.
Thus, Area of triangle $\mathrm{ABC}=\frac{1}{2}|\vec{b}||\vec{a}| \sin \theta=\frac{1}{2}|\vec{a} \times \vec{b}|$.
9. If $\vec{a}$ and $\vec{b}$ represent the adjacent sides of a parallelogram, then its area is given by $|\vec{a} \times \vec{b}|$.

From Fig 10.27, we have
Area of parallelogram $\mathrm{ABCD}=\mathrm{AB} . \mathrm{DE}$.
But $\mathrm{AB}=|\vec{b}|$ (as given), and $\mathrm{DE}=|\vec{a}| \sin \theta$.

Thus,
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-28.jpg?height=340&width=607&top_left_y=1232&top_left_x=795)

Fig 10.27

Area of parallelogram $\mathrm{ABCD}=|\vec{b}||\vec{a}| \sin \theta=|\vec{a} \times \vec{b}|$.
We now state two important properties of vector product.
Property 3 (Distributivity of vector product over addition): If $\vec{a}, \vec{b}$ and $\vec{c}$ are any three vectors and $\lambda$ be a scalar, then
(i) $\vec{a} \times(\vec{b}+\vec{c})=\vec{a} \times \vec{b}+\vec{a} \times \vec{c}$
(ii) $\lambda(\vec{a} \times \vec{b})=(\lambda \vec{a}) \times \vec{b}=\vec{a} \times(\lambda \vec{b})$

Let $\vec{a}$ and $\vec{b}$ be two vectors given in component form as $a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$ and $b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}$, respectively. Then their cross product may be given by

$$
\vec{a} \times \vec{b}=\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3}
\end{array}\right|
$$

Explanation We have

$$
\begin{aligned}
& \vec{a} \times \vec{b}=\left(a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}\right) \times\left(b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}\right) \\
&= a_{1} b_{1}(\hat{i} \times \hat{i})+a_{1} b_{2}(\hat{i} \times \hat{j})+a_{1} b_{3}(\hat{i} \times \hat{k})+a_{2} b_{1}(\hat{j} \times \hat{i}) \\
&+a_{2} b_{2}(\hat{j} \times \hat{j})+a_{2} b_{3}(\hat{j} \times \hat{k}) \\
&+a_{3} b_{1}(\hat{k} \times \hat{i})+a_{3} b_{2}(\hat{k} \times \hat{j})+a_{3} b_{3}(\hat{k} \times \hat{k}) \\
&= a_{1} b_{2}(\hat{i} \times \hat{j})-a_{1} b_{3}(\hat{k} \times \hat{i})-a_{2} b_{1}(\hat{i} \times \hat{j}) \\
&+a_{2} b_{3}(\hat{j} \times \hat{k})+a_{3} b_{1}(\hat{k} \times \hat{i})-a_{3} b_{2}(\hat{j} \times \hat{k}) \\
&(\text { as } \hat{i} \times \hat{i}=\hat{j} \times \hat{j}=\hat{k} \times \hat{k}=0 \text { and } \hat{i} \times \hat{k}=-\hat{k} \times \hat{i}, \hat{j} \times \hat{i}=-\hat{i} \times \hat{j} \text { anc } \\
&= a_{1} b_{2} \hat{k}-a_{1} b_{3} \hat{j}-a_{2} b_{1} \hat{k}+a_{2} b_{3} \hat{i}+a_{3} b_{1} \hat{j}-a_{3} b_{2} \hat{i} \\
&(\text { as } \hat{i} \times \hat{j}=\hat{k}, \hat{j} \times \hat{k}=\hat{i} \text { and } \hat{k} \times \hat{i}=\hat{j}) \\
&=\left(a_{2} b_{3}-a_{3} b_{2}\right) \hat{i}-\left(a_{1} b_{3}-a_{3} b_{1}\right) \hat{j}+\left(a_{1} b_{2}-a_{2} b_{1}\right) \hat{k} \\
&=\left|\begin{array}{lll}
\hat{i} & \hat{j} & \hat{k} \\
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3}
\end{array}\right|
\end{aligned}
$$

(by Property 1)

Example 22 Find $|\vec{a} \times \vec{b}|$, if $\vec{a}=2 \hat{i}+\hat{j}+3 \hat{k}$ and $\vec{b}=3 \hat{i}+5 \hat{j}-2 \hat{k}$
Solution We have

Hence

$$
\begin{aligned}
\vec{a} \times \vec{b} & =\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
2 & 1 & 3 \\
3 & 5 & -2
\end{array}\right| \\
& =\hat{i}(-2-15)-(-4-9) \hat{j}+(10-3) \hat{k}=-17 \hat{i}+13 \hat{j}+7 \hat{k} \\
|\vec{a} \times \vec{b}| & =\sqrt{(-17)^{2}+(13)^{2}+(7)^{2}}=\sqrt{507}
\end{aligned}
$$

Example 23 Find a unit vector perpendicular to each of the vectors $(\vec{a}+\vec{b})$ and $(\vec{a}-\vec{b})$, where $\vec{a}=\hat{i}+\hat{j}+\hat{k}, \quad \vec{b}=\hat{i}+2 \hat{j}+3 \hat{k}$.

Solution we have $\vec{a}+\vec{b}=2 \hat{i}+3 \hat{j}+4 \hat{k}$ and $\vec{a}-\vec{b}=-\hat{j}-2 \hat{k}$

A vector which is perpendicular to both $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ is given by

Now

$$
\begin{aligned}
(\vec{a}+\vec{b}) \times(\vec{a}-\vec{b}) & =\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
2 & 3 & 4 \\
0 & -1 & -2
\end{array}\right|=-2 \hat{i}+4 \hat{j}-2 \hat{k} \quad(=\vec{c}, \text { say }) \\
|\vec{c}| & =\sqrt{4+16+4}=\sqrt{24}=2 \sqrt{6}
\end{aligned}
$$

Therefore, the required unit vector is

$$
\frac{\vec{c}}{|\vec{c}|}=\frac{-1}{\sqrt{6}} \hat{i}+\frac{2}{\sqrt{6}} \hat{j}-\frac{1}{\sqrt{6}} \hat{k}
$$

Note There are two perpendicular directions to any plane. Thus, another unit vector perpendicular to $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ will be $\frac{1}{\sqrt{6}} \hat{i}-\frac{2}{\sqrt{6}} \hat{j}+\frac{1}{\sqrt{6}} \hat{k}$. But that will be a consequence of $(\vec{a}-\vec{b}) \times(\vec{a}+\vec{b})$.

Example 24 Find the area of a triangle having the points $\mathrm{A}(1,1,1), \mathrm{B}(1,2,3)$ and $\mathrm{C}(2,3,1)$ as its vertices.

Solution We have $\overrightarrow{\mathrm{AB}}=\hat{j}+2 \hat{k}$ and $\overrightarrow{\mathrm{AC}}=\hat{i}+2 \hat{j}$. The area of the given triangle is $\frac{1}{2}|\overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{AC}}|$.

Now,

$$
\overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{AC}}=\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
0 & 1 & 2 \\
1 & 2 & 0
\end{array}\right|=-4 \hat{i}+2 \hat{j}-\hat{k}
$$

Therefore

$$
|\overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{AC}}|=\sqrt{16+4+1}=\sqrt{21}
$$

Thus, the required area is $\frac{1}{2} \sqrt{21}$

Example 25 Find the area of a parallelogram whose adjacent sides are given by the vectors $\vec{a}=3 \hat{i}+\hat{j}+4 \hat{k}$ and $\vec{b}=\hat{i}-\hat{j}+\hat{k}$

Solution The area of a parallelogram with $\vec{a}$ and $\vec{b}$ as its adjacent sides is given by $|\vec{a} \times \vec{b}|$.

Now

$$
\vec{a} \times \vec{b}=\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
3 & 1 & 4 \\
1 & -1 & 1
\end{array}\right|=5 \hat{i}+\hat{j}-4 \hat{k}
$$

Therefore

$$
|\vec{a} \times \vec{b}|=\sqrt{25+1+16}=\sqrt{42}
$$

and hence, the required area is $\sqrt{42}$.

## EXERCISE 10.4

1. Find $|\vec{a} \times \vec{b}|$, if $\vec{a}=\hat{i}-7 \hat{j}+7 \hat{k}$ and $\vec{b}=3 \hat{i}-2 \hat{j}+2 \hat{k}$.
2. Find a unit vector perpendicular to each of the vector $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$, where $\vec{a}=3 \hat{i}+2 \hat{j}+2 \hat{k}$ and $\vec{b}=\hat{i}+2 \hat{j}-2 \hat{k}$.
3. If a unit vector $\vec{a}$ makes angles $\frac{\pi}{3}$ with $\hat{i}, \frac{\pi}{4}$ with $\hat{j}$ and an acute angle $\theta$ with $\hat{k}$, then find $\theta$ and hence, the components of $\vec{a}$.
4. Show that

$$
(\vec{a}-\vec{b}) \times(\vec{a}+\vec{b})=2(\vec{a} \times \vec{b})
$$

5. Find $\lambda$ and $\mu$ if $(2 \hat{i}+6 \hat{j}+27 \hat{k}) \times(\hat{i}+\lambda \hat{j}+\mu \hat{k})=\overrightarrow{0}$.
6. Given that $\vec{a} \cdot \vec{b}=0$ and $\vec{a} \times \vec{b}=\overrightarrow{0}$. What can you conclude about the vectors $\vec{a}$ and $\vec{b}$ ?
7. Let the vectors $\vec{a}, \vec{b}, \vec{c}$ be given as $a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}, b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}$, $c_{1} \hat{i}+c_{2} \hat{j}+c_{3} \hat{k}$. Then show that $\vec{a} \times(\vec{b}+\vec{c})=\vec{a} \times \vec{b}+\vec{a} \times \vec{c}$.
8. If either $\vec{a}=\overrightarrow{0}$ or $\vec{b}=\overrightarrow{0}$, then $\vec{a} \times \vec{b}=\overrightarrow{0}$. Is the converse true? Justify your answer with an example.
9. Find the area of the triangle with vertices $\mathrm{A}(1,1,2), \mathrm{B}(2,3,5)$ and $\mathrm{C}(1,5,5)$.
10. Find the area of the parallelogram whose adjacent sides are determined by the vectors $\vec{a}=\hat{i}-\hat{j}+3 \hat{k}$ and $\vec{b}=2 \hat{i}-7 \hat{j}+\hat{k}$.
11. Let the vectors $\vec{a}$ and $\vec{b}$ be such that $|\vec{a}|=3$ and $|\vec{b}|=\frac{\sqrt{2}}{3}$, then $\vec{a} \times \vec{b}$ is a unit vector, if the angle between $\vec{a}$ and $\vec{b}$ is
(A) $\pi / 6$
(B) $\pi / 4$
(C) $\pi / 3$
(D) $\pi / 2$
12. Area of a rectangle having vertices $A, B, C$ and $D$ with position vectors $-\hat{i}+\frac{1}{2} \hat{j}+4 \hat{k}, \hat{i}+\frac{1}{2} \hat{j}+4 \hat{k}, \hat{i}-\frac{1}{2} \hat{j}+4 \hat{k}$ and $-\hat{i}-\frac{1}{2} \hat{j}+4 \hat{k}$, respectively is
(A) $\frac{1}{2}$
(B) 1
(C) 2
(D) 4

## Miscellaneous Examples

Example 26 Write all the unit vectors in XY-plane.
Solution Let $\vec{r}=x \hat{i}+y \hat{j}$ be a unit vector in XY-plane (Fig 10.28). Then, from the figure, we have $x=\cos \theta$ and $y=\sin \theta$ (since $|\vec{r}|=1$ ). So, we may write the vector $\vec{r}$ as

$$
\begin{equation*}
\vec{r}(=\overrightarrow{\mathrm{OP}})=\cos \theta \hat{i}+\sin \theta \hat{j} \tag{1}
\end{equation*}
$$

Clearly,

$$
|\vec{r}|=\sqrt{\cos ^{2} \theta+\sin ^{2} \theta}=1
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_3a79e3fea893b7e865ebg-32.jpg?height=517&width=704&top_left_y=1319&top_left_x=494)

Fig 10.28
Also, as $\theta$ varies from 0 to $2 \pi$, the point P (Fig 10.28) traces the circle $x^{2}+y^{2}=1$ counterclockwise, and this covers all possible directions. So, (1) gives every unit vector in the XY-plane.

Example 27 If $\hat{i}+\hat{j}+\hat{k}, 2 \hat{i}+5 \hat{j}, 3 \hat{i}+2 \hat{j}-3 \hat{k}$ and $\hat{i}-6 \hat{j}-\hat{k}$ are the position vectors of points $A, B, C$ and $D$ respectively, then find the angle between $\overrightarrow{A B}$ and $\overrightarrow{C D}$. Deduce that $\overrightarrow{\mathrm{AB}}$ and $\overrightarrow{\mathrm{CD}}$ are collinear.

Solution Note that if $\theta$ is the angle between AB and CD , then $\theta$ is also the angle between $\overrightarrow{\mathrm{AB}}$ and $\overrightarrow{\mathrm{CD}}$.

Now

$$
\begin{aligned}
\overrightarrow{\mathrm{AB}} & =\text { Position vector of } \mathrm{B}-\text { Position vector of } \mathrm{A} \\
& =(2 \hat{i}+5 \hat{j})-(\hat{i}+\hat{j}+\hat{k})=\hat{i}+4 \hat{j}-\hat{k}
\end{aligned}
$$

Therefore

$$
|\overrightarrow{\mathrm{AB}}|=\sqrt{(1)^{2}+(4)^{2}+(-1)^{2}}=3 \sqrt{2}
$$

Similarly

$$
\overrightarrow{\mathrm{CD}}=-2 \hat{i}-8 \hat{j}+2 \hat{k} \text { and }|\overrightarrow{\mathrm{CD}}|=6 \sqrt{2}
$$

Thus

$$
\begin{aligned}
\cos \theta & =\frac{\overrightarrow{\mathrm{AB}} \cdot \overrightarrow{\mathrm{CD}}}{|\overrightarrow{\mathrm{AB}}||\overrightarrow{\mathrm{CD}}|} \\
& =\frac{1(-2)+4(-8)+(-1)(2)}{(3 \sqrt{2})(6 \sqrt{2})}=\frac{-36}{36}=-1
\end{aligned}
$$

Since $0 \leq \theta \leq \pi$, it follows that $\theta=\pi$. This shows that $\overrightarrow{\mathrm{AB}}$ and $\overrightarrow{\mathrm{CD}}$ are collinear.
Alternatively, $\overrightarrow{A B}=-\frac{1}{2} \overrightarrow{C D}$ which implies that $\overrightarrow{A B}$ and $\overrightarrow{C D}$ are collinear vectors.
Example 28 Let $\vec{a}, \vec{b}$ and $\vec{c}$ be three vectors such that $|\vec{a}|=3,|\vec{b}|=4,|\vec{c}|=5$ and each one of them being perpendicular to the sum of the other two, find $|\vec{a}+\vec{b}+\vec{c}|$.

Solution Given $\vec{a} \cdot(\vec{b}+\vec{c})=0, \vec{b} \cdot(\vec{c}+\vec{a})=0, \vec{c} \cdot(\vec{a}+\vec{b})=0$.
Now

$$
\begin{aligned}
|\vec{a}+\vec{b}+\vec{c}|^{2}= & (\vec{a}+\vec{b}+\vec{c})^{2}=(\vec{a}+\vec{b}+\vec{c}) \cdot(\vec{a}+\vec{b}+\vec{c}) \\
= & \vec{a} \cdot \vec{a}+\vec{a} \cdot(\vec{b}+\vec{c})+\vec{b} \cdot \vec{b}+\vec{b} \cdot(\vec{a}+\vec{c}) \\
& +\vec{c} \cdot(\vec{a}+\vec{b})+\vec{c} \cdot \vec{c} \\
= & |\vec{a}|^{2}+|\vec{b}|^{2}+|\vec{c}|^{2} \\
= & 9+16+25=50
\end{aligned}
$$

Therefore

$$
|\vec{a}+\vec{b}+\vec{c}|=\sqrt{50}=5 \sqrt{2}
$$

Example 29 Three vectors $\vec{a}, \vec{b}$ and $\vec{c}$ satisfy the condition $\vec{a}+\vec{b}+\vec{c}=\overrightarrow{0}$. Evaluate the quantity $\mu=\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{c} \cdot \vec{a}$, if $|\vec{a}|=3,|\vec{b}|=4$ and $|\vec{c}|=2$.

Solution Since $\vec{a}+\vec{b}+\vec{c}=\overrightarrow{0}$, we have
or

$$
\begin{align*}
\vec{a}+\vec{b}+\vec{c}=\overrightarrow{0} & =0 \\
\vec{a} \cdot \vec{a}+\vec{a} \cdot \vec{b}+\vec{a} \cdot \vec{c} & =0 \\
\vec{a} \cdot \vec{b}+\vec{a} \cdot \vec{c} & =-|\vec{a}|^{2}=-9 \tag{1}
\end{align*}
$$

Therefore

Again,

$$
\vec{b} \cdot(\vec{a}+\vec{b}+\vec{c})=0
$$

or

$$
\begin{equation*}
\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}=-|\vec{b}|^{2}=-16 \tag{2}
\end{equation*}
$$

Similarly

$$
\begin{equation*}
\vec{a} \cdot \vec{c}+\vec{b} \cdot \vec{c}=-4 \tag{3}
\end{equation*}
$$

Adding (1), (2) and (3), we have
or

$$
\begin{array}{r}
2(\vec{a} \cdot \vec{b}+\vec{b} \cdot \vec{c}+\vec{a} \cdot \vec{c})=-29 \\
2 \mu=-29, \text { i.e., } \mu=\frac{-29}{2}
\end{array}
$$

Example 30 If with reference to the right handed system of mutually perpendicular unit vectors $\hat{i}, \hat{j}$ and $\hat{k}, \vec{\alpha}=3 \hat{i}-\hat{j}, \vec{\beta}=2 \hat{i}+\hat{j}-3 \hat{k}$, then express $\vec{\beta}$ in the form $\vec{\beta}=\vec{\beta}_{1}+\vec{\beta}_{2}$, where $\vec{\beta}_{1}$ is parallel to $\vec{\alpha}$ and $\vec{\beta}_{2}$ is perpendicular to $\vec{\alpha}$.

Solution Let $\vec{\beta}_{1}=\lambda \vec{\alpha}, \lambda$ is a scalar, i.e., $\vec{\beta}_{1}=3 \lambda \hat{i}-\lambda \hat{j}$.
Now

$$
\vec{\beta}_{2}=\vec{\beta}-\vec{\beta}_{1}=(2-3 \lambda) \hat{i}+(1+\lambda) \hat{j}-3 \hat{k}
$$

Now, since $\vec{\beta}_{2}$ is to be perpendicular to $\vec{\alpha}$, we should have $\vec{\alpha} \cdot \vec{\beta}_{2}=0$. i.e.,
or

$$
3(2-3 \lambda)-(1+\lambda)=0
$$

Therefore

$$
\begin{aligned}
\lambda & =\frac{1}{2} \\
\vec{\beta}_{1} & =\frac{3}{2} \hat{i}-\frac{1}{2} \hat{j} \text { and } \vec{\beta}_{2}=\frac{1}{2} \hat{i}+\frac{3}{2} \hat{j}-3 \hat{k}
\end{aligned}
$$

## Miscellaneous Exercise on Chapter 10

1. Write down a unit vector in XY-plane, making an angle of $30^{\circ}$ with the positive direction of $x$-axis.
2. Find the scalar components and magnitude of the vector joining the points $\mathrm{P}\left(x_{1}, y_{1}, z_{1}\right)$ and $\mathrm{Q}\left(x_{2}, y_{2}, z_{2}\right)$.
3. A girl walks 4 km towards west, then she walks 3 km in a direction $30^{\circ}$ east of north and stops. Determine the girl's displacement from her initial point of departure.
4. If $\vec{a}=\vec{b}+\vec{c}$, then is it true that $|\vec{a}|=|\vec{b}|+|\vec{c}|$ ? Justify your answer.
5. Find the value of $x$ for which $x(\hat{i}+\hat{j}+\hat{k})$ is a unit vector.
6. Find a vector of magnitude 5 units, and parallel to the resultant of the vectors $\vec{a}=2 \hat{i}+3 \hat{j}-\hat{k}$ and $\vec{b}=\hat{i}-2 \hat{j}+\hat{k}$.
7. If $\vec{a}=\hat{i}+\hat{j}+\hat{k}, \vec{b}=2 \hat{i}-\hat{j}+3 \hat{k}$ and $\vec{c}=\hat{i}-2 \hat{j}+\hat{k}$, find a unit vector parallel to the vector $2 \vec{a}-\vec{b}+3 \vec{c}$.
8. Show that the points $\mathrm{A}(1,-2,-8), \mathrm{B}(5,0,-2)$ and $\mathrm{C}(11,3,7)$ are collinear, and find the ratio in which B divides AC .
9. Find the position vector of a point R which divides the line joining two points P and Q whose position vectors are $(2 \vec{a}+\vec{b})$ and $(\vec{a}-3 \vec{b})$ externally in the ratio $1: 2$. Also, show that P is the mid point of the line segment RQ .
10. The two adjacent sides of a parallelogram are $2 \hat{i}-4 \hat{j}+5 \hat{k}$ and $\hat{i}-2 \hat{j}-3 \hat{k}$. Find the unit vector parallel to its diagonal. Also, find its area.
11. Show that the direction cosines of a vector equally inclined to the axes $\mathrm{OX}, \mathrm{OY}$ and $O Z$ are $\pm\left(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right)$.
12. Let $\vec{a}=\hat{i}+4 \hat{j}+2 \hat{k}, \vec{b}=3 \hat{i}-2 \hat{j}+7 \hat{k}$ and $\vec{c}=2 \hat{i}-\hat{j}+4 \hat{k}$. Find a vector $\vec{d}$ which is perpendicular to both $\vec{a}$ and $\vec{b}$, and $\vec{c} \cdot \vec{d}=15$.
13. The scalar product of the vector $\hat{i}+\hat{j}+\hat{k}$ with a unit vector along the sum of vectors $2 \hat{i}+4 \hat{j}-5 \hat{k}$ and $\lambda \hat{i}+2 \hat{j}+3 \hat{k}$ is equal to one. Find the value of $\lambda$.
14. If $\vec{a}, \vec{b}, \overrightarrow{\mathrm{c}}$ are mutually perpendicular vectors of equal magnitudes, show that the vector $\vec{c} \cdot \vec{d}=15$ is equally inclined to $\vec{a}, \vec{b}$ and $\vec{c}$.
15. Prove that $(\vec{a}+\vec{b}) \cdot(\vec{a}+\vec{b})=|\vec{a}|^{2}+|\vec{b}|^{2}$, if and only if $\vec{a}, \vec{b}$ are perpendicular, given $\vec{a} \neq \overrightarrow{0}, \vec{b} \neq \overrightarrow{0}$.
Choose the correct answer in Exercises 16 to 19.
16. If $\theta$ is the angle between two vectors $\vec{a}$ and $\vec{b}$, then $\vec{a} \cdot \vec{b} \geq 0$ only when
(A) $0<\theta<\frac{\pi}{2}$
(B) $0 \leq \theta \leq \frac{\pi}{2}$
(C) $0<\theta<\pi$
(D) $0 \leq \theta \leq \pi$
17. Let $\vec{a}$ and $\vec{b}$ be two unit vectors and $\theta$ is the angle between them. Then $\vec{a}+\vec{b}$ is a unit vector if
(A) $\theta=\frac{\pi}{4}$
(B) $\theta=\frac{\pi}{3}$
(C) $\theta=\frac{\pi}{2}$
(D) $\theta=\frac{2 \pi}{3}$
18. The value of $\hat{i} \cdot(\hat{j} \times \hat{k})+\hat{j} \cdot(\hat{i} \times \hat{k})+\hat{k} \cdot(\hat{i} \times \hat{j})$ is
(A) 0
(B) -1
(C) 1
(D) 3
19. If $\theta$ is the angle between any two vectors $\vec{a}$ and $\vec{b}$, then $|\vec{a} \cdot \vec{b}|=|\vec{a} \times \vec{b}|$ when $\theta$ is equal to
(A) 0
(B) $\frac{\pi}{4}$
(C) $\frac{\pi}{2}$
(D) $\pi$

## Summary

- Position vector of a point $\mathrm{P}(x, y, z)$ is given as $\overrightarrow{\mathrm{OP}}(=\vec{r})=x \hat{i}+y \hat{j}+z \hat{k}$, and its magnitude by $\sqrt{x^{2}+y^{2}+z^{2}}$.
- The scalar components of a vector are its direction ratios, and represent its projections along the respective axes.
- The magnitude ( $r$ ), direction ratios ( $a, b, c$ ) and direction cosines ( $l, m, n$ ) of any vector are related as:

$$
l=\frac{a}{r}, \quad m=\frac{b}{r}, \quad n=\frac{c}{r}
$$

- The vector sum of the three sides of a triangle taken in order is $\overrightarrow{0}$.
- The vector sum of two coinitial vectors is given by the diagonal of the parallelogram whose adjacent sides are the given vectors.
- The multiplication of a given vector by a scalar $\lambda$, changes the magnitude of the vector by the multiple $|\lambda|$, and keeps the direction same (or makes it opposite) according as the value of $\lambda$ is positive (or negative).
- For a given vector $\vec{a}$, the vector $\hat{a}=\frac{\vec{a}}{|\vec{a}|}$ gives the unit vector in the direction of $\vec{a}$.
- The position vector of a point R dividing a line segment joining the points P and Q whose position vectors are $\vec{a}$ and $\vec{b}$ respectively, in the ratio $m: n$
(i) internally, is given by $\frac{n \vec{a}+m \vec{b}}{m+n}$.
(ii) externally, is given by $\frac{m \vec{b}-n \vec{a}}{m-n}$.
- The scalar product of two given vectors $\vec{a}$ and $\vec{b}$ having angle $\theta$ between them is defined as

$$
\vec{a} \cdot \vec{b}=|\vec{a}||\vec{b}| \cos \theta
$$

Also, when $\vec{a} \cdot \vec{b}$ is given, the angle ' $\theta$ ' between the vectors $\vec{a}$ and $\vec{b}$ may be determined by

$$
\cos \theta=\frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}
$$

- If $\theta$ is the angle between two vectors $\vec{a}$ and $\vec{b}$, then their cross product is given as

$$
\vec{a} \times \vec{b}=|\vec{a}||\vec{b}| \sin \theta \hat{n}
$$

where $\hat{n}$ is a unit vector perpendicular to the plane containing $\vec{a}$ and $\vec{b}$. Such that $\vec{a}, \vec{b}, \hat{n}$ form right handed system of coordinate axes.

- If we have two vectors $\vec{a}$ and $\vec{b}$, given in component form as $\vec{a}=a_{1} \hat{i}+a_{2} \hat{j}+a_{3} \hat{k}$ and $\vec{b}=b_{1} \hat{i}+b_{2} \hat{j}+b_{3} \hat{k}$ and $\lambda$ any scalar,
then

$$
\begin{aligned}
\vec{a}+\vec{b} & =\left(a_{1}+b_{1}\right) \hat{i}+\left(a_{2}+b_{2}\right) \hat{j}+\left(a_{3}+b_{3}\right) \hat{k} \\
\lambda \vec{a} & =\left(\lambda a_{1}\right) \hat{i}+\left(\lambda a_{2}\right) \hat{j}+\left(\lambda a_{3}\right) \hat{k} \\
\vec{a} \cdot \vec{b} & =a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3} \\
\vec{a} \times \vec{b} & =\left|\begin{array}{lll}
\hat{i} & \hat{j} & \hat{k} \\
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right| .
\end{aligned}
$$

## Historical Note

The word vector has been derived from a Latin word vectus, which means "to carry". The germinal ideas of modern vector theory date from around 1800 when Caspar Wessel (1745-1818) and Jean Robert Argand (1768-1822) described that how a complex number $a+i b$ could be given a geometric interpretation with the help of a directed line segment in a coordinate plane. William Rowen Hamilton (1805-1865) an Irish mathematician was the first to use the term vector for a directed line segment in his book Lectures on Quaternions (1853). Hamilton's method of quaternions (an ordered set of four real numbers given as: $a+b \hat{i}+c \hat{j}+d \hat{k}, \hat{i}, \hat{j}, \hat{k}$ following certain algebraic rules) was a solution to the problem of multiplying vectors in three dimensional space. Though, we must mention here that in practice, the idea of vector concept and their addition was known much earlier ever since the time of Aristotle (384-322 B.C.), a Greek philosopher, and pupil of Plato (427-348 B.C.). That time it was supposed to be known that the combined action of two or more forces could be seen by adding them according to parallelogram law. The correct law for the composition of forces, that forces add vectorially, had been discovered in the case of perpendicular forces by Stevin-Simon (1548-1620). In 1586 A.D., he analysed the principle of geometric addition of forces in his treatise DeBeghinselen der Weeghconst ("Principles of the Art of Weighing"), which caused a major breakthrough in the development of mechanics. But it took another 200 years for the general concept of vectors to form.

In the 1880, Josaih Willard Gibbs (1839-1903), an American physicist and mathematician, and Oliver Heaviside (1850-1925), an English engineer, created what we now know as vector analysis, essentially by separating the real (scalar)
part of quaternion from its imaginary (vector) part. In 1881 and 1884, Gibbs printed a treatise entitled Element of Vector Analysis. This book gave a systematic and concise account of vectors. However, much of the credit for demonstrating the applications of vectors is due to the D. Heaviside and P.G. Tait (1831-1901) who contributed significantly to this subject.

