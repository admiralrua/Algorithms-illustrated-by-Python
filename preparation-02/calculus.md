# Calculus

## Differential calculus
### Briefing
[Differential calculus](https://en.wikipedia.org/wiki/Differential_calculus) is a subfield of calculus concerned with the study of the rates at which quantities change. The primary objects of study in differential calculus are the derivative of a function, the derivative of a function at a chosen input value describes the rate of change of the function near that input value. The process of finding a derivative is called differentiation.

Suppose that $$x$$ and $$y$$ are real numbers and that $$y$$ is a function of $$x$$ meaning for every value of $$x$$, there is a corresponding value of $$y$$. This relationship can be written as $$y = f(x)$$. Geometrically, the derivative of $$f$$ at the point $$x = a$$, if $$f$$ is a differentiable at $$a$$, is the slope of the tangent line to the function $$f$$ at the point $$a$$ denoted $$f'(a)$$.

$$ f'(a) = \left. \frac{df}{dx} \right |_{x = a} $$

**Reserved for a figure**.

Since the derivative is the slope of the linear approximation to $$f$$ at the point $$a$$, the derivative (together with the value of $$f$$ at $$a$$) determines the best linear approximation, or [linearization](https://en.wikipedia.org/wiki/Linearization), of $$f$$ near the point $$a$$. The linear approximation of a function is the first order Taylor expansion, which will be described later, around the point of interest.


### Derivative rules

| Rules         | Meaning |
| ---           | ---     |
| Constant      | $$ \frac{d}{dx}(c) = 0 $$ |
| Power         | $$ \frac{d}{dx}(x^n) = n \times x^{n-1} $$ |
| Sum/Diff.     | $$ \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)   $$ |
| Product       | $$ \frac{d}{dx}[f(x) g(x)] = f'(x) \times g(x) + f(x) \times g'(x) $$ |
| Quotient      | $$ \frac{d}{dx} \left [ \frac{f(x)}{g(x)} \right ] = \frac{f'(x) \times g(x) - f(x) \times g'(x)}{[g(x)]^2} $$ |
| Chain         | $$ \frac{d}{dx} f(g(x)) = f'(g(x)) \times g'(x)) $$ |
| Exponential   | $$ \frac{d}{dx} \left( a^{x} \right ) = \ln(a) \cdot a^{x} $$ |
|               | $$ \frac{d}{dx} \left( a^{g(x)} \right ) = \ln(a) \cdot a^{g(x)} \cdot g'(x) $$ |
| Logarithmic   | $$ \frac{d}{dx} \left( \log_a x \right ) = \frac{1}{x \ln a} $$ |
|               | $$ \frac{d}{dx} \left( \log_a g(x) \right ) = \frac{g'(x)}{g(x) \ln a} $$ |


### Numerical differentiation
Numerical differentiation will be described in [the next section](numerical-methods.md)


## Integration
[wiki](https://en.wikipedia.org/wiki/Integral)



## Vector calculus
[wiki](https://en.wikipedia.org/wiki/Vector_calculus)



## Multivariate calculus
[wiki](https://en.wikipedia.org/wiki/Multivariable_calculus)



## Taylor series



## Fourier series



