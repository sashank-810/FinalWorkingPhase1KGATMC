![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-01.jpg?height=275&width=250&top_left_y=129&top_left_x=812)

Chapter 12

## LIMITS AND DERIVATIVES

## With the Calculus as a key, Mathematics can be successfully applied to the explanation of the course of Nature - WHITEHEAD

### 12.1 Introduction

This chapter is an introduction to Calculus. Calculus is that branch of mathematics which mainly deals with the study of change in the value of a function as the points in the domain change. First, we give an intuitive idea of derivative (without actually defining it). Then we give a naive definition of limit and study some algebra of limits. Then we come back to a definition of derivative and study some algebra of derivatives. We also obtain derivatives of certain standard functions.

### 12.2 Intuitive Idea of Derivatives

Physical experiments have confirmed that the body dropped
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-01.jpg?height=558&width=407&top_left_y=904&top_left_x=1058)

Sir Issac Newton
(1642-1727) from a tall cliff covers a distance of $4.9 t^{2}$ metres in $t$ seconds, i.e., distance $s$ in metres covered by the body as a function of time $t$ in seconds is given by $s=4.9 t^{2}$.

The adjoining Table 13.1 gives the distance travelled in metres at various intervals of time in seconds of a body dropped from a tall cliff.

The objective is to find the veloctiy of the body at time $t=2$ seconds from this data. One way to approach this problem is to find the average velocity for various intervals of time ending at $t=2$ seconds and hope that these throw some light on the velocity at $t=2$ seconds.

Average velocity between $t=t_{1}$ and $t=t_{2}$ equals distance travelled between $t=t_{1}$ and $t=t_{2}$ seconds divided by ( $t_{2}-t_{1}$ ). Hence the average velocity in the first two seconds

$$
\begin{aligned}
& =\frac{\text { Distance travelled between } t_{2}=2 \text { and } t_{1}=0}{\text { Time interval }\left(t_{2}-t_{1}\right)} \\
& =\frac{(19.6-0) \mathrm{m}}{(2-0) \mathrm{s}}=9.8 \mathrm{~m} / \mathrm{s} \\
& \text { Similarly, the average velocity between } t=1 \\
& \text { and } t=2 \text { is } \\
& \frac{(19.6-4.9) \mathrm{m}}{(2-1) \mathrm{s}}=14.7 \mathrm{~m} / \mathrm{s}
\end{aligned}
$$

Likewise we compute the average velocitiy between $t=t_{1}$ and $t=2$ for various $t_{1}$. The following Table 13.2 gives the average velocity $(v), t=t_{1}$ seconds and $t=2$ seconds.

Table 12.1

| $t$ | $s$ |
| :--- | :--- |
| 0 | 0 |
| 1 | 4.9 |
| 1.5 | 11.025 |
| 1.8 | 15.876 |
| 1.9 | 17.689 |
| 1.95 | 18.63225 |
| 2 | 19.6 |
| 2.05 | 20.59225 |
| 2.1 | 21.609 |
| 2.2 | 23.716 |
| 2.5 | 30.625 |
| 3 | 44.1 |
| 4 | 78.4 |

Table 12.2

| $t_{1}$ | 0 | 1 | 1.5 | 1.8 | 1.9 | 1.95 | 1.99 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v$ | 9.8 | 14.7 | 17.15 | 18.62 | 19.11 | 19.355 | 19.551 |

From Table 12.2, we observe that the average velocity is gradually increasing. As we make the time intervals ending at $t=2$ smaller, we see that we get a better idea of the velocity at $t=2$. Hoping that nothing really dramatic happens between 1.99 seconds and 2 seconds, we conclude that the average velocity at $t=2$ seconds is just above $19.551 \mathrm{~m} / \mathrm{s}$.

This conclusion is somewhat strengthened by the following set of computation. Compute the average velocities for various time intervals starting at $t=2$ seconds. As before the average velocity $v$ between $t=2$ seconds and $t=t_{2}$ seconds is

$$
\begin{aligned}
& =\frac{\text { Distance travelled between } 2 \text { seconds and } t_{2} \text { seconds }}{t_{2}-2} \\
& =\frac{\text { Distance travelled in } t_{2} \text { seconds }- \text { Distance travelled in } 2 \text { seconds }}{t_{2}-2}
\end{aligned}
$$

$$
=\frac{\text { Distance travelled in } t_{2} \text { seconds }-19.6}{t_{2}-2}
$$

The following Table 12.3 gives the average velocity $v$ in metres per second between $t=2$ seconds and $t_{2}$ seconds.

Table 12.3

| $t_{2}$ | 4 | 3 | 2.5 | 2.2 | 2.1 | 2.05 | 2.01 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $v$ | 29.4 | 24.5 | 22.05 | 20.58 | 20.09 | 19.845 | 19.649 |

Here again we note that if we take smaller time intervals starting at $t=2$, we get better idea of the velocity at $t=2$.

In the first set of computations, what we have done is to find average velocities in increasing time intervals ending at $t=2$ and then hope that nothing dramatic happens just before $t=2$. In the second set of computations, we have found the average velocities decreasing in time intervals ending at $t=2$ and then hope that nothing dramatic happens just after $t=2$. Purely on the physical grounds, both these sequences of average velocities must approach a common limit. We can safely conclude that the velocity of the body at $t=2$ is between $19.551 \mathrm{~m} / \mathrm{s}$ and $19.649 \mathrm{~m} / \mathrm{s}$. Technically, we say that the instantaneous velocity at $t=2$ is between $19.551 \mathrm{~m} / \mathrm{s}$ and $19.649 \mathrm{~m} / \mathrm{s}$. As is well-known, velocity is the rate of change of displacement. Hence what we have accomplished is the following. From the given data of distance covered at various time instants we have estimated the rate of change of the distance at a given instant of time. We say that the derivative of the distance function $s=4.9 t^{2}$ at $t=2$ is between 19.551 and 19.649.

An alternate way of viewing this limiting process is shown in Fig 12.1. This is a plot of distance $s$ of the body from the top of the cliff versus the time $t$ elapsed. In the limit as the sequence of time intervals $h_{1}, h_{2}, \ldots$, approaches zero, the sequence of average velocities approaches the same limit as does the sequence of ratios
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-03.jpg?height=637&width=727&top_left_y=1451&top_left_x=750)

Fig 12.1

$$
\frac{\mathrm{C}_{1} \mathrm{~B}_{1}}{\mathrm{AC}_{1}}, \frac{\mathrm{C}_{2} \mathrm{~B}_{2}}{\mathrm{AC}_{2}}, \frac{\mathrm{C}_{3} \mathrm{~B}_{3}}{\mathrm{AC}_{3}}, \ldots
$$

where $\mathrm{C}_{1} \mathrm{~B}_{1}=s_{1}-s_{0}$ is the distance travelled by the body in the time interval $h_{1}=\mathrm{AC}_{1}$, etc. From the Fig 12.1 it is safe to conclude that this latter sequence approaches the slope of the tangent to the curve at point A . In other words, the instantaneous velocity $v(t)$ of a body at time $t=2$ is equal to the slope of the tangent of the curve $s=4.9 t^{2}$ at $t=2$.

### 12.3 Limits

The above discussion clearly points towards the fact that we need to understand limiting process in greater clarity. We study a few illustrative examples to gain some familiarity with the concept of limits.

Consider the function $f(x)=x^{2}$. Observe that as $x$ takes values very close to 0 , the value of $f(x)$ also moves towards 0 (See Fig 2.10 Chapter 2). We say

$$
\lim _{x \rightarrow 0} f(x)=0
$$

(to be read as limit of $f(x)$ as $x$ tends to zero equals zero). The limit of $f(x)$ as $x$ tends to zero is to be thought of as the value $f(x)$ should assume at $x=0$.

In general as $x \rightarrow a, f(x) \rightarrow l$, then $l$ is called limit of the function $f(x)$ which is symbolically written as $\lim _{x \rightarrow a} f(x)=l$.

Consider the following function $g(x)=|x|, x \neq 0$. Observe that $g(0)$ is not defined. Computing the value of $g(x)$ for values of $x$ very near to 0 , we see that the value of $g(x)$ moves towards 0 . So, $\lim _{x \rightarrow 0} g(x)=0$. This is intuitively clear from the graph of $y=|x|$ for $x \neq 0$. (See Fig 2.13, Chapter 2).

Consider the following function.

$$
h(x)=\frac{x^{2}-4}{x-2}, x \neq 2
$$

Compute the value of $h(x)$ for values of $x$ very near to 2 (but not at 2 ). Convince yourself that all these values are near to 4 . This is somewhat strengthened by considering the graph of the function $y=h(x)$ given here (Fig 12.2).
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-04.jpg?height=632&width=581&top_left_y=1433&top_left_x=890)

Fig 12.2

In all these illustrations the value which the function should assume at a given point $x=a$ did not really depend on how is $x$ tending to $a$. Note that there are essentially two ways $x$ could approach a number $a$ either from left or from right, i.e., all the values of $x$ near $a$ could be less than $a$ or could be greater than $a$. This naturally leads to two limits - the right hand limit and the left hand limit. Right hand limit of a function $f(x)$ is that value of $f(x)$ which is dictated by the values of $f(x)$ when $x$ tends to $a$ from the right. Similarly, the left hand limit. To illustrate this, consider the function

$$
f(x)= \begin{cases}1, & x \leq 0 \\ 2, & x>0\end{cases}
$$

Graph of this function is shown in the Fig 12.3. It is clear that the value of $f$ at 0 dictated by values of $f(x)$ with $x \leq 0$ equals 1 , i.e., the left hand limit of $f(x)$ at 0 is

$$
\lim _{x \rightarrow \overline{0}} f(x)=1
$$

Similarly, the value of $f$ at 0 dictated by values of $f(x)$ with $x>0$ equals 2 , i.e., the right hand limit of $f(x)$ at 0 is

$$
\lim _{x \rightarrow 0^{+}} f(x)=2
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-05.jpg?height=467&width=418&top_left_y=745&top_left_x=1046)

Fig 12.3

In this case the right and left hand limits are different, and hence we say that the limit of $f(x)$ as $x$ tends to zero does not exist (even though the function is defined at 0 ).

## Summary

We say $\lim _{x \rightarrow a^{-}} f(x)$ is the expected value of $f$ at $x=a$ given the values of $f$ near $x$ to the left of $a$. This value is called the left hand limit of $f$ at $a$.

We say $\lim _{x \rightarrow a^{+}} f(x)$ is the expected value of $f$ at $x=a$ given the values of $f$ near $x$ to the right of $a$. This value is called the right hand limit of $f(x)$ at $a$.

If the right and left hand limits coincide, we call that common value as the limit of $f(x)$ at $x=a$ and denote it by $\lim _{x \rightarrow a} f(x)$.

Illustration 1 Consider the function $f(x)=x+10$. We want to find the limit of this function at $x=5$. Let us compute the value of the function $f(x)$ for $x$ very near to 5 . Some of the points near and to the left of 5 are 4.9, 4.95, 4.99, 4.995. . ., etc. Values of the function at these points are tabulated below. Similarly, the real number 5.001,
5.01, 5.1 are also points near and to the right of 5 . Values of the function at these points are also given in the Table 12.4.

Table 12.4

| $x$ | 4.9 | 4.95 | 4.99 | 4.995 | 5.001 | 5.01 | 5.1 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 14.9 | 14.95 | 14.99 | 14.995 | 15.001 | 15.01 | 15.1 |

From the Table 12.4, we deduce that value of $f(x)$ at $x=5$ should be greater than 14.995 and less than 15.001 assuming nothing dramatic happens between $x=4.995$ and 5.001. It is reasonable to assume that the value of the $f(x)$ at $x=5$ as dictated by the numbers to the left of 5 is 15 , i.e.,

$$
\lim _{x \rightarrow 5^{-}} f(x)=15
$$

Similarly, when $x$ approaches 5 from the right, $f(x)$ should be taking value 15, i.e.,

$$
\lim _{x \rightarrow 5^{+}} f(x)=15
$$

Hence, it is likely that the left hand limit of $f(x)$ and the right hand limit of $f(x)$ are both equal to 15 . Thus,

$$
\lim _{x \rightarrow 5^{-}} f(x)=\lim _{x \rightarrow 5^{+}} f(x)=\lim _{x \rightarrow 5} f(x)=15
$$

This conclusion about the limit being equal to 15 is somewhat strengthened by seeing the graph of this function which is given in Fig 2.16, Chapter 2. In this figure, we note that as $x$ approaches 5 from either right or left, the graph of the function $f(x)=x+10$ approaches the point $(5,15)$.

We observe that the value of the function at $x=5$ also happens to be equal to 15 .
Illustration 2 Consider the function $f(x)=x^{3}$. Let us try to find the limit of this function at $x=1$. Proceeding as in the previous case, we tabulate the value of $f(x)$ at $x$ near 1. This is given in the Table 12.5.

Table 12.5

| $x$ | 0.9 | 0.99 | 0.999 | 1.001 | 1.01 | 1.1 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 0.729 | 0.970299 | 0.997002999 | 1.003003001 | 1.030301 | 1.331 |

From this table, we deduce that value of $f(x)$ at $x=1$ should be greater than 0.997002999 and less than 1.003003001 assuming nothing dramatic happens between
$x=0.999$ and 1.001 . It is reasonable to assume that the value of the $f(x)$ at $x=1$ as dictated by the numbers to the left of 1 is 1 , i.e.,

$$
\lim _{x \rightarrow 1^{-}} f(x)=1
$$

Similarly, when $x$ approaches 1 from the right, $f(x)$ should be taking value 1, i.e.,

$$
\lim _{x \rightarrow 1^{+}} f(x)=1
$$

Hence, it is likely that the left hand limit of $f(x)$ and the right hand limit of $f(x)$ are both equal to 1 . Thus,

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1} f(x)=1
$$

This conclusion about the limit being equal to 1 is somewhat strengthened by seeing the graph of this function which is given in Fig 2.11, Chapter 2. In this figure, we note that as $x$ approaches 1 from either right or left, the graph of the function $f(x)=x^{3}$ approaches the point $(1,1)$.

We observe, again, that the value of the function at $x=1$ also happens to be equal to 1 .

Illustration 3 Consider the function $f(x)=3 x$. Let us try to find the limit of this function at $x=2$. The following Table 12.6 is now self-explanatory.

Table 12.6

| $x$ | 1.9 | 1.95 | 1.99 | 1.999 | 2.001 | 2.01 | 2.1 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 5.7 | 5.85 | 5.97 | 5.997 | 6.003 | 6.03 | 6.3 |

As before we observe that as $x$ approaches 2 from either left or right, the value of $f(x)$ seem to approach 6 . We record this as

$$
\lim _{x \rightarrow 2^{-}} f(x)=\lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2} f(x)=6
$$

Its graph shown in Fig 12.4 strengthens this fact.

Here again we note that the value of the function at $x=2$ coincides with the limit at $x=2$.

Illustration 4 Consider the constant function $f(x)=3$. Let us try to find its limit at $x=2$. This function being the constant function takes the same
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-07.jpg?height=578&width=516&top_left_y=1506&top_left_x=953)

Fig 12.4
value ( 3 , in this case) everywhere, i.e., its value at points close to 2 is 3 . Hence

$$
\lim _{x \rightarrow 2} f(x)=\lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2} f(x)=3
$$

Graph of $f(x)=3$ is anyway the line parallel to $x$-axis passing through $(0,3)$ and is shown in Fig 2.9, Chapter 2. From this also it is clear that the required limit is 3 . In fact, it is easily observed that $\lim _{x \rightarrow a} f(x)=3$ for any real number $a$.

Illustration 5 Consider the function $f(x)=x^{2}+x$. We want to find $\lim _{x \rightarrow 1} f(x)$. We tabulate the values of $f(x)$ near $x=1$ in Table 12.7.

Table 12.7

| $x$ | 0.9 | 0.99 | 0.999 | 1.01 | 1.1 | 1.2 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 1.71 | 1.9701 | 1.997001 | 2.0301 | 2.31 | 2.64 |

From this it is reasonable to deduce that
$\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1} f(x)=2$.
From the graph of $f(x)=x^{2}+x$ shown in the Fig 12.5, it is clear that as $x$ approaches 1 , the graph approaches $(1,2)$.

Here, again we observe that the

$$
\lim _{x \rightarrow 1} f(x)=f(1)
$$

Now, convince yourself of the following three facts:
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-08.jpg?height=511&width=674&top_left_y=1115&top_left_x=797)
$\mathbf{Y}^{\prime} \quad$ Fig 12.5

$$
\lim _{x \rightarrow 1} x^{2}=1, \lim _{x \rightarrow 1} x=1 \text { and } \lim _{x \rightarrow 1} x+1=2
$$

Then $\quad \lim _{x \rightarrow 1} x^{2}+\lim _{x \rightarrow 1} x=1+1=2=\lim _{x \rightarrow 1}\left[x^{2}+x\right]$.
Also $\quad \lim _{x \rightarrow 1} x . \lim _{x \rightarrow 1}(x+1)=1.2=2=\lim _{x \rightarrow 1}[x(x+1)]=\lim _{x \rightarrow 1}\left[x^{2}+x\right]$.

Illustration 6 Consider the function $f(x)=\sin x$. We are interested in $\lim _{x \rightarrow \frac{\pi}{2}} \sin x$, where the angle is measured in radians.

Here, we tabulate the (approximate) value of $f(x)$ near $\frac{\pi}{2}$ (Table 12.8). From this, we may deduce that

$$
\lim _{x \rightarrow \frac{\pi^{-}}{2}} f(x)=\lim _{x \rightarrow \frac{\pi^{+}}{2}} f(x)=\lim _{x \rightarrow \frac{\pi}{2}} f(x)=1
$$

Further, this is supported by the graph of $f(x)=\sin x$ which is given in the Fig 3.8 (Chapter 3). In this case too, we observe that $\lim _{x \rightarrow \frac{\pi}{2}} \sin x=1$.

Table 12.8

| $x$ | $\frac{\pi}{2}-0.1$ | $\frac{\pi}{2}-0.01$ | $\frac{\pi}{2}+0.01$ | $\frac{\pi}{2}+0.1$ |
| :--- | :--- | :--- | :--- | :--- |
| $f(x)$ | 0.9950 | 0.9999 | 0.9999 | 0.9950 |

Illustration 7 Consider the function $f(x)=x+\cos x$. We want to find the $\lim _{x \rightarrow 0} f(x)$. Here we tabulate the (approximate) value of $f(x)$ near 0 (Table 12.9).

## Table 12.9

| $x$ | -0.1 | -0.01 | -0.001 | 0.001 | 0.01 | 0.1 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 0.9850 | 0.98995 | 0.9989995 | 1.0009995 | 1.00995 | 1.0950 |

From the Table 13.9, we may deduce that

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0} f(x)=1
$$

In this case too, we observe that $\lim _{x \rightarrow 0} f(x)=f(0)=1$.
Now, can you convince yourself that

$$
\lim _{x \rightarrow 0}[x+\cos x]=\lim _{x \rightarrow 0} x+\lim _{x \rightarrow 0} \cos x \text { is indeed true? }
$$

Illustration 8 Consider the function $f(x)=\frac{1}{x^{2}}$ for $x>0$. We want to know $\lim _{x \rightarrow 0} f(x)$.
Here, observe that the domain of the function is given to be all positive real numbers. Hence, when we tabulate the values of $f(x)$, it does not make sense to talk of $x$ approaching 0 from the left. Below we tabulate the values of the function for positive $x$ close to 0 (in this table $n$ denotes any positive integer).

From the Table 12.10 given below, we see that as $x$ tends to $0, f(x)$ becomes larger and larger. What we mean here is that the value of $f(x)$ may be made larger than any given number.

Table 12.10

| $x$ | 1 | 0.1 | 0.01 | $10^{-n}$ |
| :--- | :--- | :--- | :--- | :--- |
| $f(x)$ | 1 | 100 | 10000 | $10^{2 n}$ |

Mathematically, we say

$$
\lim _{x \rightarrow 0} f(x)=+\infty
$$

We also remark that we will not come across such limits in this course.
Illustration 9 We want to find $\lim _{x \rightarrow 0} f(x)$, where

$$
f(x)= \begin{cases}x-2, & x<0 \\ 0, & x=0 \\ x+2, & x>0\end{cases}
$$

As usual we make a table of $x$ near 0 with $f(x)$. Observe that for negative values of $x$ we need to evaluate $x-2$ and for positive values, we need to evaluate $x+2$.

Table 12.11

| $x$ | -0.1 | -0.01 | -0.001 | 0.001 | 0.01 | 0.1 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | -2.1 | -2.01 | -2.001 | 2.001 | 2.01 | 2.1 |

From the first three entries of the Table 12.11, we deduce that the value of the function is decreasing to -2 and hence.

$$
\lim _{x \rightarrow 0^{-}} f(x)=-2
$$

From the last three entires of the table we deduce that the value of the function is increasing from 2 and hence

$$
\lim _{x \rightarrow 0^{+}} f(x)=2
$$

Since the left and right hand limits at 0 do not coincide, we say that the limit of the function at 0 does not exist.

Graph of this function is given in the Fig12.6. Here, we remark that the value of the function at $x=0$ is well defined and is, indeed, equal to 0 , but the limit of the function at $x=0$ is not even defined.

Illustration 10 As a final illustration, we find $\lim _{x \rightarrow 1} f(x)$,
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-11.jpg?height=414&width=414&top_left_y=380&top_left_x=1057)

Fig 12.6 where

$$
f(x)=\left\{\begin{array}{cc}
x+2 & x \neq 1 \\
0 & x=1
\end{array}\right.
$$

Table 12.12

| $x$ | 0.9 | 0.99 | 0.999 | 1.001 | 1.01 | 1.1 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 2.9 | 2.99 | 2.999 | 3.001 | 3.01 | 3.1 |

As usual we tabulate the values of $f(x)$ for $x$ near 1 . From the values of $f(x)$ for $x$ less than 1 , it seems that the function should take value 3 at $x=1$., i.e.,

$$
\lim _{x \rightarrow 1^{-}} f(x)=3
$$

Similarly, the value of $f(x)$ should be 3 as dictated by values of $f(x)$ at $x$ greater than 1. i.e.

$$
\lim _{x \rightarrow 1^{+}} f(x)=3
$$

But then the left and right hand limits coincide and hence

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1} f(x)=3
$$

Graph of function given in Fig 12.7 strengthens our deduction about the limit. Here, we
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-11.jpg?height=519&width=521&top_left_y=1552&top_left_x=950)

Fig 12.7
note that in general, at a given point the value of the function and its limit may be different (even when both are defined).
12.3.1 Algebra of limits In the above illustrations, we have observed that the limiting process respects addition, subtraction, multiplication and division as long as the limits and functions under consideration are well defined. This is not a coincidence. In fact, below we formalise these as a theorem without proof.

Theorem 1 Let $f$ and $g$ be two functions such that both $\lim _{x \rightarrow a} f(x)$ and $\lim _{x \rightarrow a} g(x)$ exist. Then
(i) Limit of sum of two functions is sum of the limits of the functions, i.e.,

$$
\lim _{x \rightarrow a}[f(x)+g(x)]=\lim _{x \rightarrow a} f(x)+\lim _{x \rightarrow a} g(x) .
$$

(ii) Limit of difference of two functions is difference of the limits of the functions, i.e.,

$$
\lim _{x \rightarrow a}[f(x)-g(x)]=\lim _{x \rightarrow a} f(x)-\lim _{x \rightarrow a} g(x)
$$

(iii) Limit of product of two functions is product of the limits of the functions, i.e.,

$$
\lim _{x \rightarrow a}[f(x) \cdot g(x)]=\lim _{x \rightarrow a} f(x) . \lim _{x \rightarrow a} g(x)
$$

(iv) Limit of quotient of two functions is quotient of the limits of the functions (whenever the denominator is non zero), i.e.,

$$
\lim _{x \rightarrow a} \frac{f(x)}{g(x)}=\frac{\lim _{x \rightarrow a} f(x)}{\lim _{x \rightarrow a} g(x)}
$$

$\square$ Note In particular as a special case of (iii), when $g$ is the constant function such that $g(x)=\lambda$, for some real number $\lambda$, we have

$$
\lim _{x \rightarrow a}[(\lambda \cdot f)(x)]=\lambda \cdot \lim _{x \rightarrow a} f(x) .
$$

In the next two subsections, we illustrate how to exploit this theorem to evaluate limits of special types of functions.
12.3.2 Limits of polynomials and rational functions A function $f$ is said to be a polynomial function of degree $n f(x)=a_{0}+a_{1} x+a_{2} x^{2}+\ldots+a_{n} x^{n}$, where $a_{i} s$ are real numbers such that $a_{n} \neq 0$ for some natural number $n$.

We know that $\lim _{x \rightarrow a} x=a$. Hence

$$
\lim _{x \rightarrow a} x^{2}=\lim _{x \rightarrow a}(x \cdot x)=\lim _{x \rightarrow a} x \cdot \lim _{x \rightarrow a} x=a \cdot a=a^{2}
$$

An easy exercise in induction on $n$ tells us that

$$
\lim _{x \rightarrow a} x^{n}=a^{n}
$$

Now, let $f(x)=a_{0}+a_{1} x+a_{2} x^{2}+\ldots+a_{n} x^{n}$ be a polynomial function. Thinking of each of $a_{0}, a_{1} x, a_{2} x^{2}, \ldots, a_{n} x^{n}$ as a function, we have

$$
\begin{aligned}
\lim _{x \rightarrow a} f(x) & =\lim _{x \rightarrow a}\left[a_{0}+a_{1} x+a_{2} x^{2}+\ldots+a_{n} x^{n}\right] \\
& =\lim _{x \rightarrow a} a_{0}+\lim _{x \rightarrow a} a_{1} x+\lim _{x \rightarrow a} a_{2} x^{2}+\ldots+\lim _{x \rightarrow a} a_{n} x^{n} \\
& =a_{0}+a_{1} \lim _{x \rightarrow a} x+a_{2} \lim _{x \rightarrow a} x^{2}+\ldots+a_{n} \lim _{x \rightarrow a} x^{n} \\
& =a_{0}+a_{1} a+a_{2} a^{2}+\ldots+a_{n} a^{n} \\
& =f(a)
\end{aligned}
$$

(Make sure that you understand the justification for each step in the above!)
A function $f$ is said to be a rational function, if $f(x)=\frac{g(x)}{h(x)}$, where $g(x)$ and $h(x)$ are polynomials such that $h(x) \neq 0$. Then

$$
\lim _{x \rightarrow a} f(x)=\lim _{x \rightarrow a} \frac{g(x)}{h(x)}=\frac{\lim _{x \rightarrow a} g(x)}{\lim _{x \rightarrow a} h(x)}=\frac{g(a)}{h(a)}
$$

However, if $h(a)=0$, there are two scenarios - (i) when $g(a) \neq 0$ and (ii) when $g(a)=0$. In the former case we say that the limit does not exist. In the latter case we can write $g(x)=(x-a)^{k} g_{1}(x)$, where $k$ is the maximum of powers of $(x-a)$ in $g(x)$ Similarly, $h(x)=(x-a)^{l} h_{1}(x)$ as $h(a)=0$. Now, if $k>l$, we have

$$
\lim _{x \rightarrow a} f(x)=\frac{\lim _{x \rightarrow a} g(x)}{\lim _{x \rightarrow a} h(x)}=\frac{\lim _{x \rightarrow a}(x-a)^{k} g_{1}(x)}{\lim _{x \rightarrow a}(x-a)^{l} h_{1}(x)}
$$

$$
=\frac{\lim _{x \rightarrow a}(x-a)^{(k-l)} g_{1}(x)}{\lim _{x \rightarrow a} h_{1}(x)}=\frac{0 \cdot g_{1}(a)}{h_{1}(a)}=0
$$

If $k<l$, the limit is not defined.
Example 1 Find the limits: (i) $\lim _{x \rightarrow 1}\left[x^{3}-x^{2}+1\right] \quad$ (ii) $\lim _{x \rightarrow 3}[x(x+1)]$
(iii) $\lim _{x \rightarrow-1}\left[1+x+x^{2}+\ldots+x^{10}\right]$.

Solution The required limits are all limits of some polynomial functions. Hence the limits are the values of the function at the prescribed points. We have
(i) $\lim _{x \rightarrow 1}\left[x^{3}-x^{2}+1\right]=1^{3}-1^{2}+1=1$
(ii) $\lim _{x \rightarrow 3}[x(x+1)]=3(3+1)=3(4)=12$
(iii) $\lim _{x \rightarrow-1}\left[1+x+x^{2}+\ldots+x^{10}\right]=1+(-1)+(-1)^{2}+\ldots+(-1)^{10}$ $=1-1+1 \ldots+1=1$.
Example 2 Find the limits:
(i) $\lim _{x \rightarrow 1}\left[\frac{x^{2}+1}{x+100}\right]$
(ii) $\lim _{x \rightarrow 2}\left[\frac{x^{3}-4 x^{2}+4 x}{x^{2}-4}\right]$
(iii) $\lim _{x \rightarrow 2}\left[\frac{x^{2}-4}{x^{3}-4 x^{2}+4 x}\right]$
(iv) $\lim _{x \rightarrow 2}\left[\frac{x^{3}-2 x^{2}}{x^{2}-5 x+6}\right]$
(v) $\lim _{x \rightarrow 1}\left[\frac{x-2}{x^{2}-x}-\frac{1}{x^{3}-3 x^{2}+2 x}\right]$.

Solution All the functions under consideration are rational functions. Hence, we first evaluate these functions at the prescribed points. If this is of the form $\frac{0}{0}$, we try to rewrite the function cancelling the factors which are causing the limit to be of the form $\frac{0}{0}$.
(i) We have $\lim _{x \rightarrow 1} \frac{x^{2}+1}{x+100}=\frac{1^{2}+1}{1+100}=\frac{2}{101}$
(ii) Evaluating the function at 2 , it is of the form $\frac{0}{0}$.

Hence $\lim _{x \rightarrow 2} \frac{x^{3}-4 x^{2}+4 x}{x^{2}-4}=\lim _{x \rightarrow 2} \frac{x(x-2)^{2}}{(x+2)(x-2)}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 2} \frac{x(x-2)}{(x+2)} \quad \text { as } x \neq 2 \\
& =\frac{2(2-2)}{2+2}=\frac{0}{4}=0
\end{aligned}
$$

(iii) Evaluating the function at 2 , we get it of the form $\frac{0}{0}$.

Hence $\lim _{x \rightarrow 2} \frac{x^{2}-4}{x^{3}-4 x^{2}+4 x}=\lim _{x \rightarrow 2} \frac{(x+2)(x-2)}{x(x-2)^{2}}$

$$
=\lim _{x \rightarrow 2} \frac{(x+2)}{x(x-2)}=\frac{2+2}{2(2-2)}=\frac{4}{0}
$$

which is not defined.
(iv) Evaluating the function at 2 , we get it of the form $\frac{0}{0}$.

Hence $\quad \lim _{x \rightarrow 2} \frac{x^{3}-2 x^{2}}{x^{2}-5 x+6}=\lim _{x \rightarrow 2} \frac{x^{2}(x-2)}{(x-2)(x-3)}$

$$
=\lim _{x \rightarrow 2} \frac{x^{2}}{(x-3)}=\frac{(2)^{2}}{2-3}=\frac{4}{-1}=-4
$$

(v) First, we rewrite the function as a rational function.

$$
\begin{aligned}
{\left[\frac{x-2}{x^{2}-x}-\frac{1}{x^{3}-3 x^{2}+2 x}\right] } & =\left[\frac{x-2}{x(x-1)}-\frac{1}{x\left(x^{2}-3 x+2\right)}\right] \\
& =\left[\frac{x-2}{x(x-1)}-\frac{1}{x(x-1)(x-2)}\right] \\
& =\left[\frac{x^{2}-4 x+4-1}{x(x-1)(x-2)}\right] \\
& =\frac{x^{2}-4 x+3}{x(x-1)(x-2)}
\end{aligned}
$$

Evaluating the function at 1 , we get it of the form $\frac{0}{0}$.
Hence $\quad \lim _{x \rightarrow 1}\left[\frac{x^{2}-2}{x^{2}-x}-\frac{1}{x^{3}-3 x^{2}+2 x}\right]=\lim _{x \rightarrow 1} \frac{x^{2}-4 x+3}{x(x-1)(x-2)}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 1} \frac{(x-3)(x-1)}{x(x-1)(x-2)} \\
& =\lim _{x \rightarrow 1} \frac{x-3}{x(x-2)}=\frac{1-3}{1(1-2)}=2
\end{aligned}
$$

We remark that we could cancel the term $(x-1)$ in the above evaluation because $x \neq 1$.

Evaluation of an important limit which will be used in the sequel is given as a theorem below.
Theorem 2 For any positive integer $n$,

$$
\lim _{x \rightarrow a} \frac{x^{n}-a^{n}}{x-a}=n a^{n-1}
$$

Remark The expression in the above theorem for the limit is true even if $n$ is any rational number and $a$ is positive.

Proof Dividing $\left(x^{n}-a^{n}\right)$ by $(x-a)$, we see that

$$
x^{n}-a^{n}=(x-a)\left(x^{n-1}+x^{n-2} a+x^{n-3} a^{2}+\ldots+x a^{n-2}+a^{n-1}\right)
$$

Thus, $\lim _{x \rightarrow a} \frac{x^{n}-a^{n}}{x-a}=\lim _{x \rightarrow a}\left(x^{n-1}+x^{n-2} a+x^{n-3} a^{2}+\ldots+x a^{n-2}+a^{n-1}\right)$

$$
\begin{aligned}
& =a^{n-1}+a a^{n-2}+\ldots+a^{n-2}(a)+a^{n-1} \\
& =a^{n-1}+a^{n-1}+\ldots+a^{n-1}+a^{n-1}(n \text { terms }) \\
& =n a^{n-1}
\end{aligned}
$$

## Example 3 Evaluate:

(i) $\lim _{x \rightarrow 1} \frac{x^{15}-1}{x^{10}-1}$
(ii) $\lim _{x \rightarrow 0} \frac{\sqrt{1+x}-1}{x}$

Solution (i) We have

$$
\begin{aligned}
\lim _{x \rightarrow 1} \frac{x^{15}-1}{x^{10}-1} & =\lim _{x \rightarrow 1}\left[\frac{x^{15}-1}{x-1} \div \frac{x^{10}-1}{x-1}\right] \\
& =\lim _{x \rightarrow 1}\left[\frac{x^{15}-1}{x-1}\right] \div \lim _{x \rightarrow 1}\left[\frac{x^{10}-1}{x-1}\right] \\
& =15(1)^{14} \div 10(1)^{9} \text { (by the theorem above) } \\
& =15 \div 10=\frac{3}{2}
\end{aligned}
$$

(ii) Put $y=1+x$, so that $y \rightarrow 1$ as $x \rightarrow 0$.

Then $\quad \lim _{x \rightarrow 0} \frac{\sqrt{1+x}-1}{x}=\lim _{y \rightarrow 1} \frac{\sqrt{y}-1}{y-1}$

$$
\begin{aligned}
& =\lim _{y \rightarrow 1} \frac{y^{\frac{1}{2}}-1^{\frac{1}{2}}}{y-1} \\
& =\frac{1}{2}(1)^{\frac{1}{2}-1}(\text { by the remark above })=\frac{1}{2}
\end{aligned}
$$

### 12.4 Limits of Trigonometric Functions

The following facts (stated as theorems) about functions in general come in handy in calculating limits of some trigonometric functions.

Theorem 3 Let $f$ and $g$ be two real valued functions with the same domain such that $f(x) \leq \mathrm{g}(x)$ for all $x$ in the domain of definition, For some $a$, if both $\lim _{x \rightarrow a} f(x)$ and $\lim _{x \rightarrow a} g(x)$ exist, then $\lim _{x \rightarrow a} f(x) \leq \lim _{x \rightarrow a} g(x)$. This is illustrated in Fig 12.8.
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-18.jpg?height=407&width=578&top_left_y=743&top_left_x=523)

Fig 12.8
Theorem 4 (Sandwich Theorem) Let $f, \mathrm{~g}$ and $h$ be real functions such that $f(x) \leq g(x) \leq h(x)$ for all $x$ in the common domain of definition. For some real number $a$, if $\lim _{x \rightarrow a} f(x)=l=\lim _{x \rightarrow a} h(x)$, then $\lim _{x \rightarrow a} g(x)=l$. This is illustrated in Fig 12.9.
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-18.jpg?height=476&width=669&top_left_y=1395&top_left_x=473)

Given below is a beautiful geometric proof of the following important inequality relating trigonometric functions.

$$
\begin{equation*}
\cos x<\frac{\sin x}{x}<1 \quad \text { for } 0<|x|<\frac{\pi}{2} \tag{*}
\end{equation*}
$$

Proof We know that $\sin (-x)=-\sin x$ and $\cos (-x)=\cos x$. Hence, it is sufficient to prove the inequality for $0<x<\frac{\pi}{2}$.

In the Fig 12.10, O is the centre of the unit circle such that the angle AOC is $x$ radians and $0<x<\frac{\pi}{2}$. Line segments BA and CD are perpendiculars to OA . Further, join AC . Then

Area of $\triangle \mathrm{OAC}<$ Area of sector $\mathrm{OAC}<$ Area of $\triangle \mathrm{OAB}$.
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-19.jpg?height=333&width=293&top_left_y=390&top_left_x=1178)

Fig 12.10
i.e., $\quad \frac{1}{2} \mathrm{OA} \cdot \mathrm{CD}<\frac{x}{2 \pi} \cdot \pi \cdot(\mathrm{OA})^{2}<\frac{1}{2} \mathrm{OA} \cdot \mathrm{AB}$.
i.e., $\quad \mathrm{CD}<x . \mathrm{OA}<\mathrm{AB}$.

From $\triangle \mathrm{OCD}$,

$$
\sin x=\frac{\mathrm{CD}}{\mathrm{OA}}(\text { since } \mathrm{OC}=\mathrm{OA}) \text { and hence } \mathrm{CD}=\mathrm{OA} \sin x . \text { Also } \tan x=\frac{\mathrm{AB}}{\mathrm{OA}} \text { and }
$$

hence $\quad \mathrm{AB}=\mathrm{OA} \cdot \tan x$. Thus

$$
\mathrm{OA} \sin x<\mathrm{OA} . x<\mathrm{OA} . \tan x .
$$

Since length OA is positive, we have

$$
\sin x<x<\tan x .
$$

Since $0<x<\frac{\pi}{2}, \sin x$ is positive and thus by dividing throughout by $\sin x$, we have $1<\frac{x}{\sin x}<\frac{1}{\cos x}$. Taking reciprocals throughout, we have

$$
\cos x<\frac{\sin x}{x}<1
$$

which complete the proof.
Theorem 5 The following are two important limits.
(i) $\lim _{x \rightarrow 0} \frac{\sin x}{x}=1$.
(ii) $\lim _{x \rightarrow 0} \frac{1-\cos x}{x}=0$.

Proof (i) The inequality in (*) says that the function $\frac{\sin x}{x}$ is sandwiched between the function $\cos x$ and the constant function which takes value 1 .

Further, since $\lim _{x \rightarrow 0} \cos x=1$, we see that the proof of (i) of the theorem is complete by sandwich theorem.

To prove (ii), we recall the trigonometric identity $1-\cos x=2 \sin ^{2}\left(\frac{x}{2}\right)$.
Then

$$
\begin{aligned}
\lim _{x \rightarrow 0} \frac{1-\cos x}{x} & =\lim _{x \rightarrow 0} \frac{2 \sin ^{2}\left(\frac{x}{2}\right)}{x}=\lim _{x \rightarrow 0} \frac{\sin \left(\frac{x}{2}\right)}{\frac{x}{2}} \cdot \sin \left(\frac{x}{2}\right) \\
& =\lim _{x \rightarrow 0} \frac{\sin \left(\frac{x}{2}\right)}{\frac{x}{2}} \cdot \lim _{x \rightarrow 0} \sin \left(\frac{x}{2}\right)=1 \cdot 0=0
\end{aligned}
$$

Observe that we have implicitly used the fact that $x \rightarrow 0$ is equivalent to $\frac{x}{2} \rightarrow 0$. This may be justified by putting $y=\frac{x}{2}$.

Example 4 Evaluate:

$$
\text { (i) } \lim _{x \rightarrow 0} \frac{\sin 4 x}{\sin 2 x} \quad \text { (ii) } \lim _{x \rightarrow 0} \frac{\tan x}{x}
$$

Solution (i) $\lim _{x \rightarrow 0} \frac{\sin 4 x}{\sin 2 x}=\lim _{x \rightarrow 0}\left[\frac{\sin 4 x}{4 x} \cdot \frac{2 x}{\sin 2 x} \cdot 2\right]$

$$
\begin{aligned}
& =2 \cdot \lim _{x \rightarrow 0}\left[\frac{\sin 4 x}{4 x}\right] \div\left[\frac{\sin 2 x}{2 x}\right] \\
& =2 \cdot \lim _{4 x \rightarrow 0}\left[\frac{\sin 4 x}{4 x}\right] \div \lim _{2 x \rightarrow 0}\left[\frac{\sin 2 x}{2 x}\right] \\
& =2 \cdot 1 \cdot 1=2(\text { as } x \rightarrow 0,4 x \rightarrow 0 \text { and } 2 x \rightarrow 0)
\end{aligned}
$$

(ii) We have $\lim _{x \rightarrow 0} \frac{\tan x}{x}=\lim _{x \rightarrow 0} \frac{\sin x}{x \cos x}=\lim _{x \rightarrow 0} \frac{\sin x}{x} \cdot \lim _{x \rightarrow 0} \frac{1}{\cos x}=1.1=1$

A general rule that needs to be kept in mind while evaluating limits is the following.
Say, given that the limit $\lim _{x \rightarrow a} \frac{f(x)}{g(x)}$ exists and we want to evaluate this. First we check the value of $f(a)$ and $g(a)$. If both are 0 , then we see if we can get the factor which is causing the terms to vanish, i.e., see if we can write $f(x)=f_{1}(x) f_{2}(x)$ so that $f_{1}(a)=0$ and $f_{2}(a) \neq 0$. Similarly, we write $g(x)=g_{1}(x) g_{2}(x)$, where $g_{1}(a)=0$ and $g_{2}(a) \neq 0$. Cancel out the common factors from $f(x)$ and $g(x)$ (if possible) and write

$$
\frac{f(x)}{g(x)}=\frac{p(x)}{q(x)}, \text { where } q(x) \neq 0
$$

Then

$$
\lim _{x \rightarrow a} \frac{f(x)}{g(x)}=\frac{p(a)}{q(a)}
$$

## EXERCISE 12.1

Evaluate the following limits in Exercises 1 to 22.

1. $\lim _{x \rightarrow 3} x+3$
2. $\lim _{x \rightarrow \pi}\left(x-\frac{22}{7}\right)$
3. $\lim _{r \rightarrow 1} \pi r^{2}$
4. $\lim _{x \rightarrow 4} \frac{4 x+3}{x-2}$
5. $\lim _{x \rightarrow-1} \frac{x^{10}+x^{5}+1}{x-1}$
6. $\lim _{x \rightarrow 0} \frac{(x+1)^{5}-1}{x}$
7. $\lim _{x \rightarrow 2} \frac{3 x^{2}-x-10}{x^{2}-4}$
8. $\lim _{x \rightarrow 3} \frac{x^{4}-81}{2 x^{2}-5 x-3}$
9. $\lim _{x \rightarrow 0} \frac{a x+b}{c x+1}$
10. $\lim _{z \rightarrow 1} \frac{z^{\frac{1}{3}}-1}{z^{\frac{1}{6}}-1}$
11. $\lim _{x \rightarrow 1} \frac{a x^{2}+b x+c}{c x^{2}+b x+a}, a+b+c \neq 0$
12. $\lim _{x \rightarrow-2} \frac{\frac{1}{x}+\frac{1}{2}}{x+2}$
13. $\lim _{x \rightarrow 0} \frac{\sin a x}{b x}$
14. $\lim _{x \rightarrow 0} \frac{\sin a x}{\sin b x}, a, b \neq 0$
15. $\lim _{x \rightarrow \pi} \frac{\sin (\pi-x)}{\pi(\pi-x)}$
16. $\lim _{x \rightarrow 0} \frac{\cos x}{\pi-x}$
17. $\lim _{x \rightarrow 0} \frac{\cos 2 x-1}{\cos x-1}$
18. $\lim _{x \rightarrow 0} \frac{a x+x \cos x}{b \sin x}$
19. $\lim _{x \rightarrow 0} x \sec x$
20. $\lim _{x \rightarrow 0} \frac{\sin a x+b x}{a x+\sin b x} a, b, a+b \neq 0$,
21. $\lim _{x \rightarrow 0}(\operatorname{cosec} x-\cot x)$
22. $\lim _{x \rightarrow \frac{\pi}{2}} \frac{\tan 2 x}{x-\frac{\pi}{2}}$
23. Find $\lim _{x \rightarrow 0} f(x)$ and $\lim _{x \rightarrow 1} f(x)$, where $f(x)=\left\{\begin{array}{cc}2 x+3, & x \leq 0 \\ 3(x+1), & x>0\end{array}\right.$
24. Find $\lim _{x \rightarrow 1} f(x)$, where $f(x)= \begin{cases}x^{2}-1, & x \leq 1 \\ -x^{2}-1, & x>1\end{cases}$
25. Evaluate $\lim _{x \rightarrow 0} f(x)$, where $f(x)= \begin{cases}\frac{|x|}{x}, & x \neq 0 \\ 0, & x=0\end{cases}$
26. Find $\lim _{x \rightarrow 0} f(x)$, where $f(x)=\left\{\begin{array}{cc}\frac{x}{|x|}, & x \neq 0 \\ 0, & x=0\end{array}\right.$
27. Find $\lim _{x \rightarrow 5} f(x)$, where $f(x)=|x|-5$
28. Suppose $f(x)= \begin{cases}a+b x, & x<1 \\ 4, & x=1 \\ b-a x, & x>1\end{cases}$
and if $\lim _{x \rightarrow 1} f(x)=f(1)$ what are possible values of $a$ and $b$ ?
29. Let $a_{1}, a_{2}, \ldots, a_{n}$ be fixed real numbers and define a function $f(x)=\left(x-a_{1}\right)\left(x-a_{2}\right) \ldots\left(x-a_{n}\right)$.

What is $\lim _{x \rightarrow a_{1}} f(x)$ ? For some $a \neq a_{1}, a_{2}, \ldots, a_{n}$, compute $\lim _{x \rightarrow a} f(x)$.
30. If $f(x)=\left\{\begin{array}{ll}|x|+1, & x<0 \\ 0, & x=0 \\ |x|-1, & x>0\end{array}\right.$.

For what value (s) of $a$ does $\lim _{x \rightarrow a} f(x)$ exists?
31. If the function $f(x)$ satisfies $\lim _{x \rightarrow 1} \frac{f(x)-2}{x^{2}-1}=\pi$, evaluate $\lim _{x \rightarrow 1} f(x)$.
32. If $f(x)=\left\{\begin{array}{lc}m x^{2}+n, & x<0 \\ n x+m, & 0 \leq x \leq 1 \\ n x^{3}+m, & x>1\end{array}\right.$. For what integers $m$ and $n$ does both $\lim _{x \rightarrow 0} f(x)$
and $\lim _{x \rightarrow 1} f(x)$ exist?

### 12.5 Derivatives

We have seen in the Section 13.2, that by knowing the position of a body at various time intervals it is possible to find the rate at which the position of the body is changing. It is of very general interest to know a certain parameter at various instants of time and try to finding the rate at which it is changing. There are several real life situations where such a process needs to be carried out. For instance, people maintaining a reservoir need to know when will a reservoir overflow knowing the depth of the water at several instances of time, Rocket Scientists need to compute the precise velocity with which the satellite needs to be shot out from the rocket knowing the height of the rocket at various times. Financial institutions need to predict the changes in the value of a particular stock knowing its present value. In these, and many such cases it is desirable to know how a particular parameter is changing with respect to some other parameter. The heart of the matter is derivative of a function at a given point in its domain of definition.

Definition 1 Suppose $f$ is a real valued function and $a$ is a point in its domain of definition. The derivative of $f$ at $a$ is defined by

$$
\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}
$$

provided this limit exists. Derivative of $f(x)$ at $a$ is denoted by $f^{\prime}(a)$.
Observe that $f^{\prime}(a)$ quantifies the change in $f(x)$ at $a$ with respect to $x$.
Example 5 Find the derivative at $x=2$ of the function $f(x)=3 x$.
Solution We have

$$
\begin{aligned}
f^{\prime}(2) & =\lim _{h \rightarrow 0} \frac{f(2+h)-f(2)}{h}=\lim _{h \rightarrow 0} \frac{3(2+h)-3(2)}{h} \\
& =\lim _{h \rightarrow 0} \frac{6+3 h-6}{h}=\lim _{h \rightarrow 0} \frac{3 h}{h}=\lim _{h \rightarrow 0} 3=3
\end{aligned}
$$

The derivative of the function $3 x$ at $x=2$ is 3 .
Example 6 Find the derivative of the function $f(x)=2 x^{2}+3 x-5$ at $x=-1$. Also prove that $f^{\prime}(0)+3 f^{\prime}(-1)=0$.

Solution We first find the derivatives of $f(x)$ at $x=-1$ and at $x=0$. We have

$$
\begin{aligned}
f^{\prime}(-1) & =\lim _{h \rightarrow 0} \frac{f(-1+h)-f(-1)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\left[2(-1+h)^{2}+3(-1+h)-5\right]-\left[2(-1)^{2}+3(-1)-5\right]}{h} \\
& =\lim _{h \rightarrow 0} \frac{2 h^{2}-h}{h}=\lim _{h \rightarrow 0}(2 h-1)=2(0)-1=-1
\end{aligned}
$$

and

$$
\begin{aligned}
f^{\prime}(0) & =\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\left[2(0+h)^{2}+3(0+h)-5\right]-\left[2(0)^{2}+3(0)-5\right]}{h}
\end{aligned}
$$

$$
=\lim _{h \rightarrow 0} \frac{2 h^{2}+3 h}{h}=\lim _{h \rightarrow 0}(2 h+3)=2(0)+3=3
$$

Clearly

$$
f^{\prime}(0)+3 f^{\prime}(-1)=0
$$

Remark At this stage note that evaluating derivative at a point involves effective use of various rules, limits are subjected to. The following illustrates this.
Example 7 Find the derivative of $\sin x$ at $x=0$.
Solution Let $f(x)=\sin x$. Then

$$
\begin{aligned}
f^{\prime}(0) & =\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\sin (0+h)-\sin (0)}{h}=\lim _{h \rightarrow 0} \frac{\sin h}{h}=1
\end{aligned}
$$

Example 8 Find the derivative of $f(x)=3$ at $x=0$ and at $x=3$.
Solution Since the derivative measures the change in function, intuitively it is clear that the derivative of the constant function must be zero at every point. This is indeed, supported by the following computation.

$$
f^{\prime}(0)=\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h}=\lim _{h \rightarrow 0} \frac{3-3}{h}=\lim _{h \rightarrow 0} \frac{0}{h}=0 .
$$

Similarly $\quad f^{\prime}(3)=\lim _{h \rightarrow 0} \frac{f(3+h)-f(3)}{h}=\lim _{h \rightarrow 0} \frac{3-3}{h}=0$.
We now present a geometric interpretation of derivative of a function at a point. Let $y=f(x)$ be a function and let $\mathrm{P}=(a, f(a))$ and $\mathrm{Q}=(a+h, f(a+h)$ be two points close to each other on the graph of this function. The Fig 12.11 is now self explanatory.
![](https://cdn.mathpix.com/cropped/2025_07_21_661978838205d593f2f3g-25.jpg?height=565&width=778&top_left_y=1559&top_left_x=692)

We know that $f^{\prime}(a)=\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}$
From the triangle PQR , it is clear that the ratio whose limit we are taking is precisely equal to $\tan (\mathrm{QPR})$ which is the slope of the chord PQ . In the limiting process, as $h$ tends to 0 , the point Q tends to P and we have

$$
\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}=\lim _{\mathrm{Q} \rightarrow \mathrm{P}} \frac{\mathrm{QR}}{\mathrm{PR}}
$$

This is equivalent to the fact that the chord PQ tends to the tangent at P of the curve $y=f(x)$. Thus the limit turns out to be equal to the slope of the tangent. Hence

$$
f^{\prime}(a)=\tan \psi
$$

For a given function $f$ we can find the derivative at every point. If the derivative exists at every point, it defines a new function called the derivative of $f$. Formally, we define derivative of a function as follows.

Definition 2 Suppose $f$ is a real valued function, the function defined by

$$
\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}
$$

wherever the limit exists is defined to be the derivative of $f$ at $x$ and is denoted by $f^{\prime}(x)$. This definition of derivative is also called the first principle of derivative.
Thus $\quad f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$
Clearly the domain of definition of $f^{\prime}(x)$ is wherever the above limit exists. There are different notations for derivative of a function. Sometimes $f^{\prime}(x)$ is denoted by $\frac{d}{d x}(f(x))$ or if $y=f(x)$, it is denoted by $\frac{d y}{d x}$. This is referred to as derivative of $f(x)$ or $y$ with respect to $x$. It is also denoted by $\mathrm{D}(f(x))$. Further, derivative of $f$ at $x=a$ is also denoted by $\left.\frac{d}{d x} f(x)\right|_{a}$ or $\left.\frac{d f}{d x}\right|_{a}$ or even $\left(\frac{d f}{d x}\right)_{x=a}$.

Example 9 Find the derivative of $f(x)=10 x$.
Solution Since $f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$

$$
\begin{aligned}
& =\lim _{h \rightarrow 0} \frac{10(x+h)-10(x)}{h} \\
& =\lim _{h \rightarrow 0} \frac{10 h}{h}=\lim _{h \rightarrow 0}(10)=10
\end{aligned}
$$

Example 10 Find the derivative of $f(x)=x^{2}$.
Solution We have, $f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$

$$
=\lim _{h \rightarrow 0} \frac{(x+h)^{2}-(x)^{2}}{h}=\lim _{h \rightarrow 0}(h+2 x)=2 x
$$

Example 11 Find the derivative of the constant function $f(x)=a$ for a fixed real number $a$.

Solution We have, $f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$

$$
=\lim _{h \rightarrow 0} \frac{a-a}{h}=\lim _{h \rightarrow 0} \frac{0}{h}=0 \text { as } h \neq 0
$$

Example 12 Find the derivative of $f(x)=\frac{1}{x}$
Solution We have $f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$

$$
\begin{aligned}
& =\lim _{h \rightarrow 0} \frac{\frac{1}{(x+h)}-\frac{1}{x}}{h} \\
& =\lim _{h \rightarrow 0} \frac{1}{h}\left[\frac{x-(x+h)}{x(x+h)}\right] \\
& =\lim _{h \rightarrow 0} \frac{1}{h}\left[\frac{-h}{x(x+h)}\right] \quad=\lim _{h \rightarrow 0} \frac{-1}{x(x+h)}=-\frac{1}{x^{2}}
\end{aligned}
$$

12.5.1 Algebra of derivative of functions Since the very definition of derivatives involve limits in a rather direct fashion, we expect the rules for derivatives to follow closely that of limits. We collect these in the following theorem.
Theorem 5 Let $f$ and $g$ be two functions such that their derivatives are defined in a common domain. Then
(i) Derivative of sum of two functions is sum of the derivatives of the functions.

$$
\frac{d}{d x}[f(x)+g(x)]=\frac{d}{d x} f(x)+\frac{d}{d x} g(x)
$$

(ii) Derivative of difference of two functions is difference of the derivatives of the functions.

$$
\frac{d}{d x}[f(x)-g(x)]=\frac{d}{d x} f(x)-\frac{d}{d x} g(x)
$$

(iii) Derivative of product of two functions is given by the following product rule.

$$
\frac{d}{d x}[f(x) \cdot g(x)]=\frac{d}{d x} f(x) \cdot g(x)+f(x) \cdot \frac{d}{d x} g(x)
$$

(iv) Derivative of quotient of two functions is given by the following quotient rule (whenever the denominator is non-zero).

$$
\frac{d}{d x}\left(\frac{f(x)}{g(x)}\right)=\frac{\frac{d}{d x} f(x) \cdot g(x)-f(x) \frac{d}{d x} g(x)}{(g(x))^{2}}
$$

The proofs of these follow essentially from the analogous theorem for limits. We will not prove these here. As in the case of limits this theorem tells us how to compute derivatives of special types of functions. The last two statements in the theorem may be restated in the following fashion which aids in recalling them easily:

Let $u=f(x)$ and $v=g(x)$. Then

$$
(u v)^{\prime}=u^{\prime} v+u v^{\prime}
$$

This is referred to a Leibnitz rule for differentiating product of functions or the product rule. Similarly, the quotient rule is

$$
\left(\frac{u}{v}\right)^{\prime}=\frac{u^{\prime} v-u v^{\prime}}{v^{2}}
$$

Now, let us tackle derivatives of some standard functions.
It is easy to see that the derivative of the function $f(x)=x$ is the constant function 1 . This is because $f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{x+h-x}{h}$

$$
=\lim _{h \rightarrow 0} 1=1
$$

We use this and the above theorem to compute the derivative of $f(x)=10 x=x+\ldots .+x$ (ten terms). By (i) of the above theorem

$$
\begin{aligned}
\frac{d f(x)}{d x} & =\frac{d}{d x}(x+\ldots+x)(\text { ten terms }) \\
& =\frac{d}{d x} x+\ldots+\frac{d}{d x} x \quad(\text { ten terms }) \\
& =1+\ldots+1(\text { ten terms })=10
\end{aligned}
$$

We note that this limit may be evaluated using product rule too. Write $f(x)=10 x=u v$, where $u$ is the constant function taking value 10 everywhere and $v(x)=x$. Here, $f(x)=10 x=u v$ we know that the derivative of $u$ equals 0 . Also derivative of $v(x)=x$ equals 1 . Thus by the product rule we have

$$
f^{\prime}(x)=(10 x)^{\prime}=(u v)^{\prime}=u^{\prime} v+u v^{\prime}=0 . x+10.1=10
$$

On similar lines the derivative of $f(x)=x^{2}$ may be evaluated. We have $f(x)=x^{2}=x . x$ and hence

$$
\begin{aligned}
\frac{d f}{d x} & =\frac{d}{d x}(x \cdot x)=\frac{d}{d x}(x) \cdot x+x \cdot \frac{d}{d x}(x) \\
& =1 \cdot x+x \cdot 1=2 x
\end{aligned}
$$

More generally, we have the following theorem.
Theorem 6 Derivative of $f(x)=x^{n}$ is $n x^{n-1}$ for any positive integer $n$.
Proof By definition of the derivative function, we have

$$
f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{(x+h)^{n}-x^{n}}{h}
$$

Binomial theorem tells that $(x+h)^{n}=\left({ }^{n} \mathrm{C}_{0}\right) x^{n}+\left({ }^{n} \mathrm{C}_{1}\right) x^{n-1} h+\ldots+\left({ }^{n} \mathrm{C}_{n}\right) h^{n}$ and hence $(x+h)^{n}-x^{n}=h\left(n x^{n-1}+\ldots+h^{n-1}\right)$. Thus

$$
\begin{aligned}
\frac{d f(x)}{d x} & =\lim _{h \rightarrow 0} \frac{(x+h)^{n}-x^{n}}{h} \\
& =\lim _{h \rightarrow 0} \frac{h\left(n x^{n-1}+\ldots+h^{n-1}\right)}{h} \\
& =\lim _{h \rightarrow 0}\left(n x^{n-1}+\ldots+h^{n-1}\right)=n x^{n-1}
\end{aligned}
$$

Alternatively, we may also prove this by induction on $n$ and the product rule as follows. The result is true for $n=1$, which has been proved earlier. We have

$$
\begin{aligned}
\frac{d}{d x}\left(x^{n}\right) & =\frac{d}{d x}\left(x \cdot x^{n-1}\right) \\
& =\frac{d}{d x}(x) \cdot\left(x^{n-1}\right)+x \cdot \frac{d}{d x}\left(x^{n-1}\right)(\text { by product rule }) \\
& =1 \cdot x^{n-1}+x \cdot\left((n-1) x^{n-2}\right)(\text { by induction hypothesis }) \\
& =x^{n-1}+(n-1) x^{n-1}=n x^{n-1}
\end{aligned}
$$

Remark The above theorem is true for all powers of $x$, i.e., $n$ can be any real number (but we will not prove it here).
12.5.2 Derivative of polynomials and trigonometric functions We start with the following theorem which tells us the derivative of a polynomial function.

Theorem 7 Let $f(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\ldots .+a_{1} x+a_{0}$ be a polynomial function, where $a_{i} s$ are all real numbers and $a_{n} \neq 0$. Then, the derivative function is given by

$$
\frac{d f(x)}{d x}=n a_{n} x^{n-1}+(n-1) a_{n-1} x^{x-2}+\ldots+2 a_{2} x+a_{1}
$$

Proof of this theorem is just putting together part (i) of Theorem 5 and Theorem 6.
Example 13 Compute the derivative of $6 x^{100}-x^{55}+x$.
Solution A direct application of the above theorem tells that the derivative of the above function is $600 x^{99}-55 x^{54}+1$.

Example 14 Find the derivative of $f(x)=1+x+x^{2}+x^{3}+\ldots+x^{50}$ at $x=1$.
Solution A direct application of the above Theorem 6 tells that the derivative of the above function is $1+2 x+3 x^{2}+\ldots+50 x^{49}$. At $x=1$ the value of this function equals
$1+2(1)+3(1)^{2}+\ldots+50(1)^{49}=1+2+3+\ldots+50=\frac{(50)(51)}{2}=1275$.
Example 15 Find the derivative of $f(x)=\frac{x+1}{x}$
Solution Clearly this function is defined everywhere except at $x=0$. We use the quotient rule with $u=x+1$ and $v=x$. Hence $u^{\prime}=1$ and $v^{\prime}=1$. Therefore

$$
\frac{d f(x)}{d x}=\frac{d}{d x}\left(\frac{x+1}{x}\right)=\frac{d}{d x}\left(\frac{u}{v}\right)=\frac{u^{\prime} v-u v^{\prime}}{v^{2}}=\frac{1(x)-(x+1) 1}{x^{2}}=-\frac{1}{x^{2}}
$$

## Example 16 Compute the derivative of $\sin x$.

Solution Let $f(x)=\sin x$. Then

$$
\begin{aligned}
\frac{d f(x)}{d x} & =\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{\sin (x+h)-\sin (x)}{h} \\
& =\lim _{h \rightarrow 0} \frac{2 \cos \left(\frac{2 x+h}{2}\right) \sin \left(\frac{h}{2}\right)}{h}(\text { using formula for } \sin \mathrm{A}-\sin \mathrm{B}) \\
& =\lim _{h \rightarrow 0} \cos \left(x+\frac{h}{2}\right) \cdot \lim _{h \rightarrow 0} \frac{\sin \frac{h}{2}}{\frac{h}{2}}=\cos x \cdot 1=\cos x
\end{aligned}
$$

## Example 17 Compute the derivative of $\tan x$.

Solution Let $f(x)=\tan x$. Then

$$
\begin{aligned}
\frac{d f(x)}{d x} & =\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{\tan (x+h)-\tan (x)}{h} \\
& =\lim _{h \rightarrow 0} \frac{1}{h}\left[\frac{\sin (x+h)}{\cos (x+h)}-\frac{\sin x}{\cos x}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{h \rightarrow 0}\left[\frac{\sin (x+h) \cos x-\cos (x+h) \sin x}{h \cos (x+h) \cos x}\right] \\
& =\lim _{h \rightarrow 0} \frac{\sin (x+h-x)}{h \cos (x+h) \cos x}(\text { using formula for } \sin (\mathrm{A}+\mathrm{B})) \\
& =\lim _{h \rightarrow 0} \frac{\sin h}{h} \cdot \lim _{h \rightarrow 0} \frac{1}{\cos (x+h) \cos x} \\
& =1 \cdot \frac{1}{\cos ^{2} x}=\sec ^{2} x
\end{aligned}
$$

Example 18 Compute the derivative of $f(x)=\sin ^{2} x$.
Solution We use the Leibnitz product rule to evaluate this.

$$
\begin{aligned}
\frac{d f(x)}{d x} & =\frac{d}{d x}(\sin x \sin x) \\
& =(\sin x)^{\prime} \sin x+\sin x(\sin x)^{\prime} \\
& =(\cos x) \sin x+\sin x(\cos x) \\
& =2 \sin x \cos x=\sin 2 x
\end{aligned}
$$

## EXERCISE 12.2

1. Find the derivative of $x^{2}-2$ at $x=10$.
2. Find the derivative of $x$ at $x=1$.
3. Find the derivative of $99 x$ at $x=100$.
4. Find the derivative of the following functions from first principle.
(i) $x^{3}-27$
(ii) $(x-1)(x-2)$
(iii) $\frac{1}{x^{2}}$
(iv) $\frac{x+1}{x-1}$
5. For the function

$$
f(x)=\frac{x^{100}}{100}+\frac{x^{99}}{99}+\ldots+\frac{x^{2}}{2}+x+1
$$

Prove that $f^{\prime}(1)=100 f^{\prime}(0)$.
6. Find the derivative of $x^{n}+a x^{n-1}+a^{2} x^{n-2}+\ldots+a^{n-1} x+a^{n}$ for some fixed real number $a$.
7. For some constants $a$ and $b$, find the derivative of
(i) $(x-a)(x-b)$
(ii) $\left(a x^{2}+b\right)^{2}$
(iii) $\frac{x-a}{x-b}$
8. Find the derivative of $\frac{x^{n}-a^{n}}{x-a}$ for some constant $a$.
9. Find the derivative of
(i) $2 x-\frac{3}{4}$
(ii) $\left(5 x^{3}+3 x-1\right)(x-1)$
(iii) $x^{-3}(5+3 x)$
(iv) $x^{5}\left(3-6 x^{-9}\right)$
(v) $x^{-4}\left(3-4 x^{-5}\right)$
(vi) $\frac{2}{x+1}-\frac{x^{2}}{3 x-1}$
10. Find the derivative of $\cos x$ from first principle.
11. Find the derivative of the following functions:
(i) $\sin x \cos x$
(ii) $\sec x$
(iii) $5 \sec x+4 \cos x$
(iv) $\operatorname{cosec} x$
(v) $3 \cot x+5 \operatorname{cosec} x$
(vi) $5 \sin x-6 \cos x+7$
(vii) $2 \tan x-7 \sec x$

## Miscellaneous Examples

Example 19 Find the derivative of $f$ from the first principle, where $f$ is given by
(i) $f(x)=\frac{2 x+3}{x-2}$
(ii) $f(x)=x+\frac{1}{x}$

Solution (i) Note that function is not defined at $x=2$. But, we have

$$
f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{\frac{2(x+h)+3}{x+h-2}-\frac{2 x+3}{x-2}}{h}
$$

$$
\begin{aligned}
& =\lim _{h \rightarrow 0} \frac{(2 x+2 h+3)(x-2)-(2 x+3)(x+h-2)}{h(x-2)(x+h-2)} \\
& =\lim _{h \rightarrow 0} \frac{(2 x+3)(x-2)+2 h(x-2)-(2 x+3)(x-2)-h(2 x+3)}{h(x-2)(x+h-2)} \\
& =\lim _{h \rightarrow 0} \frac{-7}{(x-2)(x+h-2)}=-\frac{7}{(x-2)^{2}}
\end{aligned}
$$

Again, note that the function $f^{\prime}$ is also not defined at $x=2$.
(ii) The function is not defined at $x=0$. But, we have

$$
\begin{aligned}
f^{\prime}(x) & =\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{\left(x+h+\frac{1}{x+h}\right)-\left(x+\frac{1}{x}\right)}{h} \\
& =\lim _{h \rightarrow 0} \frac{1}{h}\left[h+\frac{1}{x+h}-\frac{1}{x}\right] \\
& =\lim _{h \rightarrow 0} \frac{1}{h}\left[h+\frac{x-x-h}{x(x+h)}\right]=\lim _{h \rightarrow 0} \frac{1}{h}\left[h\left(1-\frac{1}{x(x+h)}\right)\right] \\
& =\lim _{h \rightarrow 0}\left[1-\frac{1}{x(x+h)}\right]=1-\frac{1}{x^{2}}
\end{aligned}
$$

Again, note that the function $f^{\prime}$ is not defined at $x=0$.
Example 20 Find the derivative of $f(x)$ from the first principle, where $f(x)$ is
(i) $\sin x+\cos x$
(ii) $x \sin x$

Solution (i) we have $f^{\prime}(x)=\frac{f(x+h)-f(x)}{h}$

$$
\begin{aligned}
& =\lim _{h \rightarrow 0} \frac{\sin (x+h)+\cos (x+h)-\sin x-\cos x}{h} \\
& =\lim _{h \rightarrow 0} \frac{\sin x \cos h+\cos x \sin h+\cos x \cos h-\sin x \sin h-\sin x-\cos x}{h}
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{h \rightarrow 0} \frac{\sin h(\cos x-\sin x)+\sin x(\cos h-1)+\cos x(\cos h-1)}{h} \\
& =\lim _{h \rightarrow 0} \frac{\sin h}{h}(\cos x-\sin x)+\lim _{h \rightarrow 0} \sin x \frac{(\cos h-1)}{h}+\lim _{h \rightarrow 0} \cos x \frac{(\cos h-1)}{h} \\
& =\cos x-\sin x
\end{aligned}
$$

(ii) $f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}=\lim _{h \rightarrow 0} \frac{(x+h) \sin (x+h)-x \sin x}{h}$

$$
\begin{aligned}
& \quad=\lim _{h \rightarrow 0} \frac{(x+h)(\sin x \cos h+\sin h \cos x)-x \sin x}{h} \\
& =\lim _{h \rightarrow 0} \frac{x \sin x(\cos h-1)+x \cos x \sin h+h(\sin x \cos h+\sin h \cos x)}{h} \\
& =\lim _{h \rightarrow 0} \frac{x \sin x(\cos h-1)}{h}+\lim _{h \rightarrow 0} x \cos x \frac{\sin h}{h}+\lim _{h \rightarrow 0}(\sin x \cos h+\sin h \cos x) \\
& =x \cos x+\sin x
\end{aligned}
$$

Example 21 Compute derivative of
(i) $f(x)=\sin 2 x$
(ii) $g(x)=\cot x$

Solution (i) Recall the trigonometric formula $\sin 2 x=2 \sin x \cos x$. Thus

$$
\begin{aligned}
\frac{d f(x)}{d x} & =\frac{d}{d x}(2 \sin x \cos x)=2 \frac{d}{d x}(\sin x \cos x) \\
& =2\left[(\sin x)^{\prime} \cos x+\sin x(\cos x)^{\prime}\right] \\
& =2[(\cos x) \cos x+\sin x(-\sin x)] \\
& =2\left(\cos ^{2} x-\sin ^{2} x\right)
\end{aligned}
$$

(ii) By definition, $\mathrm{g}(x)=\cot x=\frac{\cos x}{\sin x}$. We use the quotient rule on this function wherever it is defined. $\frac{d g}{d x}=\frac{d}{d x}(\cot x)=\frac{d}{d x}\left(\frac{\cos x}{\sin x}\right)$

$$
\begin{aligned}
& =\frac{(\cos x)^{\prime}(\sin x)-(\cos x)(\sin x)^{\prime}}{(\sin x)^{2}} \\
& =\frac{(-\sin x)(\sin x)-(\cos x)(\cos x)}{(\sin x)^{2}} \\
& =-\frac{\sin ^{2} x+\cos ^{2} x}{\sin ^{2} x}=-\operatorname{cosec}^{2} x
\end{aligned}
$$

Alternatively, this may be computed by noting that $\cot x=\frac{1}{\tan x}$. Here, we use the fact that the derivative of $\tan x$ is $\sec ^{2} x$ which we saw in Example 17 and also that the derivative of the constant function is 0 .

$$
\begin{aligned}
\frac{d g}{d x} & =\frac{d}{d x}(\cot x)=\frac{d}{d x}\left(\frac{1}{\tan x}\right) \\
& =\frac{(1)^{\prime}(\tan x)-(1)(\tan x)^{\prime}}{(\tan x)^{2}} \\
& =\frac{(0)(\tan x)-(\sec x)^{2}}{(\tan x)^{2}} \\
& =\frac{-\sec ^{2} x}{\tan ^{2} x}=-\operatorname{cosec}^{2} x
\end{aligned}
$$

Example 22 Find the derivative of
(i) $\frac{x^{5}-\cos x}{\sin x}$
(ii) $\frac{x+\cos x}{\tan x}$

Solution (i) Let $h(x)=\frac{x^{5}-\cos x}{\sin x}$. We use the quotient rule on this function wherever it is defined.

$$
h^{\prime}(x)=\frac{\left(x^{5}-\cos x\right)^{\prime} \sin x-\left(x^{5}-\cos x\right)(\sin x)^{\prime}}{(\sin x)^{2}}
$$

$$
\begin{aligned}
& =\frac{\left(5 x^{4}+\sin x\right) \sin x-\left(x^{5}-\cos x\right) \cos x}{\sin ^{2} x} \\
& =\frac{-x^{5} \cos x+5 x^{4} \sin x+1}{(\sin x)^{2}}
\end{aligned}
$$

(ii) We use quotient rule on the function $\frac{x+\cos x}{\tan x}$ wherever it is defined.

$$
\begin{aligned}
h^{\prime}(x) & =\frac{(x+\cos x)^{\prime} \tan x-(x+\cos x)(\tan x)^{\prime}}{(\tan x)^{2}} \\
& =\frac{(1-\sin x) \tan x-(x+\cos x) \sec ^{2} x}{(\tan x)^{2}}
\end{aligned}
$$

## Miscellaneous Exercise on Chapter 12

1. Find the derivative of the following functions from first principle:
(i) $-x$
(ii) $(-x)^{-1}$
(iii) $\sin (x+1)$
(iv) $\cos \left(x-\frac{\pi}{8}\right)$

Find the derivative of the following functions (it is to be understood that $a, b, c, d$, $p, q, r$ and $s$ are fixed non-zero constants and $m$ and $n$ are integers):
2. $(x+a)$
3. $(p x+q)\left(\frac{r}{x}+s\right)$
4. $(a x+b)(c x+d)^{2}$
5. $\frac{a x+b}{c x+d}$
6. $\frac{1+\frac{1}{x}}{1-\frac{1}{x}}$
7. $\frac{1}{a x^{2}+b x+c}$
8. $\frac{a x+b}{p x^{2}+q x+r}$
9. $\frac{p x^{2}+q x+r}{a x+b}$
10. $\frac{a}{x^{4}}-\frac{b}{x^{2}}+\cos x$
11. $4 \sqrt{x}-2$
12. $(a x+b)^{n}$
13. $(a x+b)^{n}(c x+d)^{m}$
14. $\sin (x+a)$
15. $\operatorname{cosec} x \cot x$
16. $\frac{\cos x}{1+\sin x}$
17. $\frac{\sin x+\cos x}{\sin x-\cos x}$
18. $\frac{\sec x-1}{\sec x+1}$
19. $\sin ^{n} x$
20. $\frac{a+b \sin x}{c+d \cos x}$
21. $\frac{\sin (x+a)}{\cos x}$
22. $x^{4}(5 \sin x-3 \cos x)$
23. $\left(x^{2}+1\right) \cos x$
24. $\left(a x^{2}+\sin x\right)(p+q \cos x)$
25. $(x+\cos x)(x-\tan x)$
26. $\frac{4 x+5 \sin x}{3 x+7 \cos x}$
27. $\frac{x^{2} \cos \left(\frac{\pi}{4}\right)}{\sin x}$
28. $\frac{x}{1+\tan x}$
29. $(x+\sec x)(x-\tan x)$
30. $\frac{x}{\sin ^{n} x}$

## Summary

- The expected value of the function as dictated by the points to the left of a point defines the left hand limit of the function at that point. Similarly the right hand limit.
Limit of a function at a point is the common value of the left and right hand limits, if they coincide.
- For a function $f$ and a real number $a, \lim _{x \rightarrow a} f(x)$ and $f(a)$ may not be same (In fact, one may be defined and not the other one).
- For functions $f$ and $g$ the following holds:
$\lim _{x \rightarrow a}[f(x) \pm g(x)]=\lim _{x \rightarrow a} f(x) \pm \lim _{x \rightarrow a} g(x)$
$\lim _{x \rightarrow a}[f(x) \cdot g(x)]=\lim _{x \rightarrow a} f(x) \cdot \lim _{x \rightarrow a} g(x)$
$\lim _{x \rightarrow a}\left[\frac{f(x)}{g(x)}\right]=\frac{\lim _{x \rightarrow a} f(x)}{\lim _{x \rightarrow a} g(x)}$
Following are some of the standard limits
$\lim _{x \rightarrow a} \frac{x^{n}-a^{n}}{x-a}=n a^{n-1}$
$\lim _{x \rightarrow 0} \frac{\sin x}{x}=1$
$\lim _{x \rightarrow 0} \frac{1-\cos x}{x}=0$
The derivative of a function $f$ at $a$ is defined by
$f^{\prime}(a)=\lim _{h \rightarrow 0} \frac{f(a+h)-f(a)}{h}$
Derivative of a function $f$ at any point $x$ is defined by
$f^{\prime}(x)=\frac{d f(x)}{d x}=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}$
- For functions $u$ and $v$ the following holds:
$(u \pm v)^{\prime}=u^{\prime} \pm v^{\prime}$
$(u v)^{\prime}=u^{\prime} v+u v^{\prime}$
$\left(\frac{u}{v}\right)^{\prime}=\frac{u^{\prime} v-u v^{\prime}}{v^{2}}$ provided all are defined.
Following are some of the standard derivatives.
$\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$
$\frac{d}{d x}(\sin x)=\cos x$
$\frac{d}{d x}(\cos x)=-\sin x$


## Historical Note

In the history of mathematics two names are prominent to share the credit for inventing calculus, Issac Newton (1642-1727) and G.W. Leibnitz (1646-1717). Both of them independently invented calculus around the seventeenth century. After the advent of calculus many mathematicians contributed for further development of calculus. The rigorous concept is mainly attributed to the great
mathematicians, A.L. Cauchy, J.L.Lagrange and Karl Weierstrass. Cauchy gave the foundation of calculus as we have now generally accepted in our textbooks. Cauchy used D'Alembert's limit concept to define the derivative of a function. Starting with definition of a limit, Cauchy gave examples such as the limit of $\frac{\sin \alpha}{\alpha}$ for $\alpha=0$. He wrote $\frac{\Delta y}{\Delta x}=\frac{f(x+i)-f(x)}{i}$, and called the limit for $i \rightarrow 0$, the "function derive'e, $y^{\prime}$ for $f^{\prime}(x)$ ".

Before 1900, it was thought that calculus is quite difficult to teach. So calculus became beyond the reach of youngsters. But just in 1900, John Perry and others in England started propagating the view that essential ideas and methods of calculus were simple and could be taught even in schools. F.L. Griffin, pioneered the teaching of calculus to first year students. This was regarded as one of the most daring act in those days.

Today not only the mathematics but many other subjects such as Physics, Chemistry, Economics and Biological Sciences are enjoying the fruits of calculus.

