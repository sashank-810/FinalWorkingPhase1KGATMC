## PROBABILITY

## The theory of probabilities is simply the Science of logic quantitatively treated. - C.S. PEIRCE

### 13.1 Introduction

In earlier Classes, we have studied the probability as a measure of uncertainty of events in a random experiment. We discussed the axiomatic approach formulated by Russian Mathematician, A.N. Kolmogorov (1903-1987) and treated probability as a function of outcomes of the experiment. We have also established equivalence between the axiomatic theory and the classical theory of probability in case of equally likely outcomes. On the basis of this relationship, we obtained probabilities of events associated with discrete sample spaces. We have also studied the addition rule of probability. In this chapter, we shall discuss the important concept of conditional probability of an event given that another event has occurred, which will be helpful in understanding the Bayes' theorem, multiplication rule of probability and independence of events. We shall also learn
![](https://cdn.mathpix.com/cropped/2025_07_21_66018d76ad34726525c6g-01.jpg?height=546&width=416&top_left_y=815&top_left_x=992)

Pierre de Fermat (1601-1665) an important concept of random variable and its probability distribution and also the mean and variance of a probability distribution. In the last section of the chapter, we shall study an important discrete probability distribution called Binomial distribution. Throughout this chapter, we shall take up the experiments having equally likely outcomes, unless stated otherwise.

### 13.2 Conditional Probability

Uptill now in probability, we have discussed the methods of finding the probability of events. If we have two events from the same sample space, does the information about the occurrence of one of the events affect the probability of the other event? Let us try to answer this question by taking up a random experiment in which the outcomes are equally likely to occur.

Consider the experiment of tossing three fair coins. The sample space of the experiment is
S = \{ННН, ННТ, НТН, ТНН, НТТ, ТНТ, ТТН, ТТТ

Since the coins are fair, we can assign the probability $\frac{1}{8}$ to each sample point. Let E be the event 'at least two heads appear' and F be the event 'first coin shows tail'. Then

$$
\mathrm{E}=\{\mathrm{HHH}, \mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}\}
$$

and $\quad \mathrm{F}=\{\mathrm{THH}$, THT, TTH, TTT $\}$
Therefore $\quad \mathrm{P}(\mathrm{E})=\mathrm{P}(\{\mathrm{HHH}\})+\mathrm{P}(\{\mathrm{HHT}\})+\mathrm{P}(\{\mathrm{HTH}\})+\mathrm{P}(\{\mathrm{THH}\})$
and

$$
=\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8}=\frac{1}{2} \text { (Why ?) }
$$

$$
\mathrm{P}(\mathrm{~F})=\mathrm{P}(\{\mathrm{THH}\})+\mathrm{P}(\{\mathrm{THT}\})+\mathrm{P}(\{\mathrm{TTH}\})+\mathrm{P}(\{\mathrm{TTT}\})
$$

$$
=\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8}=\frac{1}{2}
$$

Also

$$
E \cap F=\{T H H\}
$$

with

$$
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\{\mathrm{THH}\})=\frac{1}{8}
$$

Now, suppose we are given that the first coin shows tail, i.e. F occurs, then what is the probability of occurrence of E ? With the information of occurrence of F , we are sure that the cases in which first coin does not result into a tail should not be considered while finding the probability of E . This information reduces our sample space from the set S to its subset F for the event E . In other words, the additional information really amounts to telling us that the situation may be considered as being that of a new random experiment for which the sample space consists of all those outcomes only which are favourable to the occurrence of the event F .
Now, the sample point of F which is favourable to event E is THH.
Thus, Probability of E considering F as the sample space $=\frac{1}{4}$,
or

$$
\text { Probability of } \mathrm{E} \text { given that the event } \mathrm{F} \text { has occurred }=\frac{1}{4}
$$

This probability of the event E is called the conditional probability of $E$ given that $F$ has already occurred, and is denoted by $\mathrm{P}(\mathrm{EIF})$.

Thus

$$
\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{1}{4}
$$

Note that the elements of F which favour the event E are the common elements of E and F , i.e. the sample points of $\mathrm{E} \cap \mathrm{F}$.

Thus, we can also write the conditional probability of E given that F has occurred as

$$
\begin{aligned}
\mathrm{P}(\mathrm{EIF}) & =\frac{\text { Number of elementary events favourable to } \mathrm{E} \cap \mathrm{~F}}{\text { Number of elementary events which are favourable to } \mathrm{F}} \\
& =\frac{n(\mathrm{E} \cap \mathrm{~F})}{n(\mathrm{~F})}
\end{aligned}
$$

Dividing the numerator and the denominator by total number of elementary events of the sample space, we see that $\mathrm{P}(\mathrm{E} \mid \mathrm{F})$ can also be written as

$$
\begin{equation*}
\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{\frac{n(\mathrm{E} \cap \mathrm{~F})}{n(\mathrm{~S})}}{\frac{n(\mathrm{~F})}{n(\mathrm{~S})}}=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})} \tag{1}
\end{equation*}
$$

Note that (1) is valid only when $\mathrm{P}(\mathrm{F}) \neq 0$ i.e., $\mathrm{F} \neq \phi$ (Why?)
Thus, we can define the conditional probability as follows :
Definition 1 If $E$ and $F$ are two events associated with the same sample space of a random experiment, the conditional probability of the event E given that F has occurred, i.e. $\mathrm{P}(\mathrm{EIF})$ is given by

$$
\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})} \text { provided } \mathrm{P}(\mathrm{~F}) \neq 0
$$

### 13.2.1 Properties of conditional probability

Let E and F be events of a sample space S of an experiment, then we have Property $1 \mathrm{P}(\mathrm{S} \mid \mathrm{F})=\mathrm{P}(\mathrm{F} \mid \mathrm{F})=1$
We know that

$$
\mathrm{P}(\mathrm{~S} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{~S} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}=\frac{\mathrm{P}(\mathrm{~F})}{\mathrm{P}(\mathrm{~F})}=1
$$

Also

$$
\mathrm{P}(\mathrm{~F} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{~F} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}=\frac{\mathrm{P}(\mathrm{~F})}{\mathrm{P}(\mathrm{~F})}=1
$$

Thus

$$
\mathrm{P}(\mathrm{~S} \mid \mathrm{F})=\mathrm{P}(\mathrm{~F} \mid \mathrm{F})=1
$$

Property 2 If A and B are any two events of a sample space S and F is an event of S such that $\mathrm{P}(\mathrm{F}) \neq 0$, then

$$
\mathrm{P}((\mathrm{~A} \cup \mathrm{~B}) \mid \mathrm{F})=\mathrm{P}(\mathrm{~A} \mid \mathrm{F})+\mathrm{P}(\mathrm{~B} \mid \mathrm{F})-\mathrm{P}((\mathrm{~A} \cap \mathrm{~B}) \mid \mathrm{F})
$$

In particular, if A and B are disjoint events, then

$$
\mathrm{P}((\mathrm{~A} \cup \mathrm{~B}) \mid \mathrm{F})=\mathrm{P}(\mathrm{~A} \mid \mathrm{F})+\mathrm{P}(\mathrm{~B} \mid \mathrm{F})
$$

We have

$$
\begin{aligned}
\mathrm{P}((\mathrm{~A} \cup \mathrm{~B}) \mid \mathrm{F}) & =\frac{\mathrm{P}[(\mathrm{~A} \cup \mathrm{~B}) \cap \mathrm{F}]}{\mathrm{P}(\mathrm{~F})} \\
& =\frac{\mathrm{P}[(\mathrm{~A} \cap \mathrm{~F}) \cup(\mathrm{B} \cap \mathrm{~F})]}{\mathrm{P}(\mathrm{~F})}
\end{aligned}
$$

(by distributive law of union of sets over intersection)

$$
\begin{aligned}
& =\frac{\mathrm{P}(\mathrm{~A} \cap \mathrm{~F})+\mathrm{P}(\mathrm{~B} \cap \mathrm{~F})-\mathrm{P}(\mathrm{~A} \cap \mathrm{~B} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})} \\
& =\frac{\mathrm{P}(\mathrm{~A} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}+\frac{\mathrm{P}(\mathrm{~B} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}-\frac{\mathrm{P}[(\mathrm{~A} \cap \mathrm{~B}) \cap \mathrm{F}]}{\mathrm{P}(\mathrm{~F})} \\
& =\mathrm{P}(\mathrm{AlF})+\mathrm{P}(\mathrm{BlF})-\mathrm{P}((\mathrm{~A} \cap \mathrm{~B}) \mid \mathrm{F})
\end{aligned}
$$

When A and B are disjoint events, then

$$
\begin{array}{ll} 
& \mathrm{P}((\mathrm{~A} \cap \mathrm{~B}) \mid \mathrm{F})=0 \\
\Rightarrow & \mathrm{P}((\mathrm{~A} \cup \mathrm{~B}) \mid \mathrm{F})=\mathrm{P}(\mathrm{~A} \mid \mathrm{F})+\mathrm{P}(\mathrm{~B} \mid \mathrm{F})
\end{array}
$$

Property $3 \mathrm{P}\left(\mathrm{E}^{\prime} \mid \mathrm{F}\right)=1-\mathrm{P}(\mathrm{E} \mid \mathrm{F})$
From Property 1, we know that $\mathrm{P}(\mathrm{SIF})=1$
$\Rightarrow \quad \mathrm{P}\left(\mathrm{E} \cup \mathrm{E}^{\prime} \mid \mathrm{F}\right)=1 \quad$ since $\mathrm{S}=\mathrm{E} \cup \mathrm{E}^{\prime}$
$\Rightarrow \quad \mathrm{P}(\mathrm{E} \mid \mathrm{F})+\mathrm{P}\left(\mathrm{E}^{\prime} \mid \mathrm{F}\right)=1 \quad$ since E and $\mathrm{E}^{\prime}$ are disjoint events
Thus,

$$
\mathrm{P}\left(\mathrm{E}^{\prime} \mid \mathrm{F}\right)=1-\mathrm{P}(\mathrm{E} \mid \mathrm{F})
$$

Let us now take up some examples.
Example 1 If $\mathrm{P}(\mathrm{A})=\frac{7}{13}, \mathrm{P}(\mathrm{B})=\frac{9}{13}$ and $\mathrm{P}(\mathrm{A} \cap \mathrm{B})=\frac{4}{13}$, evaluate $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$.

Solution We have $\mathrm{P}(\mathrm{A} \mid \mathrm{B})=\frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{B})}=\frac{\frac{4}{13}}{\frac{9}{13}}=\frac{4}{9}$
Example 2 A family has two children. What is the probability that both the children are boys given that at least one of them is a boy ?

Solution Let $b$ stand for boy and $g$ for girl. The sample space of the experiment is

$$
\mathrm{S}=\{(b, b),(g, b),(b, g),(g, g)\}
$$

Let E and F denote the following events:
E: 'both the children are boys'
F: 'at least one of the child is a boy'
Then

$$
\mathrm{E}=\{(b, b)\} \text { and } \mathrm{F}=\{(b, b),(g, b),(b, g)\}
$$

Now

$$
\mathrm{E} \cap \mathrm{~F}=\{(b, b)\}
$$

Thus

$$
\mathrm{P}(\mathrm{~F})=\frac{3}{4} \text { and } \mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\frac{1}{4}
$$

Therefore

$$
\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}=\frac{\frac{1}{4}}{\frac{3}{4}}=\frac{1}{3}
$$

Example 3 Ten cards numbered 1 to 10 are placed in a box, mixed up thoroughly and then one card is drawn randomly. If it is known that the number on the drawn card is more than 3 , what is the probability that it is an even number?

Solution Let A be the event 'the number on the card drawn is even' and B be the event 'the number on the card drawn is greater than 3 '. We have to find $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$.
Now, the sample space of the experiment is $S=\{1,2,3,4,5,6,7,8,9,10\}$
Then

$$
\mathrm{A}=\{2,4,6,8,10\}, \mathrm{B}=\{4,5,6,7,8,9,10\}
$$

and

$$
A \cap B=\{4,6,8,10\}
$$

Also

$$
\mathrm{P}(\mathrm{~A})=\frac{5}{10}, \mathrm{P}(\mathrm{~B})=\frac{7}{10} \text { and } \mathrm{P}(\mathrm{~A} \cap \mathrm{~B})=\frac{4}{10}
$$

Then

$$
\mathrm{P}(\mathrm{~A} \mid \mathrm{B})=\frac{\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})}{\mathrm{P}(\mathrm{~B})}=\frac{\frac{4}{10}}{\frac{7}{10}}=\frac{4}{7}
$$

Example 4 In a school, there are 1000 students, out of which 430 are girls. It is known that out of 430, $10 \%$ of the girls study in class XII. What is the probability that a student chosen randomly studies in Class XII given that the chosen student is a girl?

Solution Let E denote the event that a student chosen randomly studies in Class XII and F be the event that the randomly chosen student is a girl. We have to find $\mathrm{P}(\mathrm{E} \mid \mathrm{F})$.

Now

$$
P(F)=\frac{430}{1000}=0.43 \text { and } P(E \cap F)=\frac{43}{1000}=0.043 \text { (Why?) }
$$

Then

$$
P(E \mid F)=\frac{P(E \cap F)}{P(F)}=\frac{0.043}{0.43}=0.1
$$

Example 5 A die is thrown three times. Events A and B are defined as below:
A : 4 on the third throw
B: 6 on the first and 5 on the second throw
Find the probability of A given that B has already occurred.
Solution The sample space has 216 outcomes.

Now

$$
\left.\begin{array}{rl}
A & =\left\{\begin{array}{lllll}
(1,1,4) & (1,2,4) & \ldots & (1,6,4) & (2,1,4) \\
(3,1,4) & (3,2,4) & \ldots & (3,6,4) & (4,1,4) \\
(5,1,4) & (5,2,4) & \ldots & (5,6,4) & (6,1,4) \\
(6,2,4) & \ldots(4,6,4)
\end{array}\right\} \\
B & =\{(6,5,1),(6,5,2),(6,5,3),(6,5,4),(6,5,5),(6,5,6)
\end{array}\right\}
$$

and

Now

$$
P(B)=\frac{6}{216} \text { and } P(A \cap B)=\frac{1}{216}
$$

Then

$$
\mathrm{P}(\mathrm{~A} \mid \mathrm{B})=\frac{\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})}{\mathrm{P}(\mathrm{~B})}=\frac{\frac{1}{216}}{\frac{6}{216}}=\frac{1}{6}
$$

Example 6 A die is thrown twice and the sum of the numbers appearing is observed to be 6 . What is the conditional probability that the number 4 has appeared at least once?

Solution Let E be the event that 'number 4 appears at least once' and F be the event that 'the sum of the numbers appearing is 6 '.
Then,

$$
E=\{(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(1,4),(2,4),(3,4),(5,4),(6,4)\}
$$

and

$$
F=\{(1,5),(2,4),(3,3),(4,2),(5,1)\}
$$

We have

$$
\mathrm{P}(\mathrm{E})=\frac{11}{36} \text { and } \mathrm{P}(\mathrm{~F})=\frac{5}{36}
$$

Also

$$
\mathrm{E} \cap \mathrm{~F}=\{(2,4),(4,2)\}
$$

Therefore

$$
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\frac{2}{36}
$$

Hence, the required probability

$$
\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}=\frac{\frac{2}{36}}{\frac{5}{36}}=\frac{2}{5}
$$

For the conditional probability discussed above, we have considered the elementtary events of the experiment to be equally likely and the corresponding definition of the probability of an event was used. However, the same definition can also be used in the general case where the elementary events of the sample space are not equally likely, the probabilities $\mathrm{P}(\mathrm{E} \cap \mathrm{F})$ and $\mathrm{P}(\mathrm{F})$ being calculated accordingly. Let us take up the following example.

Example 7 Consider the experiment of tossing a coin. If the coin shows head, toss it again but if it shows tail, then throw a die. Find the conditional probability of the event that 'the die shows a number greater than 4 ' given that 'there is at least one tail'.

Solution The outcomes of the experiment can be represented in following diagrammatic manner called the 'tree diagram'.

The sample space of the experiment may be described as
![](https://cdn.mathpix.com/cropped/2025_07_21_66018d76ad34726525c6g-07.jpg?height=416&width=482&top_left_y=1042&top_left_x=930)

Fig 13.1

$$
\mathrm{S}=\{(\mathrm{H}, \mathrm{H}),(\mathrm{H}, \mathrm{~T}),(\mathrm{T}, 1),(\mathrm{T}, 2),(\mathrm{T}, 3),(\mathrm{T}, 4),(\mathrm{T}, 5),(\mathrm{T}, 6)\}
$$

where $(\mathrm{H}, \mathrm{H})$ denotes that both the tosses result into head and ( $\mathrm{T}, i$ ) denote the first toss result into a tail and the number $i$ appeared on the die for $i=1,2,3,4,5,6$. Thus, the probabilities assigned to the 8 elementary events

$$
(\mathrm{H}, \mathrm{H}),(\mathrm{H}, \mathrm{~T}),(\mathrm{T}, 1),(\mathrm{T}, 2),(\mathrm{T}, 3)(\mathrm{T}, 4),(\mathrm{T}, 5),(\mathrm{T}, 6)
$$ are $\frac{1}{4}, \frac{1}{4}, \frac{1}{12}, \frac{1}{12}, \frac{1}{12}, \frac{1}{12}, \frac{1}{12}, \frac{1}{12}$ respectively which is clear from the Fig 13.2.

![](https://cdn.mathpix.com/cropped/2025_07_21_66018d76ad34726525c6g-07.jpg?height=489&width=482&top_left_y=1584&top_left_x=921)

Let F be the event that 'there is at least one tail' and E be the event 'the die shows a number greater than 4 '. Then

Now

$$
\begin{aligned}
\mathrm{F}= & \{(\mathrm{H}, \mathrm{~T}),(\mathrm{T}, 1),(\mathrm{T}, 2),(\mathrm{T}, 3),(\mathrm{T}, 4),(\mathrm{T}, 5),(\mathrm{T}, 6)\} \\
\mathrm{E}= & \{(\mathrm{T}, 5),(\mathrm{T}, 6)\} \text { and } \mathrm{E} \cap \mathrm{~F}=\{(\mathrm{T}, 5),(\mathrm{T}, 6)\} \\
\mathrm{P}(\mathrm{~F})= & \mathrm{P}(\{(\mathrm{H}, \mathrm{~T})\})+\mathrm{P}(\{(\mathrm{~T}, 1)\})+\mathrm{P}(\{(\mathrm{~T}, 2)\})+\mathrm{P}(\{(\mathrm{~T}, 3)\}) \\
& +\mathrm{P}(\{(\mathrm{~T}, 4)\})+\mathrm{P}(\{(\mathrm{~T}, 5)\})+\mathrm{P}(\{(\mathrm{~T}, 6)\}) \\
= & \frac{1}{4}+\frac{1}{12}+\frac{1}{12}+\frac{1}{12}+\frac{1}{12}+\frac{1}{12}+\frac{1}{12}=\frac{3}{4}
\end{aligned}
$$

and

$$
P(E \cap F)=P(\{(T, 5)\})+P(\{(T, 6)\})=\frac{1}{12}+\frac{1}{12}=\frac{1}{6}
$$

Hence

$$
\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}=\frac{\frac{1}{6}}{\frac{3}{4}}=\frac{2}{9}
$$

## EXERCISE 13.1

1. Given that E and F are events such that $\mathrm{P}(\mathrm{E})=0.6, \mathrm{P}(\mathrm{F})=0.3$ and $\mathrm{P}(\mathrm{E} \cap \mathrm{F})=0.2$, find $\mathrm{P}(\mathrm{E} \mid \mathrm{F})$ and $\mathrm{P}(\mathrm{F} \mid \mathrm{E})$
2. Compute $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$, if $\mathrm{P}(\mathrm{B})=0.5$ and $\mathrm{P}(\mathrm{A} \cap \mathrm{B})=0.32$
3. If $\mathrm{P}(\mathrm{A})=0.8, \mathrm{P}(\mathrm{B})=0.5$ and $\mathrm{P}(\mathrm{B} \mid \mathrm{A})=0.4$, find
(i) $\mathrm{P}(\mathrm{A} \cap \mathrm{B})$
(ii) $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$
(iii) $\mathrm{P}(\mathrm{A} \cup \mathrm{B})$
4. Evaluate $\mathrm{P}(\mathrm{A} \cup \mathrm{B})$, if $2 \mathrm{P}(\mathrm{A})=\mathrm{P}(\mathrm{B})=\frac{5}{13}$ and $\mathrm{P}(\mathrm{A} \mid \mathrm{B})=\frac{2}{5}$
5. If $\mathrm{P}(\mathrm{A})=\frac{6}{11}, \mathrm{P}(\mathrm{B})=\frac{5}{11}$ and $\mathrm{P}(\mathrm{A} \cup \mathrm{B})=\frac{7}{11}$, find
(i) $\mathrm{P}(\mathrm{A} \cap \mathrm{B})$
(ii) $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$
(iii) $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$

Determine $\mathrm{P}(\mathrm{E} \mid \mathrm{F})$ in Exercises 6 to 9.
6. A coin is tossed three times, where
(i) E : head on third toss, F : heads on first two tosses
(ii) E : at least two heads, F : at most two heads
(iii) E : at most two tails, F : at least one tail
7. Two coins are tossed once, where
(i) E: tail appears on one coin, F: one coin shows head
(ii) E: no tail appears, F : no head appears
8. A die is thrown three times,
$\mathrm{E}: 4$ appears on the third toss, $\mathrm{F}: 6$ and 5 appears respectively on first two tosses
9. Mother, father and son line up at random for a family picture
$E$ : son on one end, $\quad F$ : father in middle
10. A black and a red dice are rolled.
(a) Find the conditional probability of obtaining a sum greater than 9 , given that the black die resulted in a 5.
(b) Find the conditional probability of obtaining the sum 8, given that the red die resulted in a number less than 4 .
11. A fair die is rolled. Consider events $\mathrm{E}=\{1,3,5\}, \mathrm{F}=\{2,3\}$ and $\mathrm{G}=\{2,3,4,5\}$ Find
(i) $\mathrm{P}(\mathrm{E} \mid \mathrm{F})$ and $\mathrm{P}(\mathrm{F} \mid \mathrm{E})$
(ii) $\mathrm{P}(\mathrm{E} \mid \mathrm{G})$ and $\mathrm{P}(\mathrm{G} \mid \mathrm{E})$
(iii) $\mathrm{P}((\mathrm{E} \cup \mathrm{F}) \mid \mathrm{G})$ and $\mathrm{P}((\mathrm{E} \cap \mathrm{F}) \mid \mathrm{G})$
12. Assume that each born child is equally likely to be a boy or a girl. If a family has two children, what is the conditional probability that both are girls given that (i) the youngest is a girl, (ii) at least one is a girl?
13. An instructor has a question bank consisting of 300 easy True / False questions, 200 difficult True / False questions, 500 easy multiple choice questions and 400 difficult multiple choice questions. If a question is selected at random from the question bank, what is the probability that it will be an easy question given that it is a multiple choice question?
14. Given that the two numbers appearing on throwing two dice are different. Find the probability of the event 'the sum of numbers on the dice is 4 '.
15. Consider the experiment of throwing a die, if a multiple of 3 comes up, throw the die again and if any other number comes, toss a coin. Find the conditional probability of the event 'the coin shows a tail', given that 'at least one die shows a 3 '.
In each of the Exercises 16 and 17 choose the correct answer:
16. If $\mathrm{P}(\mathrm{A})=\frac{1}{2}, \mathrm{P}(\mathrm{B})=0$, then $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$ is
(A) 0
(B) $\frac{1}{2}$
(C) not defined
(D) 1
17. If A and B are events such that $\mathrm{P}(\mathrm{A} \mid \mathrm{B})=\mathrm{P}(\mathrm{B} \mid \mathrm{A})$, then
(A) $\mathrm{A} \subset \mathrm{B}$ but $\mathrm{A} \neq \mathrm{B}$
(B) $\mathrm{A}=\mathrm{B}$
(C) $\mathrm{A} \cap \mathrm{B}=\phi$
(D) $\mathrm{P}(\mathrm{A})=\mathrm{P}(\mathrm{B})$

### 13.3 Multiplication Theorem on Probability

Let E and F be two events associated with a sample space S . Clearly, the set $\mathrm{E} \cap \mathrm{F}$ denotes the event that both E and F have occurred. In other words, $\mathrm{E} \cap \mathrm{F}$ denotes the simultaneous occurrence of the events E and F . The event $\mathrm{E} \cap \mathrm{F}$ is also written as EF .

Very often we need to find the probability of the event EF . For example, in the experiment of drawing two cards one after the other, we may be interested in finding the probability of the event 'a king and a queen'. The probability of event EF is obtained by using the conditional probability as obtained below:

We know that the conditional probability of event E given that F has occurred is denoted by $\mathrm{P}(\mathrm{EIF})$ and is given by

$$
\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{~F})}, \mathrm{P}(\mathrm{~F}) \neq 0
$$

From this result, we can write

$$
\begin{equation*}
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\mathrm{~F}) \cdot \mathrm{P}(\mathrm{E} \mid \mathrm{F}) \tag{1}
\end{equation*}
$$

Also, we know that
or

$$
\mathrm{P}(\mathrm{~F} \mid \mathrm{E})=\frac{\mathrm{P}(\mathrm{~F} \cap \mathrm{E})}{\mathrm{P}(\mathrm{E})}, \mathrm{P}(\mathrm{E}) \neq 0
$$

$$
P(F \mid E)=\frac{P(E \cap F)}{P(E)}(\text { since } E \cap F=F \cap E)
$$

Thus,

$$
\begin{equation*}
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\mathrm{E}) . \mathrm{P}(\mathrm{~F} \mid \mathrm{E}) \tag{2}
\end{equation*}
$$

Combining (1) and (2), we find that

$$
\begin{aligned}
\mathrm{P}(\mathrm{E} \cap \mathrm{~F}) & =\mathrm{P}(\mathrm{E}) \mathrm{P}(\mathrm{~F} \mid \mathrm{E}) \\
& =\mathrm{P}(\mathrm{~F}) \mathrm{P}(\mathrm{E} \mid \mathrm{F}) \text { provided } \mathrm{P}(\mathrm{E}) \neq 0 \text { and } \mathrm{P}(\mathrm{~F}) \neq 0 .
\end{aligned}
$$

The above result is known as the multiplication rule of probability.
Let us now take up an example.
Example 8 An urn contains 10 black and 5 white balls. Two balls are drawn from the urn one after the other without replacement. What is the probability that both drawn balls are black?

Solution Let E and F denote respectively the events that first and second ball drawn are black. We have to find $\mathrm{P}(\mathrm{E} \cap \mathrm{F})$ or $\mathrm{P}(\mathrm{EF})$.

Now

$$
P(E)=P(\text { black ball in first draw })=\frac{10}{15}
$$

Also given that the first ball drawn is black, i.e., event E has occurred, now there are 9 black balls and five white balls left in the urn. Therefore, the probability that the second ball drawn is black, given that the ball in the first draw is black, is nothing but the conditional probability of F given that E has occurred.
i.e.

$$
\mathrm{P}(\mathrm{~F} \mid \mathrm{E})=\frac{9}{14}
$$

By multiplication rule of probability, we have

$$
\begin{aligned}
P(E \cap F) & =P(E) P(F \mid E) \\
& =\frac{10}{15} \times \frac{9}{14}=\frac{3}{7}
\end{aligned}
$$

Multiplication rule of probability for more than two events If $\mathrm{E}, \mathrm{F}$ and G are three events of sample space, we have

$$
\mathrm{P}(\mathrm{E} \cap \mathrm{~F} \cap \mathrm{G})=\mathrm{P}(\mathrm{E}) \mathrm{P}(\mathrm{~F} \mid \mathrm{E}) \mathrm{P}(\mathrm{G} \mid(\mathrm{E} \cap \mathrm{~F}))=\mathrm{P}(\mathrm{E}) \mathrm{P}(\mathrm{~F} \mid \mathrm{E}) \mathrm{P}(\mathrm{G} \mid \mathrm{EF})
$$

Similarly, the multiplication rule of probability can be extended for four or more events.

The following example illustrates the extension of multiplication rule of probability for three events.

Example 9 Three cards are drawn successively, without replacement from a pack of 52 well shuffled cards. What is the probability that first two cards are kings and the third card drawn is an ace?

Solution Let K denote the event that the card drawn is king and A be the event that the card drawn is an ace. Clearly, we have to find P (KKA)

Now

$$
\mathrm{P}(\mathrm{~K})=\frac{4}{52}
$$

Also, $\mathrm{P}(\mathrm{K} \mid \mathrm{K})$ is the probability of second king with the condition that one king has already been drawn. Now there are three kings in $(52-1)=51$ cards.

Therefore

$$
\mathrm{P}(\mathrm{~K} \mid \mathrm{K})=\frac{3}{51}
$$

Lastly, $\mathrm{P}(\mathrm{A} \mid \mathrm{KK})$ is the probability of third drawn card to be an ace, with the condition that two kings have already been drawn. Now there are four aces in left 50 cards.

Therefore

$$
\mathrm{P}(\mathrm{~A} \mid \mathrm{KK})=\frac{4}{50}
$$

By multiplication law of probability, we have

$$
\begin{aligned}
\mathrm{P}(\mathrm{KKA}) & =\mathrm{P}(\mathrm{~K}) \quad \mathrm{P}(\mathrm{~K} \mid \mathrm{K}) \quad \mathrm{P}(\mathrm{~A} \mid \mathrm{KK}) \\
& =\frac{4}{52} \times \frac{3}{51} \times \frac{4}{50}=\frac{2}{5525}
\end{aligned}
$$

### 13.4 Independent Events

Consider the experiment of drawing a card from a deck of 52 playing cards, in which the elementary events are assumed to be equally likely. If E and F denote the events 'the card drawn is a spade' and 'the card drawn is an ace' respectively, then

$$
P(E)=\frac{13}{52}=\frac{1}{4} \text { and } P(F)=\frac{4}{52}=\frac{1}{13}
$$

Also E and F is the event ' the card drawn is the ace of spades' so that

$$
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\frac{1}{52}
$$

Hence

$$
P(E \mid F)=\frac{P(E \cap F)}{P(F)}=\frac{\frac{1}{52}}{\frac{1}{13}}=\frac{1}{4}
$$

Since $\mathrm{P}(\mathrm{E})=\frac{1}{4}=\mathrm{P}(\mathrm{E} \mid \mathrm{F})$, we can say that the occurrence of event F has not affected the probability of occurrence of the event E .
We also have

$$
\mathrm{P}(\mathrm{~F} \mid \mathrm{E})=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{~F})}{\mathrm{P}(\mathrm{E})}=\frac{\frac{1}{52}}{\frac{1}{4}}=\frac{1}{13}=\mathrm{P}(\mathrm{~F})
$$

Again, $\mathrm{P}(\mathrm{F})=\frac{1}{13}=\mathrm{P}(\mathrm{F} \mid \mathrm{E})$ shows that occurrence of event E has not affected the probability of occurrence of the event F .

Thus, E and F are two events such that the probability of occurrence of one of them is not affected by occurrence of the other.
Such events are called independent events.

Definition 2 Two events E and F are said to be independent, if
and

$$
\begin{aligned}
& \mathrm{P}(\mathrm{~F} \mid \mathrm{E})=\mathrm{P}(\mathrm{~F}) \text { provided } \mathrm{P}(\mathrm{E}) \neq 0 \\
& \mathrm{P}(\mathrm{E} \mid \mathrm{F})=\mathrm{P}(\mathrm{E}) \text { provided } \mathrm{P}(\mathrm{~F}) \neq 0
\end{aligned}
$$

Thus, in this definition we need to have $\mathrm{P}(\mathrm{E}) \neq 0$ and $\mathrm{P}(\mathrm{F}) \neq 0$
Now, by the multiplication rule of probability, we have

$$
\begin{equation*}
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F} \mid \mathrm{E}) \tag{1}
\end{equation*}
$$

If E and F are independent, then (1) becomes

$$
\begin{equation*}
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F}) \tag{2}
\end{equation*}
$$

Thus, using (2), the independence of two events is also defined as follows:
Definition 3 Let E and F be two events associated with the same random experiment, then $E$ and $F$ are said to be independent if

$$
P(E \cap F)=P(E) \cdot P(F)
$$

## Remarks

(i) Two events E and F are said to be dependent if they are not independent, i.e. if

$$
\mathrm{P}(\mathrm{E} \cap \mathrm{~F}) \neq \mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F})
$$

(ii) Sometimes there is a confusion between independent events and mutually exclusive events. Term 'independent' is defined in terms of 'probability of events' whereas mutually exclusive is defined in term of events (subset of sample space). Moreover, mutually exclusive events never have an outcome common, but independent events, may have common outcome. Clearly, 'independent' and 'mutually exclusive' do not have the same meaning.
In other words, two independent events having nonzero probabilities of occurrence can not be mutually exclusive, and conversely, i.e. two mutually exclusive events having nonzero probabilities of occurrence can not be independent.
(iii) Two experiments are said to be independent if for every pair of events E and F , where E is associated with the first experiment and F with the second experiment, the probability of the simultaneous occurrence of the events E and F when the two experiments are performed is the product of $\mathrm{P}(\mathrm{E})$ and $\mathrm{P}(\mathrm{F})$ calculated separately on the basis of two experiments, i.e., $\mathrm{P}(\mathrm{E} \cap \mathrm{F})=\mathrm{P}(\mathrm{E}) . \mathrm{P}(\mathrm{F})$
(iv) Three events $\mathrm{A}, \mathrm{B}$ and C are said to be mutually independent, if

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A} \cap \mathrm{~B}) & =\mathrm{P}(\mathrm{~A}) \mathrm{P}(\mathrm{~B}) \\
\mathrm{P}(\mathrm{~A} \cap \mathrm{C}) & =\mathrm{P}(\mathrm{~A}) \mathrm{P}(\mathrm{C}) \\
\mathrm{P}(\mathrm{~B} \cap \mathrm{C}) & =\mathrm{P}(\mathrm{~B}) \mathrm{P}(\mathrm{C}) \\
\mathrm{P}(\mathrm{~A} \cap \mathrm{~B} \cap \mathrm{C}) & =\mathrm{P}(\mathrm{~A}) \mathrm{P}(\mathrm{~B}) \mathrm{P}(\mathrm{C})
\end{aligned}
$$

and

If at least one of the above is not true for three given events, we say that the events are not independent.

Example 10 A die is thrown. If E is the event 'the number appearing is a multiple of 3 ' and F be the event 'the number appearing is even' then find whether E and F are independent?

Solution We know that the sample space is $\mathrm{S}=\{1,2,3,4,5,6\}$
Now

$$
E=\{3,6\}, F=\{2,4,6\} \text { and } E \cap F=\{6\}
$$

Then

$$
\mathrm{P}(\mathrm{E})=\frac{2}{6}=\frac{1}{3}, \mathrm{P}(\mathrm{~F})=\frac{3}{6}=\frac{1}{2} \text { and } \mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\frac{1}{6}
$$

Clearly

$$
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F})
$$

Hence E and F are independent events.

Example 11 An unbiased die is thrown twice. Let the event A be 'odd number on the first throw' and B the event 'odd number on the second throw'. Check the independence of the events A and B .

Solution If all the 36 elementary events of the experiment are considered to be equally likely, we have

$$
\mathrm{P}(\mathrm{~A})=\frac{18}{36}=\frac{1}{2} \text { and } \mathrm{P}(\mathrm{~B})=\frac{18}{36}=\frac{1}{2}
$$

Also

$$
\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})=\mathrm{P}(\text { odd number on both throws })
$$

$$
=\frac{9}{36}=\frac{1}{4}
$$

Now

$$
\mathrm{P}(\mathrm{~A}) \mathrm{P}(\mathrm{~B})=\frac{1}{2} \times \frac{1}{2}=\frac{1}{4}
$$

Clearly

$$
\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})=\mathrm{P}(\mathrm{~A}) \times \mathrm{P}(\mathrm{~B})
$$

Thus,
Example 12 Three coins are tossed simultaneously. Consider the event E 'three heads or three tails', F 'at least two heads' and G 'at most two heads'. Of the pairs ( $\mathrm{E}, \mathrm{F}$ ), $(\mathrm{E}, \mathrm{G})$ and $(\mathrm{F}, \mathrm{G})$, which are independent? which are dependent?

Solution The sample space of the experiment is given by

$$
\text { S = \{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT }\}
$$

Clearly

$$
\mathrm{E}=\{\mathrm{HHH}, \mathrm{TTT}\}, \mathrm{F}=\{\mathrm{HHH}, \mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}\}
$$

and

$$
\text { G = \{HHT, HTH, THH, HTT, THT, TTH, TTT }\}
$$

Also

$$
\mathrm{E} \cap \mathrm{~F}=\{\mathrm{HHH}\}, \mathrm{E} \cap \mathrm{G}=\{\mathrm{TTT}\}, \mathrm{F} \cap \mathrm{G}=\{\mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}\}
$$

Therefore

$$
\mathrm{P}(\mathrm{E})=\frac{2}{8}=\frac{1}{4}, \mathrm{P}(\mathrm{~F})=\frac{4}{8}=\frac{1}{2}, \mathrm{P}(\mathrm{G})=\frac{7}{8}
$$

and

$$
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\frac{1}{8}, \mathrm{P}(\mathrm{E} \cap \mathrm{G})=\frac{1}{8}, \mathrm{P}(\mathrm{~F} \cap \mathrm{G})=\frac{3}{8}
$$

Also

$$
\mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F})=\frac{1}{4} \times \frac{1}{2}=\frac{1}{8}, \mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{G})=\frac{1}{4} \times \frac{7}{8}=\frac{7}{32}
$$

and

$$
P(F) \cdot P(G)=\frac{1}{2} \times \frac{7}{8}=\frac{7}{16}
$$

Thus

$$
\begin{aligned}
& \mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F}) \\
& \mathrm{P}(\mathrm{E} \cap \mathrm{G}) \neq \mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{G})
\end{aligned}
$$

and

$$
\mathrm{P}(\mathrm{~F} \cap \mathrm{G}) \neq \mathrm{P}(\mathrm{~F}) \cdot \mathrm{P}(\mathrm{G})
$$

Hence, the events (E and F) are independent, and the events (E and G) and (F and G) are dependent.

Example 13 Prove that if E and F are independent events, then so are the events E and $\mathrm{F}^{\prime}$.

Solution Since E and F are independent, we have

$$
\begin{equation*}
\mathrm{P}(\mathrm{E} \cap \mathrm{~F})=\mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F}) \tag{1}
\end{equation*}
$$

From the venn diagram in Fig 13.3, it is clear that $\mathrm{E} \cap \mathrm{F}$ and $\mathrm{E} \cap \mathrm{F}^{\prime}$ are mutually exclusive events and also $\mathrm{E}=(\mathrm{E} \cap \mathrm{F}) \cup\left(\mathrm{E} \cap \mathrm{F}^{\prime}\right)$.

Therefore

$$
\mathrm{P}(\mathrm{E})=\mathrm{P}(\mathrm{E} \cap \mathrm{~F})+\mathrm{P}\left(\mathrm{E} \cap \mathrm{~F}^{\prime}\right)
$$

or

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{E} \cap \mathrm{~F}^{\prime}\right)= & \mathrm{P}(\mathrm{E})-\mathrm{P}(\mathrm{E} \cap \mathrm{~F}) \\
= & \mathrm{P}(\mathrm{E})-\mathrm{P}(\mathrm{E}) \cdot \mathrm{P}(\mathrm{~F}) \\
& (\mathrm{by}(1)) \\
= & \mathrm{P}(\mathrm{E})(1-\mathrm{P}(\mathrm{~F})) \\
= & \mathrm{P}(\mathrm{E}) \cdot \mathrm{P}\left(\mathrm{~F}^{\prime}\right)
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_66018d76ad34726525c6g-15.jpg?height=306&width=508&top_left_y=1495&top_left_x=893)

Fig 13.3

Hence, E and $\mathrm{F}^{\prime}$ are independent

Note In a similar manner, it can be shown that if the events E and F are independent, then
(a) $\mathrm{E}^{\prime}$ and F are independent,
(b) $\mathrm{E}^{\prime}$ and $\mathrm{F}^{\prime}$ are independent

Example 14 If A and B are two independent events, then the probability of occurrence of at least one of $A$ and $B$ is given by $1-P\left(A^{\prime}\right) P\left(B^{\prime}\right)$

Solution We have

$$
\begin{aligned}
\mathrm{P}(\text { at least one of } \mathrm{A} \text { and } \mathrm{B}) & =\mathrm{P}(\mathrm{~A} \cup \mathrm{~B}) \\
& =\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})-\mathrm{P}(\mathrm{~A} \cap \mathrm{~B}) \\
& =\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})-\mathrm{P}(\mathrm{~A}) \mathrm{P}(\mathrm{~B}) \\
& =\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})[1-\mathrm{P}(\mathrm{~A})] \\
& =\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B}) \cdot \mathrm{P}\left(\mathrm{~A}^{\prime}\right) \\
& =1-\mathrm{P}\left(\mathrm{~A}^{\prime}\right)+\mathrm{P}(\mathrm{~B}) \mathrm{P}\left(\mathrm{~A}^{\prime}\right) \\
& =1-\mathrm{P}\left(\mathrm{~A}^{\prime}\right)[1-\mathrm{P}(\mathrm{~B})] \\
& =1-\mathrm{P}\left(\mathrm{~A}^{\prime}\right) \mathrm{P}\left(\mathrm{~B}^{\prime}\right)
\end{aligned}
$$

## EXERCISE 13.2

1. If $\mathrm{P}(\mathrm{A})=\frac{3}{5}$ and $\mathrm{P}(\mathrm{B})=\frac{1}{5}$, find $\mathrm{P}(\mathrm{A} \cap \mathrm{B})$ if A and B are independent events.
2. Two cards are drawn at random and without replacement from a pack of 52 playing cards. Find the probability that both the cards are black.
3. A box of oranges is inspected by examining three randomly selected oranges drawn without replacement. If all the three oranges are good, the box is approved for sale, otherwise, it is rejected. Find the probability that a box containing 15 oranges out of which 12 are good and 3 are bad ones will be approved for sale.
4. A fair coin and an unbiased die are tossed. Let A be the event 'head appears on the coin' and B be the event ' 3 on the die'. Check whether A and B are independent events or not.
5. A die marked $1,2,3$ in red and $4,5,6$ in green is tossed. Let $A$ be the event, 'the number is even,' and B be the event, 'the number is red'. Are A and B independent?
6. Let E and F be events with $\mathrm{P}(\mathrm{E})=\frac{3}{5}, \mathrm{P}(\mathrm{F})=\frac{3}{10}$ and $\mathrm{P}(\mathrm{E} \cap \mathrm{F})=\frac{1}{5}$. Are E and F independent?
7. Given that the events A and B are such that $\mathrm{P}(\mathrm{A})=\frac{1}{2}, \mathrm{P}(\mathrm{A} \cup \mathrm{B})=\frac{3}{5}$ and $\mathrm{P}(\mathrm{B})=p$. Find $p$ if they are (i) mutually exclusive (ii) independent.
8. Let A and B be independent events with $\mathrm{P}(\mathrm{A})=0.3$ and $\mathrm{P}(\mathrm{B})=0.4$. Find
(i) $\mathrm{P}(\mathrm{A} \cap \mathrm{B})$
(ii) $\mathrm{P}(\mathrm{A} \cup \mathrm{B})$
(iii) $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$
(iv) $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$
9. If A and B are two events such that $\mathrm{P}(\mathrm{A})=\frac{1}{4}, \mathrm{P}(\mathrm{B})=\frac{1}{2}$ and $\mathrm{P}(\mathrm{A} \cap \mathrm{B})=\frac{1}{8}$, find $\mathrm{P}(\operatorname{not} \mathrm{A}$ and not B$)$.
10. Events A and B are such that $\mathrm{P}(\mathrm{A})=\frac{1}{2}, \mathrm{P}(\mathrm{B})=\frac{7}{12}$ and $\mathrm{P}(\operatorname{not} \mathrm{A}$ or $\operatorname{not} \mathrm{B})=\frac{1}{4}$. State whether A and B are independent?
11. Given two independent events $A$ and $B$ such that $P(A)=0.3, P(B)=0.6$. Find
(i) $\mathrm{P}(\mathrm{A}$ and B$)$
(ii) $\mathrm{P}(\mathrm{A}$ and not B$)$
(iii) $\mathrm{P}(\mathrm{A}$ or B$)$
(iv) P (neither A nor B )
12. A die is tossed thrice. Find the probability of getting an odd number at least once.
13. Two balls are drawn at random with replacement from a box containing 10 black and 8 red balls. Find the probability that
(i) both balls are red.
(ii) first ball is black and second is red.
(iii) one of them is black and other is red.
14. Probability of solving specific problem independently by $A$ and $B$ are $\frac{1}{2}$ and $\frac{1}{3}$ respectively. If both try to solve the problem independently, find the probability that
(i) the problem is solved
(ii) exactly one of them solves the problem.
15. One card is drawn at random from a well shuffled deck of 52 cards. In which of the following cases are the events E and F independent?
(i) E : 'the card drawn is a spade'

F : 'the card drawn is an ace'
(ii) E : 'the card drawn is black'

F : 'the card drawn is a king'
(iii) E : 'the card drawn is a king or queen'

F : 'the card drawn is a queen or jack'.
16. In a hostel, $60 \%$ of the students read Hindi newspaper, $40 \%$ read English newspaper and $20 \%$ read both Hindi and English newspapers. A student is selected at random.
(a) Find the probability that she reads neither Hindi nor English newspapers.
(b) If she reads Hindi newspaper, find the probability that she reads English newspaper.
(c) If she reads English newspaper, find the probability that she reads Hindi newspaper.
Choose the correct answer in Exercises 17 and 18.
17. The probability of obtaining an even prime number on each die, when a pair of dice is rolled is
(A) 0
(B) $\frac{1}{3}$
(C) $\frac{1}{12}$
(D) $\frac{1}{36}$
18. Two events $A$ and $B$ will be independent, if
(A) A and B are mutually exclusive
(B) $\mathrm{P}\left(\mathrm{A}^{\prime} \mathrm{B}^{\prime}\right)=[1-\mathrm{P}(\mathrm{A})][1-\mathrm{P}(\mathrm{B})]$
(C) $\mathrm{P}(\mathrm{A})=\mathrm{P}(\mathrm{B})$
(D) $\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})=1$

### 13.5 Bayes' Theorem

Consider that there are two bags I and II. Bag I contains 2 white and 3 red balls and Bag II contains 4 white and 5 red balls. One ball is drawn at random from one of the bags. We can find the probability of selecting any of the bags (i.e. $\frac{1}{2}$ ) or probability of drawing a ball of a particular colour (say white) from a particular bag (say Bag I). In other words, we can find the probability that the ball drawn is of a particular colour, if we are given the bag from which the ball is drawn. But, can we find the probability that the ball drawn is from a particular bag (say Bag II), if the colour of the ball drawn is given? Here, we have to find the reverse probability of Bag II to be selected when an event occurred after it is known. Famous mathematician, John Bayes' solved the problem of finding reverse probability by using conditional probability. The formula developed by him is known as 'Bayes theorem' which was published posthumously in 1763. Before stating and proving the Bayes' theorem, let us first take up a definition and some preliminary results.

### 13.5.1 Partition of a sample space

A set of events $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{\mathrm{n}}$ is said to represent a partition of the sample space S if
(a) $\mathrm{E}_{i} \cap \mathrm{E}_{j}=\phi, i \neq j, i, j=1,2,3, \ldots, n$
(b) $\mathrm{E}_{1} \cup \mathrm{E}_{2} \cup \ldots \cup \mathrm{E}_{n}=\mathrm{S}$ and
(c) $\mathrm{P}\left(\mathrm{E}_{i}\right)>0$ for all $i=1,2, \ldots, n$.

In other words, the events $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ represent a partition of the sample space S if they are pairwise disjoint, exhaustive and have nonzero probabilities.

As an example, we see that any nonempty event E and its complement $\mathrm{E}^{\prime}$ form a partition of the sample space $S$ since they satisfy $E \cap E^{\prime}=\phi$ and $E \cup E^{\prime}=S$.

From the Venn diagram in Fig 13.3, one can easily observe that if E and F are any two events associated with a sample space S , then the set $\left\{\mathrm{E} \cap \mathrm{F}^{\prime}, \mathrm{E} \cap \mathrm{F}, \mathrm{E}^{\prime} \cap \mathrm{F}^{\prime} \mathrm{E}^{\prime} \cap \mathrm{F}^{\prime}\right\}$ is a partition of the sample space S . It may be mentioned that the partition of a sample space is not unique. There can be several partitions of the same sample space.

We shall now prove a theorem known as Theorem of total probability.

### 13.5.2 Theorem of total probability

Let $\left\{\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}\right\}$ be a partition of the sample space S , and suppose that each of the events $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ has nonzero probability of occurrence. Let A be any event associated with S , then

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A}) & =\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{~A} \mid \mathrm{E}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{AlE}_{2}\right)+\ldots+\mathrm{P}\left(\mathrm{E}_{n}\right) \mathrm{P}\left(\mathrm{Al} \mathrm{E}_{n}\right) \\
& =\sum_{j=1}^{n} \mathrm{P}\left(\mathrm{E}_{j}\right) \mathrm{P}\left(\mathrm{Al} \mathrm{E}_{j}\right)
\end{aligned}
$$

Proof Given that $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ is a partition of the sample space S (Fig 13.4). Therefore,
and

$$
\begin{aligned}
\mathrm{S} & =\mathrm{E}_{1} \cup \mathrm{E}_{2} \cup \ldots \cup \mathrm{E}_{n} \\
\mathrm{E}_{i} \cap \mathrm{E}_{j} & =\phi, i \neq j, i, j=1,2, \ldots, n
\end{aligned}
$$

Now, we know that for any event A,

$$
\begin{aligned}
\mathrm{A} & =\mathrm{A} \cap \mathrm{~S} \\
& =\mathrm{A} \cap\left(\mathrm{E}_{1} \cup \mathrm{E}_{2} \cup \ldots \cup \mathrm{E}_{n}\right) \\
& =\left(\mathrm{A} \cap \mathrm{E}_{1}\right) \cup\left(\mathrm{A} \cap \mathrm{E}_{2}\right) \cup \ldots \cup\left(\mathrm{A} \cap \mathrm{E}_{n}\right)
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_07_21_66018d76ad34726525c6g-19.jpg?height=271&width=344&top_left_y=1337&top_left_x=1056)

Fig 13.4

Also $\mathrm{A} \cap \mathrm{E}_{i}$ and $\mathrm{A} \cap \mathrm{E}_{j}$ are respectively the subsets of $\mathrm{E}_{i}$ and $\mathrm{E}_{j}$. We know that $\mathrm{E}_{i}$ and $\mathrm{E}_{j}$ are disjoint, for $i \neq j$, therefore, $\mathrm{A} \cap \mathrm{E}_{i}$ and $\mathrm{A} \cap \mathrm{E}_{j}$ are also disjoint for all $i \neq j, i, j=1,2, \ldots, n$.
Thus,

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A}) & =\mathrm{P}\left[\left(\mathrm{~A} \cap \mathrm{E}_{1}\right) \cup\left(\mathrm{A} \cap \mathrm{E}_{2}\right) \cup \ldots . . \cup\left(\mathrm{A} \cap \mathrm{E}_{n}\right)\right] \\
& =\mathrm{P}\left(\mathrm{~A} \cap \mathrm{E}_{1}\right)+\mathrm{P}\left(\mathrm{~A} \cap \mathrm{E}_{2}\right)+\ldots+\mathrm{P}\left(\mathrm{~A} \cap \mathrm{E}_{n}\right)
\end{aligned}
$$

Now, by multiplication rule of probability, we have

$$
\mathrm{P}\left(\mathrm{~A} \cap \mathrm{E}_{i}\right)=\mathrm{P}\left(\mathrm{E}_{i}\right) \mathrm{P}\left(\mathrm{Al} \mathrm{E}_{i}\right) \text { as } \mathrm{P}\left(\mathrm{E}_{i}\right) \neq 0 \forall i=1,2, \ldots, n
$$

Therefore,

$$
\mathrm{P}(\mathrm{~A})=\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{AlE}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{AlE}_{2}\right)+\ldots+\mathrm{P}\left(\mathrm{E}_{n}\right) \mathrm{P}\left(\mathrm{AlE} \mathrm{E}_{n}\right)
$$

or

$$
\mathrm{P}(\mathrm{~A})=\sum_{j=1}^{n} \mathrm{P}\left(\mathrm{E}_{j}\right) \mathrm{P}\left(\mathrm{AlE}_{j}\right)
$$

Example 15 A person has undertaken a construction job. The probabilities are 0.65 that there will be strike, 0.80 that the construction job will be completed on time if there is no strike, and 0.32 that the construction job will be completed on time if there is a strike. Determine the probability that the construction job will be completed on time.

Solution Let A be the event that the construction job will be completed on time, and B be the event that there will be a strike. We have to find $\mathrm{P}(\mathrm{A})$.
We have

$$
\begin{aligned}
\mathrm{P}(\mathrm{~B}) & =0.65, \mathrm{P}(\text { no strike })=\mathrm{P}\left(\mathrm{~B}^{\prime}\right)=1-\mathrm{P}(\mathrm{~B})=1-0.65=0.35 \\
\mathrm{P}(\mathrm{~A} \mid \mathrm{B}) & =0.32, \mathrm{P}\left(\mathrm{~A} \mid \mathrm{B}^{\prime}\right)=0.80
\end{aligned}
$$

Since events $B$ and $B^{\prime}$ form a partition of the sample space $S$, therefore, by theorem on total probability, we have

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A}) & =\mathrm{P}(\mathrm{~B}) \mathrm{P}(\mathrm{~A} \mid \mathrm{B})+\mathrm{P}\left(\mathrm{~B}^{\prime}\right) \mathrm{P}\left(\mathrm{~A}^{\prime} \mathrm{B}^{\prime}\right) \\
& =0.65 \times 0.32+0.35 \times 0.8 \\
& =0.208+0.28=0.488
\end{aligned}
$$

Thus, the probability that the construction job will be completed in time is 0.488 .
We shall now state and prove the Bayes' theorem.
Bayes' Theorem If $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ are $n$ non empty events which constitute a partition of sample space S , i.e. $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ are pairwise disjoint and $\mathrm{E}_{1} \cup \mathrm{E}_{2} \cup \ldots \cup \mathrm{E}_{n}=\mathrm{S}$ and $A$ is any event of nonzero probability, then

$$
\mathrm{P}\left(\mathrm{E}_{i} \mid \mathrm{A}\right)=\frac{\mathrm{P}\left(\mathrm{E}_{i}\right) \mathrm{P}\left(\mathrm{AlE}_{i}\right)}{\sum_{j=1}^{n} \mathrm{P}\left(\mathrm{E}_{j}\right) \mathrm{P}\left(\mathrm{AlE}_{j}\right)} \quad \text { for any } i=1,2,3, \ldots, n
$$

Proof By formula of conditional probability, we know that

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{E}_{i} \mid \mathrm{A}\right) & =\frac{\mathrm{P}\left(\mathrm{~A} \cap \mathrm{E}_{i}\right)}{\mathrm{P}(\mathrm{~A})} \\
& =\frac{\mathrm{P}\left(\mathrm{E}_{i}\right) \mathrm{P}\left(\mathrm{AlE}_{i}\right)}{\mathrm{P}(\mathrm{~A})} \text { (by multiplication rule of probability) } \\
& =\frac{\mathrm{P}\left(\mathrm{E}_{i}\right) \mathrm{P}\left(\mathrm{AlE} E_{i}\right)}{\sum_{j=1}^{n} \mathrm{P}\left(\mathrm{E}_{j}\right) \mathrm{P}\left(\mathrm{Al} E_{j}\right)} \text { (by the result of theorem of total probability) }
\end{aligned}
$$

Remark The following terminology is generally used when Bayes' theorem is applied.
The events $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ are called hypotheses.
The probability $\mathrm{P}\left(\mathrm{E}_{i}\right)$ is called the priori probability of the hypothesis $\mathrm{E}_{i}$
The conditional probability $\mathrm{P}\left(\mathrm{E}_{i} \mid \mathrm{A}\right)$ is called a posteriori probability of the hypothesis $\mathrm{E}_{i}$.

Bayes' theorem is also called the formula for the probability of "causes". Since the $\mathrm{E}_{i}$ 's are a partition of the sample space S , one and only one of the events $\mathrm{E}_{i}$ occurs (i.e. one of the events $\mathrm{E}_{i}$ must occur and only one can occur). Hence, the above formula gives us the probability of a particular $\mathrm{E}_{i}$ (i.e. a "Cause"), given that the event A has occurred.

The Bayes' theorem has its applications in variety of situations, few of which are illustrated in following examples.

Example 16 Bag I contains 3 red and 4 black balls while another Bag II contains 5 red and 6 black balls. One ball is drawn at random from one of the bags and it is found to be red. Find the probability that it was drawn from Bag II.

Solution Let $\mathrm{E}_{1}$ be the event of choosing the bag $\mathrm{I}, \mathrm{E}_{2}$ the event of choosing the bag II and A be the event of drawing a red ball.

Then

$$
\mathrm{P}\left(\mathrm{E}_{1}\right)=\mathrm{P}\left(\mathrm{E}_{2}\right)=\frac{1}{2}
$$

Also $\quad \mathrm{P}\left(\mathrm{AlE}_{1}\right)=\mathrm{P}($ drawing a red ball from Bag I$)=\frac{3}{7}$
and $\quad \mathrm{P}\left(\mathrm{AIE}_{2}\right)=\mathrm{P}($ drawing a red ball from Bag II $)=\frac{5}{11}$
Now, the probability of drawing a ball from Bag II, being given that it is red, is $\mathrm{P}\left(\mathrm{E}_{2} \mid \mathrm{A}\right)$
By using Bayes' theorem, we have

$$
\mathrm{P}\left(\mathrm{E}_{2} \mid \mathrm{A}\right)=\frac{\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{AlE}_{2}\right)}{\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{AlE}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{AlE}_{2}\right)}=\frac{\frac{1}{2} \times \frac{5}{11}}{\frac{1}{2} \times \frac{3}{7}+\frac{1}{2} \times \frac{5}{11}}=\frac{35}{68}
$$

Example 17 Given three identical boxes I, II and III, each containing two coins. In box I, both coins are gold coins, in box II, both are silver coins and in the box III, there is one gold and one silver coin. A person chooses a box at random and takes out a coin. If the coin is of gold, what is the probability that the other coin in the box is also of gold?

Solution Let $\mathrm{E}_{1}, \mathrm{E}_{2}$ and $\mathrm{E}_{3}$ be the events that boxes I, II and III are chosen, respectively.

Then

$$
\mathrm{P}\left(\mathrm{E}_{1}\right)=\mathrm{P}\left(\mathrm{E}_{2}\right)=\mathrm{P}\left(\mathrm{E}_{3}\right)=\frac{1}{3}
$$

Also, let A be the event that 'the coin drawn is of gold'

Then

$$
\begin{aligned}
& \mathrm{P}\left(\mathrm{AIE}_{1}\right)=\mathrm{P}(\text { a gold coin from bag } \mathrm{I})=\frac{2}{2}=1 \\
& \mathrm{P}\left(\mathrm{AIE}_{2}\right)=\mathrm{P}(\text { a gold coin from bag II })=0 \\
& \mathrm{P}\left(\mathrm{AIE}_{3}\right)=\mathrm{P}(\text { a gold coin from bag III })=\frac{1}{2}
\end{aligned}
$$

Now, the probability that the other coin in the box is of gold

$$
\begin{aligned}
& =\text { the probability that gold coin is drawn from the box } I . \\
& =P\left(E_{1} \mid A\right)
\end{aligned}
$$

By Bayes' theorem, we know that

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{E}_{1} \mid \mathrm{A}\right) & =\frac{\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{AlE}_{1}\right)}{\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{AlE}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{AlE}_{2}\right)+\mathrm{P}\left(\mathrm{E}_{3}\right) \mathrm{P}\left(\mathrm{AlE}_{3}\right)} \\
& =\frac{\frac{1}{3} \times 1}{\frac{1}{3} \times 1+\frac{1}{3} \times 0+\frac{1}{3} \times \frac{1}{2}}=\frac{2}{3}
\end{aligned}
$$

Example 18 Suppose that the reliability of a HIV test is specified as follows:
Of people having HIV, $90 \%$ of the test detect the disease but $10 \%$ go undetected. Of people free of HIV, 99\% of the test are judged HIV-ive but 1\% are diagnosed as showing HIV+ive. From a large population of which only $0.1 \%$ have HIV, one person is selected at random, given the HIV test, and the pathologist reports him/her as HIV+ive. What is the probability that the person actually has HIV?

Solution Let E denote the event that the person selected is actually having HIV and A the event that the person's HIV test is diagnosed as +ive. We need to find $\mathrm{P}(\mathrm{E} \mid \mathrm{A})$.
Also $\mathrm{E}^{\prime}$ denotes the event that the person selected is actually not having HIV.
Clearly, $\left\{\mathrm{E}, \mathrm{E}^{\prime}\right\}$ is a partition of the sample space of all people in the population. We are given that

$$
\mathrm{P}(\mathrm{E})=0.1 \%=\frac{0.1}{100}=0.001
$$

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{E}^{\prime}\right)= & 1-\mathrm{P}(\mathrm{E})=0.999 \\
\mathrm{P}(\mathrm{AlE})= & \mathrm{P}(\text { Person tested as HIV+ive given that he/she } \\
& \text { is actually having HIV) } \\
= & 90 \%=\frac{90}{100}=0.9
\end{aligned}
$$

and

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{AlE}^{\prime}\right)= & \mathrm{P}(\text { Person tested as HIV +ive given that he/she } \\
& \text { is actually not having HIV) } \\
= & 1 \%=\frac{1}{100}=0.01
\end{aligned}
$$

Now, by Bayes' theorem

$$
\begin{aligned}
\mathrm{P}(\mathrm{E} \mid \mathrm{A}) & =\frac{\mathrm{P}(\mathrm{E}) \mathrm{P}(\mathrm{~A} \mid \mathrm{E})}{\mathrm{P}(\mathrm{E}) \mathrm{P}(\mathrm{~A} \mid \mathrm{E})+\mathrm{P}\left(\mathrm{E}^{\prime}\right) \mathrm{P}\left(\mathrm{AlE}^{\prime}\right)} \\
& =\frac{0.001 \times 0.9}{0.001 \times 0.9+0.999 \times 0.01}=\frac{90}{1089} \\
& =0.083 \text { approx. }
\end{aligned}
$$

Thus, the probability that a person selected at random is actually having HIV given that he/she is tested HIV+ive is 0.083 .

Example 19 In a factory which manufactures bolts, machines $\mathrm{A}, \mathrm{B}$ and C manufacture respectively $25 \%, 35 \%$ and $40 \%$ of the bolts. Of their outputs, 5,4 and 2 percent are respectively defective bolts. A bolt is drawn at random from the product and is found to be defective. What is the probability that it is manufactured by the machine $B$ ?
Solution Let events $\mathrm{B}_{1}, \mathrm{~B}_{2}, \mathrm{~B}_{3}$ be the following:
$\mathrm{B}_{1}$ : the bolt is manufactured by machine A
$B_{2}$ : the bolt is manufactured by machine $B$
$\mathrm{B}_{3}$ : the bolt is manufactured by machine C
Clearly, $B_{1}, B_{2}, B_{3}$ are mutually exclusive and exhaustive events and hence, they represent a partition of the sample space.

Let the event E be 'the bolt is defective'.
The event $E$ occurs with $B_{1}$ or with $B_{2}$ or with $B_{3}$. Given that,

$$
\mathrm{P}\left(\mathrm{~B}_{1}\right)=25 \%=0.25, \mathrm{P}\left(\mathrm{~B}_{2}\right)=0.35 \text { and } \mathrm{P}\left(\mathrm{~B}_{3}\right)=0.40
$$

Again $\mathrm{P}(\mathrm{EIB})_{1}=$ Probability that the bolt drawn is defective given that it is manufactured by machine $\mathrm{A}=5 \%=0.05$
Similarly, $\quad \mathrm{P}\left(\mathrm{ElB}_{2}\right)=0.04, \mathrm{P}\left(\mathrm{ElB}_{3}\right)=0.02$.

Hence, by Bayes' Theorem, we have

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{~B}_{2} \mid \mathrm{E}\right) & =\frac{\mathrm{P}\left(\mathrm{~B}_{2}\right) \mathrm{P}\left(\mathrm{ElB}_{2}\right)}{\mathrm{P}\left(\mathrm{~B}_{1}\right) \mathrm{P}\left(\mathrm{ElB}_{1}\right)+\mathrm{P}\left(\mathrm{~B}_{2}\right) \mathrm{P}\left(\mathrm{ElB}_{2}\right)+\mathrm{P}\left(\mathrm{~B}_{3}\right) \mathrm{P}\left(\mathrm{ElB}_{3}\right)} \\
& =\frac{0.35 \times 0.04}{0.25 \times 0.05+0.35 \times 0.04+0.40 \times 0.02} \\
& =\frac{0.0140}{0.0345}=\frac{28}{69}
\end{aligned}
$$

Example 20 A doctor is to visit a patient. From the past experience, it is known that the probabilities that he will come by train, bus, scooter or by other means of transport are respectively $\frac{3}{10}, \frac{1}{5}, \frac{1}{10}$ and $\frac{2}{5}$. The probabilities that he will be late are $\frac{1}{4}, \frac{1}{3}$, and $\frac{1}{12}$, if he comes by train, bus and scooter respectively, but if he comes by other means of transport, then he will not be late. When he arrives, he is late. What is the probability that he comes by train?
Solution Let E be the event that the doctor visits the patient late and let $\mathrm{T}_{1}, \mathrm{~T}_{2}, \mathrm{~T}_{3}, \mathrm{~T}_{4}$ be the events that the doctor comes by train, bus, scooter, and other means of transport respectively.

Then

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{~T}_{1}\right) & =\frac{3}{10}, \mathrm{P}\left(\mathrm{~T}_{2}\right)=\frac{1}{5}, \mathrm{P}\left(\mathrm{~T}_{3}\right)=\frac{1}{10} \text { and } \mathrm{P}\left(\mathrm{~T}_{4}\right)=\frac{2}{5} \quad \text { (given) } \\
\mathrm{P}\left(\mathrm{EIT}_{1}\right) & =\text { Probability that the doctor arriving late comes by train }=\frac{1}{4}
\end{aligned}
$$

Similarly, $\left.\mathrm{P}\left(\mathrm{ElT}_{2}\right)=\frac{1}{3}, \mathrm{P}(\mathrm{ElT})_{3}\right)=\frac{1}{12}$ and $\mathrm{P}\left(\mathrm{ElT}_{4}\right)=0$, since he is not late if he comes by other means of transport.

Therefore, by Bayes' Theorem, we have

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{~T}_{1} \mid \mathrm{E}\right) & =\text { Probability that the doctor arriving late comes by train } \\
& =\frac{\mathrm{P}\left(\mathrm{~T}_{1}\right) \mathrm{P}\left(\mathrm{ElT}_{1}\right)}{\mathrm{P}\left(\mathrm{~T}_{1}\right) \mathrm{P}\left(\mathrm{ElT}_{1}\right)+\mathrm{P}\left(\mathrm{~T}_{2}\right) \mathrm{P}\left(\mathrm{ElT}_{2}\right)+\mathrm{P}\left(\mathrm{~T}_{3}\right) \mathrm{P}\left(\mathrm{ElT}_{3}\right)+\mathrm{P}\left(\mathrm{~T}_{4}\right) \mathrm{P}\left(\mathrm{ElT}_{4}\right)} \\
& =\frac{\frac{3}{10} \times \frac{1}{4}}{\frac{3}{10} \times \frac{1}{4}+\frac{1}{5} \times \frac{1}{3}+\frac{1}{10} \times \frac{1}{12}+\frac{2}{5} \times 0}=\frac{3}{40} \times \frac{120}{18}=\frac{1}{2}
\end{aligned}
$$

Hence, the required probability is $\frac{1}{2}$.

Example 21 A man is known to speak truth 3 out of 4 times. He throws a die and reports that it is a six. Find the probability that it is actually a six.

Solution Let E be the event that the man reports that six occurs in the throwing of the die and let $S_{1}$ be the event that six occurs and $S_{2}$ be the event that six does not occur.

Then

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{~S}_{1}\right)= & \text { Probability that } \text { si } x \text { occurs }=\frac{1}{6} \\
\mathrm{P}\left(\mathrm{~S}_{2}\right)= & \text { Probability that } \text { six } \text { does not occur }=\frac{5}{6} \\
\mathrm{P}\left(\mathrm{EIS}_{1}\right)= & \text { Probability that the man reports that six occurs when six has } \\
& \text { actually occurred on the die } \\
= & \text { Probability that the man speaks the truth }=\frac{3}{4} \\
\mathrm{P}\left(\mathrm{EIS}_{2}\right)= & \text { Probability that the man reports that six } \text { occurs when six } \text { has } \\
& \text { not actually occurred on the die } \\
= & \text { Probability that the man does not speak the truth }=1-\frac{3}{4}=\frac{1}{4} \\
& \text { Thus, by Bayes' theorem, we get } \\
\mathrm{P}\left(\mathrm{~S}_{1} \mid \mathrm{E}\right)= & \text { Probability that the report of the man that six has occurred is } \\
& \text { actually a six } \\
= & \frac{\mathrm{P}\left(\mathrm{~S}_{1}\right) \mathrm{P}\left(\mathrm{E} \mid \mathrm{S}_{1}\right)}{\mathrm{P}\left(\mathrm{~S}_{1}\right) \mathrm{P}\left(\mathrm{EIS}_{1}\right)+\mathrm{P}\left(\mathrm{~S}_{2}\right) \mathrm{P}\left(\mathrm{EI} \mathrm{~S}_{2}\right)} \\
= & \frac{1}{\frac{1}{6} \times \frac{3}{4}+\frac{3}{6} \times \frac{1}{4}}=\frac{1}{8} \times \frac{24}{8}=\frac{3}{8}
\end{aligned}
$$

Hence, the required probability is $\frac{3}{8}$.
Remark A random variable is a real valued function whose domain is the sample space of a random experiment.

For example, let us consider the experiment of tossing a coin two times in succession. The sample space of the experiment is $\mathrm{S}=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$.

If X denotes the number of heads obtained, then X is a random variable and for each outcome, its value is as given below :

$$
\mathrm{X}(\mathrm{HH})=2, \mathrm{X}(\mathrm{HT})=1, \mathrm{X}(\mathrm{TH})=1, \mathrm{X}(\mathrm{TT})=0 .
$$

More than one random variables can be defined on the same sample space. For example, let Y denote the number of heads minus the number of tails for each outcome of the above sample space $S$.

Then

$$
\mathrm{Y}(\mathrm{HH})=2, \mathrm{Y}(\mathrm{HT})=0, \mathrm{Y}(\mathrm{TH})=0, \mathrm{Y}(\mathrm{TT})=-2 .
$$

Thus, $X$ and $Y$ are two different random variables defined on the same sample space S .

## EXERCISE 13.3

1. An urn contains 5 red and 5 black balls. A ball is drawn at random, its colour is noted and is returned to the urn. Moreover, 2 additional balls of the colour drawn are put in the urn and then a ball is drawn at random. What is the probability that the second ball is red?
2. A bag contains 4 red and 4 black balls, another bag contains 2 red and 6 black balls. One of the two bags is selected at random and a ball is drawn from the bag which is found to be red. Find the probability that the ball is drawn from the first bag.
3. Of the students in a college, it is known that $60 \%$ reside in hostel and $40 \%$ are day scholars (not residing in hostel). Previous year results report that $30 \%$ of all students who reside in hostel attain A grade and $20 \%$ of day scholars attain A grade in their annual examination. At the end of the year, one student is chosen at random from the college and he has an A grade, what is the probability that the student is a hostlier?
4. In answering a question on a multiple choice test, a student either knows the answer or guesses. Let $\frac{3}{4}$ be the probability that he knows the answer and $\frac{1}{4}$ be the probability that he guesses. Assuming that a student who guesses at the answer will be correct with probability $\frac{1}{4}$. What is the probability that the student knows the answer given that he answered it correctly?
5. A laboratory blood test is $99 \%$ effective in detecting a certain disease when it is in fact, present. However, the test also yields a false positive result for $0.5 \%$ of the healthy person tested (i.e. if a healthy person is tested, then, with probability 0.005 , the test will imply he has the disease). If 0.1 percent of the population
actually has the disease, what is the probability that a person has the disease given that his test result is positive ?
6. There are three coins. One is a two headed coin (having head on both faces), another is a biased coin that comes up heads $75 \%$ of the time and third is an unbiased coin. One of the three coins is chosen at random and tossed, it shows heads, what is the probability that it was the two headed coin?
7. An insurance company insured 2000 scooter drivers, 4000 car drivers and 6000 truck drivers. The probability of an accidents are $0.01,0.03$ and 0.15 respectively. One of the insured persons meets with an accident. What is the probability that he is a scooter driver?
8. A factory has two machines A and B. Past record shows that machine A produced $60 \%$ of the items of output and machine B produced $40 \%$ of the items. Further, $2 \%$ of the items produced by machine $A$ and $1 \%$ produced by machine $B$ were defective. All the items are put into one stockpile and then one item is chosen at random from this and is found to be defective. What is the probability that it was produced by machine B ?
9. Two groups are competing for the position on the Board of directors of a corporation. The probabilities that the first and the second groups will win are 0.6 and 0.4 respectively. Further, if the first group wins, the probability of introducing a new product is 0.7 and the corresponding probability is 0.3 if the second group wins. Find the probability that the new product introduced was by the second group.
10. Suppose a girl throws a die. If she gets a 5 or 6 , she tosses a coin three times and notes the number of heads. If she gets $1,2,3$ or 4 , she tosses a coin once and notes whether a head or tail is obtained. If she obtained exactly one head, what is the probability that she threw $1,2,3$ or 4 with the die?
11. A manufacturer has three machine operators $A, B$ and $C$. The first operator $A$ produces $1 \%$ defective items, where as the other two operators B and C produce $5 \%$ and $7 \%$ defective items respectively. A is on the job for $50 \%$ of the time, $B$ is on the job for $30 \%$ of the time and $C$ is on the job for $20 \%$ of the time. A defective item is produced, what is the probability that it was produced by A ?
12. A card from a pack of 52 cards is lost. From the remaining cards of the pack, two cards are drawn and are found to be both diamonds. Find the probability of the lost card being a diamond.
13. Probability that A speaks truth is $\frac{4}{5}$. A coin is tossed. A reports that a head appears. The probability that actually there was head is
(A) $\frac{4}{5}$
(B) $\frac{1}{2}$
(C) $\frac{1}{5}$
(D) $\frac{2}{5}$
14. If $A$ and $B$ are two events such that $A \subset B$ and $P(B) \neq 0$, then which of the following is correct?
(A) $\mathrm{P}(\mathrm{A} \mid \mathrm{B})=\frac{\mathrm{P}(\mathrm{B})}{\mathrm{P}(\mathrm{A})}$
(B) $\mathrm{P}(\mathrm{A} \mid \mathrm{B})<\mathrm{P}(\mathrm{A})$
(C) $\mathrm{P}(\mathrm{A} \mid \mathrm{B}) \geq \mathrm{P}(\mathrm{A})$
(D) None of these

## Miscellaneous Examples

Example 22 Coloured balls are distributed in four boxes as shown in the following table:

| Box | Colour |  |  |  |
| :---: | :---: | :---: | :---: | :---: |
|  | Black | White | Red | Blue |
| I | 3 | 4 | 5 | 6 |
| II | 2 | 2 | 2 | 2 |
| III | 1 | 2 | 3 | 1 |
| IV | 4 | 3 | 1 | 5 |

A box is selected at random and then a ball is randomly drawn from the selected box. The colour of the ball is black, what is the probability that ball drawn is from the box III?

Solution Let $\mathrm{A}, \mathrm{E}_{1}, \mathrm{E}_{2}, \mathrm{E}_{3}$ and $\mathrm{E}_{4}$ be the events as defined below :
A : a black ball is selected
$\mathrm{E}_{1}$ : box I is selected
$\mathrm{E}_{2}$ : box II is selected
$\mathrm{E}_{3}$ : box III is selected
$\mathrm{E}_{4}$ : box IV is selected

Since the boxes are chosen at random,

Therefore

$$
\mathrm{P}\left(\mathrm{E}_{1}\right)=\mathrm{P}\left(\mathrm{E}_{2}\right)=\mathrm{P}\left(\mathrm{E}_{3}\right)=\mathrm{P}\left(\mathrm{E}_{4}\right)=\frac{1}{4}
$$

Also

$$
\mathrm{P}\left(\mathrm{AlE}_{1}\right)=\frac{3}{18}, \mathrm{P}\left(\mathrm{AlE}_{2}\right)=\frac{2}{8}, \mathrm{P}\left(\mathrm{AlE}_{3}\right)=\frac{1}{7} \text { and } \mathrm{P}\left(\mathrm{AlE}_{4}\right)=\frac{4}{13}
$$

$\mathrm{P}($ box III is selected, given that the drawn ball is black $)=\mathrm{P}\left(\mathrm{E}_{3} \mid \mathrm{A}\right)$. By Bayes' theorem,

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{E}_{3} \mid \mathrm{A}\right) & =\frac{\mathrm{P}\left(\mathrm{E}_{3}\right) \cdot \mathrm{P}\left(\mathrm{AlE}_{3}\right)}{\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{AlE}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{AlE}_{2}\right)+\mathrm{P}\left(\mathrm{E}_{3}\right) \mathrm{P}\left(\mathrm{AlE}_{3}\right)+\mathrm{P}\left(\mathrm{E}_{4}\right) \mathrm{P}\left(\mathrm{AlE}_{4}\right)} \\
& =\frac{\frac{1}{4} \times \frac{1}{7}}{\frac{1}{4} \times \frac{3}{18}+\frac{1}{4} \times \frac{1}{4}+\frac{1}{4} \times \frac{1}{7}+\frac{1}{4} \times \frac{4}{13}}=0.165
\end{aligned}
$$

Example 23 A and B throw a die alternatively till one of them gets a ' 6 ' and wins the game. Find their respective probabilities of winning, if A starts first.
Solution Let S denote the success (getting a '6') and F denote the failure (not getting a ' 6 ').

Thus,

$$
\mathrm{P}(\mathrm{~S})=\frac{1}{6}, \mathrm{P}(\mathrm{~F})=\frac{5}{6}
$$

$$
\mathrm{P}(\mathrm{~A} \text { wins in the first throw })=\mathrm{P}(\mathrm{~S})=\frac{1}{6}
$$

A gets the third throw, when the first throw by A and second throw by B result into failures.
Therefore, $\quad \mathrm{P}(\mathrm{A}$ wins in the 3rd throw $)=\mathrm{P}(\mathrm{FFS})=\mathrm{P}(\mathrm{F}) \mathrm{P}(\mathrm{F}) \mathrm{P}(\mathrm{S})=\frac{5}{6} \times \frac{5}{6} \times \frac{1}{6}$

$$
=\left(\frac{5}{6}\right)^{2} \times \frac{1}{6}
$$

$\mathrm{P}(\mathrm{A}$ wins in the 5 th throw $)=\mathrm{P}(\mathrm{FFFFS})=\left(\frac{5}{6}\right)^{4}\left(\frac{1}{6}\right)$ and so on.

Hence,

$$
\begin{aligned}
P(\text { A wins }) & =\frac{1}{6}+\left(\frac{5}{6}\right)^{2}\left(\frac{1}{6}\right)+\left(\frac{5}{6}\right)^{4}\left(\frac{1}{6}\right)+\ldots \\
& =\frac{\frac{1}{6}}{1-\frac{25}{36}}=\frac{6}{11} \\
P(\text { B wins }) & =1-P(\text { A wins })=1-\frac{6}{11}=\frac{5}{11}
\end{aligned}
$$

Remark If $a+a r+a r^{2}+\ldots+a r^{n-1}+\ldots$, where $|r|<1$, then sum of this infinite G.P. is given by $\frac{a}{1-r} \cdot$ (Refer A.1.3 of Class XI Text book).

Example 24 If a machine is correctly set up, it produces $90 \%$ acceptable items. If it is incorrectly set up, it produces only $40 \%$ acceptable items. Past experience shows that $80 \%$ of the set ups are correctly done. If after a certain set up, the machine produces 2 acceptable items, find the probability that the machine is correctly setup.

Solution Let A be the event that the machine produces 2 acceptable items.
Also let $B_{1}$ represent the event of correct set up and $B_{2}$ represent the event of incorrect setup.

Now

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{~B}_{1}\right) & =0.8, \mathrm{P}\left(\mathrm{~B}_{2}\right)=0.2 \\
\mathrm{P}\left(\mathrm{~A} \mid \mathrm{B}_{1}\right) & =0.9 \times 0.9 \text { and } \mathrm{P}\left(\mathrm{~A} \mid \mathrm{B}_{2}\right)=0.4 \times 0.4
\end{aligned}
$$

Therefore

$$
\begin{aligned}
\mathrm{P}\left(\mathrm{~B}_{1} \mid \mathrm{A}\right) & =\frac{\mathrm{P}\left(\mathrm{~B}_{1}\right) \mathrm{P}\left(\left.\mathrm{AlB}\right|_{1}\right)}{\mathrm{P}\left(\mathrm{~B}_{1}\right) \mathrm{P}\left(\left.\mathrm{AlB}\right|_{1}\right)+\mathrm{P}\left(\mathrm{~B}_{2}\right) \mathrm{P}\left(\left.\mathrm{AlB}\right|_{2}\right)} \\
& =\frac{0.8 \times 0.9 \times 0.9}{0.8 \times 0.9 \times 0.9+0.2 \times 0.4 \times 0.4}=\frac{648}{680}=0.95
\end{aligned}
$$

## Miscellaneous Exercise on Chapter 13

1. A and B are two events such that $\mathrm{P}(\mathrm{A}) \neq 0$. Find $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$, if
(i) A is a subset of B
(ii) $\mathrm{A} \cap \mathrm{B}=\phi$
2. A couple has two children,
(i) Find the probability that both children are males, if it is known that at least one of the children is male.
(ii) Find the probability that both children are females, if it is known that the elder child is a female.
3. Suppose that $5 \%$ of men and $0.25 \%$ of women have grey hair. A grey haired person is selected at random. What is the probability of this person being male? Assume that there are equal number of males and females.
4. Suppose that $90 \%$ of people are right-handed. What is the probability that at most 6 of a random sample of 10 people are right-handed?
5. If a leap year is selected at random, what is the chance that it will contain 53 tuesdays?
6. Suppose we have four boxes $\mathrm{A}, \mathrm{B}, \mathrm{C}$ and D containing coloured marbles as given below:

| Box | Marble colour |  |  |
| :---: | :---: | :---: | :---: |
|  | Red | White | Black |
| A | 1 | 6 | 3 |
| B | 6 | 2 | 2 |
| C | 8 | 1 | 1 |
| D | 0 | 6 | 4 |

One of the boxes has been selected at random and a single marble is drawn from it. If the marble is red, what is the probability that it was drawn from box A ?, box B ?, box C ?
7. Assume that the chances of a patient having a heart attack is $40 \%$. It is also assumed that a meditation and yoga course reduce the risk of heart attack by $30 \%$ and prescription of certain drug reduces its chances by $25 \%$. At a time a patient can choose any one of the two options with equal probabilities. It is given that after going through one of the two options the patient selected at random suffers a heart attack. Find the probability that the patient followed a course of meditation and yoga?
8. If each element of a second order determinant is either zero or one, what is the probability that the value of the determinant is positive? (Assume that the individual entries of the determinant are chosen independently, each value being assumed with probability $\frac{1}{2}$ ).
9. An electronic assembly consists of two subsystems, say, A and B. From previous testing procedures, the following probabilities are assumed to be known:

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A} \text { fails }) & =0.2 \\
\mathrm{P}(\mathrm{~B} \text { fails alone }) & =0.15 \\
\mathrm{P}(\mathrm{~A} \text { and } \mathrm{B} \text { fail }) & =0.15
\end{aligned}
$$

Evaluate the following probabilities
(i) P (A failsl B has failed)
(ii) P (A fails alone)
10. Bag I contains 3 red and 4 black balls and Bag II contains 4 red and 5 black balls. One ball is transferred from Bag I to Bag II and then a ball is drawn from Bag II. The ball so drawn is found to be red in colour. Find the probability that the transferred ball is black.

Choose the correct answer in each of the following:
11. If A and B are two events such that $\mathrm{P}(\mathrm{A}) \neq 0$ and $\mathrm{P}(\mathrm{B} \mid \mathrm{A})=1$, then
(A) $\mathrm{A} \subset \mathrm{B}$
(B) $\mathrm{B} \subset \mathrm{A}$
(C) $\mathrm{B}=\phi$
(D) $\mathrm{A}=\phi$
12. If $\mathrm{P}(\mathrm{A} \mid \mathrm{B})>\mathrm{P}(\mathrm{A})$, then which of the following is correct :
(A) $\mathrm{P}(\mathrm{B} \mid \mathrm{A})<\mathrm{P}(\mathrm{B})$
(B) $\mathrm{P}(\mathrm{A} \cap \mathrm{B})<\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B})$
(C) $\mathrm{P}(\mathrm{B} \mid \mathrm{A})>\mathrm{P}(\mathrm{B})$
(D) $\mathrm{P}(\mathrm{B} \mid \mathrm{A})=\mathrm{P}(\mathrm{B})$
13. If A and B are any two events such that $\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A}$ and B$)=\mathrm{P}(\mathrm{A})$, then
(A) $\mathrm{P}(\mathrm{B} \mid \mathrm{A})=1$
(B) $\mathrm{P}(\mathrm{A} \mid \mathrm{B})=1$
(C) $\mathrm{P}(\mathrm{B} \mid \mathrm{A})=0$
(D) $P(A \mid B)=0$

## Summary

The salient features of the chapter are-

- The conditional probability of an event E , given the occurrence of the event F is given by $\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\frac{\mathrm{P}(\mathrm{E} \cap \mathrm{F})}{\mathrm{P}(\mathrm{F})}, \mathrm{P}(\mathrm{F}) \neq 0$
- $0 \leq \mathrm{P}(\mathrm{E} \mid \mathrm{F}) \leq 1, \quad \mathrm{P}\left(\mathrm{E}^{\prime} \mid \mathrm{F}\right)=1-\mathrm{P}(\mathrm{E} \mid \mathrm{F})$
$\mathrm{P}((\mathrm{E} \cup \mathrm{F}) \mid \mathrm{G})=\mathrm{P}(\mathrm{E} \mid \mathrm{G})+\mathrm{P}(\mathrm{F} \mid \mathrm{G})-\mathrm{P}((\mathrm{E} \cap \mathrm{F}) \mid \mathrm{G})$
- $\mathrm{P}(\mathrm{E} \cap \mathrm{F})=\mathrm{P}(\mathrm{E}) \mathrm{P}(\mathrm{F} \mid \mathrm{E}), \mathrm{P}(\mathrm{E}) \neq 0$
$\mathrm{P}(\mathrm{E} \cap \mathrm{F})=\mathrm{P}(\mathrm{F}) \mathrm{P}(\mathrm{E} \mid \mathrm{F}), \mathrm{P}(\mathrm{F}) \neq 0$
- If E and F are independent, then
$\mathrm{P}(\mathrm{E} \cap \mathrm{F})=\mathrm{P}(\mathrm{E}) \mathrm{P}(\mathrm{F})$
$\mathrm{P}(\mathrm{E} \mid \mathrm{F})=\mathrm{P}(\mathrm{E}), \mathrm{P}(\mathrm{F}) \neq 0$
$\mathrm{P}(\mathrm{F} \mid \mathrm{E})=\mathrm{P}(\mathrm{F}), \mathrm{P}(\mathrm{E}) \neq 0$


## - Theorem of total probability

Let $\left\{\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}\right\}$ be a partition of a sample space and suppose that each of $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ has nonzero probability. Let A be any event associated with S , then
$\mathrm{P}(\mathrm{A})=\mathrm{P}\left(\mathrm{E}_{1}\right) \mathrm{P}\left(\mathrm{AlE}_{1}\right)+\mathrm{P}\left(\mathrm{E}_{2}\right) \mathrm{P}\left(\mathrm{AlE}_{2}\right)+\ldots+\mathrm{P}\left(\mathrm{E}_{n}\right) \mathrm{P}\left(\mathrm{AlE}{ }_{n}\right)$

- Bayes' theorem If $E_{1}, E_{2}, \ldots, E_{n}$ are events which constitute a partition of sample space S , i.e. $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ are pairwise disjoint and $\mathrm{E}_{1} \cup \mathrm{E}_{2} \cup \ldots \cup \mathrm{E}_{n}=\mathrm{S}$ and A be any event with nonzero probability, then

$$
\mathrm{P}\left(\mathrm{E}_{i} \mid \mathrm{A}\right)=\frac{\mathrm{P}\left(\mathrm{E}_{\mathrm{i}}\right) \mathrm{P}\left(\mathrm{~A} \mid \mathrm{E}_{\mathrm{i}}\right)}{\sum_{j=1}^{n} \mathrm{P}\left(\mathrm{E}_{j}\right) \mathrm{P}\left(\mathrm{~A} \mid \mathrm{E}_{j}\right)}
$$

## Historical Note

The earliest indication on measurement of chances in game of dice appeared in 1477 in a commentary on Dante's Divine Comedy. A treatise on gambling named liber de Ludo Alcae, by Geronimo Carden (1501-1576) was published posthumously in 1663. In this treatise, he gives the number of favourable cases for each event when two dice are thrown.

Galileo (1564-1642) gave casual remarks concerning the correct evaluation of chance in a game of three dice. Galileo analysed that when three dice are thrown, the sum of the number that appear is more likely to be 10 than the sum 9 , because the number of cases favourable to 10 are more than the number of cases for the appearance of number 9.

Apart from these early contributions, it is generally acknowledged that the true origin of the science of probability lies in the correspondence between two great men of the seventeenth century, Pascal (1623-1662) and Pierre de Fermat (1601-1665). A French gambler, Chevalier de Metre asked Pascal to explain some seeming contradiction between his theoretical reasoning and the observation gathered from gambling. In a series of letters written around 1654, Pascal and Fermat laid the first foundation of science of probability. Pascal solved the problem in algebraic manner while Fermat used the method of combinations.

Great Dutch Scientist, Huygens (1629-1695), became acquainted with the content of the correspondence between Pascal and Fermat and published a first book on probability, "De Ratiociniis in Ludo Aleae" containing solution of many interesting rather than difficult problems on probability in games of chances.

The next great work on probability theory is by Jacob Bernoulli (1654-1705), in the form of a great book, "Ars Conjectendi" published posthumously in 1713 by his nephew, Nicholes Bernoulli. To him is due the discovery of one of the most important probability distribution known as Binomial distribution. The next remarkable work on probability lies in 1993. A. N. Kolmogorov (1903-1987) is credited with the axiomatic theory of probability. His book, 'Foundations of probability' published in 1933, introduces probability as a set function and is considered a 'classic!'.

