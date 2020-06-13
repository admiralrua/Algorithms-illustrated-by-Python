# Some quick tips/tricks in Latex

#### How to use **alignat** properly

The important things to remember are that
- **alignat** doesn't add space between the columns;
- the columns are as many **rl** pairs as specified by the argument;
- this environment takes one argument, the number of *equation columns*: count the maximum number of **&** in any row, add 1 and and divide by 2.

So, if you want left alignment for the symbols, the descriptions, and the conditions, you should place them after a **&**, with another **&** to separate the pairs:

```latex
\begin{alignat*}{3}
    & d   = \frac{1}{1 + 0.2316419x}  \quad && a_1  = 0.31938153   \quad && a_2 = -0.356563782 \\
    & a_3 = 1.781477937               \quad && a_4  = -1.821255978 \quad && a_5 = 1.330274429
\end{alignat*}
```

By adding **\quad** we separate the columns. It wouldn't be necessary to specify them on all rows, but doing so spares to guess what is the widest entry.
