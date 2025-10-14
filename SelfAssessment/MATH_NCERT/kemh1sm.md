## CHAPTER 8

### 8.6 Infinite G.P. and its Sum

G.P. of the form $a, a r, a r^{2}, a r^{3}, \ldots$ is called infinite G.P. Now, to find the formulae for finding sum to infinity of a G.P., we begin with an example.

Let us consider the G.P.,

$$
1, \frac{2}{3}, \frac{4}{9}, \ldots
$$

Here $a=1, r=\frac{2}{3}$. We have

$$
\mathrm{S}_{n}=\frac{1-\left(\frac{2}{3}\right)^{n}}{1-\frac{2}{3}}=3\left[1-\left(\frac{2}{3}\right)^{n}\right]
$$

Let us study the behaviour of $\left(\frac{2}{3}\right)^{n}$ as $n$ becomes larger and larger:

| $n$ | 1 | 5 | 10 | 20 |
| :---: | :---: | :---: | :---: | :---: |
| $\left(\frac{2}{3}\right)^{n}$ | 0.6667 | 0.1316872428 | 0.01734152992 | 0.00030072866 |

We observe that as $n$ becomes larger and larger, $\left(\frac{2}{3}\right)^{n}$ becomes closer and closer to zero. Mathematically, we say that as $n$ becomes sufficiently large, $\left(\frac{2}{3}\right)^{n}$ becomes sufficiently small. In other words as $n \rightarrow \infty,\left(\frac{2}{3}\right)^{n} \rightarrow 0$. Consequently, we find that the sum of infinitely many terms is given by $S_{\infty}=3$.

Now, for a geometric progression, $a, a r, a r^{2}, \ldots$, if numerical value of common ratio $r$ is less than 1 , then

$$
\mathrm{S}_{n}=\frac{a\left(1-r^{n}\right)}{(1-r)}=\frac{a}{1-r}-\frac{a r^{n}}{1-r}
$$

In this case as $n \rightarrow \infty, r^{n} \rightarrow 0$ since $|r|<1$. Therefore

$$
S_{n} \rightarrow \frac{a}{1-r}
$$

Symbolically sum to infinity is denoted by $\mathrm{S}_{\infty}$ or S .
Thus, we have $\mathrm{S}=\frac{a}{1-r}$.
For examples,
(i) $\quad 1+\frac{1}{2}+\frac{1}{2^{2}}+\frac{1}{2^{3}}+\ldots=\frac{1}{1-\frac{1}{2}}=2$.
(ii) $\quad 1-\frac{1}{2}+\frac{1}{2^{2}}-\frac{1}{2^{3}}+\ldots=\frac{1}{1-\left(\frac{-1}{2}\right)}=\frac{1}{1+\frac{1}{2}}=\frac{2}{3}$

## Exercise 8.3

Find the sum to infinity in each of the following Geometric Progression.

1. $1, \frac{1}{3}, \frac{1}{9}, \ldots$
(Ans. 1.5)
2. $6,1.2, .24, \ldots$
(Ans. 7.5)
3. $5, \frac{20}{7}, \frac{80}{49}, \ldots$
(Ans. $\frac{35}{3}$ )
4. $\frac{-3}{4}, \frac{3}{16}, \frac{-3}{64}, \ldots$
(Ans. $\frac{-3}{5}$ )
5. Prove that $3^{\frac{1}{2}} \times 3^{\frac{1}{4}} \times 3^{\frac{1}{8}} \ldots=3$
6. Let $x=1+a+a^{2}+\ldots$ and $y=1+b+b^{2}+\ldots$, where $|a|<1$ and $|b|<1$. Prove that

$$
1+a b+a^{2} b^{2}+\ldots=\frac{x y}{x+y-1}
$$

## CHAPTER 12

### 12.6 Limits Involving Exponential and Logarithmic Functions

Before discussing evaluation of limits of the expressions involving exponential and logarithmic functions, we introduce these two functions stating their domain, range and also sketch their graphs roughly.

Leonhard Euler (1707-1783), the great Swiss mathematician introduced the number $e$ whose value lies between 2 and 3. This number is useful in defining exponential function and is defined as $f(x)=e^{x}, x \in \mathbf{R}$. Its domain is $\mathbf{R}$, range is the set of positive real numbers. The graph of exponential function, i.e., $y=e^{x}$ is as given in Fig.13.11.
![](https://cdn.mathpix.com/cropped/2025_07_21_19af64d187352f6b4acfg-3.jpg?height=657&width=678&top_left_y=836&top_left_x=482)

Fig. 13.11
Similarly, the logarithmic function expressed as $\log _{e} \mathbf{R}^{+} \rightarrow \mathbf{R}$ is given by $\log _{e} x=y$, if and only if $e^{y}=x$. Its domain is $\mathbf{R}^{+}$which is the set of all positive real numbers and range is $\mathbf{R}$. The graph of logarithmic function $y=\log _{e} x$ is shown in Fig.13.12.
![](https://cdn.mathpix.com/cropped/2025_07_21_19af64d187352f6b4acfg-4.jpg?height=729&width=773&top_left_y=373&top_left_x=465)

Fig. 13.12

In order to prove the result $\lim _{x \rightarrow 0} \frac{e^{x}-1}{x}=1$, we make use of an inequality involving the expression $\frac{e^{x}-1}{x}$ which runs as follows:
$\frac{1}{1+|x|} \leq \frac{e^{x}-1}{x} \leq 1+(e-2)|x|$ holds for all $x$ in $[-1,1] \sim\{0\}$.
Theorem 6 Prove that $\lim _{x \rightarrow 0} \frac{e^{x}-1}{x}=1$
Proof Using above inequality, we get

$$
\frac{1}{1+|x|} \leq \frac{e^{x}-1}{x} \leq 1+|x|(e-2), x \text { Î }[-1,1] \sim\{0\}
$$

Also $\quad \lim _{x \rightarrow 0} \frac{1}{1+|x|}=\frac{1}{1+\lim _{x \rightarrow 0}|x|}=\frac{1}{1+0}=1$
and $\quad \lim _{x \rightarrow 0}[1+(e-2)|x|]=1+(e-2) \lim _{x \rightarrow 0}|x|=1+(e-2) 0=1$
Therefore, by Sandwich theorem, we get

$$
\lim _{x \rightarrow 0} \frac{e^{x}-1}{x}=1
$$

Theorem 7 Prove that $\lim _{x \rightarrow 0} \frac{\log _{e}(1+x)}{x}=1$
Proof Let $\frac{\log _{e}(1+x)}{x}=y$. Then

$$
\begin{aligned}
& \log _{e}(1+x)=x y \\
& \Rightarrow 1+x=e^{x y} \\
& \Rightarrow \frac{e^{x y}-1}{x}=1 \\
& \frac{e^{x y}-1}{x y} \cdot y=1 \\
& \Rightarrow \lim _{x y \rightarrow 0} \frac{e^{x y}-1}{x y} \lim _{x \rightarrow 0} y=1(\text { since } x \rightarrow 0 \text { gives } x y \rightarrow 0) \\
& \Rightarrow \lim _{x \rightarrow 0} y=1\left(\text { as } \lim _{x y \rightarrow 0} \frac{e^{x y}-1}{x y}=1\right) \\
& \Rightarrow \lim _{x \rightarrow 0} \frac{\log _{e}(1+x)}{x}=1
\end{aligned}
$$

or

Example 5 Compute $\lim _{x \rightarrow 0} \frac{e^{3 x}-1}{x}$
Solution We have

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{e^{3 x}-1}{x}=\lim _{3 x \rightarrow 0} \frac{e^{3 x}-1}{3 x} \cdot 3 \\
& =3\left(\lim _{y \rightarrow 0} \frac{e^{y}-1}{y}\right), \quad \text { where } y=3 x \\
& =3.1=3
\end{aligned}
$$

Example 6 Compute $\lim _{x \rightarrow 0} \frac{e^{x}-\sin x-1}{x}$
Solution We have $\lim _{x \rightarrow 0} \frac{e^{x}-\sin x-1}{x}=\lim _{x \rightarrow 0}\left[\frac{e^{x}-1}{x}-\frac{\sin x}{x}\right]$

$$
=\lim _{x \rightarrow 0} \frac{e^{x}-1}{x}-\lim _{x \rightarrow 0} \frac{\sin x}{x}=1-1=0
$$

Example 7 Evaluate $\lim _{x \rightarrow 1} \frac{\log _{e} x}{x-1}$
Solution Put $x=1+h$, then as $x \rightarrow 1 \Rightarrow h \rightarrow 0$. Therefore,

$$
\lim _{x \rightarrow 1} \frac{\log _{e} x}{x-1}=\lim _{h \rightarrow 0} \frac{\log _{e}(1+h)}{h}=1\left(\text { since } \lim _{x \rightarrow 0} \frac{\log _{e}(1+x)}{x}=1\right)
$$

## Exercise 13.2

Evaluate the following limits, if exist

1. $\lim _{x \rightarrow 0} \frac{e^{4 x}-1}{x}$
(Ans. 4)
2. $\lim _{x \rightarrow 0} \frac{e^{2+x}-e^{2}}{x}$
3. $\lim _{x \rightarrow 5} \frac{e^{x}-e^{5}}{x-5}$
(Ans. $e^{5}$ ) 4. $\lim _{x \rightarrow 0} \frac{e^{\sin x}-1}{x}$
4. $\lim _{x \rightarrow 3} \frac{e^{x}-e^{3}}{x-3}$
(Ans. $e^{3}$ )
5. $\lim _{x \rightarrow 0} \frac{x\left(e^{x}-1\right)}{1-\cos x}$
6. $\lim _{x \rightarrow 0} \frac{\log _{e}(1+2 x)}{x}$
(Ans. 2)
7. $\lim _{x \rightarrow 0} \frac{\log \left(1+x^{3}\right)}{\sin ^{3} x}$
(Ans. $e^{2}$ )
(Ans. 1)
(Ans. 2)
(Ans. 1)

## Be a Student of Students

A teacher who establishes rapport with the taught, becomes one with them, learns more from them than he teaches them. He who learns nothing from his disciples is, in my opinion, worthless. Whenever I talk with someone I learn from him. I take from him more than I give him. In this way, a true teacher regards himself as a student of his students. If you will teach your pupils with this attitude, you will benefit much from them.

> Talk to Khadi Vidyalaya Students, Sevagram Harijan Seva, 15 February 1942 (CW 75, p. 269)

## Use All Resources to Be Constructive and Creative

What we need is educationists with originality, fired with true zeal, who will think out from day to day what they are going to teach their pupils. The teacher cannot get this knowledge through musty volumes. He has to use his own faculties of observation and thinking and impart his knowledge to the children through his lips, with the help of a craft. This means a revolution in the method of teaching, a revolution in the teachers' outlook. Up till now you have been guided by inspector's reports. You wanted to do what the inspector might like, so that you might get more money yet for your institutions or higher salaries for yourselves. But the new teacher will not care for all that. He will say, '1 have done my duty to my pupil if I have made him a better man and in doing so I have used all my resources. That is enough for me'.

Harijan, 18 February 1939 (CW 68, pp. 374-75)

