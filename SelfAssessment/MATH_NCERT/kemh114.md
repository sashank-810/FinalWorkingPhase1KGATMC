![](https://cdn.mathpix.com/cropped/2025_07_21_a2ea671860ffb9afb1a7g-01.jpg?height=275&width=250&top_left_y=136&top_left_x=812)

## Chapter 14

## PROBABILITY

Where a mathematical reasoning can be had, it is as great a folly to make use of any other, as to grope for a thing in the dark, when you have a candle in your hand. - JOHN ARBUTHNOT

### 14.1 Event

We have studied about random experiment and sample space associated with an experiment. The sample space serves as an universal set for all questions concerned with the experiment.

Consider the experiment of tossing a coin two times. An associated sample space is $\mathrm{S}=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$.

Now suppose that we are interested in those outcomes which correspond to the occurrence of exactly one head. We find that HT and TH are the only elements of S corresponding to the occurrence of this happening (event). These two elements form the set $\mathrm{E}=\{\mathrm{HT}, \mathrm{TH}\}$

We know that the set E is a subset of the sample space S . Similarly, we find the following correspondence between events and subsets of S .

Description of events
Corresponding subset of ' S '
Number of tails is exactly 2
$\mathrm{A}=\{\mathrm{TT}\}$
Number of tails is atleast one
$\mathrm{B}=\{\mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$
Number of heads is atmost one
$\mathrm{C}=\{\mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$
Second toss is not head
$\mathrm{D}=\{\mathrm{HT}, \mathrm{TT}\}$
Number of tails is atmost two
$\mathrm{S}=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$
Number of tails is more than two
$\phi$
The above discussion suggests that a subset of sample space is associated with an event and an event is associated with a subset of sample space. In the light of this we define an event as follows.

[^0]14.1.1 Occurrence of an event Consider the experiment of throwing a die. Let E denotes the event " a number less than 4 appears". If actually ' 1 ' had appeared on the die then we say that event E has occurred. As a matter of fact if outcomes are 2 or 3, we say that event E has occurred

Thus, the event E of a sample space S is said to have occurred if the outcome $\omega$ of the experiment is such that $\omega \in \mathrm{E}$. If the outcome $\omega$ is such that $\omega \notin \mathrm{E}$, we say that the event E has not occurred.
14.1.2 Types of events Events can be classified into various types on the basis of the elements they have.

1. Impossible and Sure Events The empty set $\phi$ and the sample space $S$ describe events. In fact $\phi$ is called an impossible event and S , i.e., the whole sample space is called the sure event.

To understand these let us consider the experiment of rolling a die. The associated sample space is

$$
\mathrm{S}=\{1,2,3,4,5,6\}
$$

Let E be the event " the number appears on the die is a multiple of 7 ". Can you write the subset associated with the event E ?

Clearly no outcome satisfies the condition given in the event, i.e., no element of the sample space ensures the occurrence of the event E. Thus, we say that the empty set only correspond to the event E . In other words we can say that it is impossible to have a multiple of 7 on the upper face of the die. Thus, the event $\mathrm{E}=\phi$ is an impossible event.

Now let us take up another event F "the number turns up is odd or even". Clearly $\mathrm{F}=\{1,2,3,4,5,6\}=$,S , i.e., all outcomes of the experiment ensure the occurrence of the event F . Thus, the event $\mathrm{F}=\mathrm{S}$ is a sure event.
2. Simple Event If an event E has only one sample point of a sample space, it is called a simple (or elementary) event.

In a sample space containing $n$ distinct elements, there are exactly $n$ simple events.

For example in the experiment of tossing two coins, a sample space is

$$
\mathrm{S}=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}
$$

There are four simple events corresponding to this sample space. These are

$$
\mathrm{E}_{1}=\{\mathrm{HH}\}, \mathrm{E}_{2}=\{\mathrm{HT}\}, \mathrm{E}_{3}=\{\mathrm{TH}\} \text { and } \mathrm{E}_{4}=\{\mathrm{TT}\}
$$

3. Compound Event If an event has more than one sample point, it is called a Compound event.

For example, in the experiment of "tossing a coin thrice" the events
E: 'Exactly one head appeared'
F: 'Atleast one head appeared'
G: 'Atmost one head appeared' etc.
are all compound events. The subsets of S associated with these events are

$$
\begin{aligned}
& \mathrm{E}=\{\mathrm{HTT}, \mathrm{THT}, \mathrm{TTH}\} \\
& \mathrm{F}=\{\mathrm{HTT}, \mathrm{THT}, \mathrm{TTH}, \mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}, \mathrm{HHH}\} \\
& \mathrm{G}=\{\mathrm{TTT}, \mathrm{THT}, \mathrm{HTT}, \mathrm{TTH}\}
\end{aligned}
$$

Each of the above subsets contain more than one sample point, hence they are all compound events.
14.1.3 Algebra of events In the Chapter on Sets, we have studied about different ways of combining two or more sets, viz, union, intersection, difference, complement of a set etc. Like-wise we can combine two or more events by using the analogous set notations.

Let $\mathrm{A}, \mathrm{B}, \mathrm{C}$ be events associated with an experiment whose sample space is S .

1. Complementary Event For every event A , there corresponds another event $\mathrm{A}^{\prime}$ called the complementary event to A . It is also called the event 'not A '.

For example, take the experiment 'of tossing three coins'. An associated sample space is

$$
\mathrm{S}=\{\mathrm{HHH}, \mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}, \mathrm{HTT}, \mathrm{THT}, \mathrm{TTH}, \mathrm{TTT}\}
$$

Let $\mathrm{A}=\{\mathrm{HTH}, \mathrm{HHT}, \mathrm{THH}\}$ be the event 'only one tail appears'
Clearly for the outcome HTT, the event A has not occurred. But we may say that the event 'not A' has occurred. Thus, with every outcome which is not in A, we say that 'not A' occurs.

Thus the complementary event 'not A ' to the event A is

$$
\mathrm{A}^{\prime}=\{\mathrm{HHH}, \mathrm{HTT}, \mathrm{THT}, \mathrm{TTH}, \mathrm{TTT}\}
$$

or

$$
A^{\prime}=\{\omega: \omega \in S \text { and } \omega \notin A\}=S-A
$$

2. The Event 'A or B' Recall that union of two sets A and B denoted by A $\sim \mathrm{B}$ contains all those elements which are either in A or in B or in both.

When the sets A and B are two events associated with a sample space, then ' $A \cup B$ ' is the event 'either $A$ or $B$ or both'. This event ' $A \cup B$ ' is also called ' $A$ or $B$ '.
Therefore

$$
\begin{aligned}
\text { Event }^{\prime} A \text { or } B^{\prime} & =A \cup B \\
& =\{\omega: \omega \in A \text { or } \omega \in B\}
\end{aligned}
$$

3. The Event 'A and B' We know that intersection of two sets $A \cap B$ is the set of those elements which are common to both A and B . i.e., which belong to both ' A and B '.
If $A$ and $B$ are two events, then the set $A \cap B$ denotes the event ' $A$ and $B$ '.
Thus, $\quad A \cap B=\{\omega: \omega \in A$ and $\omega \in B\}$
For example, in the experiment of 'throwing a die twice' Let A be the event 'score on the first throw is six' and $B$ is the event 'sum of two scores is atleast 11 ' then

$$
\mathrm{A}=\{(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)\}, \text { and } \mathrm{B}=\{(5,6),(6,5),(6,6)\}
$$

so $\quad A \cap B=\{(6,5),(6,6)\}$
Note that the set $\mathrm{A} \cap \mathrm{B}=\{(6,5),(6,6)\}$ may represent the event 'the score on the first throw is six and the sum of the scores is atleast $11^{\prime}$.
4. The Event 'A but not B' We know that A-B is the set of all those elements which are in A but not in B . Therefore, the set $\mathrm{A}-\mathrm{B}$ may denote the event ' A but not $\mathrm{B}^{\prime}$. We know that

$$
\mathrm{A}-\mathrm{B}=\mathrm{A} \cap \mathrm{~B}^{\prime}
$$

Example 1 Consider the experiment of rolling a die. Let A be the event 'getting a prime number', B be the event 'getting an odd number'. Write the sets representing the events (i) Aor B (ii) A and B (iii) A but not B (iv) 'not A'.

Solution Here $S=\{1,2,3,4,5,6\}, A=\{2,3,5\}$ and $B=\{1,3,5\}$
Obviously
(i) ' A or B ' $=\mathrm{A} \cup \mathrm{B}=\{1,2,3,5\}$
(ii) ' A and B ' $=\mathrm{A} \cap \mathrm{B}=\{3,5\}$
(iii) 'A but not B ' $=\mathrm{A}-\mathrm{B}=\{2\}$
(iv) 'not $\mathrm{A}^{\prime}=\mathrm{A}^{\prime}=\{1,4,6\}$
14.1.4 Mutually exclusive events In the experiment of rolling a die, a sample space is $S=\{1,2,3,4,5,6\}$. Consider events, A 'an odd number appears' and B 'an even number appears'

Clearly the event $A$ excludes the event $B$ and vice versa. In other words, there is no outcome which ensures the occurrence of events $A$ and $B$ simultaneously. Here
$\mathrm{A}=\{1,3,5\}$ and $\mathrm{B}=\{2,4,6\}$
Clearly $\mathrm{A} \cap \mathrm{B}=\phi$, i.e., A and B are disjoint sets.
In general, two events A and B are called mutually exclusive events if the occurrence of any one of them excludes the occurrence of the other event, i.e., if they can not occur simultaneously. In this case the sets A and B are disjoint.

Again in the experiment of rolling a die, consider the events A 'an odd number appears' and event B 'a number less than 4 appears'

Obviously $\mathrm{A}=\{1,3,5\}$ and $\mathrm{B}=\{1,2,3\}$
Now $3 \in \mathrm{~A}$ as well as $3 \in \mathrm{~B}$
Therefore, A and B are not mutually exclusive events.
Remark Simple events of a sample space are always mutually exclusive.
14.1.5 Exhaustive events Consider the experiment of throwing a die. We have $S=\{1,2,3,4,5,6\}$. Let us define the following events

A: 'a number less than 4 appears',
B: 'a number greater than 2 but less than 5 appears'
and
C : 'a number greater than 4 appears'.
Then $\mathrm{A}=\{1,2,3\}, \mathrm{B}=\{3,4\}$ and $\mathrm{C}=\{5,6\}$. We observe that

$$
\mathrm{A} \cup \mathrm{~B} \cup \mathrm{C}=\{1,2,3\} \cup\{3,4\} \cup\{5,6\}=\mathrm{S} .
$$

Such events $\mathrm{A}, \mathrm{B}$ and C are called exhaustive events. In general, if $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{\mathrm{n}}$ are $n$ events of a sample space $S$ and if

$$
\mathrm{E}_{1} \cup \mathrm{E}_{2} \cup \mathrm{E}_{3} \cup \ldots \cup \mathrm{E}_{n}=\cup_{i=1}^{n} \mathrm{E}_{i}=\mathrm{S}
$$

then $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots ., \mathrm{E}_{\mathrm{n}}$ are called exhaustive events.In other words, events $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ are said to be exhaustive if atleast one of them necessarily occurs whenever the experiment is performed.

Further, if $\mathrm{E}_{i} \cap \mathrm{E}_{j}=\phi$ for $i \neq j$ i.e., events $\mathrm{E}_{i}$ and $\mathrm{E}_{j}$ are pairwise disjoint and $\cup_{i=1}^{n} \mathrm{E}_{i}=\mathrm{S}$, then events $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ are called mutually exclusive and exhaustive events.

We now consider some examples.
Example 2 Two dice are thrown and the sum of the numbers which come up on the dice is noted. Let us consider the following events associated with this experiment

A: 'the sum is even'.
B: 'the sum is a multiple of 3 '.
C: 'the sum is less than 4 '.
D: 'the sum is greater than 11 '.
Which pairs of these events are mutually exclusive?

Solution There are 36 elements in the sample space $\mathrm{S}=\{(x, y): x, y=1,2,3,4,5,6\}$. Then

$$
\begin{aligned}
\mathrm{A}= & \{(1,1),(1,3),(1,5),(2,2),(2,4),(2,6),(3,1),(3,3),(3,5),(4,2),(4,4), \\
& (4,6),(5,1),(5,3),(5,5),(6,2),(6,4),(6,6)\} \\
\mathrm{B}= & \{(1,2),(2,1),(1,5),(5,1),(3,3),(2,4),(4,2),(3,6),(6,3),(4,5),(5,4), \\
& (6,6)\} \\
\mathrm{C}= & \{(1,1),(2,1),(1,2)\} \text { and } \mathrm{D}=\{(6,6)\}
\end{aligned}
$$

We find that

$$
A \cap B=\{(1,5),(2,4),(3,3),(4,2),(5,1),(6,6)\} \neq \phi
$$

Therefore, A and B are not mutually exclusive events.
Similarly $\mathrm{A} \cap \mathrm{C} \neq \phi, \mathrm{A} \cap \mathrm{D} \neq \phi, \mathrm{B} \cap \mathrm{C} \neq \phi$ and $\mathrm{B} \cap \mathrm{D} \neq \phi$.
Thus, the pairs of events, (A, C), (A, D), (B, C), (B, D) are not mutually exclusive events.
Also $\mathrm{C} \cap \mathrm{D}=\phi$ and so C and D are mutually exclusive events.
Example 3 A coin is tossed three times, consider the following events.
A: 'No head appears', B: 'Exactly one head appears' and C: 'Atleast two heads appear'.
Do they form a set of mutually exclusive and exhaustive events?
Solution The sample space of the experiment is
$\mathrm{S}=\{\mathrm{HHH}, \mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}, \mathrm{HTT}, \mathrm{THT}, \mathrm{TTH}, \mathrm{TTT}\}$
and $\mathrm{A}=\{\mathrm{TTT}\}, \mathrm{B}=\{\mathrm{HTT}, \mathrm{THT}, \mathrm{TTH}\}, \mathrm{C}=\{\mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}, \mathrm{HHH}\}$
Now
$\mathrm{A} \cup \mathrm{B} \cup \mathrm{C}=\{\mathrm{TTT}, \mathrm{HTT}, \mathrm{THT}, \mathrm{TTH}, \mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}, \mathrm{HHH}\}=\mathrm{S}$
Therefore, $\mathrm{A}, \mathrm{B}$ and C are exhaustive events.
Also, $\quad \mathrm{A} \cap \mathrm{B}=\phi, \mathrm{A} \cap \mathrm{C}=\phi$ and $\mathrm{B} \cap \mathrm{C}=\phi$
Therefore, the events are pair-wise disjoint, i.e., they are mutually exclusive.
Hence, $\mathrm{A}, \mathrm{B}$ and C form a set of mutually exclusive and exhaustive events.

## EXERCISE 14.1

1. A die is rolled. Let E be the event "die shows 4 " and F be the event "die shows even number". Are E and F mutually exclusive?
2. A die is thrown. Describe the following events:
(i) A: a number less than 7
(ii) B: a number greater than 7
(iii) C : a multiple of 3
(iv) D : a number less than 4
(v) E : an even number greater than 4
(vi) F : a number not less than 3

Also find $\mathrm{A} \cup \mathrm{B}, \mathrm{A} \cap \mathrm{B}, \mathrm{B} \cup \mathrm{C}, \mathrm{E} \cap \mathrm{F}, \mathrm{D} \cap \mathrm{E}, \mathrm{A}-\mathrm{C}, \mathrm{D}-\mathrm{E}, \mathrm{E} \cap \mathrm{F}^{\prime}, \mathrm{F}^{\prime}$
3. An experiment involves rolling a pair of dice and recording the numbers that come up. Describe the following events:
A: the sum is greater than $8, \mathrm{~B}: 2$ occurs on either die
C: the sum is at least 7 and a multiple of 3 .
Which pairs of these events are mutually exclusive?
4. Three coins are tossed once. Let A denote the event 'three heads show", B denote the event "two heads and one tail show", C denote the event" three tails show and D denote the event 'a head shows on the first coin". Which events are
(i) mutually exclusive?
(ii) simple?
(iii) Compound?
5. Three coins are tossed. Describe
(i) Two events which are mutually exclusive.
(ii) Three events which are mutually exclusive and exhaustive.
(iii) Two events, which are not mutually exclusive.
(iv) Two events which are mutually exclusive but not exhaustive.
(v) Three events which are mutually exclusive but not exhaustive.
6. Two dice are thrown. The events $\mathrm{A}, \mathrm{B}$ and C are as follows:
$A$ : getting an even number on the first die.
B: getting an odd number on the first die.
C: getting the sum of the numbers on the dice $\leq 5$.
Describe the events
(i) $\mathrm{A}^{\prime}$
(ii) $\operatorname{not} \mathrm{B}$
(iii) A or B
(iv) A and B
(v) A but not C
(vi) B or C
(vii) B and C
(viii) $\mathrm{A} \cap \mathrm{B}^{\prime} \cap \mathrm{C}^{\prime}$
7. Refer to question 6 above, state true or false: (give reason for your answer)
(i) A and B are mutually exclusive
(ii) A and B are mutually exclusive and exhaustive
(iii) $\mathrm{A}=\mathrm{B}^{\prime}$
(iv) A and C are mutually exclusive
(v) A and $\mathrm{B}^{\prime}$ are mutually exclusive.
(vi) $\mathrm{A}^{\prime}, \mathrm{B}^{\prime}, \mathrm{C}$ are mutually exclusive and exhaustive.

### 14.2 Axiomatic Approach to Probability

In earlier sections, we have considered random experiments, sample space and events associated with these experiments. In our day to day life we use many words about the chances of occurrence of events. Probability theory attempts to quantify these chances of occurrence or non occurrence of events.

In earlier classes, we have studied some methods of assigning probability to an event associated with an experiment having known the number of total outcomes.

Axiomatic approach is another way of describing probability of an event. In this approach some axioms or rules are depicted to assign probabilities.

Let S be the sample space of a random experiment. The probability P is a real valued function whose domain is the power set of S and range is the interval $[0,1]$ satisfying the following axioms
(i) For any event $\mathrm{E}, \mathrm{P}(\mathrm{E}) \geq 0$
(ii) $\mathrm{P}(\mathrm{S})=1$
(iii) If E and F are mutually exclusive events, then $\mathrm{P}(\mathrm{E} \cup \mathrm{F})=\mathrm{P}(\mathrm{E})+\mathrm{P}(\mathrm{F})$.

It follows from (iii) that $\mathrm{P}(\phi)=0$. To prove this, we take $\mathrm{F}=\phi$ and note that E and $\phi$ are disjoint events. Therefore, from axiom (iii), we get

$$
P(E \cup \phi)=P(E)+P(\phi) \text { or } \quad P(E)=P(E)+P(\phi) \text { i.e. } P(\phi)=0 \text {. }
$$

Let S be a sample space containing outcomes $\omega_{1}, \omega_{2}, \ldots, \omega_{n}$, i.e.,

$$
S=\left\{\omega_{1}, \omega_{2}, \ldots, \omega_{n}\right\}
$$

It follows from the axiomatic definition of probability that
(i) $0 \leq \mathrm{P}\left(\omega_{i}\right) \leq 1$ for each $\omega_{i} \in \mathrm{~S}$
(ii) $\mathrm{P}\left(\omega_{1}\right)+\mathrm{P}\left(\omega_{2}\right)+\ldots+\mathrm{P}\left(\omega_{n}\right)=1$
(iii) For any event $\mathrm{A}, \mathrm{P}(\mathrm{A})=\sum \mathrm{P}\left(\omega_{i}\right), \omega_{i} \in \mathrm{~A}$.
$\square$ Note It may be noted that the singleton $\left\{\omega_{i}\right\}$ is called elementary event and for notational convenience, we write $\mathrm{P}\left(\omega_{i}\right)$ for $\mathrm{P}\left(\left\{\omega_{i}\right\}\right)$.

For example, in 'a coin tossing' experiment we can assign the number $\frac{1}{2}$ to each of the outcomes H and T .
i.e.

$$
\begin{equation*}
\mathrm{P}(\mathrm{H})=\frac{1}{2} \text { and } \mathrm{P}(\mathrm{~T})=\frac{1}{2} \tag{1}
\end{equation*}
$$

Clearly this assignment satisfies both the conditions i.e., each number is neither less than zero nor greater than 1 and

$$
\mathrm{P}(\mathrm{H})+\mathrm{P}(\mathrm{~T})=\frac{1}{2}+\frac{1}{2}=1
$$

Therefore, in this case we can say that probability of $\mathrm{H}=\frac{1}{2}$, and probability of $\mathrm{T}=\frac{1}{2}$
If we take $\mathrm{P}(\mathrm{H})=\frac{1}{4}$ and $\mathrm{P}(\mathrm{T})=\frac{3}{4}$

Does this assignment satisfy the conditions of axiomatic approach?
Yes, in this case, probability of $\mathrm{H}=\frac{1}{4}$ and probability of $\mathrm{T}=\frac{3}{4}$.
We find that both the assignments (1) and (2) are valid for probability of H and T .

In fact, we can assign the numbers $p$ and $(1-p)$ to both the outcomes such that $0 \leq p \leq 1$ and $\mathrm{P}(\mathrm{H})+\mathrm{P}(\mathrm{T})=p+(1-p)=1$

This assignment, too, satisfies both conditions of the axiomatic approach of probability. Hence, we can say that there are many ways (rather infinite) to assign probabilities to outcomes of an experiment. We now consider some examples.
Example 4 Let a sample space be $S=\left\{\omega_{1}, \omega_{2}, \ldots, \omega_{6}\right\}$. Which of the following assignments of probabilities to each outcome are valid?

Outcomes $\quad \omega_{1} \quad \omega_{2} \quad \omega_{3} \quad \omega_{4} \quad \omega_{5} \quad \omega_{6}$
(a) $\frac{1}{6} \quad \frac{1}{6} \quad \frac{1}{6} \quad \frac{1}{6} \quad \frac{1}{6} \quad \frac{1}{6}$
(b) $\begin{array}{llllll}1 & 0 & 0 & 0 & 0 & 0\end{array}$
(c) $\frac{1}{8} \quad \frac{2}{3} \quad \frac{1}{3} \quad \frac{1}{3} \quad-\frac{1}{4} \quad-\frac{1}{3}$
(d) $\frac{1}{12} \quad \frac{1}{12} \quad \frac{1}{6} \quad \frac{1}{6} \quad \frac{1}{6} \quad \frac{3}{2}$
(e) $\quad \begin{array}{llllll}0.1 & 0.2 & 0.3 & 0.4 & 0.5 & 0.6\end{array}$

Solution (a) Condition (i): Each of the number $\mathrm{p}\left(\omega_{i}\right)$ is positive and less than one.
Condition (ii): Sum of probabilities

$$
=\frac{1}{6}+\frac{1}{6}+\frac{1}{6}+\frac{1}{6}+\frac{1}{6}+\frac{1}{6}=1
$$

Therefore, the assignment is valid
(b) Condition (i): Each of the number $p\left(\omega_{i}\right)$ is either 0 or 1.

Condition (ii) Sum of the probabilities $=1+0+0+0+0+0=1$
Therefore, the assignment is valid
(c) Condition (i) Two of the probabilities $p\left(\omega_{5}\right)$ and $p\left(\omega_{6}\right)$ are negative, the assignment is not valid
(d) Since $p\left(\omega_{6}\right)=\frac{3}{2}>1$, the assignment is not valid
(e) Since, sum of probabilities $=0.1+0.2+0.3+0.4+0.5+0.6=2.1$, the assignment is not valid.
14.2.1 Probability of an event $L$ et $S$ be a sample space associated with the experiment 'examining three consecutive pens produced by a machine and classified as Good (non-defective) and bad (defective)'. We may get $0,1,2$ or 3 defective pens as result of this examination.
A sample space associated with this experiment is

$$
\mathrm{S}=\{\mathrm{BBB}, \mathrm{BBG}, \mathrm{BGB}, \mathrm{GBB}, \mathrm{BGG}, \mathrm{GBG}, \mathrm{GGB}, \mathrm{GGG}\}
$$

where B stands for a defective or bad pen and G for a non - defective or good pen.
Let the probabilities assigned to the outcomes be as follows
Sample point: $\quad$ BBB $\quad$ BBG $\quad$ BGB $\quad$ GBB $\quad$ BGG $\quad$ GBG $\quad$ GGB $\quad$ GGG
Probability: $\quad \frac{1}{8} \quad \frac{1}{8} \quad \frac{1}{8} \quad \frac{1}{8} \quad \frac{1}{8} \quad \frac{1}{8} \quad \frac{1}{8} \quad \frac{1}{8}$
Let event A : there is exactly one defective pen and event B : there are atleast two defective pens.
Hence $\mathrm{A}=\{\mathrm{BGG}, \mathrm{GBG}, \mathrm{GGB}\}$ and $\mathrm{B}=\{\mathrm{BBG}, \mathrm{BGB}, \mathrm{GBB}, \mathrm{BBB}\}$
Now

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A}) & =\sum \mathrm{P}\left(\omega_{i}\right), \forall \omega_{i} \in A \\
& =\mathrm{P}(\mathrm{BGG})+\mathrm{P}(\mathrm{GBG})+\mathrm{P}(\mathrm{GGB})=\frac{1}{8}+\frac{1}{8}+\frac{1}{8}=\frac{3}{8}
\end{aligned}
$$

and

$$
\begin{aligned}
\mathrm{P}(\mathrm{~B}) & =\sum \mathrm{P}\left(\omega_{i}\right), \forall \omega_{i} \in B \\
& =\mathrm{P}(\mathrm{BBG})+\mathrm{P}(\mathrm{BGB})+\mathrm{P}(\mathrm{GBB})+\mathrm{P}(\mathrm{BBB})=\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8}=\frac{4}{8}=\frac{1}{2}
\end{aligned}
$$

Let us consider another experiment of 'tossing a coin "twice"
The sample space of this experiment is $\mathrm{S}=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$
Let the following probabilities be assigned to the outcomes

$$
\mathrm{P}(\mathrm{HH})=\frac{1}{4}, \mathrm{P}(\mathrm{HT})=\frac{1}{7}, \mathrm{P}(\mathrm{TH})=\frac{2}{7}, \mathrm{P}(\mathrm{TT})=\frac{9}{28}
$$

Clearly this assignment satisfies the conditions of axiomatic approach. Now, let us find the probability of the event E : 'Both the tosses yield the same result'.
Here

$$
\mathrm{E}=\{\mathrm{HH}, \mathrm{TT}\}
$$

Now

$$
\mathrm{P}(\mathrm{E})=\Sigma \mathrm{P}\left(w_{i}\right), \text { for all } w_{i} \in \mathrm{E}
$$

$$
=\mathrm{P}(\mathrm{HH})+\mathrm{P}(\mathrm{TT})=\frac{1}{4}+\frac{9}{28}=\frac{4}{7}
$$

For the event F : 'exactly two heads', we have $\mathrm{F}=\{\mathrm{HH}\}$
and

$$
\mathrm{P}(\mathrm{~F})=\mathrm{P}(\mathrm{HH})=\frac{1}{4}
$$

14.2.2 Probabilities of equally likely outcomes Let a sample space of an experiment be

$$
\mathrm{S}=\left\{\omega_{1}, \omega_{2}, \ldots, \omega_{n}\right\}
$$

Let all the outcomes are equally likely to occur, i.e., the chance of occurrence of each simple event must be same.
i.e.

$$
\mathrm{P}\left(\omega_{i}\right)=p, \text { for all } \omega_{i} \in \mathrm{~S} \text { where } 0 \leq p \leq 1
$$

Since

$$
\sum_{i=1}^{n} \mathrm{P}\left(\omega_{i}\right)=1 \text { i.e., } p+p+\ldots+p(n \text { times })=1
$$

or

$$
n p=1 \text { i.e., } p=\frac{1}{n}
$$

Let S be a sample space and E be an event, such that $n(\mathrm{~S})=n$ and $n(\mathrm{E})=m$. If each out come is equally likely, then it follows that

$$
\mathrm{P}(\mathrm{E})=\frac{m}{n} \quad=\frac{\text { Number of outcomes favourable to } \mathrm{E}}{\text { Total possible outcomes }}
$$

14.2.3 Probability of the event ' $A$ or $B$ ' Let us now find the probability of event 'A or B', i.e., $\mathrm{P}(\mathrm{A} \cup \mathrm{B})$
Let $\mathrm{A}=\{\mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}\}$ and $\mathrm{B}=\{\mathrm{HTH}, \mathrm{THH}, \mathrm{HHH}\}$ be two events associated with 'tossing of a coin thrice'
Clearly $\mathrm{A} \cup \mathrm{B}=\{\mathrm{HHT}, \mathrm{HTH}, \mathrm{THH}, \mathrm{HHH}\}$
Now

$$
\mathrm{P}(\mathrm{~A} \cup \mathrm{~B})=\mathrm{P}(\mathrm{HHT})+\mathrm{P}(\mathrm{HTH})+\mathrm{P}(\mathrm{THH})+\mathrm{P}(\mathrm{HHH})
$$

If all the outcomes are equally likely, then

$$
\mathrm{P}(\mathrm{~A} \cup \mathrm{~B})=\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8}=\frac{4}{8}=\frac{1}{2}
$$

Also

$$
\mathrm{P}(\mathrm{~A})=\mathrm{P}(\mathrm{HHT})+\mathrm{P}(\mathrm{HTH})+\mathrm{P}(\mathrm{THH})=\frac{3}{8}
$$

and

$$
\mathrm{P}(\mathrm{~B})=\mathrm{P}(\mathrm{HTH})+\mathrm{P}(\mathrm{THH})+\mathrm{P}(\mathrm{HHH})=\frac{3}{8}
$$

Therefore

$$
\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})=\frac{3}{8}+\frac{3}{8}=\frac{6}{8}
$$

It is clear that

$$
\mathrm{P}(\mathrm{~A} \cup \mathrm{~B}) \neq \mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})
$$

The points HTH and THH are common to both A and B. In the computation of $\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})$ the probabilities of points HTH and THH, i.e., the elements of $\mathrm{A} \cap \mathrm{B}$ are included twice. Thus to get the probability $\mathrm{P}(\mathrm{A} \cup \mathrm{B})$ we have to subtract the probabilities of the sample points in $\mathrm{A} \cap \mathrm{B}$ from $\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})$
i.e.

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A} \cup \mathrm{~B}) & =\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})-\sum \mathrm{P}\left(\omega_{i}\right), \forall \omega_{i} \in A \cap B \\
& =\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})-\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})
\end{aligned}
$$

Thus we observe that, $\mathrm{P}(\mathrm{A} \cup \mathrm{B})=\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A} \cap \mathrm{B})$
In general, if A and B are any two events associated with a random experiment, then by the definition of probability of an event, we have

$$
\mathrm{P}(\mathrm{~A} \cup \mathrm{~B})=\sum p\left(\omega_{i}\right), \forall \omega_{i} \in A \cup B
$$

Since

$$
A \cup B=(A-B) \cup(A \cap B) \cup(B-A)
$$

we have

$$
\begin{equation*}
\mathrm{P}(\mathrm{A} \cup \mathrm{B})=\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in(A-B)\right]+\left[\sum P\left(\omega_{i}\right) \forall \omega_{i} \in A \cap B\right]+\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in B-A\right] \tag{1}
\end{equation*}
$$

(because $\mathrm{A}-\mathrm{B}, \mathrm{A} \cap \mathrm{B}$ and $\mathrm{B}-\mathrm{A}$ are mutually exclusive)
Also $\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})=\left[\sum p\left(\omega_{i}\right) \forall \omega_{i} \in A\right]+\left[\sum p\left(\omega_{i}\right) \forall \omega_{i} \in B\right]$

$$
\begin{aligned}
= & {\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in(A-B) \cup(A \cap B)\right]+\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in(B-A) \cup(A \cap B)\right] } \\
= & {\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in(A-B)\right]+\left[\sum P\left(\omega_{i}\right) \forall \omega_{i} \in(A \cap B)\right]+\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in(B-A)\right]+} \\
& {\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in(A \cap B)\right] } \\
= & \mathrm{P}(\mathrm{~A} \cup \mathrm{~B})+\left[\sum \mathrm{P}\left(\omega_{i}\right) \forall \omega_{i} \in A \cap B\right] \quad[\text { using }(1)] \\
= & \mathrm{P}(\mathrm{~A} \cup \mathrm{~B})+\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})
\end{aligned}
$$

Hence $\quad \mathrm{P}(\mathrm{A} \cup \mathrm{B})=\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A} \cap \mathrm{B})$.
Alternatively, it can also be proved as follows:
$\mathrm{A} \cup \mathrm{B}=\mathrm{A} \cup(\mathrm{B}-\mathrm{A})$, where A and $\mathrm{B}-\mathrm{A}$ are mutually exclusive, and $\mathrm{B}=(\mathrm{A} \cap \mathrm{B}) \cup(\mathrm{B}-\mathrm{A})$, where $\mathrm{A} \cap \mathrm{B}$ and $\mathrm{B}-\mathrm{A}$ are mutually exclusive.
Using Axiom (iii) of probability, we get
and

$$
\begin{align*}
& P(A \cup B)=P(A)+P(B-A)  \tag{2}\\
& P(B)=P(A \cap B)+P(B-A) \tag{3}
\end{align*}
$$

Subtracting (3) from (2) gives
or

$$
\begin{aligned}
& P(A \cup B)-P(B)=P(A)-P(A \cap B) \\
& P(A \cup B)=P(A)+P(B)-P(A \cap B)
\end{aligned}
$$

The above result can further be verified by observing the Venn Diagram (Fig 14.1)
![](https://cdn.mathpix.com/cropped/2025_07_21_a2ea671860ffb9afb1a7g-13.jpg?height=412&width=636&top_left_y=652&top_left_x=473)

Fig 14.1
If A and B are disjoint sets, i.e., they are mutually exclusive events, then $\mathrm{A} \cap \mathrm{B}=\phi$
Therefore

$$
\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})=\mathrm{P}(\phi)=0
$$

Thus, for mutually exclusive events A and B , we have

$$
\mathrm{P}(\mathrm{~A} \cup \mathrm{~B})=\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})
$$

which is Axiom (iii) of probability.
14.2.4 Probability of event 'not $A$ ' Consider the event $\mathrm{A}=\{2,4,6,8\}$ associated with the experiment of drawing a card from a deck of ten cards numbered from 1 to 10 . Clearly the sample space is $\mathrm{S}=\{1,2,3, \ldots, 10\}$

If all the outcomes $1,2, \ldots, 10$ are considered to be equally likely, then the probability of each outcome is $\frac{1}{10}$
Now

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A}) & =\mathrm{P}(2)+\mathrm{P}(4)+\mathrm{P}(6)+\mathrm{P}(8) \\
& =\frac{1}{10}+\frac{1}{10}+\frac{1}{10}+\frac{1}{10}=\frac{4}{10}=\frac{2}{5}
\end{aligned}
$$

Also event 'not A ' $=\mathrm{A}^{\prime}=\{1,3,5,7,9,10\}$
Now

$$
\mathrm{P}\left(\mathrm{~A}^{\prime}\right)=\mathrm{P}(1)+\mathrm{P}(3)+\mathrm{P}(5)+\mathrm{P}(7)+\mathrm{P}(9)+\mathrm{P}(10)
$$

$$
=\frac{6}{10}=\frac{3}{5}
$$

Thus,

$$
\mathrm{P}\left(\mathrm{~A}^{\prime}\right)=\frac{3}{5}=1-\frac{2}{5}=1-\mathrm{P}(\mathrm{~A})
$$

Also, we know that $\mathrm{A}^{\prime}$ and A are mutually exclusive and exhaustive events i.e.,

$$
\mathrm{A} \cap \mathrm{~A}^{\prime}=\phi \text { and } \mathrm{A} \cup \mathrm{~A}^{\prime}=\mathrm{S}
$$

or

$$
\mathrm{P}\left(\mathrm{~A} \cup \mathrm{~A}^{\prime}\right)=\mathrm{P}(\mathrm{~S})
$$

Now

$$
\mathrm{P}(\mathrm{~A})+\mathrm{P}\left(\mathrm{~A}^{\prime}\right)=1, \quad \text { by using axioms (ii) and (iii) }
$$

or

$$
\mathrm{P}\left(\mathrm{~A}^{\prime}\right)=\mathrm{P}(\operatorname{not} \mathrm{~A})=1-\mathrm{P}(\mathrm{~A})
$$

We now consider some examples and exercises having equally likely outcomes unless stated otherwise.

Example 5 One card is drawn from a well shuffled deck of 52 cards. If each outcome is equally likely, calculate the probability that the card will be
(i) a diamond
(ii) not an ace
(iii) a black card (i.e., a club or, a spade)
(iv) not a diamond
(v) not a black card.

Solution When a card is drawn from a well shuffled deck of 52 cards, the number of possible outcomes is 52.
(i) Let A be the event 'the card drawn is a diamond'

Clearly the number of elements in set A is 13 .
Therefore, $\quad \mathrm{P}(\mathrm{A})=\frac{13}{52}=\frac{1}{4}$
i.e. probability of a diamond card $=\frac{1}{4}$
(ii) We assume that the event 'Card drawn is an ace' is B

Therefore 'Card drawn is not an ace' should be $\mathrm{B}^{\prime}$.
We know that $\mathrm{P}\left(\mathrm{B}^{\prime}\right)=1-\mathrm{P}(\mathrm{B})=1-\frac{4}{52}=1-\frac{1}{13}=\frac{12}{13}$
(iii) Let C denote the event 'card drawn is black card'

Therefore, number of elements in the set $\mathrm{C}=26$
i.e. $\mathrm{P}(\mathrm{C})=\frac{26}{52}=\frac{1}{2}$

Thus, probability of a black $\operatorname{card}=\frac{1}{2}$.
(iv) We assumed in (i) above that A is the event 'card drawn is a diamond', so the event 'card drawn is not a diamond' may be denoted as A' or 'not A'
Now $\mathrm{P}(\operatorname{not} \mathrm{A})=1-\mathrm{P}(\mathrm{A})=1-\frac{1}{4}=\frac{3}{4}$
(v) The event 'card drawn is not a black card' may be denoted as C ' or 'not C '.

We know that $\mathrm{P}($ not C$)=1-\mathrm{P}(\mathrm{C})=1-\frac{1}{2}=\frac{1}{2}$
Therefore, probability of not a black $\operatorname{card}=\frac{1}{2}$
Example 6 A bag contains 9 discs of which 4 are red, 3 are blue and 2 are yellow. The discs are similar in shape and size. A disc is drawn at random from the bag. Calculate the probability that it will be (i) red, (ii) yellow, (iii) blue, (iv) not blue, (v) either red or blue.

Solution There are 9 discs in all so the total number of possible outcomes is 9 .
Let the events $\mathrm{A}, \mathrm{B}, \mathrm{C}$ be defined as
A: 'the disc drawn is red'
B: 'the disc drawn is yellow'
C: 'the disc drawn is blue'.
(i) The number of red discs $=4$, i.e., $n(\mathrm{~A})=4$

Hence

$$
P(A)=\frac{4}{9}
$$

(ii) The number of yellow discs $=2$, i.e., $n(\mathrm{~B})=2$

Therefore, $\quad \mathrm{P}(\mathrm{B})=\frac{2}{9}$
(iii) The number of blue discs $=3$, i.e., $n(\mathrm{C})=3$

Therefore, $\quad \mathrm{P}(\mathrm{C})=\frac{3}{9}=\frac{1}{3}$
(iv) Clearly the event 'not blue' is 'not C '. We know that $\mathrm{P}($ not C$)=1-\mathrm{P}(\mathrm{C})$

Therefore

$$
\mathrm{P}(\operatorname{not} \mathrm{C})=1-\frac{1}{3}=\frac{2}{3}
$$

(v) The event 'either red or blue' may be described by the set 'A or C'

Since, A and C are mutually exclusive events, we have

$$
\mathrm{P}(\mathrm{~A} \text { or } \mathrm{C})=\mathrm{P}(\mathrm{~A} \cup \mathrm{C})=\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{C})=\frac{4}{9}+\frac{1}{3}=\frac{7}{9}
$$

Example 7 Two students Anil and Ashima appeared in an examination. The probability that Anil will qualify the examination is 0.05 and that Ashima will qualify the examination is 0.10 . The probability that both will qualify the examination is 0.02 . Find the probability that
(a) Both Anil and Ashima will not qualify the examination.
(b) Atleast one of them will not qualify the examination and
(c) Only one of them will qualify the examination.

Solution Let E and F denote the events that Anil and Ashima will qualify the examination, respectively. Given that

$$
\mathrm{P}(\mathrm{E})=0.05, \mathrm{P}(\mathrm{~F})=0.10 \text { and } \mathrm{P}(\mathrm{E} \cap \mathrm{~F})=0.02
$$

Then
(a) The event 'both Anil and Ashima will not qualify the examination' may be expressed as $\mathrm{E}^{\prime} \cap \mathrm{F}^{\prime}$.
Since, $E$ ' is 'not $E$ ', i.e., Anil will not qualify the examination and $F$ ' is 'not $F$ ', i.e., Ashima will not qualify the examination.
Also $\quad \mathrm{E}^{\prime} \cap \mathrm{F}^{\prime}=(\mathrm{E} \cup \mathrm{F})^{\prime}$ (by Demorgan's Law)
Now $\quad \mathrm{P}(\mathrm{E} \cup \mathrm{F})=\mathrm{P}(\mathrm{E})+\mathrm{P}(\mathrm{F})-\mathrm{P}(\mathrm{E} \cap \mathrm{F})$
or $\quad \mathrm{P}(\mathrm{E} \cup \mathrm{F})=0.05+0.10-0.02=0.13$
Therefore $\mathrm{P}\left(\mathrm{E}^{\prime} \cap \mathrm{F}^{\prime}\right)=\mathrm{P}(\mathrm{E} \cup \mathrm{F})^{\prime}=1-\mathrm{P}(\mathrm{E} \cup \mathrm{F})=1-0.13=0.87$
(b) $\quad \mathrm{P}$ (atleast one of them will not qualify)
$=1-\mathrm{P}$ (both of them will qualify)
$=1-0.02=0.98$
(c) The event only one of them will qualify the examination is same as the event either (Anil will qualify, and Ashima will not qualify) or (Anil will not qualify and Ashima
will qualify) i.e., $\mathrm{E} \cap \mathrm{F}^{\prime}$ or $\mathrm{E}^{\prime} \cap \mathrm{F}$, where $\mathrm{E} \cap \mathrm{F}^{\prime}$ and $\mathrm{E}^{\prime} \cap \mathrm{F}$ are mutually exclusive. Therefore, P (only one of them will qualify) $\quad=\mathrm{P}\left(\mathrm{E} \cap \mathrm{F}^{\prime}\right.$ or $\left.\mathrm{E}^{\prime} \cap \mathrm{F}\right)$

$$
\begin{aligned}
& =\mathrm{P}\left(\mathrm{E} \cap \mathrm{~F}^{\prime}\right)+\mathrm{P}\left(\mathrm{E}^{\prime} \cap \mathrm{F}\right)=\mathrm{P}(\mathrm{E})-\mathrm{P}(\mathrm{E} \cap \mathrm{~F})+\mathrm{P}(\mathrm{~F})-\mathrm{P}(\mathrm{E} \cap \mathrm{~F}) \\
& =0.05-0.02+0.10-0.02=0.11
\end{aligned}
$$

Example 8 A committee of two persons is selected from two men and two women. What is the probability that the committee will have (a) no man? (b) one man? (c) two men?

Solution The total number of persons $=2+2=4$. Out of these four person, two can be selected in ${ }^{4} \mathrm{C}_{2}$ ways.
(a) No men in the committee of two means there will be two women in the committee. Out of two women, two can be selected in ${ }^{2} \mathrm{C}_{2}=1$ way.

Therefore $\quad \mathrm{P}($ no man $)=\frac{{ }^{2} \mathrm{C}_{2}}{{ }^{4} \mathrm{C}_{2}}=\frac{1 \times 2 \times 1}{4 \times 3}=\frac{1}{6}$
(b) One man in the committee means that there is one woman. One man out of 2 can be selected in ${ }^{2} \mathrm{C}_{1}$ ways and one woman out of 2 can be selected in ${ }^{2} \mathrm{C}_{1}$ ways. Together they can be selected in ${ }^{2} \mathrm{C}_{1} \times{ }^{2} \mathrm{C}_{1}$ ways.
Therefore $\quad \mathrm{P}($ One man $)=\frac{{ }^{2} \mathrm{C}_{1} \times{ }^{2} \mathrm{C}_{1}}{{ }^{4} \mathrm{C}_{2}}=\frac{2 \times 2}{2 \times 3}=\frac{2}{3}$
(c) Two men can be selected in ${ }^{2} \mathrm{C}_{2}$ way.

Hence $\quad \mathrm{P}$ (Two men) $=\frac{{ }^{2} \mathrm{C}_{2}}{{ }^{4} \mathrm{C}_{2}}=\frac{1}{{ }^{4} \mathrm{C}_{2}}=\frac{1}{6}$

## EXERCISE 14.2

1. Which of the following can not be valid assignment of probabilities for outcomes of sample Space $S=\left\{\omega_{1}, \omega_{2}, \omega_{3}, \omega_{4}, \omega_{5}, \omega_{6}, \omega_{7}\right\}$

| Assignment | $\omega_{1}$ | $\omega_{2}$ | $\omega_{3}$ | $\omega_{4}$ | $\omega_{5}$ | $\omega_{6}$ | $\omega_{7}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (a) | 0.1 | 0.01 | 0.05 | 0.03 | 0.01 | 0.2 | 0.6 |
| (b) | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{1}{7}$ |
| (c) | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 |
| (d) | -0.1 | 0.2 | 0.3 | 0.4 | -0.2 | 0.1 | 0.3 |
| (e) | $\frac{1}{14}$ | $\frac{2}{14}$ | $\frac{3}{14}$ | $\frac{4}{14}$ | $\frac{5}{14}$ | $\frac{6}{14}$ | $\frac{15}{14}$ |

2. A coin is tossed twice, what is the probability that atleast one tail occurs?
3. A die is thrown, find the probability of following events:
(i) A prime number will appear,
(ii) A number greater than or equal to 3 will appear,
(iii) A number less than or equal to one will appear,
(iv) A number more than 6 will appear,
(v) A number less than 6 will appear.
4. A card is selected from a pack of 52 cards.
(a) How many points are there in the sample space?
(b) Calculate the probability that the card is an ace of spades.
(c) Calculate the probability that the card is (i) an ace (ii) black card.
5. A fair coin with 1 marked on one face and 6 on the other and a fair die are both tossed. find the probability that the sum of numbers that turn up is (i) 3 (ii) 12
6. There are four men and six women on the city council. If one council member is selected for a committee at random, how likely is it that it is a woman?
7. A fair coin is tossed four times, and a person win Re 1 for each head and lose Rs 1.50 for each tail that turns up.
From the sample space calculate how many different amounts of money you can have after four tosses and the probability of having each of these amounts.
8. Three coins are tossed once. Find the probability of getting
(i) 3 heads
(ii) 2 heads
(iii) atleast 2 heads
(iv) atmost 2 heads
(v) no head
(vi) 3 tails
(vii) exactly two tails
(viii) no tail
(ix) atmost two tails
9. If $\frac{2}{11}$ is the probability of an event, what is the probability of the event 'not A '.
10. A letter is chosen at random from the word 'ASSASSINATION'. Find the probability that letter is (i) a vowel (ii) a consonant
11. In a lottery, a person choses six different natural numbers at random from 1 to 20 , and if these six numbers match with the six numbers already fixed by the lottery committee, he wins the prize. What is the probability of winning the prize in the game? [Hint order of the numbers is not important.]
12. Check whether the following probabilities $\mathrm{P}(\mathrm{A})$ and $\mathrm{P}(\mathrm{B})$ are consistently defined
(i) $\mathrm{P}(\mathrm{A})=0.5, \mathrm{P}(\mathrm{B})=0.7, \mathrm{P}(\mathrm{A} \cap \mathrm{B})=0.6$
(ii) $\mathrm{P}(\mathrm{A})=0.5, \mathrm{P}(\mathrm{B})=0.4, \mathrm{P}(\mathrm{A} \cup \mathrm{B})=0.8$
13. Fill in the blanks in following table:

|  | $\mathbf{P}(\mathbf{A})$ | $\mathbf{P}(\mathbf{B})$ | $\mathbf{P}(\mathbf{A} \cap \mathbf{B})$ | $\mathbf{P}(\mathbf{A} \cup \mathbf{B})$ |
| :---: | :---: | :---: | :---: | :---: |
| (i) | $\frac{1}{3}$ | $\frac{1}{5}$ | $\frac{1}{15}$ | $\ldots$ |
| (ii) | 0.35 | $\ldots$ | 0.25 | 0.6 |
| (iii) | 0.5 | 0.35 | $\ldots$ | 0.7 |

14. Given $\mathrm{P}(\mathrm{A})=\frac{3}{5}$ and $\mathrm{P}(\mathrm{B})=\frac{1}{5}$. Find $\mathrm{P}(\mathrm{A}$ or B$)$, if A and B are mutually exclusive events.
15. If E and F are events such that $\mathrm{P}(\mathrm{E})=\frac{1}{4}, \mathrm{P}(\mathrm{F})=\frac{1}{2}$ and $\mathrm{P}(\mathrm{E}$ and F$)=\frac{1}{8}$, find (i) $\mathrm{P}(\mathrm{E}$ or F$)$, (ii) $\mathrm{P}(\operatorname{not} \mathrm{E}$ and not F$)$.
16. Events E and F are such that P (not E or not F$)=0.25$, State whether E and F are mutually exclusive.
17. A and B are events such that $\mathrm{P}(\mathrm{A})=0.42, \mathrm{P}(\mathrm{B})=0.48$ and $\mathrm{P}(\mathrm{A}$ and B$)=0.16$. Determine (i) $\mathrm{P}(\operatorname{not} \mathrm{A})$, (ii) $\mathrm{P}(\operatorname{not} \mathrm{B})$ and (iii) $\mathrm{P}(\mathrm{A}$ or B$)$
18. In Class XI of a school $40 \%$ of the students study Mathematics and $30 \%$ study Biology. $10 \%$ of the class study both Mathematics and Biology. If a student is selected at random from the class, find the probability that he will be studying Mathematics or Biology.
19. In an entrance test that is graded on the basis of two examinations, the probability of a randomly chosen student passing the first examination is 0.8 and the probability of passing the second examination is 0.7 . The probability of passing atleast one of them is 0.95 . What is the probability of passing both?
20. The probability that a student will pass the final examination in both English and Hindi is 0.5 and the probability of passing neither is 0.1 . If the probability of passing the English examination is 0.75 , what is the probability of passing the Hindi examination?
21. In a class of 60 students, 30 opted for NCC, 32 opted for NSS and 24 opted for both NCC and NSS. If one of these students is selected at random, find the probability that
(i) The student opted for NCC or NSS.
(ii) The student has opted neither NCC nor NSS.
(iii) The student has opted NSS but not NCC.

## Miscellaneous Examples

Example 9 On her vacations Veena visits four cities (A, B, C and D) in a random order. What is the probability that she visits
(i) A before B ?
(ii) $\quad \mathrm{A}$ before B and B before C ?
(iii) A first and B last?
(iv) A either first or second?
(v) A just before B?

Solution The number of arrangements (orders) in which Veena can visit four cities A, $\mathrm{B}, \mathrm{C}$, or D is 4 ! i.e., 24.Therefore, $n(\mathrm{~S})=24$.
Since the number of elements in the sample space of the experiment is 24 all of these outcomes are considered to be equally likely. A sample space for the experiment is

$$
\begin{aligned}
\mathrm{S}= & \{\mathrm{ABCD}, \mathrm{ABDC}, \mathrm{ACBD}, \mathrm{ACDB}, \mathrm{ADBC}, \mathrm{ADCB} \\
& \mathrm{BACD}, \mathrm{BADC}, \mathrm{BDAC}, \mathrm{BDCA}, \mathrm{BCAD}, \mathrm{BCDA} \\
& \mathrm{CABD}, \mathrm{CADB}, \mathrm{CBDA}, \mathrm{CBAD}, \mathrm{CDAB}, \mathrm{CDBA} \\
& \mathrm{DABC}, \mathrm{DACB}, \mathrm{DBCA}, \mathrm{DBAC}, \mathrm{DCAB}, \mathrm{DCBA}\}
\end{aligned}
$$

(i) Let the event 'she visits A before B ' be denoted by E

Therefore, $\mathrm{E}=\{\mathrm{ABCD}, \mathrm{CABD}, \mathrm{DABC}, \mathrm{ABDC}, \mathrm{CADB}, \mathrm{DACB}$ $\mathrm{ACBD}, \mathrm{ACDB}, \mathrm{ADBC}, \mathrm{CDAB}, \mathrm{DCAB}, \mathrm{ADCB}\}$

Thus

$$
\mathrm{P}(\mathrm{E})=\frac{n(\mathrm{E})}{n(\mathrm{~S})}=\frac{12}{24}=\frac{1}{2}
$$

(ii) Let the event 'Veena visits A before B and B before C ' be denoted by F .

Here $\quad \mathrm{F}=\{\mathrm{ABCD}, \mathrm{DABC}, \mathrm{ABDC}, \mathrm{ADBC}\}$
Therefore, $\mathrm{P}(\mathrm{F})=\frac{n(\mathrm{~F})}{n(\mathrm{~S})}=\frac{4}{24}=\frac{1}{6}$
Students are advised to find the probability in case of (iii), (iv) and (v).

Example 10 Find the probability that when a hand of 7 cards is drawn from a well shuffled deck of 52 cards, it contains (i) all Kings (ii) 3 Kings (iii) atleast 3 Kings.

Solution Total number of possible hands $={ }^{52} \mathrm{C}_{7}$
(i) Number of hands with 4 Kings $={ }^{4} \mathrm{C}_{4} \times{ }^{48} \mathrm{C}_{3}$ (other 3 cards must be chosen from the rest 48 cards)

Hence $\quad \mathrm{P}$ (a hand will have 4 Kings) $=\frac{{ }^{4} \mathrm{C}_{4} \times{ }^{48} \mathrm{C}_{3}}{{ }^{52} \mathrm{C}_{7}}=\frac{1}{7735}$
(ii) Number of hands with 3 Kings and 4 non-King cards $={ }^{4} \mathrm{C}_{3} \times{ }^{48} \mathrm{C}_{4}$

Therefore $\quad \mathrm{P}(3$ Kings $)=\frac{{ }^{4} \mathrm{C}_{3} \times{ }^{48} \mathrm{C}_{4}}{{ }^{52} \mathrm{C}_{7}}=\frac{9}{1547}$
(iii) P (atleast 3 King) $=\mathrm{P}(3$ Kings or 4 Kings $)$

$$
\begin{aligned}
& =\mathrm{P}(3 \text { Kings })+\mathrm{P}(4 \text { Kings }) \\
& =\frac{9}{1547}+\frac{1}{7735}=\frac{46}{7735}
\end{aligned}
$$

Example 11 If $\mathrm{A}, \mathrm{B}, \mathrm{C}$ are three events associated with a random experiment, prove that

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A} \cup \mathrm{~B} \cup \mathrm{C}) & =\mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})+\mathrm{P}(\mathrm{C})-\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})-\mathrm{P}(\mathrm{~A} \cap \mathrm{C}) \\
& -\mathrm{P}(\mathrm{~B} \cap \mathrm{C})+\mathrm{P}(\mathrm{~A} \cap \mathrm{~B} \cap \mathrm{C})
\end{aligned}
$$

Solution Consider $\mathrm{E}=\mathrm{B} \cup \mathrm{C}$ so that

$$
\begin{align*}
P(A \cup B \cup C) & =P(A \cup E) \\
& =P(A)+P(E)-P(A \cap E) \tag{1}
\end{align*}
$$

Now

$$
\begin{align*}
\mathrm{P}(\mathrm{E}) & =\mathrm{P}(\mathrm{~B} \cup \mathrm{C}) \\
& =\mathrm{P}(\mathrm{~B})+\mathrm{P}(\mathrm{C})-\mathrm{P}(\mathrm{~B} \cap \mathrm{C}) \tag{2}
\end{align*}
$$

Also $\quad \mathrm{A} \cap \mathrm{E}=\mathrm{A} \cap(\mathrm{B} \cup \mathrm{C})=(\mathrm{A} \cap \mathrm{B}) \cup(\mathrm{A} \cap \mathrm{C})$ [using distribution property of intersection of sets over the union]. Thus

$$
\mathrm{P}(\mathrm{~A} \cap \mathrm{E})=\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})+\mathrm{P}(\mathrm{~A} \cap \mathrm{C})-\mathrm{P}[(\mathrm{~A} \cap \mathrm{~B}) \cap(\mathrm{A} \cap \mathrm{C})]
$$

$$
\begin{equation*}
=\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})+\mathrm{P}(\mathrm{~A} \cap \mathrm{C})-\mathrm{P}[\mathrm{~A} \cap \mathrm{~B} \cap \mathrm{C}] \tag{3}
\end{equation*}
$$

Using (2) and (3) in (1), we get

$$
\begin{aligned}
\mathrm{P}[\mathrm{~A} \cup \mathrm{~B} \cup \mathrm{C}]= & \mathrm{P}(\mathrm{~A})+\mathrm{P}(\mathrm{~B})+\mathrm{P}(\mathrm{C})-\mathrm{P}(\mathrm{~B} \cap \mathrm{C}) \\
& -\mathrm{P}(\mathrm{~A} \cap \mathrm{~B})-\mathrm{P}(\mathrm{~A} \cap \mathrm{C})+\mathrm{P}(\mathrm{~A} \cap \mathrm{~B} \cap \mathrm{C})
\end{aligned}
$$

Example 12 In a relay race there are five teams $\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}$ and E .
(a) What is the probability that $\mathrm{A}, \mathrm{B}$ and C finish first, second and third, respectively.
(b) What is the probability that $\mathrm{A}, \mathrm{B}$ and C are first three to finish (in any order) (Assume that all finishing orders are equally likely)

Solution If we consider the sample space consisting of all finishing orders in the first three places, we will have ${ }^{5} \mathrm{P}_{3}$, i.e., $\frac{5!}{(5-3)!}=5 \times 4 \times 3=60$ sample points, each with a probability of $\frac{1}{60}$.
(a) $\mathrm{A}, \mathrm{B}$ and C finish first, second and third, respectively. There is only one finishing order for this, i.e., ABC .

Thus $\mathrm{P}(\mathrm{A}, \mathrm{B}$ and C finish first, second and third respectively $)=\frac{1}{60}$.
(b) $\mathrm{A}, \mathrm{B}$ and C are the first three finishers. There will be 3 ! arrangements for $\mathrm{A}, \mathrm{B}$ and $C$. Therefore, the sample points corresponding to this event will be 3 ! in number.
So $\quad \mathrm{P}(\mathrm{A}, \mathrm{B}$ and C are first three to finish $)=\frac{3!}{60}=\frac{6}{60}=\frac{1}{10}$

## Miscellaneous Exercise on Chapter 14

1. A box contains 10 red marbles, 20 blue marbles and 30 green marbles. 5 marbles are drawn from the box, what is the probability that
(i) all will be blue? (ii) atleast one will be green?
2. 4 cards are drawn from a well - shuffled deck of 52 cards. What is the probability of obtaining 3 diamonds and one spade?
3. A die has two faces each with number ' 1 ', three faces each with number ' 2 ' and one face with number ' 3 '. If die is rolled once, determine
(i) $\mathrm{P}(2)$
(ii) $\mathrm{P}(1$ or 3$)$
(iii) $\mathrm{P}(\operatorname{not} 3)$
4. In a certain lottery 10,000 tickets are sold and ten equal prizes are awarded. What is the probability of not getting a prize if you buy (a) one ticket (b) two tickets (c) 10 tickets.
5. Out of 100 students, two sections of 40 and 60 are formed. If you and your friend are among the 100 students, what is the probability that
(a) you both enter the same section?
(b) you both enter the different sections?
6. Three letters are dictated to three persons and an envelope is addressed to each of them, the letters are inserted into the envelopes at random so that each envelope contains exactly one letter. Find the probability that at least one letter is in its proper envelope.
7. A and B are two events such that $\mathrm{P}(\mathrm{A})=0.54, \mathrm{P}(\mathrm{B})=0.69$ and $\mathrm{P}(\mathrm{A} \cap \mathrm{B})=0.35$. Find (i) $\mathrm{P}(\mathrm{A} \cup \mathrm{B})$ (ii) $\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}^{\prime}\right)$ (iii) $\mathrm{P}\left(\mathrm{A} \cap \mathrm{B}^{\prime}\right)$ (iv) $\mathrm{P}\left(\mathrm{B} \cap \mathrm{A}^{\prime}\right)$
8. From the employees of a company, 5 persons are selected to represent them in the managing committee of the company. Particulars of five persons are as follows:

| S. No. | Name | Sex | Age in years |
| :---: | :--- | :---: | :---: |
| 1. | Harish | M | 30 |
| 2. | Rohan | M | 33 |
| 3. | Sheetal | F | 46 |
| 4. | Alis | F | 28 |
| 5. | Salim | M | 41 |

A person is selected at random from this group to act as a spokesperson. What is the probability that the spokesperson will be either male or over 35 years?
9. If 4-digit numbers greater than 5,000 are randomly formed from the digits $0,1,3,5$, and 7 , what is the probability of forming a number divisible by 5 when, (i) the digits are repeated? (ii) the repetition of digits is not allowed?
10. The number lock of a suitcase has 4 wheels, each labelled with ten digits i.e., from 0 to 9 . The lock opens with a sequence of four digits with no repeats. What is the probability of a person getting the right sequence to open the suitcase?

## Summary

In this Chapter, we studied about the axiomatic approach of probability. The main features of this Chapter are as follows:

- Event: A subset of the sample space
- Impossible event : The empty set
- Sure event: The whole sample space
- Complementary event or 'not event' : The set A ' or $\mathrm{S}-\mathrm{A}$
- Event A or B: The set $\mathrm{A} \cup \mathrm{B}$
- Event A and B: The set $\mathrm{A} \cap \mathrm{B}$
- Event A and not B: The set $\mathrm{A}-\mathrm{B}$
- Mutually exclusive event: A and B are mutually exclusive if $\mathrm{A} \cap \mathrm{B}=\phi$
- Exhaustive and mutually exclusive events: Events $\mathrm{E}_{1}, \mathrm{E}_{2}, \ldots, \mathrm{E}_{n}$ are mutually exclusive and exhaustive if $\mathrm{E}_{1} \cup \mathrm{E}_{2} \cup \ldots \cup \mathrm{E}_{n}=\mathrm{S}$ and $\mathrm{E}_{i} \cap \mathrm{E}_{j}=\phi \quad \forall i \neq j$
Probability: Number $\mathrm{P}\left(\omega_{i}\right)$ associated with sample point $\omega_{i}$ such that
(i) $0 \leq \mathrm{P}\left(\omega_{i}\right) \leq 1$
(ii) $\sum \mathrm{P}\left(\omega_{i}\right)$ for all $\omega_{i} \in \mathrm{~S}=1$
(iii) $\mathrm{P}(\mathrm{A})=\sum \mathrm{P}\left(\omega_{i}\right)$ for all $\omega_{i} \in \mathrm{~A}$. The number $\mathrm{P}\left(\omega_{i}\right)$ is called probability of the outcome $\omega_{i}$.
Equally likely outcomes: All outcomes with equal probability
- Probability of an event: For a finite sample space with equally likely outcomes Probability of an event $\mathrm{P}(\mathrm{A})=\frac{n(\mathrm{~A})}{n(\mathrm{~S})}$, where $n(\mathrm{~A})=$ number of elements in the set $\mathrm{A}, n(\mathrm{~S})=$ number of elements in the set S .
- If A and B are any two events, then

$$
\begin{aligned}
& P(A \text { or } B)=P(A)+P(B)-P(A \text { and } B) \\
& \text { equivalently, } P(A \cup B)=P(A)+P(B)-P(A \cap B)
\end{aligned}
$$

- If A and B are mutually exclusive, then $\mathrm{P}(\mathrm{A}$ or B$)=\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})$
- If A is any event, then

$$
\mathrm{P}(\operatorname{not} \mathrm{~A})=1-\mathrm{P}(\mathrm{~A})
$$

## Historical Note

Probability theory like many other branches of mathematics, evolved out of practical consideration. It had its origin in the 16th century when an Italian physician and mathematician Jerome Cardan (1501-1576) wrote the first book on the subject "Book on Games of Chance" (Biber de Ludo Aleae). It was published in 1663 after his death.

In 1654, a gambler Chevalier de Metre approached the well known French Philosopher and Mathematician Blaise Pascal (1623-1662) for certain dice problem. Pascal became interested in these problems and discussed with famous French Mathematician Pierre de Fermat (1601-1665). Both Pascal and Fermat solved the problem independently. Besides, Pascal and Fermat, outstanding contributions to probability theory were also made by Christian Huygenes (16291665), a Dutchman, J. Bernoulli (1654-1705), De Moivre (1667-1754), a Frenchman Pierre Laplace (1749-1827), the Russian P.L Chebyshev (18211897), A. A Markov (1856-1922) and A. N Kolmogorove (1903-1987). Kolmogorov is credited with the axiomatic theory of probability. His book 'Foundations of Probability' published in 1933, introduces probability as a set function and is considered a classic.


[^0]:    Definition Any subset E of a sample space S is called an event.

