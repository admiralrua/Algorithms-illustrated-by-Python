# \_notyet\_ Statistics


## Briefing 
[Statistics](https://en.wikipedia.org/wiki/Statistics) is the discipline that concerns the collection, organization, displaying, analysis, interpretation and presentation of data.

Two main statistical methods are used in data analysis: **descriptive statistics**, which summarize data from a sample using indexes such as the mean or standard deviation, and **inferential statistics**, which draw conclusions from data that are subject to random variation (e.g., observational errors, sampling variation). Recently, **exploratory data analysis** analyzing data sets to summarize their main characteristics (often with visual methods) also becomes popular. 

This section will give a quick introduction to the basis of statistics. The section is heavily based on the following comprehensive references:

- [wiki](https://en.wikipedia.org/wiki/Statistics)
- [The elements of statistical learning](https://www.amazon.com/Elements-Statistical-Learning-Prediction-Statistics/dp/0387848576) [or here](https://web.stanford.edu/~hastie/ElemStatLearn/)


## Statistical data
### Data preparation
The process of data preparation includes several works:

- **data collection** by experimental study or observational study
- **data summarising** (aka descriptive statistics) is considered as a problem of defining what aspects of statistical samples need to be described and how well they can be described from a typically limited sample of data; this work includes:
  + choosing summary statistics to describe a sample
  + summarising probability distributions of sample data 
  + summarising the relationships between different quantities measured on the same items 
- **data interpreting** (aka inferential statistics) finds the philosophy underlying statistical inference by using different data analytic techniques; this work includes:
  + summarising populations in the form of a fitted distribution or probability density function
  + summarising the relationship between variables using some type of regression analysis
  + providing ways of predicting the outcome of a random quantity given other related variables
  + examining the possibility of reducing the number of variables being considered within a problem (the task of Dimension Reduction Analysis)


### Data types
In statistics, groups of individual data points may be classified as belonging to any of various [statistical data types](https://en.wikipedia.org/wiki/Statistical_data_type). In the most general form, there are two types of data/variables:

- **categorical** variables: variables conform only to nominal or ordinal measurements which cannot be reasonably measured numerically; and
- **quantitative** variables: variables conform ratio and interval measurements which have numerical nature, either discrete or continuous.

[Level of measurement](https://en.wikipedia.org/wiki/Level_of_measurement)

| Incremental progress | Measure property | Mathematical operators | Central tendency |
| ---                  | ---              | ---                    | ---              |
| Nominal  | Classification, membership   | =, \><   | Mode            |  
| Ordinal  | Comparison, level            | \>, <    | Median          |
| Interval | Difference, affinity         | \+, \-   | Mean, deviation |
| Ratio    | Magnitude, amount            | \*, /    | Geometric mean, coefficient of variation |

Examples of simple data types:

| Data type                  | Possible values        | Example usage  | Level of measurement |
| ---                        | ---                    | ---            | ---                  |
| Binary                     | 0, 1                   | binary outcome | nominal              |
| Categorical                | 1, 2,... , n           | categorical outcome | nominal |
| Ordinal                    | integer or real number | relative score      | ordinal |
| Binomial                   | 0, 1,..., $$n$$        | number of success out of $$n$$ possibility | interval |
| Count                      | non-negative integer   | number of items in given interval/area/volume | ratio |
| Real-valued additive       | real number            | anything not varying over a large scale (temperature, relative distance...) | interval |
| Real-valued multiplicative | positive real number   | anything varying over a large scale (price, income, size...)  | ratio    |

Examples of multivariate data types:

- random vectors
- random matrices
- random sequences
- random processes
- random fields
- [Bayes networks](https://en.wikipedia.org/wiki/Bayesian_network) i.e. multilevel models or random trees


## Descriptive statistics
A descriptive statistic is a summary statistic that quantitatively describes or summarizes features of a data set. Descriptive statistics is distinguished from inferential statistics in that descriptive statistics aims to summarize a sample, rather than use the data to learn about the population that the sample of data is thought to represent. Numerical descriptors include mean and standard deviation for continuous data types, while frequency and percentage are more useful in terms of describing categorical data. The drawing of the sample has been subject to an element of randomness, hence the established numerical descriptors from the sample are also due to uncertainty. 

Numerical descriptors in descriptive statistics can be listed as:

| Property type | Descriptors |
| ---           | ---         |
| Center        | **Mean**, **Median**, **Mode**, **Mid-range** |
| Despersion    | **Variance**, **Standard deviation**, **Coefficient of variation**, **Percentile**, **Range/Interquartile range** |


### Mean
Mean is also called the expected value of a data set. There are several kinds of means in statistics. Let's consider a set of numbers $$x_1, x_2,... , x_n$$.

**Pythagorean means** include three classical means

| Pythagorean means | Formulation |
| ---               | ---         |
| Arithmetic        | $$ \overline{x}_A = \frac{x_1 + x_2 + ... + x_n}{n} = \sum_{i=1}^n x_i $$ |
| Geometric         | $$ \overline{x}_G = (x_1 x_2 ... x_n)^\frac{1}{n} = \left( \prod_{i=1}^n x_i \right )^\frac{1}{n} $$ |
| Harmonic          | $$ \overline{x}_H = n \left( \sum_{i=1}^n \frac{1}{x_i} \right )^{-1} $$ |

In general, $$ \overline{x}_A \ge \overline{x}_G \ge \overline{x}_H $$.

**The generalized mean**, also known as the power mean, is an abstraction of the quadratic, arithmetic, geometric and harmonic means as follows:

$$ \overline{x} = \left( \frac{1}{n} \sum_{i=1}^n x_i^m \right )^\frac{1}{m} $$

By choosing different values for the parameter $$m$$, the following types of means are obtained:

| $$m$$ | Type of means |
| ---   | ---           |
| $$ m \rightarrow \infty $$  | maximum of $$x_i$$ |
| $$ m = 2 $$                 | quadratic mean     |
| $$ m = 1 $$                 | arithmetic mean    |
| $$ m \rightarrow 0 $$       | geometric mean     |
| $$ m = -1 $$                | harmonic mean      |
| $$ m \rightarrow -\infty $$ | minimum of $$x_i$$ |


**Weighted arithmetic mean**
The weighted arithmetic mean (or weighted average) is useful if one wants to combine average values from samples of the same population with different sample sizes:

$$ \overline{x} = \frac{\sum_{i=1}^n w_i x_i}{\sum_{i=1}^n w_i} $$

The **truncated mean** is the arithmetic mean of data values after a certain number or proportion of the highest and lowest data values have been discarded.

### Median / Mode / Mid-range
The **median** is the middle value that separates the higher half from the lower half of the data set.

The most frequently occurring values in a data set is called the **mode**.

The **mid-range** of a set of statistical data values is the arithmetic mean of the maximum and minimum values in a data set:

$$ M = \frac{\max(x_i) + \min(x_i)}{2} $$


### Variance

### Standard deviation

### Coefficient of variation

### Percentile

### Range/Interquartile range


## Inferential statistics
Statistical inference is the process of using data analysis to deduce properties of an underlying probability distribution. Inferential statistical analysis infers properties of a population. It is assumed that the observed data set is sampled from a larger population. It uses patterns in the sample data to draw inferences about the population represented, accounting for randomness. These inferences may take the form of: answering yes/no questions about the data (hypothesis testing), estimating numerical characteristics of the data (estimation), describing associations within the data (correlation) and modeling relationships within the data (for example, using regression analysis). Inference can extend to forecasting, prediction and estimation of unobserved values either in or associated with the population being studied; it can include extrapolation and interpolation of time series or spatial data, and can also include data mining.

### Statistics, estimators and pivotal quantities

### Null hypothesis and alternative hypothesis

### Error

### Interval estimation

### Significance

### Examples
Some well-known statistical tests and procedures are:

- Regression analysis
- Time series analysis 
- Chi-squared test
- Correlation and dependence

## Exploratory data analysis
Exploratory data analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. A statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task. A very nice example of EDA can be found [here](https://en.wikipedia.org/wiki/Exploratory_data_analysis).
