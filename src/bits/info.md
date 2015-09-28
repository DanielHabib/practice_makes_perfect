## Things to pay attention when dealing with Strings
* are the ints `signed` or `unsigned`?
* How many bits are we dealing with?

## General Takes Aways
* Unsigned Ints cannot represent negative numbers, they therefore can represet double the amount of ints over their signed counterparts
* `Bit Shifting` by k is the same as multiplying by 2^(k). Left being positive right being negative, ONLY if none of the values are being shifted out of existence.
* `^` indicates a `XOR` which is addition with carries being lost, Xor literally stands for exclusive or that implies even if both are true it is evaluated to false. Both values must be different
* The difference between or and xor
* When dealing with negative numbers in binary, (the sign bit is 1) the method of calculating becomes subtracting the given value from the resulting bits from one more than the max
* Logical(`>>`) vs Arithmetic(`>>>`)

## Mistakes
* Not sure how to get the length of a binary number in python.
