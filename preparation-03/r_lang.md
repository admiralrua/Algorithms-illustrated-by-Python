# \[B\] Briefing on R

## Briefing

This section gives a brief introduction into R-language.

## Basic data types and structures in R

### Data types

Everything in R is an object. R has 6 basic data types:

| Type | Examples |
| :--- | :--- |
| character | "a", "swc" |
| numeric \(real or decimal\) | 2, 15.5 |
| integer | 2L |
| logical | TRUE, FALSE |
| complex | 1+4i |
| raw | _not yet_ |

R provides many functions to examine features of vectors and other objects, for example

* class\(\): what kind of object is it \(high-level\)
* typeof\(\): what is the object’s data type \(low-level\)
* length\(\): how long is it? What about two dimensional objects
* attributes\(\): does it have any metadata

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

### Data structures

Vector and slicing

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

### Working with dataframe

Dataframe in R stores data in a row-oriented which means each row represents an object, each column represents a property of an object.

#### Typer conversion

#### Making querry

#### Data extraction/manipulation

#### Filtering - aggregation

#### Merging data from different sources

~ join in SQL or vlookup in Excel

