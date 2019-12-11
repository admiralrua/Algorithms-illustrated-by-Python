# Bit manipulation

\(To be continued\)

## Theory

Let illustrate the bitwise operation by [examples](https://www.tutorialspoint.com/python/bitwise_operators_example.htm). Assume that $$a = 60 = 00111100$$ and $$b = 13 = 00001101$$. The following bitwise operators are supported by Python language.

| Operator | Description | Example | Output |
| :--- | :--- | :--- | :--- |
|  | Input | $$a$$ | 60 = 00111100 |
|  |  | $$b$$ | 13 = 00001101 |
| & | AND: copies a bit to the result if it exists in both operands. | $$a \& b$$ | 12 = 00001100 |
| \| | OR: copies a bit if it exists in either operand. | $$a \| b$$ | 61 = 00111101 |
| ^ | XOR: copies the bit if it is set in one operand but not both. | $$a \^ b$$ | 49 = 00110001 |
| ~ | Complement: provide the flipping-bit function. | $$\~a$$ | -61 = 11000011 |
| &lt;&lt; | Left\_shift: value is moved left by the number of bits specified by the right operand. | $$a << 2$$ | 240 = 11110000 |
| &gt;&gt; | Right\_shift: value is moved right by the number of bits specified by the right operand. | $$a >> 2$$ | 15 = 00001111 |

## Problems to practice

