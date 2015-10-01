## Things to pay attention when dealing with Strings
* Are the ints `signed` or `unsigned`?
* How many bits are we dealing with?

## General Takes Aways
* Unsigned Ints cannot represent negative numbers, they therefore can represet double the amount of ints over their signed counterparts
* `Bit Shifting` by k is the same as multiplying by 2^(k). Left being positive right being negative, ONLY if none of the values are being shifted out of existence.
* `^` indicates a `XOR` which is addition with carries being lost, Xor literally stands for exclusive or that implies even if both are true it is evaluated to false. Both values must be different
* The difference between or and xor
* When dealing with negative numbers in binary, (the sign bit is 1) the method of calculating becomes subtracting the given value from the resulting bits from one more than the max
* Logical(`>>`) vs Arithmetic(`>>>`)
* The difference between longs and doubles. a `double` has twice the precision of a `float`. Floats tend to have 7 digits of precision, and doubles have 15-16. so for extreme precision, always go with a double
* with floating point numbers we need to normalize the mantissa, normalize means there cant be any unsignificant digits to the left of the decimal point
* Storing floats in 8 bit words goes as follows:
 * Convert Mantissa to binary
 * Normalize the mantissa
 * convert the exponent
 * place in order of 1-bit=> sign; 3-bits=>exponent;4bits=>represent `mantissa`
* Finding the value of a float can be done by multipling the value by 2 checking if it is greater than or equal to 1, if it is then we put a append a 1 to the binary value and subtract 1 from the number, otherwise we append a 0. We repeat until the value is 0 or exceeds our limit

## Mistakes
* Not sure how to get the length of a binary number in python.
