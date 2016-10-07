# Gradient Descent
We are going to learn a way to minimize the cost function J  using an algorithm called gradient descent

Used all over the place in machine learning

minimize J(x1,x2,x3)

Start with some x0 x1
keep changing x0 x1 to reduce J(x0, x1) until we find a minima
How do I walk down this hill as rapidly as possible?
Take that step and repeat

How do you decide which step will take you down hill?
How do we decide the step length?

Choosing different initial guesses can result in finding different local minima


repeat until convergence
:= => Denotes assignment Vs Truth assertion

alpha = learning rate, controls how big a step we take down hill with gradient descent

derivataive term

update thetea zero and thetat 1
for the update equation we want to simultaneously update theta o and theta 1
Solve the right side for both, then assign them.
:
temp0 = Gradientdescent(x0)
temp1 = Gradientdescent(x1)
x0=temp0
x1=temp1

NEED TO CALCULATE BOTH AT THE SAME TIME it is more natual to implement it this way.
NOnsimultaneous update works also, but isnt what people mean by gradient descent.

Next Class will explain the partial derivative term, and then I will be able to apply gradient descent

