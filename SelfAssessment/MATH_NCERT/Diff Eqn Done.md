## DIFFERENTIAL EQUATIONS

## He who seeks for methods without having a definite problem in mind seeks for the most part in vain. - D. HILBERT

### 9.1 Introduction

In Class XI and in Chapter 5 of the present book, we discussed how to differentiate a given function $f$ with respect to an independent variable, i.e., how to find $f^{\prime}(x)$ for a given function $f$ at each $x$ in its domain of definition. Further, in the chapter on Integral Calculus, we discussed how to find a function $f$ whose derivative is the function $g$, which may also be formulated as follows:

For a given function $g$, find a function $f$ such that

$$
\begin{equation*}
\frac{d y}{d x}=g(x), \text { where } y=f(x) \tag{1}
\end{equation*}
$$

An equation of the form (1) is known as a differential equation. A formal definition will be given later.
![](https://cdn.mathpix.com/cropped/2025_07_21_467e170cd9a96b5fda7dg-01.jpg?height=535&width=412&top_left_y=809&top_left_x=998)

Henri Poincare
(1854-1912)

These equations arise in a variety of applications, may it be in Physics, Chemistry, Biology, Anthropology, Geology, Economics etc. Hence, an indepth study of differential equations has assumed prime importance in all modern scientific investigations.

In this chapter, we will study some basic concepts related to differential equation, general and particular solutions of a differential equation, formation of differential equations, some methods to solve a first order - first degree differential equation and some applications of differential equations in different areas.

### 9.2 Basic Concepts

We are already familiar with the equations of the type:

$$
\begin{array}{r}
x^{2}-3 x+3=0 \\
\sin x+\cos x=0 \\
x+y=7 \tag{3}
\end{array}
$$

Let us consider the equation:

$$
\begin{equation*}
x \frac{d y}{d x}+y=0 \tag{4}
\end{equation*}
$$

We see that equations (1), (2) and (3) involve independent and/or dependent variable (variables) only but equation (4) involves variables as well as derivative of the dependent variable $y$ with respect to the independent variable $x$. Such an equation is called a differential equation.

In general, an equation involving derivative (derivatives) of the dependent variable with respect to independent variable (variables) is called a differential equation.

A differential equation involving derivatives of the dependent variable with respect to only one independent variable is called an ordinary differential equation, e.g.,

$$
\begin{equation*}
2 \frac{d^{2} y}{d x^{2}}+\left(\frac{d y}{d x}\right)^{3}=0 \text { is an ordinary differential equation } \tag{5}
\end{equation*}
$$

Of course, there are differential equations involving derivatives with respect to more than one independent variables, called partial differential equations but at this stage we shall confine ourselves to the study of ordinary differential equations only. Now onward, we will use the term 'differential equation' for 'ordinary differential equation'.

## Note

1. We shall prefer to use the following notations for derivatives:

$$
\frac{d y}{d x}=y^{\prime}, \frac{d^{2} y}{d x^{2}}=y^{\prime \prime}, \frac{d^{3} y}{d x^{3}}=y^{\prime \prime \prime}
$$

2. For derivatives of higher order, it will be inconvenient to use so many dashes as supersuffix therefore, we use the notation $y_{n}$ for $n$th order derivative $\frac{d^{n} y}{d x^{n}}$.

### 9.2.1. Order of a differential equation

Order of a differential equation is defined as the order of the highest order derivative of the dependent variable with respect to the independent variable involved in the given differential equation.

Consider the following differential equations:

$$
\begin{equation*}
\frac{d y}{d x}=e^{x} \tag{6}
\end{equation*}
$$

$$
\begin{array}{r}
\frac{d^{2} y}{d x^{2}}+y=0 \\
\left(\frac{d^{3} y}{d x^{3}}\right)+x^{2}\left(\frac{d^{2} y}{d x^{2}}\right)^{3}=0 \tag{8}
\end{array}
$$

The equations (6), (7) and (8) involve the highest derivative of first, second and third order respectively. Therefore, the order of these equations are 1,2 and 3 respectively.

### 9.2.2 Degree of a differential equation

To study the degree of a differential equation, the key point is that the differential equation must be a polynomial equation in derivatives, i.e., $y^{\prime}, y^{\prime \prime}, y^{\prime \prime \prime}$ etc. Consider the following differential equations:

$$
\begin{align*}
\frac{d^{3} y}{d x^{3}}+2\left(\frac{d^{2} y}{d x^{2}}\right)^{2}-\frac{d y}{d x}+y & =0  \tag{9}\\
\left(\frac{d y}{d x}\right)^{2}+\left(\frac{d y}{d x}\right)-\sin ^{2} y & =0  \tag{10}\\
\frac{d y}{d x}+\sin \left(\frac{d y}{d x}\right) & =0 \tag{11}
\end{align*}
$$

We observe that equation (9) is a polynomial equation in $y^{\prime \prime \prime}, y^{\prime \prime}$ and $y^{\prime}$, equation (10) is a polynomial equation in $y^{\prime}$ (not a polynomial in $y$ though). Degree of such differential equations can be defined. But equation (11) is not a polynomial equation in $y^{\prime}$ and degree of such a differential equation can not be defined.

By the degree of a differential equation, when it is a polynomial equation in derivatives, we mean the highest power (positive integral index) of the highest order derivative involved in the given differential equation.

In view of the above definition, one may observe that differential equations (6), (7), (8) and (9) each are of degree one, equation (10) is of degree two while the degree of differential equation (11) is not defined.
$\square$ Order and degree (if defined) of a differential equation are always positive integers.

Example 1 Find the order and degree, if defined, of each of the following differential equations:
(i) $\frac{d y}{d x}-\cos x=0$
(ii) $x y \frac{d^{2} y}{d x^{2}}+x\left(\frac{d y}{d x}\right)^{2}-y \frac{d y}{d x}=0$
(iii) $y^{\prime \prime \prime}+y^{2}+e^{y^{\prime}}=0$

## Solution

(i) The highest order derivative present in the differential equation is $\frac{d y}{d x}$, so its order is one. It is a polynomial equation in $y^{\prime}$ and the highest power raised to $\frac{d y}{d x}$ is one, so its degree is one.
(ii) The highest order derivative present in the given differential equation is $\frac{d^{2} y}{d x^{2}}$, so its order is two. It is a polynomial equation in $\frac{d^{2} y}{d x^{2}}$ and $\frac{d y}{d x}$ and the highest power raised to $\frac{d^{2} y}{d x^{2}}$ is one, so its degree is one.
(iii) The highest order derivative present in the differential equation is $y^{\prime \prime \prime}$, so its order is three. The given differential equation is not a polynomial equation in its derivatives and so its degree is not defined.

## EXERCISE 9.1

Determine order and degree (if defined) of differential equations given in Exercises 1 to 10 .

1. $\frac{d^{4} y}{d x^{4}}+\sin \left(y^{\prime \prime \prime}\right)=0$
2. $y^{\prime}+5 y=0$
3. $\left(\frac{d s}{d t}\right)^{4}+3 s \frac{d^{2} s}{d t^{2}}=0$
4. $\left(\frac{d^{2} y}{d x^{2}}\right)^{2}+\cos \left(\frac{d y}{d x}\right)=0$
5. $\frac{d^{2} y}{d x^{2}}=\cos 3 x+\sin 3 x$
6. $\left(y^{\prime \prime \prime}\right)^{2}+\left(y^{\prime \prime}\right)^{3}+\left(y^{\prime}\right)^{4}+y^{5}=0$
7. $y^{\prime \prime \prime}+2 y^{\prime \prime}+y^{\prime}=0$
8. $y^{\prime}+y=e^{x}$
9. $y^{\prime \prime}+\left(y^{\prime}\right)^{2}+2 y=0$
10. $y^{\prime \prime}+2 y^{\prime}+\sin y=0$
11. The degree of the differential equation
$\left(\frac{d^{2} y}{d x^{2}}\right)^{3}+\left(\frac{d y}{d x}\right)^{2}+\sin \left(\frac{d y}{d x}\right)+1=0$ is
(A) 3
(B) 2
(C) 1
(D) not defined
12. The order of the differential equation $2 x^{2} \frac{d^{2} y}{d x^{2}}-3 \frac{d y}{d x}+y=0$ is
(A) 2
(B) 1
(C) 0
(D) not defined

### 9.3. General and Particular Solutions of a Differential Equation

In earlier Classes, we have solved the equations of the type:

$$
\begin{array}{r}
x^{2}+1=0 \\
\sin ^{2} x-\cos x=0 \tag{2}
\end{array}
$$

Solution of equations (1) and (2) are numbers, real or complex, that will satisfy the given equation i.e., when that number is substituted for the unknown $x$ in the given equation, L.H.S. becomes equal to the R.H.S..

Now consider the differential equation $\frac{d^{2} y}{d x^{2}}+y=0$
In contrast to the first two equations, the solution of this differential equation is a function $\phi$ that will satisfy it i.e., when the function $\phi$ is substituted for the unknown $y$ (dependent variable) in the given differential equation, L.H.S. becomes equal to R.H.S..

The curve $y=\phi(x)$ is called the solution curve (integral curve) of the given differential equation. Consider the function given by

$$
\begin{equation*}
y=\phi(x)=a \sin (x+b) \tag{4}
\end{equation*}
$$

where $a, b \in \mathbf{R}$. When this function and its derivative are substituted in equation (3), L.H.S. = R.H.S.. So it is a solution of the differential equation (3).

Let $a$ and $b$ be given some particular values say $a=2$ and $b=\frac{\pi}{4}$, then we get a function

$$
\begin{equation*}
y=\phi_{1}(x)=2 \sin \left(x+\frac{\pi}{4}\right) \tag{5}
\end{equation*}
$$

When this function and its derivative are substituted in equation (3) again L.H.S. $=$ R.H.S.. Therefore $\phi_{1}$ is also a solution of equation (3).

Function $\phi$ consists of two arbitrary constants (parameters) $a, b$ and it is called general solution of the given differential equation. Whereas function $\phi_{1}$ contains no arbitrary constants but only the particular values of the parameters $a$ and $b$ and hence is called a particular solution of the given differential equation.

The solution which contains arbitrary constants is called the general solution (primitive) of the differential equation.

The solution free from arbitrary constants i.e., the solution obtained from the general solution by giving particular values to the arbitrary constants is called a particular solution of the differential equation.

Example 2 Verify that the function $y=e^{-3 x}$ is a solution of the differential equation $\frac{d^{2} y}{d x^{2}}+\frac{d y}{d x}-6 y=0$

Solution Given function is $y=e^{-3 x}$. Differentiating both sides of equation with respect to $x$, we get

$$
\begin{equation*}
\frac{d y}{d x}=-3 e^{-3 x} \tag{1}
\end{equation*}
$$

Now, differentiating (1) with respect to $x$, we have

$$
\frac{d^{2} y}{d x^{2}}=9 e^{-3 x}
$$

Substituting the values of $\frac{d^{2} y}{d x^{2}}, \frac{d y}{d x}$ and $y$ in the given differential equation, we get L.H.S. $=9 e^{-3 x}+\left(-3 e^{-3 x}\right)-6 . e^{-3 x}=9 e^{-3 x}-9 e^{-3 x}=0=$ R.H.S..

Therefore, the given function is a solution of the given differential equation.
Example 3 Verify that the function $y=a \cos x+b \sin x$, where, $a, b \in \mathbf{R}$ is a solution of the differential equation $\frac{d^{2} y}{d x^{2}}+y=0$

Solution The given function is

$$
\begin{equation*}
y=a \cos x+b \sin x \tag{1}
\end{equation*}
$$

Differentiating both sides of equation (1) with respect to $x$, successively, we get

$$
\begin{aligned}
\frac{d y}{d x} & =-a \sin x+b \cos x \\
\frac{d^{2} y}{d x^{2}} & =-a \cos x-b \sin x
\end{aligned}
$$

Substituting the values of $\frac{d^{2} y}{d x^{2}}$ and $y$ in the given differential equation, we get L.H.S. $=(-a \cos x-b \sin x)+(a \cos x+b \sin x)=0=$ R.H.S.

Therefore, the given function is a solution of the given differential equation.

## EXERCISE 9.2

In each of the Exercises 1 to 10 verify that the given functions (explicit or implicit) is a solution of the corresponding differential equation:

1. $y=e^{x}+1 \quad$ : $y^{\prime \prime}-y^{\prime}=0$
2. $y=x^{2}+2 x+\mathrm{C} \quad: \quad y^{\prime}-2 x-2=0$
3. $y=\cos x+\mathrm{C} \quad: \quad y^{\prime}+\sin x=0$
4. $y=\sqrt{1+x^{2}} \quad: \quad y^{\prime}=\frac{x y}{1+x^{2}}$
5. $y=\mathrm{A} x \quad: \quad x y^{\prime}=y(x \neq 0)$
6. $y=x \sin x \quad: \quad x y^{\prime}=y+x \sqrt{x^{2}-y^{2}} \quad(x \neq 0$ and $x>y$ or $x<-y)$
7. $x y=\log y+\mathrm{C} \quad: \quad y^{\prime}=\frac{y^{2}}{1-x y}(x y \neq 1)$
8. $y-\cos y=x \quad: \quad(y \sin y+\cos y+x) y^{\prime}=y$
9. $x+y=\tan ^{-1} y \quad: \quad y^{2} y^{\prime}+y^{2}+1=0$
10. $y=\sqrt{a^{2}-x^{2}} x \in(-a, a): \quad x+y \frac{d y}{d x}=0(y \neq 0)$
11. The number of arbitrary constants in the general solution of a differential equation of fourth order are:
(A) 0
(B) 2
(C) 3
(D) 4
12. The number of arbitrary constants in the particular solution of a differential equation of third order are:
(A) 3
(B) 2
(C) 1
(D) 0

### 9.4. Methods of Solving First Order, First Degree Differential Equations

In this section we shall discuss three methods of solving first order first degree differential equations.

### 9.4.1 Differential equations with variables separable

A first order-first degree differential equation is of the form

$$
\begin{equation*}
\frac{d y}{d x}=\mathrm{F}(x, y) \tag{1}
\end{equation*}
$$

If $\mathrm{F}(x, y)$ can be expressed as a product $\mathrm{g}(x) h(y)$, where, $g(x)$ is a function of $x$ and $h(y)$ is a function of $y$, then the differential equation (1) is said to be of variable separable type. The differential equation (1) then has the form

$$
\begin{equation*}
\frac{d y}{d x}=h(y) \cdot g(x) \tag{2}
\end{equation*}
$$

If $h(y) \neq 0$, separating the variables, (2) can be rewritten as

$$
\begin{equation*}
\frac{1}{h(y)} d y=g(x) d x \tag{3}
\end{equation*}
$$

Integrating both sides of (3), we get

$$
\begin{equation*}
\int \frac{1}{h(y)} d y=\int g(x) d x \tag{4}
\end{equation*}
$$

Thus, (4) provides the solutions of given differential equation in the form

$$
\mathrm{H}(y)=\mathrm{G}(x)+\mathrm{C}
$$

Here, $\mathrm{H}(y)$ and $\mathrm{G}(x)$ are the anti derivatives of $\frac{1}{h(y)}$ and $g(x)$ respectively and C is the arbitrary constant.

Example 4 Find the general solution of the differential equation $\frac{d y}{d x}=\frac{x+1}{2-y},(y \neq 2)$
Solution We have

$$
\begin{equation*}
\frac{d y}{d x}=\frac{x+1}{2-y} \tag{1}
\end{equation*}
$$

Separating the variables in equation (1), we get

$$
\begin{equation*}
(2-y) d y=(x+1) d x \tag{2}
\end{equation*}
$$

Integrating both sides of equation (2), we get

$$
\int(2-y) d y=\int(x+1) d x
$$

or

$$
2 y-\frac{y^{2}}{2}=\frac{x^{2}}{2}+x+\mathrm{C}_{1}
$$

or

$$
\begin{aligned}
x^{2}+y^{2}+2 x-4 y+2 \mathrm{C}_{1} & =0 \\
x^{2}+y^{2}+2 x-4 y+\mathrm{C} & =0, \text { where } \mathrm{C}=2 \mathrm{C}_{1}
\end{aligned}
$$

or
which is the general solution of equation (1).

Example 5 Find the general solution of the differential equation $\frac{d y}{d x}=\frac{1+y^{2}}{1+x^{2}}$.
Solution Since $1+y^{2} \neq 0$, therefore separating the variables, the given differential equation can be written as

$$
\begin{equation*}
\frac{d y}{1+y^{2}}=\frac{d x}{1+x^{2}} \tag{1}
\end{equation*}
$$

Integrating both sides of equation (1), we get
or

$$
\begin{aligned}
\int \frac{d y}{1+y^{2}} & =\int \frac{d x}{1+x^{2}} \\
\tan ^{-1} y & =\tan ^{-1} x+\mathrm{C}
\end{aligned}
$$

which is the general solution of equation (1).
Example 6 Find the particular solution of the differential equation $\frac{d y}{d x}=-4 x y^{2}$ given that $y=1$, when $x=0$.

Solution If $y \neq 0$, the given differential equation can be written as

$$
\begin{equation*}
\frac{d y}{y^{2}}=-4 x d x \tag{1}
\end{equation*}
$$

Integrating both sides of equation (1), we get
or

$$
\begin{align*}
\int \frac{d y}{y^{2}} & =-4 \int x d x \\
-\frac{1}{y} & =-2 x^{2}+\mathrm{C} \\
y & =\frac{1}{2 x^{2}-\mathrm{C}} \tag{2}
\end{align*}
$$

or
Substituting $y=1$ and $x=0$ in equation (2), we get, $\mathrm{C}=-1$.
Now substituting the value of C in equation (2), we get the particular solution of the given differential equation as $y=\frac{1}{2 x^{2}+1}$.

Example 7 Find the equation of the curve passing through the point $(1,1)$ whose differential equation is $x d y=\left(2 x^{2}+1\right) d x(x \neq 0)$.

Solution The given differential equation can be expressed as
or

$$
\begin{align*}
d y^{*} & =\left(\frac{2 x^{2}+1}{x}\right) d x^{*} \\
d y & =\left(2 x+\frac{1}{x}\right) d x \tag{1}
\end{align*}
$$

Integrating both sides of equation (1), we get
or

$$
\begin{align*}
\int d y & =\int\left(2 x+\frac{1}{x}\right) d x \\
y & =x^{2}+\log |x|+\mathrm{C} \tag{2}
\end{align*}
$$

Equation (2) represents the family of solution curves of the given differential equation but we are interested in finding the equation of a particular member of the family which passes through the point $(1,1)$. Therefore substituting $x=1, y=1$ in equation (2), we get $\mathrm{C}=0$.

Now substituting the value of C in equation (2) we get the equation of the required curve as $y=x^{2}+\log |x|$.

Example 8 Find the equation of a curve passing through the point ( $-2,3$ ), given that the slope of the tangent to the curve at any point $(x, y)$ is $\frac{2 x}{y^{2}}$.

Solution We know that the slope of the tangent to a curve is given by $\frac{d y}{d x}$.
so,

$$
\begin{equation*}
\frac{d y}{d x}=\frac{2 x}{y^{2}} \tag{1}
\end{equation*}
$$

Separating the variables, equation (1) can be written as

$$
\begin{equation*}
y^{2} d y=2 x d x \tag{2}
\end{equation*}
$$

Integrating both sides of equation (2), we get
or

$$
\begin{align*}
\int y^{2} d y & =\int 2 x d x \\
\frac{y^{3}}{3} & =x^{2}+\mathrm{C} \tag{3}
\end{align*}
$$

[^0]Substituting $x=-2, y=3$ in equation (3), we get $\mathrm{C}=5$.
Substituting the value of C in equation (3), we get the equation of the required curve as

$$
\frac{y^{3}}{3}=x^{2}+5 \text { or } y=\left(3 x^{2}+15\right)^{\frac{1}{3}}
$$

Example 9 In a bank, principal increases continuously at the rate of 5\% per year. In how many years Rs 1000 double itself?

Solution Let P be the principal at any time $t$. According to the given problem,
or

$$
\begin{align*}
& \frac{d p}{d t}=\left(\frac{5}{100}\right) \times \mathrm{P} \\
& \frac{d p}{d t}=\frac{\mathrm{P}}{20} \tag{1}
\end{align*}
$$

separating the variables in equation (1), we get

$$
\begin{equation*}
\frac{d p}{\mathrm{P}}=\frac{d t}{20} \tag{2}
\end{equation*}
$$

Integrating both sides of equation (2), we get
or

$$
\begin{aligned}
\log \mathrm{P} & =\frac{t}{20}+\mathrm{C}_{1} \\
\mathrm{P} & =e^{\frac{t}{20}} \cdot e^{\mathrm{C}_{1}}
\end{aligned}
$$

$$
\begin{equation*}
\mathrm{P}=\mathrm{C} e^{\frac{t}{20}}\left(\text { where } e^{\mathrm{C}_{1}}=\mathrm{C}\right) \tag{3}
\end{equation*}
$$

or

$$
\mathrm{P}=1000, \text { when } t=0
$$

Substituting the values of P and $t$ in (3), we get $\mathrm{C}=1000$. Therefore, equation (3), gives

$$
\mathrm{P}=1000 e^{\frac{t}{20}}
$$

Let $t$ years be the time required to double the principal. Then

$$
2000=1000 e^{\frac{t}{20}} \Rightarrow t=20 \log _{e} 2
$$

## EXERCISE 9.3

For each of the differential equations in Exercises 1 to 10, find the general solution:

1. $\frac{d y}{d x}=\frac{1-\cos x}{1+\cos x}$
2. $\frac{d y}{d x}=\sqrt{4-y^{2}} \quad(-2<y<2)$
3. $\frac{d y}{d x}+y=1(y \neq 1)$
4. $\sec ^{2} x \tan y d x+\sec ^{2} y \tan x d y=0$
5. $\left(e^{x}+e^{-x}\right) d y-\left(e^{x}-e^{-x}\right) d x=0$
6. $\frac{d y}{d x}=\left(1+x^{2}\right)\left(1+y^{2}\right)$
7. $y \log y d x-x d y=0$
8. $x^{5} \frac{d y}{d x}=-y^{5}$
9. $\frac{d y}{d x}=\sin ^{-1} x$
10. $e^{x} \tan y d x+\left(1-e^{x}\right) \sec ^{2} y d y=0$

For each of the differential equations in Exercises 11 to 14, find a particular solution satisfying the given condition:
11. $\left(x^{3}+x^{2}+x+1\right) \frac{d y}{d x}=2 x^{2}+x ; y=1$ when $x=0$
12. $x\left(x^{2}-1\right) \frac{d y}{d x}=1 ; y=0$ when $x=2$
13. $\cos \left(\frac{d y}{d x}\right)=a(a \in \mathbf{R}) ; y=1$ when $x=0$
14. $\frac{d y}{d x}=y \tan x ; y=1$ when $x=0$
15. Find the equation of a curve passing through the point $(0,0)$ and whose differential equation is $y^{\prime}=e^{x} \sin x$.
16. For the differential equation $x y \frac{d y}{d x}=(x+2)(y+2)$, find the solution curve passing through the point $(1,-1)$.
17. Find the equation of a curve passing through the point $(0,-2)$ given that at any point ( $x, y$ ) on the curve, the product of the slope of its tangent and $y$ coordinate of the point is equal to the $x$ coordinate of the point.
18. At any point $(x, y)$ of a curve, the slope of the tangent is twice the slope of the line segment joining the point of contact to the point $(-4,-3)$. Find the equation of the curve given that it passes through $(-2,1)$.
19. The volume of spherical balloon being inflated changes at a constant rate. If initially its radius is 3 units and after 3 seconds it is 6 units. Find the radius of balloon after $t$ seconds.
20. In a bank, principal increases continuously at the rate of $r \%$ per year. Find the value of $r$ if Rs 100 double itself in 10 years ( $\log _{e} 2=0.6931$ ).
21. In a bank, principal increases continuously at the rate of $5 \%$ per year. An amount of Rs 1000 is deposited with this bank, how much will it worth after 10 years ( $e^{0.5}=1.648$ ).
22. In a culture, the bacteria count is $1,00,000$. The number is increased by $10 \%$ in 2 hours. In how many hours will the count reach $2,00,000$, if the rate of growth of bacteria is proportional to the number present?
23. The general solution of the differential equation $\frac{d y}{d x}=e^{x+y}$ is
(A) $e^{x}+e^{-y}=\mathrm{C}$
(B) $e^{x}+e^{y}=\mathrm{C}$
(C) $e^{-x}+e^{y}=\mathrm{C}$
(D) $e^{-x}+e^{-y}=\mathrm{C}$

### 9.4.2 Homogeneous differential equations

Consider the following functions in $x$ and $y$

$$
\begin{array}{ll}
\mathrm{F}_{1}(x, y)=y^{2}+2 x y, & \mathrm{~F}_{2}(x, y)=2 x-3 y \\
\mathrm{~F}_{3}(x, y)=\cos \left(\frac{y}{x}\right), & \mathrm{F}_{4}(x, y)=\sin x+\cos y
\end{array}
$$

If we replace $x$ and $y$ by $\lambda x$ and $\lambda y$ respectively in the above functions, for any nonzero constant $\lambda$, we get

$$
\begin{aligned}
& \mathrm{F}_{1}(\lambda x, \lambda y)=\lambda^{2}\left(y^{2}+2 x y\right)=\lambda^{2} \mathrm{~F}_{1}(x, y) \\
& \mathrm{F}_{2}(\lambda x, \lambda y)=\lambda(2 x-3 y)=\lambda \mathrm{F}_{2}(x, y) \\
& \mathrm{F}_{3}(\lambda x, \lambda y)=\cos \left(\frac{\lambda y}{\lambda x}\right)=\cos \left(\frac{y}{x}\right)=\lambda^{0} \mathrm{~F}_{3}(x, y) \\
& \mathrm{F}_{4}(\lambda x, \lambda y)=\sin \lambda x+\cos \lambda y \neq \lambda^{n} \mathrm{~F}_{4}(x, y), \text { for any } n \in \mathbf{N}
\end{aligned}
$$

Here, we observe that the functions $\mathrm{F}_{1}, \mathrm{~F}_{2}, \mathrm{~F}_{3}$ can be written in the form $\mathrm{F}(\lambda x, \lambda y)=\lambda^{n} \mathrm{~F}(x, y)$ but $\mathrm{F}_{4}$ can not be written in this form. This leads to the following definition:

A function $\mathrm{F}(x, y)$ is said to be homogeneous function of degree $n$ if
$\mathrm{F}(\lambda x, \lambda y)=\lambda^{n} \mathrm{~F}(x, y)$ for any nonzero constant $\lambda$.
We note that in the above examples, $\mathrm{F}_{1}, \mathrm{~F}_{2}, \mathrm{~F}_{3}$ are homogeneous functions of degree $2,1,0$ respectively but $\mathrm{F}_{4}$ is not a homogeneous function.

We also observe that
or
or
or

$$
\begin{aligned}
& \mathrm{F}_{1}(x, y)=x^{2}\left(\frac{y^{2}}{x^{2}}+\frac{2 y}{x}\right)=x^{2} h_{1}\left(\frac{y}{x}\right) \\
& \mathrm{F}_{1}(x, y)=y^{2}\left(1+\frac{2 x}{y}\right)=y^{2} h_{2}\left(\frac{x}{y}\right) \\
& \mathrm{F}_{2}(x, y)=x^{1}\left(2-\frac{3 y}{x}\right)=x^{1} h_{3}\left(\frac{y}{x}\right) \\
& \mathrm{F}_{2}(x, y)=y^{1}\left(2 \frac{x}{y}-3\right)=y^{1} h_{4}\left(\frac{x}{y}\right) \\
& \mathrm{F}_{3}(x, y)=x^{0} \cos \left(\frac{y}{x}\right)=x^{0} h_{5}\left(\frac{y}{x}\right) \\
& \mathrm{F}_{4}(x, y) \neq x^{n} h_{6}\left(\frac{y}{x}\right), \text { for any } n \in \mathbf{N} \\
& \mathrm{~F}_{4}(x, y) \neq y^{n} h_{7}\left(\frac{x}{y}\right), \text { for any } n \in \mathbf{N}
\end{aligned}
$$

## -

Therefore, a function $\mathrm{F}(x, y)$ is a homogeneous function of degree $n$ if

$$
\mathrm{F}(x, y)=x^{n} g\left(\frac{y}{x}\right) \quad \text { or } \quad y^{n} h\left(\frac{x}{y}\right)
$$

A differential equation of the form $\frac{d y}{d x}=\mathrm{F}(x, y)$ is said to be homogenous if $\mathrm{F}(x, y)$ is a homogenous function of degree zero.
To solve a homogeneous differential equation of the type

$$
\begin{equation*}
\frac{d y}{d x}=\mathrm{F}(x, y)=g\left(\frac{y}{x}\right) \tag{1}
\end{equation*}
$$

We make the substitution

$$
\begin{equation*}
y=v \cdot x \tag{2}
\end{equation*}
$$

Differentiating equation (2) with respect to $x$, we get

$$
\begin{equation*}
\frac{d y}{d x}=v+x \frac{d v}{d x} \tag{3}
\end{equation*}
$$

Substituting the value of $\frac{d y}{d x}$ from equation (3) in equation (1), we get

$$
\begin{align*}
v+x \frac{d v}{d x} & =g(v) \\
x \frac{d v}{d x} & =g(v)-v \tag{4}
\end{align*}
$$

or

Integrating both sides of equation (5), we get

$$
\begin{equation*}
\int \frac{d v}{g(v)-v}=\int \frac{1}{x} d x+\mathrm{C} \tag{6}
\end{equation*}
$$

Equation (6) gives general solution (primitive) of the differential equation (1) when we replace $v$ by $\frac{y}{x}$.

Note If the homogeneous differential equation is in the form $\frac{d x}{d y}=\mathrm{F}(x, y)$ where, $\mathrm{F}(x, y)$ is homogenous function of degree zero, then we make substitution $\frac{x}{y}=v$ i.e., $x=v y$ and we proceed further to find the general solution as discussed above by writing $\frac{d x}{d y}=\mathrm{F}(x, y)=h\left(\frac{x}{y}\right)$.

Example 10 Show that the differential equation $(x-y) \frac{d y}{d x}=x+2 y$ is homogeneous and solve it.

Solution The given differential equation can be expressed as

$$
\begin{equation*}
\frac{d y}{d x}=\frac{x+2 y}{x-y} \tag{1}
\end{equation*}
$$

Let

$$
\mathrm{F}(x, y)=\frac{x+2 y}{x-y}
$$

Now

$$
\mathrm{F}(\lambda x, \lambda y)=\frac{\lambda(x+2 y)}{\lambda(x-y)}=\lambda^{0} \cdot f(x, y)
$$

Therefore, $\mathrm{F}(x, y)$ is a homogenous function of degree zero. So, the given differential equation is a homogenous differential equation.
Alternatively,

$$
\begin{equation*}
\frac{d y}{d x}=\left(\frac{1+\frac{2 y}{x}}{1-\frac{y}{x}}\right)=g\left(\frac{y}{x}\right) \tag{2}
\end{equation*}
$$

R.H.S. of differential equation (2) is of the form $g\left(\frac{y}{x}\right)$ and so it is a homogeneous function of degree zero. Therefore, equation (1) is a homogeneous differential equation. To solve it we make the substitution

$$
\begin{equation*}
y=v x \tag{3}
\end{equation*}
$$

Differentiating equation (3) with respect to, $x$ we get

$$
\begin{equation*}
\frac{d y}{d x}=v+x \frac{d v}{d x} \tag{4}
\end{equation*}
$$

Substituting the value of $y$ and $\frac{d y}{d x}$ in equation (1) we get
or

$$
\begin{aligned}
v+x \frac{d v}{d x} & =\frac{1+2 v}{1-v} \\
x \frac{d v}{d x} & =\frac{1+2 v}{1-v}-v
\end{aligned}
$$

or

$$
x \frac{d v}{d x}=\frac{v^{2}+v+1}{1-v}
$$

or

$$
\frac{v-1}{v^{2}+v+1} d v=\frac{-d x}{x}
$$

Integrating both sides of equation (5), we get
or

$$
\begin{aligned}
\int \frac{v-1}{v^{2}+v+1} d v & =-\int \frac{d x}{x} \\
\frac{1}{2} \int \frac{2 v+1-3}{v^{2}+v+1} d v & =-\log |x|+\mathrm{C}_{1}
\end{aligned}
$$

or

$$
\frac{1}{2} \int \frac{2 v+1}{v^{2}+v+1} d v-\frac{3}{2} \int \frac{1}{v^{2}+v+1} d v=-\log |x|+\mathrm{C}_{1}
$$

or

$$
\frac{1}{2} \log \left|v^{2}+v+1\right|-\frac{3}{2} \int \frac{1}{\left(v+\frac{1}{2}\right)^{2}+\left(\frac{\sqrt{3}}{2}\right)^{2}} d v=-\log |x|+\mathrm{C}_{1}
$$

or

$$
\frac{1}{2} \log \left|v^{2}+v+1\right|-\frac{3}{2} \cdot \frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{2 v+1}{\sqrt{3}}\right)=-\log |x|+\mathrm{C}_{1}
$$

or

$$
\frac{1}{2} \log \left|v^{2}+v+1\right|+\frac{1}{2} \log x^{2}=\sqrt{3} \tan ^{-1}\left(\frac{2 v+1}{\sqrt{3}}\right)+\mathrm{C}_{1}
$$

(Why?)

Replacing $v$ by $\frac{y}{x}$, we get
or

$$
\frac{1}{2} \log \left|\frac{y^{2}}{x^{2}}+\frac{y}{x}+1\right|+\frac{1}{2} \log x^{2}=\sqrt{3} \tan ^{-1}\left(\frac{2 y+x}{\sqrt{3} x}\right)+\mathrm{C}_{1}
$$

or

$$
\frac{1}{2} \log \left|\left(\frac{y^{2}}{x^{2}}+\frac{y}{x}+1\right) x^{2}\right|=\sqrt{3} \tan ^{-1}\left(\frac{2 y+x}{\sqrt{3} x}\right)+\mathrm{C}_{1}
$$

or

$$
\log \left|\left(y^{2}+x y+x^{2}\right)\right|=2 \sqrt{3} \tan ^{-1}\left(\frac{2 y+x}{\sqrt{3} x}\right)+2 \mathrm{C}_{1}
$$

or

$$
\log \left|\left(x^{2}+x y+y^{2}\right)\right|=2 \sqrt{3} \tan ^{-1}\left(\frac{x+2 y}{\sqrt{3} x}\right)+\mathrm{C}
$$

which is the general solution of the differential equation (1)
Example 11 Show that the differential equation $x \cos \left(\frac{y}{x}\right) \frac{d y}{d x}=y \cos \left(\frac{y}{x}\right)+x$ is homogeneous and solve it.

Solution The given differential equation can be written as

$$
\begin{equation*}
\frac{d y}{d x}=\frac{y \cos \left(\frac{y}{x}\right)+x}{x \cos \left(\frac{y}{x}\right)} \tag{1}
\end{equation*}
$$

It is a differential equation of the form $\frac{d y}{d x}=\mathrm{F}(x, y)$.

Here

$$
\mathrm{F}(x, y)=\frac{y \cos \left(\frac{y}{x}\right)+x}{x \cos \left(\frac{y}{x}\right)}
$$

Replacing $x$ by $\lambda x$ and $y$ by $\lambda y$, we get

$$
\mathrm{F}(\lambda x, \lambda y)=\frac{\lambda\left[y \cos \left(\frac{y}{x}\right)+x\right]}{\lambda\left(x \cos \frac{y}{x}\right)}=\lambda^{0}[\mathrm{~F}(x, y)]
$$

Thus, $\mathrm{F}(x, y)$ is a homogeneous function of degree zero.
Therefore, the given differential equation is a homogeneous differential equation. To solve it we make the substitution

$$
\begin{equation*}
y=v x \tag{2}
\end{equation*}
$$

Differentiating equation (2) with respect to $x$, we get

$$
\begin{equation*}
\frac{d y}{d x}=v+x \frac{d v}{d x} \tag{3}
\end{equation*}
$$

Substituting the value of $y$ and $\frac{d y}{d x}$ in equation (1), we get
or

$$
v+x \frac{d v}{d x}=\frac{v \cos v+1}{\cos v}
$$

$$
x \frac{d v}{d x}=\frac{v \cos v+1}{\cos v}-v
$$

or

$$
x \frac{d v}{d x}=\frac{1}{\cos v}
$$

or

$$
\cos v d v=\frac{d x}{x}
$$

Therefore

$$
\int \cos v d v=\int \frac{1}{x} d x
$$

or
or

$$
\begin{aligned}
& \sin v=\log |x|+\log |\mathrm{C}| \\
& \sin v=\log |\mathrm{C} x|
\end{aligned}
$$

Replacing $v$ by $\frac{y}{x}$, we get

$$
\sin \left(\frac{y}{x}\right)=\log |\mathrm{C} x|
$$

which is the general solution of the differential equation (1).
Example 12 Show that the differential equation $2 y e^{\frac{x}{y}} d x+\left(y-2 x e^{\frac{x}{y}}\right) d y=0$ is homogeneous and find its particular solution, given that, $x=0$ when $y=1$.
Solution The given differential equation can be written as

$$
\begin{equation*}
\frac{d x}{d y}=\frac{2 x e^{\frac{x}{y}}-y}{2 y e^{\frac{x}{y}}} \tag{1}
\end{equation*}
$$

Let

$$
\mathrm{F}(x, y)=\frac{2 x e^{\frac{x}{y}}-y}{2 y e^{\frac{x}{y}}}
$$

Then

$$
\mathrm{F}(\lambda x, \lambda y)=\frac{\lambda\left(2 x e^{\frac{x}{y}}-y\right)}{\lambda\left(2 y e^{\frac{x}{y}}\right)}=\lambda^{0}[\mathrm{~F}(x, y)]
$$

Thus, $\mathrm{F}(x, y)$ is a homogeneous function of degree zero. Therefore, the given differential equation is a homogeneous differential equation.
To solve it, we make the substitution

$$
\begin{equation*}
x=v y \tag{2}
\end{equation*}
$$

Differentiating equation (2) with respect to $y$, we get

$$
\frac{d x}{d y}=v+y \frac{d v}{d y}
$$

Substituting the value of $x$ and $\frac{d x}{d y}$ in equation (1), we get
or

$$
\begin{aligned}
v+y \frac{d v}{d y} & =\frac{2 v e^{v}-1}{2 e^{v}} \\
y \frac{d v}{d y} & =\frac{2 v e^{v}-1}{2 e^{v}}-v \\
y \frac{d v}{d y} & =-\frac{1}{2 e^{v}}
\end{aligned}
$$

or
or

$$
2 e^{v} d v=\frac{-d y}{y}
$$

or

$$
\begin{aligned}
\int 2 e^{v} \cdot d v & =-\int \frac{d y}{y} \\
2 e^{v} & =-\log |y|+\mathrm{C}
\end{aligned}
$$

or

Substituting $x=0$ and $y=1$ in equation (3), we get

$$
2 e^{0}+\log |1|=\mathrm{C} \Rightarrow \mathrm{C}=2
$$

Substituting the value of C in equation (3), we get

$$
2 e^{\frac{x}{y}}+\log |y|=2
$$

which is the particular solution of the given differential equation.
Example 13 Show that the family of curves for which the slope of the tangent at any point $(x, y)$ on it is $\frac{x^{2}+y^{2}}{2 x y}$, is given by $x^{2}-y^{2}=c x$.
Solution We know that the slope of the tangent at any point on a curve is $\frac{d y}{d x}$.

Therefore,

$$
\frac{d y}{d x}=\frac{x^{2}+y^{2}}{2 x y}
$$

or

$$
\begin{equation*}
\frac{d y}{d x}=\frac{1+\frac{y^{2}}{x^{2}}}{\frac{2 y}{x}} \tag{1}
\end{equation*}
$$

Clearly, (1) is a homogenous differential equation. To solve it we make substitution

$$
y=v x
$$

Differentiating $y=v x$ with respect to $x$, we get
or

$$
v+x \frac{d v}{d x}=\frac{1+v^{2}}{2 v}
$$

or

$$
x \frac{d v}{d x}=\frac{1-v^{2}}{2 v}
$$

$$
\frac{2 v}{1-v^{2}} d v=\frac{d x}{x}
$$

or

$$
\frac{2 v}{v^{2}-1} d v=-\frac{d x}{x}
$$

Therefore

$$
\int \frac{2 v}{v^{2}-1} d v=-\int \frac{1}{x} d x
$$

or

$$
\log \left|v^{2}-1\right|=-\log |x|+\log \left|C_{1}\right|
$$

or

$$
\log \left|\left(v^{2}-1\right)(x)\right|=\log \left|\mathrm{C}_{1}\right|
$$

or

$$
\left(v^{2}-1\right) x= \pm \mathrm{C}_{1}
$$

Replacing $v$ by $\frac{y}{x}$, we get
or

$$
\begin{aligned}
\left(\frac{y^{2}}{x^{2}}-1\right) x & = \pm \mathrm{C}_{1} \\
\left(y^{2}-x^{2}\right) & = \pm \mathrm{C}_{1} x \text { or } x^{2}-y^{2}=\mathrm{C} x
\end{aligned}
$$

## EXERCISE 9.4

In each of the Exercises 1 to 10, show that the given differential equation is homogeneous and solve each of them.

1. $\left(x^{2}+x y\right) d y=\left(x^{2}+y^{2}\right) d x$
2. $y^{\prime}=\frac{x+y}{x}$
3. $(x-y) d y-(x+y) d x=0$
4. $\left(x^{2}-y^{2}\right) d x+2 x y d y=0$
5. $x^{2} \frac{d y}{d x}=x^{2}-2 y^{2}+x y$
6. $x d y-y d x=\sqrt{x^{2}+y^{2}} d x$
7. $\left\{x \cos \left(\frac{y}{x}\right)+y \sin \left(\frac{y}{x}\right)\right\} y d x=\left\{y \sin \left(\frac{y}{x}\right)-x \cos \left(\frac{y}{x}\right)\right\} x d y$
8. $x \frac{d y}{d x}-y+x \sin \left(\frac{y}{x}\right)=0$
9. $y d x+x \log \left(\frac{y}{x}\right) d y-2 x d y=0$
10. $\left(1+e^{\frac{x}{y}}\right) d x+e^{\frac{x}{y}}\left(1-\frac{x}{y}\right) d y=0$

For each of the differential equations in Exercises from 11 to 15, find the particular solution satisfying the given condition:
11. $(x+y) d y+(x-y) d x=0 ; y=1$ when $x=1$
12. $x^{2} d y+\left(x y+y^{2}\right) d x=0 ; y=1$ when $x=1$
13. $\left[x \sin ^{2}\left(\frac{y}{x}\right)-y\right] d x+x d y=0 ; y=\frac{\pi}{4} \quad$ when $x=1$
14. $\frac{d y}{d x}-\frac{y}{x}+\operatorname{cosec}\left(\frac{y}{x}\right)=0 ; y=0$ when $x=1$
15. $2 x y+y^{2}-2 x^{2} \frac{d y}{d x}=0 ; y=2$ when $x=1$
16. A homogeneous differential equation of the from $\frac{d x}{d y}=h\left(\frac{x}{y}\right)$ can be solved by making the substitution.
(A) $y=v x$
(B) $v=y x$
(C) $x=v y$
(D) $x=v$
17. Which of the following is a homogeneous differential equation?
(A) $(4 x+6 y+5) d y-(3 y+2 x+4) d x=0$
(B) $(x y) d x-\left(x^{3}+y^{3}\right) d y=0$
(C) $\left(x^{3}+2 y^{2}\right) d x+2 x y d y=0$
(D) $y^{2} d x+\left(x^{2}-x y-y^{2}\right) d y=0$

### 9.4.3 Linear differential equations

A differential equation of the from

$$
\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q}
$$

where, P and Q are constants or functions of $x$ only, is known as a first order linear differential equation. Some examples of the first order linear differential equation are

$$
\begin{aligned}
\frac{d y}{d x}+y & =\sin x \\
\frac{d y}{d x}+\left(\frac{1}{x}\right) y & =e^{x} \\
\frac{d y}{d x}+\left(\frac{y}{x \log x}\right) & =\frac{1}{x}
\end{aligned}
$$

Another form of first order linear differential equation is

$$
\frac{d x}{d y}+\mathrm{P}_{1} x=\mathrm{Q}_{1}
$$

where, $\mathrm{P}_{1}$ and $\mathrm{Q}_{1}$ are constants or functions of $y$ only. Some examples of this type of differential equation are

$$
\begin{aligned}
\frac{d x}{d y}+x & =\cos y \\
\frac{d x}{d y}+\frac{-2 x}{y} & =y^{2} e^{-y}
\end{aligned}
$$

To solve the first order linear differential equation of the type

$$
\begin{equation*}
\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q} \tag{1}
\end{equation*}
$$

Multiply both sides of the equation by a function of $x$ say $g(x)$ to get

$$
\begin{equation*}
g(x) \frac{d y}{d x}+\mathrm{P} \cdot(g(x)) y=\mathrm{Q} \cdot g(x) \tag{2}
\end{equation*}
$$

Choose $g(x)$ in such a way that R.H.S. becomes a derivative of $y \cdot g(x)$.
i.e.

$$
g(x) \frac{d y}{d x}+\mathrm{P} \cdot g(x) y=\frac{d}{d x}[y \cdot g(x)]
$$

or

$$
g(x) \frac{d y}{d x}+\mathrm{P} \cdot g(x) y=g(x) \frac{d y}{d x}+y g^{\prime}(x)
$$

$\Rightarrow$

$$
\text { P. } g(x)=g^{\prime}(x)
$$

or

$$
\mathrm{P}=\frac{g^{\prime}(x)}{g(x)}
$$

Integrating both sides with respect to $x$, we get
or

$$
\begin{aligned}
\int \mathrm{P} d x & =\int \frac{g^{\prime}(x)}{g(x)} d x \\
\int \mathrm{P} \cdot d x & =\log (g(x)) \\
\mathrm{g}(x) & =e^{\int \mathrm{P} d x}
\end{aligned}
$$

or
On multiplying the equation (1) by $g(x)=e^{\int \mathrm{P} d x}$, the L.H.S. becomes the derivative of some function of $x$ and $y$. This function $g(x)=e^{\int \mathrm{P} d x}$ is called Integrating Factor (I.F.) of the given differential equation.

Substituting the value of $g(x)$ in equation (2), we get
or

$$
\begin{aligned}
e^{\int \mathrm{P} d x} \frac{d y}{d x}+\mathrm{P} e^{\int \mathrm{P} d x} y & =\mathrm{Q} \cdot e^{\int \mathrm{P} d x} \\
\frac{d}{d x}\left(y e^{\int \mathrm{P} d x}\right) & =\mathrm{Q} e^{\int \mathrm{P} d x}
\end{aligned}
$$

Integrating both sides with respect to $x$, we get
or

$$
\begin{aligned}
y \cdot e^{\int \mathrm{P} d x} & =\int\left(\mathrm{Q} \cdot e^{\int \mathrm{P} d x}\right) d x \\
y & =e^{-\int \mathrm{P} d x} \cdot \int\left(\mathrm{Q} \cdot e^{\int \mathrm{P} d x}\right) d x+\mathrm{C}
\end{aligned}
$$

which is the general solution of the differential equation.

## Steps involved to solve first order linear differential equation:

(i) Write the given differential equation in the form $\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q}$ where $\mathrm{P}, \mathrm{Q}$ are constants or functions of $x$ only.
(ii) Find the Integrating Factor (I.F) $=e^{\int \mathrm{P} d x}$.
(iii) Write the solution of the given differential equation as

$$
y(\mathrm{I} . \mathrm{F})=\int(\mathrm{Q} \times \mathrm{I} . \mathrm{F}) d x+\mathrm{C}
$$

In case, the first order linear differential equation is in the form $\frac{d x}{d y}+\mathrm{P}_{1} x=\mathrm{Q}_{1}$, where, $\mathrm{P}_{1}$ and $\mathrm{Q}_{1}$ are constants or functions of $y$ only. Then I.F $=e^{\mathrm{P}_{1} d y}$ and the solution of the differential equation is given by

$$
x .(\mathrm{I} . \mathrm{F})=\int\left(\mathrm{Q}_{1} \times \mathrm{I} . \mathrm{F}\right) d y+\mathrm{C}
$$

Example 14 Find the general solution of the differential equation $\frac{d y}{d x}-y=\cos x$.
Solution Given differential equation is of the form

$$
\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q}, \text { where } \mathrm{P}=-1 \text { and } \mathrm{Q}=\cos x
$$

Therefore

$$
\text { I. } \mathrm{F}=e^{\int-1 d x}=e^{-x}
$$

Multiplying both sides of equation by I.F, we get
or

$$
\begin{aligned}
e^{-x} \frac{d y}{d x}-e^{-x} y & =e^{-x} \cos x \\
\frac{d y}{d x}\left(y e^{-x}\right) & =e^{-x} \cos x
\end{aligned}
$$

On integrating both sides with respect to $x$, we get

$$
\begin{equation*}
y e^{-x}=\int e^{-x} \cos x d x+\mathrm{C} \tag{1}
\end{equation*}
$$

Let

$$
\begin{aligned}
I & =\int e^{-x} \cos x d x \\
& =\cos x\left(\frac{e^{-x}}{-1}\right)-\int(-\sin x)\left(-e^{-x}\right) d x
\end{aligned}
$$

or

$$
\begin{aligned}
& =-\cos x e^{-x}-\int \sin x e^{-x} d x \\
& =-\cos x e^{-x}-\left[\sin x\left(-e^{-x}\right)-\int \cos x\left(-e^{-x}\right) d x\right] \\
& =-\cos x e^{-x}+\sin x e^{-x}-\int \cos x e^{-x} d x \\
\mathrm{I} & =-e^{-x} \cos x+\sin x e^{-x}-\mathrm{I} \\
2 \mathrm{I} & =(\sin x-\cos x) e^{-x} \\
\mathrm{I} & =\frac{(\sin x-\cos x) e^{-x}}{2}
\end{aligned}
$$

or
or

Substituting the value of I in equation (1), we get
or

$$
\begin{aligned}
y e^{-x} & =\left(\frac{\sin x-\cos x}{2}\right) e^{-x}+\mathrm{C} \\
y & =\left(\frac{\sin x-\cos x}{2}\right)+\mathrm{C} e^{x}
\end{aligned}
$$

which is the general solution of the given differential equation.
Example 15 Find the general solution of the differential equation $x \frac{d y}{d x}+2 y=x^{2}(x \neq 0)$.
Solution The given differential equation is

$$
\begin{equation*}
x \frac{d y}{d x}+2 y=x^{2} \tag{1}
\end{equation*}
$$

Dividing both sides of equation (1) by $x$, we get

$$
\frac{d y}{d x}+\frac{2}{x} y=x
$$

which is a linear differential equation of the type $\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q}$, where $\mathrm{P}=\frac{2}{x}$ and $\mathrm{Q}=x$.
So

$$
\mathrm{I} . \mathrm{F}=e^{\int \frac{2}{x} d x}=e^{2 \log x}=e^{\log x^{2}}=x^{2}\left[\text { as } e^{\log f(x)}=f(x)\right]
$$

Therefore, solution of the given equation is given by
or

$$
\begin{array}{r}
y \cdot x^{2}=\int(x)\left(x^{2}\right) d x+\mathrm{C}=\int x^{3} d x+\mathrm{C} \\
y=\frac{x^{2}}{4}+\mathrm{C} x^{-2}
\end{array}
$$

which is the general solution of the given differential equation.

Example 16 Find the general solution of the differential equation $y d x-\left(x+2 y^{2}\right) d y=0$.
Solution The given differential equation can be written as

$$
\frac{d x}{d y}-\frac{x}{y}=2 y
$$

This is a linear differential equation of the type $\frac{d x}{d y}+\mathrm{P}_{1} x=\mathrm{Q}_{1}$, where $\mathrm{P}_{1}=-\frac{1}{y}$ and
$\mathrm{Q}_{1}=2 y$. Therefore I. $\mathrm{F}=e^{\int-\frac{1}{y} d y}=e^{-\log y}=e^{\log (y)^{-1}}=\frac{1}{y}$
Hence, the solution of the given differential equation is
or

$$
\begin{aligned}
x \frac{1}{y} & =\int(2 y)\left(\frac{1}{y}\right) d y+\mathrm{C} \\
\frac{x}{y} & =\int(2 d y)+\mathrm{C} \\
\frac{x}{y} & =2 y+\mathrm{C} \\
x & =2 y^{2}+\mathrm{C} y
\end{aligned}
$$

or
or
or
which is a general solution of the given differential equation.
Example 17 Find the particular solution of the differential equation

$$
\frac{d y}{d x}+y \cot x=2 x+x^{2} \cot x(x \neq 0)
$$

given that $y=0$ when $x=\frac{\pi}{2}$.
Solution The given equation is a linear differential equation of the type $\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q}$, where $\mathrm{P}=\cot x$ and $\mathrm{Q}=2 x+x^{2} \cot x$. Therefore

$$
\text { I.F }=e^{\int \cot x d x}=e^{\log \sin x}=\sin x
$$

Hence, the solution of the differential equation is given by

$$
y \cdot \sin x=\int\left(2 x+x^{2} \cot x\right) \sin x d x+\mathrm{C}
$$

or

$$
\begin{aligned}
& y \sin x=\int 2 x \sin x d x+\int x^{2} \cos x d x+\mathrm{C} \\
& y \sin x=\sin x\left(\frac{2 x^{2}}{2}\right)-\int \cos x\left(\frac{2 x^{2}}{2}\right) d x+\int x^{2} \cos x d x+\mathrm{C}
\end{aligned}
$$

or

$$
y \sin x=x^{2} \sin x-\int x^{2} \cos x d x+\int x^{2} \cos x d x+\mathrm{C}
$$

or

$$
\begin{equation*}
y \sin x=x^{2} \sin x+\mathrm{C} \tag{1}
\end{equation*}
$$

Substituting $y=0$ and $x=\frac{\pi}{2}$ in equation (1), we get
or

$$
\begin{aligned}
& 0=\left(\frac{\pi}{2}\right)^{2} \sin \left(\frac{\pi}{2}\right)+C \\
& C=\frac{-\pi^{2}}{4}
\end{aligned}
$$

Substituting the value of C in equation (1), we get

$$
\begin{aligned}
y \sin x & =x^{2} \sin x-\frac{\pi^{2}}{4} \\
y & =x^{2}-\frac{\pi^{2}}{4 \sin x}(\sin x \neq 0)
\end{aligned}
$$

which is the particular solution of the given differential equation.
Example 18 Find the equation of a curve passing through the point $(0,1)$. If the slope of the tangent to the curve at any point $(x, y)$ is equal to the sum of the $x$ coordinate (abscissa) and the product of the $x$ coordinate and $y$ coordinate (ordinate) of that point.
Solution We know that the slope of the tangent to the curve is $\frac{d y}{d x}$.

Therefore,

$$
\begin{align*}
\frac{d y}{d x} & =x+x y \\
\frac{d y}{d x}-x y & =x \tag{1}
\end{align*}
$$

or
This is a linear differential equation of the type $\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q}$, where $\mathrm{P}=-x$ and $\mathrm{Q}=x$.

Therefore,

$$
\text { I. } \mathrm{F}=e^{\int-x d x}=e^{\frac{-x^{2}}{2}}
$$

Hence, the solution of equation is given by

$$
\begin{equation*}
y \cdot e^{\frac{-x^{2}}{2}}=\int(x)\left(e^{\frac{-x^{2}}{2}}\right) d x+\mathrm{C} \tag{2}
\end{equation*}
$$

Let

$$
\mathrm{I}=\int(x) e^{\frac{-x^{2}}{2}} d x
$$

Let $\frac{-x^{2}}{2}=t$, then $-x d x=d t$ or $x d x=-d t$.
Therefore, $\quad \mathrm{I}=-\int e^{t} d t=-e^{t}=-e^{\frac{-x^{2}}{2}}$
Substituting the value of I in equation (2), we get
or

$$
\begin{align*}
y e^{\frac{-x^{2}}{2}} & =-e^{\frac{-x^{2}}{2}}+\mathrm{C} \\
y & =-1+\mathrm{C} e^{\frac{x^{2}}{2}} \tag{3}
\end{align*}
$$

Now (3) represents the equation of family of curves. But we are interested in finding a particular member of the family passing through $(0,1)$. Substituting $x=0$ and $y=1$ in equation (3) we get

$$
1=-1+\mathrm{C} \cdot e^{0} \quad \text { or } \quad \mathrm{C}=2
$$

Substituting the value of C in equation (3), we get

$$
y=-1+2 e^{\frac{x^{2}}{2}}
$$

which is the equation of the required curve.

## EXERCISE 9.5

For each of the differential equations given in Exercises 1 to 12, find the general solution:

1. $\frac{d y}{d x}+2 y=\sin x$
2. $\frac{d y}{d x}+3 y=e^{-2 x}$
3. $\frac{d y}{d x}+\frac{y}{x}=x^{2}$
4. $\frac{d y}{d x}+(\sec x) y=\tan x\left(0 \leq x<\frac{\pi}{2}\right)$
5. $\cos ^{2} x \frac{d y}{d x}+y=\tan x\left(0 \leq x<\frac{\pi}{2}\right)$
6. $x \frac{d y}{d x}+2 y=x^{2} \log x$
7. $x \log x \frac{d y}{d x}+y=\frac{2}{x} \log x$
8. $\left(1+x^{2}\right) d y+2 x y d x=\cot x d x(x \neq 0)$
9. $x \frac{d y}{d x}+y-x+x y \cot x=0(x \neq 0)$
10. $(x+y) \frac{d y}{d x}=1$
11. $y d x+\left(x-y^{2}\right) d y=0$
12. $\left(x+3 y^{2}\right) \frac{d y}{d x}=y(y>0)$.

For each of the differential equations given in Exercises 13 to 15, find a particular solution satisfying the given condition:
13. $\frac{d y}{d x}+2 y \tan x=\sin x ; y=0$ when $x=\frac{\pi}{3}$
14. $\left(1+x^{2}\right) \frac{d y}{d x}+2 x y=\frac{1}{1+x^{2}} ; y=0$ when $x=1$
15. $\frac{d y}{d x}-3 y \cot x=\sin 2 x ; y=2$ when $x=\frac{\pi}{2}$
16. Find the equation of a curve passing through the origin given that the slope of the tangent to the curve at any point $(x, y)$ is equal to the sum of the coordinates of the point.
17. Find the equation of a curve passing through the point $(0,2)$ given that the sum of the coordinates of any point on the curve exceeds the magnitude of the slope of the tangent to the curve at that point by 5 .
18. The Integrating Factor of the differential equation $x \frac{d y}{d x}-y=2 x^{2}$ is
(A) $e^{-x}$
(B) $e^{-y}$
(C) $\frac{1}{x}$
(D) $x$
19. The Integrating Factor of the differential equation $\left(1-y^{2}\right) \frac{d x}{d y}+y x=a y(-1<y<1)$ is
(A) $\frac{1}{y^{2}-1}$
(B) $\frac{1}{\sqrt{y^{2}-1}}$
(C) $\frac{1}{1-y^{2}}$
(D) $\frac{1}{\sqrt{1-y^{2}}}$

## Miscellaneous Examples

Example 19 Verify that the function $y=c_{1} e^{a x} \cos b x+c_{2} e^{a x} \sin b x$, where $c_{1}, c_{2}$ are arbitrary constants is a solution of the differential equation

$$
\frac{d^{2} y}{d x^{2}}-2 a \frac{d y}{d x}+\left(a^{2}+b^{2}\right) y=0
$$

Solution The given function is

$$
\begin{equation*}
y=e^{a x}\left[c_{1} \cos b x+c_{2} \sin b x\right] \tag{1}
\end{equation*}
$$

Differentiating both sides of equation (1) with respect to $x$, we get
or

$$
\begin{align*}
& \frac{d y}{d x}=e^{a x}\left[-b c_{1} \sin b x+b c_{2} \cos b x\right]+\left[c_{1} \cos b x+c_{2} \sin b x\right] e^{a x} \cdot a \\
& \frac{d y}{d x}=e^{a x}\left[\left(b c_{2}+a c_{1}\right) \cos b x+\left(a c_{2}-b c_{1}\right) \sin b x\right] \tag{2}
\end{align*}
$$

Differentiating both sides of equation (2) with respect to $x$, we get

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}}= & e^{a x}\left[\left(b c_{2}+a c_{1}\right)(-b \sin b x)+\left(a c_{2}-b c_{1}\right)(b \cos b x)\right] \\
& +\left[\left(b c_{2}+a c_{1}\right) \cos b x+\left(a c_{2}-b c_{1}\right) \sin b x\right] e^{a x} \cdot a \\
= & e^{a x}\left[\left(a^{2} c_{2}-2 a b c_{1}-b^{2} c_{2}\right) \sin b x+\left(a^{2} c_{1}+2 a b c_{2}-b^{2} c_{1}\right) \cos b x\right]
\end{aligned}
$$

Substituting the values of $\frac{d^{2} y}{d x^{2}}, \frac{d y}{d x}$ and $y$ in the given differential equation, we get

$$
\begin{aligned}
\text { L.H.S. }= & \left.e^{a x}\left[a^{2} c_{2}-2 a b c_{1}-b^{2} c_{2}\right) \sin b x+\left(a^{2} c_{1}+2 a b c_{2}-b^{2} c_{1}\right) \cos b x\right] \\
& -2 a e^{a x}\left[\left(b c_{2}+a c_{1}\right) \cos b x+\left(a c_{2}-b c_{1}\right) \sin b x\right] \\
& +\left(a^{2}+b^{2}\right) e^{a x}\left[c_{1} \cos b x+c_{2} \sin b x\right] \\
= & e^{a x}\left[\begin{array}{l}
\left(a^{2} c_{2}-2 a b c_{1}-b^{2} c_{2}-2 a^{2} c_{2}+2 a b c_{1}+a^{2} c_{2}+b^{2} c_{2}\right) \sin b x \\
+\left(a^{2} c_{1}+2 a b c_{2}-b^{2} c_{1}-2 a b c_{2}-2 a^{2} c_{1}+a^{2} c_{1}+b^{2} c_{1}\right) \cos b x
\end{array}\right] \\
= & e^{a x}[0 \times \sin b x+0 \cos b x]=e^{a x} \times 0=0=\text { R.H.S }
\end{aligned}
$$

Hence, the given function is a solution of the given differential equation.
Example 20 Find the particular solution of the differential equation $\log \left(\frac{d y}{d x}\right)=3 x+4 y$ given that $y=0$ when $x=0$.

Solution The given differential equation can be written as

$$
\frac{d y}{d x}=e^{(3 x+4 y)}
$$

or

$$
\begin{equation*}
\frac{d y}{d x}=e^{3 x} \cdot e^{4 y} \tag{1}
\end{equation*}
$$

Separating the variables, we get

$$
\frac{d y}{e^{4 y}}=e^{3 x} d x
$$

Therefore

$$
\int e^{-4 y} d y=\int e^{3 x} d x
$$

or

$$
\frac{e^{-4 y}}{-4}=\frac{e^{3 x}}{3}+\mathrm{C}
$$

or

$$
\begin{equation*}
4 e^{3 x}+3 e^{-4 y}+12 \mathrm{C}=0 \tag{2}
\end{equation*}
$$

Substituting $x=0$ and $y=0$ in (2), we get

$$
4+3+12 C=0 \text { or } C=\frac{-7}{12}
$$

Substituting the value of C in equation (2), we get

$$
4 e^{3 x}+3 e^{-4 y}-7=0
$$

which is a particular solution of the given differential equation.
Example 21 Solve the differential equation

$$
(x d y-y d x) y \sin \left(\frac{y}{x}\right)=(y d x+x d y) x \cos \left(\frac{y}{x}\right)
$$

Solution The given differential equation can be written as
or

$$
\begin{aligned}
& {\left[x y \sin \left(\frac{y}{x}\right)-x^{2} \cos \left(\frac{y}{x}\right)\right] d y=\left[x y \cos \left(\frac{y}{x}\right)+y^{2} \sin \left(\frac{y}{x}\right)\right] d x} \\
& \frac{d y}{d x}=\frac{x y \cos \left(\frac{y}{x}\right)+y^{2} \sin \left(\frac{y}{x}\right)}{x y \sin \left(\frac{y}{x}\right)-x^{2} \cos \left(\frac{y}{x}\right)}
\end{aligned}
$$

Dividing numerator and denominator on RHS by $x^{2}$, we get

$$
\begin{equation*}
\frac{d y}{d x}=\frac{\frac{y}{x} \cos \left(\frac{y}{x}\right)+\left(\frac{y^{2}}{x^{2}}\right) \sin \left(\frac{y}{x}\right)}{\frac{y}{x} \sin \left(\frac{y}{x}\right)-\cos \left(\frac{y}{x}\right)} \tag{1}
\end{equation*}
$$

Clearly, equation (1) is a homogeneous differential equation of the form $\frac{d y}{d x}=g\left(\frac{y}{x}\right)$.
To solve it, we make the substitution

$$
\begin{align*}
y & =v x  \tag{2}\\
\frac{d y}{d x} & =v+x \frac{d v}{d x}
\end{align*}
$$

or
or

$$
v+x \frac{d v}{d x}=\frac{v \cos v+v^{2} \sin v}{v \sin v-\cos v}
$$

(using (1) and (2))
or

$$
x \frac{d v}{d x}=\frac{2 v \cos v}{v \sin v-\cos v}
$$

or

$$
\left(\frac{v \sin v-\cos v}{v \cos v}\right) d v=\frac{2 d x}{x}
$$

Therefore

$$
\int\left(\frac{v \sin v-\cos v}{v \cos v}\right) d v=2 \int \frac{1}{x} d x
$$

or

$$
\int \tan v d v-\int \frac{1}{v} d v=2 \int \frac{1}{x} d x
$$

or

$$
\log |\sec v|-\log |v|=2 \log |x|+\log \left|\mathrm{C}_{1}\right|
$$

or

$$
\log \left|\frac{\sec v}{v x^{2}}\right|=\log \left|\mathrm{C}_{1}\right|
$$

or

$$
\begin{equation*}
\frac{\sec v}{v x^{2}}= \pm \mathrm{C}_{1} \tag{3}
\end{equation*}
$$

Replacing $v$ by $\frac{y}{x}$ in equation (3), we get
or

$$
\begin{aligned}
& \frac{\sec \left(\frac{y}{x}\right)}{\left(\frac{y}{x}\right)\left(x^{2}\right)}=\mathrm{C} \text { where, } \mathrm{C}= \pm \mathrm{C}_{1} \\
& \sec \left(\frac{y}{x}\right)=\mathrm{C} x y
\end{aligned}
$$

which is the general solution of the given differential equation.

Example 22 Solve the differential equation

$$
\left(\tan ^{-1} y-x\right) d y=\left(1+y^{2}\right) d x
$$

Solution The given differential equation can be written as

$$
\begin{equation*}
\frac{d x}{d y}+\frac{x}{1+y^{2}}=\frac{\tan ^{-1} y}{1+y^{2}} \tag{1}
\end{equation*}
$$

Now (1) is a linear differential equation of the form $\frac{d x}{d y}+\mathrm{P}_{1} x=\mathrm{Q}_{1}$,
where, $\quad \mathrm{P}_{1}=\frac{1}{1+y^{2}}$ and $\mathrm{Q}_{1}=\frac{\tan ^{-1} y}{1+y^{2}}$.
Therefore, I. F $=e^{\int \frac{1}{1+y^{2}} d y}=e^{\tan ^{-1} y}$
Thus, the solution of the given differential equation is

$$
\begin{equation*}
x e^{\tan ^{-1} y}=\int\left(\frac{\tan ^{-1} y}{1+y^{2}}\right) e^{\tan ^{-1} y} d y+\mathrm{C} \tag{2}
\end{equation*}
$$

Let

$$
\mathrm{I}=\int\left(\frac{\tan ^{-1} y}{1+y^{2}}\right) e^{\tan ^{-1} y} d y
$$

Substituting $\tan ^{-1} y=t$ so that $\left(\frac{1}{1+y^{2}}\right) d y=d t$, we get
or

$$
\begin{aligned}
& \mathrm{I}=\int t e^{t} d t=t e^{t}-\int 1 \cdot e^{t} d t=t e^{t}-e^{t}=e^{t}(t-1) \\
& \mathrm{I}=e^{\tan ^{-1} y}\left(\tan ^{-1} y-1\right)
\end{aligned}
$$

Substituting the value of I in equation (2), we get
or

$$
\begin{aligned}
& x \cdot e^{\tan ^{-1} y}=e^{\tan ^{-1} y}\left(\tan ^{-1} y-1\right)+\mathrm{C} \\
x= & \left(\tan ^{-1} y-1\right)+\mathrm{C} e^{-\tan ^{-1} y}
\end{aligned}
$$

which is the general solution of the given differential equation.

## Miscellaneous Exercise on Chapter 9

1. For each of the differential equations given below, indicate its order and degree (if defined).
(i) $\frac{d^{2} y}{d x^{2}}+5 x\left(\frac{d y}{d x}\right)^{2}-6 y=\log x$
(ii) $\left(\frac{d y}{d x}\right)^{3}-4\left(\frac{d y}{d x}\right)^{2}+7 y=\sin x$
(iii) $\frac{d^{4} y}{d x^{4}}-\sin \left(\frac{d^{3} y}{d x^{3}}\right)=0$
2. For each of the exercises given below, verify that the given function (implicit or explicit) is a solution of the corresponding differential equation.
(i) $x y=a e^{x}+b e^{-x}+x^{2} \quad: x \frac{d^{2} y}{d x^{2}}+2 \frac{d y}{d x}-x y+x^{2}-2=0$
(ii) $y=e^{x}(a \cos x+b \sin x) \quad: \frac{d^{2} y}{d x^{2}}-2 \frac{d y}{d x}+2 y=0$
(iii) $y=x \sin 3 x$ $: \frac{d^{2} y}{d x^{2}}+9 y-6 \cos 3 x=0$
(iv) $x^{2}=2 y^{2} \log y$ $:\left(x^{2}+y^{2}\right) \frac{d y}{d x}-x y=0$
3. Prove that $x^{2}-y^{2}=c\left(x^{2}+y^{2}\right)^{2}$ is the general solution of differential equation $\left(x^{3}-3 x y^{2}\right) d x=\left(y^{3}-3 x^{2} y\right) d y$, where $c$ is a parameter.
4. Find the general solution of the differential equation $\frac{d y}{d x}+\sqrt{\frac{1-y^{2}}{1-x^{2}}}=0$.
5. Show that the general solution of the differential equation $\frac{d y}{d x}+\frac{y^{2}+y+1}{x^{2}+x+1}=0$ is given by $(x+y+1)=\mathrm{A}(1-x-y-2 x y)$, where A is parameter.
6. Find the equation of the curve passing through the point $\left(0, \frac{\pi}{4}\right)$ whose differential equation is $\sin x \cos y d x+\cos x \sin y d y=0$.
7. Find the particular solution of the differential equation $\left(1+e^{2 x}\right) d y+\left(1+y^{2}\right) e^{x} d x=0$, given that $y=1$ when $x=0$.
8. Solve the differential equation $y e^{\frac{x}{y}} d x=\left(x e^{\frac{x}{y}}+y^{2}\right) d y(y \neq 0)$.
9. Find a particular solution of the differential equation $(x-y)(d x+d y)=d x-d y$, given that $y=-1$, when $x=0$. (Hint: put $x-y=t$ )
10. Solve the differential equation $\left[\frac{e^{-2 \sqrt{x}}}{\sqrt{x}}-\frac{y}{\sqrt{x}}\right] \frac{d x}{d y}=1(x \neq 0)$.
11. Find a particular solution of the differential equation $\frac{d y}{d x}+y \cot x=4 x \operatorname{cosec} x$ $(x \neq 0)$, given that $y=0$ when $x=\frac{\pi}{2}$.
12. Find a particular solution of the differential equation $(x+1) \frac{d y}{d x}=2 e^{-y}-1$, given that $y=0$ when $x=0$.
13. The general solution of the differential equation $\frac{y d x-x d y}{y}=0$ is
(A) $x y=\mathrm{C}$
(B) $x=\mathrm{C} y^{2}$
(C) $y=\mathrm{C} x$
(D) $y=\mathrm{C} x^{2}$
14. The general solution of a differential equation of the type $\frac{d x}{d y}+\mathrm{P}_{1} x=\mathrm{Q}_{1}$ is
(A) $y e^{\int \mathrm{P}_{1} d y}=\int\left(\mathrm{Q}_{1} e^{\int \mathrm{P}_{1} d y}\right) d y+\mathrm{C}$
(B) $y \cdot e^{\int \mathrm{P}_{1} d x}=\int\left(\mathrm{Q}_{1} e^{\int \mathrm{P}_{1} d x}\right) d x+\mathrm{C}$
(C) $x e^{\int \mathrm{P}_{1} d y}=\int\left(\mathrm{Q}_{1} e^{\int \mathrm{P}_{1} d y}\right) d y+\mathrm{C}$
(D) $x e^{\int \mathrm{P}_{1} d x}=\int\left(\mathrm{Q}_{1} e^{\int \mathrm{P}_{1} d x}\right) d x+\mathrm{C}$
15. The general solution of the differential equation $e^{x} d y+\left(y e^{x}+2 x\right) d x=0$ is
(A) $x e^{y}+x^{2}=\mathrm{C}$
(B) $x e^{y}+y^{2}=\mathrm{C}$
(C) $y e^{x}+x^{2}=\mathrm{C}$
(D) $y e^{y}+x^{2}=\mathrm{C}$

## Summary

- An equation involving derivatives of the dependent variable with respect to independent variable (variables) is known as a differential equation.
- Order of a differential equation is the order of the highest order derivative occurring in the differential equation.
- Degree of a differential equation is defined if it is a polynomial equation in its derivatives.
- Degree (when defined) of a differential equation is the highest power (positive integer only) of the highest order derivative in it.
- A function which satisfies the given differential equation is called its solution. The solution which contains as many arbitrary constants as the order of the differential equation is called a general solution and the solution free from arbitrary constants is called particular solution.
- Variable separable method is used to solve such an equation in which variables can be separated completely i.e. terms containing $y$ should remain with $d y$ and terms containing $x$ should remain with $d x$.
- A differential equation which can be expressed in the form $\frac{d y}{d x}=f(x, y)$ or $\frac{d x}{d y}=g(x, y)$ where, $f(x, y)$ and $g(x, y)$ are homogenous functions of degree zero is called a homogeneous differential equation.
- A differential equation of the form $\frac{d y}{d x}+\mathrm{P} y=\mathrm{Q}$, where P and Q are constants or functions of $x$ only is called a first order linear differential equation.


## Historical Note

One of the principal languages of Science is that of differential equations. Interestingly, the date of birth of differential equations is taken to be November, 11,1675, when Gottfried Wilthelm Freiherr Leibnitz (1646-1716) first put in black and white the identity $\int y d y=\frac{1}{2} y^{2}$, thereby introducing both the symbols $\int$ and $d y$. Leibnitz was actually interested in the problem of finding a curve whose tangents were prescribed. This led him to discover the 'method of separation of variables' 1691. A year later he formulated the 'method of solving the homogeneous
differential equations of the first order'. He went further in a very short time to the discovery of the 'method of solving a linear differential equation of the first-order'. How surprising is it that all these methods came from a single man and that too within 25 years of the birth of differential equations!

In the old days, what we now call the 'solution' of a differential equation, was used to be referred to as 'integral' of the differential equation, the word being coined by James Bernoulli (1654-1705) in 1690. The word 'solution was first used by Joseph Louis Lagrange (1736-1813) in 1774, which was almost hundred years since the birth of differential equations. It was Jules Henri Poincare (1854-1912) who strongly advocated the use of the word 'solution' and thus the word 'solution' has found its deserved place in modern terminology. The name of the 'method of separation of variables' is due to John Bernoulli (1667-1748), a younger brother of James Bernoulli.

Application to geometric problems were also considered. It was again John Bernoulli who first brought into light the intricate nature of differential equations. In a letter to Leibnitz, dated May 20, 1715, he revealed the solutions of the differential equation

$$
x^{2} y^{\prime \prime}=2 y,
$$

which led to three types of curves, viz., parabolas, hyperbolas and a class of cubic curves. This shows how varied the solutions of such innocent looking differential equation can be. From the second half of the twentieth century attention has been drawn to the investigation of this complicated nature of the solutions of differential equations, under the heading 'qualitative analysis of differential equations'. Now-a-days, this has acquired prime importance being absolutely necessary in almost all investigations.


[^0]:    * The notation $\frac{d y}{d x}$ due to Leibnitz is extremely flexible and useful in many calculation and formal transformations, where, we can deal with symbols $d y$ and $d x$ exactly as if they were ordinary numbers. By treating $d x$ and $d y$ like separate entities, we can give neater expressions to many calculations.
    Refer: Introduction to Calculus and Analysis, volume-I page 172, By Richard Courant, Fritz John Spinger - Verlog New York.

