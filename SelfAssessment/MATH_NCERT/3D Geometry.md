## Chapter 11

## THREE DIMENSIONAL GEOMETRY

The moving power of mathematical invention is not reasoning but imagination．－A．DEMORGAN

## 11．1 Introduction

In Class XI，while studying Analytical Geometry in two dimensions，and the introduction to three dimensional geometry，we confined to the Cartesian methods only．In the previous chapter of this book，we have studied some basic concepts of vectors．We will now use vector algebra to three dimensional geometry．The purpose of this approach to 3 －dimensional geometry is that it makes the study simple and elegant＊．

In this chapter，we shall study the direction cosines and direction ratios of a line joining two points and also discuss about the equations of lines and planes in space under different conditions，angle between two lines，two planes，a line and a plane，shortest distance between two skew lines and distance of a point from a plane．Most of
![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-01.jpg?height=543&width=415&top_left_y=814&top_left_x=990)

Leonhard Euler
（1707－1783） the above results are obtained in vector form．Nevertheless，we shall also translate these results in the Cartesian form which，at times，presents a more clear geometric and analytic picture of the situation．

## 11．2 Direction Cosines and Direction Ratios of a Line

From Chapter 10，recall that if a directed line L passing through the origin makes angles $\alpha, \beta$ and $\gamma$ with $x, y$ and $z$－axes，respectively，called direction angles，then cosine of these angles，namely， $\cos \alpha, \cos \beta$ and $\cos \gamma$ are called direction cosines of the directed line L ．

If we reverse the direction of L ，then the direction angles are replaced by their supplements， i．e．，$\pi-\alpha, \pi-\beta$ and $\pi-\gamma$ ．Thus，the signs of the direction cosines are reversed．

[^0]![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-02.jpg?height=654&width=478&top_left_y=262&top_left_x=482)

Fig 11.1
Note that a given line in space can be extended in two opposite directions and so it has two sets of direction cosines. In order to have a unique set of direction cosines for a given line in space, we must take the given line as a directed line. These unique direction cosines are denoted by $l, m$ and $n$.
Remark If the given line in space does not pass through the origin, then, in order to find its direction cosines, we draw a line through the origin and parallel to the given line. Now take one of the directed lines from the origin and find its direction cosines as two parallel line have same set of direction cosines.

Any three numbers which are proportional to the direction cosines of a line are called the direction ratios of the line. If $l, m, n$ are direction cosines and $a, b, c$ are direction ratios of a line, then $a=\lambda l, b=\lambda m$ and $c=\lambda n$, for any nonzero $\lambda \in \mathbf{R}$.

Note Some authors also call direction ratios as direction numbers.
Let $a, b, c$ be direction ratios of a line and let $l, m$ and $n$ be the direction cosines (d.c's) of the line. Then

Therefore

$$
\frac{l}{a}=\frac{m}{b}=\frac{n}{c}=k \text { (say), } k \text { being a constant. }
$$

But

$$
\begin{equation*}
l=a k, m=b k, n=c k \tag{1}
\end{equation*}
$$

Therefore

$$
l^{2}+m^{2}+n^{2}=1
$$

$$
k^{2}\left(a^{2}+b^{2}+c^{2}\right)=1
$$

or

$$
k= \pm \frac{1}{\sqrt{a^{2}+b^{2}+c^{2}}}
$$

Hence, from (1), the d.c.'s of the line are

$$
l= \pm \frac{a}{\sqrt{a^{2}+b^{2}+c^{2}}}, m= \pm \frac{b}{\sqrt{a^{2}+b^{2}+c^{2}}}, n= \pm \frac{c}{\sqrt{a^{2}+b^{2}+c^{2}}}
$$

where, depending on the desired sign of $k$, either a positive or a negative sign is to be taken for $l, m$ and $n$.

For any line, if $a, b, c$ are direction ratios of a line, then $k a, k b, k c ; k \neq 0$ is also a set of direction ratios. So, any two sets of direction ratios of a line are also proportional. Also, for any line there are infinitely many sets of direction ratios.

### 11.2.1 Direction cosines of a line passing through two points

Since one and only one line passes through two given points, we can determine the direction cosines of a line passing through the given points $\mathrm{P}\left(x_{1}, y_{1}, z_{1}\right)$ and $\mathrm{Q}\left(x_{2}, y_{2}, z_{2}\right)$ as follows (Fig 11.2 (a)).
![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-03.jpg?height=492&width=1077&top_left_y=914&top_left_x=213)

Fig 11.2
Let $l, m, n$ be the direction cosines of the line PQ and let it makes angles $\alpha, \beta$ and $\gamma$ with the $x, y$ and $z$-axis, respectively.

Draw perpendiculars from P and Q to XY -plane to meet at R and S . Draw a perpendicular from P to QS to meet at N . Now, in right angle triangle $\mathrm{PNQ}, \angle \mathrm{PQN}=\gamma$ (Fig 11.2 (b).

Therefore,

$$
\cos \gamma=\frac{\mathrm{NQ}}{\mathrm{PQ}}=\frac{z_{2}-z_{1}}{\mathrm{PQ}}
$$

Similarly

$$
\cos \alpha=\frac{x_{2}-x_{1}}{\mathrm{PQ}} \text { and } \cos \beta=\frac{y_{2}-y_{1}}{\mathrm{PQ}}
$$

Hence, the direction cosines of the line segment joining the points $\mathrm{P}\left(x_{1}, y_{1}, z_{1}\right)$ and $\mathrm{Q}\left(x_{2}, y_{2}, z_{2}\right)$ are
where

$$
\begin{gathered}
\frac{x_{2}-x_{1}}{\mathrm{PQ}}, \frac{y_{2}-y_{1}}{\mathrm{PQ}}, \frac{z_{2}-z_{1}}{\mathrm{PQ}} \\
\mathrm{PQ}=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
\end{gathered}
$$

Note The direction ratios of the line segment joining $\mathrm{P}\left(x_{1}, y_{1}, z_{1}\right)$ and $\mathrm{Q}\left(x_{2}, y_{2}, z_{2}\right)$ may be taken as

$$
x_{2}-x_{1}, y_{2}-y_{1}, z_{2}-z_{1} \text { or } x_{1}-x_{2}, y_{1}-y_{2}, z_{1}-z_{2}
$$

Example 1 If a line makes angle $90^{\circ}, 60^{\circ}$ and $30^{\circ}$ with the positive direction of $x, y$ and $z$-axis respectively, find its direction cosines.
Solution Let the d.c.'s of the lines be $l, m, n$. Then $l=\cos 90^{\circ}=0, m=\cos 60^{\circ}=\frac{1}{2}$, $n=\cos 30^{\circ}=\frac{\sqrt{3}}{2}$.
Example 2 If a line has direction ratios $2,-1,-2$, determine its direction cosines.
Solution Direction cosines are

$$
\frac{2}{\sqrt{2^{2}+(-1)^{2}+(-2)^{2}}}, \frac{-1}{\sqrt{2^{2}+(-1)^{2}+(-2)^{2}}}, \frac{-2}{\sqrt{2^{2}+(-1)^{2}+(-2)^{2}}}
$$

or $\quad \frac{2}{3}, \frac{-1}{3}, \frac{-2}{3}$
Example 3 Find the direction cosines of the line passing through the two points ( $-2,4,-5$ ) and ( $1,2,3$ ).
Solution We know the direction cosines of the line passing through two points $\mathrm{P}\left(x_{1}, y_{1}, z_{1}\right)$ and $\mathrm{Q}\left(x_{2}, y_{2}, z_{2}\right)$ are given by
where

$$
\begin{aligned}
& \frac{x_{2}-x_{1}}{\mathrm{PQ}}, \frac{y_{2}-y_{1}}{\mathrm{PQ}}, \frac{z_{2}-z_{1}}{\mathrm{PQ}} \\
& \mathrm{PQ}=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
\end{aligned}
$$

Here P is $(-2,4,-5)$ and Q is $(1,2,3)$.
So

$$
\mathrm{PQ}=\sqrt{(1-(-2))^{2}+(2-4)^{2}+(3-(-5))^{2}}=\sqrt{77}
$$

Thus, the direction cosines of the line joining two points is

$$
\frac{3}{\sqrt{77}}, \frac{-2}{\sqrt{77}}, \frac{8}{\sqrt{77}}
$$

Example 4 Find the direction cosines of $x, y$ and $z$-axis.
Solution The $x$-axis makes angles $0^{\circ}, 90^{\circ}$ and $90^{\circ}$ respectively with $x, y$ and $z$-axis. Therefore, the direction cosines of $x$-axis are $\cos 0^{\circ}, \cos 90^{\circ}, \cos 90^{\circ}$ i.e., $1,0,0$.
Similarly, direction cosines of $y$-axis and $z$-axis are $0,1,0$ and $0,0,1$ respectively.
Example 5 Show that the points $\mathrm{A}(2,3,-4), \mathrm{B}(1,-2,3)$ and $\mathrm{C}(3,8,-11)$ are collinear.
Solution Direction ratios of line joining $A$ and $B$ are
$1-2,-2-3,3+4$ i.e., $-1,-5,7$.
The direction ratios of line joining $B$ and $C$ are
$3-1,8+2,-11-3$, i.e., $2,10,-14$.
It is clear that direction ratios of $A B$ and $B C$ are proportional, hence, $A B$ is parallel to BC . But point B is common to both AB and BC . Therefore, $\mathrm{A}, \mathrm{B}, \mathrm{C}$ are collinear points.

## EXERCISE 11.1

1. If a line makes angles $90^{\circ}, 135^{\circ}, 45^{\circ}$ with the $x, y$ and $z$-axes respectively, find its direction cosines.
2. Find the direction cosines of a line which makes equal angles with the coordinate axes.
3. If a line has the direction ratios $-18,12,-4$, then what are its direction cosines ?
4. Show that the points $(2,3,4),(-1,-2,1),(5,8,7)$ are collinear.
5. Find the direction cosines of the sides of the triangle whose vertices are $(3,5,-4),(-1,1,2)$ and $(-5,-5,-2)$.

### 11.3 Equation of a Line in Space

We have studied equation of lines in two dimensions in Class XI, we shall now study the vector and cartesian equations of a line in space.

A line is uniquely determined if
(i) it passes through a given point and has given direction, or
(ii) it passes through two given points.
11.3.1 Equation of a line through a given point and parallel to $\vec{a}$ given vector $\vec{b}$ Let $\vec{a}$ be the position vector of the given point A with respect to the origin O of the rectangular coordinate system. Let $l$ be the line which passes through the point A and is parallel to a given vector $\vec{b}$. Let $\vec{r}$ be the position vector of an arbitrary point P on the line (Fig 11.3).

Then $\overrightarrow{\mathrm{AP}}$ is parallel to the vector $\vec{b}$, i.e., $\overrightarrow{\mathrm{AP}}=\lambda \vec{b}$, where $\lambda$ is some real number.

But

$$
\overrightarrow{\mathrm{AP}}=\overrightarrow{\mathrm{OP}}-\overrightarrow{\mathrm{OA}}
$$

i.e.

$$
\lambda \vec{b}=\vec{r}-\vec{a}
$$

Conversely, for each value of the parameter $\lambda$, this equation gives the position vector of a point P on the line. Hence, the vector equation of the line is given by
![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-06.jpg?height=463&width=614&top_left_y=265&top_left_x=789)

$$
\begin{equation*}
\vec{r}=\vec{a}+» \vec{b} \tag{1}
\end{equation*}
$$

Remark If $\vec{b}=a \hat{i}+b \hat{j}+c \hat{k}$, then $a, b, c$ are direction ratios of the line and conversely, if $a, b, c$ are direction ratios of a line, then $\vec{b}=a \hat{i}+b \hat{j}+c \hat{k}$ will be the parallel to the line. Here, $b$ should not be confused with $|\vec{b}|$.

## Derivation of cartesian form from vector form

Let the coordinates of the given point A be ( $x_{1}, y_{1}, z_{1}$ ) and the direction ratios of the line be $a, b, c$. Consider the coordinates of any point P be ( $x, y, z$ ). Then

$$
\vec{r}=x \hat{i}+y \hat{j}+z \hat{k} ; \vec{a}=x_{1} \hat{i}+y_{1} \hat{j}+z_{1} \hat{k}
$$

and

$$
\vec{b}=a \hat{i}+b \hat{j}+c \hat{k}
$$

Substituting these values in (1) and equating the coefficients of $\hat{i}, \hat{j}$ and $\hat{k}$, we get

$$
\begin{equation*}
x=x_{1}+\lambda a ; y=y_{1}+\lambda b ; z=z_{1}+\lambda c \tag{2}
\end{equation*}
$$

These are parametric equations of the line. Eliminating the parameter $\lambda$ from (2), we get

$$
\begin{equation*}
\frac{x-x_{1}}{a}=\frac{y-y_{1}}{b}=\frac{z-z_{1}}{c} \tag{3}
\end{equation*}
$$

This is the Cartesian equation of the line.
$\square$ Note If $l, m, n$ are the direction cosines of the line, the equation of the line is

$$
\frac{x-x_{1}}{l}=\frac{y-y_{1}}{m}=\frac{z-z_{1}}{n}
$$

Example 6 Find the vector and the Cartesian equations of the line through the point $(5,2,-4)$ and which is parallel to the vector $3 \hat{i}+2 \hat{j}-8 \hat{k}$.
Solution We have

$$
\vec{a}=5 \hat{i}+2 \hat{j}-4 \hat{k} \text { and } \vec{b}=3 \hat{i}+2 \hat{j}-8 \hat{k}
$$

Therefore, the vector equation of the line is

$$
\vec{r}=5 \hat{i}+2 \hat{j}-4 \hat{k}+\lambda(3 \hat{i}+2 \hat{j}-8 \hat{k})
$$

Now, $\vec{r}$ is the position vector of any point $\mathrm{P}(x, y, z)$ on the line.
Therefore,

$$
\begin{aligned}
x \hat{i}+y \hat{j}+z \hat{k} & =5 \hat{i}+2 \hat{j}-4 \hat{k}+\lambda(3 \hat{i}+2 \hat{j}-8 \hat{k}) \\
& =(5+3 \lambda) \hat{i}+(2+2 \lambda) \hat{j}+(-4-8 \lambda) \hat{k}
\end{aligned}
$$

Eliminating $\lambda$, we get

$$
\frac{x-5}{3}=\frac{y-2}{2}=\frac{z+4}{-8}
$$

which is the equation of the line in Cartesian form.

### 11.4 Angle between Two Lines

Let $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$ be two lines passing through the origin and with direction ratios $a_{1}, b_{1}, c_{1}$ and $a_{2}, b_{2}, c_{2}$, respectively. Let P be a point on $\mathrm{L}_{1}$ and Q be a point on $\mathrm{L}_{2}$. Consider the directed lines OP and OQ as given in Fig 11.6. Let $\theta$ be the acute angle between OP and OQ . Now recall that the directed line segments OP and OQ are vectors with components $a_{1}, b_{1}, c_{1}$ and $a_{2}, b_{2}, c_{2}$, respectively. Therefore, the angle $\theta$ between them is given by
![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-07.jpg?height=476&width=506&top_left_y=799&top_left_x=896)

$$
\begin{equation*}
\cos \theta=\left|\frac{a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}}{\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}}\right| \tag{1}
\end{equation*}
$$

The angle between the lines in terms of $\sin \theta$ is given by

$$
\begin{align*}
\sin \theta & =\sqrt{1-\cos ^{2} \theta} \\
& =\sqrt{1-\frac{\left(a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}\right)^{2}}{\left(a_{1}^{2}+b_{1}^{2}+c_{1}^{2}\right)\left(a_{2}^{2}+b_{2}^{2}+c_{2}^{2}\right)}} \\
& =\frac{\sqrt{\left(a_{1}^{2}+b_{1}^{2}+c_{1}^{2}\right)\left(a_{2}^{2}+b_{2}^{2}+c_{2}^{2}\right)-\left(a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}\right)^{2}}}{\sqrt{\left(a_{1}^{2}+b_{1}^{2}+c_{1}^{2}\right)} \sqrt{\left(a_{2}^{2}+b_{2}^{2}+c_{2}^{2}\right)}} \\
& =\frac{\sqrt{\left(a_{1} b_{2}-a_{2} b_{1}\right)^{2}+\left(b_{1} c_{2}-b_{2} c_{1}\right)^{2}+\left(c_{1} a_{2}-c_{2} a_{1}\right)^{2}}}{\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}} \tag{2}
\end{align*}
$$

Note In case the lines $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$ do not pass through the origin, we may take lines $\mathrm{L}_{1}^{\prime}$ and $\mathrm{L}_{2}^{\prime}$ which are parallel to $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$ respectively and pass through the origin.

If instead of direction ratios for the lines $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$, direction cosines, namely, $l_{1}, m_{1}, n_{1}$ for $\mathrm{L}_{1}$ and $l_{2}, m_{2}, n_{2}$ for $\mathrm{L}_{2}$ are given, then (1) and (2) takes the following form:

$$
\begin{equation*}
\cos \theta=\left|l_{1} l_{2}+m_{1} m_{2}+n_{1} n_{2}\right| \quad\left(\text { as } l_{1}^{2}+m_{1}^{2}+n_{1}^{2}=1=l_{2}^{2}+m_{2}^{2}+n_{2}^{2}\right) \tag{3}
\end{equation*}
$$

and $\quad \sin \theta=\sqrt{\left(l_{1} m_{2}-l_{2} m_{1}\right)^{2}-\left(m_{1} n_{2}-m_{2} n_{1}\right)^{2}+\left(n_{1} l_{2}-n_{2} l_{1}\right)^{2}}$
Two lines with direction ratios $a_{1}, b_{1}, c_{1}$ and $a_{2}, b_{2}, c_{2}$ are
(i) perpendicular i.e. if $\theta=90^{\circ}$ by (1)

$$
a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}=0
$$

(ii) parallel i.e. if $\theta=0$ by (2)

$$
\frac{a_{1}}{a_{2}}=\frac{b_{1}}{b_{2}}=\frac{c_{1}}{c_{2}}
$$

Now, we find the angle between two lines when their equations are given. If $\theta$ is acute the angle between the lines

$$
\begin{aligned}
\vec{r} & =\bar{a}_{1}+\lambda b_{1} \text { and } \vec{r}=\vec{a}_{2}+\mu \vec{b}_{2} \\
\cos \theta & =\left|\frac{\vec{b}_{1} \cdot \vec{b}_{2}}{\left|\vec{b}_{1}\right|\left|\vec{b}_{2}\right|}\right|
\end{aligned}
$$

then es
In Cartesian form, if $\theta$ is the angle between the lines

$$
\begin{align*}
\frac{x-x_{1}}{a_{1}} & =\frac{y-y_{1}}{b_{1}}=\frac{z-z_{1}}{c_{1}}  \tag{1}\\
\frac{x-x_{2}}{a_{2}} & =\frac{y-y_{2}}{b_{2}}=\frac{z-z_{2}}{c_{2}} \tag{2}
\end{align*}
$$

and
where, $a_{1}, b_{1}, c_{1}$ and $a_{2,} b_{2}, c_{2}$ are the direction ratios of the lines (1) and (2), respectively, then

$$
\cos \theta=\left|\frac{a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}}{\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}}\right|
$$

Example 7 Find the angle between the pair of lines given by

$$
\vec{r}=3 \hat{i}+2 \hat{j}-4 \hat{k}+\lambda(\hat{i}+2 \hat{j}+2 \hat{k})
$$

and

$$
\vec{r}=5 \hat{i}-2 \hat{j}+\mu(3 \hat{i}+2 \hat{j}+6 \hat{k})
$$

Solution Here $\vec{b}_{1}=\hat{i}+2 \hat{j}+2 \hat{k}$ and $\vec{b}_{2}=3 \hat{i}+2 \hat{j}+6 \hat{k}$
The angle $\theta$ between the two lines is given by

$$
\begin{aligned}
\cos \theta & =\left|\frac{\vec{b}_{1} \cdot \vec{b}_{2}}{\left|\vec{b}_{1}\right|\left|\vec{b}_{2}\right|}\right|=\left|\frac{(\hat{i}+2 \hat{j}+2 \hat{k}) \cdot(3 \hat{i}+2 \hat{j}+6 \hat{k})}{\sqrt{1+4+4} \sqrt{9+4+36}}\right| \\
& =\left|\frac{3+4+12}{3 \times 7}\right|=\frac{19}{21}
\end{aligned}
$$

Hence

$$
\theta=\cos ^{-1}\left(\frac{19}{21}\right)
$$

Example 8 Find the angle between the pair of lines
and

$$
\begin{aligned}
& \frac{x+3}{3}=\frac{y-1}{5}=\frac{z+3}{4} \\
& \frac{x+1}{1}=\frac{y-4}{1}=\frac{z-5}{2}
\end{aligned}
$$

Solution The direction ratios of the first line are 3, 5, 4 and the direction ratios of the second line are $1,1,2$. If $\theta$ is the angle between them, then

$$
\cos \theta=\left|\frac{3.1+5.1+4.2}{\sqrt{3^{2}+5^{2}+4^{2}} \sqrt{1^{2}+1^{2}+2^{2}}}\right|=\frac{16}{\sqrt{50} \sqrt{6}}=\frac{16}{5 \sqrt{2} \sqrt{6}}=\frac{8 \sqrt{3}}{15}
$$

Hence, the required angle is $\cos ^{-1}\left(\frac{8 \sqrt{3}}{15}\right)$.

### 11.5 Shortest Distance between Two Lines

If two lines in space intersect at a point, then the shortest distance between them is zero. Also, if two lines in space are parallel, then the shortest distance between them will be the perpendicular distance, i.e. the length of the perpendicular drawn from a point on one line onto the other line.

Further, in a space, there are lines which are neither intersecting nor parallel. In fact, such pair of lines are non coplanar and are called skew lines. For example, let us consider a room of size $1,3,2$ units along
![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-09.jpg?height=471&width=647&top_left_y=1553&top_left_x=755)

Fig 11.5 $x, y$ and $z$-axes respectively Fig 11.5.

The line GE that goes diagonally across the ceiling and the line DB passes through one corner of the ceiling directly above A and goes diagonally down the wall. These lines are skew because they are not parallel and also never meet.

By the shortest distance between two lines we mean the join of a point in one line with one point on the other line so that the length of the segment so obtained is the smallest.

For skew lines, the line of the shortest distance will be perpendicular to both the lines.

### 11.5.1 Distance between two skew lines

We now determine the shortest distance between two skew lines in the following way: Let $l_{1}$ and $l_{2}$ be two skew lines with equations (Fig. 11.6)

$$
\begin{align*}
& \vec{r}=\vec{a}_{1}+\lambda \vec{b}_{1}  \tag{1}\\
& \vec{r}=\vec{a}_{2}+\mu \vec{b}_{2} \tag{2}
\end{align*}
$$

and
Take any point S on $l_{1}$ with position vector $\overrightarrow{\mathrm{a}}_{1}$ and T on $l_{2}$, with position vector $\overrightarrow{\mathrm{a}}_{2}$. Then the magnitude of the shortest distance vector will be equal to that of the projection of ST along the direction of the line of shortest distance (See 10.6.2).

If $\overrightarrow{\mathrm{PQ}}$ is the shortest distance vector between $l_{1}$ and $l_{2}$, then it being perpendicular to both $\vec{b}_{1}$ and $\vec{b}_{2}$, the unit vector $\hat{n}$ along $\overrightarrow{\mathrm{PQ}}$ would therefore be
![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-10.jpg?height=307&width=484&top_left_y=1020&top_left_x=918)

Fig 11.6

$$
\begin{equation*}
\hat{n}=\frac{\vec{b}_{1} \times \vec{b}_{2}}{\left|\vec{b}_{1} \times \vec{b}_{2}\right|} \tag{3}
\end{equation*}
$$

Then

$$
\overrightarrow{\mathrm{PQ}}=d \hat{n}
$$

where, $d$ is the magnitude of the shortest distance vector. Let $\theta$ be the angle between $\overrightarrow{\mathrm{ST}}$ and $\overrightarrow{\mathrm{PQ}}$. Then

$$
\begin{array}{rlr}
\mathrm{PQ} & =\mathrm{ST}|\cos \theta| & \\
\cos \theta & =\left|\frac{\overrightarrow{\mathrm{PQ}} \cdot \overrightarrow{\mathrm{ST}}}{|\overrightarrow{\mathrm{PQ}}||\overrightarrow{\mathrm{ST}}|}\right| & \\
& =\left|\frac{d \hat{n} \cdot\left(\vec{a}_{2}-\vec{a}_{1}\right)}{d \mathrm{ST}}\right| & \left(\text { since } \overrightarrow{\mathrm{ST}}=\vec{a}_{2}-\vec{a}_{1}\right) \\
& =\left|\frac{\left(\vec{b}_{1} \times \vec{b}_{2}\right) \cdot\left(\vec{a}_{2}-\vec{a}_{1}\right)}{\mathrm{ST}\left|\vec{b}_{1} \times \vec{b}_{2}\right|}\right| & \text { [From (3)] } \tag{3}
\end{array}
$$

Hence, the required shortest distance is
or

$$
\begin{aligned}
& d=\mathrm{PQ}=\mathrm{ST}|\cos \theta| \\
& d=\left|\frac{\left(\overrightarrow{\mathrm{b}}_{1} \times \overrightarrow{\mathrm{b}}_{2}\right) \cdot\left(\vec{a}_{2} \times \vec{a}_{1}\right)}{\left|\vec{b}_{1} \times \vec{b}_{2}\right|}\right|
\end{aligned}
$$

## Cartesian form

The shortest distance between the lines
and

$$
\begin{aligned}
& l_{1}: \frac{x-x_{1}}{a_{1}}=\frac{y-y_{1}}{b_{1}}=\frac{z-z_{1}}{c_{1}} \\
& l_{2}: \frac{x-x_{2}}{a_{2}}=\frac{y-y_{2}}{b_{2}}=\frac{z-z_{2}}{c_{2}}
\end{aligned}
$$

is

$$
\left|\frac{\left|\begin{array}{ccc}
x_{2}-x_{1} & y_{2}-y_{1} & z_{2}-z_{1} \\
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|}{\sqrt{\left(b_{1} c_{2}-b_{2} c_{1}\right)^{2}+\left(c_{1} a_{2}-c_{2} a_{1}\right)^{2}+\left(a_{1} b_{2}-a_{2} b_{1}\right)^{2}}}\right|
$$

### 11.5.2 Distance between parallel lines

If two lines $l_{1}$ and $l_{2}$ are parallel, then they are coplanar. Let the lines be given by
and

$$
\begin{gather*}
\vec{r}=\vec{a}_{1}+\lambda \vec{b}  \tag{1}\\
\vec{r}=\vec{a}_{2}+\mu \vec{b} \tag{2}
\end{gather*}
$$

where, $\overrightarrow{\mathrm{a}}_{1}$ is the position vector of a point $S$ on $l_{1}$ and $\overrightarrow{\mathrm{a}}_{2}$ is the position vector of a point T on $l_{2}$ Fig 11.7.

As $l_{1}, l_{2}$ are coplanar, if the foot of the perpendicular from T on the line $l_{1}$ is P , then the distance between the lines $l_{1}$ and $l_{2}=|\mathrm{TP}|$.

Let $\theta$ be the angle between the vectors $\overrightarrow{\mathrm{ST}}$ and $\vec{b}$.
Then
![](https://cdn.mathpix.com/cropped/2025_07_21_4fba676d12865e31fde2g-11.jpg?height=291&width=476&top_left_y=1437&top_left_x=933)

Fig 11.7

$$
\begin{equation*}
\vec{b} \times \overrightarrow{\mathrm{ST}}=(|\vec{b}||\overrightarrow{\mathrm{ST}}| \sin \theta) \hat{n} \ldots \tag{3}
\end{equation*}
$$

where $\hat{n}$ is the unit vector perpendicular to the plane of the lines $l_{1}$ and $l_{2}$
But

$$
\overrightarrow{\mathrm{ST}}=\vec{a}_{2}-\vec{a}_{1}
$$

Therefore, from (3), we get
i.e.,

$$
\begin{aligned}
\vec{b} \times\left(\vec{a}_{2}-\vec{a}_{1}\right)=\vec{b} \mid \mathrm{PT} \hat{n} & (\text { since } \mathrm{PT}=\mathrm{ST} \sin \theta) \\
\left|\vec{b} \times\left(\vec{a}_{2}-\vec{a}_{1}\right)\right|=|\vec{b}| \mathrm{PT} \cdot 1 & (\text { as }|\hat{n}|=1)
\end{aligned}
$$

Hence, the distance between the given parallel lines is

$$
d=|\overrightarrow{\mathrm{PT}}|=\left|\frac{\vec{b} \times\left(\vec{a}_{2}-\vec{a}_{1}\right)}{|\vec{b}|}\right|
$$

Example 9 Find the shortest distance between the lines $l_{1}$ and $l_{2}$ whose vector equations are
and

$$
\begin{align*}
\vec{r} & =\hat{i}+\hat{j}+\lambda(2 \hat{i}-\hat{j}+\hat{k})  \tag{1}\\
\vec{r} & =2 \hat{i}+\hat{j}-\hat{k}+\mu(3 \hat{i}-5 \hat{j}+2 \hat{k}) \tag{2}
\end{align*}
$$

Solution Comparing (1) and (2) with $\vec{r}=\vec{a}_{1}+\lambda \vec{b}_{1}$ and $\overrightarrow{\mathrm{r}}=\overrightarrow{\mathrm{a}}_{2}+\mu \overrightarrow{\mathrm{b}}_{2}$ respectively, we get

$$
\begin{aligned}
& \overrightarrow{\mathrm{a}}_{1}=\hat{i}+\hat{j}, \vec{b}_{1}=2 \hat{i}-\hat{j}+\hat{k} \\
& \overrightarrow{\mathrm{a}}_{2}=2 \hat{i}+\hat{j}-\hat{k} \text { and } \vec{b}_{2}=3 \hat{i}-5 \hat{j}+2 \hat{k}
\end{aligned}
$$

Therefore $\vec{a}_{2}-\vec{a}_{1}=\hat{i}-\hat{k}$
and

$$
\begin{aligned}
\vec{b}_{1} \times \vec{b}_{2} & =(2 \hat{i}-\hat{j}+\hat{k}) \times(3 \hat{i}-5 \hat{j}+2 \hat{k}) \\
& =\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
2 & -1 & 1 \\
3 & -5 & 2
\end{array}\right|=3 \hat{i}-\hat{j}-7 \hat{k}
\end{aligned}
$$

So

$$
\left|\vec{b}_{1} \times \vec{b}_{2}\right|=\sqrt{9+1+49}=\sqrt{59}
$$

Hence, the shortest distance between the given lines is given by

$$
d=\left|\frac{\left(\overrightarrow{\mathrm{b}}_{1} \times \overrightarrow{\mathrm{b}}_{2}\right) \cdot\left(\overrightarrow{\mathrm{a}}_{2}-\overrightarrow{\mathrm{a}}_{1}\right)}{\left|\overrightarrow{\mathrm{b}}_{1} \times \overrightarrow{\mathrm{b}}_{2}\right|}\right|=\frac{|3-0+7|}{\sqrt{59}}=\frac{10}{\sqrt{59}}
$$

Example 10 Find the distance between the lines $l_{1}$ and $l_{2}$ given by

$$
\vec{r}=\hat{i}+2 \hat{j}-4 \hat{k}+\lambda(2 \hat{i}+3 \hat{j}+6 \hat{k})
$$

and

$$
\vec{r}=3 \hat{i}+3 \hat{j}-5 \hat{k}+\mu(2 \hat{i}+3 \hat{j}+6 \hat{k})
$$

Solution The two lines are parallel (Why?) We have

$$
\overrightarrow{\mathrm{a}}_{1}=\hat{i}+2 \hat{j}-4 \hat{k}, \overrightarrow{\mathrm{a}}_{2}=3 \hat{i}+3 \hat{j}-5 \hat{k} \text { and } \vec{b}=2 \hat{i}+3 \hat{j}+6 \hat{k}
$$

Therefore, the distance between the lines is given by

$$
\begin{aligned}
d & =\left|\frac{\vec{b} \times\left(\vec{a}_{2}-\vec{a}_{1}\right)}{|\vec{b}|}\right|=\left|\frac{\left|\begin{array}{ccc}
\hat{i} & \hat{j} & \hat{k} \\
2 & 3 & 6 \\
2 & 1 & -1
\end{array}\right|}{\sqrt{4+9+36}}\right| \\
& =\frac{|-9 \hat{i}+14 \hat{j}-4 \hat{k}|}{\sqrt{49}}=\frac{\sqrt{293}}{\sqrt{49}}=\frac{\sqrt{293}}{7}
\end{aligned}
$$

or

## EXERCISE 11.2

1. Show that the three lines with direction cosines
$\frac{12}{13}, \frac{-3}{13}, \frac{-4}{13} ; \frac{4}{13}, \frac{12}{13}, \frac{3}{13} ; \frac{3}{13}, \frac{-4}{13}, \frac{12}{13}$ are mutually perpendicular.
2. Show that the line through the points $(1,-1,2),(3,4,-2)$ is perpendicular to the line through the points $(0,3,2)$ and $(3,5,6)$.
3. Show that the line through the points $(4,7,8),(2,3,4)$ is parallel to the line through the points $(-1,-2,1),(1,2,5)$.
4. Find the equation of the line which passes through the point $(1,2,3)$ and is parallel to the vector $3 \hat{i}+2 \hat{j}-2 \hat{k}$.
5. Find the equation of the line in vector and in cartesian form that passes through the point with position vector $2 \hat{i}-j+4 \hat{k}$ and is in the direction $\hat{i}+2 \hat{j}-\hat{k}$.
6. Find the cartesian equation of the line which passes through the point $(-2,4,-5)$ and parallel to the line given by $\frac{x+3}{3}=\frac{y-4}{5}=\frac{z+8}{6}$.
7. The cartesian equation of a line is $\frac{x-5}{3}=\frac{y+4}{7}=\frac{z-6}{2}$. Write its vector form.
8. Find the angle between the following pairs of lines:
(i) $\vec{r}=2 \hat{i}-5 \hat{j}+\hat{k}+\lambda(3 \hat{i}+2 \hat{j}+6 \hat{k})$ and $\vec{r}=7 \hat{i}-6 \hat{k}+\mu(\hat{i}+2 \hat{j}+2 \hat{k})$
(ii) $\vec{r}=3 \hat{i}+\hat{j}-2 \hat{k}+\lambda(\hat{i}-\hat{j}-2 \hat{k})$ and $\vec{r}=2 \hat{i}-\hat{j}-56 \hat{k}+\mu(3 \hat{i}-5 \hat{j}-4 \hat{k})$
9. Find the angle between the following pair of lines:
(i) $\frac{x-2}{2}=\frac{y-1}{5}=\frac{z+3}{-3}$ and $\frac{x+2}{-1}=\frac{y-4}{8}=\frac{z-5}{4}$
(ii) $\frac{x}{2}=\frac{y}{2}=\frac{z}{1}$ and $\frac{x-5}{4}=\frac{y-2}{1}=\frac{z-3}{8}$
10. Find the values of $p$ so that the lines $\frac{1-x}{3}=\frac{7 y-14}{2 p}=\frac{z-3}{2}$ and $\frac{7-7 x}{3 p}=\frac{y-5}{1}=\frac{6-z}{5}$ are at right angles.
11. Show that the lines $\frac{x-5}{7}=\frac{y+2}{-5}=\frac{z}{1}$ and $\frac{x}{1}=\frac{y}{2}=\frac{z}{3}$ are perpendicular to each other.
12. Find the shortest distance between the lines
$\vec{r}=(\hat{i}+2 \hat{j}+\hat{k})+\lambda(\hat{i}-\hat{j}+\hat{k})$ and
$\vec{r}=2 \hat{i}-\hat{j}-\hat{k}+\mu(2 \hat{i}+\hat{j}+2 \hat{k})$
13. Find the shortest distance between the lines
$\frac{x+1}{7}=\frac{y+1}{-6}=\frac{z+1}{1}$ and $\frac{x-3}{1}=\frac{y-5}{-2}=\frac{z-7}{1}$
14. Find the shortest distance between the lines whose vector equations are
$\vec{r}=(\hat{i}+2 \hat{j}+3 \hat{k})+\lambda(\hat{i}-3 \hat{j}+2 \hat{k})$
and $\vec{r}=4 \hat{i}+5 \hat{j}+6 \hat{k}+\mu(2 \hat{i}+3 \hat{j}+\hat{k})$
15. Find the shortest distance between the lines whose vector equations are
$\vec{r}=(1-t) \hat{i}+(t-2) \hat{j}+(3-2 t) \hat{k}$ and
$\vec{r}=(s+1) \hat{i}+(2 s-1) \hat{j}-(2 s+1) \hat{k}$

## Miscellaneous Exercise on Chapter 11

1. Find the angle between the lines whose direction ratios are $a, b, c$ and $b-c, c-a, a-b$.
2. Find the equation of a line parallel to $x$-axis and passing through the origin.
3. If the lines $\frac{x-1}{-3}=\frac{y-2}{2 k}=\frac{z-3}{2}$ and $\frac{x-1}{3 k}=\frac{y-1}{1}=\frac{z-6}{-5}$ are perpendicular, find the value of $k$.
4. Find the shortest distance between lines $\vec{r}=6 \hat{i}+2 \hat{j}+2 \hat{k}+\lambda(\hat{i}-2 \hat{j}+2 \hat{k})$ and $\vec{r}=-4 \hat{i}-\hat{k}+\mu(3 \hat{i}-2 \hat{j}-2 \hat{k})$.
5. Find the vector equation of the line passing through the point $(1,2,-4)$ and perpendicular to the two lines:

$$
\frac{x-8}{3}=\frac{y+19}{-16}=\frac{z-10}{7} \text { and } \frac{x-15}{3}=\frac{y-29}{8}=\frac{z-5}{-5} .
$$

## Summary

- Direction cosines of a line are the cosines of the angles made by the line with the positive directions of the coordinate axes.
- If $l, m, n$ are the direction cosines of a line, then $l^{2}+m^{2}+n^{2}=1$.
- Direction cosines of a line joining two points $\mathrm{P}\left(x_{1}, y_{1}, z_{1}\right)$ and $\mathrm{Q}\left(x_{2}, y_{2}, z_{2}\right)$ are $\frac{x_{2}-x_{1}}{\mathrm{PQ}}, \frac{y_{2}-y_{1}}{\mathrm{PQ}}, \frac{z_{2}-z_{1}}{\mathrm{PQ}}$
where $\mathrm{PQ}=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}$
- Direction ratios of a line are the numbers which are proportional to the direction cosines of a line.
- If $l, m, n$ are the direction cosines and $a, b, c$ are the direction ratios of a line then

$$
l=\frac{a}{\sqrt{a^{2}+b^{2}+c^{2}}} ; m=\frac{b}{\sqrt{a^{2}+b^{2}+c^{2}}} ; n=\frac{c}{\sqrt{a^{2}+b^{2}+c^{2}}}
$$

- Skew lines are lines in space which are neither parallel nor intersecting. They lie in different planes.
- Angle between skew lines is the angle between two intersecting lines drawn from any point (preferably through the origin) parallel to each of the skew lines.
- If $l_{1}, m_{1}, n_{1}$ and $l_{2}, m_{2}, n_{2}$ are the direction cosines of two lines; and $\theta$ is the acute angle between the two lines; then

$$
\cos \theta=\left|l_{1} l_{2}+m_{1} m_{2}+n_{1} n_{2}\right|
$$

- If $a_{1}, b_{1}, c_{1}$ and $a_{2}, b_{2}, c_{2}$ are the direction ratios of two lines and $\theta$ is the acute angle between the two lines; then

$$
\cos \theta=\left|\frac{a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}}{\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}}\right|
$$

- Vector equation of a line that passes through the given point whose position vector is $\vec{a}$ and parallel to a given vector $\vec{b}$ is $\vec{r}=\vec{a}+\lambda \vec{b}$.
- Equation of a line through a point $\left(x_{1}, y_{1}, z_{1}\right)$ and having direction cosines $l, m, n$ is $\frac{x-x_{1}}{l}=\frac{y-y_{1}}{m}=\frac{z-z_{1}}{n}$
- The vector equation of a line which passes through two points whose position vectors are $\vec{a}$ and $\vec{b}$ is $\vec{r}=\vec{a}+\lambda(\vec{b}-\vec{a})$.
- If $\theta$ is the acute angle between $\vec{r}=\vec{a}_{1}+\lambda \vec{b}_{1}$ and $\vec{r}=\vec{a}_{2}+\lambda \vec{b}_{2}$, then $\cos \theta=\left|\frac{\vec{b}_{1} \cdot \vec{b}_{2}}{\left|\vec{b}_{1}\right|\left|\vec{b}_{2}\right|}\right|$
- If $\frac{x-x_{1}}{l_{1}}=\frac{y-y_{1}}{m_{1}}=\frac{z-z_{1}}{n_{1}}$ and $\frac{x-x_{2}}{l_{2}}=\frac{y-y_{2}}{m_{2}}=\frac{z-z_{2}}{n_{2}}$
are the equations of two lines, then the acute angle between the two lines is given by $\cos \theta=\left|l_{1} l_{2}+m_{1} m_{2}+n_{1} n_{2}\right|$.
- Shortest distance between two skew lines is the line segment perpendicular to both the lines.
- Shortest distance between $\vec{r}=\vec{a}_{1}+\lambda \vec{b}_{1}$ and $\vec{r}=\vec{a}_{2}+\mu \vec{b}_{2}$ is

$$
\left|\frac{\left(\vec{b}_{1} \times \vec{b}_{2}\right) \cdot\left(\vec{a}_{2}-\vec{a}_{1}\right)}{\left|\vec{b}_{1} \times \vec{b}_{2}\right|}\right|
$$

- Shortest distance between the lines: $\frac{x-x_{1}}{a_{1}}=\frac{y-y_{1}}{b_{1}}=\frac{z-z_{1}}{c_{1}}$ and $\frac{x-x_{2}}{a_{2}}=\frac{y-y_{2}}{b_{2}}=\frac{z-z_{2}}{c_{2}}$ is

$$
\frac{\left|\begin{array}{ccc}
x_{2}-x_{1} & y_{2}-y_{1} & z_{2}-z_{1} \\
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|}{\sqrt{\left(b_{1} c_{2}-b_{2} c_{1}\right)^{2}+\left(c_{1} a_{2}-c_{2} a_{1}\right)^{2}+\left(a_{1} b_{2}-a_{2} b_{1}\right)^{2}}}
$$

- Distance between parallel lines $\vec{r}=\vec{a}_{1}+\lambda \vec{b}$ and $\vec{r}=\vec{a}_{2}+\mu \vec{b}$ is

$$
\left|\frac{\vec{b} \times\left(\vec{a}_{2}-\vec{a}_{1}\right)}{|\vec{b}|}\right|
$$


[^0]:    ＊For various activities in three dimensional geometry，one may refer to the Book
    ＂A Hand Book for designing Mathematics Laboratory in Schools＂，NCERT， 2005

