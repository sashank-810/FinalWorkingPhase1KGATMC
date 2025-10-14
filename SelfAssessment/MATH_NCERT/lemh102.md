## INVERSE TRIGONOMETRIC FUNCTIONS

## Mathematics，in general，is fundamentally the science of self－evident things．－FELIX KLEIN

## 2．1 Introduction

In Chapter 1，we have studied that the inverse of a function $f$ ，denoted by $f^{-1}$ ，exists if $f$ is one－one and onto．There are many functions which are not one－one，onto or both and hence we can not talk of their inverses．In Class XI，we studied that trigonometric functions are not one－one and onto over their natural domains and ranges and hence their inverses do not exist．In this chapter，we shall study about the restrictions on domains and ranges of trigonometric functions which ensure the existence of their inverses and observe their behaviour through graphical representations． Besides，some elementary properties will also be discussed．

The inverse trigonometric functions play an important role in calculus for they serve to define many integrals．
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-01.jpg?height=532&width=409&top_left_y=866&top_left_x=1064)

Aryabhata
（476－550 A．D．）

The concepts of inverse trigonometric functions is also used in science and engineering．

## 2．2 Basic Concepts

In Class XI，we have studied trigonometric functions，which are defined as follows：
sine function，i．e．，sine ： $\mathbf{R} \rightarrow[-1,1]$
cosine function，i．e．， $\cos : \mathbf{R} \rightarrow[-1,1]$
tangent function，i．e．， $\tan : \mathbf{R}-\left\{x: x=(2 n+1) \frac{\pi}{2}, n \in \mathbf{Z}\right\} \rightarrow \mathbf{R}$
cotangent function，i．e．， $\cot : \mathbf{R}-\{x: x=n \pi, n \in \mathbf{Z}\} \rightarrow \mathbf{R}$
secant function，i．e．， $\sec : \mathbf{R}-\left\{x: x=(2 n+1) \frac{\pi}{2}, n \in \mathbf{Z}\right\} \rightarrow \mathbf{R}-(-1,1)$
cosecant function，i．e．， $\operatorname{cosec}: \mathbf{R}-\{x: x=n \pi, n \in \mathbf{Z}\} \rightarrow \mathbf{R}-(-1,1)$

We have also learnt in Chapter 1 that if $f: \mathrm{X} \rightarrow \mathrm{Y}$ such that $f(x)=y$ is one-one and onto, then we can define a unique function $g: \mathrm{Y} \rightarrow \mathrm{X}$ such that $g(y)=x$, where $x \in \mathrm{X}$ and $y=f(x), y \in \mathrm{Y}$. Here, the domain of $g=$ range of $f$ and the range of $g=$ domain of $f$. The function $g$ is called the inverse of $f$ and is denoted by $f^{-1}$. Further, $g$ is also one-one and onto and inverse of $g$ is $f$. Thus, $g^{-1}=\left(f^{-1}\right)^{-1}=f$. We also have
and

$$
\begin{aligned}
& \left(f^{-1} \circ f\right)(x)=f^{-1}(f(x))=f^{-1}(y)=x \\
& \left(f \circ f^{-1}\right)(y)=f\left(f^{-1}(y)\right)=f(x)=y
\end{aligned}
$$

Since the domain of sine function is the set of all real numbers and range is the closed interval $[-1,1]$. If we restrict its domain to $\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$, then it becomes one-one and onto with range $[-1,1]$. Actually, sine function restricted to any of the intervals

$$
\frac{-3 \pi}{2}, \frac{\pi}{2},\left[\frac{-\pi}{2}, \frac{\pi}{2}\right],\left[\frac{\pi}{2}, \frac{3 \pi}{2}\right] \text { etc., is one-one and its range is }[-1,1] \text {. We can, }
$$

therefore, define the inverse of sine function in each of these intervals. We denote the inverse of sine function by $\sin ^{-1}$ (arc sine function). Thus, $\sin ^{-1}$ is a function whose domain is $[-1,1]$ and range could be any of the intervals $\left[\frac{-3 \pi}{2}, \frac{-\pi}{2}\right],\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$ or $\left[\frac{\pi}{2}, \frac{3 \pi}{2}\right]$, and so on. Corresponding to each such interval, we get a branch of the function $\sin ^{-1}$. The branch with range $\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$ is called the principal value branch, whereas other intervals as range give different branches of $\sin ^{-1}$. When we refer to the function $\sin ^{-1}$, we take it as the function whose domain is $[-1,1]$ and range is $\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$. We write $\sin ^{-1}:[-1,1] \rightarrow\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$

From the definition of the inverse functions, it follows that $\sin \left(\sin ^{-1} x\right)=x$ if $-1 \leq x \leq 1$ and $\sin ^{-1}(\sin x)=x$ if $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$. In other words, if $y=\sin ^{-1} x$, then $\sin y=x$.

## Remarks

(i) We know from Chapter 1, that if $y=f(x)$ is an invertible function, then $x=f^{-1}(y)$. Thus, the graph of $\sin ^{-1}$ function can be obtained from the graph of original function by interchanging $x$ and $y$ axes, i.e., if $(a, b)$ is a point on the graph of sine function, then $(b, a)$ becomes the corresponding point on the graph of inverse
of sine function. Thus, the graph of the function $y=\sin ^{-1} x$ can be obtained from the graph of $y=\sin x$ by interchanging $x$ and $y$ axes. The graphs of $y=\sin x$ and $y=\sin ^{-1} x$ are as given in Fig 2.1 (i), (ii), (iii). The dark portion of the graph of $y=\sin ^{-1} x$ represent the principal value branch.
(ii) It can be shown that the graph of an inverse function can be obtained from the corresponding graph of original function as a mirror image (i.e., reflection) along the line $y=x$. This can be visualised by looking the graphs of $y=\sin x$ and $y=\sin ^{-1} x$ as given in the same axes (Fig 2.1 (iii)).
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-03.jpg?height=288&width=873&top_left_y=705&top_left_x=361)

Fig 2.1 (i)
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-03.jpg?height=838&width=303&top_left_y=1061&top_left_x=157)

Fig 2.1 (ii)
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-03.jpg?height=861&width=956&top_left_y=1040&top_left_x=482)

Fig 2.1 (iii)

Like sine function, the cosine function is a function whose domain is the set of all real numbers and range is the set $[-1,1]$. If we restrict the domain of cosine function to $[0, \pi]$, then it becomes one-one and onto with range $[-1,1]$. Actually, cosine function
restricted to any of the intervals $[-\pi, 0],[0, \pi],[\pi, 2 \pi]$ etc., is bijective with range as $[-1,1]$. We can, therefore, define the inverse of cosine function in each of these intervals. We denote the inverse of the cosine function by $\cos ^{-1}$ (arc cosine function). Thus, $\cos ^{-1}$ is a function whose domain is $[-1,1]$ and range could be any of the intervals $[-\pi, 0],[0, \pi],[\pi, 2 \pi]$ etc. Corresponding to each such interval, we get a branch of the function $\cos ^{-1}$. The branch with range $[0, \pi]$ is called the principal value branch of the function $\cos ^{-1}$. We write

$$
\cos ^{-1}:[-1,1] \rightarrow[0, \pi] .
$$

The graph of the function given by $y=\cos ^{-1} x$ can be drawn in the same way as discussed about the graph of $y=\sin ^{-1} x$. The graphs of $y=\cos x$ and $y=\cos ^{-1} x$ are given in Fig 2.2 (i) and (ii).
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-04.jpg?height=370&width=887&top_left_y=1035&top_left_x=155)

Fig 2.2 (i)
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-04.jpg?height=906&width=340&top_left_y=500&top_left_x=1129)

Fig 2.2 (ii)

Let us now discuss $\operatorname{cosec}^{-1} x$ and $\sec ^{-1} x$ as follows:
Since, $\operatorname{cosec} x=\frac{1}{\sin x}$, the domain of the cosec function is the set $\{x: x \in \mathbf{R}$ and $x \neq n \pi, n \in \mathbf{Z}\}$ and the range is the set $\{y: y \in \mathbf{R}, y \geq 1$ or $y \leq-1\}$ i.e., the set $\mathbf{R}-(-1,1)$. It means that $y=\operatorname{cosec} x$ assumes all real values except $-1<y<1$ and is not defined for integral multiple of $\pi$. If we restrict the domain of cosec function to $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$, then it is one to one and onto with its range as the set $\mathbf{R}-(-1,1)$. Actually, cosec function restricted to any of the intervals $\left[\frac{-3 \pi}{2}, \frac{-\pi}{2}\right]-\{-\pi\},\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]-\{0\}$, $\left[\frac{\pi}{2}, \frac{3 \pi}{2}\right]-\{\pi\}$ etc., is bijective and its range is the set of all real numbers $\mathbf{R}-(-1,1)$.

Thus $\operatorname{cosec}^{-1}$ can be defined as a function whose domain is $\mathbf{R}-(-1,1)$ and range could be any of the intervals $\frac{-3 \pi}{2}, \frac{-\pi}{2}-\{-\pi\}, \frac{-\pi}{2}, \frac{\pi}{2}-\{0\},\left[\frac{\pi}{2}, \frac{3 \pi}{2}\right]-\{\pi\}$ etc. The function corresponding to the range $\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]-\{0\}$ is called the principal value branch of $\operatorname{cosec}^{-1}$. We thus have principal branch as

$$
\operatorname{cosec}^{-1}: \mathbf{R}-(-1,1) \rightarrow\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]-\{0\}
$$

The graphs of $y=\operatorname{cosec} x$ and $y=\operatorname{cosec}^{-1} x$ are given in Fig 2.3 (i), (ii).
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-05.jpg?height=622&width=676&top_left_y=1025&top_left_x=154)

Fig 2.3 (i)
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-05.jpg?height=745&width=604&top_left_y=880&top_left_x=872)

Fig 2.3 (ii)

Also, since $\sec x=\frac{1}{\cos x}$, the domain of $y=\sec x$ is the set $\mathbf{R}-\left\{x: x=(2 n+1) \frac{\pi}{2}\right.$, $n \in \mathbf{Z}\}$ and range is the set $\mathbf{R}-(-1,1)$. It means that sec (secant function) assumes all real values except $-1<y<1$ and is not defined for odd multiples of $\frac{\pi}{2}$. If we restrict the domain of secant function to $[0, \pi]-\left\{\frac{\pi}{2}\right\}$, then it is one-one and onto with
its range as the set $\mathbf{R}-(-1,1)$. Actually, secant function restricted to any of the intervals $[-\pi, 0]-\left\{\frac{-\pi}{2}\right\},[0, \pi]-\left\{\frac{\pi}{2}\right\},[\pi, 2 \pi]-\left\{\frac{3 \pi}{2}\right\}$ etc., is bijective and its range is $\mathbf{R}-\{-1,1\}$. Thus $\sec ^{-1}$ can be defined as a function whose domain is $\mathbf{R}-(-1,1)$ and range could be any of the intervals $[-\pi, 0]-\left\{\frac{-\pi}{2}\right\},[0, \pi]-\left\{\frac{\pi}{2}\right\},[\pi, 2 \pi]-\left\{\frac{3 \pi}{2}\right\}$ etc. Corresponding to each of these intervals, we get different branches of the function $\mathrm{sec}^{-1}$. The branch with range $[0, \pi]-\left\{\frac{\pi}{2}\right\}$ is called the principal value branch of the function $\mathrm{sec}^{-1}$. We thus have

$$
\sec ^{-1}: \mathbf{R}-(-1,1) \rightarrow[0, \pi]-\left\{\frac{\pi}{2}\right\}
$$

The graphs of the functions $y=\sec x$ and $y=\sec ^{-1} x$ are given in Fig 2.4 (i), (ii).
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-06.jpg?height=620&width=671&top_left_y=1114&top_left_x=156)

Fig 2.4 (i)
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-06.jpg?height=720&width=590&top_left_y=983&top_left_x=881)

Fig 2.4 (ii)

Finally, we now discuss $\tan ^{-1}$ and $\cot ^{-1}$
We know that the domain of the tan function (tangent function) is the set $\left\{x: x \in \mathbf{R}\right.$ and $\left.x \neq(2 n+1) \frac{\pi}{2}, n \in \mathbf{Z}\right\}$ and the range is $\mathbf{R}$. It means that tan function is not defined for odd multiples of $\frac{\pi}{2}$. If we restrict the domain of tangent function to
$\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$, then it is one-one and onto with its range as $\mathbf{R}$. Actually, tangent function restricted to any of the intervals $\left(\frac{-3 \pi}{2}, \frac{-\pi}{2}\right),\left(\frac{-\pi}{2}, \frac{\pi}{2}\right),\left(\frac{\pi}{2}, \frac{3 \pi}{2}\right)$ etc., is bijective and its range is $\mathbf{R}$. Thus $\tan ^{-1}$ can be defined as a function whose domain is $\mathbf{R}$ and range could be any of the intervals $\left(\frac{-3 \pi}{2}, \frac{-\pi}{2}\right),\left(\frac{-\pi}{2}, \frac{\pi}{2}\right),\left(\frac{\pi}{2}, \frac{3 \pi}{2}\right)$ and so on. These intervals give different branches of the function $\tan ^{-1}$. The branch with range $\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$ is called the principal value branch of the function $\tan ^{-1}$.

We thus have

$$
\tan ^{-1}: \mathbf{R} \rightarrow\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)
$$

The graphs of the function $y=\tan x$ and $y=\tan ^{-1} x$ are given in Fig 2.5 (i), (ii).
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-07.jpg?height=569&width=646&top_left_y=1214&top_left_x=166)

Fig 2.5 (i)
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-07.jpg?height=679&width=518&top_left_y=1052&top_left_x=947)

Fig 2.5 (ii)

We know that domain of the cot function (cotangent function) is the set $\{x: x \in \mathbf{R}$ and $x \neq n \pi, n \in \mathbf{Z}\}$ and range is $\mathbf{R}$. It means that cotangent function is not defined for integral multiples of $\pi$. If we restrict the domain of cotangent function to $(0, \pi)$, then it is bijective with and its range as $\mathbf{R}$. In fact, cotangent function restricted to any of the intervals $(-\pi, 0),(0, \pi),(\pi, 2 \pi)$ etc., is bijective and its range is $\mathbf{R}$. Thus $\cot ^{-1}$ can be defined as a function whose domain is the $\mathbf{R}$ and range as any of the
intervals $(-\pi, 0),(0, \pi),(\pi, 2 \pi)$ etc. These intervals give different branches of the function $\cot ^{-1}$. The function with range ( $0, \pi$ ) is called the principal value branch of the function $\cot ^{-1}$. We thus have

$$
\cot ^{-1}: \mathbf{R} \rightarrow(0, \pi)
$$

The graphs of $y=\cot x$ and $y=\cot ^{-1} x$ are given in Fig 2.6 (i), (ii).
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-08.jpg?height=549&width=629&top_left_y=725&top_left_x=168)
$y=\cot x$
Fig 2.6 (i)
![](https://cdn.mathpix.com/cropped/2025_07_21_9285e5942c529515a344g-08.jpg?height=748&width=546&top_left_y=568&top_left_x=928)

Fig 2.6 (ii)

The following table gives the inverse trigonometric function (principal value branches) along with their domains and ranges.

| $\sin ^{-1}$ | [-1, 1] | $\rightarrow$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| :--- | :--- | :--- | :--- |
| $\cos ^{-1}$ | [-1, 1] | $\rightarrow$ | $[0, \pi]$ |
| $\operatorname{cosec}^{-1}$ | $\mathbf{R}$ - (-1,1) | $\rightarrow$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$ |
| $\mathrm{sec}^{-1}$ | $\mathbf{R}-(-1,1)$ | $\rightarrow$ | $[0, \pi]-\left\{\frac{\pi}{2}\right\}$ |
| $\tan ^{-1}$ | R | $\rightarrow$ | $\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$ |
| $\cot ^{-1}$ | R | $\rightarrow$ | $(0, \pi)$ |

## Note

1. $\sin ^{-1} x$ should not be confused with $(\sin x)^{-1}$. In fact $(\sin x)^{-1}=\frac{1}{\sin x}$ and similarly for other trigonometric functions.
2. Whenever no branch of an inverse trigonometric functions is mentioned, we mean the principal value branch of that function.
3. The value of an inverse trigonometric functions which lies in the range of principal branch is called the principal value of that inverse trigonometric functions.

We now consider some examples:
Example 1 Find the principal value of $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)$.
Solution Let $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)=y$. Then, $\sin y=\frac{1}{\sqrt{2}}$.
We know that the range of the principal value branch of $\sin ^{-1}$ is $\frac{-\pi}{2}, \frac{\pi}{2}$ and $\sin \left(\frac{\pi}{4}\right)=\frac{1}{\sqrt{2}}$. Therefore, principal value of $\sin ^{-1}\left(\frac{1}{\sqrt{2}}\right)$ is $\frac{\pi}{4}$
Example 2 Find the principal value of $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$
Solution Let $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)=y$. Then,

$$
\cot y=\frac{-1}{\sqrt{3}}=-\cot \left(\frac{\pi}{3}\right)=\cot \left(\pi-\frac{\pi}{3}\right)=\cot \left(\frac{2 \pi}{3}\right)
$$

We know that the range of principal value branch of $\cot ^{-1}$ is $(0, \pi)$ and $\cot \left(\frac{2 \pi}{3}\right)=\frac{-1}{\sqrt{3}}$. Hence, principal value of $\cot ^{-1}\left(\frac{-1}{\sqrt{3}}\right)$ is $\frac{2 \pi}{3}$

## EXERCISE 2.1

Find the principal values of the following:

1. $\sin ^{-1}\left(-\frac{1}{2}\right)$
2. $\cos ^{-1}\left(\frac{\sqrt{3}}{2}\right)$
3. $\operatorname{cosec}^{-1}$
(2)
4. $\tan ^{-1}(-\sqrt{3})$
5. $\cos ^{-1}\left(-\frac{1}{2}\right)$
6. $\tan ^{-1}(-1)$
7. $\sec ^{-1}\left(\frac{2}{\sqrt{3}}\right)$
8. $\cot ^{-1}(\sqrt{3})$
9. $\cos ^{-1}\left(-\frac{1}{\sqrt{2}}\right)$
10. $\operatorname{cosec}^{-1}(-\sqrt{2})$

Find the values of the following:
11. $\tan ^{-1}(1)+\cos ^{-1}-\frac{1}{2}+\sin ^{-1}-\frac{1}{2}$
12. $\cos ^{-1} \frac{1}{2}+2 \sin ^{-1} \frac{1}{2}$
13. If $\sin ^{-1} x=y$, then
(A) $0 \leq y \leq \pi$
(B) $-\frac{\pi}{2} \leq y \leq \frac{\pi}{2}$
(C) $0<y<\pi$
(D) $-\frac{\pi}{2}<y<\frac{\pi}{2}$
14. $\tan ^{-1} \sqrt{3}-\sec ^{-1}(-2)$ is equal to
(A) $\pi$
(B) $-\frac{\pi}{3}$
(C) $\frac{\pi}{3}$
(D) $\frac{2 \pi}{3}$

### 2.3 Properties of Inverse Trigonometric Functions

In this section, we shall prove some important properties of inverse trigonometric functions. It may be mentioned here that these results are valid within the principal value branches of the corresponding inverse trigonometric functions and wherever they are defined. Some results may not be valid for all values of the domains of inverse trigonometric functions. In fact, they will be valid only for some values of $x$ for which inverse trigonometric functions are defined. We will not go into the details of these values of $x$ in the domain as this discussion goes beyond the scope of this textbook.

Let us recall that if $y=\sin ^{-1} x$, then $x=\sin y$ and if $x=\sin y$, then $y=\sin ^{-1} x$. This is equivalent to

$$
\sin \left(\sin ^{-1} x\right)=x, x \in[-1,1] \text { and } \sin ^{-1}(\sin x)=x, x \in\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]
$$

For suitable values of domain similar results follow for remaining trigonometric functions.

We now consider some examples.
Example 3 Show that
(i) $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \sin ^{-1} x,-\frac{1}{\sqrt{2}} \leq x \leq \frac{1}{\sqrt{2}}$
(ii) $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \cos ^{-1} x, \frac{1}{\sqrt{2}} \leq x \leq 1$

## Solution

(i) Let $x=\sin \theta$. Then $\sin ^{-1} x=\theta$. We have

$$
\begin{aligned}
\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right) & =\sin ^{-1}\left(2 \sin \theta \sqrt{1-\sin ^{2} \theta}\right) \\
& =\sin ^{-1}(2 \sin \theta \cos \theta)=\sin ^{-1}(\sin 2 \theta)=2 \theta \\
& =2 \sin ^{-1} x
\end{aligned}
$$

(ii) Take $x=\cos \theta$, then proceeding as above, we get, $\sin ^{-1}\left(2 x \sqrt{1-x^{2}}\right)=2 \cos ^{-1} x$

Example 4 Express $\tan ^{-1} \frac{\cos x}{1-\sin x},-\frac{3 \pi}{2}<x<\frac{\pi}{2}$ in the simplest form.
Solution We write

$$
\begin{aligned}
\tan ^{-1}\left(\frac{\cos x}{1-\sin x}\right) & =\tan ^{-1}\left[\frac{\cos ^{2} \frac{x}{2}-\sin ^{2} \frac{x}{2}}{\cos ^{2} \frac{x}{2}+\sin ^{2} \frac{x}{2}-2 \sin \frac{x}{2} \cos \frac{x}{2}}\right] \\
& =\tan ^{-1}\left[\frac{\left(\cos \frac{x}{2}+\sin \frac{x}{2}\right)\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)}{\left(\cos \frac{x}{2}-\sin \frac{x}{2}\right)^{2}}\right] \\
& =\tan ^{-1}\left[\frac{\cos \frac{x}{2}+\sin \frac{x}{2}}{\cos \frac{x}{2}-\sin \frac{x}{2}}\right]=\tan ^{-1}\left[\frac{1+\tan \frac{x}{2}}{1-\tan \frac{x}{2}}\right] \\
& =\tan ^{-1}\left[\tan \left(\frac{\pi}{4}+\frac{x}{2}\right)\right]=\frac{\pi}{4}+\frac{x}{2}
\end{aligned}
$$

Example 5 Write $\cot ^{-1}\left(\frac{1}{\sqrt{x^{2}-1}}\right), x>1$ in the simplest form.

Solution Let $x=\sec \theta$, then $\sqrt{x^{2}-1}=\sqrt{\sec ^{2} \theta-1}=\tan \theta$
Therefore, $\cot ^{-1} \frac{1}{\sqrt{x^{2}-1}}=\cot ^{-1}(\cot \theta)=\theta=\sec ^{-1} x$, which is the simplest form.

## EXERCISE 2.2

Prove the following:

1. $3 \sin ^{-1} x=\sin ^{-1}\left(3 x-4 x^{3}\right), x \in\left[-\frac{1}{2}, \frac{1}{2}\right]$
2. $3 \cos ^{-1} x=\cos ^{-1}\left(4 x^{3}-3 x\right), x \in\left[\frac{1}{2}, 1\right]$

Write the following functions in the simplest form:
3. $\tan ^{-1} \frac{\sqrt{1+x^{2}}-1}{x}, x \neq 0$
4. $\tan ^{-1}\left(\sqrt{\frac{1-\cos x}{1+\cos x}}\right), 0<x<\pi$
5. $\tan ^{-1}\left(\frac{\cos x-\sin x}{\cos x+\sin x}\right), \frac{-\pi}{4}<x<\frac{3 \pi}{4}$
6. $\tan ^{-1} \frac{x}{\sqrt{a^{2}-x^{2}}},|x|<a$
7. $\tan ^{-1}\left(\frac{3 a^{2} x-x^{3}}{a^{3}-3 a x^{2}}\right), a>0 ; \frac{-a}{\sqrt{3}}<x<\frac{a}{\sqrt{3}}$

Find the values of each of the following:
8. $\tan ^{-1}\left[2 \cos \left(2 \sin ^{-1} \frac{1}{2}\right)\right]$
9. $\tan \frac{1}{2}\left[\sin ^{-1} \frac{2 x}{1+x^{2}}+\cos ^{-1} \frac{1-y^{2}}{1+y^{2}}\right],|x|<1, y>0$ and $x y<1$

Find the values of each of the expressions in Exercises 16 to 18.
10. $\sin ^{-1}\left(\sin \frac{2 \pi}{3}\right)$
11. $\tan ^{-1}\left(\tan \frac{3 \pi}{4}\right)$
12. $\tan \left(\sin ^{-1} \frac{3}{5}+\cot ^{-1} \frac{3}{2}\right)$
13. $\cos ^{-1}\left(\cos \frac{7 \pi}{6}\right)$ is equal to
(A) $\frac{7 \pi}{6}$
(B) $\frac{5 \pi}{6}$
(C) $\frac{\pi}{3}$
(D) $\frac{\pi}{6}$
14. $\sin \left(\frac{\pi}{3}-\sin ^{-1}\left(-\frac{1}{2}\right)\right)$ is equal to
(A) $\frac{1}{2}$
(B) $\frac{1}{3}$
(C) $\frac{1}{4}$
(D) 1
15. $\tan ^{-1} \sqrt{3}-\cot ^{-1}(-\sqrt{3})$ is equal to
(A) $\pi$
(B) $-\frac{\pi}{2}$
(C) 0
(D) $2 \sqrt{3}$

## Miscellaneous Examples

Example 6 Find the value of $\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)$
Solution We know that $\sin ^{-1}(\sin x)=x$. Therefore, $\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\frac{3 \pi}{5}$

But $\frac{3 \pi}{5} \notin\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, which is the principal branch of $\sin ^{-1} x$
However $\quad \sin \left(\frac{3 \pi}{5}\right)=\sin \left(\pi-\frac{3 \pi}{5}\right)=\sin \frac{2 \pi}{5}$ and $\frac{2 \pi}{5} \in\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$

Therefore $\sin ^{-1}\left(\sin \frac{3 \pi}{5}\right)=\sin ^{-1}\left(\sin \frac{2 \pi}{5}\right)=\frac{2 \pi}{5}$

## Miscellaneous Exercise on Chapter 2

Find the value of the following:

1. $\cos ^{-1}\left(\cos \frac{13 \pi}{6}\right)$
2. $\tan ^{-1}\left(\tan \frac{7 \pi}{6}\right)$

Prove that
3. $2 \sin ^{-1} \frac{3}{5}=\tan ^{-1} \frac{24}{7}$
4. $\sin ^{-1} \frac{8}{17}+\sin ^{-1} \frac{3}{5}=\tan ^{-1} \frac{77}{36}$
5. $\cos ^{-1} \frac{4}{5}+\cos ^{-1} \frac{12}{13}=\cos ^{-1} \frac{33}{65}$
6. $\cos ^{-1} \frac{12}{13}+\sin ^{-1} \frac{3}{5}=\sin ^{-1} \frac{56}{65}$
7. $\tan ^{-1} \frac{63}{16}=\sin ^{-1} \frac{5}{13}+\cos ^{-1} \frac{3}{5}$

Prove that
8. $\tan ^{-1} \sqrt{x}=\frac{1}{2} \cos ^{-1} \frac{1-x}{1+x}, x \in[0,1]$
9. $\cot ^{-1}\left(\frac{\sqrt{1+\sin x}+\sqrt{1-\sin x}}{\sqrt{1+\sin x}-\sqrt{1-\sin x}}\right)=\frac{x}{2}, x \in\left(0, \frac{\pi}{4}\right)$
10. $\tan ^{-1}\left(\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}\right)=\frac{\pi}{4}-\frac{1}{2} \cos ^{-1} x,-\frac{1}{\sqrt{2}} \leq x \leq 1$ [Hint: Put $x=\cos 2 \theta$ ]

Solve the following equations:
11. $2 \tan ^{-1}(\cos x)=\tan ^{-1}(2 \operatorname{cosec} x)$
12. $\tan ^{-1} \frac{1-x}{1+x}=\frac{1}{2} \tan ^{-1} x,(x>0)$
13. $\sin \left(\tan ^{-1} x\right),|x|<1$ is equal to
(A) $\frac{x}{\sqrt{1-x^{2}}}$
(B) $\frac{1}{\sqrt{1-x^{2}}}$
(C) $\frac{1}{\sqrt{1+x^{2}}}$
(D) $\frac{x}{\sqrt{1+x^{2}}}$
14. $\sin ^{-1}(1-x)-2 \sin ^{-1} x=\frac{\pi}{2}$, then $x$ is equal to
(A) $0, \frac{1}{2}$
(B) $1, \frac{1}{2}$
(C) 0
(D) $\frac{1}{2}$

## Summary

- The domains and ranges (principal value branches) of inverse trigonometric functions are given in the following table:

| Functions | Domain | Range (Principal Value Branches) |
| :--- | :--- | :--- |
| $y=\sin ^{-1} x$ | [-1, 1] | $\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]$ |
| $y=\cos ^{-1} x$ | [-1, 1] | $[0, \pi]$ |
| $y=\operatorname{cosec}^{-1} x$ | $\mathbf{R}$ - (-1,1) | $\left[\frac{-\pi}{2}, \frac{\pi}{2}\right]-\{0\}$ |
| $y=\sec ^{-1} x$ | $\mathbf{R}$ - ( $-1,1$ ) | $[0, \pi]-\left\{\frac{\pi}{2}\right\}$ |
| $y=\tan ^{-1} x$ | R | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |
| $y=\cot ^{-1} x$ | R | $(0, \pi)$ |

- $\sin ^{-1} x$ should not be confused with $(\sin x)^{-1}$. In fact $(\sin x)^{-1}=\frac{1}{\sin x}$ and similarly for other trigonometric functions.
- The value of an inverse trigonometric functions which lies in its principal value branch is called the principal value of that inverse trigonometric functions.

For suitable values of domain, we have

- $y=\sin ^{-1} x \Rightarrow x=\sin y$
- $\sin \left(\sin ^{-1} x\right)=x$
- $x=\sin y \Rightarrow y=\sin ^{-1} x$
- $\sin ^{-1}(\sin x)=x$


## Historical Note

The study of trigonometry was first started in India. The ancient Indian Mathematicians, Aryabhata (476A.D.), Brahmagupta (598 A.D.), Bhaskara I (600 A.D.) and Bhaskara II (1114 A.D.) got important results of trigonometry. All this knowledge went from India to Arabia and then from there to Europe. The Greeks had also started the study of trigonometry but their approach was so clumsy that when the Indian approach became known, it was immediately adopted throughout the world.

In India, the predecessor of the modern trigonometric functions, known as the sine of an angle, and the introduction of the sine function represents one of the main contribution of the siddhantas (Sanskrit astronomical works) to mathematics.

Bhaskara I (about 600 A.D.) gave formulae to find the values of sine functions for angles more than $90^{\circ}$. A sixteenth century Malayalam work Yuktibhasa contains a proof for the expansion of $\sin (\mathrm{A}+\mathrm{B})$. Exact expression for sines or cosines of $18^{\circ}, 36^{\circ}, 54^{\circ}, 72^{\circ}$, etc., were given by Bhaskara II.

The symbols $\sin ^{-1} x, \cos ^{-1} x$, etc., for $\operatorname{arc} \sin x, \operatorname{arc} \cos x$, etc., were suggested by the astronomer Sir John F.W. Hersehel (1813) The name of Thales (about 600 B.C.) is invariably associated with height and distance problems. He is credited with the determination of the height of a great pyramid in Egypt by measuring shadows of the pyramid and an auxiliary staff (or gnomon) of known height, and comparing the ratios:

$$
\frac{\mathrm{H}}{\mathrm{~S}}=\frac{h}{S}=\tan \text { (sun's altitude) }
$$

Thales is also said to have calculated the distance of a ship at sea through the proportionality of sides of similar triangles. Problems on height and distance using the similarity property are also found in ancient Indian works.

