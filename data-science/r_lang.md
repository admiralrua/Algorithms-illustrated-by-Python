# Basic of R

## Briefing
This section gives a brief introduction into R-language. 

Numeric variables

```r
x <- 4
y <- 5
z <- x + y
```

Character variables

```r
a <- "hello"
b <- "world"
c <- paste(a, b, sep = " ")                  # this is a function to concate two strings
```

Vecter and slicing

```r
x <- c(2, 5, 1, 7, 8)
x[2]
x[2:4]
x[2:length(x)]
x[c(2,4)]                                    # direct slicing
index <- c(2,4)                              # indirect slicing
x[index]
x[x >= 5]                                    # conditional slicing
x[(x >= 5) & (x %% 2 == 0)]
y <- x >= 5                                  # y is a logical variable                    
x[y]
seq(1, 100, 2)                               # different ways to define a sequence
seq(1, 10, length.out = 101)
seq(0,10000000, length.out = 6)
rep(5,20)
rep(c("Q1", "Q2", "Q3", "Q4"), 10)
rep(c("Q1", "Q2", "Q3", "Q4"), each = 10)
```
