## RELATIONS AND FUNCTIONS

## Mathematics is the indispensable instrument of all physical research. - BERTHELOT

### 2.1 Introduction

Much of mathematics is about finding a pattern - a recognisable link between quantities that change. In our daily life, we come across many patterns that characterise relations such as brother and sister, father and son, teacher and student. In mathematics also, we come across many relations such as number $m$ is less than number $n$, line $l$ is parallel to line $m$, set A is a subset of set B . In all these, we notice that a relation involves pairs of objects in certain order. In this Chapter, we will learn how to link pairs of objects from two sets and then introduce relations between the two objects in the pair. Finally, we will learn about special relations which will qualify to be functions. The
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-01.jpg?height=521&width=400&top_left_y=825&top_left_x=1057)
G. W. Leibnitz
(1646-1716) concept of function is very important in mathematics since it captures the idea of a mathematically precise correspondence between one quantity with the other.

### 2.2 Cartesian Products of Sets

Suppose A is a set of 2 colours and B is a set of 3 objects, i.e.,

$$
\mathrm{A}=\{\text { red, blue }\} \text { and } \mathrm{B}=\{b, c, s\},
$$

where $b, c$ and $s$ represent a particular bag, coat and shirt, respectively. How many pairs of coloured objects can be made from these two sets?
Proceeding in a very orderly manner, we can see that there will be 6 distinct pairs as given below:

$$
(\text { (red, } b),(\text { red, } c),(\text { red, } s),(\text { blue, } b),(\text { blue, } c),(\text { blue, } s) .
$$

Thus, we get 6 distinct objects (Fig 2.1).
Let us recall from our earlier classes that an ordered pair of elements taken from any two sets P and Q is a pair of elements written in small
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-01.jpg?height=244&width=215&top_left_y=1803&top_left_x=1247)

Fig 2.1
brackets and grouped together in a particular order, i.e., $(p, q), p \in \mathrm{P}$ and $q \in \mathrm{Q}$. This leads to the following definition:
Definition 1 Given two non-empty sets P and Q . The cartesian product $\mathrm{P} \times \mathrm{Q}$ is the set of all ordered pairs of elements from P and Q , i.e.,

$$
\mathrm{P} \times \mathrm{Q}=\{(p, q): p \in \mathrm{P}, q \in \mathrm{Q}\}
$$

If either P or Q is the null set, then $\mathrm{P} \times \mathrm{Q}$ will also be empty set, i.e., $\mathrm{P} \times \mathrm{Q}=\phi$
From the illustration given above we note that
$\mathrm{A} \times \mathrm{B}=\{(\mathrm{red}, b),(\mathrm{red}, c),(\mathrm{red}, s),(\mathrm{blue}, b),(\mathrm{blue}, c),(\mathrm{blue}, s)\}$.
Again, consider the two sets:
$\mathrm{A}=\{\mathrm{DL}, \mathrm{MP}, \mathrm{KA}\}$, where $\mathrm{DL}, \mathrm{MP}, \mathrm{KA}$ represent Delhi, Madhya Pradesh and Karnataka, respectively and $B=\{01,02$, $03\}$ representing codes for the licence plates of vehicles issued by DL, MP and KA .

If the three states, Delhi, Madhya Pradesh and Karnataka were making codes for the licence plates of vehicles, with the restriction that the code begins with an element from set A , which are the pairs available from these sets and how many such
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-02.jpg?height=260&width=349&top_left_y=793&top_left_x=1122)

Fig 2.2 pairs will there be (Fig 2.2)?

The available pairs are:(DL,01), (DL,02), (DL,03), (MP,01), (MP,02), (MP,03), ( $\mathrm{KA}, 01$ ), ( $\mathrm{KA}, 02$ ), (KA,03) and the product of set A and set B is given by $\mathrm{A} \times \mathrm{B}=\{(\mathrm{DL}, 01),(\mathrm{DL}, 02),(\mathrm{DL}, 03),(\mathrm{MP}, 01),(\mathrm{MP}, 02),(\mathrm{MP}, 03),(\mathrm{KA}, 01),(\mathrm{KA}, 02)$, (KA,03)\}.
It can easily be seen that there will be 9 such pairs in the Cartesian product, since there are 3 elements in each of the sets A and B . This gives us 9 possible codes. Also note that the order in which these elements are paired is crucial. For example, the code (DL, 01 ) will not be the same as the code ( $01, \mathrm{DL}$ ).

As a final illustration, consider the two sets $\mathrm{A}=\left\{a_{1}, a_{2}\right\}$ and
$\mathrm{B}=\left\{b_{1}, b_{2}, b_{3}, b_{4}\right\}$ (Fig 2.3).
$\mathrm{A} \times \mathrm{B}=\left\{\left(a_{1}, b_{1}\right),\left(a_{1}, b_{2}\right),\left(a_{1}, b_{3}\right),\left(a_{1}, b_{4}\right),\left(a_{2}, b_{1}\right),\left(a_{2}, b_{2}\right)\right.$, $\left.\left(a_{2}, b_{3}\right),\left(a_{2}, b_{4}\right)\right\}$.
The 8 ordered pairs thus formed can represent the position of points in the plane if A and B are subsets of the set of real numbers and it is obvious that the point in the position $\left(a_{1}, b_{2}\right)$ will be distinct from the point in the position $\left(b_{2}, a_{1}\right)$.
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-02.jpg?height=335&width=224&top_left_y=1565&top_left_x=1245)

Fig 2.3

## Remarks

(i) Two ordered pairs are equal, if and only if the corresponding first elements are equal and the second elements are also equal.
(ii) If there are $p$ elements in A and $q$ elements in B , then there will be $p q$ elements in $\mathrm{A} \times \mathrm{B}$, i.e., if $n(\mathrm{~A})=p$ and $n(\mathrm{~B})=q$, then $n(\mathrm{~A} \times \mathrm{B})=p q$.
(iii) If A and B are non-empty sets and either A or B is an infinite set, then so is $\mathrm{A} \times \mathrm{B}$.
(iv) $\mathrm{A} \times \mathrm{A} \times \mathrm{A}=\{(a, b, c): a, b, c \in \mathrm{~A}\}$. Here ( $a, b, c$ ) is called an ordered triplet.

## Example 1 If $(x+1, y-2)=(3,1)$, find the values of $x$ and $y$.

Solution Since the ordered pairs are equal, the corresponding elements are equal.
Therefore $x+1=3$ and $y-2=1$.
Solving we get $x=2$ and $y=3$.

Example 2 If $\mathrm{P}=\{a, b, c\}$ and $\mathrm{Q}=\{r\}$, form the sets $\mathrm{P} \times \mathrm{Q}$ and $\mathrm{Q} \times \mathrm{P}$. Are these two products equal?

Solution By the definition of the cartesian product,

$$
\mathrm{P} \times \mathrm{Q}=\{(a, r),(b, r),(c, r)\} \text { and } \mathrm{Q} \times \mathrm{P}=\{(r, a),(r, b),(r, c)\}
$$

Since, by the definition of equality of ordered pairs, the pair ( $a, r$ ) is not equal to the pair ( $r, a$ ), we conclude that $\mathrm{P} \times \mathrm{Q} \neq \mathrm{Q} \times \mathrm{P}$.
However, the number of elements in each set will be the same.
Example 3 Let $\mathrm{A}=\{1,2,3\}, \mathrm{B}=\{3,4\}$ and $\mathrm{C}=\{4,5,6\}$. Find
(i) $\mathrm{A} \times(\mathrm{B} \cap \mathrm{C})$
(ii) $(\mathrm{A} \times \mathrm{B}) \cap(\mathrm{A} \times \mathrm{C})$
(iii) $\mathrm{A} \times(\mathrm{B} \cup \mathrm{C})$
(iv) $(\mathrm{A} \times \mathrm{B}) \cup(\mathrm{A} \times \mathrm{C})$

Solution (i) By the definition of the intersection of two sets, $(\mathrm{B} \cap \mathrm{C})=\{4\}$.
Therefore, $\mathrm{A} \times(\mathrm{B} \cap \mathrm{C})=\{(1,4),(2,4),(3,4)\}$.
(ii) $\operatorname{Now}(\mathrm{A} \times \mathrm{B})=\{(1,3),(1,4),(2,3),(2,4),(3,3),(3,4)\}$ and $(A \times C)=\{(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)\}$
Therefore, $(\mathrm{A} \times \mathrm{B}) \cap(\mathrm{A} \times \mathrm{C})=\{(1,4),(2,4),(3,4)\}$.
(iii) Since, $(\mathrm{B} \cup \mathrm{C})=\{3,4,5,6\}$, we have $A \times(B \cup C)=\{(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6),(3,3)$, $(3,4),(3,5),(3,6)\}$.
(iv) Using the sets $\mathrm{A} \times \mathrm{B}$ and $\mathrm{A} \times \mathrm{C}$ from part (ii) above, we obtain $(A \times B) \cup(A \times C)=\{(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(2,6)$, $(3,3),(3,4),(3,5),(3,6)\}$.

Example 4 If $\mathrm{P}=\{1,2\}$, form the set $\mathrm{P} \times \mathrm{P} \times \mathrm{P}$.
Solution We have, $\mathrm{P} \times \mathrm{P} \times \mathrm{P}=\{(1,1,1),(1,1,2),(1,2,1),(1,2,2),(2,1,1),(2,1,2),(2,2,1)$, (2,2,2)\}.
Example 5 If $\mathbf{R}$ is the set of all real numbers, what do the cartesian products $\mathbf{R} \times \mathbf{R}$ and $\mathbf{R} \times \mathbf{R} \times \mathbf{R}$ represent?

Solution The Cartesian product $\mathbf{R} \times \mathbf{R}$ represents the set $\mathbf{R} \times \mathbf{R}=\{(x, y): x, y \in \mathbf{R}\}$ which represents the coordinates of all the points in two dimensional space and the cartesian product $\mathbf{R} \times \mathbf{R} \times \mathbf{R}$ represents the set $\mathbf{R} \times \mathbf{R} \times \mathbf{R}=\{(x, y, z): x, y, z \in \mathbf{R}\}$ which represents the coordinates of all the points in three-dimensional space.

Example 6 If $\mathrm{A} \times \mathrm{B}=\{(p, q),(p, r),(m, q),(m, r)\}$, find A and B .
Solution

$$
\begin{aligned}
& \mathrm{A}=\text { set of first elements }=\{p, m\} \\
& \mathrm{B}=\text { set of second elements }=\{q, r\}
\end{aligned}
$$

## EXERCISE 2.1

1. If $\left(\frac{x}{3}+1, y-\frac{2}{3}\right)=\left(\frac{5}{3}, \frac{1}{3}\right)$, find the values of $x$ and $y$.
2. If the set A has 3 elements and the set $\mathrm{B}=\{3,4,5\}$, then find the number of elements in $(\mathrm{A} \times \mathrm{B})$.
3. If $\mathrm{G}=\{7,8\}$ and $\mathrm{H}=\{5,4,2\}$, find $\mathrm{G} \times \mathrm{H}$ and $\mathrm{H} \times \mathrm{G}$.
4. State whether each of the following statements are true or false. If the statement is false, rewrite the given statement correctly.
(i) If $\mathrm{P}=\{m, n\}$ and $\mathrm{Q}=\{n, m\}$, then $\mathrm{P} \times \mathrm{Q}=\{(m, n),(n, m)\}$.
(ii) If A and B are non-empty sets, then $\mathrm{A} \times \mathrm{B}$ is a non-empty set of ordered pairs $(x, y)$ such that $x \in \mathrm{~A}$ and $y \in \mathrm{~B}$.
(iii) If $\mathrm{A}=\{1,2\}, \mathrm{B}=\{3,4\}$, then $\mathrm{A} \times(\mathrm{B} \cap \phi)=\phi$.
5. If $\mathrm{A}=\{-1,1\}$, find $\mathrm{A} \times \mathrm{A} \times \mathrm{A}$.
6. If $\mathrm{A} \times \mathrm{B}=\{(a, x),(a, y),(b, x),(b, y)\}$. Find A and B .
7. Let $\mathrm{A}=\{1,2\}, \mathrm{B}=\{1,2,3,4\}, \mathrm{C}=\{5,6\}$ and $\mathrm{D}=\{5,6,7,8\}$. Verify that (i) $\mathrm{A} \times(\mathrm{B} \cap \mathrm{C})=(\mathrm{A} \times \mathrm{B}) \cap(\mathrm{A} \times \mathrm{C})$. (ii) $\mathrm{A} \times \mathrm{C}$ is a subset of $\mathrm{B} \times \mathrm{D}$.
8. Let $A=\{1,2\}$ and $B=\{3,4\}$. Write $A \times B$. How many subsets will $A \times B$ have? List them.
9. Let A and B be two sets such that $n(\mathrm{~A})=3$ and $n(\mathrm{~B})=2$. If $(x, 1),(y, 2),(z, 1)$ are in $\mathrm{A} \times \mathrm{B}$, find A and B , where $x, y$ and $z$ are distinct elements.
10. The Cartesian product $\mathrm{A} \times \mathrm{A}$ has 9 elements among which are found ( $-1,0$ ) and $(0,1)$. Find the set A and the remaining elements of $\mathrm{A} \times \mathrm{A}$.

### 2.3 Relations

Consider the two sets $\mathrm{P}=\{a, b, c\}$ and $\mathrm{Q}=\{$ Ali, Bhanu, Binoy, Chandra, Divya $\}$. The cartesian product of P and Q has 15 ordered pairs which can be listed as $\mathrm{P} \times \mathrm{Q}=\{(a, \mathrm{Ali})$, (a, Bhanu), (a, Binoy), ..., (c, Divya)\}.

We can now obtain a subset of $\mathrm{P} \times \mathrm{Q}$ by introducing a relation R between the first element $x$ and the second element $y$ of each ordered pair
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-05.jpg?height=365&width=704&top_left_y=555&top_left_x=761) $(x, y)$ as
$\mathrm{R}=\{(x, y): x$ is the first letter of the name $y, x \in \mathrm{P}, y \in \mathrm{Q}\}$.
Then $\mathrm{R}=\{(a, \mathrm{Ali}),(b, \mathrm{Bhanu}),(b, \mathrm{Binoy}),(c, \mathrm{Chandra})\}$
A visual representation of this relation R (called an arrow diagram) is shown in Fig 2.4.

Definition 2 A relation R from a non-empty set A to a non-empty set B is a subset of the cartesian product $\mathrm{A} \times \mathrm{B}$. The subset is derived by describing a relationship between the first element and the second element of the ordered pairs in $\mathrm{A} \times \mathrm{B}$. The second element is called the image of the first element.

Definition 3 The set of all first elements of the ordered pairs in a relation $R$ from a set $A$ to a set $B$ is called the domain of the relation $R$.

Definition 4 The set of all second elements in a relation $R$ from a set $A$ to a set $B$ is called the range of the relation R . The whole set B is called the codomain of the relation $R$. Note that range $\subset$ codomain.

Remarks (i) A relation may be represented algebraically either by the Roster method or by the Set-builder method.
(ii) An arrow diagram is a visual representation of a relation.

Example 7 Let $\mathrm{A}=\{1,2,3,4,5,6\}$. Define a relation R from A to A by
$\mathrm{R}=\{(x, y): y=x+1\}$
(i) Depict this relation using an arrow diagram.
(ii) Write down the domain, codomain and range of R .

Solution (i) By the definition of the relation, $R=\{(1,2),(2,3),(3,4),(4,5),(5,6)\}$.

The corresponding arrow diagram is shown in Fig 2.5.
(ii) We can see that the domain $=\{1,2,3,4,5$,

Similarly, the range $=\{2,3,4,5,6\}$ and the codomain $=\{1,2,3,4,5,6\}$.

Example 8 The Fig 2.6 shows a relation
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-06.jpg?height=301&width=639&top_left_y=325&top_left_x=824)

Fig 2.5 between the sets P and Q . Write this relation (i) in set-builder form, (ii) in roster form. What is its domain and range?

Solution It is obvious that the relation R is " $x$ is the square of $y$ ".
(i) In set-builder form, $\mathrm{R}=\{(x, y): x$ is the square of $y, x \in \mathrm{P}, y \in \mathbf{Q}\}$
(ii) In roster form, $\mathrm{R}=\{(9,3)$, $(9,-3),(4,2),(4,-2),(25,5),(25,-5)\}$
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-06.jpg?height=335&width=639&top_left_y=744&top_left_x=824)

Fig 2.6

The domain of this relation is $\{4,9,25\}$.
The range of this relation is $\{-2,2,-3,3,-5,5\}$.
Note that the element 1 is not related to any element in set P .
The set Q is the codomain of this relation.
Note The total number of relations that can be defined from a set A to a set B is the number of possible subsets of $\mathrm{A} \times \mathrm{B}$. If $n(\mathrm{~A})=p$ and $n(\mathrm{~B})=q$, then $n(\mathrm{~A} \times \mathrm{B})=p q$ and the total number of relations is $2^{p q}$.

Example 9 Let $\mathrm{A}=\{1,2\}$ and $\mathrm{B}=\{3,4\}$. Find the number of relations from A to B .
Solution We have,

$$
A \times B=\{(1,3),(1,4),(2,3),(2,4)\}
$$

Since $n(\mathrm{~A} \times \mathrm{B})=4$, the number of subsets of $\mathrm{A} \times \mathrm{B}$ is $2^{4}$. Therefore, the number of relations from $A$ into $B$ will be $2{ }^{4}$.
Remark A relation R from A to A is also stated as a relation on A .

## EXERCISE 2.2

1. Let $\mathrm{A}=\{1,2,3, \ldots, 14\}$. Define a relation R from A to A by $\mathrm{R}=\{(x, y): 3 x-y=0$, where $x, y \in \mathrm{~A}\}$. Write down its domain, codomain and range.
2. Define a relation R on the set $\mathbf{N}$ of natural numbers by $\mathrm{R}=\{(x, y): y=x+5$, $x$ is a natural number less than $4 ; x, y \in \mathbf{N}\}$. Depict this relationship using roster form. Write down the domain and the range.
3. $\mathrm{A}=\{1,2,3,5\}$ and $\mathrm{B}=\{4,6,9\}$. Define a relation R from A to B by $\mathrm{R}=\{(x, y)$ : the difference between $x$ and $y$ is odd; $x \in \mathrm{~A}, y \in \mathrm{~B}\}$. Write R in roster form.
4. The Fig2.7 shows a relationship between the sets P and Q . Write this relation
(i) in set-builder form (ii) roster form. What is its domain and range?
5. Let $\mathrm{A}=\{1,2,3,4,6\}$. Let R be the relation on A defined by
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-07.jpg?height=342&width=633&top_left_y=620&top_left_x=834) $\{(a, b): a, b \in \mathrm{~A}, b$ is exactly divisible by $a\}$.
(i) Write R in roster form
(ii) Find the domain of R
(iii) Find the range of R .
6. Determine the domain and range of the relation R defined by $\mathrm{R}=\{(x, x+5): x \in\{0,1,2,3,4,5\}\}$.
7. Write the relation $\mathrm{R}=\left\{\left(x, x^{3}\right): x\right.$ is a prime number less than 10$\}$ in roster form.
8. Let $\mathrm{A}=\{x, y, z\}$ and $\mathrm{B}=\{1,2\}$. Find the number of relations from A to B .
9. Let R be the relation on $\mathbf{Z}$ defined by $\mathrm{R}=\{(a, b): a, b \in \mathbf{Z}, a-b$ is an integer $\}$. Find the domain and range of R .

### 2.4 Functions

In this Section, we study a special type of relation called function. It is one of the most important concepts in mathematics. We can, visualise a function as a rule, which produces new elements out of some given elements. There are many terms such as 'map' or 'mapping' used to denote a function.

Definition 5 A relation $f$ from a set A to a set B is said to be a function if every element of set A has one and only one image in set B .

In other words, a function $f$ is a relation from a non-empty set A to a non-empty set B such that the domain of $f$ is A and no two distinct ordered pairs in $f$ have the same first element.

If $f$ is a function from A to B and $(a, b) \in f$, then $f(a)=b$, where $b$ is called the image of $a$ under $f$ and $a$ is called the preimage of $b$ under $f$.

The function $f$ from A to B is denoted by $f: \mathrm{A} \rightarrow \mathrm{B}$.
Looking at the previous examples, we can easily see that the relation in Example 7 is not a function because the element 6 has no image.

Again, the relation in Example 8 is not a function because the elements in the domain are connected to more than one images. Similarly, the relation in Example 9 is also not a function. (Why?) In the examples given below, we will see many more relations some of which are functions and others are not.
Example 10 Let $\mathbf{N}$ be the set of natural numbers and the relation R be defined on N such that $\mathrm{R}=\{(x, y): y=2 x, x, y \in \mathbf{N}\}$.

What is the domain, codomain and range of R ? Is this relation a function?
Solution The domain of R is the set of natural numbers $\mathbf{N}$. The codomain is also $\mathbf{N}$. The range is the set of even natural numbers.

Since every natural number $n$ has one and only one image, this relation is a function.

Example 11 Examine each of the following relations given below and state in each case, giving reasons whether it is a function or not?
(i) $\mathrm{R}=\{(2,1),(3,1),(4,2)\}$, (ii) $\mathrm{R}=\{(2,2),(2,4),(3,3),(4,4)\}$
(iii) $\mathrm{R}=\{(1,2),(2,3),(3,4),(4,5),(5,6),(6,7)\}$

Solution (i) Since 2,3,4 are the elements of domain of $R$ having their unique images, this relation $R$ is a function.
(ii) Since the same first element 2 corresponds to two different images 2 and 4 , this relation is not a function.
(iii) Since every element has one and only one image, this relation is a function.

Definition 6 A function which has either $R$ or one of its subsets as its range is called a real valued function. Further, if its domain is also either R or a subset of R , it is called a real function.

Example 12 Let $\mathbf{N}$ be the set of natural numbers. Define a real valued function $f: \mathbf{N} \rightarrow \mathbf{N}$ by $f(x)=2 x+1$. Using this definition, complete the table given below.

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | $f(1)=\ldots$ | $f(2)=\ldots$ | $f(3)=\ldots$ | $f(4)=\ldots$ | $f(5)=\ldots$ | $f(6)=\ldots$ | $f(7)=\ldots$ |

Solution The completed table is given by

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | $f(1)=3$ | $f(2)=5$ | $f(3)=7$ | $f(4)=9$ | $f(5)=11$ | $f(6)=13$ | $f(7)=15$ |

### 2.4.1 Some functions and their graphs

(i) Identity function Let $\mathbf{R}$ be the set of real numbers. Define the real valued function $f: \mathbf{R} \rightarrow \mathbf{R}$ by $y=f(x)=x$ for each $x \in \mathbf{R}$. Such a function is called the identity function. Here the domain and range of $f$ are $\mathbf{R}$. The graph is a straight line as shown in Fig 2.8. It passes through the origin.
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-09.jpg?height=621&width=641&top_left_y=587&top_left_x=487)

Fig 2.8
(ii) Constant function Define the function $f: \mathbf{R} \rightarrow \mathbf{R}$ by $y=f(x)=c, x \in \mathbf{R}$ where $c$ is a constant and each $x \in \mathbf{R}$. Here domain of $f$ is $\mathbf{R}$ and its range is $\{c\}$.
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-09.jpg?height=722&width=699&top_left_y=1360&top_left_x=458)

Fig 2.9

The graph is a line parallel to $x$-axis. For example, if $f(x)=3$ for each $x \in \mathbf{R}$, then its graph will be a line as shown in the Fig 2.9.
(iii) Polynomial function A function $f: \mathbf{R} \rightarrow \mathbf{R}$ is said to be polynomial function if for each $x$ in $\mathbf{R}, y=f(x)=a_{0}+a_{1} x+a_{2} x^{2}+\ldots+a_{n} x^{n}$, where $n$ is a non-negative integer and $a_{0}, a_{1}, a_{2}, \ldots, a_{n} \in \mathbf{R}$.
The functions defined by $f(x)=x^{3}-x^{2}+2$, and $g(x)=x^{4}+\sqrt{2} x$ are some examples of polynomial functions, whereas the function $h$ defined by $h(x)=x^{\frac{2}{3}}+2 x$ is not a polynomial function.(Why?)

Example 13 Define the function $f: \mathbf{R} \rightarrow \mathbf{R}$ by $y=f(x)=x^{2}, x \in \mathbf{R}$. Complete the Table given below by using this definition. What is the domain and range of this function? Draw the graph of $f$.

| $x$ | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $y=f(x)=x^{2}$ |  |  |  |  |  |  |  |  |  |

Solution The completed Table is given below:

| $x$ | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $y=f(x)=x^{2}$ | 16 | 9 | 4 | 1 | 0 | 1 | 4 | 9 | 16 |

Domain of $f=\{x: x \in \mathbf{R}\}$. Range of $f=\left\{x^{2}: x \in \mathbf{R}\right\}$. The graph of $f$ is given by Fig 2.10
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-10.jpg?height=727&width=660&top_left_y=1404&top_left_x=475)

Example 14 Draw the graph of the function $\boldsymbol{f}: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=x^{3}, x \in \mathbf{R}$.
Solution We have
$f(0)=0, f(1)=1, f(-1)=-1, f(2)=8, f(-2)=-8, f(3)=27 ; f(-3)=-27$, etc.
Therefore, $f=\left\{\left(x, x^{3}\right): x \in \mathbf{R}\right\}$.
The graph of $f$ is given in Fig 2.11.
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-11.jpg?height=692&width=692&top_left_y=491&top_left_x=651)

Fig 2.11
(iv) Rational functions are functions of the type $\frac{f(x)}{g(x)}$, where $f(x)$ and $g(x)$ are polynomial functions of $x$ defined in a domain, where $g(x) \neq 0$.
Example 15 Define the real valued function $f: \mathbf{R}-\{0\} \rightarrow \mathbf{R}$ defined by $f(x)=\frac{1}{x}$, $x \in \mathbf{R}-\{0\}$. Complete the Table given below using this definition. What is the domain and range of this function?

| $x$ | -2 | -1.5 | -1 | -0.5 | 0.25 | 0.5 | 1 | 1.5 | 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y=\frac{1}{x}$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ |

Solution The completed Table is given by

| $x$ | -2 | -1.5 | -1 | -0.5 | 0.25 | 0.5 | 1 | 1.5 | 2 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $y=\frac{1}{x}$ | -0.5 | -0.67 | -1 | -2 | 4 | 2 | 1 | 0.67 | 0.5 |

The domain is all real numbers except 0 and its range is also all real numbers except 0 . The graph of $f$ is given in Fig 2.12.
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-12.jpg?height=727&width=656&top_left_y=416&top_left_x=449)

Fig 2.12
(v) The Modulus function The function $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=|x|$ for each $x \in \mathbf{R}$ is called modulus function. For each non-negative value of $x, f(x)$ is equal to $x$. But for negative values of $x$, the value of $f(x)$ is the negative of the value of $x$, i.e.,

$$
f(x)=\left\{\begin{array}{l}
x, x \geq 0 \\
-x, x<0
\end{array}\right.
$$

The graph of the modulus function is given in Fig 2.13.
(vi) Signum function The function $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by

$$
f(x)=\left\{\begin{array}{l}
1, \text { if } x>0 \\
0, \text { if } x=0 \\
-1, \text { if } x<0
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-12.jpg?height=700&width=658&top_left_y=1204&top_left_x=812)

Fig 2.13
is called the signum function. The domain of the signum function is $\mathbf{R}$ and the range is the set $\{-1,0,1\}$. The graph of the signum function is given by the Fig 2.14.
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-13.jpg?height=485&width=532&top_left_y=430&top_left_x=541)

Fig 2.14
(vii) Greatest integer function The function $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=[x], x \in \mathbf{R}$ assumes the value of the greatest integer, less than or equal to $x$. Such a function is called the greatest integer function.

From the definition of $[x]$, we can see that

$$
\begin{aligned}
& {[x]=-1 \text { for }-1 \leq x<0} \\
& {[x]=0 \text { for } 0 \leq x<1} \\
& {[x]=1 \text { for } 1 \leq x<2} \\
& {[x]=2 \text { for } 2 \leq x<3 \text { and }}
\end{aligned}
$$

so on.
The graph of the function is
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-13.jpg?height=676&width=796&top_left_y=975&top_left_x=669)

Fig 2.15 shown in Fig 2.15.
2.4.2 Algebra of real functions In this Section, we shall learn how to add two real functions, subtract a real function from another, multiply a real function by a scalar (here by a scalar we mean a real number), multiply two real functions and divide one real function by another.
(i) Addition of two real functions Let $f: \mathrm{X} \rightarrow \mathbf{R}$ and $g: \mathrm{X} \rightarrow \mathbf{R}$ be any two real functions, where $\mathrm{X} \subset \mathbf{R}$. Then, we define $(f+g): \mathrm{X} \rightarrow \mathbf{R}$ by $(f+g)(x)=f(x)+g(x)$, for all $x \in X$.
(ii) Subtraction of a real function from another Let $f: \mathrm{X} \rightarrow \mathbf{R}$ and $g: \mathrm{X} \rightarrow \mathbf{R}$ be any two real functions, where $\mathrm{X} \subset \mathbf{R}$. Then, we define $(f-g): \mathrm{X} \rightarrow \mathbf{R}$ by $(f-g)(x)=f(x)-g(x)$, for all $x \in \mathrm{X}$.
(iii) Multiplication by a scalar Let $f: \mathrm{X} \rightarrow \mathbf{R}$ be a real valued function and $\alpha$ be a scalar. Here by scalar, we mean a real number. Then the product $\alpha f$ is a function from X to $\mathbf{R}$ defined by $(\alpha f)(x)=\alpha f(x), x \in \mathrm{X}$.
(iv) Multiplication of two real functions The product (or multiplication) of two real functions $f: X \rightarrow \mathbf{R}$ and $g: X \rightarrow \mathbf{R}$ is a function $f g: X \rightarrow \mathbf{R}$ defined by $(f g)(x)=f(x) g(x)$, for all $x \in \mathrm{X}$.
This is also called pointwise multiplication.
(v) Quotient of two real functions Let $f$ and $g$ be two real functions defined from $\mathrm{X} \rightarrow \mathbf{R}$, where $\mathrm{X} \subset \mathbf{R}$. The quotient of $f$ by $g$ denoted by $\frac{f}{g}$ is a function defined by, $\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}$, provided $g(x) \neq 0, x \in \mathrm{X}$
Example 16 Let $f(x)=x^{2}$ and $g(x)=2 x+1$ be two real functions.Find

$$
(f+g)(x),(f-g)(x),(f g)(x),\left(\frac{f}{g}\right)(x)
$$

Solution We have,

$$
\begin{aligned}
& (f+g)(x)=x^{2}+2 x+1,(f-g)(x)=x^{2}-2 x-1 \\
& (f g)(x)=x^{2}(2 x+1)=2 x^{3}+x^{2},\left(\frac{f}{g}\right)(x)=\frac{x^{2}}{2 x+1}, x \neq-\frac{1}{2}
\end{aligned}
$$

Example 17 Let $f(x)=\sqrt{x}$ and $g(x)=x$ be two functions defined over the set of nonnegative real numbers. Find $(f+g)(x),(f-g)(x),(f g)(x)$ and $\left(\frac{f}{g}\right)(x)$.
Solution We have

$$
\begin{aligned}
& (f+g)(x)=\sqrt{x}+x,(f-g)(x)=\sqrt{x}-x \\
& (f g) x=\sqrt{x}(x)=x^{\frac{3}{2}} \text { and }\left(\frac{f}{g}\right)(x)=\frac{\sqrt{x}}{x}=x^{-\frac{1}{2}}, x \neq 0
\end{aligned}
$$

## EXERCISE 2.3

1. Which of the following relations are functions? Give reasons. If it is a function, determine its domain and range.
(i) $\{(2,1),(5,1),(8,1),(11,1),(14,1),(17,1)\}$
(ii) $\{(2,1),(4,2),(6,3),(8,4),(10,5),(12,6),(14,7)\}$
(iii) $\{(1,3),(1,5),(2,5)\}$.
2. Find the domain and range of the following real functions:
(i) $f(x)=-|x|$
(ii) $f(x)=\sqrt{9-x^{2}}$.
3. A function $f$ is defined by $f(x)=2 x-5$. Write down the values of
(i) $\quad f(0)$,
(ii) $f(7)$,
(iii) $f(-3)$.
4. The function ' $t$ ' which maps temperature in degree Celsius into temperature in degree Fahrenheit is defined by $t(\mathrm{C})=\frac{9 \mathrm{C}}{5}+32$.
Find (i) $t(0)$ (ii) $t(28)$ (iii) $t(-10)$ (iv) The value of C , when $t(\mathrm{C})=212$.
5. Find the range of each of the following functions.
(i) $f(x)=2-3 x, x \in \mathbf{R}, x>0$.
(ii) $f(x)=x^{2}+2, x$ is a real number.
(iii) $f(x)=x, x$ is a real number.

## Miscellaneous Examples

Example 18 Let $\mathbf{R}$ be the set of real numbers. Define the real function

$$
f: \mathbf{R} \rightarrow \mathbf{R} \text { by } f(x)=x+10
$$

and sketch the graph of this function.
Solution Here $f(0)=10, f(1)=11, f(2)=12, \ldots$, $f(10)=20$, etc., and $f(-1)=9, f(-2)=8, \ldots, f(-10)=0$ and so on.
Therefore, shape of the graph of the given function assumes the form as shown in Fig 2.16.

Remark The function $f$ defined by $f(x)=m x+c$, $x \in \mathbf{R}$, is called linear function, where $m$ and $c$ are constants. Above function is an example of a linear function.
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-15.jpg?height=581&width=502&top_left_y=1472&top_left_x=967)

Fig 2.16

Example 19 Let R be a relation from $\mathbf{Q}$ to $\mathbf{Q}$ defined by $\mathrm{R}=\{(a, b): a, b \in \mathbf{Q}$ and $a-b \in \mathbf{Z}\}$. Show that
(i) $(a, a) \in \mathrm{R}$ for all $a \in \mathbf{Q}$
(ii) $(a, b) \in \mathrm{R}$ implies that $(b, a) \in \mathrm{R}$
(iii) $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R}$ implies that $(a, c) \in \mathrm{R}$

Solution (i) Since, $a-a=0 \in \mathbf{Z}$, if follows that $(a, a) \in \mathrm{R}$.
(ii) $(a, b) \in \mathrm{R}$ implies that $a-b \in \mathbf{Z}$. So, $b-a \in \mathbf{Z}$. Therefore, $(b, a) \in \mathrm{R}$
(iii) $(a, b)$ and $(b, c) \in \mathrm{R}$ implies that $a-b \in \mathbf{Z} . b-c \in \mathbf{Z}$. So, $a-c=(a-b)+(b-c) \in \mathbf{Z}$. Therefore, $(a, c) \in \mathrm{R}$

Example 20 Let $f=\{(1,1),(2,3),(0,-1),(-1,-3)\}$ be a linear function from $\mathbf{Z}$ into $\mathbf{Z}$. Find $f(x)$.

Solution Since $f$ is a linear function, $f(x)=m x+c$. Also, since $(1,1),(0,-1) \in \mathrm{R}$, $f(1)=m+c=1$ and $f(0)=c=-1$. This gives $m=2$ and $f(x)=2 x-1$.

Example 21 Find the domain of the function $f(x)=\frac{x^{2}+3 x+5}{x^{2}-5 x+4}$
Solution Since $x^{2}-5 x+4=(x-4)(x-1)$, the function $f$ is defined for all real numbers except at $x=4$ and $x=1$. Hence the domain of $f$ is $\mathbf{R}-\{1,4\}$.

Example 22 The function $f$ is defined by

$$
f(x)= \begin{cases}1-x, & x<0 \\ 1, & x=0 \\ x+1, & x>0\end{cases}
$$

Draw the graph of $f(x)$.
Solution Here, $f(x)=1-x, x<0$, this gives

$$
\begin{aligned}
& f(-4)=1-(-4)=5 \\
& f(-3)=1-(-3)=4 \\
& f(-2)=1-(-2)=3 \\
& f(-1)=1-(-1)=2 ; \text { etc }
\end{aligned}
$$

and $f(1)=2, f(2)=3, f(3)=4$
$f(4)=5$ and so on for $f(x)=x+1, x>0$.
Thus, the graph of $f$ is as shown in Fig 2.17
![](https://cdn.mathpix.com/cropped/2025_07_21_46cc3e7fd99566e6cb95g-16.jpg?height=688&width=607&top_left_y=1379&top_left_x=868)

Fig 2.17

## Miscellaneous Exercise on Chapter 2

1. The relation $f$ is defined by $f(x)=\left\{\begin{array}{l}x^{2}, 0 \leq x \leq 3 \\ 3 x, 3 \leq x \leq 10\end{array}\right.$

The relation $g$ is defined by $g(x)= \begin{cases}x^{2}, & 0 \leq x \leq 2 \\ 3 x, & 2 \leq x \leq 10\end{cases}$
Show that $f$ is a function and $g$ is not a function.
2. If $f(x)=x^{2}$, find $\frac{f(1.1)-f(1)}{(1.1-1)}$.
3. Find the domain of the function $f(x)=\frac{x^{2}+2 x+1}{x^{2}-8 x+12}$.
4. Find the domain and the range of the real function $f$ defined by $f(x)=\sqrt{(x-1)}$.
5. Find the domain and the range of the real function $f$ defined by $f(x)=|x-1|$.
6. Let $f=\left\{\left(x, \frac{x^{2}}{1+x^{2}}\right): x \in \mathbf{R}\right\}$ be a function from $\mathbf{R}$ into $\mathbf{R}$. Determine the range of $f$.
7. Let $f, g: \mathbf{R} \rightarrow \mathbf{R}$ be defined, respectively by $f(x)=x+1, g(x)=2 x-3$. Find $f+g, f-g$ and $\frac{f}{g}$.
8. Let $f=\{(1,1),(2,3),(0,-1),(-1,-3)\}$ be a function from $\mathbf{Z}$ to $\mathbf{Z}$ defined by $f(x)=a x+b$, for some integers $a, b$. Determine $a, b$.
9. Let R be a relation from $\mathbf{N}$ to $\mathbf{N}$ defined by $\mathrm{R}=\left\{(a, b): a, b \in \mathbf{N}\right.$ and $\left.a=b^{2}\right\}$. Are the following true?
(i) $(a, a) \in \mathrm{R}$, for all $a \in \mathbf{N}$
(ii) $(a, b) \in \mathrm{R}$, implies $(b, a) \in \mathrm{R}$
(iii) $(a, b) \in \mathrm{R},(b, c) \in \mathrm{R}$ implies $(a, c) \in \mathrm{R}$.

Justify your answer in each case.
10. Let $\mathrm{A}=\{1,2,3,4\}, \mathrm{B}=\{1,5,9,11,15,16\}$ and $f=\{(1,5),(2,9),(3,1),(4,5),(2,11)\}$ Are the following true?
(i) $f$ is a relation from A to B
(ii) $f$ is a function from A to B .

Justify your answer in each case.
11. Let $f$ be the subset of $\mathbf{Z} \times \mathbf{Z}$ defined by $f=\{(a b, a+b): a, b \in \mathbf{Z}\}$. Is $f$ a function from $\mathbf{Z}$ to $\mathbf{Z}$ ? Justify your answer.
12. Let $\mathrm{A}=\{9,10,11,12,13\}$ and let $f: \mathrm{A} \rightarrow \mathbf{N}$ be defined by $f(n)=$ the highest prime factor of $n$. Find the range of $f$.

## Summary

In this Chapter, we studied about relations and functions. The main features of this Chapter are as follows:

- Ordered pair A pair of elements grouped together in a particular order.
- Cartesian product $\mathrm{A} \times \mathrm{B}$ of two sets A and B is given by
$\mathrm{A} \times \mathrm{B}=\{(a, b): a \in \mathrm{~A}, b \in \mathrm{~B}\}$
In particular $\mathbf{R} \times \mathbf{R}=\{(x, y): x, y \in \mathbf{R}\}$
and $\mathbf{R} \times \mathbf{R} \times \mathbf{R}=\{(x, y, z): x, y, z \in \mathbf{R}\}$
If $(a, b)=(x, y)$, then $a=x$ and $b=y$.
If $n(\mathrm{~A})=p$ and $n(\mathrm{~B})=q$, then $n(\mathrm{~A} \times \mathrm{B})=p q$.
- $\mathrm{A} \times \phi=\phi$
- In general, $\mathrm{A} \times \mathrm{B} \neq \mathrm{B} \times \mathrm{A}$.
- Relation A relation R from a set A to a set B is a subset of the cartesian product $\mathrm{A} \times \mathrm{B}$ obtained by describing a relationship between the first element $x$ and the second element $y$ of the ordered pairs in $\mathrm{A} \times \mathrm{B}$.
- The image of an element $x$ under a relation R is given by $y$, where $(x, y) \in \mathrm{R}$,
- The domain of R is the set of all first elements of the ordered pairs in a relation R .
- The range of the relation R is the set of all second elements of the ordered pairs in a relation R .
- Function A function $f$ from a set A to a set B is a specific type of relation for which every element $x$ of set A has one and only one image $y$ in set B .
We write $f$ : $\mathrm{A} \rightarrow \mathrm{B}$, where $f(x)=y$.
- A is the domain and B is the codomain of $f$.
- The range of the function is the set of images.
- A real function has the set of real numbers or one of its subsets both as its domain and as its range.
Algebra of functions For functions $f: \mathrm{X} \rightarrow \mathbf{R}$ and $g: \mathrm{X} \rightarrow \mathbf{R}$, we have

$$
\begin{aligned}
& (f+g)(x)=f(x)+g(x), x \in \mathrm{X} \\
& (f-g)(x)=f(x)-g(x), x \in \mathrm{X} \\
& (f . g)(x) \quad=f(x) . g(x), x \in \mathrm{X} \\
& (k f)(x) \quad=k(f(x)), x \in \mathrm{X}, \text { where } k \text { is a real number. } \\
& \left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}, x \in \mathrm{X}, g(x) \neq 0
\end{aligned}
$$

## Historical Note

The word FUNCTION first appears in a Latin manuscript "Methodus tangentium inversa, seu de fuctionibus" written by Gottfried Wilhelm Leibnitz (1646-1716) in 1673; Leibnitz used the word in the non-analytical sense. He considered a function in terms of "mathematical job" - the "employee" being just a curve.

On July 5, 1698, Johan Bernoulli, in a letter to Leibnitz, for the first time deliberately assigned a specialised use of the term function in the analytical sense. At the end of that month, Leibnitz replied showing his approval.

Function is found in English in 1779 in Chambers' Cyclopaedia: "The term function is used in algebra, for an analytical expression any way compounded of a variable quantity, and of numbers, or constant quantities".

