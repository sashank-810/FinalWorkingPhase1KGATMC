Chapter
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-01.jpg?height=165&width=138&top_left_y=247&top_left_x=1332)

## CONTINUITY AND DIFFERENTIABILITY

## The whole of science is nothing more than a refinement of everyday thinking." - ALBERT EINSTEIN

### 5.1 Introduction

This chapter is essentially a continuation of our study of differentiation of functions in Class XI. We had learnt to differentiate certain functions like polynomial functions and trigonometric functions. In this chapter, we introduce the very important concepts of continuity, differentiability and relations between them. We will also learn differentiation of inverse trigonometric functions. Further, we introduce a new class of functions called exponential and logarithmic functions. These functions lead to powerful techniques of differentiation. We illustrate certain geometrically obvious conditions through differential calculus. In the process, we will learn some fundamental theorems in this area.

### 5.2 Continuity

![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-01.jpg?height=585&width=411&top_left_y=821&top_left_x=1061)

Sir Issac Newton
(1642-1727)

We start the section with two informal examples to get a feel of continuity. Consider the function

$$
f(x)=\left\{\begin{array}{l}
1, \text { if } x \leq 0 \\
2, \text { if } x>0
\end{array}\right.
$$

This function is of course defined at every point of the real line. Graph of this function is given in the Fig 5.1. One can deduce from the graph that the value of the function at nearby points on $x$-axis remain close to each other except at $x=0$. At the points near and to the left of 0 , i.e., at points like $-0.1,-0.01,-0.001$, the value of the function is 1 . At the points near and to the right of 0 , i.e., at points like 0.1, 0.01,
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-01.jpg?height=439&width=583&top_left_y=1613&top_left_x=880)

Fig 5.1
0.001 , the value of the function is 2 . Using the language of left and right hand limits, we may say that the left (respectively right) hand limit of $f$ at 0 is 1 (respectively 2 ). In particular the left and right hand limits do not coincide. We also observe that the value of the function at $x=0$ concides with the left hand limit. Note that when we try to draw the graph, we cannot draw it in one stroke, i.e., without lifting pen from the plane of the paper, we can not draw the graph of this function. In fact, we need to lift the pen when we come to 0 from left. This is one instance of function being not continuous at $x=0$.

Now, consider the function defined as

$$
f(x)=\begin{aligned}
& 1, \text { if } x \neq 0 \\
& 2, \text { if } x=0
\end{aligned}
$$

This function is also defined at every point. Left and the right hand limits at $x=0$ are both equal to 1 . But the value of the function at $x=0$ equals 2 which does not coincide with the common value of the left and right hand limits. Again, we note that we cannot draw the graph of the function without lifting the pen. This is yet another instance of a function being not continuous at $x=0$.

Naively, we may say that a function is continuous at a fixed point if we can draw the graph of the function around that point without lifting the pen from the plane of the paper.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-02.jpg?height=427&width=604&top_left_y=937&top_left_x=855)

Fig 5.2

Mathematically, it may be phrased precisely as follows:
Definition 1 Suppose $f$ is a real function on a subset of the real numbers and let $c$ be a point in the domain of $f$. Then $f$ is continuous at $c$ if

$$
\lim _{x \rightarrow c} f(x)=f(c)
$$

More elaborately, if the left hand limit, right hand limit and the value of the function at $x=c$ exist and equal to each other, then $f$ is said to be continuous at $x=c$. Recall that if the right hand and left hand limits at $x=c$ coincide, then we say that the common value is the limit of the function at $x=c$. Hence we may also rephrase the definition of continuity as follows: a function is continuous at $x=c$ if the function is defined at $x=c$ and if the value of the function at $x=c$ equals the limit of the function at $x=c$. If $f$ is not continuous at $c$, we say $f$ is discontinuous at $c$ and $c$ is called a point of discontinuity of $f$.

Example 1 Check the continuity of the function $f$ given by $f(x)=2 x+3$ at $x=1$.
Solution First note that the function is defined at the given point $x=1$ and its value is 5 . Then find the limit of the function at $x=1$. Clearly

Thus

$$
\lim _{x \rightarrow 1} f(x)=\lim _{x \rightarrow 1}(2 x+3)=2(1)+3=5
$$

Hence, $f$ is continuous at $x=1$.
Example 2 Examine whether the function $f$ given by $f(x)=x^{2}$ is continuous at $x=0$.
Solution First note that the function is defined at the given point $x=0$ and its value is 0 . Then find the limit of the function at $x=0$. Clearly

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0} x^{2}=0^{2}=0
$$

Thus

$$
\lim _{x \rightarrow 0} f(x)=0=f(0)
$$

Hence, $f$ is continuous at $x=0$.
Example 3 Discuss the continuity of the function $f$ given by $f(x)=|x|$ at $x=0$.
Solution By definition

$$
f(x)= \begin{cases}-x, & \text { if } x<0 \\ x, & \text { if } x \geq 0\end{cases}
$$

Clearly the function is defined at 0 and $f(0)=0$. Left hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(-x)=0
$$

Similarly, the right hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}} x=0
$$

Thus, the left hand limit, right hand limit and the value of the function coincide at $x=0$. Hence, $f$ is continuous at $x=0$.

Example 4 Show that the function $f$ given by

$$
f(x)= \begin{cases}x^{3}+3, & \text { if } x \neq 0 \\ 1, & \text { if } x=0\end{cases}
$$

is not continuous at $x=0$.

Solution The function is defined at $x=0$ and its value at $x=0$ is 1 . When $x \neq 0$, the function is given by a polynomial. Hence,

$$
\lim _{x \rightarrow 0} f(x)=\lim _{x \rightarrow 0}\left(x^{3}+3\right)=0^{3}+3=3
$$

Since the limit of $f$ at $x=0$ does not coincide with $f(0)$, the function is not continuous at $x=0$. It may be noted that $x=0$ is the only point of discontinuity for this function.

Example 5 Check the points where the constant function $f(x)=k$ is continuous.
Solution The function is defined at all real numbers and by definition, its value at any real number equals $k$. Let $c$ be any real number. Then

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} k=k
$$

Since $f(c)=k=\lim _{x \rightarrow c} f(x)$ for any real number $c$, the function $f$ is continuous at every real number.
Example 6 Prove that the identity function on real numbers given by $f(x)=x$ is continuous at every real number.
Solution The function is clearly defined at every point and $f(c)=c$ for every real number c. Also,

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
$$

Thus, $\lim _{x \rightarrow c} f(x)=c=f(c)$ and hence the function is continuous at every real number.
Having defined continuity of a function at a given point, now we make a natural extension of this definition to discuss continuity of a function.
Definition 2 A real function $f$ is said to be continuous if it is continuous at every point in the domain of $f$.

This definition requires a bit of elaboration. Suppose $f$ is a function defined on a closed interval $[a, b]$, then for $f$ to be continuous, it needs to be continuous at every point in $[a, b]$ including the end points $a$ and $b$. Continuity of $f$ at $a$ means

$$
\lim _{x \rightarrow a^{+}} f(x)=f(a)
$$

and continuity of $f$ at $b$ means

$$
\lim _{x \rightarrow b^{-}} f(x)=f(b)
$$

Observe that $\lim _{x \rightarrow a^{-}} f(x)$ and $\lim _{x \rightarrow b^{+}} f(x)$ do not make sense. As a consequence of this definition, if $f$ is defined only at one point, it is continuous there, i.e., if the domain of $f$ is a singleton, $f$ is a continuous function.

Example 7 Is the function defined by $f(x)=|x|$, a continuous function?
Solution We may rewrite $f$ as

$$
f(x)= \begin{cases}-x, & \text { if } x<0 \\ x, & \text { if } x \geq 0\end{cases}
$$

By Example 3, we know that $f$ is continuous at $x=0$.
Let $c$ be a real number such that $c<0$. Then $f(c)=-c$. Also

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x)=-c \quad \text { (Why?) }
$$

Since $\lim _{x \rightarrow c} f(x)=f(c), f$ is continuous at all negative real numbers.
Now, let $c$ be a real number such that $c>0$. Then $f(c)=c$. Also

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} x=c
$$

(Why?)
Since $\lim _{x \rightarrow c} f(x)=f(c), f$ is continuous at all positive real numbers. Hence, $f$ is continuous at all points.

Example 8 Discuss the continuity of the function $f$ given by $f(x)=x^{3}+x^{2}-1$.
Solution Clearly $f$ is defined at every real number $c$ and its value at $c$ is $c^{3}+c^{2}-1$. We also know that

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}\left(x^{3}+x^{2}-1\right)=c^{3}+c^{2}-1
$$

Thus $\lim _{x \rightarrow c} f(x)=f(c)$, and hence $f$ is continuous at every real number. This means $f$ is a continuous function.

Example 9 Discuss the continuity of the function $f$ defined by $f(x)=\frac{1}{x}, x \neq 0$.
Solution Fix any non zero real number $c$, we have

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c} \frac{1}{x}=\frac{1}{c}
$$

Also, since for $c \neq 0, f(c)=\frac{1}{c}$, we have $\lim _{x \rightarrow c} f(x)=f(c)$ and hence, $f$ is continuous at every point in the domain of $f$. Thus $f$ is a continuous function.

We take this opportunity to explain the concept of infinity. This we do by analysing the function $f(x)=\frac{1}{x}$ near $x=0$. To carry out this analysis we follow the usual trick of finding the value of the function at real numbers close to 0 . Essentially we are trying to find the right hand limit of $f$ at 0 . We tabulate this in the following (Table 5.1).

Table 5.1

| $x$ | 1 | 0.3 | 0.2 | $0.1=10^{-1}$ | $0.01=10^{-2}$ | $0.001=10^{-3}$ | $10^{-n}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | 1 | $3.333 \ldots$ | 5 | 10 | $100=10^{2}$ | $1000=10^{3}$ | $10^{n}$ |

We observe that as $x$ gets closer to 0 from the right, the value of $f(x)$ shoots up higher. This may be rephrased as: the value of $f(x)$ may be made larger than any given number by choosing a positive real number very close to 0 . In symbols, we write

$$
\lim _{x \rightarrow 0^{+}} f(x)=+\infty
$$

(to be read as: the right hand limit of $f(x)$ at 0 is plus infinity). We wish to emphasise that $+\infty$ is NOT a real number and hence the right hand limit of $f$ at 0 does not exist (as a real number).

Similarly, the left hand limit of $f$ at 0 may be found. The following table is self explanatory.

Table 5.2

| $x$ | -1 | -0.3 | -0.2 | $-10^{-1}$ | $-10^{-2}$ | $-10^{-3}$ | $-10^{-n}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f(x)$ | -1 | $-3.333 \ldots$ | -5 | -10 | $-10^{2}$ | $-10^{3}$ | $-10^{n}$ |

From the Table 5.2, we deduce that the value of $f(x)$ may be made smaller than any given number by choosing a negative real number very close to 0 . In symbols, we write

$$
\lim _{x \rightarrow 0^{-}} f(x)=-\infty
$$

(to be read as: the left hand limit of $f(x)$ at 0 is minus infinity). Again, we wish to emphasise that $-\infty$ is NOT a real number and hence the left hand limit of $f$ at 0 does not exist (as a real number). The graph of the reciprocal function given in Fig 5.3 is a geometric representation of the above mentioned facts.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-06.jpg?height=615&width=618&top_left_y=1460&top_left_x=853)

Fig 5.3

Example 10 Discuss the continuity of the function $f$ defined by

$$
f(x)=\left\{\begin{array}{l}
x+2, \text { if } x \leq 1 \\
x-2, \text { if } x>1
\end{array}\right.
$$

Solution The function $f$ is defined at all points of the real line.
Case 1 If $c<1$, then $f(c)=c+2$. Therefore, $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+2)=c+2$ Thus, $f$ is continuous at all real numbers less than 1 .
Case 2 If $c>1$, then $f(c)=c-2$. Therefore,

$$
\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x-2)=c-2=f(c)
$$

Thus, $f$ is continuous at all points $x>1$.
Case 3 If $c=1$, then the left hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+2)=1+2=3
$$

The right hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x-2)=1-2=-1
$$

Since the left and right hand limits of $f$ at $x=1$
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-07.jpg?height=523&width=527&top_left_y=703&top_left_x=938)

Fig 5.4 do not coincide, $f$ is not continuous at $x=1$. Hence $x=1$ is the only point of discontinuity of $f$. The graph of the function is given in Fig 5.4.

Example 11 Find all the points of discontinuity of the function $f$ defined by

$$
f(x)=\left\{\begin{array}{cc}
x+2, & \text { if } x<1 \\
0, & \text { if } x=1 \\
x-2, & \text { if } x>1
\end{array}\right.
$$

Solution As in the previous example we find that $f$ is continuous at all real numbers $x \neq 1$. The left hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}}(x+2)=1+2=3
$$

The right hand limit of $f$ at $x=1$ is

$$
\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}}(x-2)=1-2=-1
$$

Since, the left and right hand limits of $f$ at $x=1$ do not coincide, $f$ is not continuous at $x=1$. Hence $x=1$ is the only point of discontinuity of $f$. The graph of the function is given in the Fig 5.5.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-07.jpg?height=523&width=530&top_left_y=1543&top_left_x=934)

Fig 5.5

Example 12 Discuss the continuity of the function defined by

$$
f(x)=\left\{\begin{array}{r}
x+2, \text { if } x<0 \\
-x+2, \text { if } x>0
\end{array}\right.
$$

Solution Observe that the function is defined at all real numbers except at 0 . Domain of definition of this function is

$$
\begin{aligned}
\mathrm{D}_{1} \cup \mathrm{D}_{2} \text { where } \mathrm{D}_{1} & =\{x \in \mathbf{R}: x<0\} \text { and } \\
\mathrm{D}_{2} & =\{x \in \mathbf{R}: x>0\}
\end{aligned}
$$

Case 1 If $c \in \mathrm{D}_{1}$, then $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(x+2)$ $=c+2=f(c)$ and hence $f$ is continuous in $\mathrm{D}_{1}$.
Case 2 If $c \in \mathrm{D}_{2}$, then $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}(-x+2)$ $=-c+2=f(c)$ and hence $f$ is continuous in $\mathrm{D}_{2}$. Since $f$ is continuous at all points in the domain of $f$, we deduce that $f$ is continuous. Graph of this function is given in the Fig 5.6. Note that to graph this function we need to lift the pen from the plane
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-08.jpg?height=527&width=534&top_left_y=618&top_left_x=937)

Fig 5.6 of the paper, but we need to do that only for those points where the function is not defined.

Example 13 Discuss the continuity of the function $f$ given by

$$
f(x)= \begin{cases}x, & \text { if } x \geq 0 \\ x^{2}, & \text { if } x<0\end{cases}
$$

Solution Clearly the function is defined at every real number. Graph of the function is given in Fig 5.7. By inspection, it seems prudent to partition the domain of definition of $f$ into three disjoint subsets of the real line.
Let

$$
\begin{aligned}
& D_{1}=\{x \in \mathbf{R}: x<0\}, D_{2}=\{0\} \text { and } \\
& D_{3}=\{x \in \mathbf{R}: x>0\}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-08.jpg?height=439&width=599&top_left_y=1390&top_left_x=872)

Fig 5.7

Case 1 At any point in $\mathrm{D}_{1}$, we have $f(x)=x^{2}$ and it is easy to see that it is continuous there (see Example 2).
Case 2 At any point in $\mathrm{D}_{3}$, we have $f(x)=x$ and it is easy to see that it is continuous there (see Example 6).

Case 3 Now we analyse the function at $x=0$. The value of the function at 0 is $f(0)=0$. The left hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}} x^{2}=0^{2}=0
$$

The right hand limit of $f$ at 0 is

$$
\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}} x=0
$$

Thus $\lim _{x \rightarrow 0} f(x)=0=f(0)$ and hence $f$ is continuous at 0 . This means that $f$ is continuous at every point in its domain and hence, $f$ is a continuous function.
Example 14 Show that every polynomial function is continuous.
Solution Recall that a function $p$ is a polynomial function if it is defined by $p(x)=a_{0}+a_{1} x+\ldots+a_{n} x^{n}$ for some natural number $n, a_{n} \neq 0$ and $a_{i} \in \mathbf{R}$. Clearly this function is defined for every real number. For a fixed real number $c$, we have

$$
\lim _{x \rightarrow c} p(x)=p(c)
$$

By definition, $p$ is continuous at $c$. Since $c$ is any real number, $p$ is continuous at every real number and hence $p$ is a continuous function.

Example 15 Find all the points of discontinuity of the greatest integer function defined by $f(x)=[x]$, where $[x]$ denotes the greatest integer less than or equal to $x$.

Solution First observe that $f$ is defined for all real numbers. Graph of the function is given in Fig 5.8. From the graph it looks like that $f$ is discontinuous at every integral point. Below we explore, if this is true.
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-09.jpg?height=627&width=794&top_left_y=1454&top_left_x=415)

Fig 5.8

Case 1 Let $c$ be a real number which is not equal to any integer. It is evident from the graph that for all real numbers close to $c$ the value of the function is equal to $[c]$; i.e., $\lim _{x \rightarrow c} f(x)=\lim _{x \rightarrow c}[x]=[c]$. Also $f(c)=[c]$ and hence the function is continuous at all real numbers not equal to integers.
Case 2 Let $c$ be an integer. Then we can find a sufficiently small real number $r>0$ such that $[c-r]=c-1$ whereas $[c+r]=c$.
This, in terms of limits mean that

$$
\lim _{x \rightarrow c^{-}} f(x)=c-1, \lim _{x \rightarrow c^{+}} f(x)=c
$$

Since these limits cannot be equal to each other for any $c$, the function is discontinuous at every integral point.

### 5.2.1 Algebra of continuous functions

In the previous class, after having understood the concept of limits, we learnt some algebra of limits. Analogously, now we will study some algebra of continuous functions. Since continuity of a function at a point is entirely dictated by the limit of the function at that point, it is reasonable to expect results analogous to the case of limits.
Theorem 1 Suppose $f$ and $g$ be two real functions continuous at a real number $c$. Then
(1) $f+g$ is continuous at $x=c$.
(2) $f-g$ is continuous at $x=c$.
(3) $f . g$ is continuous at $x=c$.
(4) $\left(\frac{f}{g}\right)$ is continuous at $x=c$, (provided $g(c) \neq 0$ ).

Proof We are investigating continuity of $(f+g)$ at $x=c$. Clearly it is defined at $x=c$. We have

$$
\begin{aligned}
\lim _{x \rightarrow c}(f+g)(x) & =\lim _{x \rightarrow c}[f(x)+g(x)] & & \text { (by definition of } f+g) \\
& =\lim _{x \rightarrow c} f(x)+\lim _{x \rightarrow c} g(x) & & \text { (by the theorem on limits) } \\
& =f(c)+g(c) & & \text { (as } f \text { and } g \text { are continuous) } \\
& =(f+g)(c) & & \text { (by definition of } f+g)
\end{aligned}
$$

Hence, $f+g$ is continuous at $x=c$.
Proofs for the remaining parts are similar and left as an exercise to the reader.

## Remarks

(i) As a special case of (3) above, if $f$ is a constant function, i.e., $f(x)=\lambda$ for some real number $\lambda$, then the function ( $\lambda . g$ ) defined by $(\lambda . g)(x)=\lambda . g(x)$ is also continuous. In particular if $\lambda=-1$, the continuity of $f$ implies continuity of $-f$.
(ii) As a special case of (4) above, if $f$ is the constant function $f(x)=\lambda$, then the function $\frac{\lambda}{g}$ defined by $\frac{\lambda}{g}(x)=\frac{\lambda}{g(x)}$ is also continuous wherever $g(x) \neq 0$. In particular, the continuity of $g$ implies continuity of $\frac{1}{g}$.
The above theorem can be exploited to generate many continuous functions. They also aid in deciding if certain functions are continuous or not. The following examples illustrate this:

Example 16 Prove that every rational function is continuous.
Solution Recall that every rational function $f$ is given by

$$
f(x)=\frac{p(x)}{q(x)}, q(x) \neq 0
$$

where $p$ and $q$ are polynomial functions. The domain of $f$ is all real numbers except points at which $q$ is zero. Since polynomial functions are continuous (Example 14), $f$ is continuous by (4) of Theorem 1.

Example 17 Discuss the continuity of sine function.
Solution To see this we use the following facts

$$
\lim _{x \rightarrow 0} \sin x=0
$$

We have not proved it, but is intuitively clear from the graph of $\sin x$ near 0 .
Now, observe that $f(x)=\sin x$ is defined for every real number. Let $c$ be a real number. Put $x=c+h$. If $x \rightarrow c$ we know that $h \rightarrow 0$. Therefore

$$
\begin{aligned}
\lim _{x \rightarrow c} f(x) & =\lim _{x \rightarrow c} \sin x \\
& =\lim _{h \rightarrow 0} \sin (c+h) \\
& =\lim _{h \rightarrow 0}[\sin c \cos h+\cos c \sin h] \\
& =\lim _{h \rightarrow 0}[\sin c \cos h]+\lim _{h \rightarrow 0}[\cos c \sin h] \\
& =\sin c+0=\sin c=f(c)
\end{aligned}
$$

Thus $\lim _{x \rightarrow c} f(x)=f(c)$ and hence $f$ is a continuous function.

Remark A similar proof may be given for the continuity of cosine function.
Example 18 Prove that the function defined by $f(x)=\tan x$ is a continuous function.
Solution The function $f(x)=\tan x=\frac{\sin x}{\cos x}$. This is defined for all real numbers such that $\cos x \neq 0$, i.e., $x \neq(2 n+1) \frac{\pi}{2}$. We have just proved that both sine and cosine functions are continuous. Thus $\tan x$ being a quotient of two continuous functions is continuous wherever it is defined.

An interesting fact is the behaviour of continuous functions with respect to composition of functions. Recall that if $f$ and $g$ are two real functions, then

$$
(f \circ g)(x)=f(g(x))
$$

is defined whenever the range of $g$ is a subset of domain of $f$. The following theorem (stated without proof) captures the continuity of composite functions.
Theorem 2 Suppose $f$ and $g$ are real valued functions such that ( $f \mathrm{o} g$ ) is defined at $c$. If $g$ is continuous at $c$ and if $f$ is continuous at $g(c)$, then $(f \mathrm{o} g)$ is continuous at $c$.

The following examples illustrate this theorem.
Example 19 Show that the function defined by $f(x)=\sin \left(x^{2}\right)$ is a continuous function.
Solution Observe that the function is defined for every real number. The function $f$ may be thought of as a composition $g$ o $h$ of the two functions $g$ and $h$, where $g(x)=\sin x$ and $h(x)=x^{2}$. Since both $g$ and $h$ are continuous functions, by Theorem 2, it can be deduced that $f$ is a continuous function.

Example 20 Show that the function $f$ defined by

$$
f(x)=|1-x+|x||,
$$

where $x$ is any real number, is a continuous function.
Solution Define $g$ by $g(x)=1-x+|x|$ and $h$ by $h(x)=|x|$ for all real $x$. Then

$$
\begin{aligned}
(h \circ g)(x) & =h(g(x)) \\
& =h(1-x+|x|) \\
& =|1-x+|x||=f(x)
\end{aligned}
$$

In Example 7, we have seen that $h$ is a continuous function. Hence $g$ being a sum of a polynomial function and the modulus function is continuous. But then $f$ being a composite of two continuous functions is continuous.

## EXERCISE 5.1

1. Prove that the function $f(x)=5 x-3$ is continuous at $x=0$, at $x=-3$ and at $x=5$.
2. Examine the continuity of the function $f(x)=2 x^{2}-1$ at $x=3$.
3. Examine the following functions for continuity.
(a) $f(x)=x-5$
(b) $f(x)=\frac{1}{x-5}, x \neq 5$
(c) $f(x)=\frac{x^{2}-25}{x+5}, x \neq-5$
(d) $f(x)=|x-5|$
4. Prove that the function $f(x)=x^{n}$ is continuous at $x=n$, where $n$ is a positive integer.
5. Is the function $f$ defined by

$$
f(x)=\left\{\begin{array}{l}
x, \text { if } x \leq 1 \\
5, \text { if } x>1
\end{array}\right.
$$

continuous at $x=0$ ? At $x=1$ ? At $x=2$ ?
Find all points of discontinuity of $f$, where $f$ is defined by
6. $f(x)=\left\{\begin{array}{l}2 x+3, \text { if } x \leq 2 \\ 2 x-3, \text { if } x>2\end{array}\right.$
7. $f(x)=\left\{\begin{array}{cl}|x|+3, & \text { if } x \leq-3 \\ -2 x, & \text { if }-3<x<3 \\ 6 x+2, & \text { if } x \geq 3\end{array}\right.$
8. $f(x)=\left\{\begin{array}{cc}\frac{|x|}{x}, & \text { if } x \neq 0 \\ 0, & \text { if } x=0\end{array}\right.$
9. $f(x)= \begin{cases}\frac{x}{|x|}, & \text { if } x<0 \\ -1, & \text { if } x \geq 0\end{cases}$
10. $f(x)= \begin{cases}x+1, & \text { if } x \geq 1 \\ x^{2}+1, & \text { if } x<1\end{cases}$
11. $f(x)= \begin{cases}x^{3}-3, & \text { if } x \leq 2 \\ x^{2}+1, & \text { if } x>2\end{cases}$
12. $f(x)= \begin{cases}x^{10}-1, & \text { if } x \leq 1 \\ x^{2}, & \text { if } x>1\end{cases}$
13. Is the function defined by

$$
f(x)= \begin{cases}x+5, & \text { if } x \leq 1 \\ x-5, & \text { if } x>1\end{cases}
$$

a continuous function?

Discuss the continuity of the function $f$, where $f$ is defined by
14. $f(x)=\left\{\begin{array}{l}3, \text { if } 0 \leq x \leq 1 \\ 4, \text { if } 1<x<3 \\ 5, \text { if } 3 \leq x \leq 10\end{array}\right.$
15. $f(x)= \begin{cases}2 x, & \text { if } x<0 \\ 0, & \text { if } 0 \leq x \leq 1 \\ 4 x, & \text { if } x>1\end{cases}$
16. $f(x)= \begin{cases}-2, & \text { if } x \leq-1 \\ 2 x, & \text { if }-1<x \leq 1 \\ 2, & \text { if } x>1\end{cases}$
17. Find the relationship between $a$ and $b$ so that the function $f$ defined by

$$
f(x)= \begin{cases}a x+1, & \text { if } x \leq 3 \\ b x+3, & \text { if } x>3\end{cases}
$$

is continuous at $x=3$.
18. For what value of $\lambda$ is the function defined by

$$
f(x)= \begin{cases}\lambda\left(x^{2}-2 x\right), & \text { if } x \leq 0 \\ 4 x+1, & \text { if } x>0\end{cases}
$$

continuous at $x=0$ ? What about continuity at $x=1$ ?
19. Show that the function defined by $g(x)=x-[x]$ is discontinuous at all integral points. Here $[x]$ denotes the greatest integer less than or equal to $x$.
20. Is the function defined by $f(x)=x^{2}-\sin x+5$ continuous at $x=\pi$ ?
21. Discuss the continuity of the following functions:
(a) $f(x)=\sin x+\cos x$
(b) $f(x)=\sin x-\cos x$
(c) $f(x)=\sin x \cdot \cos x$
22. Discuss the continuity of the cosine, cosecant, secant and cotangent functions.
23. Find all points of discontinuity of $f$, where

$$
f(x)= \begin{cases}\frac{\sin x}{x}, & \text { if } x<0 \\ x+1, & \text { if } x \geq 0\end{cases}
$$

24. Determine if $f$ defined by

$$
f(x)= \begin{cases}x^{2} \sin \frac{1}{x}, & \text { if } x \neq 0 \\ 0, & \text { if } x=0\end{cases}
$$

is a continuous function?
25. Examine the continuity of $f$, where $f$ is defined by

$$
f(x)= \begin{cases}\sin x-\cos x, & \text { if } x \neq 0 \\ -1, & \text { if } x=0\end{cases}
$$

Find the values of $k$ so that the function $f$ is continuous at the indicated point in Exercises 26 to 29.
26. $f(x)=\left\{\begin{array}{ll}\frac{k \cos x}{\pi-2 x}, & \text { if } x \neq \frac{\pi}{2} \\ 3, & \text { if } x=\frac{\pi}{2}\end{array} \quad\right.$ at $x=\frac{\pi}{2}$
27. $f(x)=\left\{\begin{array}{ll}k x^{2}, & \text { if } x \leq 2 \\ 3, & \text { if } x>2\end{array} \quad\right.$ at $x=2$
28. $f(x)=\left\{\begin{array}{ll}k x+1, & \text { if } x \leq \pi \\ \cos x, & \text { if } x>\pi\end{array} \quad\right.$ at $x=\pi$
29. $f(x)=\left\{\begin{array}{l}k x+1, \text { if } x \leq 5 \\ 3 x-5, \text { if } x>5\end{array} \quad\right.$ at $x=5$
30. Find the values of $a$ and $b$ such that the function defined by

$$
f(x)= \begin{cases}5, & \text { if } x \leq 2 \\ a x+b, & \text { if } 2<x<10 \\ 21, & \text { if } x \geq 10\end{cases}
$$

is a continuous function.
31. Show that the function defined by $f(x)=\cos \left(x^{2}\right)$ is a continuous function.
32. Show that the function defined by $f(x)=|\cos x|$ is a continuous function.
33. Examine that $\sin |x|$ is a continuous function.
34. Find all the points of discontinuity of $f$ defined by $f(x)=|x|-|x+1|$.

### 5.3. Differentiability

Recall the following facts from previous class. We had defined the derivative of a real function as follows:

Suppose $f$ is a real function and $c$ is a point in its domain. The derivative of $f$ at $c$ is defined by

$$
\lim _{h \rightarrow 0} \frac{f(c+h)-f(c)}{h}
$$

provided this limit exists. Derivative of $f$ at $c$ is denoted by $f^{\prime}(c)$ or $\left.\frac{d}{d x}(f(x))\right|_{c}$. The function defined by

$$
f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h}
$$

wherever the limit exists is defined to be the derivative of $f$. The derivative of $f$ is denoted by $f^{\prime}(x)$ or $\frac{d}{d x}(f(x))$ or if $y=f(x)$ by $\frac{d y}{d x}$ or $y^{\prime}$. The process of finding derivative of a function is called differentiation. We also use the phrase differentiate $f(x)$ with respect to $x$ to mean find $f^{\prime}(x)$.

The following rules were established as a part of algebra of derivatives:
(1) $(u \pm v)^{\prime}=u^{\prime} \pm v^{\prime}$
(2) $(u v)^{\prime}=u^{\prime} v+u v^{\prime}$ (Leibnitz or product rule)
(3) $\left(\frac{u}{v}\right)^{\prime}=\frac{u^{\prime} v-u v^{\prime}}{v^{2}}$, wherever $v \neq 0$ (Quotient rule).

The following table gives a list of derivatives of certain standard functions:
Table 5.3

| $f(x)$ | $x^{n}$ | $\sin x$ | $\cos x$ | $\tan x$ |
| :---: | :---: | :---: | :---: | :---: |
| $f^{\prime}(x)$ | $n x^{n-1}$ | $\cos x$ | $-\sin x$ | $\sec ^{2} x$ |

Whenever we defined derivative, we had put a caution provided the limit exists. Now the natural question is; what if it doesn't? The question is quite pertinent and so is its answer. If $\lim _{h \rightarrow 0} \frac{f(c+h)-f(c)}{h}$ does not exist, we say that $f$ is not differentiable at $c$. In other words, we say that a function $f$ is differentiable at a point $c$ in its domain if both $\lim _{h \rightarrow 0^{-}} \frac{f(c+h)-f(c)}{h}$ and $\lim _{h \rightarrow 0^{+}} \frac{f(c+h)-f(c)}{h}$ are finite and equal. A function is said to be differentiable in an interval $[a, b]$ if it is differentiable at every point of $[a, b]$. As in case of continuity, at the end points $a$ and $b$, we take the right hand limit and left hand limit, which are nothing but left hand derivative and right hand derivative of the function at $a$ and $b$ respectively. Similarly, a function is said to be differentiable in an interval $(a, b)$ if it is differentiable at every point of $(a, b)$.

Theorem 3 If a function $f$ is differentiable at a point $c$, then it is also continuous at that point.

Proof Since $f$ is differentiable at $c$, we have

$$
\lim _{x \rightarrow c} \frac{f(x)-f(c)}{x-c}=f^{\prime}(c)
$$

But for $x \neq c$, we have

$$
f(x)-f(c)=\frac{f(x)-f(c)}{x-c} \cdot(x-c)
$$

Therefore

$$
\lim _{x \rightarrow c}[f(x)-f(c)]=\lim _{x \rightarrow c}\left[\frac{f(x)-f(c)}{x-c} \cdot(x-c)\right]
$$

or

$$
\begin{aligned}
\lim _{x \rightarrow c}[f(x)]-\lim _{x \rightarrow c}[f(c)] & =\lim _{x \rightarrow c}\left[\frac{f(x)-f(c)}{x-c}\right] \cdot \lim _{x \rightarrow c}[(x-c)] \\
& =f^{\prime}(c) \cdot 0=0
\end{aligned}
$$

or

$$
\lim _{x \rightarrow c} f(x)=f(c)
$$

Hence $f$ is continuous at $x=c$.
Corollary 1 Every differentiable function is continuous.
We remark that the converse of the above statement is not true. Indeed we have seen that the function defined by $f(x)=|x|$ is a continuous function. Consider the left hand limit

$$
\lim _{h \rightarrow 0^{-}} \frac{f(0+h)-f(0)}{h}=\frac{-h}{h}=-1
$$

The right hand limit

$$
\lim _{h \rightarrow 0^{+}} \frac{f(0+h)-f(0)}{h}=\frac{h}{h}=1
$$

Since the above left and right hand limits at 0 are not equal, $\lim _{h \rightarrow 0} \frac{f(0+h)-f(0)}{h}$ does not exist and hence $f$ is not differentiable at 0 . Thus $f$ is not a differentiable function.

### 5.3.1 Derivatives of composite functions

To study derivative of composite functions, we start with an illustrative example. Say, we want to find the derivative of $f$, where

$$
f(x)=(2 x+1)^{3}
$$

One way is to expand $(2 x+1)^{3}$ using binomial theorem and find the derivative as a polynomial function as illustrated below.

$$
\begin{aligned}
\frac{d}{d x} f(x) & =\frac{d}{d x}\left[(2 x+1)^{3}\right] \\
& =\frac{d}{d x}\left(8 x^{3}+12 x^{2}+6 x+1\right) \\
& =24 x^{2}+24 x+6 \\
& =6(2 x+1)^{2} \\
f(x) & =(h \circ g)(x)
\end{aligned}
$$

Now, observe that
where $g(x)=2 x+1$ and $h(x)=x^{3}$. Put $t=g(x)=2 x+1$. Then $f(x)=h(t)=t^{3}$. Thus

$$
\frac{d f}{d x}=6(2 x+1)^{2}=3(2 x+1)^{2} \cdot 2=3 t^{2} \cdot 2=\frac{d h}{d t} \cdot \frac{d t}{d x}
$$

The advantage with such observation is that it simplifies the calculation in finding the derivative of, say, $(2 x+1)^{100}$. We may formalise this observation in the following theorem called the chain rule.
Theorem 4 (Chain Rule) Let $f$ be a real valued function which is a composite of two functions $u$ and $v$; i.e., $f=v \mathrm{o} u$. Suppose $t=u(x)$ and if both $\frac{d t}{d x}$ and $\frac{d v}{d t}$ exist, we have

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}
$$

We skip the proof of this theorem. Chain rule may be extended as follows. Suppose $f$ is a real valued function which is a composite of three functions $u, v$ and $w$; i.e.,
$f=(w \circ u) \circ v$. If $t=v(x)$ and $s=u(t)$, then

$$
\frac{d f}{d x}=\frac{d(w \mathrm{o} u)}{d t} \cdot \frac{d t}{d x}=\frac{d w}{d s} \cdot \frac{d s}{d t} \cdot \frac{d t}{d x}
$$

provided all the derivatives in the statement exist. Reader is invited to formulate chain rule for composite of more functions.

Example 21 Find the derivative of the function given by $f(x)=\sin \left(x^{2}\right)$.
Solution Observe that the given function is a composite of two functions. Indeed, if $t=u(x)=x^{2}$ and $v(t)=\sin t$, then

$$
f(x)=(v \circ u)(x)=v(u(x))=v\left(x^{2}\right)=\sin x^{2}
$$

Put $t=u(x)=x^{2}$. Observe that $\frac{d v}{d t}=\cos t$ and $\frac{d t}{d x}=2 x$ exist. Hence, by chain rule

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}=\cos t \cdot 2 x
$$

It is normal practice to express the final result only in terms of $x$. Thus

$$
\frac{d f}{d x}=\cos t \cdot 2 x=2 x \cos x^{2}
$$

## EXERCISE 5.2

Differentiate the functions with respect to $x$ in Exercises 1 to 8 .

1. $\sin \left(x^{2}+5\right)$
2. $\cos (\sin x)$
3. $\sin (a x+b)$
4. $\sec (\tan (\sqrt{x}))$
5. $\frac{\sin (a x+b)}{\cos (c x+d)}$
6. $\cos x^{3} \cdot \sin ^{2}\left(x^{5}\right)$
7. $2 \sqrt{\cot \left(x^{2}\right)}$
8. $\cos (\sqrt{x})$
9. Prove that the function $f$ given by

$$
f(x)=|x-1|, x \in \mathbf{R}
$$

is not differentiable at $x=1$.
10. Prove that the greatest integer function defined by

$$
f(x)=[x], 0<x<3
$$

is not differentiable at $x=1$ and $x=2$.

### 5.3.2 Derivatives of implicit functions

Until now we have been differentiating various functions given in the form $y=f(x)$. But it is not necessary that functions are always expressed in this form. For example, consider one of the following relationships between $x$ and $y$ :

$$
\begin{array}{r}
x-y-\pi=0 \\
x+\sin x y-y=0
\end{array}
$$

In the first case, we can solve for $y$ and rewrite the relationship as $y=x-\pi$. In the second case, it does not seem that there is an easy way to solve for $y$. Nevertheless, there is no doubt about the dependence of $y$ on $x$ in either of the cases. When a relationship between $x$ and $y$ is expressed in a way that it is easy to solve for $y$ and write $y=f(x)$, we say that $y$ is given as an explicit function of $x$. In the latter case it
is implicit that $y$ is a function of $x$ and we say that the relationship of the second type, above, gives function implicitly. In this subsection, we learn to differentiate implicit functions.

Example 22 Find $\frac{d y}{d x}$ if $x-y=\pi$.
Solution One way is to solve for $y$ and rewrite the above as

$$
y=x-\pi
$$

But then

$$
\frac{d y}{d x}=1
$$

Alternatively, directly differentiating the relationship w.r.t., $x$, we have

$$
\frac{d}{d x}(x-y)=\frac{d \pi}{d x}
$$

Recall that $\frac{d \pi}{d x}$ means to differentiate the constant function taking value $\pi$ everywhere w.r.t., $x$. Thus

$$
\frac{d}{d x}(x)-\frac{d}{d x}(y)=0
$$

which implies that

$$
\frac{d y}{d x}=\frac{d x}{d x}=1
$$

Example 23 Find $\frac{d y}{d x}$, if $y+\sin y=\cos x$.
Solution We differentiate the relationship directly with respect to $x$, i.e.,

$$
\frac{d y}{d x}+\frac{d}{d x}(\sin y)=\frac{d}{d x}(\cos x)
$$

which implies using chain rule

$$
\frac{d y}{d x}+\cos y \cdot \frac{d y}{d x}=-\sin x
$$

This gives

$$
\frac{d y}{d x}=-\frac{\sin x}{1+\cos y}
$$

where

$$
y \neq(2 n+1) \pi
$$

### 5.3.3 Derivatives of inverse trigonometric functions

We remark that inverse trigonometric functions are continuous functions, but we will not prove this. Now we use chain rule to find derivatives of these functions.

Example 24 Find the derivative of $f$ given by $f(x)=\sin ^{-1} x$ assuming it exists.
Solution Let $y=\sin ^{-1} x$. Then, $x=\sin y$.
Differentiating both sides w.r.t. $x$, we get

$$
1=\cos y \frac{d y}{d x}
$$

which implies that

$$
\frac{d y}{d x}=\frac{1}{\cos y}=\frac{1}{\cos \left(\sin ^{-1} x\right)}
$$

Observe that this is defined only for $\cos y \neq 0$, i.e., $\sin ^{-1} x \neq-\frac{\pi}{2}, \frac{\pi}{2}$, i.e., $x \neq-1,1$, i.e., $x \in(-1,1)$.

To make this result a bit more attractive, we carry out the following manipulation. Recall that for $x \in(-1,1), \sin \left(\sin ^{-1} x\right)=x$ and hence

$$
\cos ^{2} y=1-(\sin y)^{2}=1-\left(\sin \left(\sin ^{-1} x\right)\right)^{2}=1-x^{2}
$$

Also, since $y \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right), \cos y$ is positive and hence $\cos y=\sqrt{1-x^{2}}$
Thus, for $x \in(-1,1)$,

$$
\frac{d y}{d x}=\frac{1}{\cos y}=\frac{1}{\sqrt{1-x^{2}}}
$$

| $f(x)$ | $\sin ^{-1} x$ | $\cos ^{-1} x$ | $\tan ^{-1} x$ |
| :---: | :---: | :---: | :---: |
| $f^{1}(x)$ | $1 / \sqrt{1-x^{2}}$ | $-1 / \sqrt{1-x^{2}}$ | $1 / 1+x^{2}$ |
| Domain off | $(-1,1)$ | $(-1,1)$ | R |

## EXERCISE 5.3

Find $\frac{d y}{d x}$ in the following:

1. $2 x+3 y=\sin x$
2. $2 x+3 y=\sin y$
3. $a x+b y^{2}=\cos y$
4. $x y+y^{2}=\tan x+y$
5. $x^{2}+x y+y^{2}=100$
6. $x^{3}+x^{2} y+x y^{2}+y^{3}=81$
7. $\sin ^{2} y+\cos x y=\kappa$
8. $\sin ^{2} x+\cos ^{2} y=1$
9. $y=\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right)$
10. $y=\tan ^{-1}\left(\frac{3 x-x^{3}}{1-3 x^{2}}\right),-\frac{1}{\sqrt{3}}<x<\frac{1}{\sqrt{3}}$
11. $y=\cos ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right), 0<x<1$
12. $y=\sin ^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right), 0<x<1$
13. $y=\cos ^{-1}\left(\frac{2 x}{1+x^{2}}\right),-1<x<1$
14. $y=\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right),-\frac{1}{\sqrt{2}}<x<\frac{1}{\sqrt{2}}$
15. $y=\sec ^{-1}\left(\frac{1}{2 x^{2}-1}\right), 0<x<\frac{1}{\sqrt{2}}$

### 5.4 Exponential and Logarithmic Functions

Till now we have learnt some aspects of different classes of functions like polynomial functions, rational functions and trigonometric functions. In this section, we shall learn about a new class of (related) functions called exponential functions and logarithmic functions. It needs to be emphasized that many statements made in this section are motivational and precise proofs of these are well beyond the scope of this text.

The Fig 5.9 gives a sketch of $y=f_{1}(x)=x, y=f_{2}(x)=x^{2}, y=f_{3}(x)=x^{3}$ and $y=f_{4}(x)$ $=x^{4}$. Observe that the curves get steeper as the power of $x$ increases. Steeper the curve, faster is the rate of growth. What this means is that for a fixed increment in the value of $x(>1)$, the increment in the value of $y=f_{n}(x)$ increases as $n$ increases for $n$ $=1,2,3,4$. It is conceivable that such a statement is true for all positive values of $n$,
where $f_{n}(x)=x^{n}$. Essentially, this means that the graph of $y=f_{n}(x)$ leans more towards the $y$-axis as $n$ increases. For example, consider $f_{10}(x)=x^{10}$ and $f_{15}(x)$ $=x^{15}$. If $x$ increases from 1 to $2, f_{10}$ increases from 1 to $2^{10}$ whereas $f_{15}$ increases from 1 to $2^{15}$. Thus, for the same increment in $x, f_{15}$ grow faster than $f_{10}$.

Upshot of the above discussion is that the growth of polynomial functions is dependent on the degree of the polynomial function - higher the degree, greater is the growth. The next natural question is:
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-23.jpg?height=632&width=664&top_left_y=292&top_left_x=807)

Fig 5.9

Is there a function which grows faster than any polynomial function. The answer is in affirmative and an example of such a function is

$$
y=f(x)=10^{x} .
$$

Our claim is that this function $f$ grows faster than $f_{n}(x)=x^{n}$ for any positive integer $n$. For example, we can prove that $10^{x}$ grows faster than $f_{100}(x)=x^{100}$. For large values of $x$ like $x=10^{3}$, note that $f_{100}(x)=\left(10^{3}\right)^{100}=10^{300}$ whereas $f\left(10^{3}\right)=10^{10^{3}}=10^{1000}$. Clearly $f(x)$ is much greater than $f_{100}(x)$. It is not difficult to prove that for all $x>10^{3}, f(x)>f_{100}(x)$. But we will not attempt to give a proof of this here. Similarly, by choosing large values of $x$, one can verify that $f(x)$ grows faster than $f_{n}(x)$ for any positive integer $n$.

Definition 3 The exponential function with positive base $b>1$ is the function

$$
y=f(x)=b^{x}
$$

The graph of $y=10^{x}$ is given in the Fig 5.9.
It is advised that the reader plots this graph for particular values of $b$ like 2,3 and 4. Following are some of the salient features of the exponential functions:
(1) Domain of the exponential function is $\mathbf{R}$, the set of all real numbers.
(2) Range of the exponential function is the set of all positive real numbers.
(3) The point $(0,1)$ is always on the graph of the exponential function (this is a restatement of the fact that $b^{0}=1$ for any real $b>1$ ).
(4) Exponential function is ever increasing; i.e., as we move from left to right, the graph rises above.
(5) For very large negative values of $x$, the exponential function is very close to 0 . In other words, in the second quadrant, the graph approaches $x$-axis (but never meets it).
Exponential function with base 10 is called the common exponential function. In the Appendix A.1.4 of Class XI, it was observed that the sum of the series

$$
1+\frac{1}{1!}+\frac{1}{2!}+\ldots
$$

is a number between 2 and 3 and is denoted by $e$. Using this $e$ as the base we obtain an extremely important exponential function $y=e^{x}$.

This is called natural exponential function.
It would be interesting to know if the inverse of the exponential function exists and has nice interpretation. This search motivates the following definition.

Definition 4 Let $b>1$ be a real number. Then we say logarithm of $a$ to base $b$ is $x$ if $b^{x}=a$.

Logarithm of $a$ to base $b$ is denoted by $\log _{b} a$. Thus $\log _{b} a=x$ if $b^{x}=a$. Let us work with a few explicit examples to get a feel for this. We know $2^{3}=8$. In terms of logarithms, we may rewrite this as $\log _{2} 8=3$. Similarly, $10^{4}=10000$ is equivalent to saying $\log _{10} 10000=4$. Also, $625=5^{4}=25^{2}$ is equivalent to saying $\log _{5} 625=4$ or $\log _{25} 625=2$.

On a slightly more mature note, fixing a base $b>1$, we may look at logarithm as a function from positive real numbers to all real numbers. This function, called the logarithmic function, is defined by

$$
\begin{aligned}
\log _{b}: \mathbf{R}^{+} & \rightarrow \mathbf{R} \\
x & \rightarrow \log _{b} x=y \quad \text { if } b^{y}=x
\end{aligned}
$$

As before if the base $b=10$, we say it is common logarithms and if $b=e$, then we say it is natural logarithms. Often natural logarithm is denoted by ln. In this chapter, $\log x$ denotes the logarithm function to base e, i.e., $\ln x$ will be written as simply $\log x$. The Fig 5.10 gives the plots of logarithm function to base $2, e$ and 10 .

Some of the important observations about the logarithm function to any base $b>1$ are listed below:
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-24.jpg?height=534&width=646&top_left_y=1521&top_left_x=825)

Fig 5.10
(1) We cannot make a meaningful definition of logarithm of non-positive numbers and hence the domain of $\log$ function is $\mathbf{R}^{+}$.
(2) The range of $\log$ function is the set of all real numbers.
(3) The point $(1,0)$ is always on the graph of the log function.
(4) The log function is ever increasing, i.e., as we move from left to right the graph rises above.
(5) For $x$ very near to zero, the value of $\log x$ can be made lesser than any given real number. In other words in the fourth quadrant the graph approaches $y$-axis (but never meets it).
(6) Fig 5.11 gives the plot of $y=e^{x}$ and $y=\ln x$. It is of interest to observe that the two curves are the mirror
![](https://cdn.mathpix.com/cropped/2025_07_21_3a79fb6dc7d8b8025edeg-25.jpg?height=519&width=646&top_left_y=557&top_left_x=816)

Fig 5.11 images of each other reflected in the line $y=x$.
Two properties of 'log' functions are proved below:
(1) There is a standard change of base rule to obtain $\log _{a} p$ in terms of $\log _{b} p$. Let $\log _{a} p=\alpha, \log _{b} p=\beta$ and $\log _{b} a=\gamma$. This means $a^{\alpha}=p, b^{\beta}=p$ and $b^{\gamma}=a$.
Substituting the third equation in the first one, we have

$$
\left(b^{\gamma}\right)^{\alpha}=b^{\gamma \alpha}=p
$$

Using this in the second equation, we get

$$
b^{\beta}=p=b^{\gamma \alpha}
$$

which implies $\quad \beta=\alpha \gamma$ or $\alpha=\frac{\beta}{\gamma}$. But then

$$
\log _{a} p=\frac{\log _{b} p}{\log _{b} a}
$$

(2) Another interesting property of the log function is its effect on products. Let $\log _{b} p q=\alpha$. Then $b^{\alpha}=p q$. If $\log _{b} p=\beta$ and $\log _{b} q=\gamma$, then $b^{\beta}=p$ and $b^{\gamma}=q$. But then $b^{\alpha}=p q=b^{\beta} b^{\gamma}=b^{\beta+\gamma}$
which implies $\alpha=\beta+\gamma$, i.e.,

$$
\log _{b} p q=\log _{b} p+\log _{b} q
$$

A particularly interesting and important consequence of this is when $p=q$. In this case the above may be rewritten as

$$
\log _{b} p^{2}=\log _{b} p+\log _{b} p=2 \log p
$$

An easy generalisation of this (left as an exercise!) is

$$
\log _{b} p^{n}=n \log p
$$

for any positive integer $n$. In fact this is true for any real number $n$, but we will not attempt to prove this. On the similar lines the reader is invited to verify

$$
\log _{b} \frac{x}{y}=\log _{b} x-\log _{b} y
$$

Example 25 Is it true that $x=e^{\log x}$ for all real $x$ ?
Solution First, observe that the domain of log function is set of all positive real numbers. So the above equation is not true for non-positive real numbers. Now, let $y=e^{\log x}$. If $y>0$, we may take logarithm which gives us $\log y=\log \left(e^{\log x}\right)=\log x \cdot \log e=\log x$. Thus $y=x$. Hence $x=e^{\log x}$ is true only for positive values of $x$.

One of the striking properties of the natural exponential function in differential calculus is that it doesn't change during the process of differentiation. This is captured in the following theorem whose proof we skip.

## Theorem 5*

(1) The derivative of $e^{x}$ w.r.t., $x$ is $e^{x}$; i.e., $\frac{d}{d x}\left(e^{x}\right)=e^{x}$.
(2) The derivative of $\log x$ w.r.t., $x$ is $\frac{1}{x}$; i.e., $\frac{d}{d x}(\log x)=\frac{1}{x}$.

Example 26 Differentiate the following w.r.t. $x$ :
(i) $e^{-x}$
(ii) $\sin (\log x), x>0$
(iii) $\cos ^{-1}\left(e^{x}\right)$
(iv) $e^{\cos x}$

## Solution

(i) Let $y=e^{-x}$. Using chain rule, we have

$$
\frac{d y}{d x}=e^{-x} \cdot \frac{d}{d x}(-x)=-e^{-x}
$$

(ii) Let $y=\sin (\log x)$. Using chain rule, we have

$$
\frac{d y}{d x}=\cos (\log x) \cdot \frac{d}{d x}(\log x)=\frac{\cos (\log x)}{x}
$$

[^0](iii) Let $y=\cos ^{-1}\left(e^{x}\right)$. Using chain rule, we have
$$
\frac{d y}{d x}=\frac{-1}{\sqrt{1-\left(e^{x}\right)^{2}}} \cdot \frac{d}{d x}\left(e^{x}\right)=\frac{-e^{x}}{\sqrt{1-e^{2 x}}}
$$
(iv) Let $y=e^{\cos x}$. Using chain rule, we have
$$
\frac{d y}{d x}=e^{\cos x} \cdot(-\sin x)=-(\sin x) e^{\cos x}
$$

## EXERCISE 5.4

Differentiate the following w.r.t. $x$ :

1. $\frac{e^{x}}{\sin x}$
2. $e^{\sin ^{-1} x}$
3. $e^{x^{3}}$
4. $\sin \left(\tan ^{-1} e^{-x}\right)$
5. $\log \left(\cos e^{x}\right)$
6. $e^{x}+e^{x^{2}}+\ldots+e^{x^{5}}$
7. $\sqrt{e^{\sqrt{x}}}, x>0$
8. $\log (\log x), x>1$
9. $\frac{\cos x}{\log x}, x>0$
10. $\cos \left(\log x+e^{x}\right), x>0$

### 5.5. Logarithmic Differentiation

In this section, we will learn to differentiate certain special class of functions given in the form

$$
y=f(x)=[u(x)]^{v(x)}
$$

By taking logarithm (to base $e$ ) the above may be rewritten as

$$
\log y=v(x) \log [u(x)]
$$

Using chain rule we may differentiate this to get

$$
\frac{1}{y} \cdot \frac{d y}{d x}=v(x) \cdot \frac{1}{u(x)} \cdot u^{\prime}(x)+v^{\prime}(x) \cdot \log [u(x)]
$$

which implies that

$$
\frac{d y}{d x}=y\left[\frac{v(x)}{u(x)} \cdot u^{\prime}(x)+v^{\prime}(x) \cdot \log [u(x)]\right]
$$

The main point to be noted in this method is that $f(x)$ and $u(x)$ must always be positive as otherwise their logarithms are not defined. This process of differentiation is known as logarithms differentiation and is illustrated by the following examples:

Example 27 Differentiate $\sqrt{\frac{(x-3)\left(x^{2}+4\right)}{3 x^{2}+4 x+5}}$ w.r.t. $x$.
Solution Let $y=\sqrt{\frac{(x-3)\left(x^{2}+4\right)}{\left(3 x^{2}+4 x+5\right)}}$
Taking logarithm on both sides, we have

$$
\log y=\frac{1}{2}\left[\log (x-3)+\log \left(x^{2}+4\right)-\log \left(3 x^{2}+4 x+5\right)\right]
$$

Now, differentiating both sides w.r.t. $x$, we get
or

$$
\begin{aligned}
\frac{1}{y} \cdot \frac{d y}{d x} & =\frac{1}{2}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right] \\
\frac{d y}{d x} & =\frac{y}{2}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right] \\
& =\frac{1}{2} \sqrt{\frac{(x-3)\left(x^{2}+4\right)}{3 x^{2}+4 x+5}}\left[\frac{1}{(x-3)}+\frac{2 x}{x^{2}+4}-\frac{6 x+4}{3 x^{2}+4 x+5}\right]
\end{aligned}
$$

Example 28 Differentiate $a^{x}$ w.r.t. $x$, where $a$ is a positive constant.
Solution Let $y=a^{x}$. Then

$$
\log y=x \log a
$$

Differentiating both sides w.r.t. $x$, we have
or

$$
\frac{1}{y} \frac{d y}{d x}=\log a
$$

$$
\frac{d y}{d x}=y \log a
$$

Thus

$$
\frac{d}{d x}\left(a^{x}\right)=a^{x} \log a
$$

Alternatively

$$
\begin{aligned}
\frac{d}{d x}\left(a^{x}\right) & =\frac{d}{d x}\left(e^{x \log a}\right)=e^{x \log a} \frac{d}{d x}(x \log a) \\
& =e^{x \log a} \cdot \log a=a^{x} \log a
\end{aligned}
$$

Example 29 Differentiate $x^{\sin x}, x>0$ w.r.t. $x$.
Solution Let $y=x^{\sin x}$. Taking logarithm on both sides, we have

Therefore

$$
\log y=\sin x \log x
$$

or

$$
\frac{1}{y} \cdot \frac{d y}{d x}=\sin x \frac{d}{d x}(\log x)+\log x \frac{d}{d x}(\sin x)
$$

or

$$
\frac{1}{y} \frac{d y}{d x}=(\sin x) \frac{1}{x}+\log x \cos x
$$

$$
\begin{aligned}
\frac{d y}{d x} & =y\left[\frac{\sin x}{x}+\cos x \log x\right] \\
& =x^{\sin x}\left[\frac{\sin x}{x}+\cos x \log x\right] \\
& =x^{\sin x-1} \cdot \sin x+x^{\sin x} \cdot \cos x \log x
\end{aligned}
$$

Example 30 Find $\frac{d y}{d x}$, if $y^{x}+x^{y}+x^{x}=a^{b}$.
Solution Given that $y^{x}+x^{y}+x^{x}=a^{b}$.
Putting $u=y^{x}, v=x^{y}$ and $w=x^{x}$, we get $u+v+w=a^{b}$

Therefore

$$
\begin{equation*}
\frac{d u}{d x}+\frac{d v}{d x}+\frac{d w}{d x}=0 \tag{1}
\end{equation*}
$$

Now, $u=y^{x}$. Taking logarithm on both sides, we have

$$
\log u=x \log y
$$

Differentiating both sides w.r.t. $x$, we have

So

$$
\begin{align*}
\frac{1}{u} \cdot \frac{d u}{d x} & =x \frac{d}{d x}(\log y)+\log y \frac{d}{d x}(x) \\
& =x \frac{1}{y} \cdot \frac{d y}{d x}+\log y \cdot 1 \\
\frac{d u}{d x} & =u\left(\frac{x}{y} \frac{d y}{d x}+\log y\right)=y^{x}\left[\frac{x}{y} \frac{d y}{d x}+\log y\right] \tag{2}
\end{align*}
$$

Also $v=x^{y}$

Taking logarithm on both sides, we have

$$
\log v=y \log x
$$

Differentiating both sides w.r.t. $x$, we have

So

$$
\begin{aligned}
\frac{1}{v} \cdot \frac{d v}{d x} & =y \frac{d}{d x}(\log x)+\log x \frac{d y}{d x} \\
& =y \cdot \frac{1}{x}+\log x \cdot \frac{d y}{d x}
\end{aligned}
$$

楼

$$
\begin{align*}
\frac{d v}{d x} & =v\left[\frac{y}{x}+\log x \frac{d y}{d x}\right] \\
& =x^{y}\left[\frac{y}{x}+\log x \frac{d y}{d x}\right]  \tag{3}\\
w & =x^{x}
\end{align*}
$$

Again
Taking logarithm on both sides, we have

$$
\log w=x \log x
$$

Differentiating both sides w.r.t. $x$, we have

$$
\begin{aligned}
\frac{1}{w} \cdot \frac{d w}{d x} & =x \frac{d}{d x}(\log x)+\log x \cdot \frac{d}{d x}(x) \\
& =x \cdot \frac{1}{x}+\log x \cdot 1
\end{aligned}
$$

i.e.

$$
\begin{align*}
\frac{d w}{d x} & =w(1+\log x) \\
& =x^{x}(1+\log x) \tag{4}
\end{align*}
$$

From (1), (2), (3), (4), we have
or

$$
\begin{aligned}
\left(x \cdot y^{x-1}+x^{y} \cdot \log x\right) \frac{d y}{d x} & =-x^{x}(1+\log x)-y \cdot x^{y-1}-y^{x} \log y \\
\frac{d y}{d x} & =\frac{-\left[y^{x} \log y+y \cdot x^{y-1}+x^{x}(1+\log x)\right]}{x \cdot y^{x-1}+x^{y} \log x}
\end{aligned}
$$

Therefore

$$
y^{x}\left(\frac{x}{y} \frac{d y}{d x}+\log y\right)+x^{y}\left(\frac{y}{x}+\log x \frac{d y}{d x}\right)+x^{x}(1+\log x)=0
$$

## EXERCISE 5.5

Differentiate the functions given in Exercises 1 to 11 w.r.t. $x$.

1. $\cos x \cdot \cos 2 x \cdot \cos 3 x$
2. $\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}$
3. $(\log x)^{\cos x}$
4. $x^{x}-2^{\sin x}$
5. $(x+3)^{2} \cdot(x+4)^{3} \cdot(x+5)^{4}$
6. $\left(x+\frac{1}{x}\right)^{x}+x^{\left(1+\frac{1}{x}\right)}$
7. $(\log x)^{x}+x^{\log x}$
8. $(\sin x)^{x}+\sin ^{-1} \sqrt{x}$
9. $x^{\sin x}+(\sin x)^{\cos x}$
10. $x^{x \cos x}+\frac{x^{2}+1}{x^{2}-1}$
11. $(x \cos x)^{x}+(x \sin x)^{\frac{1}{x}}$

Find $\frac{d y}{d x}$ of the functions given in Exercises 12 to 15.
12. $x^{y}+y^{x}=1$
13. $y^{x}=x^{y}$
14. $(\cos x)^{y}=(\cos y)^{x}$
15. $x y=e^{(x-y)}$
16. Find the derivative of the function given by $f(x)=(1+x)\left(1+x^{2}\right)\left(1+x^{4}\right)\left(1+x^{8}\right)$ and hence find $f^{\prime}(1)$.
17. Differentiate $\left(x^{2}-5 x+8\right)\left(x^{3}+7 x+9\right)$ in three ways mentioned below:
(i) by using product rule
(ii) by expanding the product to obtain a single polynomial.
(iii) by logarithmic differentiation.

Do they all give the same answer?
18. If $u, v$ and $w$ are functions of $x$, then show that

$$
\frac{d}{d x}(u \cdot v \cdot w)=\frac{d u}{d x} v \cdot w+u \cdot \frac{d v}{d x} \cdot w+u \cdot v \frac{d w}{d x}
$$

in two ways - first by repeated application of product rule, second by logarithmic differentiation.

### 5.6 Derivatives of Functions in Parametric Forms

Sometimes the relation between two variables is neither explicit nor implicit, but some link of a third variable with each of the two variables, separately, establishes a relation between the first two variables. In such a situation, we say that the relation between
them is expressed via a third variable. The third variable is called the parameter. More precisely, a relation expressed between two variables $x$ and $y$ in the form $x=f(t), y=g(t)$ is said to be parametric form with $t$ as a parameter.

In order to find derivative of function in such form, we have by chain rule.

$$
\frac{d y}{d t}=\frac{d y}{d x} \cdot \frac{d x}{d t}
$$

or

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}\left(\text { whenever } \frac{d x}{d t} \neq 0\right)
$$

Thus

$$
\frac{d y}{d x}=\frac{g^{\prime}(t)}{f^{\prime}(t)}\left(\text { as } \frac{d y}{d t}=g^{\prime}(t) \text { and } \frac{d x}{d t}=f^{\prime}(t)\right)\left[\text { provided } f^{\prime}(t) \neq 0\right]
$$

Example 31 Find $\frac{d y}{d x}$, if $x=a \cos \theta, y=a \sin \theta$.
Solution Given that

$$
x=a \cos \theta, y=a \sin \theta
$$

Therefore

$$
\frac{d x}{d \theta}=-a \sin \theta, \frac{d y}{d \theta}=a \cos \theta
$$

Hence

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{a \cos \theta}{-a \sin \theta}=-\cot \theta
$$

Example 32 Find $\frac{d y}{d x}$, if $x=a t^{2}, y=2 a t$.
Solution Given that $x=a t^{2}, y=2 a t$
So

$$
\frac{d x}{d t}=2 a t \quad \text { and } \quad \frac{d y}{d t}=2 a
$$

Therefore

$$
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{2 a}{2 a t}=\frac{1}{t}
$$

Example 33 Find $\frac{d y}{d x}$, if $x=a(\theta+\sin \theta), y=a(1-\cos \theta)$.
Solution We have $\frac{d x}{d \theta}=a(1+\cos \theta), \frac{d y}{d \theta}=a(\sin \theta)$

Therefore

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{a \sin \theta}{a(1+\cos \theta)}=\tan \frac{\theta}{2}
$$

$\approx$ Note It may be noted here that $\frac{d y}{d x}$ is expressed in terms of parameter only without directly involving the main variables $x$ and $y$.

Example 34 Find $\frac{d y}{d x}$, if $x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}}$.
Solution Let $x=a \cos ^{3} \theta, y=a \sin ^{3} \theta$. Then

$$
\begin{aligned}
x^{\frac{2}{3}}+y^{\frac{2}{3}} & =\left(a \cos ^{3} \theta\right)^{\frac{2}{3}}+\left(a \sin ^{3} \theta\right)^{\frac{2}{3}} \\
& =a^{\frac{2}{3}}\left(\cos ^{2} \theta+\left(\sin ^{2} \theta\right)=a^{\frac{2}{3}}\right.
\end{aligned}
$$

Hence, $x=a \cos ^{3} \theta, y=a \sin ^{3} \theta$ is parametric equation of $x^{\frac{2}{3}}+y^{\frac{2}{3}}=a^{\frac{2}{3}}$

Now $\frac{d x}{d \theta}=-3 a \cos ^{2} \theta \sin \theta$ and $\frac{d y}{d \theta}=3 a \sin ^{2} \theta \cos \theta$

Therefore

$$
\frac{d y}{d x}=\frac{\frac{d y}{d \theta}}{\frac{d x}{d \theta}}=\frac{3 a \sin ^{2} \theta \cos \theta}{-3 a \cos ^{2} \theta \sin \theta}=-\tan \theta=-\sqrt[3]{\frac{y}{x}}
$$

## EXERCISE 5.6

If $x$ and $y$ are connected parametrically by the equations given in Exercises 1 to 10, without eliminating the parameter, Find $\frac{d y}{d x}$.

1. $x=2 a t^{2}, y=a t^{4}$
2. $x=a \cos \theta, y=b \cos \theta$
3. $x=\sin t, y=\cos 2 t$
4. $x=4 t, y=\frac{4}{t}$
5. $x=\cos \theta-\cos 2 \theta, y=\sin \theta-\sin 2 \theta$
6. $x=a(\theta-\sin \theta), y=a(1+\cos \theta)$ 7. $x=\frac{\sin ^{3} t}{\sqrt{\cos 2 t}}, y=\frac{\cos ^{3} t}{\sqrt{\cos 2 t}}$
7. $x=a\left(\cos t+\log \tan \frac{t}{2}\right) y=a \sin t \quad 9 . x=a \sec \theta, y=b \tan \theta$
8. $x=a(\cos \theta+\theta \sin \theta), y=a(\sin \theta-\theta \cos \theta)$
9. If $x=\sqrt{a^{\sin ^{-1} t}}, y=\sqrt{a^{\cos ^{-1} t}}$, show that $\frac{d y}{d x}=-\frac{y}{x}$

### 5.7 Second Order Derivative

Let $\quad y=f(x)$. Then

$$
\begin{equation*}
\frac{d y}{d x}=f^{\prime}(x) \tag{1}
\end{equation*}
$$

If $f^{\prime}(x)$ is differentiable, we may differentiate (1) again w.r.t. $x$. Then, the left hand side becomes $\frac{d}{d x}\left(\frac{d y}{d x}\right)$ which is called the second order derivative of $y$ w.r.t. $x$ and is denoted by $\frac{d^{2} y}{d x^{2}}$. The second order derivative of $f(x)$ is denoted by $f^{\prime \prime}(x)$. It is also denoted by $\mathrm{D}^{2} y$ or $y^{\prime \prime}$ or $y_{2}$ if $y=f(x)$. We remark that higher order derivatives may be defined similarly.

Example 35 Find $\frac{d^{2} y}{d x^{2}}$, if $y=x^{3}+\tan x$.
Solution Given that $y=x^{3}+\tan x$. Then

Therefore

$$
\begin{aligned}
\frac{d y}{d x} & =3 x^{2}+\sec ^{2} x \\
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(3 x^{2}+\sec ^{2} x\right) \\
& =6 x+2 \sec x \cdot \sec x \tan x=6 x+2 \sec ^{2} x \tan x
\end{aligned}
$$

Example 36 If $y=\mathrm{A} \sin x+\mathrm{B} \cos x$, then prove that $\frac{d^{2} y}{d x^{2}}+y=0$.
Solution We have
and

$$
\frac{d y}{d x}=\mathrm{A} \cos x-\mathrm{B} \sin x
$$

Hence

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}(\mathrm{~A} \cos x-\mathrm{B} \sin x) \\
& =-\mathrm{A} \sin x-\mathrm{B} \cos x=-y
\end{aligned}
$$

Hence $\quad \frac{d^{2} y}{d x^{2}}+y=0$
Example 37 If $y=3 e^{2 x}+2 e^{3 x}$, prove that $\frac{d^{2} y}{d x^{2}}-5 \frac{d y}{d x}+6 y=0$.
Solution Given that $y=3 e^{2 x}+2 e^{3 x}$. Then

$$
\frac{d y}{d x}=6 e^{2 x}+6 e^{3 x}=6\left(e^{2 x}+e^{3 x}\right)
$$

Therefore

$$
\frac{d^{2} y}{d x^{2}}=12 e^{2 x}+18 e^{3 x}=6\left(2 e^{2 x}+3 e^{3 x}\right)
$$

Hence

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}}-5 \frac{d y}{d x}+6 y= & 6\left(2 e^{2 x}+3 e^{3 x}\right) \\
& -30\left(e^{2 x}+e^{3 x}\right)+6\left(3 e^{2 x}+2 e^{3 x}\right)=0
\end{aligned}
$$

Example 38 If $y=\sin ^{-1} x$, show that $\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}=0$.
Solution We have $y=\sin ^{-1} x$. Then
or

$$
\frac{d y}{d x}=\frac{1}{\sqrt{\left(1-x^{2}\right)}}
$$

So

$$
\sqrt{\left(1-x^{2}\right)} \frac{d y}{d x}=1
$$

or

$$
\frac{d}{d x}\left(\sqrt{\left(1-x^{2}\right)} \cdot \frac{d y}{d x}\right)=0
$$

$$
\sqrt{\left(1-x^{2}\right)} \cdot \frac{d^{2} y}{d x^{2}}+\frac{d y}{d x} \cdot \frac{d}{d x}\left(\sqrt{\left(1-x^{2}\right)}\right)=0
$$

or

$$
\sqrt{\left(1-x^{2}\right)} \cdot \frac{d^{2} y}{d x^{2}}-\frac{d y}{d x} \cdot \frac{2 x}{2 \sqrt{1-x^{2}}}=0
$$

Hence

$$
\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}=0
$$

Alternatively, Given that $y=\sin ^{-1} x$, we have

$$
y_{1}=\frac{1}{\sqrt{1-x^{2}}} \text {, i.e., }\left(1-x^{2}\right) y_{1}^{2}=1
$$

So

$$
\left(1-x^{2}\right) \cdot 2 y_{1} y_{2}+y_{1}^{2}(0-2 x)=0
$$

Hence

$$
\left(1-x^{2}\right) y_{2}-x y_{1}=0
$$

## EXERCISE 5.7

Find the second order derivatives of the functions given in Exercises 1 to 10.

1. $x^{2}+3 x+2$
2. $x^{20}$
3. $x \cdot \cos x$
4. $\log x$
5. $x^{3} \log x$
6. $e^{x} \sin 5 x$
7. $e^{6 x} \cos 3 x$
8. $\tan ^{-1} x$
9. $\log (\log x)$
10. $\sin (\log x)$
11. If $y=5 \cos x-3 \sin x$, prove that $\frac{d^{2} y}{d x^{2}}+y=0$
12. If $y=\cos ^{-1} x$, Find $\frac{d^{2} y}{d x^{2}}$ in terms of $y$ alone.
13. If $y=3 \cos (\log x)+4 \sin (\log x)$, show that $x^{2} y_{2}+x y_{1}+y=0$
14. If $y=\mathrm{A} e^{m x}+\mathrm{B} e^{n x}$, show that $\frac{d^{2} y}{d x^{2}}-(m+n) \frac{d y}{d x}+m n y=0$
15. If $y=500 e^{7 x}+600 e^{-7 x}$, show that $\frac{d^{2} y}{d x^{2}}=49 y$
16. If $e^{y}(x+1)=1$, show that $\frac{d^{2} y}{d x^{2}}=\left(\frac{d y}{d x}\right)^{2}$
17. If $y=\left(\tan ^{-1} x\right)^{2}$, show that $\left(x^{2}+1\right)^{2} y_{2}+2 x\left(x^{2}+1\right) y_{1}=2$

## Miscellaneous Examples

Example 39 Differentiate w.r.t. $x$, the following function:
(i) $\sqrt{3 x+2}+\frac{1}{\sqrt{2 x^{2}+4}}$
(ii) $\log _{7}(\log x)$

## Solution

(i) Let $y=\sqrt{3 x+2}+\frac{1}{\sqrt{2 x^{2}+4}}=(3 x+2)^{\frac{1}{2}}+\left(2 x^{2}+4\right)^{-\frac{1}{2}}$

Note that this function is defined at all real numbers $x>-\frac{2}{3}$. Therefore

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{1}{2}(3 x+2)^{\frac{1}{2}-1} \cdot \frac{d}{d x}(3 x+2)+\left(-\frac{1}{2}\right)\left(2 x^{2}+4\right)^{-\frac{1}{2}-1} \cdot \frac{d}{d x}\left(2 x^{2}+4\right) \\
& =\frac{1}{2}(3 x+2)^{-\frac{1}{2}} \cdot(3)-\frac{1}{2}\left(2 x^{2}+4\right)^{-\frac{3}{2}} \cdot 4 x \\
& =\frac{3}{2 \sqrt{3 x+2}}-\frac{2 x}{\left(2 x^{2}+4\right)^{\frac{3}{2}}}
\end{aligned}
$$

This is defined for all real numbers $x>-\frac{2}{3}$.
(ii) Let $y=\log _{7}(\log x)=\frac{\log (\log x)}{\log 7}$ (by change of base formula).

The function is defined for all real numbers $x>1$. Therefore

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{1}{\log 7} \frac{d}{d x}(\log (\log x)) \\
& =\frac{1}{\log 7} \frac{1}{\log x} \cdot \frac{d}{d x}(\log x) \\
& =\frac{1}{x \log 7 \log x}
\end{aligned}
$$

Example 40 Differentiate the following w.r.t. $x$.
(i) $\cos ^{-1}(\sin x)$
(ii) $\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right)$
(iii) $\sin ^{-1}\left(\frac{2^{x+1}}{1+4^{x}}\right)$

## Solution

(i) Let $f(x)=\cos ^{-1}(\sin x)$. Observe that this function is defined for all real numbers. We may rewrite this function as

$$
\begin{aligned}
f(x) & =\cos ^{-1}(\sin x) \\
& =\cos ^{-1} \cos \frac{\pi}{2}-x \\
& =\frac{\pi}{2}-x
\end{aligned}
$$

Thus

$$
f^{\prime}(x)=-1 .
$$

(ii) Let $f(x)=\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right)$. Observe that this function is defined for all real numbers, where $\cos x \neq-1$; i.e., at all odd multiplies of $\pi$. We may rewrite this function as

$$
\begin{aligned}
f(x) & =\tan ^{-1}\left(\frac{\sin x}{1+\cos x}\right) \\
& =\tan ^{-1}\left[\frac{2 \sin \left(\frac{x}{2}\right) \cos \left(\frac{x}{2}\right)}{2 \cos ^{2} \frac{x}{2}}\right]
\end{aligned}
$$

$$
=\tan ^{-1}\left[\tan \left(\frac{x}{2}\right)\right]=\frac{x}{2}
$$

Observe that we could cancel $\cos \left(\frac{x}{2}\right)$ in both numerator and denominator as it is not equal to zero. Thus $f^{\prime}(x)=\frac{1}{2}$.
(iii) Let $f(x)=\sin ^{-1}\left(\frac{2^{x+1}}{1+4^{x}}\right)$. To find the domain of this function we need to find all $x$ such that $-1 \leq \frac{2^{x+1}}{1+4^{x}} \leq 1$. Since the quantity in the middle is always positive, we need to find all $x$ such that $\frac{2^{x+1}}{1+4^{x}} \leq 1$, i.e., all $x$ such that $2^{x+1} \leq 1+4^{x}$. We may rewrite this as $2 \leq \frac{1}{2^{x}}+2^{x}$ which is true for all $x$. Hence the function is defined at every real number. By putting $2^{x}=\tan \theta$, this function may be rewritten as

$$
\begin{aligned}
f(x) & =\sin ^{-1}\left[\frac{2^{x+1}}{1+4^{x}}\right] \\
& =\sin ^{-1} \frac{2^{x} \cdot 2}{1+\left(2^{x}\right)^{2}} \\
& =\sin ^{-1}\left[\frac{2 \tan \theta}{1+\tan ^{2} \theta}\right] \\
& =\sin ^{-1}[\sin 2 \theta] \\
& =2 \theta=2 \tan ^{-1}\left(2^{x}\right) \\
f^{\prime}(x) & =2 \cdot \frac{1}{1+\left(2^{x}\right)^{2}} \cdot \frac{d}{d x}\left(2^{x}\right) \\
& =\frac{2}{1+4^{x}} \cdot\left(2^{x}\right) \log 2 \\
& =\frac{2^{x+1} \log 2}{1+4^{x}}
\end{aligned}
$$

Thus

Example 41 Find $f^{\prime}(x)$ if $f(x)=(\sin x)^{\sin x}$ for all $0<x<\pi$.
Solution The function $y=(\sin x)^{\sin x}$ is defined for all positive real numbers. Taking logarithms, we have

$$
\log y=\log (\sin x)^{\sin x}=\sin x \log (\sin x)
$$

Then

$$
\begin{aligned}
\frac{1}{y} \frac{d y}{d x} & =\frac{d}{d x}(\sin x \log (\sin x)) \\
& =\cos x \log (\sin x)+\sin x \cdot \frac{1}{\sin x} \cdot \frac{d}{d x}(\sin x) \\
& =\cos x \log (\sin x)+\cos x \\
& =(1+\log (\sin x)) \cos x
\end{aligned}
$$

Thus

$$
\frac{d y}{d x}=y((1+\log (\sin x)) \cos x)=(1+\log (\sin x))(\sin x)^{\sin x} \cos x
$$

Example 42 For a positive constant $a$ find $\frac{d y}{d x}$, where

$$
y=a^{t+\frac{1}{t}} \text {, and } x=\left(t+\frac{1}{t}\right)^{a}
$$

Solution Observe that both $y$ and $x$ are defined for all real $t \neq 0$. Clearly

$$
\begin{aligned}
\frac{d y}{d t}=\frac{d}{d t}\left(a^{t+\frac{1}{t}}\right) & =a^{t+\frac{1}{t}} \frac{d}{d t}\left(t+\frac{1}{t}\right) \cdot \log a \\
& =a^{t+\frac{1}{t}}\left(1-\frac{1}{t^{2}}\right) \log a \\
\frac{d x}{d t} & =a\left[t+\frac{1}{t}\right]^{a-1} \cdot \frac{d}{d t}\left(t+\frac{1}{t}\right) \\
& =a\left[t+\frac{1}{t}\right]^{a-1} \cdot\left(1-\frac{1}{t^{2}}\right)
\end{aligned}
$$

Similarly
$\frac{d x}{d t} \neq 0$ only if $t \neq \pm 1$. Thus for $t \neq \pm 1$,

$$
\begin{aligned}
\frac{d y}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}= & \frac{a^{t+\frac{1}{t}} 1-\frac{1}{t^{2}} \log a}{a t+\frac{1}{t}{ }^{a-1} \cdot 1-\frac{1}{t^{2}}} \\
& =\frac{a^{t+\frac{1}{t}} \log a}{a\left(t+\frac{1}{t}\right)^{a-1}}
\end{aligned}
$$

Example 43 Differentiate $\sin ^{2} x$ w.r.t. $e^{\cos x}$.
Solution Let $u(x)=\sin ^{2} x$ and $v(x)=e^{\cos x}$. We want to find $\frac{d u}{d v}=\frac{d u / d x}{d v / d x}$. Clearly

$$
\frac{d u}{d x}=2 \sin x \cos x \text { and } \frac{d v}{d x}=e^{\cos x}(-\sin x)=-(\sin x) e^{\cos x}
$$

Thus

$$
\frac{d u}{d v}=\frac{2 \sin x \cos x}{-\sin x e^{\cos x}}=-\frac{2 \cos x}{e^{\cos x}}
$$

## Miscellaneous Exercise on Chapter 5

Differentiate w.r.t. $x$ the function in Exercises 1 to 11.

1. $\left(3 x^{2}-9 x+5\right)^{9}$
2. $\sin ^{3} x+\cos ^{6} x$
3. $(5 x)^{3 \cos 2 x}$
4. $\sin ^{-1}(x \sqrt{x}), 0 \leq x \leq 1$
5. $\frac{\cos ^{-1} \frac{x}{2}}{\sqrt{2 x+7}},-2<x<2$
6. $\cot ^{-1}\left[\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right], 0<x<\frac{\pi}{2}$
7. $(\log x)^{\log x}, x>1$
8. $\cos (a \cos x+b \sin x)$, for some constant $a$ and $b$.
9. $(\sin x-\cos x)^{(\sin x-\cos x)}, \frac{\pi}{4}<x<\frac{3 \pi}{4}$
10. $x^{x}+x^{a}+a^{x}+a^{a}$, for some fixed $a>0$ and $x>0$
11. $x^{x^{2}-3}+(x-3)^{x^{2}}$, for $x>3$
12. Find $\frac{d y}{d x}$, if $y=12(1-\cos t), x=10(t-\sin t),-\frac{\pi}{2}<t<\frac{\pi}{2}$
13. Find $\frac{d y}{d x}$, if $y=\sin ^{-1} x+\sin ^{-1} \sqrt{1-x^{2}}, 0<x<1$
14. If $x \sqrt{1+y}+y \sqrt{1+x}=0$, for , $-1<x<1$, prove that

$$
\frac{d y}{d x}=-\frac{1}{(1+x)^{2}}
$$

15. If $(x-a)^{2}+(y-b)^{2}=c^{2}$, for some $c>0$, prove that

$$
\frac{\left[1+\left(\frac{d y}{d x}\right)^{2}\right]^{\frac{3}{2}}}{\frac{d^{2} y}{d x^{2}}}
$$

is a constant independent of $a$ and $b$.
16. If $\cos y=x \cos (a+y)$, with $\cos a \neq \pm 1$, prove that $\frac{d y}{d x}=\frac{\cos ^{2}(a+y)}{\sin a}$.
17. If $x=a(\cos t+t \sin t)$ and $y=a(\sin t-t \cos t)$, find $\frac{d^{2} y}{d x^{2}}$.
18. If $f(x)=|x|^{3}$, show that $f^{\prime \prime}(x)$ exists for all real $x$ and find it.
19. Using the fact that $\sin (\mathrm{A}+\mathrm{B})=\sin \mathrm{A} \cos \mathrm{B}+\cos \mathrm{A} \sin \mathrm{B}$ and the differentiation, obtain the sum formula for cosines.
20. Does there exist a function which is continuous everywhere but not differentiable at exactly two points? Justify your answer.
21. If $y=\left|\begin{array}{ccc}f(x) & g(x) & h(x) \\ l & m & n \\ a & b & c\end{array}\right|$, prove that $\frac{d y}{d x}=\left|\begin{array}{ccc}f^{\prime}(x) & g^{\prime}(x) & h^{\prime}(x) \\ l & m & n \\ a & b & c\end{array}\right|$
22. If $y=e^{a \cos ^{-1} x},-1 \leq x \leq 1$, show that $\left(1-x^{2}\right) \frac{d^{2} y}{d x^{2}}-x \frac{d y}{d x}-a^{2} y=0$.

## Summary

- A real valued function is continuous at a point in its domain if the limit of the function at that point equals the value of the function at that point. A function is continuous if it is continuous on the whole of its domain.
- Sum, difference, product and quotient of continuous functions are continuous. i.e., if $f$ and $g$ are continuous functions, then
$(f \pm g)(x)=f(x) \pm g(x)$ is continuous.
$(f \cdot g)(x)=f(x) \cdot g(x)$ is continuous.
$\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}$ (wherever $g(x) \neq 0$ ) is continuous.
- Every differentiable function is continuous, but the converse is not true.
- Chain rule is rule to differentiate composites of functions. If $f=v$ o $u, t=u(x)$ and if both $\frac{d t}{d x}$ and $\frac{d v}{d t}$ exist then

$$
\frac{d f}{d x}=\frac{d v}{d t} \cdot \frac{d t}{d x}
$$

- Following are some of the standard derivatives (in appropriate domains):

$$
\begin{array}{ll}
\frac{d}{d x}\left(\sin ^{-1} x\right)=\frac{1}{\sqrt{1-x^{2}}} & \frac{d}{d x}\left(\cos ^{-1} x\right)=-\frac{1}{\sqrt{1-x^{2}}} \\
\frac{d}{d x}\left(\tan ^{-1} x\right)=\frac{1}{1+x^{2}} & \\
\frac{d}{d x}\left(e^{x}\right)=e^{x} & \frac{d}{d x}(\log x)=\frac{1}{x}
\end{array}
$$

- Logarithmic differentiation is a powerful technique to differentiate functions of the form $f(x)=[u(x)]^{v(x)}$. Here both $f(x)$ and $u(x)$ need to be positive for this technique to make sense.


[^0]:    * Please see supplementary material on Page 222.

