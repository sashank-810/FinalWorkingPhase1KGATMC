Chapter

## APPLICATION OF DERIVATIVES

With the Calculus as a key, Mathematics can be successfully applied to the explanation of the course of Nature." - WHITEHEAD

### 6.1 Introduction

In Chapter 5, we have learnt how to find derivative of composite functions, inverse trigonometric functions, implicit functions, exponential functions and logarithmic functions. In this chapter, we will study applications of the derivative in various disciplines, e.g., in engineering, science, social science, and many other fields. For instance, we will learn how the derivative can be used (i) to determine rate of change of quantities, (ii) to find the equations of tangent and normal to a curve at a point, (iii) to find turning points on the graph of a function which in turn will help us to locate points at which largest or smallest value (locally) of a function occurs. We will also use derivative to find intervals on which a function is increasing or decreasing. Finally, we use the derivative to find approximate value of certain quantities.

### 6.2 Rate of Change of Quantities

Recall that by the derivative $\frac{d s}{d t}$, we mean the rate of change of distance $s$ with respect to the time $t$. In a similar fashion, whenever one quantity $y$ varies with another quantity $x$, satisfying some rule $y=f(x)$, then $\frac{d y}{d x}$ (or $f^{\prime}(x)$ ) represents the rate of change of $y$ with respect to $x$ and $\frac{d y}{d x}{ }_{x=x_{0}}$ (or $f^{\prime}\left(x_{0}\right)$ ) represents the rate of change of $y$ with respect to $x$ at $x=x_{0}$.

Further, if two variables $x$ and $y$ are varying with respect to another variable $t$, i.e., if $x=f(t)$ and $y=g(t)$, then by Chain Rule

$$
\frac{d y}{d x}=\frac{d y}{d t} / \frac{d x}{d t}, \text { if } \frac{d x}{d t} \neq 0
$$

Thus, the rate of change of $y$ with respect to $x$ can be calculated using the rate of change of $y$ and that of $x$ both with respect to $t$.

Let us consider some examples.
Example 1 Find the rate of change of the area of a circle per second with respect to its radius $r$ when $r=5 \mathrm{~cm}$.

Solution The area A of a circle with radius $r$ is given by $\mathrm{A}=\pi r^{2}$. Therefore, the rate of change of the area A with respect to its radius $r$ is given by $\frac{d \mathrm{~A}}{d r}=\frac{d}{d r}\left(\pi r^{2}\right)=2 \pi r$.

When $r=5 \mathrm{~cm}, \frac{d \mathrm{~A}}{d r}=10 \pi$. Thus, the area of the circle is changing at the rate of $10 \pi \mathrm{~cm}^{2} / \mathrm{s}$.

Example 2 The volume of a cube is increasing at a rate of 9 cubic centimetres per second. How fast is the surface area increasing when the length of an edge is 10 centimetres ?

Solution Let $x$ be the length of a side, V be the volume and S be the surface area of the cube. Then, $\mathrm{V}=x^{3}$ and $\mathrm{S}=6 x^{2}$, where $x$ is a function of time $t$.

Now

$$
\frac{d \mathrm{~V}}{d t}=9 \mathrm{~cm}^{3} / \mathrm{s} \text { (Given) }
$$

Therefore

$$
\begin{aligned}
9 & =\frac{d \mathrm{~V}}{d t}=\frac{d}{d t}\left(x^{3}\right)=\frac{d}{d x}\left(x^{3}\right) \cdot \frac{d x}{d t} \quad \text { (By Chain Rule) } \\
& =3 x^{2} \cdot \frac{d x}{d t}
\end{aligned}
$$

or

$$
\begin{equation*}
\frac{d x}{d t}=\frac{3}{x^{2}} \tag{1}
\end{equation*}
$$

Now

$$
\begin{array}{rlr}
\frac{d S}{d t} & =\frac{d}{d t}\left(6 x^{2}\right)=\frac{d}{d x}\left(6 x^{2}\right) \cdot \frac{d x}{d t} & \text { (By Chain Rule) } \\
& =12 x \cdot\left(\frac{3}{x^{2}}\right)=\frac{36}{x} & \text { (Using (1)) } \tag{1}
\end{array}
$$

Hence, when $\quad x=10 \mathrm{~cm}, \frac{d S}{d t}=3.6 \mathrm{~cm}^{2} / \mathrm{s}$

Example 3 A stone is dropped into a quiet lake and waves move in circles at a speed of 4 cm per second. At the instant, when the radius of the circular wave is 10 cm , how fast is the enclosed area increasing?

Solution The area A of a circle with radius $r$ is given by $\mathrm{A}=\pi r^{2}$. Therefore, the rate of change of area A with respect to time $t$ is

$$
\frac{d \mathrm{~A}}{d t}=\frac{d}{d t}\left(\pi r^{2}\right)=\frac{d}{d r}\left(\pi r^{2}\right) \cdot \frac{d r}{d t}=2 \pi r \frac{d r}{d t}
$$

(By Chain Rule)

It is given that

$$
\frac{d r}{d t}=4 \mathrm{~cm} / \mathrm{s}
$$

Therefore, when $r=10 \mathrm{~cm}, \quad \frac{d \mathrm{~A}}{d t}=2 \pi(10)(4)=80 \pi$
Thus, the enclosed area is increasing at the rate of $80 \pi \mathrm{~cm}^{2} / \mathrm{s}$, when $r=10 \mathrm{~cm}$.
$\square$ Note $\frac{d y}{d x}$ is positive if $y$ increases as $x$ increases and is negative if $y$ decreases as $x$ increases.

Example 4 The length $x$ of a rectangle is decreasing at the rate of $3 \mathrm{~cm} /$ minute and the width $y$ is increasing at the rate of $2 \mathrm{~cm} /$ minute. When $x=10 \mathrm{~cm}$ and $y=6 \mathrm{~cm}$, find the rates of change of (a) the perimeter and (b) the area of the rectangle.

Solution Since the length $x$ is decreasing and the width $y$ is increasing with respect to time, we have

$$
\frac{d x}{d t}=-3 \mathrm{~cm} / \mathrm{min} \quad \text { and } \quad \frac{d y}{d t}=2 \mathrm{~cm} / \mathrm{min}
$$

(a) The perimeter P of a rectangle is given by

Therefore

$$
\begin{aligned}
& \text { angle is given by } \\
& \qquad \begin{aligned}
\mathrm{P} & =2(x+y) \\
\frac{d \mathrm{P}}{d t} & =2 \frac{d x}{d t}+\frac{d y}{d t}=2(-3+2)=-2 \mathrm{~cm} / \mathrm{min}
\end{aligned}
\end{aligned}
$$

(b) The area A of the rectangle is given by

$$
\mathrm{A}=x \cdot y
$$

Therefore

$$
\begin{aligned}
\frac{d \mathrm{~A}}{d t} & =\frac{d x}{d t} \cdot y+x \cdot \frac{d y}{d t} \\
& =-3(6)+10(2) \quad(\text { as } x=10 \mathrm{~cm} \text { and } y=6 \mathrm{~cm}) \\
& =2 \mathrm{~cm}^{2} / \mathrm{min}
\end{aligned}
$$

Example 5 The total cost $\mathrm{C}(x)$ in Rupees, associated with the production of $x$ units of an item is given by

$$
\mathrm{C}(x)=0.005 x^{3}-0.02 x^{2}+30 x+5000
$$

Find the marginal cost when 3 units are produced, where by marginal cost we mean the instantaneous rate of change of total cost at any level of output.

Solution Since marginal cost is the rate of change of total cost with respect to the output, we have

Marginal

$$
\operatorname{cost}(\mathrm{MC})=\frac{d C}{d x}=0.005\left(3 x^{2}\right)-0.02(2 x)+30
$$

When

$$
\begin{aligned}
x=3, \mathrm{MC} & =0.015\left(3^{2}\right)-0.04(3)+30 \\
& =0.135-0.12+30=30.015
\end{aligned}
$$

Hence, the required marginal cost is ₹ 30.02 (nearly).
Example 6 The total revenue in Rupees received from the sale of $x$ units of a product is given by $\mathrm{R}(x)=3 x^{2}+36 x+5$. Find the marginal revenue, when $x=5$, where by marginal revenue we mean the rate of change of total revenue with respect to the number of items sold at an instant.

Solution Since marginal revenue is the rate of change of total revenue with respect to the number of units sold, we have

Marginal Revenue

$$
\begin{aligned}
(\mathrm{MR}) & =\frac{d \mathrm{R}}{d x}=6 x+36 \\
x & =5, \mathrm{MR}=6(5)+36=66
\end{aligned}
$$

When
Hence, the required marginal revenue is ₹ 66 .

## EXERCISE 6.1

1. Find the rate of change of the area of a circle with respect to its radius $r$ when
(a) $r=3 \mathrm{~cm}$
(b) $r=4 \mathrm{~cm}$
2. The volume of a cube is increasing at the rate of $8 \mathrm{~cm}^{3} / \mathrm{s}$. How fast is the surface area increasing when the length of an edge is 12 cm ?
3. The radius of a circle is increasing uniformly at the rate of $3 \mathrm{~cm} / \mathrm{s}$. Find the rate at which the area of the circle is increasing when the radius is 10 cm .
4. An edge of a variable cube is increasing at the rate of $3 \mathrm{~cm} / \mathrm{s}$. How fast is the volume of the cube increasing when the edge is 10 cm long?
5. A stone is dropped into a quiet lake and waves move in circles at the speed of $5 \mathrm{~cm} / \mathrm{s}$. At the instant when the radius of the circular wave is 8 cm , how fast is the enclosed area increasing?
6. The radius of a circle is increasing at the rate of $0.7 \mathrm{~cm} / \mathrm{s}$. What is the rate of increase of its circumference?
7. The length $x$ of a rectangle is decreasing at the rate of $5 \mathrm{~cm} /$ minute and the width $y$ is increasing at the rate of $4 \mathrm{~cm} /$ minute. When $x=8 \mathrm{~cm}$ and $y=6 \mathrm{~cm}$, find the rates of change of (a) the perimeter, and (b) the area of the rectangle.
8. A balloon, which always remains spherical on inflation, is being inflated by pumping in 900 cubic centimetres of gas per second. Find the rate at which the radius of the balloon increases when the radius is 15 cm .
9. A balloon, which always remains spherical has a variable radius. Find the rate at which its volume is increasing with the radius when the later is 10 cm .
10. A ladder 5 m long is leaning against a wall. The bottom of the ladder is pulled along the ground, away from the wall, at the rate of $2 \mathrm{~cm} / \mathrm{s}$. How fast is its height on the wall decreasing when the foot of the ladder is 4 m away from the wall ?
11. A particle moves along the curve $6 y=x^{3}+2$. Find the points on the curve at which the $y$-coordinate is changing 8 times as fast as the $x$-coordinate.
12. The radius of an air bubble is increasing at the rate of $\frac{1}{2} \mathrm{~cm} / \mathrm{s}$. At what rate is the volume of the bubble increasing when the radius is 1 cm ?
13. A balloon, which always remains spherical, has a variable diameter $\frac{3}{2}(2 x+1)$. Find the rate of change of its volume with respect to $x$.
14. Sand is pouring from a pipe at the rate of $12 \mathrm{~cm}^{3} / \mathrm{s}$. The falling sand forms a cone on the ground in such a way that the height of the cone is always one-sixth of the radius of the base. How fast is the height of the sand cone increasing when the height is 4 cm ?
15. The total cost $\mathrm{C}(x)$ in Rupees associated with the production of $x$ units of an item is given by

$$
\mathrm{C}(x)=0.007 x^{3}-0.003 x^{2}+15 x+4000
$$

Find the marginal cost when 17 units are produced.
16. The total revenue in Rupees received from the sale of $x$ units of a product is given by

$$
\mathrm{R}(x)=13 x^{2}+26 x+15
$$

Find the marginal revenue when $x=7$.
Choose the correct answer for questions 17 and 18 .
17. The rate of change of the area of a circle with respect to its radius $r$ at $r=6 \mathrm{~cm}$ is
(A) $10 \pi$
(B) $12 \pi$
(C) $8 \pi$
(D) $11 \pi$
18. The total revenue in Rupees received from the sale of $x$ units of a product is given by
$\mathrm{R}(x)=3 x^{2}+36 x+5$. The marginal revenue, when $x=15$ is
(A) 116
(B) 96
(C) 90
(D) 126

### 6.3 Increasing and Decreasing Functions

In this section, we will use differentiation to find out whether a function is increasing or decreasing or none.

Consider the function $f$ given by $f(x)=x^{2}, x \in \mathbf{R}$. The graph of this function is a parabola as given in Fig 6.1.

Values left to origin

| $x$ | $f(x)=x^{2}$ |
| :---: | :---: |
| -2 | 4 |
| $-\frac{3}{2}$ | $\frac{9}{4}$ |
| -1 | 1 |
| $-\frac{1}{2}$ | $\frac{1}{4}$ |
| 0 | 0 |

as we move from left to right, the height of the graph decreases
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-06.jpg?height=479&width=852&top_left_y=853&top_left_x=553)
as we move from left to right, the height of the graph increases

Values right to origin
ig 6.1

First consider the graph (Fig 6.1) to the right of the origin. Observe that as we move from left to right along the graph, the height of the graph continuously increases. For this reason, the function is said to be increasing for the real numbers $x>0$.

Now consider the graph to the left of the origin and observe here that as we move from left to right along the graph, the height of the graph continuously decreases. Consequently, the function is said to be decreasing for the real numbers $x<0$.

We shall now give the following analytical definitions for a function which is increasing or decreasing on an interval.

Definition 1 Let I be an interval contained in the domain of a real valued function $f$. Then $f$ is said to be
(i) increasing on I if $x_{1}<x_{2}$ in $\mathrm{I} \Rightarrow f\left(x_{1}\right) \leq f\left(x_{2}\right)$ for all $x_{1}, x_{2} \in \mathrm{I}$.
(ii) decreasing on I, if $x_{1}<x_{2}$ in $\mathrm{I} \Rightarrow f\left(x_{1}\right) \geq f\left(x_{2}\right)$ for all $x_{1}, x_{2} \in \mathrm{I}$.
(iii) constant on I, if $f(x)=c$ for all $x \in \mathrm{I}$, where $c$ is a constant.
(iv) strictly increasing on I if $x_{1}<x_{2}$ in $\mathrm{I} \Rightarrow f\left(x_{1}\right)<f\left(x_{2}\right)$ for all $x_{1}, x_{2} \in \mathrm{I}$.
(v) strictly decreasing on I if $x_{1}<x_{2}$ in $\mathrm{I} \Rightarrow f\left(x_{1}\right)>f\left(x_{2}\right)$ for all $x_{1}, x_{2} \in \mathrm{I}$.

For graphical representation of such functions see Fig 6.2.
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-07.jpg?height=495&width=1263&top_left_y=523&top_left_x=208)

Fig 6.2
We shall now define when a function is increasing or decreasing at a point.
Definition 2 Let $x_{0}$ be a point in the domain of definition of a real valued function $f$. Then $f$ is said to be increasing, decreasing at $x_{0}$ if there exists an open interval I containing $x_{0}$ such that $f$ is increasing, decreasing, respectively, in I.

Let us clarify this definition for the case of increasing function.
Example 7 Show that the function given by $f(x)=7 x-3$ is increasing on $\mathbf{R}$.
Solution Let $x_{1}$ and $x_{2}$ be any two numbers in $\mathbf{R}$. Then

$$
x_{1}<x_{2} \Rightarrow 7 x_{1}<7 x_{2} \Rightarrow 7 x_{1}-3<7 x_{2}-3 \Rightarrow f\left(x_{1}\right)<f\left(x_{2}\right)
$$

Thus, by Definition 1, it follows that $f$ is strictly increasing on $\mathbf{R}$.
We shall now give the first derivative test for increasing and decreasing functions. The proof of this test requires the Mean Value Theorem studied in Chapter 5.

Theorem 1 Let $f$ be continuous on $[a, b]$ and differentiable on the open interval ( $a, b$ ). Then
(a) $f$ is increasing in $[a, b]$ if $f^{\prime}(x) \geq 0$ for each $x \in(a, b)$
(b) $f$ is decreasing in $[a, b]$ if $f^{\prime}(x) \leq 0$ for each $x \in(a, b)$
(c) $f$ is a constant function in $[a, b]$ if $f^{\prime}(x)=0$ for each $x \in(a, b)$

Proof (a) Let $x_{1}, x_{2} \in[a, b]$ be such that $x_{1}<x_{2}$.
Then, by Mean Value Theorem (Theorem 8 in Chapter 5), there exists a point $c$ between $x_{1}$ and $x_{2}$ such that
i.e.

$$
f\left(x_{2}\right)-f\left(x_{1}\right)=f^{\prime}(c)\left(x_{2}-x_{1}\right)
$$

## i.e.

$$
f\left(x_{2}\right)-f\left(x_{1}\right)>0 \quad\left(\text { as } f^{\prime}(c)>0(\text { given })\right)
$$

$$
f\left(x_{2}\right)>f\left(x_{1}\right)
$$

Thus, we have

$$
x_{1}<x_{2} \Rightarrow f\left(x_{1}\right)<f\left(x_{2}\right), \text { for all } x_{1}, x_{2} \in[a, b]
$$

Hence, $f$ is an increasing function in $[a, b]$.
The proofs of part (b) and (c) are similar. It is left as an exercise to the reader.

## Remarks

There is a more generalised theorem, which states that if $f(x)>0$ for $x$ in an interval excluding the end points and $f$ is continuous in the interval, then $f$ is increasing. Similarly, if $f(x)<0$ for $x$ in an interval excluding the end points and $f$ is continuous in the interval, then $f$ is decreasing.

Example 8 Show that the function $f$ given by

$$
f(x)=x^{3}-3 x^{2}+4 x, x \in \mathbf{R}
$$

is increasing on $\mathbf{R}$.
Solution Note that

$$
\begin{aligned}
f^{\prime}(x) & =3 x^{2}-6 x+4 \\
& =3\left(x^{2}-2 x+1\right)+1 \\
& =3(x-1)^{2}+1>0, \text { in every interval of } \mathbf{R}
\end{aligned}
$$

Therefore, the function $f$ is increasing on $\mathbf{R}$.
Example 9 Prove that the function given by $f(x)=\cos x$ is
(a) decreasing in $(0, \pi)$
(b) increasing in ( $\pi, 2 \pi$ ), and
(c) neither increasing nor decreasing in ( $0,2 \pi$ ).

Solution Note that $f^{\prime}(x)=-\sin x$
(a) Since for each $x \in(0, \pi)$, $\sin x>0$, we have $f^{\prime}(x)<0$ and so $f$ is decreasing in $(0, \pi)$.
(b) Since for each $x \in(\pi, 2 \pi), \sin x<0$, we have $f^{\prime}(x)>0$ and so $f$ is increasing in $(\pi, 2 \pi)$.
(c) Clearly by (a) and (b) above, $f$ is neither increasing nor decreasing in ( $0,2 \pi$ ).

Example 10 Find the intervals in which the function $f$ given by $f(x)=x^{2}-4 x+6$ is
(a) increasing
(b) decreasing

Solution We have
or

$$
\begin{aligned}
& f(x)=x^{2}-4 x+6 \\
& f^{\prime}(x)=2 x-4
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-09.jpg?height=73&width=615&top_left_y=877&top_left_x=843)

Fig 6.3

Therefore, $f^{\prime}(x)=0$ gives $x=2$. Now the point $x=2$ divides the real line into two disjoint intervals namely, ( $-\infty, 2$ ) and ( $2, \infty$ ) (Fig 6.3). In the interval ( $-\infty, 2$ ), $f^{\prime}(x)=2 x$ $-4<0$.

Therefore, $f$ is decreasing in this interval. Also, in the interval $(2, \infty), f^{\prime}(x)>0$ and so the function $f$ is increasing in this interval.

Example 11 Find the intervals in which the function $f$ given by $f(x)=4 x^{3}-6 x^{2}-72 x$ +30 is (a) increasing (b) decreasing.

Solution We have

$$
f(x)=4 x^{3}-6 x^{2}-72 x+30
$$

or

$$
\begin{aligned}
f^{\prime}(x) & =12 x^{2}-12 x-72 \\
& =12\left(x^{2}-x-6\right) \\
& =12(x-3)(x+2)
\end{aligned}
$$

Therefore, $f^{\prime}(x)=0$ gives $x=-2,3$. The points $x=-2$ and $x=3$ divides the real line into three disjoint intervals, namely, $(-\infty,-2),(-2,3)$
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-09.jpg?height=66&width=548&top_left_y=1848&top_left_x=911)

Fig 6.4 and $(3, \infty)$.

In the intervals $(-\infty,-2)$ and $(3, \infty), f^{\prime}(x)$ is positive while in the interval $(-2,3)$, $f^{\prime}(x)$ is negative. Consequently, the function $f$ is increasing in the intervals $(-\infty,-2)$ and $(3, \infty)$ while the function is decreasing in the interval $(-2,3)$. However, $f$ is neither increasing nor decreasing in $\mathbf{R}$.

| Interval | Sign of $f^{\prime}(x)$ | Nature of function $f$ |
| :---: | :---: | :---: |
| $(-\infty,-2)$ | $(-)(-)>0$ | $f$ is increasing |
| $(-2,3)$ | $(-)(+)<0$ | $f$ is decreasing |
| $(3, \infty)$ | $(+)(+)>0$ | $f$ is increasing |

Example 12 Find intervals in which the function given by $f(x)=\sin 3 x, x \in 0, \frac{\pi}{2}$ is (a) increasing (b) decreasing.

Solution We have
or

$$
\begin{aligned}
f(x) & =\sin 3 x \\
f^{\prime}(x) & =3 \cos 3 x
\end{aligned}
$$

Therefore, $f^{\prime}(x)=0$ gives $\cos 3 x=0$ which in turn gives $3 x=\frac{\pi}{2}, \frac{3 \pi}{2}$ (as $x \in 0, \frac{\pi}{2}$ implies $3 x \in\left[0, \frac{3 \pi}{2}\right]$ ). So $x=\frac{\pi}{6}$ and $\frac{\pi}{2}$. The point $x=\frac{\pi}{6}$ divides the interval $0, \frac{\pi}{2}$ into two disjoint intervals $\left[0, \frac{\pi}{6}\right)$ and $\frac{\pi}{6}, \frac{\pi}{2}$.
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-10.jpg?height=107&width=467&top_left_y=1454&top_left_x=991)

Fig 6.5

Now, $f^{\prime}(x)>0$ for all $x \in\left[0, \frac{\pi}{6}\right)$ as $0 \leq x<\frac{\pi}{6} \Rightarrow 0 \leq 3 x<\frac{\pi}{2}$ and $f^{\prime}(x)<0$ for all $x \in\left(\frac{\pi}{6}, \frac{\pi}{2}\right)$ as $\frac{\pi}{6}<x<\frac{\pi}{2} \Rightarrow \frac{\pi}{2}<3 x<\frac{3 \pi}{2}$.

Therefore, $f$ is increasing in $\left[0, \frac{\pi}{6}\right)$ and decreasing in $\left(\frac{\pi}{6}, \frac{\pi}{2}\right)$.

Also, the given function is continuous at $x=0$ and $x=\frac{\pi}{6}$. Therefore, by Theorem 1 , $f$ is increasing on $0, \frac{\pi}{6}$ and decreasing on $\frac{\pi}{6}, \frac{\pi}{2}$.

Example 13 Find the intervals in which the function $f$ given by

$$
f(x)=\sin x+\cos x, 0 \leq x \leq 2 \pi
$$

is increasing or decreasing.
Solution We have
or

$$
\begin{aligned}
f(x) & =\sin x+\cos x \\
f^{\prime}(x) & =\cos x-\sin x
\end{aligned}
$$

Now $f^{\prime}(x)=0$ gives $\sin x=\cos x$ which gives that $x=\frac{\pi}{4}, \frac{5 \pi}{4}$ as $0 \leq x \leq 2 \pi$
The points $x=\frac{\pi}{4}$ and $x=\frac{5 \pi}{4}$ divide the interval $[0,2 \pi]$ into three disjoint intervals, namely, $\left[0, \frac{\pi}{4}\right), \frac{\pi}{4}, \frac{5 \pi}{4}$ and $\left(\frac{5 \pi}{4}, 2 \pi\right]$.
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-11.jpg?height=108&width=532&top_left_y=1282&top_left_x=931)

Fig 6.6

Note that $\quad f^{\prime}(x)>0$ if $x \in\left[0, \frac{\pi}{4}\right) \cup\left(\frac{5 \pi}{4}, 2 \pi\right]$
or $\quad f$ is increasing in the intervals $\left[0, \frac{\pi}{4}\right)$ and $\left(\frac{5 \pi}{4}, 2 \pi\right]$

Also $\quad f^{\prime}(x)<0$ if $x \in \frac{\pi}{4}, \frac{5 \pi}{4}$
or $\quad f$ is decreasing in $\frac{\pi}{4}, \frac{5 \pi}{4}$

| Interval | Sign of $f^{\prime}(x)$ | Nature of function |
| :--- | :--- | :--- |
| $\left[0, \frac{\pi}{4}\right)$ | > 0 | $f$ is increasing |
| $\frac{\pi}{4}, \frac{5 \pi}{4}$ | < 0 | $f$ is decreasing |
| $\left(\frac{5 \pi}{4}, 2 \pi\right]$ | > 0 | $f$ is increasing |

## EXERCISE 6.2

1. Show that the function given by $f(x)=3 x+17$ is increasing on $\mathbf{R}$.
2. Show that the function given by $f(x)=e^{2 x}$ is increasing on $\mathbf{R}$.
3. Show that the function given by $f(x)=\sin x$ is
(a) increasing in $\left(0, \frac{\pi}{2}\right)$
(b) decreasing in $\left(\frac{\pi}{2}, \pi\right)$
(c) neither increasing nor decreasing in $(0, \pi)$
4. Find the intervals in which the function $f$ given by $f(x)=2 x^{2}-3 x$ is
(a) increasing
(b) decreasing
5. Find the intervals in which the function $f$ given by $f(x)=2 x^{3}-3 x^{2}-36 x+7$ is
(a) increasing
(b) decreasing
6. Find the intervals in which the following functions are strictly increasing or decreasing:
(a) $x^{2}+2 x-5$
(b) $10-6 x-2 x^{2}$
(c) $-2 x^{3}-9 x^{2}-12 x+1$
(d) $6-9 x-x^{2}$
(e) $(x+1)^{3}(x-3)^{3}$
7. Show that $y=\log (1+x)-\frac{2 x}{2+x}, x>-1$, is an increasing function of $x$ throughout its domain.
8. Find the values of $x$ for which $y=[x(x-2)]^{2}$ is an increasing function.
9. Prove that $y=\frac{4 \sin \theta}{(2+\cos \theta)}-\theta$ is an increasing function of $\theta$ in $0, \frac{\pi}{2}$.
10. Prove that the logarithmic function is increasing on $(0, \infty)$.
11. Prove that the function $f$ given by $f(x)=x^{2}-x+1$ is neither strictly increasing nor decreasing on $(-1,1)$.
12. Which of the following functions are decreasing on $0, \frac{\pi}{2}$ ?
(A) $\cos x$
(B) $\cos 2 x$
(C) $\cos 3 x$
(D) $\tan x$
13. On which of the following intervals is the function $f$ given by $f(x)=x^{100}+\sin x-1$ decreasing ?
(A) $(0,1)$
(B) $\frac{\pi}{2}, \pi$
(C) $0, \frac{\pi}{2}$
(D) None of these
14. For what values of $a$ the function $f$ given by $f(x)=x^{2}+a x+1$ is increasing on $[1,2]$ ?
15. Let I be any interval disjoint from $[-1,1]$. Prove that the function $f$ given by $f(x)=x+\frac{1}{x}$ is increasing on I .
16. Prove that the function $f$ given by $f(x)=\log \sin x$ is increasing on $0, \frac{\pi}{2}$ and decreasing on $\frac{\pi}{2}, \pi$.
17. Prove that the function $f$ given by $f(x)=\log |\cos x|$ is decreasing on $\left(0, \frac{\pi}{2}\right)$ and increasing on $\left(\frac{3 \pi}{2}, 2 \pi\right)$.
18. Prove that the function given by $f(x)=x^{3}-3 x^{2}+3 x-100$ is increasing in $\mathbf{R}$.
19. The interval in which $y=x^{2} e^{-x}$ is increasing is
(A) $(-\infty, \infty)$
(B) $(-2,0)$
(C) $(2, \infty)$
(D) $(0,2)$

### 6.4 Maxima and Minima

In this section, we will use the concept of derivatives to calculate the maximum or minimum values of various functions. In fact, we will find the 'turning points' of the graph of a function and thus find points at which the graph reaches its highest (or
lowest) locally. The knowledge of such points is very useful in sketching the graph of a given function. Further, we will also find the absolute maximum and absolute minimum of a function that are necessary for the solution of many applied problems.

Let us consider the following problems that arise in day to day life.
(i) The profit from a grove of orange trees is given by $\mathrm{P}(x)=a x+b x^{2}$, where $a, b$ are constants and $x$ is the number of orange trees per acre. How many trees per acre will maximise the profit?
(ii) A ball, thrown into the air from a building 60 metres high, travels along a path given by $h(x)=60+x-\frac{x^{2}}{60}$, where $x$ is the horizontal distance from the building and $h(x)$ is the height of the ball. What is the maximum height the ball will reach?
(iii) An Apache helicopter of enemy is flying along the path given by the curve $f(x)=x^{2}+7$. A soldier, placed at the point $(1,2)$, wants to shoot the helicopter when it is nearest to him. What is the nearest distance?

In each of the above problem, there is something common, i.e., we wish to find out the maximum or minimum values of the given functions. In order to tackle such problems, we first formally define maximum or minimum values of a function, points of local maxima and minima and test for determining such points.
Definition 3 Let $f$ be a function defined on an interval I. Then
(a) $f$ is said to have a maximum value in I, if there exists a point $c$ in I such that $f(c)>f(x)$, for all $x \in \mathrm{I}$.

The number $f(c)$ is called the maximum value of $f$ in I and the point $c$ is called a point of maximum value of $f$ in I .
(b) $\quad f$ is said to have a minimum value in I, if there exists a point $c$ in I such that $f(c)<f(x)$, for all $x \in \mathrm{I}$.
The number $f(c)$, in this case, is called the minimum value of $f$ in I and the point $c$, in this case, is called a point of minimum value of $f$ in I .
(c) $f$ is said to have an extreme value in I if there exists a point $c$ in I such that $f(c)$ is either a maximum value or a minimum value of $f$ in I .
The number $f(c)$, in this case, is called an extreme value of $f$ in I and the point $c$ is called an extreme point.

Remark In Fig 6.7(a), (b) and (c), we have exhibited that graphs of certain particular functions help us to find maximum value and minimum value at a point. Infact, through graphs, we can even find maximum/minimum value of a function at a point at which it is not even differentiable (Example 15).
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-15.jpg?height=416&width=1233&top_left_y=323&top_left_x=193)

Example 14 Find the maximum and the minimum values, if any, of the function $f$ given by

$$
f(x)=x^{2}, x \in \mathbf{R} .
$$

Solution From the graph of the given function (Fig 6.8), we have $f(x)=0$ if $x=0$. Also

$$
f(x) \geq 0, \text { for all } x \in \mathbf{R} .
$$

Therefore, the minimum value of $f$ is 0 and the point of minimum value of $f$ is $x=0$. Further, it may be observed from the graph of the function that $f$ has no maximum value and hence no point of maximum value of $f$ in $\mathbf{R}$.
$\square$ Note If we restrict the domain of $f$ to $[-2,1]$ only,
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-15.jpg?height=482&width=407&top_left_y=812&top_left_x=1072)

Fig 6.8 then $f$ will have maximum value $(-2)^{2}=4$ at $x=-2$.

Example 15 Find the maximum and minimum values of $f$, if any, of the function given by $f(x)=|x|, x \in \mathbf{R}$.

Solution From the graph of the given function (Fig 6.9), note that
$f(x) \geq 0$, for all $x \in \mathbf{R}$ and $f(x)=0$ if $x=0$.
Therefore, the function $f$ has a minimum value 0 and the point of minimum value of $f$ is $x=0$. Also, the graph clearly shows that $f$ has no maximum value in $\mathbf{R}$ and hence no point of maximum value in $\mathbf{R}$.
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-15.jpg?height=407&width=477&top_left_y=1448&top_left_x=1000)

Fig 6.9

## Note

(i) If we restrict the domain of $f$ to $[-2,1]$ only, then $f$ will have maximum value $|-2|=2$.
(ii) One may note that the function $f$ in Example 27 is not differentiable at $x=0$.

Example 16 Find the maximum and the minimum values, if any, of the function given by

$$
f(x)=x, x \in(0,1) .
$$

Solution The given function is an increasing (strictly) function in the given interval $(0,1)$. From the graph (Fig 6.10) of the function $f$, it seems that, it should have the minimum value at a point closest to 0 on its right and the maximum value at a point closest to 1 on its left. Are such points available? Of course, not. It is not possible to locate such points. Infact, if a point $x_{0}$ is closest to 0 , then we find $\frac{x_{0}}{2}<x_{0}$ for all $x_{0} \in(0,1)$. Also, if $x_{1}$ is closest to 1 , then $\frac{x_{1}+1}{2}>x_{1}$ for all $x_{1} \in(0,1)$.

Therefore, the given function has neither the
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-16.jpg?height=412&width=490&top_left_y=652&top_left_x=984)

Fig 6.10 maximum value nor the minimum value in the interval $(0,1)$.

Remark The reader may observe that in Example 16, if we include the points 0 and 1 in the domain of $f$, i.e., if we extend the domain of $f$ to $[0,1]$, then the function $f$ has minimum value 0 at $x=0$ and maximum value 1 at $x=1$. Infact, we have the following results (The proof of these results are beyond the scope of the present text)

Every monotonic function assumes its maximum/minimum value at the end points of the domain of definition of the function.

A more general result is
Every continuous function on a closed interval has a maximum and a minimum value.

Note By a monotonic function $f$ in an interval I, we mean that $f$ is either increasing in I or decreasing in I.

Maximum and minimum values of a function defined on a closed interval will be discussed later in this section.

Let us now examine the graph of a function as shown in Fig 6.11. Observe that at points $\mathrm{A}, \mathrm{B}, \mathrm{C}$ and D on the graph, the function changes its nature from decreasing to increasing or vice-versa. These points may be called turning points of the given function. Further, observe that at turning points, the graph has either a little hill or a little valley. Roughly speaking, the function has minimum value in some neighbourhood (interval) of each of the points A and C which are at the bottom of their respective
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-17.jpg?height=403&width=808&top_left_y=332&top_left_x=426)

Fig 6.11
valleys. Similarly, the function has maximum value in some neighbourhood of points B and D which are at the top of their respective hills. For this reason, the points A and C may be regarded as points of local minimum value (or relative minimum value) and points B and D may be regarded as points of local maximum value (or relative maximum value) for the function. The local maximum value and local minimum value of the function are referred to as local maxima and local minima, respectively, of the function.

We now formally give the following definition
Definition 4 Let $f$ be a real valued function and let $c$ be an interior point in the domain of $f$. Then
(a) $\quad c$ is called a point of local maxima if there is an $h>0$ such that

$$
f(c) \geq f(x), \text { for all } x \text { in }(c-h, c+h), x \neq c
$$

The value $f(c)$ is called the local maximum value of $f$.
(b) $\quad c$ is called a point of local minima if there is an $h>0$ such that

$$
f(c) \leq f(x), \text { for all } x \text { in }(c-h, c+h)
$$

The value $f(\mathrm{c})$ is called the local minimum value of $f$.
Geometrically, the above definition states that if $x=c$ is a point of local maxima of $f$, then the graph of $f$ around $c$ will be as shown in Fig 6.12(a). Note that the function $f$ is increasing (i.e., $f^{\prime}(x)>0$ ) in the interval ( $c-h, c$ ) and decreasing (i.e., $f^{\prime}(x)<0$ ) in the interval ( $c, c+h$ ).

This suggests that $f^{\prime}(c)$ must be zero.
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-17.jpg?height=398&width=446&top_left_y=1756&top_left_x=280)

Fig 6.12
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-17.jpg?height=373&width=490&top_left_y=1778&top_left_x=917)

Similarly, if $c$ is a point of local minima of $f$, then the graph of $f$ around $c$ will be as shown in Fig 6.14(b). Here $f$ is decreasing (i.e., $f^{\prime}(x)<0$ ) in the interval ( $c-h, c$ ) and increasing (i.e., $f^{\prime}(x)>0$ ) in the interval ( $c, c+h$ ). This again suggest that $f^{\prime}(c)$ must be zero.

The above discussion lead us to the following theorem (without proof).
Theorem 2 Let $f$ be a function defined on an open interval I. Suppose $c \in \mathrm{I}$ be any point. If $f$ has a local maxima or a local minima at $x=c$, then either $f^{\prime}(c)=0$ or $f$ is not differentiable at $c$.

Remark The converse of above theorem need not be true, that is, a point at which the derivative vanishes need not be a point of local maxima or local minima. For example, if $f(x)=x^{3}$, then $f^{\prime}(x)=3 x^{2}$ and so $f^{\prime}(0)=0$. But 0 is neither a point of local maxima nor a point of local minima (Fig 6.13).

Note A point c in the domain of a function $f$ at which either $f^{\prime}(c)=0$ or $f$ is not differentiable is called a critical point of $f$. Note that if $f$ is continuous at $c$ and $f^{\prime}(c)=0$, then there exists an $h>0$ such that $f$ is differentiable in the interval $(c-h, c+h)$.
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-18.jpg?height=536&width=544&top_left_y=734&top_left_x=964)

Fig 6.13

We shall now give a working rule for finding points of local maxima or points of local minima using only the first order derivatives.

Theorem 3 (First Derivative Test) Let $f$ be a function defined on an open interval I. Let $f$ be continuous at a critical point $c$ in I. Then
(i) If $f^{\prime}(x)$ changes sign from positive to negative as $x$ increases through c , i.e., if $f^{\prime}(x)>0$ at every point sufficiently close to and to the left of $c$, and $f^{\prime}(x)<0$ at every point sufficiently close to and to the right of $c$, then $c$ is a point of local maxima.
(ii) If $f^{\prime}(x)$ changes sign from negative to positive as $x$ increases through $c$, i.e., if $f^{\prime}(x)<0$ at every point sufficiently close to and to the left of $c$, and $f^{\prime}(x)>0$ at every point sufficiently close to and to the right of $c$, then $c$ is a point of local minima.
(iii) If $f^{\prime}(x)$ does not change sign as $x$ increases through $c$, then $c$ is neither a point of local maxima nor a point of local minima. Infact, such a point is called point of inflection (Fig 6.13).


#### Abstract

Note If $c$ is a point of local maxima of $f$, then $f(c)$ is a local maximum value of $f$. Similarly, if $c$ is a point of local minima of $f$, then $f(c)$ is a local minimum value of $f$.


Figures 6.13 and 6.14, geometrically explain Theorem 3.
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-19.jpg?height=491&width=1047&top_left_y=543&top_left_x=302)

Fig 6.14
Example 17 Find all points of local maxima and local minima of the function $f$ given by

$$
f(x)=x^{3}-3 x+3 .
$$

Solution We have
or

$$
\begin{aligned}
f(x) & =x^{3}-3 x+3 \\
f^{\prime}(x) & =3 x^{2}-3=3(x-1)(x+1) \\
f^{\prime}(x) & =0 \text { at } x=1 \text { and } x=-1
\end{aligned}
$$

or
Thus, $x= \pm 1$ are the only critical points which could possibly be the points of local maxima and/or local minima of $f$. Let us first examine the point $x=1$.

Note that for values close to 1 and to the right of $1, f^{\prime}(x)>0$ and for values close to 1 and to the left of $1, f^{\prime}(x)<0$. Therefore, by first derivative test, $x=1$ is a point of local minima and local minimum value is $f(1)=1$. In the case of $x=-1$, note that $f^{\prime}(x)>0$, for values close to and to the left of -1 and $f^{\prime}(x)<0$, for values close to and to the right of -1 . Therefore, by first derivative test, $x=-1$ is a point of local maxima and local maximum value is $f(-1)=5$.

|  | Values of $\boldsymbol{x}$ | Sign of $\boldsymbol{f}^{\prime}(\boldsymbol{x})=\mathbf{3}(\boldsymbol{x}-\mathbf{1})(\boldsymbol{x}+\mathbf{1})$ |
| :--- | :--- | :---: |
| Close to 1 | to the right (say 1.1 etc.) <br> to the left (say 0.9 etc.) | $>0$ |
| Close to -1 | to the right (say -0.9 etc.) <br> to the left (say -1.1 etc.) | $<0$ |

Example 18 Find all the points of local maxima and local minima of the function $f$ given by

$$
f(x)=2 x^{3}-6 x^{2}+6 x+5 .
$$

Solution We have
or

$$
\begin{aligned}
f(x) & =2 x^{3}-6 x^{2}+6 x+5 \\
f^{\prime}(x) & =6 x^{2}-12 x+6=6(x-1)^{2} \\
f^{\prime}(x) & =0 \quad \text { at } \quad x=1
\end{aligned}
$$

or
Thus, $x=1$ is the only critical point of $f$. We shall now examine this point for local maxima and/or local minima of $f$. Observe that $f^{\prime}(x) \geq 0$, for all $x \in \mathbf{R}$ and in particular $f^{\prime}(x)>0$, for values close to 1 and to the left and to the right of 1 . Therefore, by first derivative test, the point $x=1$ is neither a point of local maxima nor a point of local minima. Hence $x=1$ is a point of inflexion.

Remark One may note that since $f^{\prime}(x)$, in Example 30, never changes its sign on $\mathbf{R}$, graph of $f$ has no turning points and hence no point of local maxima or local minima.

We shall now give another test to examine local maxima and local minima of a given function. This test is often easier to apply than the first derivative test.
Theorem 4 (Second Derivative Test) Let $f$ be a function defined on an interval I and $c \in \mathrm{I}$. Let $f$ be twice differentiable at $c$. Then
(i) $x=c$ is a point of local maxima if $f^{\prime}(c)=0$ and $f^{\prime \prime}(c)<0$

The value $f(c)$ is local maximum value of $f$.
(ii) $x=c$ is a point of local minima if $f^{\prime}(c)=0$ and $f^{\prime \prime}(c)>0$

In this case, $f(c)$ is local minimum value of $f$.
(iii) The test fails if $f^{\prime}(c)=0$ and $f^{\prime \prime}(c)=0$.

In this case, we go back to the first derivative test and find whether $c$ is a point of local maxima, local minima or a point of inflexion.

- Note As $f$ is twice differentiable at $c$, we mean second order derivative of $f$ exists at $c$.

Example 19 Find local minimum value of the function $f$ given by $f(x)=3+|x|, x \in \mathbf{R}$.

Solution Note that the given function is not differentiable at $x=0$. So, second derivative test fails. Let us try first derivative test. Note that 0 is a critical point of $f$. Now to the left of $0, f(x)=3-x$ and so $f^{\prime}(x)=-1<0$. Also to
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-20.jpg?height=399&width=441&top_left_y=1656&top_left_x=1039)

Fig 6.15
the right of $0, f(x)=3+x$ and so $f^{\prime}(x)=1>0$. Therefore, by first derivative test, $x=$ 0 is a point of local minima of $f$ and local minimum value of $f$ is $f(0)=3$.

Example 20 Find local maximum and local minimum values of the function $f$ given by

$$
f(x)=3 x^{4}+4 x^{3}-12 x^{2}+12
$$

Solution We have
or

$$
\begin{aligned}
f(x) & =3 x^{4}+4 x^{3}-12 x^{2}+12 \\
f^{\prime}(x) & =12 x^{3}+12 x^{2}-24 x=12 x(x-1)(x+2) \\
f^{\prime}(x) & =0 \text { at } x=0, x=1 \text { and } x=-2 \\
f^{\prime \prime}(x) & =36 x^{2}+24 x-24=12\left(3 x^{2}+2 x-2\right)
\end{aligned}
$$

or
Now

$$
\begin{array}{ll}
f^{\prime \prime}(0) & =-24<0 \\
f^{\prime \prime}(1) & =36>0 \\
f^{\prime \prime}(-2) & =72>0
\end{array}
$$

Therefore, by second derivative test, $x=0$ is a point of local maxima and local maximum value of $f$ at $x=0$ is $f(0)=12$ while $x=1$ and $x=-2$ are the points of local minima and local minimum values of $f$ at $x=-1$ and -2 are $f(1)=7$ and $f(-2)=-20$, respectively.

Example 21 Find all the points of local maxima and local minima of the function $f$ given by

$$
f(x)=2 x^{3}-6 x^{2}+6 x+5 .
$$

Solution We have
or

$$
\begin{gathered}
f(x)=2 x^{3}-6 x^{2}+6 x+5 \\
\left\{\begin{array}{l}
f^{\prime}(x)=6 x^{2}-12 x+6=6(x-1)^{2} \\
f^{\prime \prime}(x)=12(x-1)
\end{array}\right.
\end{gathered}
$$

Now $f^{\prime}(x)=0$ gives $x=1$. Also $f^{\prime \prime}(1)=0$. Therefore, the second derivative test fails in this case. So, we shall go back to the first derivative test.

We have already seen (Example 18) that, using first derivative test, $x=1$ is neither a point of local maxima nor a point of local minima and so it is a point of inflexion.

Example 22 Find two positive numbers whose sum is 15 and the sum of whose squares is minimum.

Solution Let one of the numbers be $x$. Then the other number is ( $15-x$ ). Let $\mathrm{S}(x)$ denote the sum of the squares of these numbers. Then
or

$$
\begin{gathered}
S(x)=x^{2}+(15-x)^{2}=2 x^{2}-30 x+225 \\
\left\{\begin{array}{l}
S^{\prime}(x)=4 x-30 \\
S^{\prime \prime}(x)=4
\end{array}\right.
\end{gathered}
$$

Now $S^{\prime}(x)=0$ gives $x=\frac{15}{2}$. Also $S^{\prime \prime}\left(\frac{15}{2}\right)=4>0$. Therefore, by second derivative test, $x=\frac{15}{2}$ is the point of local minima of S . Hence the sum of squares of numbers is minimum when the numbers are $\frac{15}{2}$ and $15-\frac{15}{2}=\frac{15}{2}$.

Remark Proceeding as in Example 34 one may prove that the two positive numbers, whose sum is $k$ and the sum of whose squares is minimum, are $\frac{k}{2}$ and $\frac{k}{2}$.

Example 23 Find the shortest distance of the point ( $0, c$ ) from the parabola $y=x^{2}$, where $\frac{1}{2} \leq c \leq 5$.

Solution Let $(h, k)$ be any point on the parabola $y=x^{2}$. Let D be the required distance between $(h, k)$ and $(0, c)$. Then

$$
\begin{equation*}
\mathrm{D}=\sqrt{(h-0)^{2}+(k-c)^{2}}=\sqrt{h^{2}+(k-c)^{2}} \tag{1}
\end{equation*}
$$

Since ( $h, k$ ) lies on the parabola $y=x^{2}$, we have $k=h^{2}$. So (1) gives

$$
\mathrm{D} \equiv \mathrm{D}(k)=\sqrt{k+(k-c)^{2}}
$$

or

$$
\begin{aligned}
& \mathrm{D}^{\prime}(k)=\frac{1+2(k-c)}{2 \sqrt{k+(k-c)^{2}}} \\
& \mathrm{D}^{\prime}(k)=0 \text { gives } k=\frac{2 c-1}{2}
\end{aligned}
$$

Now

Observe that when $k<\frac{2 c-1}{2}$, then $2(k-c)+1<0$, i.e., $\mathrm{D}^{\prime}(k)<0$. Also when $k>\frac{2 c-1}{2}$, then $\mathrm{D}^{\prime}(k)>0$. So, by first derivative test, $\mathrm{D}(k)$ is minimum at $k=\frac{2 c-1}{2}$.

Hence, the required shortest distance is given by

$$
\mathrm{D}\left(\frac{2 c-1}{2}\right)=\sqrt{\frac{2 c-1}{2}+\left(\frac{2 c-1}{2}-c\right)^{2}}=\frac{\sqrt{4 c-1}}{2}
$$

~ Note The reader may note that in Example 35, we have used first derivative test instead of the second derivative test as the former is easy and short.

Example 24 Let AP and BQ be two vertical poles at points A and B , respectively. If $\mathrm{AP}=16 \mathrm{~m}, \mathrm{BQ}=22 \mathrm{~m}$ and $\mathrm{AB}=20 \mathrm{~m}$, then find the distance of a point R on AB from the point A such that $\mathrm{RP}^{2}+\mathrm{RQ}^{2}$ is minimum.

Solution Let R be a point on AB such that $\mathrm{AR}=x \mathrm{~m}$. Then $\mathrm{RB}=(20-x) \mathrm{m}($ as $\mathrm{AB}=20 \mathrm{~m})$. From Fig 6.16, we have

$$
\mathrm{RP}^{2}=\mathrm{AR}^{2}+\mathrm{AP}^{2}
$$

and

$$
\mathrm{RQ}^{2}=\mathrm{RB}^{2}+\mathrm{BQ}^{2}
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-23.jpg?height=356&width=460&top_left_y=782&top_left_x=1020)

Fig 6.16

Therefore

$$
\begin{aligned}
\mathrm{RP}^{2}+\mathrm{RQ}^{2} & =\mathrm{AR}^{2}+\mathrm{AP}^{2}+\mathrm{RB}^{2}+\mathrm{BQ}^{2} \\
& =x^{2}+(16)^{2}+(20-x)^{2}+(22)^{2} \\
& =2 x^{2}-40 x+1140
\end{aligned}
$$

Let

$$
\mathrm{S} \equiv \mathrm{~S}(x)=\mathrm{RP}^{2}+\mathrm{RQ}^{2}=2 x^{2}-40 x+1140 .
$$

Therefore

$$
\mathrm{S}^{\prime}(x)=4 x-40
$$

Now $\mathrm{S}^{\prime}(x)=0$ gives $x=10$. Also $\mathrm{S}^{\prime \prime}(x)=4>0$, for all $x$ and so $\mathrm{S}^{\prime \prime}(10)>0$. Therefore, by second derivative test, $x=10$ is the point of local minima of S . Thus, the distance of R from A on AB is $\mathrm{AR}=x=10 \mathrm{~m}$.

Example 25 If length of three sides of a trapezium other than base are equal to 10 cm , then find the area of the trapezium when it is maximum.
Solution The required trapezium is as given in Fig 6.17. Draw perpendiculars DP and
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-23.jpg?height=365&width=755&top_left_y=1775&top_left_x=446)

Fig 6.17

CQ on AB . Let $\mathrm{AP}=x \mathrm{~cm}$. Note that $\triangle \mathrm{APD} \sim \triangle \mathrm{BQC}$. Therefore, $\mathrm{QB}=x \mathrm{~cm}$. Also, by Pythagoras theorem, $\mathrm{DP}=\mathrm{QC}=\sqrt{100-x^{2}}$. Let A be the area of the trapezium. Then

$$
\begin{aligned}
A \equiv A(x) & =\frac{1}{2} \text { (sum of parallel sides) (height) } \\
& =\frac{1}{2}(2 x+10+10)\left(\sqrt{100-x^{2}}\right) \\
& =(x+10)\left(\sqrt{100-x^{2}}\right)
\end{aligned}
$$

or

$$
\begin{aligned}
\mathrm{A}^{\prime}(x) & =(x+10) \frac{(-2 x)}{2 \sqrt{100-x^{2}}}+\left(\sqrt{100-x^{2}}\right) \\
& =\frac{-2 x^{2}-10 x+100}{\sqrt{100-x^{2}}}
\end{aligned}
$$

Now $\quad \mathrm{A}^{\prime}(x)=0$ gives $2 x^{2}+10 x-100=0$, i.e., $x=5$ and $x=-10$.
Since $x$ represents distance, it can not be negative.
So, $x=5$. Now

$$
\begin{aligned}
A^{\prime \prime}(x) & =\frac{\sqrt{100-x^{2}}(-4 x-10)-\left(-2 x^{2}-10 x+100\right) \frac{(-2 x)}{2 \sqrt{100-x^{2}}}}{100-x^{2}} \\
& =\frac{2 x^{3}-300 x-1000}{\left(100-x^{2}\right)^{\frac{3}{2}}}(\text { on simplification })
\end{aligned}
$$

or

$$
A^{\prime \prime}(5)=\frac{2(5)^{3}-300(5)-1000}{\left(100-(5)^{2}\right)^{\frac{3}{2}}}=\frac{-2250}{75 \sqrt{75}}=\frac{-30}{\sqrt{75}}<0
$$

Thus, area of trapezium is maximum at $x=5$ and the area is given by

$$
A(5)=(5+10) \sqrt{100-(5)^{2}}=15 \sqrt{75}=75 \sqrt{3} \mathrm{~cm}^{2}
$$

Example 26 Prove that the radius of the right circular cylinder of greatest curved surface area which can be inscribed in a given cone is half of that of the cone.

Solution Let $\mathrm{OC}=r$ be the radius of the cone and $\mathrm{OA}=h$ be its height. Let a cylinder with radius $\mathrm{OE}=x$ inscribed in the given cone (Fig 6.18). The height QE of the cylinder is given by

$$
\frac{\mathrm{QE}}{\mathrm{OA}}=\frac{\mathrm{EC}}{\mathrm{OC}} \quad(\text { since } \Delta \mathrm{QEC} \sim \Delta \mathrm{AOC})
$$

or

$$
\frac{\mathrm{QE}}{h}=\frac{r-x}{r}
$$

or

$$
\mathrm{QE}=\frac{h(r-x)}{r}
$$

Let S be the curved surface area of the given cylinder. Then

$$
\mathrm{S} \equiv \mathrm{~S}(x)=\frac{2 \pi x h(r-x)}{r}=\frac{2 \pi h}{r}\left(r x-x^{2}\right)
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-25.jpg?height=502&width=458&top_left_y=347&top_left_x=1023)

Fig 6.18
or

$$
\left\{\begin{array}{l}
\mathrm{S}^{\prime}(x)=\frac{2 \pi h}{r}(r-2 x) \\
\mathrm{S}^{\prime \prime}(x)=\frac{-4 \pi h}{r}
\end{array}\right.
$$

Now $\mathrm{S}^{\prime}(x)=0$ gives $x=\frac{r}{2}$. Since $\mathrm{S}^{\prime \prime}(x)<0$ for all $x, \mathrm{~S}^{\prime \prime}\left(\frac{r}{2}\right)<0$. So $x=\frac{r}{2}$ is a point of maxima of S . Hence, the radius of the cylinder of greatest curved surface area which can be inscribed in a given cone is half of that of the cone.

### 6.4.1 Maximum and Minimum Values of a Function in a Closed Interval

Let us consider a function $f$ given by

$$
f(x)=x+2, x \in(0,1)
$$

Observe that the function is continuous on $(0,1)$ and neither has a maximum value nor has a minimum value. Further, we may note that the function even has neither a local maximum value nor a local minimum value.

However, if we extend the domain of $f$ to the closed interval $[0,1]$, then $f$ still may not have a local maximum (minimum) values but it certainly does have maximum value $3=f(1)$ and minimum value $2=f(0)$. The maximum value 3 of $f$ at $x=1$ is called absolute maximum value (global maximum or greatest value) of $f$ on the interval $[0,1]$. Similarly, the minimum value 2 of $f$ at $x=0$ is called the absolute minimum value (global minimum or least value) of $f$ on $[0,1]$.

Consider the graph given in Fig 6.19 of a continuous function defined on a closed interval $[a, d]$. Observe that the function $f$ has a local minima at $x=b$ and local
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-26.jpg?height=467&width=829&top_left_y=337&top_left_x=420)

Fig 6.19
minimum value is $f(b)$. The function also has a local maxima at $x=c$ and local maximum value is $f(c)$.

Also from the graph, it is evident that $f$ has absolute maximum value $f(a)$ and absolute minimum value $f(d)$. Further note that the absolute maximum (minimum) value of $f$ is different from local maximum (minimum) value of $f$.

We will now state two results (without proof) regarding absolute maximum and absolute minimum values of a function on a closed interval I.

Theorem 5 Let $f$ be a continuous function on an interval $\mathrm{I}=[a, b]$. Then $f$ has the absolute maximum value and $f$ attains it at least once in I. Also, $f$ has the absolute minimum value and attains it at least once in I.

Theorem 6 Let $f$ be a differentiable function on a closed interval I and let $c$ be any interior point of I. Then
(i) $f^{\prime}(c)=0$ if $f$ attains its absolute maximum value at $c$.
(ii) $f^{\prime}(c)=0$ if $f$ attains its absolute minimum value at $c$.

In view of the above results, we have the following working rule for finding absolute maximum and/or absolute minimum values of a function in a given closed interval $[a, b]$.

## Working Rule

Step 1: Find all critical points of $f$ in the interval, i.e., find points $x$ where either $f^{\prime}(x)=0$ or $f$ is not differentiable.

Step 2: Take the end points of the interval.
Step 3: At all these points (listed in Step 1 and 2), calculate the values of $f$.
Step 4: Identify the maximum and minimum values of $f$ out of the values calculated in Step 3. This maximum value will be the absolute maximum (greatest) value of $f$ and the minimum value will be the absolute minimum (least) value of $f$.

Example 27 Find the absolute maximum and minimum values of a function $f$ given by

$$
f(x)=2 x^{3}-15 x^{2}+36 x+1 \text { on the interval }[1,5] .
$$

Solution We have
or

$$
\begin{aligned}
f(x) & =2 x^{3}-15 x^{2}+36 x+1 \\
f^{\prime}(x) & =6 x^{2}-30 x+36=6(x-3)(x-2)
\end{aligned}
$$

Note that $f^{\prime}(x)=0$ gives $x=2$ and $x=3$.
We shall now evaluate the value of $f$ at these points and at the end points of the interval $[1,5]$, i.e., at $x=1, x=2, x=3$ and at $x=5$. So

$$
\begin{aligned}
& f(1)=2\left(1^{3}\right)-15\left(1^{2}\right)+36(1)+1=24 \\
& f(2)=2\left(2^{3}\right)-15\left(2^{2}\right)+36(2)+1=29 \\
& f(3)=2\left(3^{3}\right)-15\left(3^{2}\right)+36(3)+1=28 \\
& f(5)=2\left(5^{3}\right)-15\left(5^{2}\right)+36(5)+1=56
\end{aligned}
$$

Thus, we conclude that absolute maximum value of $f$ on $[1,5]$ is 56 , occurring at $x=5$, and absolute minimum value of $f$ on $[1,5]$ is 24 which occurs at $x=1$.

Example 28 Find absolute maximum and minimum values of a function $f$ given by

$$
f(x)=12 x^{\frac{4}{3}}-6 x^{\frac{1}{3}}, x \in[-1,1]
$$

Solution We have
or

$$
\begin{aligned}
f(x) & =12 x^{\frac{4}{3}}-6 x^{\frac{1}{3}} \\
f^{\prime}(x) & =16 x^{\frac{1}{3}}-\frac{2}{x^{\frac{2}{3}}}=\frac{2(8 x-1)}{x^{\frac{2}{3}}}
\end{aligned}
$$

Thus, $f^{\prime}(x)=0$ gives $x=\frac{1}{8}$. Further note that $f^{\prime}(x)$ is not defined at $x=0$. So the critical points are $x=0$ and $x=\frac{1}{8}$. Now evaluating the value of $f$ at critical points $x=0, \frac{1}{8}$ and at end points of the interval $x=-1$ and $x=1$, we have

$$
\begin{aligned}
f(-1) & =12(-1)^{\frac{4}{3}}-6(-1)^{\frac{1}{3}}=18 \\
f(0) & =12(0)-6(0)=0
\end{aligned}
$$

$$
\begin{aligned}
f\left(\frac{1}{8}\right) & =12\left(\frac{1}{8}\right)^{\frac{4}{3}}-6\left(\frac{1}{8}\right)^{\frac{1}{3}}=\frac{-9}{4} \\
f(1) & =12(1)^{\frac{4}{3}}-6(1)^{\frac{1}{3}}=6
\end{aligned}
$$

Hence, we conclude that absolute maximum value of $f$ is 18 that occurs at $x=-1$ and absolute minimum value of $f$ is $\frac{-9}{4}$ that occurs at $x=\frac{1}{8}$.

Example 29 An Apache helicopter of enemy is flying along the curve given by $y=x^{2}+7$. A soldier, placed at ( 3,7 ), wants to shoot down the helicopter when it is nearest to him. Find the nearest distance.

Solution For each value of $x$, the helicopter's position is at point ( $x, x^{2}+7$ ). Therefore, the distance between the helicopter and the soldier placed at $(3,7)$ is

$$
\sqrt{(x-3)^{2}+\left(x^{2}+7-7\right)^{2}} \text {, i.e., } \sqrt{(x-3)^{2}+x^{4}} \text {. }
$$

Let

$$
f(x)=(x-3)^{2}+x^{4}
$$

or

$$
f^{\prime}(x)=2(x-3)+4 x^{3}=2(x-1)\left(2 x^{2}+2 x+3\right)
$$

Thus, $f^{\prime}(x)=0$ gives $x=1$ or $2 x^{2}+2 x+3=0$ for which there are no real roots. Also, there are no end points of the interval to be added to the set for which $f^{\prime}$ is zero, i.e., there is only one point, namely, $x=1$. The value of $f$ at this point is given by $f(1)=(1-3)^{2}+(1)^{4}=5$. Thus, the distance between the solider and the helicopter is $\sqrt{f(1)}=\sqrt{5}$.

Note that $\sqrt{5}$ is either a maximum value or a minimum value. Since

$$
\sqrt{f(0)}=\sqrt{(0-3)^{2}+(0)^{4}}=3>\sqrt{5}
$$

it follows that $\sqrt{5}$ is the minimum value of $\sqrt{f(x)}$. Hence, $\sqrt{5}$ is the minimum distance between the soldier and the helicopter.

## EXERCISE 6.3

1. Find the maximum and minimum values, if any, of the following functions given by
(i) $f(x)=(2 x-1)^{2}+3$
(ii) $f(x)=9 x^{2}+12 x+2$
(iii) $f(x)=-(x-1)^{2}+10$
(iv) $g(x)=x^{3}+1$
2. Find the maximum and minimum values, if any, of the following functions given by
(i) $f(x)=|x+2|-1$
(ii) $g(x)=-|x+1|+3$
(iii) $h(x)=\sin (2 x)+5$
(iv) $f(x)=|\sin 4 x+3|$
(v) $h(x)=x+1, x \in(-1,1)$
3. Find the local maxima and local minima, if any, of the following functions. Find also the local maximum and the local minimum values, as the case may be:
(i) $f(x)=x^{2}$
(ii) $g(x)=x^{3}-3 x$
(iii) $h(x)=\sin x+\cos x, 0<x<\frac{\pi}{2}$
(iv) $f(x)=\sin x-\cos x, 0<x<2 \pi$
(v) $f(x)=x^{3}-6 x^{2}+9 x+15$
(vi) $g(x)=\frac{x}{2}+\frac{2}{x}, x>0$
(vii) $g(x)=\frac{1}{x^{2}+2}$
(viii) $f(x)=x \sqrt{1-x}, \quad 0<x<1$
4. Prove that the following functions do not have maxima or minima:
(i) $f(x)=e^{x}$
(ii) $g(x)=\log x$
(iii) $h(x)=x^{3}+x^{2}+x+1$
5. Find the absolute maximum value and the absolute minimum value of the following functions in the given intervals:
(i) $f(x)=x^{3}, x \in[-2,2]$
(ii) $f(x)=\sin x+\cos x, x \in[0, \pi]$
(iii) $f(x)=4 x-\frac{1}{2} x^{2}, x \in\left[-2, \frac{9}{2}\right]$
(iv) $\left.f(x)=(x-1)^{2}+3, x \in-3,1\right]$
6. Find the maximum profit that a company can make, if the profit function is given by

$$
p(x)=41-72 x-18 x^{2}
$$

7. Find both the maximum value and the minimum value of $3 x^{4}-8 x^{3}+12 x^{2}-48 x+25$ on the interval $[0,3]$.
8. At what points in the interval $[0,2 \pi]$, does the function $\sin 2 x$ attain its maximum value?
9. What is the maximum value of the function $\sin x+\cos x$ ?
10. Find the maximum value of $2 x^{3}-24 x+107$ in the interval $[1,3]$. Find the maximum value of the same function in $[-3,-1]$.
11. It is given that at $x=1$, the function $x^{4}-62 x^{2}+a x+9$ attains its maximum value, on the interval $[0,2]$. Find the value of $a$.
12. Find the maximum and minimum values of $x+\sin 2 x$ on $[0,2 \pi]$.
13. Find two numbers whose sum is 24 and whose product is as large as possible.
14. Find two positive numbers $x$ and $y$ such that $x+y=60$ and $x y^{3}$ is maximum.
15. Find two positive numbers $x$ and $y$ such that their sum is 35 and the product $x^{2} y^{5}$ is a maximum.
16. Find two positive numbers whose sum is 16 and the sum of whose cubes is minimum.
17. A square piece of tin of side 18 cm is to be made into a box without top, by cutting a square from each corner and folding up the flaps to form the box. What should be the side of the square to be cut off so that the volume of the box is the maximum possible.
18. A rectangular sheet of tin 45 cm by 24 cm is to be made into a box without top, by cutting off square from each corner and folding up the flaps. What should be the side of the square to be cut off so that the volume of the box is maximum ?
19. Show that of all the rectangles inscribed in a given fixed circle, the square has the maximum area.
20. Show that the right circular cylinder of given surface and maximum volume is such that its height is equal to the diameter of the base.
21. Of all the closed cylindrical cans (right circular), of a given volume of 100 cubic centimetres, find the dimensions of the can which has the minimum surface area?
22. A wire of length 28 m is to be cut into two pieces. One of the pieces is to be made into a square and the other into a circle. What should be the length of the two pieces so that the combined area of the square and the circle is minimum?
23. Prove that the volume of the largest cone that can be inscribed in a sphere of radius $R$ is $\frac{8}{27}$ of the volume of the sphere.
24. Show that the right circular cone of least curved surface and given volume has an altitude equal to $\sqrt{2}$ time the radius of the base.
25. Show that the semi-vertical angle of the cone of the maximum volume and of given slant height is $\tan ^{-1} \sqrt{2}$.
26. Show that semi-vertical angle of right circular cone of given surface area and maximum volume is $\sin ^{-1} \frac{1}{3}$.

Choose the correct answer in Questions 27 and 29.
27. The point on the curve $x^{2}=2 y$ which is nearest to the point $(0,5)$ is
(A) $(2 \sqrt{2}, 4)$
(B) $(2 \sqrt{2}, 0)$
(C) $(0,0)$
(D) $(2,2)$
28. For all real values of $x$, the minimum value of $\frac{1-x+x^{2}}{1+x+x^{2}}$ is
(A) 0
(B) 1
(C) 3
(D) $\frac{1}{3}$
29. The maximum value of $[x(x-1)+1]^{\frac{1}{3}}, 0 \leq x \leq 1$ is
(A) $\frac{1}{3}^{\frac{1}{3}}$
(B) $\frac{1}{2}$
(C) 1
(D) 0

## Miscellaneous Examples

Example 30 A car starts from a point P at time $t=0$ seconds and stops at point Q . The distance $x$, in metres, covered by it, in $t$ seconds is given by

$$
x=t^{2} \quad 2-\frac{t}{3}
$$

Find the time taken by it to reach Q and also find distance between P and Q .
Solution Let $v$ be the velocity of the car at $t$ seconds.

Now

$$
\begin{aligned}
& x=t^{2}\left(2-\frac{t}{3}\right) \\
& v=\frac{d x}{d t}=4 t-t^{2}=t(4-t)
\end{aligned}
$$

Therefore

Thus, $v=0$ gives $t=0$ and/or $t=4$.
Now $v=0$ at P as well as at Q and at $\mathrm{P}, t=0$. So, at $\mathrm{Q}, t=4$. Thus, the car will reach the point Q after 4 seconds. Also the distance travelled in 4 seconds is given by

$$
x]_{t=4}=4^{2}\left(2-\frac{4}{3}\right)=16\left(\frac{2}{3}\right)=\frac{32}{3} \mathrm{~m}
$$

Example 31 A water tank has the shape of an inverted right circular cone with its axis vertical and vertex lowermost. Its semi-vertical angle is $\tan ^{-1}(0.5)$. Water is poured into it at a constant rate of 5 cubic metre per hour. Find the rate at which the level of the water is rising at the instant when the depth of water in the tank is 4 m .

Solution Let $r, h$ and $\alpha$ be as in Fig 6.20. Then $\tan \alpha=\frac{r}{h}$.

So

$$
\alpha=\tan ^{-1}\left(\frac{r}{h}\right) .
$$

But

$$
\alpha=\tan ^{-1}(0.5) \quad \text { (given) }
$$

or

$$
\frac{r}{h}=0.5
$$

or

$$
r=\frac{h}{2}
$$

Let V be the volume of the cone. Then

$$
\mathrm{V}=\frac{1}{3} \pi r^{2} h=\frac{1}{3} \pi\left(\frac{h}{2}\right)^{2} h=\frac{\pi h^{3}}{12}
$$

Fig 6.20
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-32.jpg?height=425&width=367&top_left_y=655&top_left_x=1113)
(by Chain Rule)

Therefore

$$
\frac{d \mathrm{~V}}{d t}=\frac{d}{d h}\left(\frac{\pi h^{3}}{12}\right) \cdot \frac{d h}{d t}
$$

$$
=\frac{\pi}{4} h^{2} \frac{d h}{d t}
$$

Now rate of change of volume, i.e., $\frac{d \mathrm{~V}}{d t}=5 \mathrm{~m}^{3} / \mathrm{h}$ and $h=4 \mathrm{~m}$.

Therefore

$$
\begin{aligned}
5 & =\frac{\pi}{4}(4)^{2} \cdot \frac{d h}{d t} \\
\frac{d h}{d t} & =\frac{5}{4 \pi}=\frac{35}{88} \mathrm{~m} / \mathrm{h}\left(\pi=\frac{22}{7}\right)
\end{aligned}
$$

Thus, the rate of change of water level is $\frac{35}{88} \mathrm{~m} / \mathrm{h}$.
Example 32 A man of height 2 metres walks at a uniform speed of $5 \mathrm{~km} / \mathrm{h}$ away from a lamp post which is 6 metres high. Find the rate at which the length of his shadow increases.

Solution In Fig 6．21，Let AB be the lamp－post，the lamp being at the position B and let MN be the man at a particular time $t$ and let $\mathrm{AM}=l$ metres．Then， MS is the shadow of the man．Let $\mathrm{MS}=s$ metres．

Note that
or

$$
\begin{aligned}
\Delta \mathrm{MSN} & \sim \Delta \mathrm{ASB} \\
\frac{\mathrm{MS}}{\mathrm{AS}} & =\frac{\mathrm{MN}}{\mathrm{AB}}
\end{aligned}
$$

or

$$
\mathrm{AS}=3 s(\text { as } \mathrm{MN}=
$$

Thus
So

Therefore

2 and $\mathrm{AB}=6$（given））

            2 and $\mathrm{AB}=6$ (given))
    hus
$=3 s($ as $\mathrm{MN}=$

Since $\frac{d l}{d t}=5 \mathrm{~km} / \mathrm{h}$ ．Hence，the length of the shadow increases at the rate $\frac{5}{2} \mathrm{~km} / \mathrm{h}$ ．

$$
f(x)=\frac{3}{10} x^{4}-\frac{4}{5} x^{3}-3 x^{2}+\frac{36}{5} x+11
$$

is（a）increasing（b）decreasing．
Solution We have

Therefore

$$
\begin{aligned}
\mathrm{AM} & =3 s-s=2 s . \mathrm{But} \mathrm{AM}=l \\
l & =2 s \\
\frac{d l}{d t} & =2 \frac{d s}{d t}
\end{aligned}
$$c

Example 33 Find intervals in which the function given by
....
1
--

$\qquad$

Fig 6.21
類
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-33.jpg?height=32&width=24&top_left_y=783&top_left_x=1512)類![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-33.jpg?height=61&width=45&top_left_y=772&top_left_x=1048)
$\overline{d t}$

    $f(x)=\frac{3}{10} x^{4}-\frac{4}{5} x^{3}-3 x^{2}+\frac{36}{5} x+11$
    $$
f^{\prime}(x)=\frac{3}{10}\left(4 x^{3}\right)-\frac{4}{5}\left(3 x^{2}\right)-3(2 x)+\frac{36}{5}
$$

$$
=\frac{6}{5}(x-1)(x+2)(x-3) \quad(\text { on simplification })
$$

Now $f^{\prime}(x)=0$ gives $x=1, x=-2$, or $x=3$. The points $x=1,-2$, and 3 divide the real line into four disjoint intervals namely, $(-\infty,-2),(-2,1),(1,3)$
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-34.jpg?height=63&width=502&top_left_y=358&top_left_x=971)

Fig 6.22 and $(3, \infty)$ (Fig 6.22).

Consider the interval $(-\infty,-2)$, i.e., when $-\infty<x<-2$.
In this case, we have $x-1<0, x+2<0$ and $x-3<0$.
(In particular, observe that for $x=-3, f^{\prime}(x)=(x-1)(x+2)(x-3)=(-4)(-1)$ ( -6 ) < 0)

Therefore, $\quad f^{\prime}(x)<0$ when $-\infty<x<-2$.
Thus, the function $f$ is decreasing in ( $-\infty,-2$ ).
Consider the interval $(-2,1)$, i.e., when $-2<x<1$.
In this case, we have $x-1<0, x+2>0$ and $x-3<0$
(In particular, observe that for $x=0, f^{\prime}(x)=(x-1)(x+2)(x-3)=(-1)(2)(-3)$ $=6>0$ )
So

$$
f^{\prime}(x)>0 \text { when }-2<x<1 .
$$

Thus,

$$
f \text { is increasing in }(-2,1) \text {. }
$$

Now consider the interval (1, 3), i.e., when $1<x<3$. In this case, we have $x-1>0, x+2>0$ and $x-3<0$.

So,

$$
f^{\prime}(x)<0 \text { when } 1<x<3 .
$$

Thus,

$$
f \text { is decreasing in }(1,3) \text {. }
$$

Finally, consider the interval $(3, \infty)$, i.e., when $x>3$. In this case, we have $x-1>0$, $x+2>0$ and $x-3>0$. So $f^{\prime}(x)>0$ when $x>3$.

Thus, $f$ is increasing in the interval $(3, \infty)$.
Example 34 Show that the function $f$ given by

$$
f(x)=\tan ^{-1}(\sin x+\cos x), x>0
$$

is always an increasing function in $0, \frac{\pi}{4}$.
Solution We have

Therefore

$$
\begin{aligned}
f(x) & =\tan ^{-1}(\sin x+\cos x), x>0 \\
f^{\prime}(x) & =\frac{1}{1+(\sin x+\cos x)^{2}}(\cos x-\sin x)
\end{aligned}
$$

$$
=\frac{\cos x-\sin x}{2+\sin 2 x}
$$

(on simplification)

Note that $2+\sin 2 x>0$ for all $x$ in $0, \frac{\pi}{4}$.
Therefore $\quad f^{\prime}(x)>0$ if $\cos x-\sin x>0$
or $\quad f^{\prime}(x)>0$ if $\cos x>\sin x$ or $\cot x>1$

Now $\cot x>1$ if $\tan x<1$, i.e., if $0<x<\frac{\pi}{4}$

Thus

$$
f^{\prime}(x)>0 \text { in } 0, \frac{\pi}{4}
$$

Hence $f$ is increasing function in $\left(0, \frac{\pi}{4}\right)$.
Example 35 A circular disc of radius 3 cm is being heated. Due to expansion, its radius increases at the rate of $0.05 \mathrm{~cm} / \mathrm{s}$. Find the rate at which its area is increasing when radius is 3.2 cm .

Solution Let $r$ be the radius of the given disc and A be its area. Then

$$
\mathrm{A}=\pi r^{2}
$$

or

$$
\frac{d \mathrm{~A}}{d t}=2 \pi r \frac{d r}{d t}
$$

(by Chain Rule)

Now approximate rate of increase of radius $=d r=\frac{d r}{d t} \Delta t=0.05 \mathrm{~cm} / \mathrm{s}$.
Therefore, the approximate rate of increase in area is given by

$$
\begin{aligned}
d \mathrm{~A} & =\frac{d \mathrm{~A}}{d t}(\Delta t)=2 \pi r\left(\frac{d r}{d t} \Delta t\right) \\
& =2 \pi(3.2)(0.05)=0.320 \pi \mathrm{~cm}^{2} / \mathrm{s} \quad(r=3.2 \mathrm{~cm})
\end{aligned}
$$

Example 36 An open topped box is to be constructed by removing equal squares from each corner of a 3 metre by 8 metre rectangular sheet of aluminium and folding up the sides. Find the volume of the largest such box.

Solution Let $x$ metre be the length of a side of the removed squares. Then, the height of the box is $x$, length is $8-2 x$ and breadth is $3-2 x$ (Fig 6.23). If $\mathrm{V}(x)$ is the volume of the box, then
![](https://cdn.mathpix.com/cropped/2025_07_21_d425024c568c0257e01bg-36.jpg?height=247&width=1019&top_left_y=491&top_left_x=335)

Fig 6.23

$$
\begin{aligned}
\mathrm{V}(x) & =x(3-2 x)(8-2 x) \\
& =4 x^{3}-22 x^{2}+24 x
\end{aligned}
$$

Therefore

$$
\left\{\begin{array}{l}
\mathrm{V}^{\prime}(x)=12 x^{2}-44 x+24=4(x-3)(3 x-2) \\
\mathrm{V}^{\prime \prime}(x)=24 x-44
\end{array}\right.
$$

Now

$$
\mathrm{V}^{\prime}(x)=0 \text { gives } x=3, \frac{2}{3} \text {. But } x \neq 3 \text { (Why?) }
$$

Thus, we have $x=\frac{2}{3}$. Now $\mathrm{V}^{\prime \prime}\left(\frac{2}{3}\right)=24\left(\frac{2}{3}\right)-44=-28<0$.
Therefore, $x=\frac{2}{3}$ is the point of maxima, i.e., if we remove a square of side $\frac{2}{3}$ metre from each corner of the sheet and make a box from the remaining sheet, then the volume of the box such obtained will be the largest and it is given by

$$
\begin{aligned}
V\left(\frac{2}{3}\right) & =4\left(\frac{2}{3}\right)^{3}-22\left(\frac{2}{3}\right)^{2}+24\left(\frac{2}{3}\right) \\
& =\frac{200}{27} \mathrm{~m}^{3}
\end{aligned}
$$

Example 37 Manufacturer can sell $x$ items at a price of rupees $5-\frac{x}{100}$ each. The cost price of $x$ items is Rs $\frac{x}{5}+500$. Find the number of items he should sell to earn maximum profit.

Solution Let $\mathrm{S}(x)$ be the selling price of $x$ items and let $\mathrm{C}(x)$ be the cost price of $x$ items. Then, we have
and

$$
\begin{aligned}
& \mathrm{S}(x)=\left(5-\frac{x}{100}\right) x=5 x-\frac{x^{2}}{100} \\
& \mathrm{C}(x)=\frac{x}{5}+500
\end{aligned}
$$

Thus, the profit function $\mathrm{P}(x)$ is given by
i.e.

$$
P(x)=S(x)-C(x)=5 x-\frac{x^{2}}{100}-\frac{x}{5}-500
$$

or

$$
\mathrm{P}(x)=\frac{24}{5} x-\frac{x^{2}}{100}-500
$$

$$
\mathrm{P}^{\prime}(x)=\frac{24}{5}-\frac{x}{50}
$$

Now $\mathrm{P}^{\prime}(x)=0$ gives $x=240$. Also $\mathrm{P}^{\prime \prime}(x)=\frac{-1}{50}$. So $\mathrm{P}^{\prime \prime}(240)=\frac{-1}{50}<0$
Thus, $x=240$ is a point of maxima. Hence, the manufacturer can earn maximum profit, if he sells 240 items.

## Miscellaneous Exercise on Chapter 6

1. Show that the function given by $f(x)=\frac{\log x}{x}$ has maximum at $x=e$.
2. The two equal sides of an isosceles triangle with fixed base $b$ are decreasing at the rate of 3 cm per second. How fast is the area decreasing when the two equal sides are equal to the base ?
3. Find the intervals in which the function $f$ given by

$$
f(x)=\frac{4 \sin x-2 x-x \cos x}{2+\cos x}
$$

is (i) increasing (ii) decreasing.
4. Find the intervals in which the function $f$ given by $f(x)=x^{3}+\frac{1}{x^{3}}, x \neq 0$ is
(i) increasing
(ii) decreasing.
5. Find the maximum area of an isosceles triangle inscribed in the ellipse $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ with its vertex at one end of the major axis.
6. A tank with rectangular base and rectangular sides, open at the top is to be constructed so that its depth is 2 m and volume is $8 \mathrm{~m}^{3}$. If building of tank costs Rs 70 per sq metres for the base and Rs 45 per square metre for sides. What is the cost of least expensive tank?
7. The sum of the perimeter of a circle and square is $k$, where $k$ is some constant. Prove that the sum of their areas is least when the side of square is double the radius of the circle.
8. A window is in the form of a rectangle surmounted by a semicircular opening. The total perimeter of the window is 10 m . Find the dimensions of the window to admit maximum light through the whole opening.
9. A point on the hypotenuse of a triangle is at distance $a$ and $b$ from the sides of the triangle.

Show that the minimum length of the hypotenuse is $\left(a^{\frac{2}{3}}+b^{\frac{2}{3}}\right)^{\frac{3}{2}}$.
10. Find the points at which the function $f$ given by $f(x)=(x-2)^{4}(x+1)^{3}$ has
(i) local maxima
(ii) local minima
(iii) point of inflexion
11. Find the absolute maximum and minimum values of the function $f$ given by

$$
f(x)=\cos ^{2} x+\sin x, x \in[0, \pi]
$$

12. Show that the altitude of the right circular cone of maximum volume that can be inscribed in a sphere of radius $r$ is $\frac{4 r}{3}$.
13. Let $f$ be a function defined on $[a, b]$ such that $f^{\prime}(x)>0$, for all $x \in(a, b)$. Then prove that $f$ is an increasing function on ( $a, b$ ).
14. Show that the height of the cylinder of maximum volume that can be inscribed in a sphere of radius R is $\frac{2 \mathrm{R}}{\sqrt{3}}$. Also find the maximum volume.
15. Show that height of the cylinder of greatest volume which can be inscribed in a right circular cone of height $h$ and semi vertical angle $\alpha$ is one-third that of the cone and the greatest volume of cylinder is $\frac{4}{27} \pi h^{3} \tan ^{2} \alpha$.
16. A cylindrical tank of radius 10 m is being filled with wheat at the rate of 314 cubic metre per hour. Then the depth of the wheat is increasing at the rate of
(A) $1 \mathrm{~m} / \mathrm{h}$
(B) $0.1 \mathrm{~m} / \mathrm{h}$
(C) $1.1 \mathrm{~m} / \mathrm{h}$
(D) $0.5 \mathrm{~m} / \mathrm{h}$

## Summary

- If a quantity $y$ varies with another quantity $x$, satisfying some rule $y=f(x)$, then $\frac{d y}{d x}$ (or $f^{\prime}(x)$ ) represents the rate of change of $y$ with respect to $x$ and $\frac{d y}{d x}{ }_{x=x_{0}}$ (or $f^{\prime}\left(x_{0}\right)$ ) represents the rate of change of $y$ with respect to $x$ at $x=x_{0}$.
- If two variables $x$ and $y$ are varying with respect to another variable $t$, i.e., if $x=f(t)$ and $y=g(t)$, then by Chain Rule

$$
\frac{d y}{d x}=\frac{d y}{d t} / \frac{d x}{d t}, \text { if } \frac{d x}{d t} \neq 0 .
$$

- A function $f$ is said to be
(a) increasing on an interval ( $a, b$ ) if $x_{1}<x_{2}$ in ( $\left.a, b\right) \Rightarrow f\left(x_{1}\right)<f\left(x_{2}\right)$ for all $x_{1}, x_{2} \in(a, b)$.
Alternatively, if $f^{\prime}(x) \geq 0$ for each $x$ in ( $a, b$ )
(b) decreasing on $(a, b)$ if

$$
x_{1}<x_{2} \text { in }(a, b) \Rightarrow f\left(x_{1}\right)>f\left(x_{2}\right) \text { for all } x_{1}, x_{2} \in(a, b) .
$$

(c) constant in $(a, b)$, if $f(x)=c$ for all $x \in(a, b)$, where $c$ is a constant.

- A point $c$ in the domain of a function $f$ at which either $f^{\prime}(c)=0$ or $f$ is not differentiable is called a critical point of $f$.
- First Derivative Test Let $f$ be a function defined on an open interval I. Let $f$ be continuous at a critical point $c$ in I. Then
(i) If $f^{\prime}(x)$ changes sign from positive to negative as $x$ increases through c , i.e., if $f^{\prime}(x)>0$ at every point sufficiently close to and to the left of $c$, and $f^{\prime}(x)<0$ at every point sufficiently close to and to the right of $c$, then $c$ is a point of local maxima.
(ii) If $f^{\prime}(x)$ changes sign from negative to positive as $x$ increases through $c$, i.e., if $f^{\prime}(x)<0$ at every point sufficiently close to and to the left of $c$, and $f^{\prime}(x)>0$ at every point sufficiently close to and to the right of $c$, then $c$ is a point of local minima.
(iii) If $f^{\prime}(x)$ does not change sign as $x$ increases through $c$, then $c$ is neither a point of local maxima nor a point of local minima. Infact, such a point is called point of inflexion.
- Second Derivative Test Let $f$ be a function defined on an interval I and $c \in \mathrm{I}$. Let $f$ be twice differentiable at $c$. Then
(i) $x=c$ is a point of local maxima if $f^{\prime}(c)=0$ and $f^{\prime \prime}(c)<0$

The values $f(c)$ is local maximum value of $f$.
(ii) $x=c$ is a point of local minima if $f^{\prime}(c)=0$ and $f^{\prime \prime}(c)>0$

In this case, $f(c)$ is local minimum value of $f$.
(iii) The test fails if $f^{\prime}(c)=0$ and $f^{\prime \prime}(c)=0$.

In this case, we go back to the first derivative test and find whether $c$ is a point of maxima, minima or a point of inflexion.

- Working rule for finding absolute maxima and/or absolute minima

Step 1: Find all critical points of $f$ in the interval, i.e., find points $x$ where either $f^{\prime}(x)=0$ or $f$ is not differentiable.
Step 2:Take the end points of the interval.
Step 3: At all these points (listed in Step 1 and 2), calculate the values of $f$.
Step 4: Identify the maximum and minimum values of $f$ out of the values calculated in Step 3. This maximum value will be the absolute maximum value of $f$ and the minimum value will be the absolute minimum value of $f$.

