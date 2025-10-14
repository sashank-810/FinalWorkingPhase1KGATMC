## Mathematics is a most exact science and its conclusions are capable of absolute proofs．－C．P．STEINMETZ

## 7．1 Introduction

In earlier classes，we have learnt how to find the squares and cubes of binomials like $a+b$ and $a-b$ ．Using them，we could evaluate the numerical values of numbers like $(98)^{2}=(100-2)^{2},(999)^{3}=(1000-1)^{3}$ ，etc．However，for higher powers like $(98)^{5},(101)^{6}$ ，etc．，the calculations become difficult by using repeated multiplication．This difficulty was overcome by a theorem known as binomial theorem．It gives an easier way to expand $(a+b)^{n}$ ，where $n$ is an integer or a rational number．In this Chapter，we study binomial theorem for positive integral indices only．

## 7．2 Binomial Theorem for Positive Integral Indices

![](https://cdn.mathpix.com/cropped/2025_07_21_87825a85202fbc5bfefeg-1.jpg?height=577&width=392&top_left_y=834&top_left_x=1075)

Blaise Pascal
（1623－1662）

Let us have a look at the following identities done earlier：

$$
\begin{aligned}
& (a+b)^{0}=1 \quad a+b \neq 0 \\
& (a+b)^{1}=a+b \quad \\
& (a+b)^{2}=a^{2}+2 a b+b^{2} \\
& (a+b)^{3}=a^{3}+3 a^{2} b+3 a b^{2}+b^{3} \\
& (a+b)^{4}=(a+b)^{3}(a+b)=a^{4}+4 a^{3} b+6 a^{2} b^{2}+4 a b^{3}+b^{4}
\end{aligned}
$$

In these expansions，we observe that
（i）The total number of terms in the expansion is one more than the index．For example，in the expansion of $(a+b)^{2}$ ，number of terms is 3 whereas the index of $(a+b)^{2}$ is 2 ．
（ii）Powers of the first quantity＇$a$＇go on decreasing by 1 whereas the powers of the second quantity＇$b$＇increase by 1 ，in the successive terms．
（iii）In each term of the expansion，the sum of the indices of $a$ and $b$ is the same and is equal to the index of $a+b$ ．

We now arrange the coefficients in these expansions as follows (Fig 7.1):
![](https://cdn.mathpix.com/cropped/2025_07_21_87825a85202fbc5bfefeg-2.jpg?height=370&width=627&top_left_y=397&top_left_x=494)

Fig 7.1
Do we observe any pattern in this table that will help us to write the next row? Yes we do. It can be seen that the addition of 1's in the row for index 1 gives rise to 2 in the row for index 2. The addition of 1, 2 and 2, 1 in the row for index 2, gives rise to 3 and 3 in the row for index 3 and so on. Also, 1 is present at the beginning and at the end of each row. This can be continued till any index of our interest.

We can extend the pattern given in Fig 7.2 by writing a few more rows.
![](https://cdn.mathpix.com/cropped/2025_07_21_87825a85202fbc5bfefeg-2.jpg?height=410&width=794&top_left_y=1117&top_left_x=429)

Fig 7.2

## Pascal's Triangle

The structure given in Fig 7.2 looks like a triangle with 1 at the top vertex and running down the two slanting sides. This array of numbers is known as Pascal's triangle, after the name of French mathematician Blaise Pascal. It is also known as Meru Prastara by Pingla.

Expansions for the higher powers of a binomial are also possible by using Pascal's triangle. Let us expand $(2 x+3 y)^{5}$ by using Pascal's triangle. The row for index 5 is

$$
\begin{array}{llllll}
1 & 5 & 10 & 10 & 5 & 1
\end{array}
$$

Using this row and our observations (i), (ii) and (iii), we get

$$
\begin{aligned}
(2 x+3 y)^{5} & =(2 x)^{5}+5(2 x)^{4}(3 y)+10(2 x)^{3}(3 y)^{2}+10(2 x)^{2}(3 y)^{3}+5(2 x)(3 y)^{4}+(3 y)^{5} \\
& =32 x^{5}+240 x^{4} y+720 x^{3} y^{2}+1080 x^{2} y^{3}+810 x y^{4}+243 y^{5}
\end{aligned}
$$

Now, if we want to find the expansion of $(2 x+3 y)^{12}$, we are first required to get the row for index 12. This can be done by writing all the rows of the Pascal's triangle till index 12. This is a slightly lengthy process. The process, as you observe, will become more difficult, if we need the expansions involving still larger powers.

We thus try to find a rule that will help us to find the expansion of the binomial for any power without writing all the rows of the Pascal's triangle, that come before the row of the desired index.

For this, we make use of the concept of combinations studied earlier to rewrite the numbers in the Pascal's triangle. We know that ${ }^{n} \mathrm{C}_{r}=\frac{n!}{r!(n-r)!}, 0 \leq r \leq n$ and $n$ is a non-negative integer. Also, $\quad{ }^{n} \mathrm{C}_{0}=1={ }^{n} \mathrm{C}_{n}$.
The Pascal's triangle can now be rewritten as (Fig 7.3)

| Index | Coefficients |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 |  |  | $\begin{aligned} & { }^{0} \mathrm{C}_{0} \\ & (=1) \end{aligned}$ |  |  |  |  |
| 1 |  |  | $\begin{aligned} & { }^{1} \mathrm{C}_{0} \\ & (=1) \end{aligned}$ | $\begin{aligned} & { }^{1} \mathrm{C}_{1} \\ & (=1) \end{aligned}$ |  |  |  |
| 2 |  | $\begin{aligned} & { }^{2} \mathrm{C}_{0} \\ & (=1) \end{aligned}$ | $\begin{aligned} & { }^{2} \mathrm{C}_{1} \\ & (=2) \end{aligned}$ | $\begin{aligned} & { }^{2} \mathrm{C}_{2} \\ & (=1) \end{aligned}$ |  |  |  |
| 3 |  | $\begin{gathered} { }^{3} \mathrm{C}_{0} \\ (=1) \end{gathered}$ | ${ }^{3} \mathrm{C}_{1}$ (=3) |  | $\begin{aligned} & { }^{3} \mathrm{C}_{3} \\ & (=1) \end{aligned}$ |  |  |
| 4 | $\begin{aligned} & { }^{4} \mathrm{C}_{0} \\ & (=1) \end{aligned}$ | ${ }^{4} \mathrm{C}_{1}$ $(=4)$ | $\begin{gathered} { }^{4} \mathrm{C}_{2} \\ (=6) \end{gathered}$ | $\begin{gathered} { }^{4} \mathrm{C}_{3} \\ (=4) \end{gathered}$ |  | $\begin{gathered} { }^{4} C_{4} \\ (=1) \end{gathered}$ |  |
| 5 | $\begin{gathered} { }^{5} \mathrm{C}_{0} \\ (=1) \end{gathered}$ | ${ }^{5} \mathrm{C}_{1}$ $(=5)$ | ${ }^{5} \mathrm{C}_{2}$ (=10) | ${ }^{5} \mathrm{C}_{3}$ (=10) | ${ }^{5} \mathrm{C}_{4}$ (=5) |  | ${ }^{5} \mathrm{C}_{5}$ (=1) |

Fig 7.3 Pascal's triangle
Observing this pattern, we can now write the row of the Pascal's triangle for any index without writing the earlier rows. For example, for the index 7 the row would be

$$
\begin{array}{lllllllll}
{ }^{7} \mathrm{C}_{0} & { }^{7} \mathrm{C}_{1} & { }^{7} \mathrm{C}_{2} & { }^{7} \mathrm{C}_{3} & { }^{7} \mathrm{C}_{4} & { }^{7} \mathrm{C}_{5} & { }^{7} \mathrm{C}_{6} & { }^{7} \mathrm{C}_{7} .
\end{array}
$$

Thus, using this row and the observations (i), (ii) and (iii), we have $(a+b)^{7}={ }^{7} \mathrm{C}_{0} a^{7}+7 \mathrm{C}_{1} a^{6} b+{ }^{7} \mathrm{C}_{2} a^{5} b^{2}+{ }^{7} \mathrm{C}_{3} a^{4} b^{3}+7 \mathrm{C}_{4} a^{3} b^{4}+{ }^{7} \mathrm{C}_{5} a^{2} b^{5}+{ }^{7} \mathrm{C}_{6} a b^{6}+{ }^{7} \mathrm{C}_{7} b^{7}$
An expansion of a binomial to any positive integral index say $n$ can now be visualised using these observations. We are now in a position to write the expansion of a binomial to any positive integral index.
7.2.1 Binomial theorem for any positive integer $n$,

$$
(a+b)^{n}={ }^{n} \mathrm{C}_{0} a^{n}+{ }^{n} \mathrm{C}_{1} a^{n-1} b+{ }^{n} \mathrm{C}_{2} a^{n-2} b^{2}+\ldots+{ }^{n} \mathrm{C}_{n-1} a \cdot b^{n-1}+{ }^{n} \mathrm{C}_{n} b^{n}
$$

Proof The proof is obtained by applying principle of mathematical induction.
Let the given statement be

$$
\mathrm{P}(n):(a+b)^{n}={ }^{n} \mathrm{C}_{0} a^{n}+{ }^{n} \mathrm{C}_{1} a^{n-1} b+{ }^{n} \mathrm{C}_{2} a^{n-2} b^{2}+\ldots+{ }^{n} \mathrm{C}_{n-1} a \cdot b^{n-1}+{ }^{n} \mathrm{C}_{n} b^{n}
$$

For $n=1$, we have

$$
\mathrm{P}(1):(a+b)^{1}={ }^{1} \mathrm{C}_{0} a^{1}+{ }^{1} \mathrm{C}_{1} b^{1}=a+b
$$

Thus, $\mathrm{P}(1)$ is true.
Suppose $\mathrm{P}(k)$ is true for some positive integer $k$, i.e.

$$
\begin{equation*}
(a+b)^{k}={ }^{k} \mathrm{C}_{0} a^{k}+{ }^{k} \mathrm{C}_{1} a^{k-1} b+{ }^{k} \mathrm{C}_{2} a^{k-2} b^{2}+\ldots+{ }^{k} \mathrm{C}_{k} b^{k} \tag{1}
\end{equation*}
$$

We shall prove that $\mathrm{P}(k+1)$ is also true, i.e.,

$$
(a+b)^{k+1}={ }^{k+1} \mathrm{C}_{0} a^{k+1}+{ }^{k+1} \mathrm{C}_{1} a^{k} b+{ }^{k+1} \mathrm{C}_{2} a^{k-1} b^{2}+\ldots+{ }^{k+1} \mathrm{C}_{k+1} b^{k+1}
$$

Now, $(a+b)^{k+1}=(a+b)(a+b)^{k}$

$$
\begin{align*}
= & (a+b)\left({ }^{k} \mathrm{C}_{0} a^{k}+{ }^{k} \mathrm{C}_{1} a^{k-1} b+{ }^{k} \mathrm{C}_{2} a^{k-2} b^{2}+\ldots+{ }^{k} \mathrm{C}_{k-1} a b^{k-1}+{ }^{k} \mathrm{C}_{k} b^{k}\right)  \tag{1}\\
= & \quad[\operatorname{from}(1)] \\
= & { }^{k} \mathrm{C}_{0} a^{k+1}+{ }^{k} \mathrm{C}_{1} a^{k} b+{ }^{k} \mathrm{C}_{2} a^{k-1} b^{2}+\ldots+{ }^{k} \mathrm{C}_{k-1} a^{2} b^{k-1}+{ }^{k} \mathrm{C}_{k} a b^{k}+{ }^{k} \mathrm{C}_{0} a^{k} b \\
& +{ }^{k} \mathrm{C}_{1} a^{k-1} b^{2}+{ }^{k} \mathrm{C}_{2} a^{k-2} b^{3}+\ldots+{ }^{k} \mathrm{C}_{k-1} a b^{k}+{ }^{k} \mathrm{C}_{k} b^{k+1}
\end{align*}
$$

[by actual multiplication]

$$
\begin{aligned}
= & { }^{k} \mathrm{C}_{0} a^{k+1}+\left({ }^{k} \mathrm{C}_{1}+{ }^{k} \mathrm{C}_{0}\right) a^{k} b+\left({ }^{k} \mathrm{C}_{2}+{ }^{k} \mathrm{C}_{1}\right) a^{k-1} b^{2}+\ldots \\
& +\left({ }^{k} \mathrm{C}_{k}+{ }^{k} \mathrm{C}_{k-1}\right) a b^{k}+{ }^{k} \mathrm{C}_{k} b^{k+1} \quad \text { [grouping like terms] } \\
= & { }^{k+1} \mathrm{C}_{0} a^{k+1}+{ }^{k+1} \mathrm{C}_{1} a^{k} b+{ }^{k+1} \mathrm{C}_{2} a^{k-1} \mathrm{~b}^{2}+\ldots+{ }^{k+1} \mathrm{C}_{k} a b^{k+}{ }^{k+1} \mathrm{C}_{k+1} b^{k+1}
\end{aligned}
$$

(by using ${ }^{k+1} \mathrm{C}_{0}=1,{ }^{k} \mathrm{C}_{r}+{ }^{k} \mathrm{C}_{r-1}={ }^{k+1} \mathrm{C}_{r} \quad$ and ${ }^{k} \mathrm{C}_{k}=1={ }^{k+1} \mathrm{C}_{k+1}$ )
Thus, it has been proved that $\mathrm{P}(k+1)$ is true whenever $\mathrm{P}(k)$ is true. Therefore, by principle of mathematical induction, $\mathrm{P}(n)$ is true for every positive integer $n$.

We illustrate this theorem by expanding $(x+2)^{6}$ :

$$
\begin{aligned}
(x+2)^{6} & ={ }^{6} \mathrm{C}_{0} x^{6}+{ }^{6} \mathrm{C}_{1} x^{5} \cdot 2+{ }^{6} \mathrm{C}_{2} x^{4} 2^{2}+{ }^{6} \mathrm{C}_{3} x^{3} \cdot 2^{3}+{ }^{6} \mathrm{C}_{4} x^{2} \cdot 2^{4}+{ }^{6} \mathrm{C}_{5} x \cdot 2^{5}+{ }^{6} \mathrm{C}_{6} \cdot 2^{6} . \\
& =x^{6}+12 x^{5}+60 x^{4}+160 x^{3}+240 x^{2}+192 x+64
\end{aligned}
$$

Thus $(x+2)^{6}=x^{6}+12 x^{5}+60 x^{4}+160 x^{3}+240 x^{2}+192 x+64$.

## Observations

1. The notation $\sum_{k=0}^{n}{ }^{n} \mathrm{C}_{k} a^{n-k} b^{k}$ stands for
${ }^{n} \mathrm{C}_{0} a^{n} b^{0}+{ }^{n} \mathrm{C}_{1} a^{n-1} b^{1}+\ldots+{ }^{n} \mathrm{C}_{\mathrm{r}} a^{n-r} b^{r}+\ldots+{ }^{n} \mathrm{C}_{n} a^{n-n} b^{n}$, where $b^{0}=1=a^{n-n}$.
Hence the theorem can also be stated as

$$
(a+b)^{n}=\sum_{k=0}^{n}{ }^{n} \mathrm{C}_{k} a^{n-k} b^{k}
$$

2. The coefficients ${ }^{n} \mathrm{C}_{r}$ occuring in the binomial theorem are known as binomial coefficients.
3. There are $(n+1)$ terms in the expansion of $(a+b)^{n}$, i.e., one more than the index.
4. In the successive terms of the expansion the index of $a$ goes on decreasing by unity. It is $n$ in the first term, ( $n-1$ ) in the second term, and so on ending with zero in the last term. At the same time the index of $b$ increases by unity, starting with zero in the first term, 1 in the second and so on ending with $n$ in the last term.
5. In the expansion of $(a+b)^{n}$, the sum of the indices of $a$ and $b$ is $n+0=n$ in the first term, $(n-1)+1=n$ in the second term and so on $0+n=n$ in the last term. Thus, it can be seen that the sum of the indices of $a$ and $b$ is $n$ in every term of the expansion.
7.2.2 Some special cases In the expansion of $(a+b)^{n}$,
(i) Taking $a=x$ and $b=-y$, we obtain

$$
\begin{aligned}
(x-y)^{n} & =[x+(-y)]^{n} \\
& ={ }^{n} \mathrm{C}_{0} x^{n}+{ }^{n} \mathrm{C}_{1} x^{n-1}(-y)+{ }^{n} \mathrm{C}_{2} x^{n-2}(-y)^{2}+{ }^{n} \mathrm{C}_{3} x^{n-3}(-y)^{3}+\ldots+{ }^{n} \mathrm{C}_{n}(-y)^{n} \\
& ={ }^{n} \mathrm{C}_{0} x^{n}-{ }^{n} \mathrm{C}_{1} x^{n-1} y+{ }^{n} \mathrm{C}_{2} x^{n-2} y^{2}-{ }^{n} \mathrm{C}_{3} x^{n-3} y^{3}+\ldots+(-1)^{n}{ }^{n} \mathrm{C}_{n} y^{n}
\end{aligned}
$$

Thus $(x-y)^{n}={ }^{n} \mathrm{C}_{0} x^{n}-{ }^{n} \mathrm{C}_{1} x^{n-1} y+{ }^{n} \mathrm{C}_{2} x^{n-2} y^{2}+\ldots+(-1)^{n}{ }^{n} \mathrm{C}_{n} y^{n}$
Using this, we have $\quad(x-2 y)^{5}={ }^{5} \mathrm{C}_{0} x^{5}-{ }^{5} \mathrm{C}_{1} x^{4}(2 y)+{ }^{5} \mathrm{C}_{2} x^{3}(2 y)^{2}-{ }^{5} \mathrm{C}_{3} x^{2}(2 y)^{3}+$

$$
\begin{aligned}
& { }^{5} \mathrm{C}_{4} x(2 y)^{4}-{ }^{5} \mathrm{C}_{5}(2 y)^{5} \\
= & x^{5}-10 x^{4} \mathrm{y}+40 x^{3} y^{2}-80 x^{2} y^{3}+80 x y^{4}-32 y^{5} .
\end{aligned}
$$

(ii) Taking $a=1, b=x$, we obtain

$$
\begin{gathered}
(1+x)^{n}={ }^{n} \mathrm{C}_{0}(1)^{n}+{ }^{n} \mathrm{C}_{1}(1)^{n-1} x+{ }^{n} \mathrm{C}_{2}(1)^{n-2} x^{2}+\ldots+{ }^{n} \mathrm{C}_{n} x^{n} \\
={ }^{n} \mathrm{C}_{0}+{ }^{n} \mathrm{C}_{1} x+{ }^{n} \mathrm{C}_{2} x^{2}+{ }^{n} \mathrm{C}_{3} x^{3}+\ldots+{ }^{n} \mathrm{C}_{n} x^{n}
\end{gathered}
$$

Thus

$$
(1+x)^{n}={ }^{n} \mathrm{C}_{0}+{ }^{n} \mathrm{C}_{1} x+{ }^{n} \mathrm{C}_{2} x^{2}+{ }^{n} \mathrm{C}_{3} x^{3}+\ldots+{ }^{n} \mathrm{C}_{n} x^{n}
$$

In particular, for $x=1$, we have

$$
2^{n}={ }^{n} \mathrm{C}_{0}+{ }^{n} \mathrm{C}_{1}+{ }^{n} \mathrm{C}_{2}+\ldots+{ }^{n} \mathrm{C}_{n}
$$

(iii) Taking $a=1, b=-x$, we obtain

$$
(1-x)^{n}={ }^{n} \mathrm{C}_{0}-{ }^{n} \mathrm{C}_{1} x+{ }^{n} \mathrm{C}_{2} x^{2}-\ldots+(-1)^{n}{ }^{n} \mathrm{C}_{n} x^{n}
$$

In particular, for $x=1$, we get

$$
0={ }^{n} \mathrm{C}_{0}-{ }^{n} \mathrm{C}_{1}+{ }^{n} \mathrm{C}_{2}-\ldots+(-1)^{n}{ }^{n} \mathrm{C}_{n}
$$

Example 1 Expand $\left(x^{2}+\frac{3}{x}\right)^{4}, x \neq 0$
Solution By using binomial theorem, we have

$$
\begin{aligned}
x^{2}+\frac{3^{4}}{x} & ={ }^{4} \mathrm{C}_{0}\left(x^{2}\right)^{4}+{ }^{4} \mathrm{C}_{1}\left(x^{2}\right)^{3}\left(\frac{3}{x}\right)+{ }^{4} \mathrm{C}_{2}\left(x^{2}\right)^{2}\left(\frac{3}{x}\right)^{2}+{ }^{4} \mathrm{C}_{3}\left(x^{2}\right)\left(\frac{3}{x}\right)^{3}+{ }^{4} \mathrm{C}_{4}\left(\frac{3}{x}\right)^{4} \\
& =x^{8}+4 \cdot x^{6} \cdot \frac{3}{x}+6 \cdot x^{4} \cdot \frac{9}{x^{2}}+4 \cdot x^{2} \cdot \frac{27}{x^{3}}+\frac{81}{x^{4}} \\
& =x^{8}+12 x^{5}+54 x^{2}+\frac{108}{x}+\frac{81}{x^{4}}
\end{aligned}
$$

## Example 2 Compute (98) ${ }^{5}$.

Solution We express 98 as the sum or difference of two numbers whose powers are easier to calculate, and then use Binomial Theorem.
Write $98=100-2$
Therefore, $(98)^{5}=(100-2)^{5}$

$$
\begin{aligned}
= & { }^{5} \mathrm{C}_{0}(100)^{5}-{ }^{5} \mathrm{C}_{1}(100)^{4} \cdot 2+{ }^{5} \mathrm{C}_{2}(100)^{3} 2^{2} \\
& -{ }^{5} \mathrm{C}_{3}(100)^{2}(2)^{3}+{ }^{5} \mathrm{C}_{4}(100)(2)^{4}-{ }^{5} \mathrm{C}_{5}(2)^{5} \\
= & 10000000000-5 \times 100000000 \times 2+10 \times 1000000 \times 4-10 \times 10000 \\
& \times 8+5 \times 100 \times 16-32 \\
= & 10040008000-1000800032=9039207968
\end{aligned}
$$

Example 3 Which is larger $(1.01)^{1000000}$ or 10,000 ?
Solution Splitting 1.01 and using binomial theorem to write the first few terms we have

$$
\begin{aligned}
(1.01)^{1000000} & =(1+0.01)^{1000000} \\
& ={ }^{1000000} \mathrm{C}_{0}+{ }^{1000000} \mathrm{C}_{1}(0.01)+\text { other positive terms } \\
& =1+1000000 \times 0.01+\text { other positive terms } \\
& =1+10000+\text { other positive terms } \\
& \quad>10000
\end{aligned}
$$

Hence $\quad(1.01)^{1000000}>10000$
Example 4 Using binomial theorem, prove that $6^{n}-5 n$ always leaves remainder 1 when divided by 25 .

Solution For two numbers $a$ and $b$ if we can find numbers $q$ and $r$ such that $a=b q+r$, then we say that $b$ divides $a$ with $q$ as quotient and $r$ as remainder. Thus, in order to show that $6^{n}-5 n$ leaves remainder 1 when divided by 25 , we prove that $6^{n}-5 n=25 k+1$, where $k$ is some natural number.

We have

$$
(1+a)^{n}={ }^{n} \mathrm{C}_{0}+{ }^{n} \mathrm{C}_{1} a+{ }^{n} \mathrm{C}_{2} a^{2}+\ldots+{ }^{n} \mathrm{C}_{n} a^{n}
$$

For $a \quad=5$, we get

$$
(1+5)^{n}={ }^{n} \mathrm{C}_{0}+{ }^{n} \mathrm{C}_{1} 5+{ }^{n} \mathrm{C}_{2} 5^{2}+\ldots+{ }^{n} \mathrm{C}_{n} 5^{n}
$$

i.e.

$$
(6)^{n}=1+5 n+5^{2} \cdot{ }^{n} \mathrm{C}_{2}+5^{3} \cdot{ }^{n} \mathrm{C}_{3}+\ldots+5^{n}
$$

i.e.

$$
6^{n}-5 n=1+5^{2}\left({ }^{n} \mathrm{C}_{2}+{ }^{n} \mathrm{C}_{3} 5+\ldots+5^{n-2}\right)
$$

or

$$
6^{n}-5 n=1+25\left({ }^{n} \mathrm{C}_{2}+5 \cdot{ }^{n} \mathrm{C}_{3}+\ldots+5^{n-2}\right)
$$

or

$$
6^{n}-5 n=25 k+1 \quad \text { where } k={ }^{n} \mathrm{C}_{2}+5 \cdot{ }^{n} \mathrm{C}_{3}+\ldots+5^{n-2}
$$

This shows that when divided by $25,6^{n}-5 n$ leaves remainder 1 .

## EXERCISE 7.1

Expand each of the expressions in Exercises 1 to 5.

1. $(1-2 x)^{5}$
2. $\left(\frac{2}{x}-\frac{x}{2}\right)^{5}$
3. $(2 x-3)^{6}$
4. $\left(\frac{x}{3}+\frac{1}{x}\right)^{5}$
5. $\left(x+\frac{1}{x}\right)^{6}$

Using binomial theorem, evaluate each of the following:
6. $(96)^{3}$
7. $(102)^{5}$
8. $(101)^{4}$
9. $(99)^{5}$
10. Using Binomial Theorem, indicate which number is larger $(1.1)^{10000}$ or 1000.
11. Find $(a+b)^{4}-(a-b)^{4}$. Hence, evaluate $(\sqrt{3}+\sqrt{2})^{4}-(\sqrt{3}-\sqrt{2})^{4}$.
12. Find $(x+1)^{6}+(x-1)^{6}$. Hence or otherwise evaluate $(\sqrt{2}+1)^{6}+(\sqrt{2}-1)^{6}$.
13. Show that $9^{n+1}-8 n-9$ is divisible by 64 , whenever $n$ is a positive integer.
14. Prove that $\sum_{r=0}^{n} 3^{r}{ }^{n} \mathrm{C}_{r}=4^{n}$.

## Miscellaneous Exercise on Chapter 7

1. If $a$ and $b$ are distinct integers, prove that $a-b$ is a factor of $a^{n}-b^{n}$, whenever $n$ is a positive integer.
[Hint write $a^{n}=(a-b+b)^{n}$ and expand]
2. Evaluate $(\sqrt{3}+\sqrt{2})^{6}-(\sqrt{3}-\sqrt{2})^{6}$.
3. Find the value of $\left(a^{2}+\sqrt{a^{2}-1}\right)^{4}+\left(a^{2}-\sqrt{a^{2}-1}\right)^{4}$.
4. Find an approximation of $(0.99)^{5}$ using the first three terms of its expansion.
5. Expand using Binomial Theorem $\left(1+\frac{x}{2}-\frac{2}{x}\right)^{4}, x \neq 0$.
6. Find the expansion of $\left(3 x^{2}-2 a x+3 a^{2}\right)^{3}$ using binomial theorem.

## Summary

- The expansion of a binomial for any positive integral $n$ is given by Binomial Theorem, which is $(a+b)^{n}={ }^{n} \mathrm{C}_{0} a^{n}+{ }^{n} \mathrm{C}_{1} a^{n-1} b+{ }^{n} \mathrm{C}_{2} a^{n-2} b^{2}+\ldots+$ ${ }^{n} \mathrm{C}_{n-1} a \cdot b^{n-1}+{ }^{n} \mathrm{C}_{n} b^{n}$.
- The coefficients of the expansions are arranged in an array. This array is called Pascal's triangle.


## Historical Note

The ancient Indian mathematicians knew about the coefficients in the expansions of $(x+y)^{n}, 0 \leq n \leq 7$. The arrangement of these coefficients was in the form of a diagram called Meru-Prastara, provided by Pingla in his book Chhanda shastra (200B.C.). This triangular arrangement is also found in the work of Chinese mathematician Chu-shi-kie in 1303. The term binomial coefficients was first introduced by the German mathematician, Michael Stipel (1486-1567) in approximately 1544. Bombelli (1572) also gave the coefficients in the expansion of $(a+b)^{n}$, for $n=1,2 \ldots, 7$ and Oughtred (1631) gave them for $n=1,2, \ldots, 10$. The arithmetic triangle, popularly known as Pascal's triangle and similar to the MeruPrastara of Pingla was constructed by the French mathematician Blaise Pascal (1623-1662) in 1665.

The present form of the binomial theorem for integral values of $n$ appeared in Trate du triange arithmetic, written by Pascal and published posthumously in 1665.

