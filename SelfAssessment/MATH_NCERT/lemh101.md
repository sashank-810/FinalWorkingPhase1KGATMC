## RELATIONS AND FUNCTIONS

There is no permanent place in the world for ugly mathematics ... . It may be very hard to define mathematical beauty but that is just as true of beauty of any kind, we may not know quite what we mean by a beautiful poem, but that does not prevent us from recognising one when we read it. - G. H. HARDY

### 1.1 Introduction

Recall that the notion of relations and functions, domain, co-domain and range have been introduced in Class XI along with different types of specific real valued functions and their graphs. The concept of the term 'relation' in mathematics has been drawn from the meaning of relation in English language, according to which two objects or quantities are related if there is a recognisable connection or link between the two objects or quantities. Let A be the set of students of Class XII of a school and B be the set of students of Class XI of the same school. Then some of the examples of relations from A to B are
(i) $\{(a, b) \in \mathrm{A} \times \mathrm{B}: a$ is brother of $b\}$,
(ii) $\{(a, b) \in \mathrm{A} \times \mathrm{B}: a$ is sister of $b\}$,
![](https://cdn.mathpix.com/cropped/2025_07_21_e122063659afbdd12741g-01.jpg?height=532&width=412&top_left_y=945&top_left_x=1042)

Lejeune Dirichlet
(1805-1859)
(iii) $\{(a, b) \in \mathrm{A} \times \mathrm{B}$ : age of $a$ is greater than age of $b\}$,
(iv) $\{(a, b) \in \mathrm{A} \times \mathrm{B}$ : total marks obtained by $a$ in the final examination is less than the total marks obtained by $b$ in the final examination $\}$,
(v) $\quad\{(a, b) \in \mathrm{A} \times \mathrm{B}$ : $a$ lives in the same locality as $b\}$. However, abstracting from this, we define mathematically a relation R from A to B as an arbitrary subset of $\mathrm{A} \times \mathrm{B}$.
If $(a, b) \in \mathrm{R}$, we say that $a$ is related to $b$ under the relation R and we write as $a \mathrm{R} b$. In general, $(a, b) \in \mathrm{R}$, we do not bother whether there is a recognisable connection or link between $a$ and $b$. As seen in Class XI, functions are special kind of relations.

In this chapter, we will study different types of relations and functions, composition of functions, invertible functions and binary operations.

### 1.2 Types of Relations

In this section, we would like to study different types of relations. We know that a relation in a set A is a subset of $\mathrm{A} \times \mathrm{A}$. Thus, the empty set $\phi$ and $\mathrm{A} \times \mathrm{A}$ are two extreme relations. For illustration, consider a relation R in the set $\mathrm{A}=\{1,2,3,4\}$ given by $\mathrm{R}=\{(a, b): a-b=10\}$. This is the empty set, as no pair $(a, b)$ satisfies the condition $a-b=10$. Similarly, $\mathrm{R}^{\prime}=\{(a, b):|a-b| \geq 0\}$ is the whole set $\mathrm{A} \times \mathrm{A}$, as all pairs $(a, b)$ in $\mathrm{A} \times \mathrm{A}$ satisfy $|a-b| \geq 0$. These two extreme examples lead us to the following definitions.

Definition 1 A relation R in a set A is called empty relation, if no element of A is related to any element of A, i.e., $\mathrm{R}=\phi \subset \mathrm{A} \times \mathrm{A}$.
Definition 2 A relation $R$ in a set $A$ is called universal relation, if each element of $A$ is related to every element of A, i.e., $\mathrm{R}=\mathrm{A} \times \mathrm{A}$.

Both the empty relation and the universal relation are some times called trivial relations.

Example 1 Let A be the set of all students of a boys school. Show that the relation R in A given by $\mathrm{R}=\{(a, b): a$ is sister of $b\}$ is the empty relation and $\mathrm{R}^{\prime}=\{(a, b):$ the difference between heights of $a$ and $b$ is less than 3 meters $\}$ is the universal relation.

Solution Since the school is boys school, no student of the school can be sister of any student of the school. Hence, $\mathrm{R}=\phi$, showing that R is the empty relation. It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that $\mathrm{R}^{\prime}=\mathrm{A} \times \mathrm{A}$ is the universal relation.

Remark In Class XI, we have seen two ways of representing a relation, namely raster method and set builder method. However, a relation $R$ in the set $\{1,2,3,4\}$ defined by $R$ $=\{(a, b): b=a+1\}$ is also expressed as $a \mathrm{R} b$ if and only if $b=a+1$ by many authors. We may also use this notation, as and when convenient.

If $(a, b) \in \mathrm{R}$, we say that $a$ is related to $b$ and we denote it as $a \mathrm{R} b$.
One of the most important relation, which plays a significant role in Mathematics, is an equivalence relation. To study equivalence relation, we first consider three types of relations, namely reflexive, symmetric and transitive.
Definition 3 A relation R in a set A is called
(i) reflexive, if $(a, a) \in \mathrm{R}$, for every $a \in \mathrm{~A}$,
(ii) symmetric, if $\left(a_{1}, a_{2}\right) \in \mathrm{R}$ implies that $\left(a_{2}, a_{1}\right) \in \mathrm{R}$, for all $a_{1}, a_{2} \in \mathrm{~A}$.
(iii) transitive, if $\left(a_{1}, a_{2}\right) \in \mathrm{R}$ and $\left(a_{2}, a_{3}\right) \in \mathrm{R}$ implies that $\left(a_{1}, a_{3}\right) \in \mathrm{R}$, for all $a_{1}, a_{2}$, $a_{3} \in \mathrm{~A}$.

Definition 4 A relation $R$ in a set $A$ is said to be an equivalence relation if $R$ is reflexive, symmetric and transitive.

Example 2 Let T be the set of all triangles in a plane with R a relation in T given by $\mathrm{R}=\left\{\left(\mathrm{T}_{1}, \mathrm{~T}_{2}\right): \mathrm{T}_{1}\right.$ is congruent to $\left.\mathrm{T}_{2}\right\}$. Show that R is an equivalence relation.

Solution $R$ is reflexive, since every triangle is congruent to itself. Further, $\left(T_{1}, T_{2}\right) \in R \Rightarrow T_{1}$ is congruent to $T_{2} \Rightarrow T_{2}$ is congruent to $T_{1} \Rightarrow\left(T_{2}, T_{1}\right) \in R$. Hence, $R$ is symmetric. Moreover, $\left(T_{1}, T_{2}\right),\left(T_{2}, T_{3}\right) \in R \Rightarrow T_{1}$ is congruent to $T_{2}$ and $T_{2}$ is congruent to $T_{3} \Rightarrow T_{1}$ is congruent to $T_{3} \Rightarrow\left(T_{1}, T_{3}\right) \in R$. Therefore, $R$ is an equivalence relation.

Example 3 Let L be the set of all lines in a plane and R be the relation in L defined as $\mathrm{R}=\left\{\left(\mathrm{L}_{1}, \mathrm{~L}_{2}\right): \mathrm{L}_{1}\right.$ is perpendicular to $\left.\mathrm{L}_{2}\right\}$. Show that R is symmetric but neither reflexive nor transitive.

Solution R is not reflexive, as a line $\mathrm{L}_{1}$ can not be perpendicular to itself, i.e., ( $\mathrm{L}_{1}, \mathrm{~L}_{1}$ ) $\notin R$. $R$ is symmetric as $\left(L_{1}, L_{2}\right) \in R$
$\Rightarrow \quad \mathrm{L}_{1}$ is perpendicular to $\mathrm{L}_{2}$
$\Rightarrow \quad \mathrm{L}_{2}$ is perpendicular to $\mathrm{L}_{1}$
$\Rightarrow \quad\left(\mathrm{L}_{2}, \mathrm{~L}_{1}\right) \in \mathrm{R}$.
R is not transitive. Indeed, if $\mathrm{L}_{1}$ is perpendicular to $\mathrm{L}_{2}$ and
![](https://cdn.mathpix.com/cropped/2025_07_21_e122063659afbdd12741g-03.jpg?height=210&width=344&top_left_y=1048&top_left_x=1120)

Fig 1.1 $\mathrm{L}_{2}$ is perpendicular to $\mathrm{L}_{3}$, then $\mathrm{L}_{1}$ can never be perpendicular to $\mathrm{L}_{3}$. In fact, $\mathrm{L}_{1}$ is parallel to $\mathrm{L}_{3}$, i.e., $\left(\mathrm{L}_{1}, \mathrm{~L}_{2}\right) \in \mathrm{R},\left(\mathrm{L}_{2}, \mathrm{~L}_{3}\right) \in \mathrm{R}$ but $\left(\mathrm{L}_{1}, \mathrm{~L}_{3}\right) \notin \mathrm{R}$.
Example 4 Show that the relation R in the set $\{1,2,3\}$ given by $\mathrm{R}=\{(1,1),(2,2)$, $(3,3),(1,2),(2,3)\}$ is reflexive but neither symmetric nor transitive.

Solution $R$ is reflexive, since $(1,1),(2,2)$ and $(3,3)$ lie in $R$. Also, $R$ is not symmetric, as $(1,2) \in R$ but $(2,1) \notin R$. Similarly, $R$ is not transitive, as $(1,2) \in R$ and $(2,3) \in R$ but $(1,3) \notin \mathrm{R}$.

Example 5 Show that the relation R in the set $\mathbf{Z}$ of integers given by

$$
\mathrm{R}=\{(a, b): 2 \text { divides } a-b\}
$$

is an equivalence relation.
Solution R is reflexive, as 2 divides ( $a-a$ ) for all $a \in \mathbf{Z}$. Further, if ( $a, b$ ) $\in \mathrm{R}$, then 2 divides $a-b$. Therefore, 2 divides $b-a$. Hence, $(b, a) \in \mathrm{R}$, which shows that R is symmetric. Similarly, if $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R}$, then $a-b$ and $b-c$ are divisible by 2. Now, $a-c=(a-b)+(b-c)$ is even (Why?). So, $(a-c)$ is divisible by 2 . This shows that R is transitive. Thus, R is an equivalence relation in $\mathbf{Z}$.

In Example 5, note that all even integers are related to zero, as $(0, \pm 2),(0, \pm 4)$ etc., lie in R and no odd integer is related to 0 , as $(0, \pm 1),(0, \pm 3)$ etc., do not lie in R . Similarly, all odd integers are related to one and no even integer is related to one. Therefore, the set E of all even integers and the set O of all odd integers are subsets of $\mathbf{Z}$ satisfying following conditions:
(i) All elements of E are related to each other and all elements of O are related to each other.
(ii) No element of E is related to any element of O and vice-versa.
(iii) E and O are disjoint and $\mathbf{Z}=\mathrm{E} \cup \mathrm{O}$.

The subset E is called the equivalence class containing zero and is denoted by [0]. Similarly, O is the equivalence class containing 1 and is denoted by [1]. Note that $[0] \neq[1],[0]=[2 r]$ and $[1]=[2 r+1], r \in \mathbf{Z}$. Infact, what we have seen above is true for an arbitrary equivalence relation R in a set X . Given an arbitrary equivalence relation $R$ in an arbitrary set $X, R$ divides $X$ into mutually disjoint subsets $A_{i}$ called partitions or subdivisions of $X$ satisfying:
(i) all elements of $\mathrm{A}_{i}$ are related to each other, for all $i$.
(ii) no element of $\mathrm{A}_{i}$ is related to any element of $\mathrm{A}_{j}, i \neq j$.
(iii) $\cup \mathrm{A}_{j}=\mathrm{X}$ and $\mathrm{A}_{i} \cap \mathrm{~A}_{j}=\phi, i \neq j$.

The subsets $\mathrm{A}_{i}$ are called equivalence classes. The interesting part of the situation is that we can go reverse also. For example, consider a subdivision of the set $\mathbf{Z}$ given by three mutually disjoint subsets $A_{1}, A_{2}$ and $A_{3}$ whose union is $\mathbf{Z}$ with

$$
\begin{aligned}
& \mathrm{A}_{1}=\{x \in \mathbf{Z}: x \text { is a multiple of } 3\}=\{\ldots,-6,-3,0,3,6, \ldots\} \\
& \mathrm{A}_{2}=\{x \in \mathbf{Z}: x-1 \text { is a multiple of } 3\}=\{\ldots,-5,-2,1,4,7, \ldots\} \\
& \mathrm{A}_{3}=\{x \in \mathbf{Z}: x-2 \text { is a multiple of } 3\}=\{\ldots,-4,-1,2,5,8, \ldots\}
\end{aligned}
$$

Define a relation R in $\mathbf{Z}$ given by $\mathrm{R}=\{(a, b): 3$ divides $a-b\}$. Following the arguments similar to those used in Example 5, we can show that R is an equivalence relation. Also, $A_{1}$ coincides with the set of all integers in $\mathbf{Z}$ which are related to zero, $A_{2}$ coincides with the set of all integers which are related to 1 and $A_{3}$ coincides with the set of all integers in $\mathbf{Z}$ which are related to 2 . Thus, $A_{1}=[0], A_{2}=[1]$ and $A_{3}=[2]$. In fact, $\mathrm{A}_{1}=[3 r], \mathrm{A}_{2}=[3 r+1]$ and $\mathrm{A}_{3}=[3 r+2]$, for all $r \in \mathbf{Z}$.

Example 6 Let R be the relation defined in the set $\mathrm{A}=\{1,2,3,4,5,6,7\}$ by $\mathrm{R}=\{(a, b)$ : both $a$ and $b$ are either odd or even $\}$. Show that R is an equivalence relation. Further, show that all the elements of the subset $\{1,3,5,7\}$ are related to each other and all the elements of the subset $\{2,4,6\}$ are related to each other, but no element of the subset $\{1,3,5,7\}$ is related to any element of the subset $\{2,4,6\}$.

Solution Given any element $a$ in A , both $a$ and $a$ must be either odd or even, so that $(a, a) \in \mathrm{R}$. Further, $(a, b) \in \mathrm{R} \Rightarrow$ both $a$ and $b$ must be either odd or even $\Rightarrow(b, a) \in \mathrm{R}$. Similarly, $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R} \Rightarrow$ all elements $a, b, c$, must be either even or odd simultaneously $\Rightarrow(a, c) \in \mathrm{R}$. Hence, R is an equivalence relation. Further, all the elements of $\{1,3,5,7\}$ are related to each other, as all the elements of this subset are odd. Similarly, all the elements of the subset $\{2,4,6\}$ are related to each other, as all of them are even. Also, no element of the subset $\{1,3,5,7\}$ can be related to any element of $\{2,4,6\}$, as elements of $\{1,3,5,7\}$ are odd, while elements of $\{2,4,6\}$ are even.

## EXERCISE 1.1

1. Determine whether each of the following relations are reflexive, symmetric and transitive:
(i) Relation R in the set $\mathrm{A}=\{1,2,3, \ldots, 13,14\}$ defined as

$$
\mathrm{R}=\{(x, y): 3 x-y=0\}
$$

(ii) Relation R in the set $\mathbf{N}$ of natural numbers defined as

$$
\mathrm{R}=\{(x, y): y=x+5 \text { and } x<4\}
$$

(iii) Relation R in the set $\mathrm{A}=\{1,2,3,4,5,6\}$ as

$$
\mathrm{R}=\{(x, y): y \text { is divisible by } x\}
$$

(iv) Relation R in the set $\mathbf{Z}$ of all integers defined as

$$
\mathrm{R}=\{(x, y): x-y \text { is an integer }\}
$$

(v) Relation R in the set A of human beings in a town at a particular time given by
(a) $\mathrm{R}=\{(x, y): x$ and $y$ work at the same place $\}$
(b) $\mathrm{R}=\{(x, y): x$ and $y$ live in the same locality $\}$
(c) $\mathrm{R}=\{(x, y): x$ is exactly 7 cm taller than $y\}$
(d) $\mathrm{R}=\{(x, y): x$ is wife of $y\}$
(e) $\mathrm{R}=\{(x, y): x$ is father of $y\}$
2. Show that the relation R in the set $\mathbf{R}$ of real numbers, defined as $\mathrm{R}=\left\{(a, b): a \leq b^{2}\right\}$ is neither reflexive nor symmetric nor transitive.
3. Check whether the relation $R$ defined in the set $\{1,2,3,4,5,6\}$ as $\mathrm{R}=\{(a, b): b=a+1\}$ is reflexive, symmetric or transitive.
4. Show that the relation R in $\mathbf{R}$ defined as $\mathrm{R}=\{(a, b): a \leq b\}$, is reflexive and transitive but not symmetric.
5. Check whether the relation R in $\mathbf{R}$ defined by $\mathrm{R}=\left\{(a, b): a \leq b^{3}\right\}$ is reflexive, symmetric or transitive.
6. Show that the relation R in the set $\{1,2,3\}$ given by $\mathrm{R}=\{(1,2),(2,1)\}$ is symmetric but neither reflexive nor transitive.
7. Show that the relation R in the set A of all the books in a library of a college, given by $\mathrm{R}=\{(x, y): x$ and $y$ have same number of pages $\}$ is an equivalence relation.
8. Show that the relation $R$ in the set $A=\{1,2,3,4,5\}$ given by
$\mathrm{R}=\{(a, b):|a-b|$ is even $\}$, is an equivalence relation. Show that all the elements of $\{1,3,5\}$ are related to each other and all the elements of $\{2,4\}$ are related to each other. But no element of $\{1,3,5\}$ is related to any element of $\{2,4\}$.
9. Show that each of the relation R in the set $\mathrm{A}=\{x \in \mathbf{Z}: 0 \leq x \leq 12\}$, given by
(i) $\mathrm{R}=\{(a, b):|a-b|$ is a multiple of 4$\}$
(ii) $\mathrm{R}=\{(a, b): a=b\}$
is an equivalence relation. Find the set of all elements related to 1 in each case.
10. Give an example of a relation. Which is
(i) Symmetric but neither reflexive nor transitive.
(ii) Transitive but neither reflexive nor symmetric.
(iii) Reflexive and symmetric but not transitive.
(iv) Reflexive and transitive but not symmetric.
(v) Symmetric and transitive but not reflexive.
11. Show that the relation $R$ in the set $A$ of points in a plane given by $\mathrm{R}=\{(\mathrm{P}, \mathrm{Q})$ : distance of the point P from the origin is same as the distance of the point Q from the origin\}, is an equivalence relation. Further, show that the set of all points related to a point $\mathrm{P} \neq(0,0)$ is the circle passing through P with origin as centre.
12. Show that the relation R defined in the set A of all triangles as $\mathrm{R}=\left\{\left(\mathrm{T}_{1}, \mathrm{~T}_{2}\right): \mathrm{T}_{1}\right.$ is similar to $\mathrm{T}_{2}$ \}, is equivalence relation. Consider three right angle triangles $\mathrm{T}_{1}$ with sides $3,4,5, \mathrm{~T}_{2}$ with sides $5,12,13$ and $\mathrm{T}_{3}$ with sides $6,8,10$. Which triangles among $\mathrm{T}_{1}, \mathrm{~T}_{2}$ and $\mathrm{T}_{3}$ are related?
13. Show that the relation R defined in the set A of all polygons as $\mathrm{R}=\left\{\left(\mathrm{P}_{1}, \mathrm{P}_{2}\right)\right.$ : $P_{1}$ and $P_{2}$ have same number of sides\}, is an equivalence relation. What is the set of all elements in A related to the right angle triangle T with sides 3,4 and 5 ?
14. Let $L$ be the set of all lines in $X Y$ plane and $R$ be the relation in $L$ defined as $\mathrm{R}=\left\{\left(\mathrm{L}_{1}, \mathrm{~L}_{2}\right): \mathrm{L}_{1}\right.$ is parallel to $\left.\mathrm{L}_{2}\right\}$. Show that R is an equivalence relation. Find the set of all lines related to the line $y=2 x+4$.
15. Let $R$ be the relation in the set $\{1,2,3,4\}$ given by $R=\{(1,2),(2,2),(1,1),(4,4)$, $(1,3),(3,3),(3,2)\}$. Choose the correct answer.
(A) R is reflexive and symmetric but not transitive.
(B) R is reflexive and transitive but not symmetric.
(C) R is symmetric and transitive but not reflexive.
(D) R is an equivalence relation.
16. Let R be the relation in the set $\mathbf{N}$ given by $\mathrm{R}=\{(a, b): a=b-2, b>6\}$. Choose the correct answer.
(A) $(2,4) \in \mathrm{R}$
(B) $(3,8) \in R$
(C) $(6,8) \in \mathrm{R}$
(D) $(8,7) \in R$

### 1.3 Types of Functions

The notion of a function along with some special functions like identity function, constant function, polynomial function, rational function, modulus function, signum function etc. along with their graphs have been given in Class XI.

Addition, subtraction, multiplication and division of two functions have also been studied. As the concept of function is of paramount importance in mathematics and among other disciplines as well, we would like to extend our study about function from where we finished earlier. In this section, we would like to study different types of functions.

Consider the functions $f_{1}, f_{2}, f_{3}$ and $f_{4}$ given by the following diagrams.
In Fig 1.2, we observe that the images of distinct elements of $\mathrm{X}_{1}$ under the function $f_{1}$ are distinct, but the image of two distinct elements 1 and 2 of $\mathrm{X}_{1}$ under $f_{2}$ is same, namely $b$. Further, there are some elements like $e$ and $f$ in $\mathrm{X}_{2}$ which are not images of any element of $\mathrm{X}_{1}$ under $f_{1}$, while all elements of $\mathrm{X}_{3}$ are images of some elements of $\mathrm{X}_{1}$ under $f_{3}$. The above observations lead to the following definitions:
Definition 5 A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is defined to be one-one (or injective), if the images of distinct elements of X under $f$ are distinct, i.e., for every $x_{1}, x_{2} \in \mathrm{X}, f\left(x_{1}\right)=f\left(x_{2}\right)$ implies $x_{1}=x_{2}$. Otherwise, $f$ is called many-one.

The function $f_{1}$ and $f_{4}$ in Fig 1.2 (i) and (iv) are one-one and the function $f_{2}$ and $f_{3}$ in Fig 1.2 (ii) and (iii) are many-one.
Definition 6 A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is said to be onto (or surjective), if every element of Y is the image of some element of X under $f$, i.e., for every $y \in \mathrm{Y}$, there exists an element $x$ in X such that $f(x)=y$.

The function $f_{3}$ and $f_{4}$ in Fig 1.2 (iii), (iv) are onto and the function $f_{1}$ in Fig 1.2 (i) is not onto as elements $e, f$ in $\mathrm{X}_{2}$ are not the image of any element in $\mathrm{X}_{1}$ under $f_{1}$.
![](https://cdn.mathpix.com/cropped/2025_07_21_e122063659afbdd12741g-08.jpg?height=806&width=1242&top_left_y=321&top_left_x=191)

Fig 1.2 (i) to (iv)
Remark $f: \mathrm{X} \rightarrow \mathrm{Y}$ is onto if and only if Range of $f=\mathrm{Y}$.
Definition 7 A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is said to be one-one and onto (or bijective), if $f$ is both one-one and onto.

The function $f_{4}$ in Fig 1.2 (iv) is one-one and onto.
Example 7 Let A be the set of all 50 students of Class X in a school. Let $f: \mathrm{A} \rightarrow \mathbf{N}$ be function defined by $f(x)=$ roll number of the student $x$. Show that $f$ is one-one but not onto.

Solution No two different students of the class can have same roll number. Therefore, $f$ must be one-one. We can assume without any loss of generality that roll numbers of students are from 1 to 50 . This implies that 51 in $\mathbf{N}$ is not roll number of any student of the class, so that 51 can not be image of any element of X under $f$. Hence, $f$ is not onto.

Example 8 Show that the function $f: \mathbf{N} \rightarrow \mathbf{N}$, given by $f(x)=2 x$, is one-one but not onto.

Solution The function $f$ is one-one, for $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow 2 x_{1}=2 x_{2} \Rightarrow x_{1}=x_{2}$. Further, $f$ is not onto, as for $1 \in \mathbf{N}$, there does not exist any $x$ in $\mathbf{N}$ such that $f(x)=2 x=1$.

Example 9 Prove that the function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by $f(x)=2 x$, is one-one and onto. Solution $f$ is one-one, as $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow 2 x_{1}=2 x_{2} \Rightarrow x_{1}=x_{2}$. Also, given any real number $y$ in R , there exists $\frac{y}{2}$ in R such that $f\left(\frac{y}{2}\right)=2 \cdot\left(\frac{y}{2}\right)=y$. Hence, $f$ is onto.
![](https://cdn.mathpix.com/cropped/2025_07_21_e122063659afbdd12741g-09.jpg?height=537&width=588&top_left_y=608&top_left_x=518)

Fig 1.3
Example 10 Show that the function $f: \mathbf{N} \rightarrow \mathbf{N}$, given by $f(1)=f(2)=1$ and $f(x)=x-1$, for every $x>2$, is onto but not one-one.

Solution $f$ is not one-one, as $f(1)=f(2)=1$. But $f$ is onto, as given any $y \in \mathbf{N}, y \neq 1$, we can choose $x$ as $y+1$ such that $f(y+1)=y+1-1=y$. Also for $1 \in \mathbf{N}$, we have $f(1)=1$.

Example 11 Show that the function $f: \mathbf{R} \rightarrow \mathbf{R}$, defined as $f(x)=x^{2}$, is neither one-one nor onto.

Solution Since $f(-1)=1=f(1), f$ is not oneone. Also, the element - 2 in the co-domain $\mathbf{R}$ is not image of any element $x$ in the domain $\mathbf{R}$ (Why?). Therefore $f$ is not onto.

Example 12 Show that $f: \mathbf{N} \rightarrow \mathbf{N}$, given by

$$
f(x)=\begin{aligned}
& x+1, \text { if } x \text { is odd } \\
& x-1, \text { if } x \text { is even }
\end{aligned}
$$

is both one-one and onto.
![](https://cdn.mathpix.com/cropped/2025_07_21_e122063659afbdd12741g-09.jpg?height=525&width=564&top_left_y=1542&top_left_x=910)

Fig 1.4

Solution Suppose $f\left(x_{1}\right)=f\left(x_{2}\right)$. Note that if $x_{1}$ is odd and $x_{2}$ is even, then we will have $x_{1}+1=x_{2}-1$, i.e., $x_{2}-x_{1}=2$ which is impossible. Similarly, the possibility of $x_{1}$ being even and $x_{2}$ being odd can also be ruled out, using the similar argument. Therefore, both $x_{1}$ and $x_{2}$ must be either odd or even. Suppose both $x_{1}$ and $x_{2}$ are odd. Then $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}+1=x_{2}+1 \Rightarrow x_{1}=x_{2}$. Similarly, if both $x_{1}$ and $x_{2}$ are even, then also $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}-1=x_{2}-1 \Rightarrow x_{1}=x_{2}$. Thus, $f$ is one-one. Also, any odd number $2 r+1$ in the co-domain $\mathbf{N}$ is the image of $2 r+2$ in the domain $\mathbf{N}$ and any even number $2 r$ in the co-domain $\mathbf{N}$ is the image of $2 r-1$ in the domain $\mathbf{N}$. Thus, $f$ is onto.

Example 13 Show that an onto function $f:\{1,2,3\} \rightarrow\{1,2,3\}$ is always one-one.
Solution Suppose $f$ is not one-one. Then there exists two elements, say 1 and 2 in the domain whose image in the co-domain is same. Also, the image of 3 under $f$ can be only one element. Therefore, the range set can have at the most two elements of the co-domain $\{1,2,3\}$, showing that $f$ is not onto, a contradiction. Hence, $f$ must be one-one.
Example 14 Show that a one-one function $f:\{1,2,3\} \rightarrow\{1,2,3\}$ must be onto.
Solution Since $f$ is one-one, three elements of $\{1,2,3\}$ must be taken to 3 different elements of the co-domain $\{1,2,3\}$ under $f$. Hence, $f$ has to be onto.

Remark The results mentioned in Examples 13 and 14 are also true for an arbitrary finite set X , i.e., a one-one function $f: \mathrm{X} \rightarrow \mathrm{X}$ is necessarily onto and an onto map $f: \mathrm{X} \rightarrow \mathrm{X}$ is necessarily one-one, for every finite set X . In contrast to this, Examples 8 and 10 show that for an infinite set, this may not be true. In fact, this is a characteristic difference between a finite and an infinite set.

## EXERCISE 1.2

1. Show that the function $f: \mathbf{R}_{*} \rightarrow \mathbf{R}_{*}$ defined by $f(x)=\frac{1}{x}$ is one-one and onto, where $\mathbf{R}_{*}$ is the set of all non-zero real numbers. Is the result true, if the domain $\mathbf{R}_{*}$ is replaced by $\mathbf{N}$ with co-domain being same as $\mathbf{R}_{*}$ ?
2. Check the injectivity and surjectivity of the following functions:
(i) $f: \mathbf{N} \rightarrow \mathbf{N}$ given by $f(x)=x^{2}$
(ii) $f: \mathbf{Z} \rightarrow \mathbf{Z}$ given by $f(x)=x^{2}$
(iii) $f: \mathbf{R} \rightarrow \mathbf{R}$ given by $f(x)=x^{2}$
(iv) $f: \mathbf{N} \rightarrow \mathbf{N}$ given by $f(x)=x^{3}$
(v) $f: \mathbf{Z} \rightarrow \mathbf{Z}$ given by $f(x)=x^{3}$
3. Prove that the Greatest Integer Function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by $f(x)=[x]$, is neither one-one nor onto, where $[x]$ denotes the greatest integer less than or equal to $x$.
4. Show that the Modulus Function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by $f(x)=|x|$, is neither oneone nor onto, where $|x|$ is $x$, if $x$ is positive or 0 and $|x|$ is $-x$, if $x$ is negative.
5. Show that the Signum Function $f: \mathbf{R} \rightarrow \mathbf{R}$, given by

$$
f(x)=\begin{array}{r}
1, \text { if } x>0 \\
0, \text { if } x=0 \\
1, \text { if } x<0
\end{array}
$$

is neither one-one nor onto.
6. Let $\mathrm{A}=\{1,2,3\}, \mathrm{B}=\{4,5,6,7\}$ and let $f=\{(1,4),(2,5),(3,6)\}$ be a function from A to B . Show that $f$ is one-one.
7. In each of the following cases, state whether the function is one-one, onto or bijective. Justify your answer.
(i) $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=3-4 x$
(ii) $f: \mathbf{R} \rightarrow \mathbf{R}$ defined by $f(x)=1+x^{2}$
8. Let A and B be sets. Show that $f: \mathrm{A} \times \mathrm{B} \rightarrow \mathrm{B} \times \mathrm{A}$ such that $f(a, b)=(b, a)$ is bijective function.
9. Let $f: \mathbf{N} \rightarrow \mathbf{N}$ be defined by $f(n)=\frac{\frac{n+1}{2}}{\frac{n}{2}}$, if $n$ is odd for all $n \in \mathbf{N}$.

State whether the function $f$ is bijective. Justify your answer.
10. Let $\mathrm{A}=\mathbf{R}-\{3\}$ and $\mathrm{B}=\mathbf{R}-\{1\}$. Consider the function $f: \mathrm{A} \rightarrow \mathrm{B}$ defined by $f(x)=\left(\frac{x-2}{x-3}\right)$. Is $f$ one-one and onto? Justify your answer.
11. Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be defined as $f(x)=x^{4}$. Choose the correct answer.
(A) $f$ is one-one onto
(B) $f$ is many-one onto
(C) $f$ is one-one but not onto
(D) $f$ is neither one-one nor onto.
12. Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be defined as $f(x)=3 x$. Choose the correct answer.
(A) $f$ is one-one onto
(B) $f$ is many-one onto
(C) $f$ is one-one but not onto
(D) $f$ is neither one-one nor onto.

### 1.4 Composition of Functions and Invertible Function

Definition 8 Let $f: \mathrm{A} \rightarrow \mathrm{B}$ and $g: \mathrm{B} \rightarrow \mathrm{C}$ be two functions. Then the composition of $f$ and $g$, denoted by $g \circ f$, is defined as the function $g \circ f: \mathrm{A} \rightarrow \mathrm{C}$ given by

$$
g o f(x)=g(f(x)), \forall x \in \mathrm{~A} .
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_e122063659afbdd12741g-12.jpg?height=300&width=1279&top_left_y=578&top_left_x=177)

Fig 1.5
Example 15 Let $f:\{2,3,4,5\} \rightarrow\{3,4,5,9\}$ and $g:\{3,4,5,9\} \rightarrow\{7,11,15\}$ be functions defined as $f(2)=3, f(3)=4, f(4)=f(5)=5$ and $g(3)=g(4)=7$ and $g(5)=g(9)=11$. Find $g o f$.
Solution We have $g o f(2)=g(f(2))=g(3)=7, g o f(3)=g(f(3))=g(4)=7$, $g o f(4)=g(f(4))=g(5)=11$ and $g o f(5)=g(5)=11$.

Example 16 Find $g \circ f$ and $f \circ g$, if $f: \mathbf{R} \rightarrow \mathbf{R}$ and $g: \mathbf{R} \rightarrow \mathbf{R}$ are given by $f(x)=\cos x$ and $g(x)=3 x^{2}$. Show that $g o f \neq f o g$.

Solution We have $g o f(x)=g(f(x))=g(\cos x)=3(\cos x)^{2}=3 \cos ^{2} x$. Similarly, $f o g(x)=f(g(x))=f\left(3 x^{2}\right)=\cos \left(3 x^{2}\right)$. Note that $3 \cos ^{2} x \neq \cos 3 x^{2}$, for $x=0$. Hence, $g o f \neq f o g$.
Definition 9 A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is defined to be invertible, if there exists a function $g: \mathrm{Y} \rightarrow \mathrm{X}$ such that $g \circ f=\mathrm{I}_{\mathrm{X}}$ and fog $=\mathrm{I}_{\mathrm{Y}}$. The function $g$ is called the inverse off and is denoted by $f^{-1}$.

Thus, if $f$ is invertible, then $f$ must be one-one and onto and conversely, if $f$ is one-one and onto, then $f$ must be invertible. This fact significantly helps for proving a function $f$ to be invertible by showing that $f$ is one-one and onto, specially when the actual inverse of $f$ is not to be determined.

Example 17 Let $f: \mathbf{N} \rightarrow \mathrm{Y}$ be a function defined as $f(x)=4 x+3$, where, $\mathrm{Y}=\{y \in \mathbf{N}: y=4 x+3$ for some $x \in \mathbf{N}\}$. Show that $f$ is invertible. Find the inverse.
Solution Consider an arbitrary element $y$ of Y . By the definition of $\mathrm{Y}, y=4 x+3$, for some $x$ in the domain $\mathbf{N}$. This shows that $x=\frac{(y-3)}{4}$. Define $g: \mathrm{Y} \rightarrow \mathbf{N}$ by
$g(y)=\frac{(y-3)}{4}$. Now, $g \circ f(x)=g(f(x))=g(4 x+3)=\frac{(4 x+3-3)}{4}=x$ and
$f \circ g(y)=f(g(y))=f\left(\frac{(y-3)}{4}\right)=\frac{4(y-3)}{4}+3=y-3+3=y$. This shows that $g \circ f=\mathrm{I}_{\mathrm{N}}$
and $f o g=\mathrm{I}_{\mathrm{Y}}$, which implies that $f$ is invertible and $g$ is the inverse of $f$.

## Miscellaneous Examples

Example 18 If $R_{1}$ and $R_{2}$ are equivalence relations in a set $A$, show that $R_{1} \cap R_{2}$ is also an equivalence relation.

Solution Since $\mathrm{R}_{1}$ and $\mathrm{R}_{2}$ are equivalence relations, $(a, a) \in \mathrm{R}_{1}$, and $(a, a) \in \mathrm{R}_{2} \forall a \in \mathrm{~A}$. This implies that $(a, a) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}, \forall a$, showing $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is reflexive. Further, $(a, b) \in \mathrm{R}_{1} \cap \mathrm{R}_{2} \Rightarrow(a, b) \in \mathrm{R}_{1}$ and $(a, b) \in \mathrm{R}_{2} \Rightarrow(b, a) \in \mathrm{R}_{1}$ and $(b, a) \in \mathrm{R}_{2} \Rightarrow$ $(b, a) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$, hence, $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is symmetric. Similarly, $(a, b) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$ and $(b, c) \in \mathrm{R}_{1} \cap \mathrm{R}_{2} \Rightarrow(a, c) \in \mathrm{R}_{1}$ and $(a, c) \in \mathrm{R}_{2} \Rightarrow(a, c) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$. This shows that $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is transitive. Thus, $\mathrm{R}_{1} \cap \mathrm{R}_{2}$ is an equivalence relation.
Example 19 Let R be a relation on the set A of ordered pairs of positive integers defined by $(x, y) \mathrm{R}(u, v)$ if and only if $x v=y u$. Show that R is an equivalence relation.

Solution Clearly, $(x, y) \mathrm{R}(x, y), \forall(x, y) \in \mathrm{A}$, since $x y=y x$. This shows that R is reflexive. Further, $(x, y) \mathrm{R}(u, v) \Rightarrow x v=y u \Rightarrow u y=v x$ and hence $(u, v) \mathrm{R}(x, y)$. This shows that R is symmetric. Similarly, $(x, y) \mathrm{R}(u, v)$ and $(u, v) \mathrm{R}(a, b) \Rightarrow x v=y u$ and $u b=v a \Rightarrow x v \frac{a}{u}=y u \frac{a}{u} \Rightarrow x v \frac{b}{v}=y u \frac{a}{u} \Rightarrow x b=y a$ and hence $(x, y) \mathrm{R}(a, b)$. Thus, R is transitive. Thus, R is an equivalence relation.

Example 20 Let $\mathrm{X}=\{1,2,3,4,5,6,7,8,9\}$. Let $\mathrm{R}_{1}$ be a relation in X given by $\mathrm{R}_{1}=\{(x, y): x-y$ is divisible by 3$\}$ and $\mathrm{R}_{2}$ be another relation on X given by $\mathrm{R}_{2}=\{(x, y):\{x, y\} \subset\{1,4,7\}\}$ or $\{x, y\} \subset\{2,5,8\}$ or $\left.\{x, y\} \subset\{3,6,9\}\right\}$. Show that $\mathrm{R}_{1}=\mathrm{R}_{2}$.

Solution Note that the characteristic of sets $\{1,4,7\},\{2,5,8\}$ and $\{3,6,9\}$ is that difference between any two elements of these sets is a multiple of 3 . Therefore, $(x, y) \in \mathrm{R}_{1} \Rightarrow x-y$ is a multiple of $3 \Rightarrow\{x, y\} \subset\{1,4,7\}$ or $\{x, y\} \subset\{2,5,8\}$ or $\{x, y\} \subset\{3,6,9\} \Rightarrow(x, y) \in \mathrm{R}_{2}$. Hence, $\mathrm{R}_{1} \subset \mathrm{R}_{2}$. Similarly, $\{x, y\} \in \mathrm{R}_{2} \Rightarrow\{x, y\}$
$\subset\{1,4,7\}$ or $\{x, y\} \subset\{2,5,8\}$ or $\{x, y\} \subset\{3,6,9\} \Rightarrow x-y$ is divisible by $3 \Rightarrow\{x, y\} \in \mathrm{R}_{1}$. This shows that $\mathrm{R}_{2} \subset \mathrm{R}_{1}$. Hence, $\mathrm{R}_{1}=\mathrm{R}_{2}$.
Example 21 Let $f: \mathrm{X} \rightarrow \mathrm{Y}$ be a function. Define a relation R in X given by $\mathrm{R}=\{(a, b): f(a)=f(b)\}$. Examine whether R is an equivalence relation or not.

Solution For every $a \in \mathrm{X},(a, a) \in \mathrm{R}$, since $f(a)=f(a)$, showing that R is reflexive. Similarly, $(a, b) \in \mathrm{R} \Rightarrow f(a)=f(b) \Rightarrow f(b)=f(a) \Rightarrow(b, a) \in \mathrm{R}$. Therefore, R is symmetric. Further, $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R} \Rightarrow f(a)=f(b)$ and $f(b)=f(c) \Rightarrow f(a)$ $=f(c) \Rightarrow(a, c) \in \mathrm{R}$, which implies that R is transitive. Hence, R is an equivalence relation.

Example 22 Find the number of all one-one functions from set $\mathrm{A}=\{1,2,3\}$ to itself.
Solution One-one function from $\{1,2,3\}$ to itself is simply a permutation on three symbols $1,2,3$. Therefore, total number of one-one maps from $\{1,2,3\}$ to itself is same as total number of permutations on three symbols $1,2,3$ which is $3!=6$.
Example 23 Let $\mathrm{A}=\{1,2,3\}$. Then show that the number of relations containing $(1,2)$ and $(2,3)$ which are reflexive and transitive but not symmetric is three.

Solution The smallest relation $\mathrm{R}_{1}$ containing $(1,2)$ and $(2,3)$ which is reflexive and transitive but not symmetric is $\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)\}$. Now, if we add the pair ( 2,1 ) to $R_{1}$ to get $R_{2}$, then the relation $R_{2}$ will be reflexive, transitive but not symmetric. Similarly, we can obtain $R_{3}$ by adding $(3,2)$ to $R_{1}$ to get the desired relation. However, we can not add two pairs $(2,1),(3,2)$ or single pair $(3,1)$ to $R_{1}$ at a time, as by doing so, we will be forced to add the remaining pair in order to maintain transitivity and in the process, the relation will become symmetric also which is not required. Thus, the total number of desired relations is three.

Example 24 Show that the number of equivalence relation in the set $\{1,2,3\}$ containing $(1,2)$ and $(2,1)$ is two.

Solution The smallest equivalence relation $R_{1}$ containing ( 1,2 ) and ( 2,1 ) is $\{(1,1)$, $(2,2),(3,3),(1,2),(2,1)\}$. Now we are left with only 4 pairs namely $(2,3),(3,2)$, $(1,3)$ and $(3,1)$. If we add any one, say $(2,3)$ to $R_{1}$, then for symmetry we must add $(3,2)$ also and now for transitivity we are forced to add $(1,3)$ and $(3,1)$. Thus, the only equivalence relation bigger than $R_{1}$ is the universal relation. This shows that the total number of equivalence relations containing $(1,2)$ and $(2,1)$ is two.
Example 25 Consider the identity function $\mathrm{I}_{\mathbf{N}}: \mathbf{N} \rightarrow \mathbf{N}$ defined as $\mathrm{I}_{\mathbf{N}}(x)=x \forall x \in \mathbf{N}$. Show that although $\mathrm{I}_{\mathrm{N}}$ is onto but $\mathrm{I}_{\mathbf{N}}+\mathrm{I}_{\mathbf{N}}: \mathbf{N} \rightarrow \mathbf{N}$ defined as

$$
\left(\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}\right)(x)=\mathrm{I}_{\mathrm{N}}(x)+\mathrm{I}_{\mathrm{N}}(x)=x+x=2 x \text { is not onto. }
$$

Solution Clearly $\mathrm{I}_{\mathrm{N}}$ is onto. But $\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}$ is not onto, as we can find an element 3 in the co-domain $\mathbf{N}$ such that there does not exist any $x$ in the domain $\mathbf{N}$ with $\left(\mathrm{I}_{\mathrm{N}}+\mathrm{I}_{\mathrm{N}}\right)(x)=2 x=3$.
Example 26 Consider a function $f:\left[0, \frac{\pi}{2}\right] \rightarrow \mathbf{R}$ given by $f(x)=\sin x$ and $g:\left[0, \frac{\pi}{2}\right] \rightarrow \mathbf{R}$ given by $g(x)=\cos x$. Show that $f$ and $g$ are one-one, but $f+g$ is not one-one.

Solution Since for any two distinct elements $x_{1}$ and $x_{2}$ in $\left[0, \frac{\pi}{2}\right], \sin x_{1} \neq \sin x_{2}$ and $\cos x_{1} \neq \cos x_{2}$, both $f$ and $g$ must be one-one. But $(f+g)(0)=\sin 0+\cos 0=1$ and $(f+g)\left(\frac{\pi}{2}\right)=\sin \frac{\pi}{2}+\cos \frac{\pi}{2}=1$. Therefore, $f+g$ is not one-one.

## Miscellaneous Exercise on Chapter 1

1. Show that the function $f: \mathbf{R} \rightarrow\{x \in \mathbf{R}:-1<x<1\}$ defined by $f(x)=\frac{x}{1+|x|}$, $x \in \mathbf{R}$ is one one and onto function.
2. Show that the function $f: \mathbf{R} \rightarrow \mathbf{R}$ given by $f(x)=x^{3}$ is injective.
3. Given a non empty set X , consider $\mathrm{P}(\mathrm{X})$ which is the set of all subsets of X . Define the relation $R$ in $P(X)$ as follows:
For subsets $\mathrm{A}, \mathrm{B}$ in $\mathrm{P}(\mathrm{X}), \mathrm{ARB}$ if and only if $\mathrm{A} \subset \mathrm{B}$. Is R an equivalence relation on $\mathrm{P}(\mathrm{X})$ ? Justify your answer.
4. Find the number of all onto functions from the set $\{1,2,3, \ldots \ldots, n\}$ to itself.
5. Let $\mathrm{A}=\{-1,0,1,2\}, \mathrm{B}=\{-4,-2,0,2\}$ and $f, g: \mathrm{A} \rightarrow \mathrm{B}$ be functions defined by $f(x)=x^{2}-x, x \in \mathrm{~A}$ and $g(x)=2\left|x-\frac{1}{2}\right|-1, x \in \mathrm{~A}$. Are $f$ and $g$ equal? Justify your answer. (Hint: One may note that two functions $f: \mathrm{A} \rightarrow \mathrm{B}$ and $g: \mathrm{A} \rightarrow \mathrm{B}$ such that $f(a)=g(a) \forall a \in \mathrm{~A}$, are called equal functions).
6. Let $\mathrm{A}=\{1,2,3\}$. Then number of relations containing ( 1,2 ) and ( 1,3 ) which are reflexive and symmetric but not transitive is
(A) 1
(B) 2
(C) 3
(D) 4
7. Let $\mathrm{A}=\{1,2,3\}$. Then number of equivalence relations containing ( 1,2 ) is
(A) 1
(B) 2
(C) 3
(D) 4

## Summary

In this chapter, we studied different types of relations and equivalence relation, composition of functions, invertible functions and binary operations. The main features of this chapter are as follows:

- Empty relation is the relation R in X given by $\mathrm{R}=\phi \subset \mathrm{X} \times \mathrm{X}$.
- Universal relation is the relation R in X given by $\mathrm{R}=\mathrm{X} \times \mathrm{X}$.
- Reflexive relation R in X is a relation with $(a, a) \in \mathrm{R} \forall a \in \mathrm{X}$.
- Symmetric relation R in X is a relation satisfying $(a, b) \in \mathrm{R}$ implies $(b, a) \in \mathrm{R}$.
- Transitive relation R in X is a relation satisfying $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R}$ implies that $(a, c) \in \mathrm{R}$.
- Equivalence relation R in X is a relation which is reflexive, symmetric and transitive.
- Equivalence class [ $a$ ] containing $a \in \mathrm{X}$ for an equivalence relation R in X is the subset of X containing all elements $b$ related to $a$.
- A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is one-one (or injective) if $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}=x_{2} \forall x_{1}, x_{2} \in \mathrm{X}$.
- A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is onto (or surjective) if given any $y \in \mathrm{Y}, \exists x \in \mathrm{X}$ such that $f(x)=y$.
- A function $f: \mathrm{X} \rightarrow \mathrm{Y}$ is one-one and onto (or bijective), if $f$ is both one-one and onto.
- Given a finite set X , a function $f: \mathrm{X} \rightarrow \mathrm{X}$ is one-one (respectively onto) if and only if $f$ is onto (respectively one-one). This is the characteristic property of a finite set. This is not true for infinite set


## Historical Note

The concept of function has evolved over a long period of time starting from R. Descartes (1596-1650), who used the word 'function' in his manuscript "Geometrie" in 1637 to mean some positive integral power $x^{n}$ of a variable $x$ while studying geometrical curves like hyperbola, parabola and ellipse. James Gregory (1636-1675) in his work "Vera Circuli et Hyperbolae Quadratura" (1667) considered function as a quantity obtained from other quantities by successive use of algebraic operations or by any other operations. Later G. W. Leibnitz (1646-1716) in his manuscript "Methodus tangentium inversa, seu de functionibus" written in 1673 used the word 'function' to mean a quantity varying from point to point on a curve such as the coordinates of a point on the curve, the slope of the curve, the tangent and the normal to the curve at a point. However, in his manuscript "Historia" (1714), Leibnitz used the word 'function' to mean quantities that depend on a variable. He was the first to use the phrase 'function of $x$ '. John Bernoulli (1667-1748) used the notation $\phi x$ for the first time in 1718 to indicate a function of $x$. But the general adoption of symbols like $f, \mathrm{~F}, \phi, \psi \ldots$ to represent functions was made by Leonhard Euler (1707-1783) in 1734 in the first part of his manuscript "Analysis Infinitorium". Later on, Joeph Louis Lagrange (1736-1813) published his manuscripts "Theorie des functions analytiques" in 1793, where he discussed about analytic function and used the notion $f(x), \mathrm{F}(x)$, $\phi(x)$ etc. for different function of $x$. Subsequently, Lejeunne Dirichlet (1805-1859) gave the definition of function which was being used till the set theoretic definition of function presently used, was given after set theory was developed by Georg Cantor (1845-1918). The set theoretic definition of function known to us presently is simply an abstraction of the definition given by Dirichlet in a rigorous manner.

