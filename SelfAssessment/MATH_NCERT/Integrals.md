## INTEGRALS

> Just as a mountaineer climbs a mountain－because it is there，so a good mathematics student studies new material because it is there．－JAMES B．BRISTOL

## 7．1 Introduction

Differential Calculus is centred on the concept of the derivative．The original motivation for the derivative was the problem of defining tangent lines to the graphs of functions and calculating the slope of such lines．Integral Calculus is motivated by the problem of defining and calculating the area of the region bounded by the graph of the functions．

If a function $f$ is differentiable in an interval I，i．e．，its derivative $f^{\prime}$ exists at each point of I，then a natural question arises that given $f^{\prime}$ at each point of I ，can we determine the function？The functions that could possibly have given function as a derivative are called anti derivatives（or primitive）of the function．Further，the formula that gives
![](https://cdn.mathpix.com/cropped/2025_07_21_6f1e5706ec7b4b2554adg-01.jpg?height=535&width=405&top_left_y=871&top_left_x=1004)

G．W．Leibnitz （1646－1716） all these anti derivatives is called the indefinite integral of the function and such process of finding anti derivatives is called integration．Such type of problems arise in many practical situations．For instance，if we know the instantaneous velocity of an object at any instant，then there arises a natural question，i．e．，can we determine the position of the object at any instant？There are several such practical and theoretical situations where the process of integration is involved．The development of integral calculus arises out of the efforts of solving the problems of the following types：
（a）the problem of finding a function whenever its derivative is given，
（b）the problem of finding the area bounded by the graph of a function under certain conditions．
These two problems lead to the two forms of the integrals，e．g．，indefinite and definite integrals，which together constitute the Integral Calculus．

There is a connection, known as the Fundamental Theorem of Calculus, between indefinite integral and definite integral which makes the definite integral as a practical tool for science and engineering. The definite integral is also used to solve many interesting problems from various disciplines like economics, finance and probability.

In this Chapter, we shall confine ourselves to the study of indefinite and definite integrals and their elementary properties including some techniques of integration.

### 7.2 Integration as an Inverse Process of Differentiation

Integration is the inverse process of differentiation. Instead of differentiating a function, we are given the derivative of a function and asked to find its primitive, i.e., the original function. Such a process is called integration or anti differentiation.
Let us consider the following examples:

We know that

$$
\begin{align*}
\frac{d}{d x}(\sin x) & =\cos x  \tag{1}\\
\frac{d}{d x}\left(\frac{x^{3}}{3}\right) & =x^{2} \tag{2}
\end{align*}
$$

and

$$
\begin{equation*}
\frac{d}{d x}\left(e^{x}\right)=e^{x} \tag{3}
\end{equation*}
$$

We observe that in (1), the function $\cos x$ is the derived function of $\sin x$. We say that $\sin x$ is an anti derivative (or an integral) of $\cos x$. Similarly, in (2) and (3), $\frac{x^{3}}{3}$ and $e^{x}$ are the anti derivatives (or integrals) of $x^{2}$ and $e^{x}$, respectively. Again, we note that for any real number C , treated as constant function, its derivative is zero and hence, we can write (1), (2) and (3) as follows :

$$
\frac{d}{d x}(\sin x+\mathrm{C})=\cos x, \frac{d}{d x}\left(\frac{x^{3}}{3}+\mathrm{C}\right)=x^{2} \text { and } \frac{d}{d x}\left(e^{x}+\mathrm{C}\right)=e^{x}
$$

Thus, anti derivatives (or integrals) of the above cited functions are not unique. Actually, there exist infinitely many anti derivatives of each of these functions which can be obtained by choosing C arbitrarily from the set of real numbers. For this reason C is customarily referred to as arbitrary constant. In fact, C is the parameter by varying which one gets different anti derivatives (or integrals) of the given function. More generally, if there is a function F such that $\frac{d}{d x} \mathrm{~F}(x)=f(x), \forall x \in \mathrm{I}$ (interval), then for any arbitrary real number C , (also called constant of integration)

$$
\frac{d}{d x}[\mathrm{~F}(x)+\mathrm{C}]=f(x), x \in \mathrm{I}
$$

Thus, $\quad\{\mathrm{F}+\mathrm{C}, \mathrm{C} \in \mathbf{R}\}$ denotes a family of anti derivatives of $f$.
Remark Functions with same derivatives differ by a constant. To show this, let $g$ and $h$ be two functions having the same derivatives on an interval I.
Consider the function $f=g-h$ defined by $f(x)=g(x)-h(x), \forall x \in \mathrm{I}$

Then

$$
\frac{d f}{d x}=f^{\prime}=g^{\prime}-h^{\prime} \text { giving } f^{\prime}(x)=g^{\prime}(x)-h^{\prime}(x) \forall x \in \mathrm{I}
$$

or

$$
f^{\prime}(x)=0, \forall x \in \text { I by hypothesis, }
$$

i.e., the rate of change of $f$ with respect to $x$ is zero on I and hence $f$ is constant.

In view of the above remark, it is justified to infer that the family $\{\mathrm{F}+\mathrm{C}, \mathrm{C} \in \mathbf{R}\}$ provides all possible anti derivatives of $f$.

We introduce a new symbol, namely, $\int f(x) d x$ which will represent the entire class of anti derivatives read as the indefinite integral of $f$ with respect to $x$.
Symbolically, we write $\int f(x) d x=\mathrm{F}(x)+\mathrm{C}$.
Notation Given that $\frac{d y}{d x}=f(x)$, we write $y=\int f(x) d x$.
For the sake of convenience, we mention below the following symbols/terms/phrases with their meanings as given in the Table (7.1).

Table 7.1

| Symbols/Terms/Phrases | Meaning |
| :--- | :--- |
| $\int f(x) d x$ | Integral of $f$ with respect to $x$ |
| $f(x)$ in $\int f(x) d x$ | Integrand |
| $x$ in $\int f(x) d x$ | Variable of integration |
| Integrate | Find the integral |
| An integral of $f$ | A function F such that $\mathrm{F}^{\prime}(x)=f(x)$ |
| Integration | The process of finding the integral |
| Constant of Integration | Any real number C, considered as constant function |

We already know the formulae for the derivatives of many important functions. From these formulae, we can write down immediately the corresponding formulae (referred to as standard formulae) for the integrals of these functions, as listed below which will be used to find integrals of other functions.

## Derivatives

(i) $\frac{d}{d x}\left(\frac{x^{n+1}}{n+1}\right)=x^{n}$;

Particularly, we note that

$$
\frac{d}{d x}(x)=1
$$

(ii) $\frac{d}{d x}(\sin x)=\cos x$;
(iii) $\frac{d}{d x}(-\cos x)=\sin x$;
(iv) $\frac{d}{d x}(\tan x)=\sec ^{2} x$;
(v) $\frac{d}{d x}(-\cot x)=\operatorname{cosec}^{2} x$;
(vi) $\frac{d}{d x}(\sec x)=\sec x \tan x$;
(vii) $\frac{d}{d x}(-\operatorname{cosec} x)=\operatorname{cosec} x \cot x$;
(viii) $\frac{d}{d x}\left(\sin ^{-1} x\right)=\frac{1}{\sqrt{1-x^{2}}}$;
(ix) $\frac{d}{d x}\left(-\cos ^{-1} x\right)=\frac{1}{\sqrt{1-x^{2}}}$;
(x) $\frac{d}{d x}\left(\tan ^{-1} x\right)=\frac{1}{1+x^{2}}$;
(xi) $\frac{d}{d x}\left(e^{x}\right)=e^{x}$;

## Integrals (Anti derivatives)

$$
\int x^{n} d x=\frac{x^{n+1}}{n+1}+\mathrm{C}, n \neq-1
$$

$$
\int d x=x+\mathrm{C}
$$

$\int \cos x d x=\sin x+\mathrm{C}$

$$
\int \sin x d x=-\cos x+C
$$

$\int \sec ^{2} x d x=\tan x+\mathrm{C}$

$$
\int \operatorname{cosec}^{2} x d x=-\cot x+\mathrm{C}
$$

$\int \sec x \tan x d x=\sec x+\mathrm{C}$
$\int \operatorname{cosec} x \cot x d x=-\operatorname{cosec} x+\mathrm{C}$

$$
\int \frac{d x}{\sqrt{1-x^{2}}}=\sin ^{-1} x+\mathrm{C}
$$

$$
\int \frac{d x}{\sqrt{1-x^{2}}}=-\cos ^{-1} x+\mathrm{C}
$$

$$
\int \frac{d x}{1+x^{2}}=\tan ^{-1} x+\mathrm{C}
$$

$$
\int e^{x} d x=e^{x}+\mathrm{C}
$$

(xii) $\frac{d}{d x}(\log |x|)=\frac{1}{x}$;
$\int \frac{1}{x} d x=\log |x|+\mathrm{C}$
(xiii) $\frac{d}{d x}\left(\frac{a^{x}}{\log a}\right)=a^{x}$;
$\int a^{x} d x=\frac{a^{x}}{\log a}+\mathrm{C}$
Note In practice, we normally do not mention the interval over which the various functions are defined. However, in any specific problem one has to keep it in mind.

### 7.2.1 Some properties of indefinite integral

In this sub section, we shall derive some properties of indefinite integrals.
(I) The process of differentiation and integration are inverses of each other in the sense of the following results :

$$
\frac{d}{d x} \int f(x) d x=f(x)
$$

and

$$
\int f^{\prime}(x) d x=f(x)+\mathrm{C}, \text { where } \mathrm{C} \text { is any arbitrary constant. }
$$

Proof Let F be any anti derivative of $f$, i.e.,

$$
\frac{d}{d x} \mathrm{~F}(x)=f(x)
$$

Then

$$
\int f(x) d x=\mathrm{F}(x)+\mathrm{C}
$$

Therefore

$$
\begin{aligned}
\frac{d}{d x} \int f(x) d x & =\frac{d}{d x}(\mathrm{~F}(x)+\mathrm{C}) \\
& =\frac{d}{d x} \mathrm{~F}(x)=f(x)
\end{aligned}
$$

Similarly, we note that

$$
f^{\prime}(x)=\frac{d}{d x} f(x)
$$

and hence

$$
\int f^{\prime}(x) d x=f(x)+\mathrm{C}
$$

where C is arbitrary constant called constant of integration.
(II) Two indefinite integrals with the same derivative lead to the same family of curves and so they are equivalent.

Proof Let $f$ and $g$ be two functions such that

$$
\frac{d}{d x} \int f(x) d x=\frac{d}{d x} \int g(x) d x
$$

or

$$
\frac{d}{d x}\left[\int f(x) d x-\int g(x) d x\right]=0
$$

Hence $\quad \int f(x) d x-\int g(x) d x=\mathrm{C}$, where C is any real number (Why?)
or $\quad \int f(x) d x=\int g(x) d x+\mathrm{C}$
So the families of curves $\left\{\int f(x) d x+\mathrm{C}_{1}, \mathrm{C}_{1} \in \mathrm{R}\right\}$
and $\quad\left\{\int g(x) d x+\mathrm{C}_{2}, \mathrm{C}_{2} \in \mathrm{R}\right\}$ are identical.
Hence, in this sense, $\int f(x) d x$ and $\int g(x) d x$ are equivalent.
Note The equivalence of the families $\left\{\int f(x) d x+\mathrm{C}_{1}, \mathrm{C}_{1} \in \mathbf{R}\right\}$ and $\left\{\int g(x) d x+\mathrm{C}_{2}, \mathrm{C}_{2} \in \mathbf{R}\right\}$ is customarily expressed by writing $\int f(x) d x=\int g(x) d x$, without mentioning the parameter.
(III) $\int[f(x)+g(x)] d x=\int f(x) d x+\int g(x) d x$

Proof By Property (I), we have

$$
\begin{equation*}
\frac{d}{d x}\left[\int[f(x)+g(x)] d x\right]=f(x)+g(x) \tag{1}
\end{equation*}
$$

On the otherhand, we find that

$$
\begin{align*}
\frac{d}{d x}\left[\int f(x) d x+\int g(x) d x\right] & =\frac{d}{d x} \int f(x) d x+\frac{d}{d x} \int g(x) d x \\
& =f(x)+g(x) \tag{2}
\end{align*}
$$

Thus, in view of Property (II), it follows by (1) and (2) that

$$
\int(f(x)+g(x)) d x=\int f(x) d x+\int g(x) d x .
$$

(IV) For any real number $k, \int k f(x) d x=k \int f(x) d x$

Proof By the Property (I), $\frac{d}{d x} \int k f(x) d x=k f(x)$.

Also

$$
\frac{d}{d x}\left[k \int f(x) d x\right]=k \frac{d}{d x} \int f(x) d x=k f(x)
$$

Therefore, using the Property (II), we have $\int k f(x) d x=k \int f(x) d x$.
(V) Properties (III) and (IV) can be generalised to a finite number of functions $f_{1}, f_{2}, \ldots, f_{n}$ and the real numbers, $k_{1}, k_{2}, \ldots, k_{n}$ giving

$$
\begin{aligned}
& \int\left[k_{1} f_{1}(x)+k_{2} f_{2}(x)+\ldots+k_{n} f_{n}(x)\right] d x \\
& =k_{1} \int f_{1}(x) d x+k_{2} \int f_{2}(x) d x+\ldots+k_{n} \int f_{n}(x) d x
\end{aligned}
$$

To find an anti derivative of a given function, we search intuitively for a function whose derivative is the given function. The search for the requisite function for finding an anti derivative is known as integration by the method of inspection. We illustrate it through some examples.

Example 1 Write an anti derivative for each of the following functions using the method of inspection:
(i) $\cos 2 x$
(ii) $3 x^{2}+4 x^{3}$
(iii) $\frac{1}{x}, x \neq 0$

## Solution

(i) We look for a function whose derivative is $\cos 2 x$. Recall that

$$
\frac{d}{d x} \sin 2 x=2 \cos 2 x
$$

or $\quad \cos 2 x=\frac{1}{2} \frac{d}{d x}(\sin 2 x)=\frac{d}{d x}\left(\frac{1}{2} \sin 2 x\right)$
Therefore, an anti derivative of $\cos 2 x$ is $\frac{1}{2} \sin 2 x$.
(ii) We look for a function whose derivative is $3 x^{2}+4 x^{3}$. Note that

$$
\frac{d}{d x}\left(x^{3}+x^{4}\right)=3 x^{2}+4 x^{3}
$$

Therefore, an anti derivative of $3 x^{2}+4 x^{3}$ is $x^{3}+x^{4}$.
(iii) We know that

$$
\frac{d}{d x}(\log x)=\frac{1}{x}, x>0 \text { and } \frac{d}{d x}[\log (-x)]=\frac{1}{-x}(-1)=\frac{1}{x}, x<0
$$

Combining above, we get $\frac{d}{d x}(\log |x|)=\frac{1}{x}, x \neq 0$
Therefore, $\int \frac{1}{x} d x=\log |x|$ is one of the anti derivatives of $\frac{1}{x}$.

## Example 2 Find the following integrals:

(i) $\int \frac{x^{3}-1}{x^{2}} d x$
(ii) $\int\left(x^{\frac{2}{3}}+1\right) d x$
(iii) $\int\left(x^{\frac{3}{2}}+2 e^{x}-\frac{1}{x}\right) d x$

## Solution

(i) We have

$$
\begin{aligned}
\int \frac{x^{3}-1}{x^{2}} d x & =\int x d x-\int x^{-2} d x \quad(\text { by Property } \mathrm{V}) \\
& =\left(\frac{x^{1+1}}{1+1}+\mathrm{C}_{1}\right)-\left(\frac{x^{-2+1}}{-2+1}+\mathrm{C}_{2}\right) ; \mathrm{C}_{1}, \mathrm{C}_{2} \text { are constants of integration } \\
& =\frac{x^{2}}{2}+\mathrm{C}_{1}-\frac{x^{-1}}{-1}-\mathrm{C}_{2}=\frac{x^{2}}{2}+\frac{1}{x}+\mathrm{C}_{1}-\mathrm{C}_{2} \\
& =\frac{x^{2}}{2}+\frac{1}{x}+\mathrm{C}, \text { where } \mathrm{C}=\mathrm{C}_{1}-\mathrm{C}_{2} \text { is another constant of integration. }
\end{aligned}
$$

Note From now onwards, we shall write only one constant of integration in the final answer.
(ii) We have

$$
\begin{aligned}
\int\left(x^{\frac{2}{3}}+1\right) d x & =\int x^{\frac{2}{3}} d x+\int d x \\
& =\frac{x^{\frac{2}{3}+1}}{\frac{2}{3}+1}+x+\mathrm{C}=\frac{3}{5} x^{\frac{5}{3}}+x+\mathrm{C}
\end{aligned}
$$

(iii) We have $\int\left(x^{\frac{3}{2}}+2 e^{x}-\frac{1}{x}\right) d x=\int x^{\frac{3}{2}} d x+\int 2 e^{x} d x-\int \frac{1}{x} d x$

$$
\begin{aligned}
& =\frac{x^{\frac{3}{2}+1}}{\frac{3}{2}+1}+2 e^{x}-\log |x|+\mathrm{C} \\
& =\frac{2}{5} x^{\frac{5}{2}}+2 e^{x}-\log |x|+\mathrm{C}
\end{aligned}
$$

Example 3 Find the following integrals:
(i) $\int(\sin x+\cos x) d x$
(ii) $\int \operatorname{cosec} x(\operatorname{cosec} x+\cot x) d x$
(iii) $\int \frac{1-\sin x}{\cos ^{2} x} d x$

## Solution

(i) We have

$$
\begin{aligned}
\int(\sin x+\cos x) d x & =\int \sin x d x+\int \cos x d x \\
& =-\cos x+\sin x+\mathrm{C}
\end{aligned}
$$

(ii) We have

$$
\begin{aligned}
\int(\operatorname{cosec} x(\operatorname{cosec} x+\cot x) d x & =\int \operatorname{cosec}^{2} x d x+\int \operatorname{cosec} x \cot x d x \\
& =-\cot x-\operatorname{cosec} x+\mathrm{C}
\end{aligned}
$$

(iii) We have

$$
\begin{aligned}
\int \frac{1-\sin x}{\cos ^{2} x} d x & =\int \frac{1}{\cos ^{2} x} d x-\int \frac{\sin x}{\cos ^{2} x} d x \\
& =\int \sec ^{2} x d x-\int \tan x \sec x d x \\
& =\tan x-\sec x+\mathrm{C}
\end{aligned}
$$

Example 4 Find the anti derivative F of $f$ defined by $f(x)=4 x^{3}-6$, where $\mathrm{F}(0)=3$
Solution One anti derivative of $f(x)$ is $x^{4}-6 x$ since

$$
\frac{d}{d x}\left(x^{4}-6 x\right)=4 x^{3}-6
$$

Therefore, the anti derivative F is given by

$$
\mathrm{F}(x)=x^{4}-6 x+\mathrm{C}, \text { where } \mathrm{C} \text { is constant. }
$$

Given that

$$
\begin{aligned}
\mathrm{F}(0) & =3 \text {, which gives, } \\
3 & =0-6 \times 0+\mathrm{C} \text { or } \mathrm{C}=3
\end{aligned}
$$

Hence, the required anti derivative is the unique function F defined by

$$
\mathrm{F}(x)=x^{4}-6 x+3
$$

## Remarks

(i) We see that if F is an anti derivative of $f$, then so is $\mathrm{F}+\mathrm{C}$, where C is any constant. Thus, if we know one anti derivative F of a function $f$, we can write down an infinite number of anti derivatives of $f$ by adding any constant to F expressed by $\mathrm{F}(x)+\mathrm{C}, \mathrm{C} \in \mathbf{R}$. In applications, it is often necessary to satisfy an additional condition which then determines a specific value of C giving unique anti derivative of the given function.
(ii) Sometimes, F is not expressible in terms of elementary functions viz., polynomial, logarithmic, exponential, trigonometric functions and their inverses etc. We are therefore blocked for finding $\int f(x) d x$. For example, it is not possible to find $\int e^{-x^{2}} d x$ by inspection since we can not find a function whose derivative is $e^{-x^{2}}$
(iii) When the variable of integration is denoted by a variable other than $x$, the integral formulae are modified accordingly. For instance

$$
\int y^{4} d y=\frac{y^{4+1}}{4+1}+\mathrm{C}=\frac{1}{5} y^{5}+\mathrm{C}
$$

## EXERCISE 7.1

Find an anti derivative (or integral) of the following functions by the method of inspection.

1. $\sin 2 x$
2. $\cos 3 x$
3. $e^{2 x}$
4. $(a x+b)^{2}$
5. $\sin 2 x-4 e^{3 x}$

Find the following integrals in Exercises 6 to 20:
6. $\int\left(4 e^{3 x}+1\right) d x$
7. $\int x^{2}\left(1-\frac{1}{x^{2}}\right) d x$
8. $\int\left(a x^{2}+b x+c\right) d x$
9. $\int\left(2 x^{2}+e^{x}\right) d x$
10. $\int\left(\sqrt{x}-\frac{1}{\sqrt{x}}\right)^{2} d x$
11. $\int \frac{x^{3}+5 x^{2}-4}{x^{2}} d x$
12. $\int \frac{x^{3}+3 x+4}{\sqrt{x}} d x$
13. $\int \frac{x^{3}-x^{2}+x-1}{x-1} d x$
14. $\int(1-x) \sqrt{x} d x$
15. $\int \sqrt{x}\left(3 x^{2}+2 x+3\right) d x$
17. $\int\left(2 x^{2}-3 \sin x+5 \sqrt{x}\right) d x$
19. $\int \frac{\sec ^{2} x}{\operatorname{cosec}^{2} x} d x$
16. $\int\left(2 x-3 \cos x+e^{x}\right) d x$
18. $\int \sec x(\sec x+\tan x) d x$

Choose the correct answer in Exercises 21 and 22.
21. The anti derivative of $\left(\sqrt{x}+\frac{1}{\sqrt{x}}\right)$ equals
(A) $\frac{1}{3} x^{\frac{1}{3}}+2 x^{\frac{1}{2}}+\mathrm{C}$
(B) $\frac{2}{3} x^{\frac{2}{3}}+\frac{1}{2} x^{2}+\mathrm{C}$
(C) $\frac{2}{3} x^{\frac{3}{2}}+2 x^{\frac{1}{2}}+\mathrm{C}$
(D) $\frac{3}{2} x^{\frac{3}{2}}+\frac{1}{2} x^{\frac{1}{2}}+\mathrm{C}$
22. If $\frac{d}{d x} f(x)=4 x^{3}-\frac{3}{x^{4}}$ such that $f(2)=0$. Then $f(x)$ is
(A) $x^{4}+\frac{1}{x^{3}}-\frac{129}{8}$
(B) $x^{3}+\frac{1}{x^{4}}+\frac{129}{8}$
(C) $x^{4}+\frac{1}{x^{3}}+\frac{129}{8}$
(D) $x^{3}+\frac{1}{x^{4}}-\frac{129}{8}$

### 7.3 Methods of Integration

In previous section, we discussed integrals of those functions which were readily obtainable from derivatives of some functions. It was based on inspection, i.e., on the search of a function F whose derivative is $f$ which led us to the integral of $f$. However, this method, which depends on inspection, is not very suitable for many functions. Hence, we need to develop additional techniques or methods for finding the integrals by reducing them into standard forms. Prominent among them are methods based on:

1. Integration by Substitution
2. Integration using Partial Fractions
3. Integration by Parts

### 7.3.1 Integration by substitution

In this section, we consider the method of integration by substitution.
The given integral $\int f(x) d x$ can be transformed into another form by changing the independent variable $x$ to $t$ by substituting $x=g(t)$.

Consider

$$
\mathrm{I}=\int f(x) d x
$$

Put $x=g(t)$ so that $\frac{d x}{d t}=g^{\prime}(t)$.
We write

$$
d x=g^{\prime}(t) d t
$$

Thus

$$
\mathrm{I}=\int f(x) d x=\int f(g(t)) g^{\prime}(t) d t
$$

This change of variable formula is one of the important tools available to us in the name of integration by substitution. It is often important to guess what will be the useful substitution. Usually, we make a substitution for a function whose derivative also occurs in the integrand as illustrated in the following examples.

Example 5 Integrate the following functions w.r.t. $x$ :
(i) $\sin m x$
(ii) $2 x \sin \left(x^{2}+1\right)$
(iii) $\frac{\tan ^{4} \sqrt{x} \sec ^{2} \sqrt{x}}{\sqrt{x}}$
(iv) $\frac{\sin \left(\tan ^{-1} x\right)}{1+x^{2}}$

## Solution

(i) We know that derivative of $m x$ is $m$. Thus, we make the substitution $m x=t$ so that $m d x=d t$.

Therefore, $\quad \int \sin m x d x=\frac{1}{m} \int \sin t d t=-\frac{1}{m} \cos t+\mathrm{C}=-\frac{1}{m} \cos m x+\mathrm{C}$
(ii) Derivative of $x^{2}+1$ is $2 x$. Thus, we use the substitution $x^{2}+1=t$ so that $2 x d x=d t$.
Therefore, $\int 2 x \sin \left(x^{2}+1\right) d x=\int \sin t d t=-\cos t+\mathrm{C}=-\cos \left(x^{2}+1\right)+\mathrm{C}$
(iii) Derivative of $\sqrt{x}$ is $\frac{1}{2} x^{-\frac{1}{2}}=\frac{1}{2 \sqrt{x}}$. Thus, we use the substitution
$\sqrt{x}=t$ so that $\frac{1}{2 \sqrt{x}} d x=d t$ giving $d x=2 t d t$.
Thus, $\quad \int \frac{\tan ^{4} \sqrt{x} \sec ^{2} \sqrt{x}}{\sqrt{x}} d x=\int \frac{2 t \tan ^{4} t \sec ^{2} t d t}{t}=2 \int \tan ^{4} t \sec ^{2} t d t$
Again, we make another substitution $\tan t=u$ so that

$$
\sec ^{2} t d t=d u
$$

Therefore, $\quad 2 \int \tan ^{4} t \sec ^{2} t d t=2 \int u^{4} d u=2 \frac{u^{5}}{5}+\mathrm{C}$

$$
\begin{aligned}
& =\frac{2}{5} \tan ^{5} t+\mathrm{C}(\text { since } u=\tan t) \\
& =\frac{2}{5} \tan ^{5} \sqrt{x}+\mathrm{C}(\text { since } t=\sqrt{x})
\end{aligned}
$$

Hence, $\quad \int \frac{\tan ^{4} \sqrt{x} \sec ^{2} \sqrt{x}}{\sqrt{x}} d x=\frac{2}{5} \tan ^{5} \sqrt{x}+\mathrm{C}$
Alternatively, make the substitution $\tan \sqrt{x}=t$
(iv) Derivative of $\tan ^{-1} x=\frac{1}{1+x^{2}}$. Thus, we use the substitution

$$
\tan ^{-1} x=t \text { so that } \frac{d x}{1+x^{2}}=d t
$$

Therefore, $\int \frac{\sin \left(\tan ^{-1} x\right)}{1+x^{2}} d x=\int \sin t d t=-\cos t+\mathrm{C}=-\cos \left(\tan ^{-1} x\right)+\mathrm{C}$
Now, we discuss some important integrals involving trigonometric functions and their standard integrals using substitution technique. These will be used later without reference.
(i) $\int \tan x d x=\log |\sec x|+\mathrm{C}$

We have

$$
\int \tan x d x=\int \frac{\sin x}{\cos x} d x
$$

Put $\cos x=t$ so that $\sin x d x=-d t$
Then

$$
\int \tan x d x=-\int \frac{d t}{t}=-\log |t|+\mathrm{C}=-\log |\cos x|+\mathrm{C}
$$

or

$$
\int \tan x d x=\log |\sec x|+\mathrm{C}
$$

(ii) $\int \cot x d x=\log |\sin x|+\mathrm{C}$

We have $\int \cot x d x=\int \frac{\cos x}{\sin x} d x$

Put $\sin x=t$ so that $\cos x d x=d t$

Then

$$
\int \cot x d x=\int \frac{d t}{t}=\log |t|+\mathrm{C}=\log |\sin x|+\mathrm{C}
$$

(iii) $\int \sec x d x=\log |\sec x+\tan x|+\mathrm{C}$

We have

$$
\int \sec x d x=\int \frac{\sec x(\sec x+\tan x)}{\sec x+\tan x} d x
$$

Put $\sec x+\tan x=t$ so that $\sec x(\tan x+\sec x) d x=d t$
Therefore, $\int \sec x d x=\int \frac{d t}{t}=\log |t|+\mathrm{C}=\log |\sec x+\tan x|+\mathrm{C}$
(iv) $\int \operatorname{cosec} x d x=\log |\operatorname{cosec} x-\cot x|+C$

We have

$$
\int \operatorname{cosec} x d x=\int \frac{\operatorname{cosec} x(\operatorname{cosec} x+\cot x)}{(\operatorname{cosec} x+\cot x)} d x
$$

Put $\operatorname{cosec} x+\cot x=t$ so that $-\operatorname{cosec} x(\operatorname{cosec} x+\cot x) d x=d t$
So

$$
\begin{aligned}
\int \operatorname{cosec} x d x & =-\int \frac{d t}{t}=-\log |t|=-\log |\operatorname{cosec} x+\cot x|+\mathrm{C} \\
& =-\log \left|\frac{\operatorname{cosec}^{2} x-\cot ^{2} x}{\operatorname{cosec} x-\cot x}\right|+\mathrm{C} \\
& =\log |\operatorname{cosec} x-\cot x|+\mathrm{C}
\end{aligned}
$$

Example 6 Find the following integrals:
(i) $\int \sin ^{3} x \cos ^{2} x d x$
(ii) $\int \frac{\sin x}{\sin (x+a)} d x$
(iii) $\int \frac{1}{1+\tan x} d x$

## Solution

(i) We have

$$
\begin{aligned}
\int \sin ^{3} x \cos ^{2} x d x & =\int \sin ^{2} x \cos ^{2} x(\sin x) d x \\
& =\int\left(1-\cos ^{2} x\right) \cos ^{2} x(\sin x) d x
\end{aligned}
$$

Put $t=\cos x$ so that $d t=-\sin x d x$

Therefore, $\quad \int \sin ^{2} x \cos ^{2} x(\sin x) d x=-\int\left(1-t^{2}\right) t^{2} d t$

$$
\begin{aligned}
& =-\int\left(t^{2}-t^{4}\right) d t=-\left(\frac{t^{3}}{3}-\frac{t^{5}}{5}\right)+\mathrm{C} \\
& =-\frac{1}{3} \cos ^{3} x+\frac{1}{5} \cos ^{5} x+\mathrm{C}
\end{aligned}
$$

(ii) Put $x+a=t$. Then $d x=d t$. Therefore

$$
\begin{aligned}
\int \frac{\sin x}{\sin (x+a)} d x & =\int \frac{\sin (t-a)}{\sin t} d t \\
& =\int \frac{\sin t \cos a-\cos t \sin a}{\sin t} d t \\
& =\cos a \int d t-\sin a \int \cot t d t \\
& =(\cos a) t-(\sin a)\left[\log |\sin t|+\mathrm{C}_{1}\right] \\
& =(\cos a)(x+a)-(\sin a)\left[\log |\sin (x+a)|+\mathrm{C}_{1}\right] \\
& =x \cos a+a \cos a-(\sin a) \log |\sin (x+a)|-\mathrm{C}_{1} \sin a
\end{aligned}
$$

Hence, $\int \frac{\sin x}{\sin (x+a)} d x=x \cos a-\sin a \log |\sin (x+a)|+\mathrm{C}$,
where, $\mathrm{C}=-\mathrm{C}_{1} \sin a+a \cos a$, is another arbitrary constant.
(iii) $\int \frac{d x}{1+\tan x}=\int \frac{\cos x d x}{\cos x+\sin x}$

$$
\begin{align*}
& =\frac{1}{2} \int \frac{(\cos x+\sin x+\cos x-\sin x) d x}{\cos x+\sin x} \\
& =\frac{1}{2} \int d x+\frac{1}{2} \int \frac{\cos x-\sin x}{\cos x+\sin x} d x \\
& =\frac{x}{2}+\frac{\mathrm{C}_{1}}{2}+\frac{1}{2} \int \frac{\cos x-\sin x}{\cos x+\sin x} d x \tag{1}
\end{align*}
$$

Now, consider $\mathrm{I}=\int \frac{\cos x-\sin x}{\cos x+\sin x} d x$
Put $\cos x+\sin x=t$ so that $(\cos x-\sin x) d x=d t$
Therefore

$$
\mathrm{I}=\int \frac{d t}{t}=\log |t|+\mathrm{C}_{2}=\log |\cos x+\sin x|+\mathrm{C}_{2}
$$

Putting it in (1), we get

$$
\begin{aligned}
\int \frac{d x}{1+\tan x} & =\frac{x}{2}+\frac{\mathrm{C}_{1}}{2}+\frac{1}{2} \log |\cos x+\sin x|+\frac{\mathrm{C}_{2}}{2} \\
& =\frac{x}{2}+\frac{1}{2} \log |\cos x+\sin x|+\frac{\mathrm{C}_{1}}{2}+\frac{\mathrm{C}_{2}}{2} \\
& =\frac{x}{2}+\frac{1}{2} \log |\cos x+\sin x|+\mathrm{C},\left(\mathrm{C}=\frac{\mathrm{C}_{1}}{2}+\frac{\mathrm{C}_{2}}{2}\right)
\end{aligned}
$$

## EXERCISE 7.2

Integrate the functions in Exercises 1 to 37:

1. $\frac{2 x}{1+x^{2}}$
2. $\frac{(\log x)^{2}}{x}$
3. $\frac{1}{x+x \log x}$
4. $\sin x \sin (\cos x)$
5. $\sin (a x+b) \cos (a x+b)$
6. $\sqrt{a x+b}$
7. $x \sqrt{x+2}$
8. $x \sqrt{1+2 x^{2}}$
9. $(4 x+2) \sqrt{x^{2}+x+1}$
10. $\frac{1}{x-\sqrt{x}}$
11. $\frac{x}{\sqrt{x+4}}, x>0$
12. $\left(x^{3}-1\right)^{\frac{1}{3}} x^{5}$
13. $\frac{x^{2}}{\left(2+3 x^{3}\right)^{3}}$
14. $\frac{1}{x(\log x)^{m}}, x>0, m \neq 1$
15. $\frac{x}{9-4 x^{2}}$
16. $e^{2 x+3}$
17. $\frac{x}{e^{x^{2}}}$
18. $\frac{e^{\tan ^{-1} x}}{1+x^{2}}$
19. $\frac{e^{2 x}-1}{e^{2 x}+1}$
20. $\frac{e^{2 x}-e^{-2 x}}{e^{2 x}+e^{-2 x}}$
21. $\tan ^{2}(2 x-3)$
22. $\sec ^{2}(7-4 x)$
23. $\frac{\sin ^{-1} x}{\sqrt{1-x^{2}}}$
24. $\frac{2 \cos x-3 \sin x}{6 \cos x+4 \sin x}$
25. $\frac{1}{\cos ^{2} x(1-\tan x)^{2}}$
26. $\frac{\cos \sqrt{x}}{\sqrt{x}}$
27. $\sqrt{\sin 2 x} \cos 2 x$
28. $\frac{\cos x}{\sqrt{1+\sin x}}$
29. $\cot x \log \sin x$
30. $\frac{\sin x}{1+\cos x}$
31. $\frac{\sin x}{(1+\cos x)^{2}}$
32. $\frac{1}{1+\cot x}$
33. $\frac{1}{1-\tan x}$
34. $\frac{\sqrt{\tan x}}{\sin x \cos x}$
35. $\frac{(1+\log x)^{2}}{x}$
36. $\frac{(x+1)(x+\log x)^{2}}{x}$
37. $\frac{x^{3} \sin \left(\tan ^{-1} x^{4}\right)}{1+x^{8}}$

Choose the correct answer in Exercises 38 and 39.
38. $\int \frac{10 x^{9}+10^{x} \log _{e} 10 d x}{x^{10}+10^{x}}$ equals
(A) $10^{x}-x^{10}+\mathrm{C}$
(B) $10^{x}+x^{10}+\mathrm{C}$
(C) $\left(10^{x}-x^{10}\right)^{-1}+\mathrm{C}$
(D) $\log \left(10^{x}+x^{10}\right)+\mathrm{C}$
39. $\int \frac{d x}{\sin ^{2} x \cos ^{2} x}$ equals
(A) $\tan x+\cot x+\mathrm{C}$
(B) $\tan x-\cot x+\mathrm{C}$
(C) $\tan x \cot x+\mathrm{C}$
(D) $\tan x-\cot 2 x+\mathrm{C}$

### 7.3.2 Integration using trigonometric identities

When the integrand involves some trigonometric functions, we use some known identities to find the integral as illustrated through the following example.
Example 7 Find (i) $\int \cos ^{2} x d x$
(ii) $\int \sin 2 x \cos 3 x d x$
(iii) $\int \sin ^{3} x d x$

## Solution

(i) Recall the identity $\cos 2 x=2 \cos ^{2} x-1$, which gives

$$
\cos ^{2} x=\frac{1+\cos 2 x}{2}
$$

Therefore, $\quad \int \cos ^{2} x d x=\frac{1}{2} \int(1+\cos 2 x) d x=\frac{1}{2} \int d x+\frac{1}{2} \int \cos 2 x d x$

$$
=\frac{x}{2}+\frac{1}{4} \sin 2 x+\mathrm{C}
$$

(ii) Recall the identity $\sin x \cos y=\frac{1}{2}[\sin (x+y)+\sin (x-y)]$

Then $\int \sin 2 x \cos 3 x d x=\frac{1}{2}\left[\int \sin 5 x d x-\int \sin x d x\right]$

$$
\begin{aligned}
& =\frac{1}{2}\left[-\frac{1}{5} \cos 5 x+\cos x\right]+C \\
& =-\frac{1}{10} \cos 5 x+\frac{1}{2} \cos x+C
\end{aligned}
$$

(iii) From the identity $\sin 3 x=3 \sin x-4 \sin ^{3} x$, we find that

$$
\sin ^{3} x=\frac{3 \sin x-\sin 3 x}{4}
$$

Therefore, $\quad \int \sin ^{3} x d x=\frac{3}{4} \int \sin x d x-\frac{1}{4} \int \sin 3 x d x$

$$
=-\frac{3}{4} \cos x+\frac{1}{12} \cos 3 x+C
$$

Alternatively, $\int \sin ^{3} x d x=\int \sin ^{2} x \sin x d x=\int\left(1-\cos ^{2} x\right) \sin x d x$
Put $\cos x=t$ so that $-\sin x d x=d t$
Therefore, $\quad \int \sin ^{3} x d x=-\int\left(1-t^{2}\right) d t=-\int d t+\int t^{2} d t=-t+\frac{t^{3}}{3}+\mathrm{C}$

$$
=-\cos x+\frac{1}{3} \cos ^{3} x+C
$$

Remark It can be shown using trigonometric identities that both answers are equivalent.

## EXERCISE 7.3

Find the integrals of the functions in Exercises 1 to 22:

1. $\sin ^{2}(2 x+5)$
2. $\sin 3 x \cos 4 x$
3. $\cos 2 x \cos 4 x \cos 6 x$
4. $\sin ^{3}(2 x+1)$
5. $\sin ^{3} x \cos ^{3} x$
6. $\sin x \sin 2 x \sin 3 x$
7. $\sin 4 x \sin 8 x$
8. $\frac{1-\cos x}{1+\cos x}$
9. $\frac{\cos x}{1+\cos x}$
10. $\sin ^{4} x$
11. $\cos ^{4} 2 x$
12. $\frac{\sin ^{2} x}{1+\cos x}$
13. $\frac{\cos 2 x-\cos 2 \alpha}{\cos x-\cos \alpha}$
14. $\frac{\cos x-\sin x}{1+\sin 2 x}$
15. $\tan ^{3} 2 x \sec 2 x$
16. $\tan ^{4} x$
17. $\frac{\sin ^{3} x+\cos ^{3} x}{\sin ^{2} x \cos ^{2} x}$
18. $\frac{\cos 2 x+2 \sin ^{2} x}{\cos ^{2} x}$
19. $\frac{1}{\sin x \cos ^{3} x}$
20. $\frac{\cos 2 x}{(\cos x+\sin x)^{2}}$
21. $\sin ^{-1}(\cos x)$
22. $\frac{1}{\cos (x-a) \cos (x-b)}$

Choose the correct answer in Exercises 23 and 24.
23. $\int \frac{\sin ^{2} x-\cos ^{2} x}{\sin ^{2} x \cos ^{2} x} d x$ is equal to
(A) $\tan x+\cot x+\mathrm{C}$
(B) $\tan x+\operatorname{cosec} x+\mathrm{C}$
(C) $-\tan x+\cot x+\mathrm{C}$
(D) $\tan x+\sec x+\mathrm{C}$
24. $\int \frac{e^{x}(1+x)}{\cos ^{2}\left(e^{x} x\right)} d x$ equals
(A) $-\cot \left(e x^{x}\right)+\mathrm{C}$
(B) $\tan \left(x e^{x}\right)+\mathrm{C}$
(C) $\tan \left(e^{x}\right)+\mathrm{C}$
(D) $\cot \left(e^{x}\right)+\mathrm{C}$

### 7.4 Integrals of Some Particular Functions

In this section, we mention below some important formulae of integrals and apply them for integrating many other related standard integrals:
(1) $\int \frac{d x}{x^{2}-a^{2}}=\frac{1}{2 a} \log \left|\frac{x-a}{x+a}\right|+\mathrm{C}$
(2) $\int \frac{d x}{a^{2}-x^{2}}=\frac{1}{2 a} \log \left|\frac{a+x}{a-x}\right|+\mathrm{C}$
(3) $\int \frac{d x}{x^{2}+a^{2}}=\frac{1}{a} \tan ^{-1} \frac{x}{a}+\mathrm{C}$
(4) $\int \frac{d x}{\sqrt{x^{2}-a^{2}}}=\log \left|x+\sqrt{x^{2}-a^{2}}\right|+\mathrm{C}$
(5) $\int \frac{d x}{\sqrt{a^{2}-x^{2}}}=\sin ^{-1} \frac{x}{a}+\mathrm{C}$
(6) $\int \frac{d x}{\sqrt{x^{2}+a^{2}}}=\log \left|x+\sqrt{x^{2}+a^{2}}\right|+\mathrm{C}$

We now prove the above results:
(1) We have $\frac{1}{x^{2}-a^{2}}=\frac{1}{(x-a)(x+a)}$

$$
=\frac{1}{2 a}\left[\frac{(x+a)-(x-a)}{(x-a)(x+a)}\right]=\frac{1}{2 a}\left[\frac{1}{x-a}-\frac{1}{x+a}\right]
$$

Therefore, $\int \frac{d x}{x^{2}-a^{2}}=\frac{1}{2 a}\left[\int \frac{d x}{x-a}-\int \frac{d x}{x+a}\right]$

$$
\begin{aligned}
& =\frac{1}{2 a}[\log |(x-a)|-\log |(x+a)|]+\mathrm{C} \\
& =\frac{1}{2 a} \log \left|\frac{x-a}{x+a}\right|+\mathrm{C}
\end{aligned}
$$

(2) In view of (1) above, we have

$$
\frac{1}{a^{2}-x^{2}}=\frac{1}{2 a}\left[\frac{(a+x)+(a-x)}{(a+x)(a-x)}\right]=\frac{1}{2 a}\left[\frac{1}{a-x}+\frac{1}{a+x}\right]
$$

Therefore, $\int \frac{d x}{a^{2}-x^{2}}=\frac{1}{2 a}\left[\int \frac{d x}{a-x}+\int \frac{d x}{a+x}\right]$

$$
\begin{aligned}
& =\frac{1}{2 a}[-\log |a-x|+\log |a+x|]+\mathrm{C} \\
& =\frac{1}{2 a} \log \left|\frac{a+x}{a-x}\right|+\mathrm{C}
\end{aligned}
$$

Note The technique used in (1) will be explained in Section 7.5.
(3) Put $x=a \tan \theta$. Then $d x=a \sec ^{2} \theta d \theta$.

Therefore, $\quad \int \frac{d x}{x^{2}+a^{2}}=\int \frac{a \sec ^{2} \theta d \theta}{a^{2} \tan ^{2} \theta+a^{2}}$

$$
=\frac{1}{a} \int d \theta=\frac{1}{a} \theta+\mathrm{C}=\frac{1}{a} \tan ^{-1} \frac{x}{a}+\mathrm{C}
$$

(4) Let $x=a \sec \theta$. Then $d x=a \sec \theta \tan \theta d \theta$.

Therefore,

$$
\begin{aligned}
\int \frac{d x}{\sqrt{x^{2}-a^{2}}} & =\int \frac{a \sec \theta \tan \theta d \theta}{\sqrt{a^{2} \sec ^{2} \theta-a^{2}}} \\
& =\int \sec \theta d \theta=\log |\sec \theta+\tan \theta|+\mathrm{C}_{1} \\
& =\log \left|\frac{x}{a}+\sqrt{\frac{x^{2}}{a^{2}}-1}\right|+\mathrm{C}_{1} \\
& =\log \left|x+\sqrt{x^{2}-a^{2}}\right|-\log |a|+\mathrm{C}_{1} \\
& =\log \left|x+\sqrt{x^{2}-a^{2}}\right|+\mathrm{C}, \text { where } \mathrm{C}=\mathrm{C}_{1}-\log |a|
\end{aligned}
$$

(5) Let $x=a \sin \theta$. Then $d x=a \cos \theta \mathrm{~d} \theta$.

Therefore,

$$
\begin{aligned}
\int \frac{d x}{\sqrt{a^{2}-x^{2}}} & =\int \frac{a \cos \theta d \theta}{\sqrt{a^{2}-a^{2} \sin ^{2} \theta}} \\
& =\int d \theta=\theta+\mathrm{C}=\sin ^{-1} \frac{x}{a}+\mathrm{C}
\end{aligned}
$$

(6) Let $x=a \tan \theta$. Then $d x=a \sec ^{2} \theta \mathrm{~d} \theta$.

Therefore,

$$
\begin{aligned}
\int \frac{d x}{\sqrt{x^{2}+a^{2}}} & =\int \frac{a \sec ^{2} \theta d \theta}{\sqrt{a^{2} \tan ^{2} \theta+a^{2}}} \\
& =\int \sec \theta d \theta=\log |(\sec \theta+\tan \theta)|+\mathrm{C}_{1}
\end{aligned}
$$

$$
\begin{aligned}
& =\log \left|\frac{x}{a}+\sqrt{\frac{x^{2}}{a^{2}}+1}\right|+\mathrm{C}_{1} \\
& =\log \left|x+\sqrt{x^{2}+a^{2}}\right|-\log |a|+\mathrm{C}_{1} \\
& =\log \left|x+\sqrt{x^{2}+a^{2}}\right|+\mathrm{C}, \text { where } \mathrm{C}=\mathrm{C}_{1}-\log |a|
\end{aligned}
$$

Applying these standard formulae, we now obtain some more formulae which are useful from applications point of view and can be applied directly to evaluate other integrals.
(7) To find the integral $\int \frac{d x}{a x^{2}+b x+c}$, we write

$$
a x^{2}+b x+c=a\left[x^{2}+\frac{b}{a} x+\frac{c}{a}\right]=a\left[\left(x+\frac{b}{2 a}\right)^{2}+\left(\frac{c}{a}-\frac{b^{2}}{4 a^{2}}\right)\right]
$$

Now, put $x+\frac{b}{2 a}=t$ so that $d x=d t$ and writing $\frac{c}{a}-\frac{b^{2}}{4 a^{2}}= \pm k^{2}$. We find the integral reduced to the form $\frac{1}{a} \int \frac{d t}{t^{2} \pm k^{2}}$ depending upon the sign of $\left(\frac{c}{a}-\frac{b^{2}}{4 a^{2}}\right)$ and hence can be evaluated.
(8) To find the integral of the type $\int \frac{d x}{\sqrt{a x^{2}+b x+c}}$, proceeding as in (7), we obtain the integral using the standard formulae.
(9) To find the integral of the type $\int \frac{p x+q}{a x^{2}+b x+c} d x$, where $p, q, a, b, c$ are constants, we are to find real numbers $\mathrm{A}, \mathrm{B}$ such that

$$
p x+q=\mathrm{A} \frac{d}{d x}\left(a x^{2}+b x+c\right)+\mathrm{B}=\mathrm{A}(2 a x+b)+\mathrm{B}
$$

To determine A and B , we equate from both sides the coefficients of $x$ and the constant terms. A and B are thus obtained and hence the integral is reduced to one of the known forms.
(10) For the evaluation of the integral of the type $\int \frac{(p x+q) d x}{\sqrt{a x^{2}+b x+c}}$, we proceed as in (9) and transform the integral into known standard forms.
Let us illustrate the above methods by some examples.
Example 8 Find the following integrals:
(i) $\int \frac{d x}{x^{2}-16}$
(ii) $\int \frac{d x}{\sqrt{2 x-x^{2}}}$

## Solution

(i) We have $\int \frac{d x}{x^{2}-16}=\int \frac{d x}{x^{2}-4^{2}}=\frac{1}{8} \log \left|\frac{x-4}{x+4}\right|+\mathrm{C}[$ by 7.4 (1) $]$
(ii) $\int \frac{d x}{\sqrt{2 x-x^{2}}}=\int \frac{d x}{\sqrt{1-(x-1)^{2}}}$

Put $x-1=t$. Then $d x=d t$.
Therefore, $\quad \int \frac{d x}{\sqrt{2 x-x^{2}}}=\int \frac{d t}{\sqrt{1-t^{2}}}=\sin ^{-1}(t)+\mathrm{C}$
[by 7.4 (5)]

$$
=\sin ^{-1}(x-1)+C
$$

Example 9 Find the following integrals:
(i) $\int \frac{d x}{x^{2}-6 x+13}$
(ii) $\int \frac{d x}{3 x^{2}+13 x-10}$
(iii) $\int \frac{d x}{\sqrt{5 x^{2}-2 x}}$

## Solution

(i) We have $x^{2}-6 x+13=x^{2}-6 x+3^{2}-3^{2}+13=(x-3)^{2}+4$

So, $\int \frac{d x}{x^{2}-6 x+13}=\int \frac{1}{(x-3)^{2}+2^{2}} d x$
Let $\quad x-3=t$. Then $d x=d t$
Therefore, $\quad \int \frac{d x}{x^{2}-6 x+13}=\int \frac{d t}{t^{2}+2^{2}}=\frac{1}{2} \tan ^{-1} \frac{t}{2}+\mathrm{C}$
[by 7.4 (3)]

$$
=\frac{1}{2} \tan ^{-1} \frac{x-3}{2}+\mathrm{C}
$$

(ii) The given integral is of the form 7.4 (7). We write the denominator of the integrand,

$$
\begin{aligned}
3 x^{2}+13 x-10 & =3\left(x^{2}+\frac{13 x}{3}-\frac{10}{3}\right) \\
& =3\left[\left(x+\frac{13}{6}\right)^{2}-\left(\frac{17}{6}\right)^{2}\right] \text { (completing the square) }
\end{aligned}
$$

Thus $\int \frac{d x}{3 x^{2}+13 x-10}=\frac{1}{3} \int \frac{d x}{\left(x+\frac{13}{6}\right)^{2}-\left(\frac{17}{6}\right)^{2}}$
Put $x+\frac{13}{6}=t$. Then $d x=d t$.
Therefore, $\quad \int \frac{d x}{3 x^{2}+13 x-10}=\frac{1}{3} \int \frac{d t}{t^{2}-\left(\frac{17}{6}\right)^{2}}$

$$
\begin{equation*}
=\frac{1}{3 \times 2 \times \frac{17}{6}} \log \left|\frac{t-\frac{17}{6}}{t+\frac{17}{6}}\right|+\mathrm{C}_{1} \tag{i}
\end{equation*}
$$

$$
\begin{aligned}
& =\frac{1}{17} \log \left|\frac{x+\frac{13}{6}-\frac{17}{6}}{x+\frac{13}{6}+\frac{17}{6}}\right|+\mathrm{C}_{1} \\
& =\frac{1}{17} \log \left|\frac{6 x-4}{6 x+30}\right|+\mathrm{C}_{1} \\
& =\frac{1}{17} \log \left|\frac{3 x-2}{x+5}\right|+\mathrm{C}_{1}+\frac{1}{17} \log \frac{1}{3} \\
& =\frac{1}{17} \log \left|\frac{3 x-2}{x+5}\right|+\mathrm{C}, \text { where } \mathrm{C}=\mathrm{C}_{1}+\frac{1}{17} \log \frac{1}{3}
\end{aligned}
$$

(iii) We have $\int \frac{d x}{\sqrt{5 x^{2}-2 x}}=\int \frac{d x}{\sqrt{5\left(x^{2}-\frac{2 x}{5}\right)}}$

$$
=\frac{1}{\sqrt{5}} \int \frac{d x}{\sqrt{\left(x-\frac{1}{5}\right)^{2}-\left(\frac{1}{5}\right)^{2}}} \text { (completing the square) }
$$

Put $x-\frac{1}{5}=t$. Then $d x=d t$.
Therefore, $\quad \int \frac{d x}{\sqrt{5 x^{2}-2 x}}=\frac{1}{\sqrt{5}} \int \frac{d t}{\sqrt{t^{2}-\left(\frac{1}{5}\right)^{2}}}$

$$
\begin{align*}
& =\frac{1}{\sqrt{5}} \log \left|t+\sqrt{t^{2}-\left(\frac{1}{5}\right)^{2}}\right|+\mathrm{C}  \tag{4}\\
& =\frac{1}{\sqrt{5}} \log \left|x-\frac{1}{5}+\sqrt{x^{2}-\frac{2 x}{5}}\right|+\mathrm{C}
\end{align*}
$$

Example 10 Find the following integrals:
(i) $\int \frac{x+2}{2 x^{2}+6 x+5} d x$
(ii) $\int \frac{x+3}{\sqrt{5-4 x-x^{2}}} d x$

## Solution

(i) Using the formula 7.4 (9), we express

$$
x+2=\mathrm{A} \frac{d}{d x}\left(2 x^{2}+6 x+5\right)+\mathrm{B}=\mathrm{A}(4 x+6)+\mathrm{B}
$$

Equating the coefficients of $x$ and the constant terms from both sides, we get $4 \mathrm{~A}=1$ and $6 \mathrm{~A}+\mathrm{B}=2 \quad$ or $\mathrm{A}=\frac{1}{4}$ and $\mathrm{B}=\frac{1}{2}$.
Therefore, $\quad \int \frac{x+2}{2 x^{2}+6 x+5}=\frac{1}{4} \int \frac{4 x+6}{2 x^{2}+6 x+5} d x+\frac{1}{2} \int \frac{d x}{2 x^{2}+6 x+5}$

$$
\begin{equation*}
=\frac{1}{4} \mathrm{I}_{1}+\frac{1}{2} \mathrm{I}_{2} \quad \text { (say) } \tag{1}
\end{equation*}
$$

In $\mathrm{I}_{1}$, put $2 x^{2}+6 x+5=t$, so that $(4 x+6) d x=d t$
Therefore,

$$
\begin{align*}
\mathrm{I}_{1} & =\int \frac{d t}{t}=\log |t|+\mathrm{C}_{1} \\
& =\log \left|2 x^{2}+6 x+5\right|+\mathrm{C}_{1} \tag{2}
\end{align*}
$$

and

$$
\begin{aligned}
\mathrm{I}_{2} & =\int \frac{d x}{2 x^{2}+6 x+5}=\frac{1}{2} \int \frac{d x}{x^{2}+3 x+\frac{5}{2}} \\
& =\frac{1}{2} \int \frac{d x}{\left(x+\frac{3}{2}\right)^{2}+\left(\frac{1}{2}\right)^{2}}
\end{aligned}
$$

Put $x+\frac{3}{2}=t$, so that $d x=d t$, we get

$$
\begin{align*}
\mathrm{I}_{2} & =\frac{1}{2} \int \frac{d t}{t^{2}+\left(\frac{1}{2}\right)^{2}}=\frac{1}{2 \times \frac{1}{2}} \tan ^{-1} 2 t+\mathrm{C}_{2}  \tag{3}\\
& =\tan ^{-1} 2\left(x+\frac{3}{2}\right)+\mathrm{C}_{2}=\tan ^{-1}(2 x+3)+\mathrm{C}_{2} \tag{3}
\end{align*}
$$

Using (2) and (3) in (1), we get

$$
\int \frac{x+2}{2 x^{2}+6 x+5} d x=\frac{1}{4} \log \left|2 x^{2}+6 x+5\right|+\frac{1}{2} \tan ^{-1}(2 x+3)+\mathrm{C}
$$

where,

$$
\mathrm{C}=\frac{\mathrm{C}_{1}}{4}+\frac{\mathrm{C}_{2}}{2}
$$

(ii) This integral is of the form given in 7.4 (10). Let us express
$x+3=\mathrm{A} \frac{d}{d x}\left(5-4 x-x^{2}\right)+\mathrm{B}=\mathrm{A}(-4-2 x)+\mathrm{B}$
Equating the coefficients of $x$ and the constant terms from both sides, we get $-2 \mathrm{~A}=1$ and $-4 \mathrm{~A}+\mathrm{B}=3$, i.e., $\mathrm{A}=-\frac{1}{2}$ and $\mathrm{B}=1$

Therefore, $\int \frac{x+3}{\sqrt{5-4 x-x^{2}}} d x=-\frac{1}{2} \int \frac{(-4-2 x) d x}{\sqrt{5-4 x-x^{2}}}+\int \frac{d x}{\sqrt{5-4 x-x^{2}}}$

$$
\begin{equation*}
=-\frac{1}{2} \mathrm{I}_{1}+\mathrm{I}_{2} \tag{1}
\end{equation*}
$$

In $\mathrm{I}_{1}$, put $5-4 x-x^{2}=t$, so that $(-4-2 x) d x=d t$.
Therefore,

$$
\begin{align*}
\mathrm{I}_{1} & =\int \frac{(-4-2 x) d x}{\sqrt{5-4 x-x^{2}}}=\int \frac{d t}{\sqrt{t}}=2 \sqrt{t}+\mathrm{C}_{1} \\
& =2 \sqrt{5-4 x-x^{2}}+\mathrm{C}_{1} \tag{2}
\end{align*}
$$

Now consider

$$
\mathrm{I}_{2}=\int \frac{d x}{\sqrt{5-4 x-x^{2}}}=\int \frac{d x}{\sqrt{9-(x+2)^{2}}}
$$

Put $x+2=t$, so that $d x=d t$.

Therefore,

$$
\begin{align*}
I_{2} & =\int \frac{d t}{\sqrt{3^{2}-t^{2}}}=\sin ^{-1} \frac{t}{3}+C_{2}  \tag{5}\\
& =\sin ^{-1} \frac{x+2}{3}+C_{2} \tag{3}
\end{align*}
$$

Substituting (2) and (3) in (1), we obtain
$\int \frac{x+3}{\sqrt{5-4 x-x^{2}}}=-\sqrt{5-4 x-x^{2}}+\sin ^{-1} \frac{x+2}{3}+\mathrm{C}$, where $\mathrm{C}=\mathrm{C}_{2}-\frac{\mathrm{C}_{1}}{2}$

## EXERCISE 7.4

Integrate the functions in Exercises 1 to 23.

1. $\frac{3 x^{2}}{x^{6}+1}$
2. $\frac{1}{\sqrt{1+4 x^{2}}}$
3. $\frac{1}{\sqrt{(2-x)^{2}+1}}$
4. $\frac{1}{\sqrt{9-25 x^{2}}}$
5. $\frac{3 x}{1+2 x^{4}}$
6. $\frac{x^{2}}{1-x^{6}}$
7. $\frac{x-1}{\sqrt{x^{2}-1}}$
8. $\frac{x^{2}}{\sqrt{x^{6}+a^{6}}}$
9. $\frac{\sec ^{2} x}{\sqrt{\tan ^{2} x+4}}$
10. $\frac{1}{\sqrt{x^{2}+2 x+2}}$
11. $\frac{1}{9 x^{2}+6 x+5}$
12. $\frac{1}{\sqrt{7-6 x-x^{2}}}$
13. $\frac{1}{\sqrt{(x-1)(x-2)}}$
14. $\frac{1}{\sqrt{8+3 x-x^{2}}}$
15. $\frac{1}{\sqrt{(x-a)(x-b)}}$
16. $\frac{4 x+1}{\sqrt{2 x^{2}+x-3}}$
17. $\frac{x+2}{\sqrt{x^{2}-1}}$
18. $\frac{5 x-2}{1+2 x+3 x^{2}}$
19. $\frac{6 x+7}{\sqrt{(x-5)(x-4)}}$
20. $\frac{x+2}{\sqrt{4 x-x^{2}}}$
21. $\frac{x+2}{\sqrt{x^{2}+2 x+3}}$
22. $\frac{x+3}{x^{2}-2 x-5}$
23. $\frac{5 x+3}{\sqrt{x^{2}+4 x+10}}$.

Choose the correct answer in Exercises 24 and 25.
24. $\int \frac{d x}{x^{2}+2 x+2}$ equals
(A) $x \tan ^{-1}(x+1)+\mathrm{C}$
(B) $\tan ^{-1}(x+1)+C$
(C) $(x+1) \tan ^{-1} x+\mathrm{C}$
(D) $\tan ^{-1} x+\mathrm{C}$
25. $\int \frac{d x}{\sqrt{9 x-4 x^{2}}}$ equals
(A) $\frac{1}{9} \sin ^{-1}\left(\frac{9 x-8}{8}\right)+\mathrm{C}$
(B) $\frac{1}{2} \sin ^{-1}\left(\frac{8 x-9}{9}\right)+\mathrm{C}$
(C) $\frac{1}{3} \sin ^{-1}\left(\frac{9 x-8}{8}\right)+C$
(D) $\frac{1}{2} \sin ^{-1}\left(\frac{9 x-8}{9}\right)+\mathrm{C}$

### 7.5 Integration by Partial Fractions

Recall that a rational function is defined as the ratio of two polynomials in the form $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}$, where $\mathrm{P}(x)$ and $\mathrm{Q}(x)$ are polynomials in $x$ and $\mathrm{Q}(x) \neq 0$. If the degree of $\mathrm{P}(x)$ is less than the degree of $\mathrm{Q}(x)$, then the rational function is called proper, otherwise, it is called improper. The improper rational functions can be reduced to the proper rational
functions by long division process. Thus, if $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}$ is improper, then $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}=\mathrm{T}(x)+\frac{\mathrm{P}_{1}(x)}{\mathrm{Q}(x)}$, where $\mathrm{T}(x)$ is a polynomial in $x$ and $\frac{\mathrm{P}_{1}(x)}{\mathrm{Q}(x)}$ is a proper rational function. As we know how to integrate polynomials, the integration of any rational function is reduced to the integration of a proper rational function. The rational functions which we shall consider here for integration purposes will be those whose denominators can be factorised into linear and quadratic factors. Assume that we want to evaluate $\int \frac{\mathrm{P}(x)}{\mathrm{Q}(x)} d x$, where $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}$ is proper rational function. It is always possible to write the integrand as a sum of simpler rational functions by a method called partial fraction decomposition. After this, the integration can be carried out easily using the already known methods. The following Table 7.2 indicates the types of simpler partial fractions that are to be associated with various kind of rational functions.

Table 7.2

| S.No. | Form of the rational function | Form of the partial fraction |
| :--- | :--- | :--- |
| 1. | $\frac{p x+q}{(x-a)(x-b)}, a \neq b$ | $\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{x-b}$ |
| 2. | $\frac{p x+q}{(x-a)^{2}}$ | $\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{(x-a)^{2}}$ |
| 3. | $\frac{p x^{2}+q x+r}{(x-a)(x-b)(x-c)}$ | $\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{x-b}+\frac{\mathrm{C}}{x-c}$ |
| 4. | $\frac{p x^{2}+q x+r}{(x-a)^{2}(x-b)}$ | $\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{(x-a)^{2}}+\frac{\mathrm{C}}{x-b}$ |
| 5. | where $x^{2}+b x+\mathrm{c}$ cannot be factorised further | $\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B} x+\mathrm{C}}{x^{2}+b x+c}$, |

In the above table, $\mathrm{A}, \mathrm{B}$ and C are real numbers to be determined suitably.

Example 11 Find $\int \frac{d x}{(x+1)(x+2)}$

Solution The integrand is a proper rational function. Therefore, by using the form of partial fraction [Table 7.2 (i)], we write

$$
\begin{equation*}
\frac{1}{(x+1)(x+2)}=\frac{A}{x+1}+\frac{B}{x+2} \tag{1}
\end{equation*}
$$

where, real numbers $A$ and $B$ are to be determined suitably. This gives

$$
1=\mathrm{A}(x+2)+\mathrm{B}(x+1) .
$$

Equating the coefficients of $x$ and the constant term, we get
and

$$
\begin{array}{r}
A+B=0 \\
2 A+B=1
\end{array}
$$

Solving these equations, we get $\mathrm{A}=1$ and $\mathrm{B}=-1$.
Thus, the integrand is given by

$$
\frac{1}{(x+1)(x+2)}=\frac{1}{x+1}+\frac{-1}{x+2}
$$

Therefore,

$$
\begin{aligned}
\int \frac{d x}{(x+1)(x+2)} & =\int \frac{d x}{x+1}-\int \frac{d x}{x+2} \\
& =\log |x+1|-\log |x+2|+\mathrm{C} \\
& =\log \left|\frac{x+1}{x+2}\right|+\mathrm{C}
\end{aligned}
$$

Remark The equation (1) above is an identity, i.e. a statement true for all (permissible) values of $x$. Some authors use the symbol ' $\equiv$ ' to indicate that the statement is an identity and use the symbol ' $=$ ' to indicate that the statement is an equation, i.e., to indicate that the statement is true only for certain values of $x$.

Example 12 Find $\int \frac{x^{2}+1}{x^{2}-5 x+6} d x$
Solution Here the integrand $\frac{x^{2}+1}{x^{2}-5 x+6}$ is not proper rational function, so we divide $x^{2}+1$ by $x^{2}-5 x+6$ and find that

$$
\frac{x^{2}+1}{x^{2}-5 x+6}=1+\frac{5 x-5}{x^{2}-5 x+6}=1+\frac{5 x-5}{(x-2)(x-3)}
$$

Let

$$
\frac{5 x-5}{(x-2)(x-3)}=\frac{A}{x-2}+\frac{B}{x-3}
$$

So that

$$
5 x-5=\mathrm{A}(x-3)+\mathrm{B}(x-2)
$$

Equating the coefficients of $x$ and constant terms on both sides, we get $\mathrm{A}+\mathrm{B}=5$ and $3 A+2 B=5$. Solving these equations, we get $A=-5$ and $B=10$

Thus,

$$
\frac{x^{2}+1}{x^{2}-5 x+6}=1-\frac{5}{x-2}+\frac{10}{x-3}
$$

Therefore,

$$
\begin{aligned}
\int \frac{x^{2}+1}{x^{2}-5 x+6} d x & =\int d x-5 \int \frac{1}{x-2} d x+10 \int \frac{d x}{x-3} \\
& =x-5 \log |x-2|+10 \log |x-3|+\mathrm{C}
\end{aligned}
$$

Example 13 Find $\int \frac{3 x-2}{(x+1)^{2}(x+3)} d x$
Solution The integrand is of the type as given in Table 7.2 (4). We write

$$
\begin{aligned}
\frac{3 x-2}{(x+1)^{2}(x+3)} & =\frac{\mathrm{A}}{x+1}+\frac{\mathrm{B}}{(x+1)^{2}}+\frac{\mathrm{C}}{x+3} \\
3 x-2 & =\mathrm{A}(x+1)(x+3)+\mathrm{B}(x+3)+\mathrm{C}(x+1)^{2} \\
& =\mathrm{A}\left(x^{2}+4 x+3\right)+\mathrm{B}(x+3)+\mathrm{C}\left(x^{2}+2 x+1\right)
\end{aligned}
$$

Comparing coefficient of $x^{2}, x$ and constant term on both sides, we get $\mathrm{A}+\mathrm{C}=0,4 \mathrm{~A}+\mathrm{B}+2 \mathrm{C}=3$ and $3 \mathrm{~A}+3 \mathrm{~B}+\mathrm{C}=-2$. Solving these equations, we get $\mathrm{A}=\frac{11}{4}, \mathrm{~B}=\frac{-5}{2}$ and $\mathrm{C}=\frac{-11}{4}$. Thus the integrand is given by

$$
\frac{3 x-2}{(x+1)^{2}(x+3)}=\frac{11}{4(x+1)}-\frac{5}{2(x+1)^{2}}-\frac{11}{4(x+3)}
$$

Therefore,

$$
\begin{aligned}
\int \frac{3 x-2}{(x+1)^{2}(x+3)} & =\frac{11}{4} \int \frac{d x}{x+1}-\frac{5}{2} \int \frac{d x}{(x+1)^{2}}-\frac{11}{4} \int \frac{d x}{x+3} \\
& =\frac{11}{4} \log |x+1|+\frac{5}{2(x+1)}-\frac{11}{4} \log |x+3|+\mathrm{C} \\
& =\frac{11}{4} \log \left|\frac{x+1}{x+3}\right|+\frac{5}{2(x+1)}+\mathrm{C}
\end{aligned}
$$

Example 14 Find $\int \frac{x^{2}}{\left(x^{2}+1\right)\left(x^{2}+4\right)} d x$
Solution Consider $\frac{x^{2}}{\left(x^{2}+1\right)\left(x^{2}+4\right)}$ and put $x^{2}=y$.

Then

$$
\frac{x^{2}}{\left(x^{2}+1\right)\left(x^{2}+4\right)}=\frac{y}{(y+1)(y+4)}
$$

Write

$$
\frac{y}{(y+1)(y+4)}=\frac{\mathrm{A}}{y+1}+\frac{\mathrm{B}}{y+4}
$$

So that

$$
y=\mathrm{A}(y+4)+\mathrm{B}(y+1)
$$

Comparing coefficients of $y$ and constant terms on both sides, we get $\mathrm{A}+\mathrm{B}=1$ and $4 \mathrm{~A}+\mathrm{B}=0$, which give

$$
\mathrm{A}=-\frac{1}{3} \quad \text { and } \quad \mathrm{B}=\frac{4}{3}
$$

Thus,

$$
\frac{x^{2}}{\left(x^{2}+1\right)\left(x^{2}+4\right)}=-\frac{1}{3\left(x^{2}+1\right)}+\frac{4}{3\left(x^{2}+4\right)}
$$

Therefore,

$$
\begin{aligned}
\int \frac{x^{2} d x}{\left(x^{2}+1\right)\left(x^{2}+4\right)} & =-\frac{1}{3} \int \frac{d x}{x^{2}+1}+\frac{4}{3} \int \frac{d x}{x^{2}+4} \\
& =-\frac{1}{3} \tan ^{-1} x+\frac{4}{3} \times \frac{1}{2} \tan ^{-1} \frac{x}{2}+C \\
& =-\frac{1}{3} \tan ^{-1} x+\frac{2}{3} \tan ^{-1} \frac{x}{2}+C
\end{aligned}
$$

In the above example, the substitution was made only for the partial fraction part and not for the integration part. Now, we consider an example, where the integration involves a combination of the substitution method and the partial fraction method.

Example 15 Find $\int \frac{(3 \sin \phi-2) \cos \phi}{5-\cos ^{2} \phi-4 \sin \phi} d \phi$
Solution Let $y=\sin \phi$
Then

$$
d y=\cos \phi d \phi
$$

Therefore, $\quad \int \frac{(3 \sin \phi-2) \cos \phi}{5-\cos ^{2} \phi-4 \sin \phi} d \phi=\int \frac{(3 y-2) d y}{5-\left(1-y^{2}\right)-4 y}$

$$
\begin{aligned}
& =\int \frac{3 y-2}{y^{2}-4 y+4} d y \\
& =\int \frac{3 y-2}{(y-2)^{2}}=\mathrm{I} \text { (say) }
\end{aligned}
$$

Now, we write

$$
\frac{3 y-2}{(y-2)^{2}}=\frac{\mathrm{A}}{y-2}+\frac{\mathrm{B}}{(y-2)^{2}}
$$

[by Table 7.2 (2)]

Therefore,

$$
3 y-2=\mathrm{A}(y-2)+\mathrm{B}
$$

Comparing the coefficients of $y$ and constant term, we get $\mathrm{A}=3$ and $\mathrm{B}-2 \mathrm{~A}=-2$, which gives $\mathrm{A}=3$ and $\mathrm{B}=4$.
Therefore, the required integral is given by

$$
\begin{aligned}
\mathrm{I} & =\int\left[\frac{3}{y-2}+\frac{4}{(y-2)^{2}}\right] d y=3 \int \frac{d y}{y-2}+4 \int \frac{d y}{(y-2)^{2}} \\
& =3 \log |y-2|+4\left(-\frac{1}{y-2}\right)+\mathrm{C} \\
& =3 \log |\sin \phi-2|+\frac{4}{2-\sin \phi}+\mathrm{C} \\
& =3 \log (2-\sin \phi)+\frac{4}{2-\sin \phi}+\mathrm{C}(\text { since, } 2-\sin \phi \text { is always positive })
\end{aligned}
$$

Example 16 Find $\int \frac{x^{2}+x+1 d x}{(x+2)\left(x^{2}+1\right)}$
Solution The integrand is a proper rational function. Decompose the rational function into partial fraction [Table 2.2(5)]. Write

Therefore,

$$
\frac{x^{2}+x+1}{\left(x^{2}+1\right)(x+2)}=\frac{\mathrm{A}}{x+2}+\frac{\mathrm{B} x+\mathrm{C}}{\left(x^{2}+1\right)}
$$

Therefore,

$$
x^{2}+x+1=\mathrm{A}\left(x^{2}+1\right)+(\mathrm{B} x+\mathrm{C})(x+2)
$$

Equating the coefficients of $x^{2}, x$ and of constant term of both sides, we get $\mathrm{A}+\mathrm{B}=1,2 \mathrm{~B}+\mathrm{C}=1$ and $\mathrm{A}+2 \mathrm{C}=1$. Solving these equations, we get $\mathrm{A}=\frac{3}{5}, \mathrm{~B}=\frac{2}{5}$ and $\mathrm{C}=\frac{1}{5}$

Thus, the integrand is given by

$$
\frac{x^{2}+x+1}{\left(x^{2}+1\right)(x+2)}=\frac{3}{5(x+2)}+\frac{\frac{2}{5} x+\frac{1}{5}}{x^{2}+1}=\frac{3}{5(x+2)}+\frac{1}{5}\left(\frac{2 x+1}{x^{2}+1}\right)
$$

Therefore, $\quad \int \frac{x^{2}+x+1}{\left(x^{2}+1\right)(x+2)} d x=\frac{3}{5} \int \frac{d x}{x+2}+\frac{1}{5} \int \frac{2 x}{x^{2}+1} d x+\frac{1}{5} \int \frac{1}{x^{2}+1} d x$

$$
=\frac{3}{5} \log |x+2|+\frac{1}{5} \log \left|x^{2}+1\right|+\frac{1}{5} \tan ^{-1} x+\mathrm{C}
$$

## EXERCISE 7.5

Integrate the rational functions in Exercises 1 to 21.

1. $\frac{x}{(x+1)(x+2)}$
2. $\frac{1}{x^{2}-9}$
3. $\frac{3 x-1}{(x-1)(x-2)(x-3)}$
4. $\frac{x}{(x-1)(x-2)(x-3)}$
5. $\frac{2 x}{x^{2}+3 x+2}$
6. $\frac{1-x^{2}}{x(1-2 x)}$
7. $\frac{x}{\left(x^{2}+1\right)(x-1)}$
8. $\frac{x}{(x-1)^{2}(x+2)}$
9. $\frac{3 x+5}{x^{3}-x^{2}-x+1}$
10. $\frac{2 x-3}{\left(x^{2}-1\right)(2 x+3)}$
11. $\frac{5 x}{(x+1)\left(x^{2}-4\right)}$
12. $\frac{x^{3}+x+1}{x^{2}-1}$
13. $\frac{2}{(1-x)\left(1+x^{2}\right)}$
14. $\frac{3 x-1}{(x+2)^{2}}$
15. $\frac{1}{x^{4}-1}$
16. $\frac{1}{x\left(x^{n}+1\right)}$ [Hint: multiply numerator and denominator by $x^{n-1}$ and put $\left.x^{n}=t\right]$
17. $\frac{\cos x}{(1-\sin x)(2-\sin x)}$
[Hint : Put $\sin x=t$ ]
18. $\frac{\left(x^{2}+1\right)\left(x^{2}+2\right)}{\left(x^{2}+3\right)\left(x^{2}+4\right)}$
19. $\frac{2 x}{\left(x^{2}+1\right)\left(x^{2}+3\right)}$
20. $\frac{1}{x\left(x^{4}-1\right)}$
21. $\frac{1}{\left(e^{x}-1\right)}\left[\right.$ Hint : Put $\left.e^{x}=t\right]$

Choose the correct answer in each of the Exercises 22 and 23.
22. $\int \frac{x d x}{(x-1)(x-2)}$ equals
(A) $\log \left|\frac{(x-1)^{2}}{x-2}\right|+C$
(B) $\quad \log \left|\frac{(x-2)^{2}}{x-1}\right|+C$
(C) $\log \left|\left(\frac{x-1}{x-2}\right)^{2}\right|+\mathrm{C}$
(D) $\log |(x-1)(x-2)|+C$
23. $\int \frac{d x}{x\left(x^{2}+1\right)}$ equals
(A) $\log |x|-\frac{1}{2} \log \left(x^{2}+1\right)+C$
(B) $\log |x|+\frac{1}{2} \log \left(x^{2}+1\right)+C$
(C) $-\log |x|+\frac{1}{2} \log \left(x^{2}+1\right)+C$
(D) $\frac{1}{2} \log |x|+\log \left(x^{2}+1\right)+C$

### 7.6 Integration by Parts

In this section, we describe one more method of integration, that is found quite useful in integrating products of functions.

If $u$ and $v$ are any two differentiable functions of a single variable $x$ (say). Then, by the product rule of differentiation, we have

$$
\frac{d}{d x}(u v)=u \frac{d v}{d x}+v \frac{d u}{d x}
$$

Integrating both sides, we get
or

$$
\begin{align*}
u v & =\int u \frac{d v}{d x} d x+\int v \frac{d u}{d x} d x \\
\int u \frac{d v}{d x} d x & =u v-\int v \frac{d u}{d x} d x  \tag{1}\\
u & =f(x) \text { and } \frac{d v}{d x}=\mathrm{g}(x) . \text { Then } \\
\frac{d u}{d x} & =f^{\prime}(x) \text { and } v=\int g(x) d x
\end{align*}
$$

Let

Therefore, expression (1) can be rewritten as
i.e.,

$$
\begin{aligned}
\int f(x) g(x) d x & =f(x) \int g(x) d x-\int\left[\int g(x) d x\right] f^{\prime}(x) d x \\
\int f(x) g(x) d x & =f(x) \int g(x) d x-\int\left[f^{\prime}(x) \int g(x) d x\right] d x
\end{aligned}
$$

If we take $f$ as the first function and $g$ as the second function, then this formula may be stated as follows:
"The integral of the product of two functions $=($ first function $) \times($ integral of the second function) - Integral of [(differential coefficient of the first function) $\times$ (integral of the second function)]"
Example 17 Find $\int x \cos x d x$
Solution Put $f(x)=x$ (first function) and $g(x)=\cos x$ (second function). Then, integration by parts gives

$$
\begin{aligned}
\int x \cos x d x & =x \int \cos x d x-\int\left[\frac{d}{d x}(x) \int \cos x d x\right] d x \\
& =x \sin x-\int \sin x d x=x \sin x+\cos x+\mathrm{C}
\end{aligned}
$$

Suppose, we take $f(x)=\cos x$ and $g(x)=x$. Then

$$
\begin{aligned}
\int x \cos x d x & =\cos x \int x d x-\int\left[\frac{d}{d x}(\cos x) \int x d x\right] d x \\
& =(\cos x) \frac{x^{2}}{2}+\int \sin x \frac{x^{2}}{2} d x
\end{aligned}
$$

Thus, it shows that the integral $\int x \cos x d x$ is reduced to the comparatively more complicated integral having more power of $x$. Therefore, the proper choice of the first function and the second function is significant.

## Remarks

(i) It is worth mentioning that integration by parts is not applicable to product of functions in all cases. For instance, the method does not work for $\int \sqrt{x} \sin x d x$. The reason is that there does not exist any function whose derivative is $\sqrt{x} \sin x$.
(ii) Observe that while finding the integral of the second function, we did not add any constant of integration. If we write the integral of the second function $\cos x$
as $\sin x+k$, where $k$ is any constant, then

$$
\begin{aligned}
\int x \cos x d x & =x(\sin x+k)-\int(\sin x+k) d x \\
& =x(\sin x+k)-\int\left(\sin x d x-\int k d x\right. \\
& =x(\sin x+k)-\cos x-k x+\mathrm{C}=x \sin x+\cos x+\mathrm{C}
\end{aligned}
$$

This shows that adding a constant to the integral of the second function is superfluous so far as the final result is concerned while applying the method of integration by parts.
(iii) Usually, if any function is a power of $x$ or a polynomial in $x$, then we take it as the first function. However, in cases where other function is inverse trigonometric function or logarithmic function, then we take them as first function.
Example 18 Find $\int \log x d x$
Solution To start with, we are unable to guess a function whose derivative is $\log x$. We take $\log x$ as the first function and the constant function 1 as the second function. Then, the integral of the second function is $x$.

Hence,

$$
\begin{aligned}
\int(\log x .1) d x & =\log x \int 1 d x-\int\left[\frac{d}{d x}(\log x) \int 1 d x\right] d x \\
& =(\log x) \cdot x-\int \frac{1}{x} x d x=x \log x-x+\mathrm{C}
\end{aligned}
$$

Example 19 Find $\int x e^{x} d x$
Solution Take first function as $x$ and second function as $e^{x}$. The integral of the second function is $e^{x}$.

Therefore,

$$
\int x e^{x} d x=x e^{x}-\int 1 \cdot e^{x} d x=x e^{x}-e^{x}+\mathrm{C}
$$

Example 20 Find $\int \frac{x \sin ^{-1} x}{\sqrt{1-x^{2}}} d x$
Solution Let first function be $\sin ^{-1} x$ and second function be $\frac{x}{\sqrt{1-x^{2}}}$.
First we find the integral of the second function, i.e., $\int \frac{x d x}{\sqrt{1-x^{2}}}$.
Put $t=1-x^{2}$. Then $d t=-2 x d x$

Therefore,

$$
\int \frac{x d x}{\sqrt{1-x^{2}}}=-\frac{1}{2} \int \frac{d t}{\sqrt{t}}=-\sqrt{t}=-\sqrt{1-x^{2}}
$$

Hence,

$$
\begin{aligned}
\int \frac{x \sin ^{-1} x}{\sqrt{1-x^{2}}} d x & =\left(\sin ^{-1} x\right)\left(-\sqrt{1-x^{2}}\right)-\int \frac{1}{\sqrt{1-x^{2}}}\left(-\sqrt{1-x^{2}}\right) d x \\
& =-\sqrt{1-x^{2}} \sin ^{-1} x+x+\mathrm{C}=x-\sqrt{1-x^{2}} \sin ^{-1} x+\mathrm{C}
\end{aligned}
$$

Alternatively, this integral can also be worked out by making substitution $\sin ^{-1} x=\theta$ and then integrating by parts.

Example 21 Find $\int e^{x} \sin x d x$
Solution Take $e^{x}$ as the first function and $\sin x$ as second function. Then, integrating by parts, we have

$$
\begin{align*}
\mathrm{I}=\int e^{x} \sin x d x & =e^{x}(-\cos x)+\int e^{x} \cos x d x \\
& =-e^{x} \cos x+\mathrm{I}_{1} \text { (say) } \tag{1}
\end{align*}
$$

Taking $e^{x}$ and $\cos x$ as the first and second functions, respectively, in $\mathrm{I}_{1}$, we get

$$
\mathrm{I}_{1}=e^{x} \sin x-\int e^{x} \sin x d x
$$

Substituting the value of $\mathrm{I}_{1}$ in (1), we get

$$
\mathrm{I}=-e^{x} \cos x+e^{x} \sin x-\mathrm{I} \text { or } 2 \mathrm{I}=e^{x}(\sin x-\cos x)
$$

Hence,

$$
\mathrm{I}=\int e^{x} \sin x d x=\frac{e^{x}}{2}(\sin x-\cos x)+\mathrm{C}
$$

Alternatively, above integral can also be determined by taking $\sin x$ as the first function and $e^{x}$ the second function.
76.1 Integral of the type $\int e^{x}\left[f(x)+f^{\prime}(x)\right] d x$

We have

$$
\begin{align*}
\mathrm{I} & =\int e^{x}\left[f(x)+f^{\prime}(x)\right] d x=\int e^{x} f(x) d x+\int e^{x} f^{\prime}(x) d x \\
& =\mathrm{I}_{1}+\int e^{x} f^{\prime}(x) d x, \text { where } \mathrm{I}_{1}=\int e^{x} f(x) d x \tag{1}
\end{align*}
$$

Taking $f(x)$ and $e^{x}$ as the first function and second function, respectively, in $\mathrm{I}_{1}$ and integrating it by parts, we have $\mathrm{I}_{1}=f(x) e^{x}-\int f^{\prime}(x) e^{x} d x+\mathrm{C}$
Substituting $\mathrm{I}_{1}$ in (1), we get

$$
\mathrm{I}=e^{x} f(x)-\int f^{\prime}(x) e^{x} d x+\int e^{x} f^{\prime}(x) d x+\mathrm{C}=e^{x} f(x)+\mathrm{C}
$$

Thus,

$$
\int e^{x}\left[f(x)+f^{\prime}(x)\right] d x=e^{x} f(x)+\mathrm{C}
$$

Example 22 Find (i) $\int e^{x}\left(\tan ^{-1} x+\frac{1}{1+x^{2}}\right) d x$ (ii) $\int \frac{\left(x^{2}+1\right) e^{x}}{(x+1)^{2}} d x$

## Solution

(i) We have $\mathrm{I}=\int e^{x}\left(\tan ^{-1} x+\frac{1}{1+x^{2}}\right) d x$

Consider $f(x)=\tan ^{-1} x$, then $f^{\prime}(x)=\frac{1}{1+x^{2}}$
Thus, the given integrand is of the form $e^{x}\left[f(x)+f^{\prime}(x)\right]$.
Therefore, $\mathrm{I}=\int e^{x}\left(\tan ^{-1} x+\frac{1}{1+x^{2}}\right) d x=e^{x} \tan ^{-1} x+\mathrm{C}$
(ii) We have $\mathrm{I}=\int \frac{\left(x^{2}+1\right) e^{x}}{(x+1)^{2}} d x=\int e^{x}\left[\frac{\left.x^{2}-1+1+1\right)}{(x+1)^{2}}\right] d x$

$$
=\int e^{x}\left[\frac{x^{2}-1}{(x+1)^{2}}+\frac{2}{(x+1)^{2}}\right] d x=\int e^{x}\left[\frac{x-1}{x+1}+\frac{2}{(x+1)^{2}}\right] d x
$$

Consider $f(x)=\frac{x-1}{x+1}$, then $f^{\prime}(x)=\frac{2}{(x+1)^{2}}$
Thus, the given integrand is of the form $e^{x}\left[f(x)+f^{\prime}(x)\right]$.
Therefore, $\quad \int \frac{x^{2}+1}{(x+1)^{2}} e^{x} d x=\frac{x-1}{x+1} e^{x}+\mathrm{C}$

## EXERCISE 7.6

Integrate the functions in Exercises 1 to 22.

1. $x \sin x$
2. $x \sin 3 x$
3. $x^{2} e^{x}$
4. $x \log x$
5. $x \log 2 x$
6. $x^{2} \log x$
7. $x \sin ^{-1} x$
8. $x \tan ^{-1} x$
9. $x \cos ^{-1} x$
10. $\left(\sin ^{-1} x\right)^{2}$
11. $\frac{x \cos ^{-1} x}{\sqrt{1-x^{2}}}$
12. $x \sec ^{2} x$
13. $\tan ^{-1} x$
14. $x(\log x)^{2}$
15. $\left(x^{2}+1\right) \log x$
16. $e^{x}(\sin x+\cos x)$
17. $\frac{x e^{x}}{(1+x)^{2}}$
18. $e^{x}\left(\frac{1+\sin x}{1+\cos x}\right)$
19. $e^{x}\left(\frac{1}{x}-\frac{1}{x^{2}}\right)$
20. $\frac{(x-3) e^{x}}{(x-1)^{3}}$
21. $e^{2 x} \sin x$
22. $\sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right)$

Choose the correct answer in Exercises 23 and 24.
23. $\int x^{2} e^{x^{3}} d x$ equals
(A) $\frac{1}{3} e^{x^{3}}+\mathrm{C}$
(B) $\frac{1}{3} e^{x^{2}}+\mathrm{C}$
(C) $\frac{1}{2} e^{x^{3}}+\mathrm{C}$
(D) $\frac{1}{2} e^{x^{2}}+\mathrm{C}$
24. $\int e^{x} \sec x(1+\tan x) d x$ equals
(A) $e^{x} \cos x+\mathrm{C}$
(B) $e^{x} \sec x+\mathrm{C}$
(C) $e^{x} \sin x+\mathrm{C}$
(D) $e^{x} \tan x+\mathrm{C}$

### 7.6.2 Integrals of some more types

Here, we discuss some special types of standard integrals based on the technique of integration by parts :
(i) $\int \sqrt{x^{2}-a^{2}} d x$
(ii) $\int \sqrt{x^{2}+a^{2}} d x$
(iii) $\int \sqrt{a^{2}-x^{2}} d x$
(i) Let $\mathrm{I}=\int \sqrt{x^{2}-a^{2}} d x$

Taking constant function 1 as the second function and integrating by parts, we have

$$
\begin{aligned}
\mathrm{I} & =x \sqrt{x^{2}-a^{2}}-\int \frac{1}{2} \frac{2 x}{\sqrt{x^{2}-a^{2}}} x d x \\
& =x \sqrt{x^{2}-a^{2}}-\int \frac{x^{2}}{\sqrt{x^{2}-a^{2}}} d x=x \sqrt{x^{2}-a^{2}}-\int \frac{x^{2}-a^{2}+a^{2}}{\sqrt{x^{2}-a^{2}}} d x
\end{aligned}
$$

or
or

$$
\begin{aligned}
& =x \sqrt{x^{2}-a^{2}}-\int \sqrt{x^{2}-a^{2}} d x-a^{2} \int \frac{d x}{\sqrt{x^{2}-a^{2}}} \\
& =x \sqrt{x^{2}-a^{2}}-\mathrm{I}-a^{2} \int \frac{d x}{\sqrt{x^{2}-a^{2}}} \\
2 \mathrm{I} & =x \sqrt{x^{2}-a^{2}}-a^{2} \int \frac{d x}{\sqrt{x^{2}-a^{2}}} \\
\mathbf{I} & =\int \sqrt{\boldsymbol{x}^{\mathbf{2}}-\boldsymbol{a}^{\mathbf{2}}} \boldsymbol{d} \boldsymbol{x}=\frac{\boldsymbol{x}}{\mathbf{2}} \sqrt{\boldsymbol{x}^{\mathbf{2}}-\boldsymbol{a}^{\mathbf{2}}}-\frac{\boldsymbol{a}^{\mathbf{2}}}{\mathbf{2}} \boldsymbol{\operatorname { l o g }}\left|\boldsymbol{x}+\sqrt{\boldsymbol{x}^{\mathbf{2}}-\boldsymbol{a}^{\mathbf{2}}}\right|+\mathbf{C}
\end{aligned}
$$

Similarly, integrating other two integrals by parts, taking constant function 1 as the second function, we get
(ii) $\int \sqrt{x^{2}+a^{2}} d x=\frac{1}{2} x \sqrt{x^{2}+a^{2}}+\frac{a^{2}}{2} \log \left|x+\sqrt{x^{2}+a^{2}}\right|+\mathrm{C}$
(iii) $\int \sqrt{a^{2}-x^{2}} d x=\frac{1}{2} x \sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2} \sin ^{-1} \frac{x}{a}+\mathrm{C}$

Alternatively, integrals (i), (ii) and (iii) can also be found by making trigonometric substitution $x=a \sec \theta$ in (i), $x=a \tan \theta$ in (ii) and $x=a \sin \theta$ in (iii) respectively.
Example 23 Find $\int \sqrt{x^{2}+2 x+5} d x$
Solution Note that

$$
\int \sqrt{x^{2}+2 x+5} d x=\int \sqrt{(x+1)^{2}+4} d x
$$

Put $x+1=y$, so that $d x=d y$. Then

$$
\begin{align*}
\int \sqrt{x^{2}+2 x+5} d x & =\int \sqrt{y^{2}+2^{2}} d y \\
& =\frac{1}{2} y \sqrt{y^{2}+4}+\frac{4}{2} \log \left|y+\sqrt{y^{2}+4}\right|+\mathrm{C} \quad[\text { using 7.6.2 }  \tag{ii}\\
& =\frac{1}{2}(x+1) \sqrt{x^{2}+2 x+5}+2 \log \left|x+1+\sqrt{x^{2}+2 x+5}\right|+\mathrm{C}
\end{align*}
$$

Example 24 Find $\int \sqrt{3-2 x-x^{2}} d x$
Solution Note that $\int \sqrt{3-2 x-x^{2}} d x=\int \sqrt{4-(x+1)^{2}} d x$

Put $x+1=y$ so that $d x=d y$.
Thus

$$
\begin{aligned}
\int \sqrt{3-2 x-x^{2}} d x & =\int \sqrt{4-y^{2}} d y \\
& =\frac{1}{2} y \sqrt{4-y^{2}}+\frac{4}{2} \sin ^{-1} \frac{y}{2}+\mathrm{C} \quad[\text { using 7.6.2 (iii) }] \\
& =\frac{1}{2}(x+1) \sqrt{3-2 x-x^{2}}+2 \sin ^{-1}\left(\frac{x+1}{2}\right)+\mathrm{C}
\end{aligned}
$$

## EXERCISE 7.7

Integrate the functions in Exercises 1 to 9.

1. $\sqrt{4-x^{2}}$
2. $\sqrt{1-4 x^{2}}$
3. $\sqrt{x^{2}+4 x+6}$
4. $\sqrt{x^{2}+4 x+1}$
5. $\sqrt{1-4 x-x^{2}}$
6. $\sqrt{x^{2}+4 x-5}$
7. $\sqrt{1+3 x-x^{2}}$
8. $\sqrt{x^{2}+3 x}$
9. $\sqrt{1+\frac{x^{2}}{9}}$

Choose the correct answer in Exercises 10 to 11.
10. $\int \sqrt{1+x^{2}} d x$ is equal to
(A) $\frac{x}{2} \sqrt{1+x^{2}}+\frac{1}{2} \log \left|\left(x+\sqrt{1+x^{2}}\right)\right|+\mathrm{C}$
(B) $\frac{2}{3}\left(1+x^{2}\right)^{\frac{3}{2}}+\mathrm{C}$
(C) $\frac{2}{3} x\left(1+x^{2}\right)^{\frac{3}{2}}+\mathrm{C}$
(D) $\frac{x^{2}}{2} \sqrt{1+x^{2}}+\frac{1}{2} x^{2} \log \left|x+\sqrt{1+x^{2}}\right|+\mathrm{C}$
11. $\int \sqrt{x^{2}-8 x+7} d x$ is equal to
(A) $\frac{1}{2}(x-4) \sqrt{x^{2}-8 x+7}+9 \log \left|x-4+\sqrt{x^{2}-8 x+7}\right|+\mathrm{C}$
(B) $\frac{1}{2}(x+4) \sqrt{x^{2}-8 x+7}+9 \log \left|x+4+\sqrt{x^{2}-8 x+7}\right|+\mathrm{C}$
(C) $\frac{1}{2}(x-4) \sqrt{x^{2}-8 x+7}-3 \sqrt{2} \log \left|x-4+\sqrt{x^{2}-8 x+7}\right|+\mathrm{C}$
(D) $\frac{1}{2}(x-4) \sqrt{x^{2}-8 x+7}-\frac{9}{2} \log \left|x-4+\sqrt{x^{2}-8 x+7}\right|+\mathrm{C}$

### 7.7 Definite Integral

In the previous sections, we have studied about the indefinite integrals and discussed few methods of finding them including integrals of some special functions. In this section, we shall study what is called definite integral of a function. The definite integral has a unique value. A definite integral is denoted by $\int_{a}^{b} f(x) d x$, where $a$ is called the lower limit of the integral and $b$ is called the upper limit of the integral. The definite integral is introduced either as the limit of a sum or if it has an anti derivative F in the interval $[a, b]$, then its value is the difference between the values of F at the end points, i.e., $\mathrm{F}(b)-\mathrm{F}(a)$.

### 7.8 Fundamental Theorem of Calculus

### 7.8.1 Area function

We have defined $\int_{a}^{b} f(x) d x$ as the area of the region bounded by the curve $y=f(x)$, the ordinates $x=a$ and $x=b$ and $x$-axis. Let $x$ be a given point in $[a, b]$. Then $\int_{a}^{x} f(x) d x$ represents the area of the light shaded region in Fig 7.1 [Here it is assumed that $f(x)>0$ for $x \in[a, b]$, the assertion made below is equally true for other functions as well]. The area of this shaded region depends upon
![](https://cdn.mathpix.com/cropped/2025_07_21_6f1e5706ec7b4b2554adg-43.jpg?height=526&width=603&top_left_y=932&top_left_x=808) the value of $x$.

In other words, the area of this shaded region is a function of $x$. We denote this function of $x$ by $\mathrm{A}(x)$. We call the function $\mathrm{A}(x)$ as Area function and is given by

$$
\begin{equation*}
\mathbf{A}(x)=\int_{a}^{x} f(x) d x \tag{1}
\end{equation*}
$$

Based on this definition, the two basic fundamental theorems have been given. However, we only state them as their proofs are beyond the scope of this text book.

### 7.8.2 First fundamental theorem of integral calculus

Theorem 1 Let $f$ be a continuous function on the closed interval $[a, b]$ and let $\mathrm{A}(x)$ be the area function. Then $\mathbf{A}^{\prime}(\boldsymbol{x})=\boldsymbol{f}(\boldsymbol{x})$, for all $\boldsymbol{x} \in[\boldsymbol{a}, \boldsymbol{b}]$.

### 7.8.3 Second fundamental theorem of integral calculus

We state below an important theorem which enables us to evaluate definite integrals by making use of anti derivative.

Theorem 2 Let $f$ be continuous function defined on the closed interval $[a, b]$ and F be an anti derivative of $f$. Then $\int_{a}^{b} f(x) d x=[\mathbf{F}(x)]_{a}^{b}=\mathbf{F}(b)-\mathbf{F}(a)$.

## Remarks

(i) In words, the Theorem 2 tells us that $\int_{a}^{b} f(x) d x=$ (value of the anti derivative F of $f$ at the upper limit $b-$ value of the same anti derivative at the lower limit $a$ ).
(ii) This theorem is very useful, because it gives us a method of calculating the definite integral more easily, without calculating the limit of a sum.
(iii) The crucial operation in evaluating a definite integral is that of finding a function whose derivative is equal to the integrand. This strengthens the relationship between differentiation and integration.
(iv) In $\int_{a}^{b} f(x) d x$, the function $f$ needs to be well defined and continuous in $[a, b]$. For instance, the consideration of definite integral $\int_{-2}^{3} x\left(x^{2}-1\right)^{\frac{1}{2}} d x$ is erroneous since the function $f$ expressed by $f(x)=x\left(x^{2}-1\right)^{\frac{1}{2}}$ is not defined in a portion $-1<x<1$ of the closed interval $[-2,3]$.

Steps for calculating $\int_{a}^{b} f(x) d x$.
(i) Find the indefinite integral $\int f(x) d x$. Let this be $\mathrm{F}(x)$. There is no need to keep integration constant C because if we consider $\mathrm{F}(x)+\mathrm{C}$ instead of $\mathrm{F}(x)$, we get $\int_{a}^{b} f(x) d x=[\mathrm{F}(x)+\mathrm{C}]_{a}^{b}=[\mathrm{F}(b)+\mathrm{C}]-[\mathrm{F}(a)+\mathrm{C}]=\mathrm{F}(b)-\mathrm{F}(a)$.
Thus, the arbitrary constant disappears in evaluating the value of the definite integral.
(ii) Evaluate $\mathrm{F}(b)-\mathrm{F}(a)=[\mathrm{F}(x)]_{a}^{b}$, which is the value of $\int_{a}^{b} f(x) d x$.

We now consider some examples

Example 25 Evaluate the following integrals:
(i) $\int_{2}^{3} x^{2} d x$
(ii) $\int_{4}^{9} \frac{\sqrt{x}}{\left(30-x^{\frac{3}{2}}\right)^{2}} d x$
(iii) $\int_{1}^{2} \frac{x d x}{(x+1)(x+2)}$
(iv) $\int_{0}^{\frac{\pi}{4}} \sin ^{3} 2 t \cos 2 t d t$

## Solution

(i) Let $\mathrm{I}=\int_{2}^{3} x^{2} d x$. Since $\int x^{2} d x=\frac{x^{3}}{3}=\mathrm{F}(x)$,

Therefore, by the second fundamental theorem, we get

$$
I=F(3)-F(2)=\frac{27}{3}-\frac{8}{3}=\frac{19}{3}
$$

(ii) Let $\mathrm{I}=\int_{4}^{9} \frac{\sqrt{x}}{\left(30-x^{\frac{3}{2}}\right)^{2}} d x$. We first find the anti derivative of the integrand.

Put $30-x^{\frac{3}{2}}=t$. Then $-\frac{3}{2} \sqrt{x} d x=d t$ or $\sqrt{x} d x=-\frac{2}{3} d t$
Thus, $\int \frac{\sqrt{x}}{\left(30-x^{\frac{3}{2}}\right)^{2}} d x=-\frac{2}{3} \int \frac{d t}{t^{2}}=\frac{2}{3}\left[\frac{1}{t}\right]=\frac{2}{3}\left[\frac{1}{\left(30-x^{\frac{3}{2}}\right)}\right]=\mathrm{F}(x)$
Therefore, by the second fundamental theorem of calculus, we have

$$
\begin{aligned}
\mathrm{I} & =\mathrm{F}(9)-\mathrm{F}(4)=\frac{2}{3}\left[\frac{1}{\left(30-x^{\frac{3}{2}}\right)}\right]_{4}^{9} \\
& =\frac{2}{3}\left[\frac{1}{(30-27)}-\frac{1}{30-8}\right]=\frac{2}{3}\left[\frac{1}{3}-\frac{1}{22}\right]=\frac{19}{99}
\end{aligned}
$$

(iii) Let $\mathrm{I}=\int_{1}^{2} \frac{x d x}{(x+1)(x+2)}$

Using partial fraction, we get $\frac{x}{(x+1)(x+2)}=\frac{-1}{x+1}+\frac{2}{x+2}$

So

$$
\int \frac{x d x}{(x+1)(x+2)}=-\log |x+1|+2 \log |x+2|=\mathrm{F}(x)
$$

Therefore, by the second fundamental theorem of calculus, we have

$$
\begin{aligned}
I & =F(2)-F(1)=[-\log 3+2 \log 4]-[-\log 2+2 \log 3] \\
& =-3 \log 3+\log 2+2 \log 4=\log \left(\frac{32}{27}\right)
\end{aligned}
$$

(iv) Let $\mathrm{I}=\int_{0}^{\frac{\pi}{4}} \sin ^{3} 2 t \cos 2 t d t$. Consider $\int \sin ^{3} 2 t \cos 2 t d t$

Put $\sin 2 t=u$ so that $2 \cos 2 t d t=d u$ or $\cos 2 t d t=\frac{1}{2} d u$

So

$$
\begin{aligned}
\int \sin ^{3} 2 t \cos 2 t d t & =\frac{1}{2} \int u^{3} d u \\
& =\frac{1}{8}\left[u^{4}\right]=\frac{1}{8} \sin ^{4} 2 t=\mathrm{F}(t) \text { say }
\end{aligned}
$$

Therefore, by the second fundamental theorem of integral calculus
$I=F\left(\frac{\pi}{4}\right)-F(0)=\frac{1}{8}\left[\sin ^{4} \frac{\pi}{2}-\sin ^{4} 0\right]=\frac{1}{8}$

## EXERCISE 7.8

Evaluate the definite integrals in Exercises 1 to 20.

1. $\int_{-1}^{1}(x+1) d x$
2. $\int_{2}^{3} \frac{1}{x} d x$
3. $\int_{1}^{2}\left(4 x^{3}-5 x^{2}+6 x+9\right) d x$
4. $\int_{0}^{\frac{\pi}{4}} \sin 2 x d x$
5. $\int_{0}^{\frac{\pi}{2}} \cos 2 x d x$
6. $\int_{4}^{5} e^{x} d x$
7. $\int_{0}^{\frac{\pi}{4}} \tan x d x$
8. $\int_{\frac{\pi}{6}}^{\frac{\pi}{4}} \operatorname{cosec} x d x$
9. $\int_{0}^{1} \frac{d x}{\sqrt{1-x^{2}}}$
10. $\int_{0}^{1} \frac{d x}{1+x^{2}}$
11. $\int_{2}^{3} \frac{d x}{x^{2}-1}$
12. $\int_{0}^{\frac{\pi}{2}} \cos ^{2} x d x$
13. $\int_{2}^{3} \frac{x d x}{x^{2}+1}$
14. $\int_{0}^{1} \frac{2 x+3}{5 x^{2}+1} d x$
15. $\int_{0}^{1} x e^{x^{2}} d x$
16. $\int_{1}^{2} \frac{5 x^{2}}{x^{2}+4 x+3}$
17. $\int_{0}^{\frac{\pi}{4}}\left(2 \sec ^{2} x+x^{3}+2\right) d x$
18. $\int_{0}^{\pi}\left(\sin ^{2} \frac{x}{2}-\cos ^{2} \frac{x}{2}\right) d x$
19. $\int_{0}^{2} \frac{6 x+3}{x^{2}+4} d x$
20. $\int_{0}^{1}\left(x e^{x}+\sin \frac{\pi x}{4}\right) d x$

Choose the correct answer in Exercises 21 and 22.
21. $\int_{1}^{\sqrt{3}} \frac{d x}{1+x^{2}}$ equals
(A) $\frac{\pi}{3}$
(B) $\frac{2 \pi}{3}$
(C) $\frac{\pi}{6}$
(D) $\frac{\pi}{12}$
22. $\int_{0}^{\frac{2}{3}} \frac{d x}{4+9 x^{2}}$ equals
(A) $\frac{\pi}{6}$
(B) $\frac{\pi}{12}$
(C) $\frac{\pi}{24}$
(D) $\frac{\pi}{4}$

### 7.9 Evaluation of Definite Integrals by Substitution

In the previous sections, we have discussed several methods for finding the indefinite integral. One of the important methods for finding the indefinite integral is the method of substitution.

To evaluate $\int_{a}^{b} f(x) d x$, by substitution, the steps could be as follows:

1. Consider the integral without limits and substitute, $y=f(x)$ or $x=g(y)$ to reduce the given integral to a known form.
2. Integrate the new integrand with respect to the new variable without mentioning the constant of integration.
3. Resubstitute for the new variable and write the answer in terms of the original variable.
4. Find the values of answers obtained in (3) at the given limits of integral and find the difference of the values at the upper and lower limits.

## Note In order to quicken this method, we can proceed as follows: After performing steps 1, and 2, there is no need of step 3. Here, the integral will be kept in the new variable itself, and the limits of the integral will accordingly be changed, so that we can perform the last step.

Let us illustrate this by examples.
Example 26 Evaluate $\int_{-1}^{1} 5 x^{4} \sqrt{x^{5}+1} d x$.

Solution Put $t=x^{5}+1$, then $d t=5 x^{4} d x$.

Therefore,

$$
\int 5 x^{4} \sqrt{x^{5}+1} d x=\int \sqrt{t} d t=\frac{2}{3} t^{\frac{3}{2}}=\frac{2}{3}\left(x^{5}+1\right)^{\frac{3}{2}}
$$

Hence,

$$
\begin{aligned}
\int_{-1}^{1} 5 x^{4} \sqrt{x^{5}+1} d x & =\frac{2}{3}\left[\left(x^{5}+1\right)^{\frac{3}{2}}\right]_{-1}^{1} \\
& =\frac{2}{3}\left[\left(1^{5}+1\right)^{\frac{3}{2}}-\left((-1)^{5}+1\right)^{\frac{3}{2}}\right] \\
& =\frac{2}{3}\left[2^{\frac{3}{2}}-0^{\frac{3}{2}}\right]=\frac{2}{3}(2 \sqrt{2})=\frac{4 \sqrt{2}}{3}
\end{aligned}
$$

Alternatively, first we transform the integral and then evaluate the transformed integral with new limits.
Let

$$
\begin{aligned}
& t=x^{5}+1 \text {. Then } d t=5 x^{4} d x \\
& x=-1, t=0 \text { and when } x=1, t=2
\end{aligned}
$$

Note that, when
ies from 0 to 2
Thus, as $x$ varies from -1 to $1, t$ varies from 0 to 2
Therefore

$$
\begin{aligned}
\int_{-1}^{1} 5 x^{4} \sqrt{x^{5}+1} d x & =\int_{0}^{2} \sqrt{t} d t \\
& =\frac{2}{3}\left[t^{\frac{3}{2}}\right]_{0}^{2}=\frac{2}{3}\left[2^{\frac{3}{2}}-0^{\frac{3}{2}}\right]=\frac{2}{3}(2 \sqrt{2})=\frac{4 \sqrt{2}}{3}
\end{aligned}
$$

Example 27 Evaluate $\int_{0}^{1} \frac{\tan ^{-1} x}{1+x^{2}} d x$

Solution Let $t=\tan ^{-1} x$, then $d t=\frac{1}{1+x^{2}} d x$. The new limits are, when $x=0, t=0$ and when $x=1, t=\frac{\pi}{4}$. Thus, as $x$ varies from 0 to $1, t$ varies from 0 to $\frac{\pi}{4}$.

Therefore

$$
\int_{0}^{1} \frac{\tan ^{-1} x}{1+x^{2}} d x=\int_{0}^{\frac{\pi}{4}} t d t\left[\frac{t^{2}}{2}\right]_{0}^{\frac{\pi}{4}}=\frac{1}{2}\left[\frac{\pi^{2}}{16}-0\right]=\frac{\pi^{2}}{32}
$$

## EXERCISE 7.9

Evaluate the integrals in Exercises 1 to 8 using substitution.

1. $\int_{0}^{1} \frac{x}{x^{2}+1} d x$
2. $\int_{0}^{\frac{\pi}{2}} \sqrt{\sin \phi} \cos ^{5} \phi d \phi$
3. $\int_{0}^{1} \sin ^{-1}\left(\frac{2 x}{1+x^{2}}\right) d x$
4. $\int_{0}^{2} x \sqrt{x+2}$ (Put $x+2=t^{2}$ )
5. $\int_{0}^{\frac{\pi}{2}} \frac{\sin x}{1+\cos ^{2} x} d x$
6. $\int_{0}^{2} \frac{d x}{x+4-x^{2}}$
7. $\int_{-1}^{1} \frac{d x}{x^{2}+2 x+5}$
8. $\int_{1}^{2}\left(\frac{1}{x}-\frac{1}{2 x^{2}}\right) e^{2 x} d x$

Choose the correct answer in Exercises 9 and 10.
9. The value of the integral $\int_{\frac{1}{3}}^{1} \frac{\left(x-x^{3}\right)^{\frac{1}{3}}}{x^{4}} d x$ is
(A) 6
(B) 0
(C) 3
(D) 4
10. If $f(x)=\int_{0}^{x} t \sin t d t$, then $f^{\prime}(x)$ is
(A) $\cos x+x \sin x$
(B) $x \sin x$
(C) $x \cos x$
(D) $\sin x+x \cos x$

### 7.10 Some Properties of Definite Integrals

We list below some important properties of definite integrals. These will be useful in evaluating the definite integrals more easily.

$$
\begin{array}{ll}
\mathbf{P}_{0}: & \int_{a}^{b} f(x) d x=\int_{a}^{b} f(t) d t \\
\mathbf{P}_{1}: & \int_{a}^{b} f(x) d x=-\int_{b}^{a} f(x) d x . \text { In particular, } \int_{a}^{a} f(x) d x=0 \\
\mathbf{P}_{2}: & \int_{a}^{b} f(x) d x=\int_{a}^{c} f(x) d x+\int_{c}^{b} f(x) d x
\end{array}
$$

$$
\begin{array}{ll}
\mathbf{P}_{3}: & \int_{a}^{b} f(x) d x=\int_{a}^{b} f(a+b-x) d x \\
\mathbf{P}_{4}: & \int_{0}^{a} f(x) d x=\int_{0}^{a} f(a-x) d x
\end{array}
$$

(Note that $\mathrm{P}_{4}$ is a particular case of $\mathrm{P}_{3}$ )
$\mathbf{P}_{5}: \quad \int_{0}^{2 a} f(x) d x=\int_{0}^{a} f(x) d x+\int_{0}^{a} f(2 a-x) d x$
$\mathbf{P}_{\mathbf{6}}: \quad \int_{0}^{2 a} f(x) d x=2 \int_{0}^{a} f(x) d x$, if $f(2 a-x)=f(x)$ and

$$
0 \text { if } f(2 a-x)=-f(x)
$$

$\mathbf{P}_{7}: \quad$ (i) $\int_{-a}^{a} f(x) d x=2 \int_{0}^{a} f(x) d x$, if $f$ is an even function, i.e., if $f(-x)=f(x)$.
(ii) $\int_{-a}^{a} f(x) d x=0$, if $f$ is an odd function, i.e., if $f(-x)=-f(x)$.

We give the proofs of these properties one by one.
Proof of $\mathbf{P}_{\mathbf{0}}$ It follows directly by making the substitution $x=t$.
Proof of $\mathbf{P}_{\mathbf{1}}$ Let F be anti derivative of $f$. Then, by the second fundamental theorem of calculus, we have $\int_{a}^{b} f(x) d x=\mathrm{F}(b)-\mathrm{F}(a)=-[\mathrm{F}(a)-\mathrm{F}(b)]=-\int_{b}^{a} f(x) d x$ Here, we observe that, if $a=b$, then $\int_{a}^{a} f(x) d x=0$.

Proof of $\mathbf{P}_{\mathbf{2}}$ Let F be anti derivative of $f$. Then

$$
\begin{align*}
& \int_{a}^{b} f(x) d x=\mathrm{F}(b)-\mathrm{F}(a)  \tag{1}\\
& \int_{a}^{c} f(x) d x=\mathrm{F}(c)-\mathrm{F}(a)  \tag{2}\\
& \int_{c}^{b} f(x) d x=\mathrm{F}(b)-\mathrm{F}(c) \tag{3}
\end{align*}
$$

and
Adding (2) and (3), we get $\int_{a}^{c} f(x) d x+\int_{c}^{b} f(x) d x=\mathrm{F}(b)-\mathrm{F}(a)=\int_{a}^{b} f(x) d x$
This proves the property $\mathrm{P}_{2}$.
Proof of $\mathbf{P}_{3}$ Let $t=a+b-x$. Then $d t=-d x$. When $x=a, t=b$ and when $x=b, t=a$. Therefore

$$
\int_{a}^{b} f(x) d x=-\int_{b}^{a} f(a+b-t) d t
$$

$$
\begin{aligned}
& =\int_{a}^{b} f(a+b-t) d t\left(\text { by } \mathrm{P}_{1}\right) \\
& =\int_{a}^{b} f(a+b-x) d x \text { by } \mathrm{P}_{0}
\end{aligned}
$$

Proof of $\mathbf{P}_{4}$ Put $t=a-x$. Then $d t=-d x$. When $x=0, t=a$ and when $x=a, t=0$. Now proceed as in $\mathrm{P}_{3}$.
Proof of $\mathbf{P}_{\mathbf{5}}$ Using $\mathrm{P}_{2}$, we have $\int_{0}^{2 a} f(x) d x=\int_{0}^{a} f(x) d x+\int_{a}^{2 a} f(x) d x$.
Let

$$
\begin{aligned}
t & =2 a-x \text { in the second integral on the right hand side. Then } \\
d t & =-d x \text {. When } x=a, t=a \text { and when } x=2 a, t=0 \text {. Also } x=2 a-t \text {. }
\end{aligned}
$$

Therefore, the second integral becomes

$$
\int_{a}^{2 a} f(x) d x=-\int_{a}^{0} f(2 a-t) d t=\int_{0}^{a} f(2 a-t) d t=\int_{0}^{a} f(2 a-x) d x
$$

Hence $\quad \int_{0}^{2 a} f(x) d x=\int_{0}^{a} f(x) d x+\int_{0}^{a} f(2 a-x) d x$
Proof of $\mathbf{P}_{\mathbf{6}}$ Using $\mathrm{P}_{5}$, we have $\int_{0}^{2 a} f(x) d x=\int_{0}^{a} f(x) d x+\int_{0}^{a} f(2 a-x) d x$
Now, if $f(2 a-x)=f(x)$, then (1) becomes

$$
\int_{0}^{2 a} f(x) d x=\int_{0}^{a} f(x) d x+\int_{0}^{a} f(x) d x=2 \int_{0}^{a} f(x) d x
$$

and if $f(2 a-x)=-f(x)$, then $(1)$ becomes

$$
\int_{0}^{2 a} f(x) d x=\int_{0}^{a} f(x) d x-\int_{0}^{a} f(x) d x=0
$$

Proof of $\mathbf{P}_{7}$ Using $\mathrm{P}_{2}$, we have

$$
\int_{-a}^{a} f(x) d x=\int_{-a}^{0} f(x) d x+\int_{0}^{a} f(x) d x \text {. Then }
$$

Let

$$
\begin{aligned}
t & =-x \text { in the first integral on the right hand side. } \\
d t & =-d x \text {. When } x=-a, t=a \text { and when } \\
x & =0, t=0 \text {. Also } x=-t
\end{aligned}
$$

Therefore

$$
\begin{align*}
\int_{-a}^{a} f(x) d x & =-\int_{a}^{0} f(-t) d t+\int_{0}^{a} f(x) d x \\
& =\int_{0}^{a} f(-x) d x+\int_{0}^{a} f(x) d x \quad\left(\text { by } \mathrm{P}_{0}\right) \tag{1}
\end{align*}
$$

(i) Now, if $f$ is an even function, then $f(-x)=f(x)$ and so (1) becomes

$$
\int_{-a}^{a} f(x) d x=\int_{0}^{a} f(x) d x+\int_{0}^{a} f(x) d x=2 \int_{0}^{a} f(x) d x
$$

(ii) If $f$ is an odd function, then $f(-x)=-f(x)$ and so (1) becomes

$$
\int_{-a}^{a} f(x) d x=-\int_{0}^{a} f(x) d x+\int_{0}^{a} f(x) d x=0
$$

Example 28 Evaluate $\int_{-1}^{2}\left|x^{3}-x\right| d x$

Solution We note that $x^{3}-x \geq 0$ on $[-1,0]$ and $x^{3}-x \leq 0$ on $[0,1]$ and that $x^{3}-x \geq 0$ on [1,2]. So by $\mathrm{P}_{2}$ we write

$$
\begin{aligned}
\int_{-1}^{2}\left|x^{3}-x\right| d x & =\int_{-1}^{0}\left(x^{3}-x\right) d x+\int_{0}^{1}-\left(x^{3}-x\right) d x+\int_{1}^{2}\left(x^{3}-x\right) d x \\
& =\int_{-1}^{0}\left(x^{3}-x\right) d x+\int_{0}^{1}\left(x-x^{3}\right) d x+\int_{1}^{2}\left(x^{3}-x\right) d x \\
& =\left[\frac{x^{4}}{4}-\frac{x^{2}}{2}\right]_{-1}^{0}+\left[\frac{x^{2}}{2}-\frac{x^{4}}{4}\right]_{0}^{1}+\left[\frac{x^{4}}{4}-\frac{x^{2}}{2}\right]_{1}^{2} \\
& =-\left(\frac{1}{4}-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{4}\right)+(4-2)-\left(\frac{1}{4}-\frac{1}{2}\right) \\
& =-\frac{1}{4}+\frac{1}{2}+\frac{1}{2}-\frac{1}{4}+2-\frac{1}{4}+\frac{1}{2}=\frac{3}{2}-\frac{3}{4}+2=\frac{11}{4}
\end{aligned}
$$

Example 29 Evaluate $\int_{\frac{-\pi}{4}}^{\frac{\pi}{4}} \sin ^{2} x d x$
Solution We observe that $\sin ^{2} x$ is an even function. Therefore, by $\mathrm{P}_{7}(\mathrm{i})$, we get

$$
\begin{aligned}
\int_{\frac{-\pi}{4}}^{\frac{\pi}{4}} \sin ^{2} x d x & =2 \int_{0}^{\frac{\pi}{4}} \sin ^{2} x d x \\
& =2 \int_{0}^{\frac{\pi}{4}} \frac{(1-\cos 2 x)}{2} d x=\int_{0}^{\frac{\pi}{4}}(1-\cos 2 x) d x
\end{aligned}
$$

$$
=\left[x-\frac{1}{2} \sin 2 x\right]_{0}^{\frac{\pi}{4}}=\left(\frac{\pi}{4}-\frac{1}{2} \sin \frac{\pi}{2}\right)-0=\frac{\pi}{4}-\frac{1}{2}
$$

Example 30 Evaluate $\int_{0}^{\pi} \frac{x \sin x}{1+\cos ^{2} x} d x$
Solution Let $\mathrm{I}=\int_{0}^{\pi} \frac{x \sin x}{1+\cos ^{2} x} d x$. Then, by $\mathrm{P}_{4}$, we have
or

$$
\begin{aligned}
\mathrm{I} & =\int_{0}^{\pi} \frac{(\pi-x) \sin (\pi-x) d x}{1+\cos ^{2}(\pi-x)} \\
& =\int_{0}^{\pi} \frac{(\pi-x) \sin x d x}{1+\cos ^{2} x}=\pi \int_{0}^{\pi} \frac{\sin x d x}{1+\cos ^{2} x}-\mathrm{I} \\
2 \mathrm{I} & =\pi \int_{0}^{\pi} \frac{\sin x d x}{1+\cos ^{2} x} \\
\mathrm{I} & =\frac{\pi}{2} \int_{0}^{\pi} \frac{\sin x d x}{1+\cos ^{2} x}
\end{aligned}
$$

or

Put $\cos x=t$ so that $-\sin x d x=d t$. When $x=0, t=1$ and when $x=\pi, t=-1$. Therefore, (by $\mathrm{P}_{1}$ ) we get

$$
\begin{aligned}
\mathrm{I} & =\frac{-\pi}{2} \int_{1}^{-1} \frac{d t}{1+t^{2}}=\frac{\pi}{2} \int_{-1}^{1} \frac{d t}{1+t^{2}} \\
& =\pi \int_{0}^{1} \frac{d t}{1+t^{2}}\left(\text { by } \mathrm{P}_{7}, \text { since } \frac{1}{1+t^{2}} \text { is even function }\right) \\
& =\pi\left[\tan ^{-1} t\right]_{0}^{1}=\pi\left[\tan ^{-1} 1-\tan ^{-1} 0\right]=\pi\left[\frac{\pi}{4}-0\right]=\frac{\pi^{2}}{4}
\end{aligned}
$$

Example 31 Evaluate $\int_{-1}^{1} \sin ^{5} x \cos ^{4} x d x$
Solution Let $\mathrm{I}=\int_{-1}^{1} \sin ^{5} x \cos ^{4} x d x$. Let $f(x)=\sin ^{5} x \cos ^{4} x$. Then
$f(-x)=\sin ^{5}(-x) \cos ^{4}(-x)=-\sin ^{5} x \cos ^{4} x=-f(x)$, i.e., $f$ is an odd function.
Therefore, by $\mathrm{P}_{7}$ (ii), $\mathrm{I}=0$

Example 32 Evaluate $\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{4} x}{\sin ^{4} x+\cos ^{4} x} d x$
Solution Let $\mathrm{I}=\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{4} x}{\sin ^{4} x+\cos ^{4} x} d x$
Then, by $\mathrm{P}_{4}$

$$
\begin{equation*}
I=\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{4}\left(\frac{\pi}{2}-x\right)}{\sin ^{4}\left(\frac{\pi}{2}-x\right)+\cos ^{4}\left(\frac{\pi}{2}-x\right)} d x=\int_{0}^{\frac{\pi}{2}} \frac{\cos ^{4} x}{\cos ^{4} x+\sin ^{4} x} d x \tag{2}
\end{equation*}
$$

Adding (1) and (2), we get

$$
2 I=\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{4} x+\cos ^{4} x}{\sin ^{4} x+\cos ^{4} x} d x=\int_{0}^{\frac{\pi}{2}} d x=[x]_{0}^{\frac{\pi}{2}}=\frac{\pi}{2}
$$

Hence

$$
I=\frac{\pi}{4}
$$

Example 33 Evaluate $\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{d x}{1+\sqrt{\tan x}}$
Solution Let $\mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{d x}{1+\sqrt{\tan x}}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sqrt{\cos x} d x}{\sqrt{\cos x}+\sqrt{\sin x}}$
Then, by $\mathrm{P}_{3} \quad \mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sqrt{\cos \left(\frac{\pi}{3}+\frac{\pi}{6}-x\right)} d x}{\sqrt{\cos \left(\frac{\pi}{3}+\frac{\pi}{6}-x\right)}+\sqrt{\sin \left(\frac{\pi}{3}+\frac{\pi}{6}-x\right)}}$

$$
\begin{equation*}
=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}} d x \tag{2}
\end{equation*}
$$

Adding (1) and (2), we get

$$
2 \mathrm{I}=\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} d x=[x]_{\frac{\pi}{6}}^{\frac{\pi}{3}}=\frac{\pi}{3}-\frac{\pi}{6}=\frac{\pi}{6} . \text { Hence } \mathrm{I}=\frac{\pi}{12}
$$

Example 34 Evaluate $\int_{0}^{\frac{\pi}{2}} \log \sin x d x$
Solution Let $\mathrm{I}=\int_{0}^{\frac{\pi}{2}} \log \sin x d x$
Then, by $\mathrm{P}_{4}$

$$
\mathrm{I}=\int_{0}^{\frac{\pi}{2}} \log \sin \left(\frac{\pi}{2}-x\right) d x=\int_{0}^{\frac{\pi}{2}} \log \cos x d x
$$

Adding the two values of I, we get

$$
\begin{aligned}
2 \mathrm{I} & =\int_{0}^{\frac{\pi}{2}}(\log \sin x+\log \cos x) d x \\
& =\int_{0}^{\frac{\pi}{2}}(\log \sin x \cos x+\log 2-\log 2) d x \text { (by adding and subtracting } \log 2 \text { ) } \\
& =\int_{0}^{\frac{\pi}{2}} \log \sin 2 x d x-\int_{0}^{\frac{\pi}{2}} \log 2 d x \quad \text { (Why?) }
\end{aligned}
$$

Put $2 x=t$ in the first integral. Then $2 d x=d t$, when $x=0, t=0$ and when $x=\frac{\pi}{2}$, $t=\pi$.

Therefore

$$
\begin{aligned}
2 \mathrm{I} & =\frac{1}{2} \int_{0}^{\pi} \log \sin t d t-\frac{\pi}{2} \log 2 \\
& \left.=\frac{2}{2} \int_{0}^{\frac{\pi}{2}} \log \sin t d t-\frac{\pi}{2} \log 2 \text { [by } \mathrm{P}_{6} \text { as } \sin (\pi-t)=\sin t\right) \\
& =\int_{0}^{\frac{\pi}{2}} \log \sin x d x-\frac{\pi}{2} \log 2(\text { by changing variable } t \text { to } x) \\
& =\mathrm{I}-\frac{\pi}{2} \log 2
\end{aligned}
$$

Hence

$$
\int_{0}^{\frac{\pi}{2}} \log \sin x d x=\frac{-\pi}{2} \log 2
$$

## EXERCISE 7.10

By using the properties of definite integrals, evaluate the integrals in Exercises 1 to 19.

1. $\int_{0}^{\frac{\pi}{2}} \cos ^{2} x d x$
2. $\int_{0}^{\frac{\pi}{2}} \frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}} d x$
3. $\int_{0}^{\frac{\pi}{2}} \frac{\sin ^{\frac{3}{2}} x d x}{\sin ^{\frac{3}{2}} x+\cos ^{\frac{3}{2}} x}$
4. $\int_{0}^{\frac{\pi}{2}} \frac{\cos ^{5} x d x}{\sin ^{5} x+\cos ^{5} x}$
5. $\int_{-5}^{5}|x+2| d x$
6. $\int_{2}^{8}|x-5| d x$
7. $\int_{0}^{1} x(1-x)^{n} d x$
8. $\int_{0}^{\frac{\pi}{4}} \log (1+\tan x) d x$
9. $\int_{0}^{2} x \sqrt{2-x} d x$
10. $\int_{0}^{\frac{\pi}{2}}(2 \log \sin x-\log \sin 2 x) d x$
11. $\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} \sin ^{2} x d x$
12. $\int_{0}^{\pi} \frac{x d x}{1+\sin x}$
13. $\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}} \sin ^{7} x d x$
14. $\int_{0}^{2 \pi} \cos ^{5} x d x$
15. $\int_{0}^{\frac{\pi}{2}} \frac{\sin x-\cos x}{1+\sin x \cos x} d x$
16. $\int_{0}^{\pi} \log (1+\cos x) d x$
17. $\int_{0}^{a} \frac{\sqrt{x}}{\sqrt{x}+\sqrt{a-x}} d x$
18. $\int_{0}^{4}|x-1| d x$
19. Show that $\int_{0}^{a} f(x) g(x) d x=2 \int_{0}^{a} f(x) d x$, if $f$ and $g$ are defined as $f(x)=f(a-x)$ and $g(x)+g(a-x)=4$

Choose the correct answer in Exercises 20 and 21.
20. The value of $\int_{\frac{-\pi}{2}}^{\frac{\pi}{2}}\left(x^{3}+x \cos x+\tan ^{5} x+1\right) d x$ is
(A) 0
(B) 2
(C) $\pi$
(D) 1
21. The value of $\int_{0}^{\frac{\pi}{2}} \log \left(\frac{4+3 \sin x}{4+3 \cos x}\right) d x$ is
(A) 2
(B) $\frac{3}{4}$
(C) 0
(D) -2

## Miscellaneous Examples

Example 35 Find $\int \cos 6 x \sqrt{1+\sin 6 x} d x$
Solution Put $t=1+\sin 6 x$, so that $d t=6 \cos 6 x d x$

Therefore

$$
\begin{aligned}
\int \cos 6 x \sqrt{1+\sin 6 x} d x & =\frac{1}{6} \int t^{\frac{1}{2}} d t \\
& =\frac{1}{6} \times \frac{2}{3}(t)^{\frac{3}{2}}+\mathrm{C}=\frac{1}{9}(1+\sin 6 x)^{\frac{3}{2}}+\mathrm{C}
\end{aligned}
$$

Example 36 Find $\int \frac{\left(x^{4}-x\right)^{\frac{1}{4}}}{x^{5}} d x$
Solution We have $\int \frac{\left(x^{4}-x\right)^{\frac{1}{4}}}{x^{5}} d x=\int \frac{\left(1-\frac{1}{x^{3}}\right)^{\frac{1}{4}}}{x^{4}} d x$
Put $1-\frac{1}{x^{3}}=1-x^{-3}=t$, so that $\frac{3}{x^{4}} d x=d t$
Therefore $\int \frac{\left(x^{4}-x\right)^{\frac{1}{4}}}{x^{5}} d x=\frac{1}{3} \int t^{\frac{1}{4}} d t=\frac{1}{3} \times \frac{4}{5} t^{\frac{5}{4}}+\mathrm{C}=\frac{4}{15}\left(1-\frac{1}{x^{3}}\right)^{\frac{5}{4}}+\mathrm{C}$

Example 37 Find $\int \frac{x^{4} d x}{(x-1)\left(x^{2}+1\right)}$
Solution We have

$$
\begin{align*}
\frac{x^{4}}{(x-1)\left(x^{2}+1\right)} & =(x+1)+\frac{1}{x^{3}-x^{2}+x-1} \\
& =(x+1)+\frac{1}{(x-1)\left(x^{2}+1\right)}  \tag{1}\\
\frac{1}{(x-1)\left(x^{2}+1\right)} & =\frac{\mathrm{A}}{(x-1)}+\frac{\mathrm{B} x+\mathrm{C}}{\left(x^{2}+1\right)} \tag{2}
\end{align*}
$$

Now express

So

$$
\begin{aligned}
1 & =\mathrm{A}\left(x^{2}+1\right)+(\mathrm{B} x+\mathrm{C})(x-1) \\
& =(\mathrm{A}+\mathrm{B}) x^{2}+(\mathrm{C}-\mathrm{B}) x+\mathrm{A}-\mathrm{C}
\end{aligned}
$$

Equating coefficients on both sides, we get $\mathrm{A}+\mathrm{B}=0, \mathrm{C}-\mathrm{B}=0$ and $\mathrm{A}-\mathrm{C}=1$, which give $\mathrm{A}=\frac{1}{2}, \mathrm{~B}=\mathrm{C}=-\frac{1}{2}$. Substituting values of $\mathrm{A}, \mathrm{B}$ and C in (2), we get

$$
\begin{equation*}
\frac{1}{(x-1)\left(x^{2}+1\right)}=\frac{1}{2(x-1)}-\frac{1}{2} \frac{x}{\left(x^{2}+1\right)}-\frac{1}{2\left(x^{2}+1\right)} \tag{3}
\end{equation*}
$$

Again, substituting (3) in (1), we have

$$
\frac{x^{4}}{(x-1)\left(x^{2}+x+1\right)}=(x+1)+\frac{1}{2(x-1)}-\frac{1}{2} \frac{x}{\left(x^{2}+1\right)}-\frac{1}{2\left(x^{2}+1\right)}
$$

Therefore

$$
\int \frac{x^{4}}{(x-1)\left(x^{2}+x+1\right)} d x=\frac{x^{2}}{2}+x+\frac{1}{2} \log |x-1|-\frac{1}{4} \log \left(x^{2}+1\right)-\frac{1}{2} \tan ^{-1} x+\mathrm{C}
$$

Example 38 Find $\int\left[\log (\log x)+\frac{1}{(\log x)^{2}}\right] d x$
Solution Let $\mathrm{I}=\int\left[\log (\log x)+\frac{1}{(\log x)^{2}}\right] d x$

$$
=\int \log (\log x) d x+\int \frac{1}{(\log x)^{2}} d x
$$

In the first integral, let us take 1 as the second function. Then integrating it by parts, we get

$$
\begin{align*}
\mathrm{I} & =x \log (\log x)-\int \frac{1}{x \log x} x d x+\int \frac{d x}{(\log x)^{2}} \\
& =x \log (\log x)-\int \frac{d x}{\log x}+\int \frac{d x}{(\log x)^{2}} \tag{1}
\end{align*}
$$

Again, consider $\int \frac{d x}{\log x}$, take 1 as the second function and integrate it by parts, we have $\int \frac{d x}{\log x}=\left[\frac{x}{\log x}-\int x\left\{-\frac{1}{(\log x)^{2}}\left(\frac{1}{x}\right)\right\} d x\right]$

Putting (2) in (1), we get

$$
\mathrm{I}=x \log (\log x)-\frac{x}{\log x}-\int \frac{d x}{(\log x)^{2}}+\int \frac{d x}{(\log x)^{2}}=x \log (\log x)-\frac{x}{\log x}+\mathrm{C}
$$

Example 39 Find $\int[\sqrt{\cot x}+\sqrt{\tan x}] d x$
Solution We have

$$
\mathrm{I}=\int[\sqrt{\cot x}+\sqrt{\tan x}] d x=\int \sqrt{\tan x}(1+\cot x) d x
$$

Put $\tan x=t^{2}$, so that $\sec ^{2} x d x=2 t d t$
or

$$
d x=\frac{2 t d t}{1+t^{4}}
$$

Then

$$
\begin{aligned}
\mathrm{I} & =\int t\left(1+\frac{1}{t^{2}}\right) \frac{2 t}{\left(1+t^{4}\right)} d t \\
& =2 \int \frac{\left(t^{2}+1\right)}{t^{4}+1} d t=2 \int \frac{\left(1+\frac{1}{t^{2}}\right) d t}{\left(t^{2}+\frac{1}{t^{2}}\right)}=2 \int \frac{\left(1+\frac{1}{t^{2}}\right) d t}{\left(t-\frac{1}{t}\right)^{2}+2}
\end{aligned}
$$

Put $t-\frac{1}{t}=y$, so that $\left(1+\frac{1}{t^{2}}\right) d t=d y$. Then

$$
\begin{aligned}
\mathrm{I} & =2 \int \frac{d y}{y^{2}+(\sqrt{2})^{2}}=\sqrt{2} \tan ^{-1} \frac{y}{\sqrt{2}}+\mathrm{C}=\sqrt{2} \tan ^{-1} \frac{\left(t-\frac{1}{t}\right)}{\sqrt{2}}+\mathrm{C} \\
& =\sqrt{2} \tan ^{-1}\left(\frac{t^{2}-1}{\sqrt{2} t}\right)+\mathrm{C}=\sqrt{2} \tan ^{-1}\left(\frac{\tan x-1}{\sqrt{2 \tan x}}\right)+\mathrm{C}
\end{aligned}
$$

Example 40 Find $\int \frac{\sin 2 x \cos 2 x d x}{\sqrt{9-\cos ^{4}(2 x)}}$
Solution Let $I=\int \frac{\sin 2 x \cos 2 x}{\sqrt{9-\cos ^{4} 2 x}} d x$

Put $\cos ^{2}(2 x)=t$ so that $4 \sin 2 x \cos 2 x d x=-d t$

Therefore

$$
\mathrm{I}=-\frac{1}{4} \int \frac{d t}{\sqrt{9-t^{2}}}=-\frac{1}{4} \sin ^{-1}\left(\frac{t}{3}\right)+\mathrm{C}=-\frac{1}{4} \sin ^{-1}\left[\frac{1}{3} \cos ^{2} 2 x\right]+\mathrm{C}
$$

Example 41 Evaluate $\int_{-1}^{\frac{3}{2}}|x \sin (\pi x)| d x$
Solution Here $f(x)=|x \sin \pi x|=\left\{\begin{array}{l}x \sin \pi x \text { for }-1 \leq x \leq 1 \\ -x \sin \pi x \text { for } 1 \leq x \leq \frac{3}{2}\end{array}\right.$

Therefore

$$
\begin{aligned}
\int_{-1}^{\frac{3}{2}}|x \sin \pi x| d x & =\int_{-1}^{1} x \sin \pi x d x+\int_{1}^{\frac{3}{2}}-x \sin \pi x d x \\
& =\int_{-1}^{1} x \sin \pi x d x-\int_{1}^{\frac{3}{2}} x \sin \pi x d x
\end{aligned}
$$

Integrating both integrals on righthand side, we get

$$
\begin{aligned}
\int_{-1}^{\frac{3}{2}}|x \sin \pi x| d x & =\left[\frac{-x \cos \pi x}{\pi}+\frac{\sin \pi x}{\pi^{2}}\right]_{-1}^{1}-\left[\frac{-x \cos \pi x}{\pi}+\frac{\sin \pi x}{\pi^{2}}\right]_{1}^{\frac{3}{2}} \\
& =\frac{2}{\pi}-\left[-\frac{1}{\pi^{2}}-\frac{1}{\pi}\right]=\frac{3}{\pi}+\frac{1}{\pi^{2}}
\end{aligned}
$$

Example 42 Evaluate $\int_{0}^{\pi} \frac{x d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}$
Solution Let $\mathrm{I}=\int_{0}^{\pi} \frac{x d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}=\int_{0}^{\pi} \frac{(\pi-x) d x}{a^{2} \cos ^{2}(\pi-x)+b^{2} \sin ^{2}(\pi-x)}$ (using $\mathrm{P}_{4}$ )

$$
\begin{aligned}
& =\pi \int_{0}^{\pi} \frac{d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}-\int_{0}^{\pi} \frac{x d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x} \\
& =\pi \int_{0}^{\pi} \frac{d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}-\mathrm{I}
\end{aligned}
$$

Thus

$$
2 \mathrm{I}=\pi \int_{0}^{\pi} \frac{d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}
$$

or

$$
\begin{aligned}
\mathrm{I} & =\frac{\pi}{2} \int_{0}^{\pi} \frac{d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}=\frac{\pi}{2} \cdot 2 \int_{0}^{\frac{\pi}{2}} \frac{d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}\left(\text { using } \mathrm{P}_{6}\right) \\
& =\pi\left[\int_{0}^{\frac{\pi}{4}} \frac{d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}} \frac{d x}{a^{2} \cos ^{2} x+b^{2} \sin ^{2} x}\right] \\
& =\pi\left[\int_{0}^{\frac{\pi}{4}} \frac{\sec ^{2} x d x}{a^{2}+b^{2} \tan ^{2} x}+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}} \frac{\operatorname{cosec}^{2} x d x}{a^{2} \cot ^{2} x+b^{2}}\right] \\
& =\pi\left[\int_{0}^{1} \frac{d t}{a^{2}+b^{2} t^{2}}-\int_{1}^{0} \frac{d u}{a^{2} u^{2}+b^{2}}\right](p u t \tan x=\operatorname{tand} \cot x=u) \\
& =\frac{\pi}{a b}\left[\tan ^{-1} \frac{b t}{a}\right]_{0}^{1}-\frac{\pi}{a b}\left[\tan ^{-1} \frac{a u}{b}\right]_{1}^{0}=\frac{\pi}{a b}\left[\tan ^{-1} \frac{b}{a}+\tan ^{-1} \frac{a}{b}\right]=\frac{\pi^{2}}{2 a b}
\end{aligned}
$$

## Miscellaneous Exercise on Chapter 7

Integrate the functions in Exercises 1 to 23.

1. $\frac{1}{x-x^{3}}$
2. $\frac{1}{\sqrt{x+a}+\sqrt{x+b}}$
3. $\frac{1}{x \sqrt{a x-x^{2}}}\left[\right.$ Hint:Put $\left.x=\frac{a}{t}\right]$
4. $\frac{1}{x^{2}\left(x^{4}+1\right)^{\frac{3}{4}}}$
5. $\frac{1}{x^{\frac{1}{2}}+x^{\frac{1}{3}}}$
$\left[\right.$ Hint: $\frac{1}{x^{\frac{1}{2}}+x^{\frac{1}{3}}}=\frac{1}{x^{\frac{1}{3}}\left(1+x^{\frac{1}{6}}\right)}$, put $\left.x=t^{6}\right]$
6. $\frac{5 x}{(x+1)\left(x^{2}+9\right)}$
7. $\frac{\sin x}{\sin (x-a)}$
8. $\frac{e^{5 \log x}-e^{4 \log x}}{e^{3 \log x}-e^{2 \log x}}$
9. $\frac{\cos x}{\sqrt{4-\sin ^{2} x}}$
10. $\frac{\sin ^{8}-\cos ^{8} x}{1-2 \sin ^{2} x \cos ^{2} x}$
11. $\frac{1}{\cos (x+a) \cos (x+b)}$
12. $\frac{x^{3}}{\sqrt{1-x^{8}}}$
13. $\frac{e^{x}}{\left(1+e^{x}\right)\left(2+e^{x}\right)}$
14. $\frac{1}{\left(x^{2}+1\right)\left(x^{2}+4\right)}$
15. $\cos ^{3} x e^{\log \sin x}$
16. $e^{3 \log x}\left(x^{4}+1\right)^{-1}$
17. $f^{\prime}(a x+b)[f(a x+b)]^{n}$
18. $\frac{1}{\sqrt{\sin ^{3} x \sin (x+\alpha)}}$
19. $\sqrt{\frac{1-\sqrt{x}}{1+\sqrt{x}}}$
20. $\frac{2+\sin 2 x}{1+\cos 2 x} e^{x}$
21. $\frac{x^{2}+x+1}{(x+1)^{2}(x+2)}$
22. $\tan ^{-1} \sqrt{\frac{1-x}{1+x}}$
23. $\frac{\sqrt{x^{2}+1}\left[\log \left(x^{2}+1\right)-2 \log x\right]}{x^{4}}$

Evaluate the definite integrals in Exercises 24 to 31.
24. $\int_{\frac{\pi}{2}}^{\pi} e^{x}\left(\frac{1-\sin x}{1-\cos x}\right) d x$
25. $\int_{0}^{\frac{\pi}{4}} \frac{\sin x \cos x}{\cos ^{4} x+\sin ^{4} x} d x$
26. $\int_{0}^{\frac{\pi}{2}} \frac{\cos ^{2} x d x}{\cos ^{2} x+4 \sin ^{2} x}$
27. $\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sin x+\cos x}{\sqrt{\sin 2 x}} d x$
28. $\int_{0}^{1} \frac{d x}{\sqrt{1+x}-\sqrt{x}}$
29. $\int_{0}^{\frac{\pi}{4}} \frac{\sin x+\cos x}{9+16 \sin 2 x} d x$
30. $\int_{0}^{\frac{\pi}{2}} \sin 2 x \tan ^{-1}(\sin x) d x$
31. $\int_{1}^{4}[|x-1|+|x-2|+|x-3|] d x$

Prove the following (Exercises 32 to 37)
32. $\int_{1}^{3} \frac{d x}{x^{2}(x+1)}=\frac{2}{3}+\log \frac{2}{3}$
33. $\int_{0}^{1} x e^{x} d x=1$
34. $\int_{-1}^{1} x^{17} \cos ^{4} x d x=0$
35. $\int_{0}^{\frac{\pi}{2}} \sin ^{3} x d x=\frac{2}{3}$
36. $\int_{0}^{\frac{\pi}{4}} 2 \tan ^{3} x d x=1-\log 2$
37. $\int_{0}^{1} \sin ^{-1} x d x=\frac{\pi}{2}-1$

Choose the correct answers in Exercises 38 to 40
38. $\int \frac{d x}{e^{x}+e^{-x}}$ is equal to
(A) $\tan ^{-1}\left(e^{x}\right)+\mathrm{C}$
(B) $\tan ^{-1}\left(e^{-x}\right)+\mathrm{C}$
(C) $\log \left(e^{x}-e^{-x}\right)+\mathrm{C}$
(D) $\log \left(e^{x}+e^{-x}\right)+\mathrm{C}$
39. $\int \frac{\cos 2 x}{(\sin x+\cos x)^{2}} d x$ is equal to
(A) $\frac{-1}{\sin x+\cos x}+\mathrm{C}$
(B) $\log |\sin x+\cos x|+C$
(C) $\log |\sin x-\cos x|+C$
(D) $\frac{1}{(\sin x+\cos x)^{2}}$
40. If $f(a+b-x)=f(x)$, then $\int_{a}^{b} x f(x) d x$ is equal to
(A) $\frac{a+b}{2} \int_{a}^{b} f(b-x) d x$
(B) $\frac{a+b}{2} \int_{a}^{b} f(b+x) d x$
(C) $\frac{b-a}{2} \int_{a}^{b} f(x) d x$
(D) $\frac{a+b}{2} \int_{a}^{b} f(x) d x$

## Summary

- Integration is the inverse process of differentiation. In the differential calculus, we are given a function and we have to find the derivative or differential of this function, but in the integral calculus, we are to find a function whose differential is given. Thus, integration is a process which is the inverse of differentiation.
Let $\frac{d}{d x} \mathrm{~F}(x)=f(x)$. Then we write $\int f(x) d x=\mathrm{F}(x)+\mathrm{C}$. These integrals are called indefinite integrals or general integrals, C is called constant of integration. All these integrals differ by a constant.
- Some properties of indefinite integrals are as follows:

1. $\int[f(x)+g(x)] d x=\int f(x) d x+\int g(x) d x$
2. For any real number $k, \int k f(x) d x=k \int f(x) d x$

More generally, if $f_{1}, f_{2}, f_{3}, \ldots, f_{n}$ are functions and $k_{1}, k_{2}, \ldots, k_{n}$ are real numbers. Then

$$
\begin{aligned}
\int\left[k_{1} f_{1}(x)+k_{2} f_{2}(x)\right. & \left.+\ldots+k_{n} f_{n}(x)\right] d x \\
& =k_{1} \int f_{1}(x) d x+k_{2} \int f_{2}(x) d x+\ldots+k_{n} \int f_{n}(x) d x
\end{aligned}
$$

- Some standard integrals
(i) $\int x^{n} d x=\frac{x^{n+1}}{n+1}+\mathrm{C}, n \neq-1$. Particularly, $\int d x=x+\mathrm{C}$
(ii) $\int \cos x d x=\sin x+\mathrm{C}$
(iii) $\int \sin x d x=-\cos x+\mathrm{C}$
(iv) $\int \sec ^{2} x d x=\tan x+\mathrm{C}$
(v) $\int \operatorname{cosec}^{2} x d x=-\cot x+\mathrm{C}$
(vi) $\int \sec x \tan x d x=\sec x+\mathrm{C}$
(vii) $\int \operatorname{cosec} x \cot x d x=-\operatorname{cosec} x+\mathrm{C}$
(viii) $\int \frac{d x}{\sqrt{1-x^{2}}}=\sin ^{-1} x+\mathrm{C}$
(ix) $\int \frac{d x}{\sqrt{1-x^{2}}}=-\cos ^{-1} x+\mathrm{C}$
(x) $\int \frac{d x}{1+x^{2}}=\tan ^{-1} x+\mathrm{C}$
(xi) $\int \frac{d x}{1+x^{2}}=-\cot ^{-1} x+\mathrm{C}$
(xii) $\int e^{x} d x=e^{x}+\mathrm{C}$
(xiii) $\int a^{x} d x=\frac{a^{x}}{\log a}+\mathrm{C}$
(xiv) $\int \frac{1}{x} d x=\log |x|+\mathrm{C}$
- Integration by partial fractions

Recall that a rational function is ratio of two polynomials of the form $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}$, where $\mathrm{P}(x)$ and $\mathrm{Q}(x)$ are polynomials in $x$ and $\mathrm{Q}(x) \neq 0$. If degree of the polynomial $\mathrm{P}(x)$ is greater than the degree of the polynomial $\mathrm{Q}(x)$, then we may divide $\mathrm{P}(x)$ by $\mathrm{Q}(x)$ so that $\frac{\mathrm{P}(x)}{\mathrm{Q}(x)}=\mathrm{T}(x)+\frac{\mathrm{P}_{1}(x)}{\mathrm{Q}(x)}$, where $\mathrm{T}(x)$ is a polynomial in $x$ and degree of $\mathrm{P}_{1}(x)$ is less than the degree of $\mathrm{Q}(x) . \mathrm{T}(x)$ being polynomial can be easily integrated. $\frac{\mathrm{P}_{1}(x)}{\mathrm{Q}(x)}$ can be integrated by expressing $\frac{\mathrm{P}_{1}(x)}{\mathrm{Q}(x)}$ as the sum of partial fractions of the following type:

1. $\frac{p x+q}{(x-a)(x-b)}=\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{x-b}, a \neq b$
2. $\frac{p x+q}{(x-a)^{2}}=\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{(x-a)^{2}}$
3. $\frac{p x^{2}+q x+r}{(x-a)(x-b)(x-c)}=\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{x-b}+\frac{\mathrm{C}}{x-c}$
4. $\frac{p x^{2}+q x+r}{(x-a)^{2}(x-b)}=\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B}}{(x-a)^{2}}+\frac{\mathrm{C}}{x-b}$
5. $\frac{p x^{2}+q x+r}{(x-a)\left(x^{2}+b x+c\right)}=\frac{\mathrm{A}}{x-a}+\frac{\mathrm{B} x+\mathrm{C}}{x^{2}+b x+c}$
where $x^{2}+b x+c$ can not be factorised further.

- Integration by substitution

A change in the variable of integration often reduces an integral to one of the fundamental integrals. The method in which we change the variable to some other variable is called the method of substitution. When the integrand involves some trigonometric functions, we use some well known identities to find the integrals. Using substitution technique, we obtain the following standard integrals.
(i) $\int \tan x d x=\log |\sec x|+\mathrm{C}$
(ii) $\int \cot x d x=\log |\sin x|+\mathrm{C}$
(iii) $\int \sec x d x=\log |\sec x+\tan x|+\mathrm{C}$
(iv) $\int \operatorname{cosec} x d x=\log |\operatorname{cosec} x-\cot x|+\mathrm{C}$

- Integrals of some special functions
(i) $\int \frac{d x}{x^{2}-a^{2}}=\frac{1}{2 a} \log \left|\frac{x-a}{x+a}\right|+\mathrm{C}$
(ii) $\int \frac{d x}{a^{2}-x^{2}}=\frac{1}{2 a} \log \left|\frac{a+x}{a-x}\right|+\mathrm{C}$
(iii) $\int \frac{d x}{x^{2}+a^{2}}=\frac{1}{a} \tan ^{-1} \frac{x}{a}+\mathrm{C}$
(iv) $\int \frac{d x}{\sqrt{x^{2}-a^{2}}}=\log \left|x+\sqrt{x^{2}-a^{2}}\right|+\mathrm{C}$ (v) $\int \frac{d x}{\sqrt{a^{2}-x^{2}}}=\sin ^{-1} \frac{x}{a}+\mathrm{C}$
(vi) $\int \frac{d x}{\sqrt{x^{2}+a^{2}}}=\log \left|x+\sqrt{x^{2}+a^{2}}\right|+\mathrm{C}$


## - Integration by parts

For given functions $f_{1}$ and $f_{2}$, we have
$\int f_{1}(x) \cdot f_{2}(x) d x=f_{1}(x) \int f_{2}(x) d x-\int\left[\frac{d}{d x} f_{1}(x) \cdot \int f_{2}(x) d x\right] d x$, i.e., the integral of the product of two functions $=$ first function $\times$ integral of the second function - integral of \{differential coefficient of the first function $\times$ integral of the second function \}. Care must be taken in choosing the first function and the second function. Obviously, we must take that function as the second function whose integral is well known to us.

- $\int e^{x}\left[f(x)+f^{\prime}(x)\right] d x=\int e^{x} f(x) d x+\mathrm{C}$
- Some special types of integrals
(i) $\int \sqrt{x^{2}-a^{2}} d x=\frac{x}{2} \sqrt{x^{2}-a^{2}}-\frac{a^{2}}{2} \log \left|x+\sqrt{x^{2}-a^{2}}\right|+\mathrm{C}$
(ii) $\int \sqrt{x^{2}+a^{2}} d x=\frac{x}{2} \sqrt{x^{2}+a^{2}}+\frac{a^{2}}{2} \log \left|x+\sqrt{x^{2}+a^{2}}\right|+\mathrm{C}$
(iii) $\int \sqrt{a^{2}-x^{2}} d x=\frac{x}{2} \sqrt{a^{2}-x^{2}}+\frac{a^{2}}{2} \sin ^{-1} \frac{x}{a}+\mathrm{C}$
(iv) Integrals of the types $\int \frac{d x}{a x^{2}+b x+c}$ or $\int \frac{d x}{\sqrt{a x^{2}+b x+c}}$ can be transformed into standard form by expressing
$a x^{2}+b x+c=a\left[x^{2}+\frac{b}{a} x+\frac{c}{a}\right]=a\left[\left(x+\frac{b}{2 a}\right)^{2}+\left(\frac{c}{a}-\frac{b^{2}}{4 a^{2}}\right)\right]$
(v) Integrals of the types $\int \frac{p x+q d x}{a x^{2}+b x+c}$ or $\int \frac{p x+q d x}{\sqrt{a x^{2}+b x+c}}$ can be transformed into standard form by expressing $p x+q=\mathrm{A} \frac{d}{d x}\left(a x^{2}+b x+c\right)+\mathrm{B}=\mathrm{A}(2 a x+b)+\mathrm{B}$, where A and B are determined by comparing coefficients on both sides.
- We have defined $\int_{a}^{b} f(x) d x$ as the area of the region bounded by the curve $y=f(x), a \leq x \leq b$, the $x$-axis and the ordinates $x=a$ and $x=b$. Let $x$ be a
given point in $[a, b]$. Then $\int_{a}^{x} f(x) d x$ represents the Area function $\mathrm{A}(x)$.
This concept of area function leads to the Fundamental Theorems of Integral Calculus.
- First fundamental theorem of integral calculus

Let the area function be defined by $\mathrm{A}(x)=\int_{a}^{x} f(x) d x$ for all $x \geq a$, where the function $f$ is assumed to be continuous on $[a, b]$. Then $\mathrm{A}^{\prime}(x)=f(x)$ for all $x \in[a, b]$.

- Second fundamental theorem of integral calculus

Let $f$ be a continuous function of $x$ defined on the closed interval $[a, b]$ and let F be another function such that $\frac{d}{d x} \mathrm{~F}(x)=f(x)$ for all $x$ in the domain of $f$, then $\int_{a}^{b} f(x) d x=[\mathrm{F}(x)+\mathrm{C}]_{a}^{b}=\mathrm{F}(b)-\mathrm{F}(a)$.
This is called the definite integral of $f$ over the range $[a, b]$, where $a$ and $b$ are called the limits of integration, $a$ being the lower limit and $b$ the upper limit.

