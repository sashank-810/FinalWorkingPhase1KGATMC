## COMPLEX NUMBERS AND QUADRATIC EQUATIONS

Mathematics is the Queen of Sciences and Arithmetic is the Queen of Mathematics. - GAUSS

### 4.1 Introduction

In earlier classes, we have studied linear equations in one and two variables and quadratic equations in one variable. We have seen that the equation $x^{2}+1=0$ has no real solution as $x^{2}+1=0$ gives $x^{2}=-1$ and square of every real number is non-negative. So, we need to extend the real number system to a larger system so that we can find the solution of the equation $x^{2}=-1$. In fact, the main objective is to solve the equation $a x^{2}+b x+c=0$, where $\mathrm{D}=b^{2}-4 a c<0$, which is not possible in the system of real numbers.

### 4.2 Complex Numbers

![](https://cdn.mathpix.com/cropped/2025_07_21_85fe3faf24544835bc4cg-01.jpg?height=653&width=414&top_left_y=949&top_left_x=1048)

Let us denote $\sqrt{-1}$ by the symbol $i$. Then, we have $i^{2}=-1$. This means that $i$ is a solution of the equation $x^{2}+1=0$.

A number of the form $a+i b$, where $a$ and $b$ are real numbers, is defined to be a complex number. For example, $2+i 3,(-1)+i \sqrt{3}, 4+i\left(\frac{-1}{11}\right)$ are complex numbers.

For the complex number $z=a+i b, a$ is called the real part, denoted by $\operatorname{Re} z$ and $b$ is called the imaginary part denoted by $\operatorname{Im} z$ of the complex number $z$. For example, if $z=2+i 5$, then $\operatorname{Re} z=2$ and $\operatorname{Im} z=5$.

Two complex numbers $z_{1}=a+i b$ and $z_{2}=c+i d$ are equal if $a=c$ and $b=d$.

Example 1 If $4 x+i(3 x-y)=3+i(-6)$, where $x$ and $y$ are real numbers, then find the values of $x$ and $y$.

Solution We have

$$
\begin{equation*}
4 x+i(3 x-y)=3+i(-6) \tag{1}
\end{equation*}
$$

Equating the real and the imaginary parts of (1), we get

$$
4 x=3,3 x-y=-6
$$

which, on solving simultaneously, give $x=\frac{3}{4}$ and $y=\frac{33}{4}$.

### 4.3 Algebra of Complex Numbers

In this Section, we shall develop the algebra of complex numbers.
4.3.1 Addition of two complex numbers Let $z_{1}=a+i b$ and $z_{2}=c+i d$ be any two complex numbers. Then, the sum $z_{1}+z_{2}$ is defined as follows:
$z_{1}+z_{2}=(a+c)+i(b+d)$, which is again a complex number.
For example, $(2+i 3)+(-6+i 5)=(2-6)+i(3+5)=-4+i 8$
The addition of complex numbers satisfy the following properties:
(i) The closure law The sum of two complex numbers is a complex number, i.e., $z_{1}+z_{2}$ is a complex number for all complex numbers $z_{1}$ and $z_{2}$.
(ii) The commutative law For any two complex numbers $z_{1}$ and $z_{2}$, $z_{1}+z_{2}=z_{2}+z_{1}$
(iii) The associative law For any three complex numbers $z_{1}, z_{2}, z_{3}$, $\left(z_{1}+z_{2}\right)+z_{3}=z_{1}+\left(z_{2}+z_{3}\right)$.
(iv) The existence of additive identity There exists the complex number $0+i 0$ (denoted as 0 ), called the additive identity or the zero complex number, such that, for every complex number $z, z+0=z$.
(v) The existence of additive inverse To every complex number $z=a+i b$, we have the complex number $-a+i(-b)$ (denoted as $-z$ ), called the additive inverse or negative of $z$. We observe that $z+(-z)=0$ (the additive identity).
4.3.2 Difference of two complex numbers Given any two complex numbers $z_{1}$ and $z_{2}$, the difference $z_{1}-z_{2}$ is defined as follows:

$$
z_{1}-z_{2}=z_{1}+\left(-z_{2}\right)
$$

For example, $\quad(6+3 i)-(2-i)=(6+3 i)+(-2+i)=4+4 i$ and

$$
(2-i)-(6+3 i)=(2-i)+(-6-3 i)=-4-4 i
$$

4.3.3 Multiplication of two complex numbers Let $z_{1}=a+i b$ and $z_{2}=c+i d$ be any two complex numbers. Then, the product $z_{1} z_{2}$ is defined as follows:

$$
z_{1} z_{2}=(a c-b d)+i(a d+b c)
$$

For example, $(3+i 5)(2+i 6)=(3 \times 2-5 \times 6)+i(3 \times 6+5 \times 2)=-24+i 28$
The multiplication of complex numbers possesses the following properties, which we state without proofs.
(i) The closure law The product of two complex numbers is a complex number, the product $z_{1} z_{2}$ is a complex number for all complex numbers $z_{1}$ and $z_{2}$.
(ii) The commutative law For any two complex numbers $z_{1}$ and $z_{2}$,

$$
z_{1} z_{2}=z_{2} z_{1}
$$

(iii) The associative law For any three complex numbers $z_{1}, z_{2}, z_{3}$, $\left(z_{1} z_{2}\right) z_{3}=z_{1}\left(z_{2} z_{3}\right)$.
(iv) The existence of multiplicative identity There exists the complex number $1+i 0$ (denoted as 1), called the multiplicative identity such that $z .1=z$, for every complex number $z$.
(v) The existence of multiplicative inverse For every non-zero complex number $z=a+i b$ or $a+b i(a \neq 0, \mathrm{~b} \neq 0)$, we have the complex number $\frac{a}{a^{2}+b^{2}}+i \frac{-b}{a^{2}+b^{2}}\left(\right.$ denoted by $\frac{1}{z}$ or $\left.z^{-1}\right)$, called the multiplicative inverse of $z$ such that $z \cdot \frac{1}{z}=1$ (the multiplicative identity).
(vi) The distributive law For any three complex numbers $z_{1}, z_{2}, z_{3}$,
(a) $z_{1}\left(z_{2}+z_{3}\right)=z_{1} z_{2}+z_{1} z_{3}$
(b) $\left(z_{1}+z_{2}\right) z_{3}=z_{1} z_{3}+z_{2} z_{3}$
4.3.4 Division of two complex numbers Given any two complex numbers $z_{1}$ and $z_{2}$, where $z_{2} \neq 0$, the quotient $\frac{z_{1}}{z_{2}}$ is defined by

$$
\frac{z_{1}}{z_{2}}=z_{1} \frac{1}{z_{2}}
$$

For example, let $z_{1}=6+3 i$ and $z_{2}=2-i$

Then

$$
\frac{z_{1}}{z_{2}}=\left((6+3 i) \times \frac{1}{2-i}\right)=(6+3 i)\left(\frac{2}{2^{2}+(-1)^{2}}+i \frac{-(-1)}{2^{2}+(-1)^{2}}\right)
$$

$$
=(6+3 i)\left(\frac{2+i}{5}\right)=\frac{1}{5}[12-3+i(6+6)]=\frac{1}{5}(9+12 i)
$$

4.3.5 Power of $i$ we know that

$$
\begin{array}{ll}
i^{3}=i^{2} i=(-1) i=-i, & i^{4}=\left(i^{2}\right)^{2}=(-1)^{2}=1 \\
i^{5}=\left(i^{2}\right)^{2} i=(-1)^{2} i=i, & i^{6}=\left(i^{2}\right)^{3}=(-1)^{3}=-1, \text { etc. }
\end{array}
$$

Also, we have $\quad i^{-1}=\frac{1}{i} \times \frac{i}{i}=\frac{i}{-1}=-i, \quad i^{-2}=\frac{1}{i^{2}}=\frac{1}{-1}=-1$,

$$
i^{-3}=\frac{1}{i^{3}}=\frac{1}{-i} \times \frac{i}{i}=\frac{i}{1}=i, \quad i^{-4}=\frac{1}{i^{4}}=\frac{1}{1}=1
$$

In general, for any integer $k, i^{4 k}=1, i^{4 k+1}=i, i^{4 k+2}=-1, i^{4 k+3}=-i$

### 4.3.6 The square roots of a negative real number

Note that $i^{2}=-1$ and $(-i)^{2}=i^{2}=-1$
Therefore, the square roots of -1 are $i,-i$. However, by the symbol $\sqrt{-1}$, we would mean $i$ only.

Now, we can see that $i$ and $-i$ both are the solutions of the equation $x^{2}+1=0$ or $x^{2}=-1$.

Similarly

$$
\begin{aligned}
& (\sqrt{3} i)^{2}=(\sqrt{3})^{2} i^{2}=3(-1)=-3 \\
& (-\sqrt{3} i)^{2}=(-\sqrt{3})^{2} i^{2}=-3
\end{aligned}
$$

Therefore, the square roots of -3 are $\sqrt{3} i$ and $-\sqrt{3} i$.
Again, the symbol $\sqrt{-3}$ is meant to represent $\sqrt{3} i$ only, i.e., $\sqrt{-3}=\sqrt{3} i$.
Generally, if $a$ is a positive real number, $\sqrt{-a}=\sqrt{a} \sqrt{-1}=\sqrt{a} i$,
We already know that $\sqrt{a} \times \sqrt{b}=\sqrt{a b}$ for all positive real number $a$ and $b$. This result also holds true when either $a>0, b<0$ or $a<0, b>0$. What if $a<0, b<0$ ? Let us examine.

Note that
$i^{2}=\sqrt{-1} \sqrt{-1}=\sqrt{(-1)(-1)}$ (by assuming $\sqrt{a} \times \sqrt{b}=\sqrt{a b}$ for all real numbers) $=\sqrt{1}=1$, which is a contradiction to the fact that $i^{2}=-1$. Therefore, $\sqrt{a} \times \sqrt{b} \neq \sqrt{a b}$ if both $a$ and $b$ are negative real numbers.

Further, if any of $a$ and $b$ is zero, then, clearly, $\sqrt{a} \times \sqrt{b}=\sqrt{a b}=0$.
4.3.7 Identities We prove the following identity $\left(z_{1}+z_{2}\right)^{2}=z_{1}^{2}+z_{2}^{2}+2 z_{1} z_{2}$, for all complex numbers $z_{1}$ and $z_{2}$.

Proof We have, $\left(z_{1}+z_{2}\right)^{2}=\left(z_{1}+z_{2}\right)\left(z_{1}+z_{2}\right)$,

$$
\begin{array}{ll}
=\left(z_{1}+z_{2}\right) z_{1}+\left(z_{1}+z_{2}\right) z_{2} & (\text { Distributive law }) \\
=z_{1}^{2}+z_{2} z_{1}+z_{1} z_{2}+z_{2}^{2} & (\text { Distributive law }) \\
=z_{1}^{2}+z_{1} z_{2}+z_{1} z_{2}+z_{2}^{2} & (\text { Commutative law of multiplication }) \\
=z_{1}^{2}+2 z_{1} z_{2}+z_{2}^{2} &
\end{array}
$$

Similarly, we can prove the following identities:
(i) $\left(z_{1}-z_{2}\right)^{2}=z_{1}^{2}-2 z_{1} z_{2}+z_{2}^{2}$
(ii) $\left(z_{1}+z_{2}\right)^{3}=z_{1}^{3}+3 z_{1}^{2} z_{2}+3 z_{1} z_{2}^{2}+z_{2}^{3}$
(iii) $\left(z_{1}-z_{2}\right)^{3}=z_{1}^{3}-3 z_{1}^{2} z_{2}+3 z_{1} z_{2}^{2}-z_{2}^{3}$
(iv) $z_{1}^{2}-z_{2}^{2}=\left(z_{1}+z_{2}\right)\left(z_{1}-z_{2}\right)$

In fact, many other identities which are true for all real numbers, can be proved to be true for all complex numbers.

Example 2 Express the following in the form of $a+b i$ :
(i) $(-5 i)\left(\frac{1}{8} i\right)$
(ii) $(-i)(2 i)\left(-\frac{1}{8} i\right)^{3}$

Solution
(i) $(-5 i)\left(\frac{1}{8} i\right)=\frac{-5}{8} i^{2}=\frac{-5}{8}(-1)=\frac{5}{8}=\frac{5}{8}+i 0$
(ii) $\quad(-i)(2 i)\left(-\frac{1}{8} i\right)^{3}=2 \times \frac{1}{8 \times 8 \times 8} \times i^{5}=\frac{1}{256}\left(i^{2}\right)^{2} i=\frac{1}{256} i$.

Example 3 Express $(5-3 i)^{3}$ in the form $a+i b$.
Solution We have, $(5-3 i)^{3}=5^{3}-3 \times 5^{2} \times(3 i)+3 \times 5(3 i)^{2}-(3 i)^{3}$

$$
=125-225 i-135+27 i=-10-198 i
$$

Example 4 Express $(-\sqrt{3}+\sqrt{-2})(2 \sqrt{3}-i)$ in the form of $a+i b$
Solution We have, $(-\sqrt{3}+\sqrt{-2})(2 \sqrt{3}-i)=(-\sqrt{3}+\sqrt{2} i)(2 \sqrt{3}-i)$

$$
=-6+\sqrt{3} i+2 \sqrt{6} i-\sqrt{2} i^{2}=(-6+\sqrt{2})+\sqrt{3}(1+2 \sqrt{2}) i
$$

### 4.4 The Modulus and the Conjugate of a Complex Number

Let $z=a+i b$ be a complex number. Then, the modulus of $z$, denoted by $|z|$, is defined to be the non-negative real number $\sqrt{a^{2}+b^{2}}$, i.e., $|z|=\sqrt{a^{2}+b^{2}}$ and the conjugate of $z$, denoted as $\bar{z}$, is the complex number $a-i b$, i.e., $\bar{z}=a-i b$.

For example,

$$
|3+i|=\sqrt{3^{2}+1^{2}}=\sqrt{10},|2-5 i|=\sqrt{2^{2}+(-5)^{2}}=\sqrt{29}
$$

and

$$
\overline{3+i}=3-i, \overline{2-5 i}=2+5 i, \overline{-3 i-5}=3 i-5
$$

Observe that the multiplicative inverse of the non-zero complex number $z$ is given by

$$
z^{-1}=\frac{1}{a+i b}=\frac{a}{a^{2}+b^{2}}+i \frac{-b}{a^{2}+b^{2}}=\frac{a-i b}{a^{2}+b^{2}}=\frac{\bar{z}}{|z|^{2}}
$$

or

$$
z \bar{z}=|z|^{2}
$$

Furthermore, the following results can easily be derived.
For any two compex numbers $z_{1}$ and $z_{2}$, we have
(i) $\left|z_{1} z_{2}\right|=\left|z_{1}\right|\left|z_{2}\right|$
(ii) $\left|\frac{z_{1}}{z_{2}}\right|=\frac{\left|z_{1}\right|}{\left|z_{2}\right|}$ provided $\left|z_{2}\right| \neq 0$
(iii) $\overline{z_{1} z_{2}}=\overline{z_{1}} \overline{z_{2}}$
(iv) $\overline{z_{1} \pm z_{2}}=\overline{z_{1}} \pm \overline{z_{2}}$ (v) $\overline{\left(\frac{z_{1}}{z_{2}}\right)}=\frac{\overline{z_{1}}}{\overline{z_{2}}}$ provided $z_{2} \neq 0$.

Example 5 Find the multiplicative inverse of $2-3 i$.
Solution Let $z=2-3 i$
Then $\quad \bar{z}=2+3 i$ and $\quad|z|^{2}=2^{2}+(-3)^{2}=13$
Therefore, the multiplicative inverse of $2-3 i$ is given by

$$
z^{-1}=\frac{\bar{z}}{|z|^{2}}=\frac{2+3 i}{13}=\frac{2}{13}+\frac{3}{13} i
$$

The above working can be reproduced in the following manner also,

$$
\begin{aligned}
z^{-1} & =\frac{1}{2-3 i}=\frac{2+3 i}{(2-3 i)(2+3 i)} \\
& =\frac{2+3 i}{2^{2}-(3 i)^{2}}=\frac{2+3 i}{13}=\frac{2}{13}+\frac{3}{13} i
\end{aligned}
$$

Example 6 Express the following in the form $a+i b$
(i) $\frac{5+\sqrt{2} i}{1-\sqrt{2} i}$
(ii) $i^{-35}$

Solution (i) We have, $\frac{5+\sqrt{2} i}{1-\sqrt{2} i}=\frac{5+\sqrt{2} i}{1-\sqrt{2} i} \times \frac{1+\sqrt{2} i}{1+\sqrt{2} i}=\frac{5+5 \sqrt{2} i+\sqrt{2} i-2}{1-(\sqrt{2} i)^{2}}$

$$
=\frac{3+6 \sqrt{2} i}{1+2}=\frac{3(1+2 \sqrt{2} i)}{3}=1+2 \sqrt{2} i
$$

(ii) $i^{-35}=\frac{1}{i^{35}}=\frac{1}{\left(i^{2}\right)^{17} i}=\frac{1}{-i} \times \frac{i}{i}=\frac{i}{-i^{2}}=i$

## EXERCISE 4.1

Express each of the complex number given in the Exercises 1 to 10 in the form $a+i b$.

1. $(5 i)\left(-\frac{3}{5} i\right)$
2. $i^{9}+i^{19}$
3. $i^{-39}$
4. $3(7+i 7)+i(7+i 7)$
5. $(1-i)-(-1+i 6)$
6. $\left(\frac{1}{5}+i \frac{2}{5}\right)-\left(4+i \frac{5}{2}\right)$
7. $\left[\left(\frac{1}{3}+i \frac{7}{3}\right)+\left(4+i \frac{1}{3}\right)\right]-\left(-\frac{4}{3}+i\right)$
8. $(1-i)^{4}$
9. $\left(\frac{1}{3}+3 i\right)^{3}$
10. $\left(-2-\frac{1}{3} i\right)^{3}$

Find the multiplicative inverse of each of the complex numbers given in the Exercises 11 to 13.
11. $4-3 i$
12. $\sqrt{5}+3 i$
13. $-i$
14. Express the following expression in the form of $a+i b$ :

$$
\frac{(3+i \sqrt{5})(3-i \sqrt{5})}{(\sqrt{3}+\sqrt{2} i)-(\sqrt{3}-i \sqrt{2})}
$$

### 4.5 Argand Plane and Polar Representation

We already know that corresponding to each ordered pair of real numbers $(x, y)$, we get a unique point in the XYplane and vice-versa with reference to a set of mutually perpendicular lines known as the $x$-axis and the $y$-axis. The complex number $x+i y$ which corresponds to the ordered pair $(x, y)$ can be represented geometrically as the unique point $\mathrm{P}(x, y)$ in the XY-plane and vice-versa.

Some complex numbers such as $2+4 i,-2+3 i, 0+1 i, 2+0 i,-5-2 i$ and $1-2 i$ which correspond to the ordered
![](https://cdn.mathpix.com/cropped/2025_07_21_85fe3faf24544835bc4cg-08.jpg?height=614&width=687&top_left_y=1168&top_left_x=786)

Fig 4.1 pairs $(2,4),(-2,3),(0,1),(2,0),(-5,-2)$, and $(1,-2)$, respectively, have been represented geometrically by the points $\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}$, and F , respectively in the Fig 4.1.

The plane having a complex number assigned to each of its point is called the complex plane or the Argand plane.

Obviously, in the Argand plane, the modulus of the complex number $x+i y=\sqrt{x^{2}+y^{2}}$ is the distance between the point $\mathrm{P}(x, y)$ and the origin $\mathrm{O}(0,0)$ (Fig 4.2). The points on the $x$-axis corresponds to the complex numbers of the form $a+i 0$ and the points on the $y$-axis corresponds to the complex numbers of the form
![](https://cdn.mathpix.com/cropped/2025_07_21_85fe3faf24544835bc4cg-09.jpg?height=594&width=713&top_left_y=575&top_left_x=469)
$0+i b$. The $x$-axis and $y$-axis in the Argand plane are called, respectively, the real axis and the imaginary axis.

The representation of a complex number $z=x+i y$ and its conjugate $z=x-i y$ in the Argand plane are, respectively, the points $\mathrm{P}(x, y)$ and $\mathrm{Q}(x,-y)$.

Geometrically, the point $(x,-y)$ is the mirror image of the point $(x, y)$ on the real axis (Fig 4.3).
![](https://cdn.mathpix.com/cropped/2025_07_21_85fe3faf24544835bc4cg-09.jpg?height=536&width=653&top_left_y=1518&top_left_x=485)

Fig 4.3

## Miscellaneous Examples

Example 7 Find the conjugate of $\frac{(3-2 i)(2+3 i)}{(1+2 i)(2-i)}$.
Solution We have, $\frac{(3-2 i)(2+3 i)}{(1+2 i)(2-i)}$

$$
\begin{aligned}
& =\frac{6+9 i-4 i+6}{2-i+4 i+2}=\frac{12+5 i}{4+3 i} \times \frac{4-3 i}{4-3 i} \\
& =\frac{48-36 i+20 i+15}{16+9}=\frac{63-16 i}{25}=\frac{63}{25}-\frac{16}{25} i
\end{aligned}
$$

Therefore, conjugate of $\frac{(3-2 i)(2+3 i)}{(1+2 i)(2-i)}$ is $\frac{63}{25}+\frac{16}{25} i$.
Example 8 If $x+i y=\frac{a+i b}{a-i b}$, prove that $x^{2}+y^{2}=1$.
Solution We have,

$$
x+i y=\frac{(a+i b)(a+i b)}{(a-i b)(a+i b)}=\frac{a^{2}-b^{2}+2 a b i}{a^{2}+b^{2}}=\frac{a^{2}-b^{2}}{a^{2}+b^{2}}+\frac{2 a b}{a^{2}+b^{2}} i
$$

So that, $x-i y=\frac{a^{2}-b^{2}}{a^{2}+b^{2}}-\frac{2 a b}{a^{2}+b^{2}} i$
Therefore,
$x^{2}+y^{2}=(x+i y)(x-i y)=\frac{\left(a^{2}-b^{2}\right)^{2}}{\left(a^{2}+b^{2}\right)^{2}}+\frac{4 a^{2} b^{2}}{\left(a^{2}+b^{2}\right)^{2}}=\frac{\left(a^{2}+b^{2}\right)^{2}}{\left(a^{2}+b^{2}\right)^{2}}=1$

## Miscellaneous Exercise on Chapter 4

1. Evaluate: $\left[i^{18}+\left(\frac{1}{i}\right)^{25}\right]^{3}$.
2. For any two complex numbers $z_{1}$ and $z_{2}$, prove that
$\operatorname{Re}\left(z_{1} z_{2}\right)=\operatorname{Re} z_{1} \operatorname{Re} z_{2}-\operatorname{Im} z_{1} \operatorname{Im} z_{2}$.
3. Reduce $\left(\frac{1}{1-4 i}-\frac{2}{1+i}\right)\left(\frac{3-4 i}{5+i}\right)$ to the standard form.
4. If $x-i y=\sqrt{\frac{a-i b}{c-i d}}$ prove that $\left(x^{2}+y^{2}\right)^{2}=\frac{a^{2}+b^{2}}{c^{2}+d^{2}}$.
5. If $z_{1}=2-i, z_{2}=1+i$, find $\left|\frac{z_{1}+z_{2}+1}{z_{1}-z_{2}+1}\right|$.
6. If $a+i b=\frac{(x+i)^{2}}{2 x^{2}+1}$, prove that $a^{2}+b^{2}=\frac{\left(x^{2}+1\right)^{2}}{\left(2 x^{2}+1\right)^{2}}$.
7. Let $z_{1}=2-i, z_{2}=-2+i$. Find
(i) $\operatorname{Re}\left(\frac{z_{1} z_{2}}{\bar{z}_{1}}\right)$,
(ii) $\operatorname{Im}\left(\frac{1}{z_{1} \bar{z}_{1}}\right)$.
8. Find the real numbers $x$ and $y$ if $(x-i y)(3+5 i)$ is the conjugate of $-6-24 i$.
9. Find the modulus of $\frac{1+i}{1-i}-\frac{1-i}{1+i}$.
10. If $(x+i y)^{3}=u+i v$, then show that $\frac{u}{x}+\frac{v}{y}=4\left(x^{2}-y^{2}\right)$.
11. If $\alpha$ and $\beta$ are different complex numbers with $|\beta|=1$, then find $\left|\frac{\beta-\alpha}{1-\bar{\alpha} \beta}\right|$.
12. Find the number of non-zero integral solutions of the equation $|1-i|^{x}=2^{x}$.
13. If $(a+i b)(c+i d)(e+i f)(g+i h)=\mathrm{A}+i \mathrm{~B}$, then show that $\left(a^{2}+b^{2}\right)\left(c^{2}+d^{2}\right)\left(e^{2}+f^{2}\right)\left(g^{2}+h^{2}\right)=\mathrm{A}^{2}+\mathrm{B}^{2}$
14. If $\left(\frac{1+i}{1-i}\right)^{m}=1$, then find the least positive integral value of $m$.

## Summary

- A number of the form $a+i b$, where $a$ and $b$ are real numbers, is called a complex number, $a$ is called the real part and $b$ is called the imaginary part of the complex number.
-Let $z_{1}=a+i b$ and $z_{2}=c+i d$. Then
(i) $z_{1}+z_{2}=(a+c)+i(b+d)$
(ii) $z_{1} z_{2}=(a c-b d)+i(a d+b c)$
- For any non-zero complex number $z=a+i b(a \neq 0, b \neq 0)$, there exists the complex number $\frac{a}{a^{2}+b^{2}}+i \frac{-b}{a^{2}+b^{2}}$, denoted by $\frac{1}{z}$ or $z^{-1}$, called the multiplicative inverse of $z$ such that $(a+i b) \frac{a}{a^{2}+b^{2}}+i \frac{-b}{a^{2}+b^{2}}=1+i 0$ $=1$
- For any integer $k, i^{4 k}=1, i^{4 k+1}=i, i^{4 k+2}=-1, i^{4 k+3}=-i$
- The conjugate of the complex number $z=a+i b$, denoted by $\bar{z}$, is given by $\bar{z}=a-i b$.


## Historical Note

The fact that square root of a negative number does not exist in the real number system was recognised by the Greeks. But the credit goes to the Indian mathematician Mahavira (850) who first stated this difficulty clearly. "He mentions in his work 'Ganitasara Sangraha' as in the nature of things a negative (quantity) is not a square (quantity)', it has, therefore, no square root". Bhaskara, another Indian mathematician, also writes in his work Bijaganita, written in 1150. "There is no square root of a negative quantity, for it is not a square." Cardan (1545) considered the problem of solving

$$
x+y=10, x y=40
$$

He obtained $x=5+\sqrt{-15}$ and $y=5-\sqrt{-15}$ as the solution of it, which was discarded by him by saying that these numbers are 'useless'. Albert Girard (about 1625) accepted square root of negative numbers and said that this will enable us to get as many roots as the degree of the polynomial equation. Euler was the first to introduce the symbol $i$ for $\sqrt{-1}$ and W.R. Hamilton (about 1830) regarded the complex number $a+i b$ as an ordered pair of real numbers ( $a, b$ ) thus giving it a purely mathematical definition and avoiding use of the so called 'imaginary numbers'.

