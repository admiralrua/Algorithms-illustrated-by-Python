# \_notyet\_ Calculus

## Differential calculus

### Briefing

[Differential calculus](https://en.wikipedia.org/wiki/Differential_calculus) is a subfield of calculus concerned with the study of the rates at which quantities change. The primary objects of study in differential calculus are the derivative of a function, the derivative of a function at a chosen input value describes the rate of change of the function near that input value. The process of finding a derivative is called differentiation.

Suppose that $$x$$ and $$y$$ are real numbers and that $$y$$ is a function of $$x$$ meaning for every value of $$x$$, there is a corresponding value of $$y$$. This relationship can be written as $$y = f(x)$$. Geometrically, the derivative of $$f$$ at the point $$x = a$$, if $$f$$ is a differentiable at $$a$$, is the slope of the tangent line to the function $$f$$ at the point $$a$$ denoted $$f'(a)$$.

$$f'(a) = \left. \frac{df}{dx} \right |_{x = a}$$

**Reserved for a figure**.

Since the derivative is the slope of the linear approximation to $$f$$ at the point $$a$$, the derivative \(together with the value of $$f$$ at $$a$$\) determines the best linear approximation, or [linearization](https://en.wikipedia.org/wiki/Linearization), of $$f$$ near the point $$a$$. The linear approximation of a function is the first order Taylor expansion, which will be described later, around the point of interest.

### Basic derivative rules

Numerous basic derivative rules can be found [here](https://en.wikipedia.org/wiki/Differentiation_rules). Some of them are presented below:

| Rules | Meaning |
| :--- | :--- |
| Constant | $$\frac{d}{dx}(c) = 0$$ |
| Power | $$\frac{d}{dx}(x^n) = n \times x^{n-1}$$ |
|  | $$\frac{d}{dx} \left( f(x)^{g(x)} \right ) = f(x)^{g(x)} \left( f'(x) \frac{g(x)}{f(x)} + g'(x) \cdot \ln f(x) \right )$$ |
| Sum/Diff. | $$\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$$ |
| Product | $$\frac{d}{dx}[f(x) g(x)] = f'(x) \times g(x) + f(x) \times g'(x)$$ |
| Quotient | $$\frac{d}{dx} \left [ \frac{f(x)}{g(x)} \right ] = \frac{f'(x) \times g(x) - f(x) \times g'(x)}{[g(x)]^2}$$ |
| Chain | $$\frac{d}{dx} f(g(x)) = f'(g(x)) \times g'(x))$$ |
| Exponential | $$\frac{d}{dx} \left( a^{x} \right ) = \ln(a) \cdot a^{x}$$ |
|  | $$\frac{d}{dx} \left( a^{g(x)} \right ) = \ln(a) \cdot a^{g(x)} \cdot g'(x)$$ |
| Logarithmic | $$\frac{d}{dx} \left( \log_a x \right ) = \frac{1}{x \ln a}$$ |
|  | $$\frac{d}{dx} \left( \log_a g(x) \right ) = \frac{g'(x)}{g(x) \ln a}$$ |

### Problems for practice

Compute the derivaties of the following [activation functions](https://en.wikipedia.org/wiki/Activation_function):

| Name | Function |
| :--- | :--- |
| Identity | $$f(x) = x$$ |
| Logistic | $$f(x) = \frac{1}{1+e^{-x}}$$ |
| Arctan | $$f(x) = \frac{1}{\tan{x}}$$ |
| Tanh | $$f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$ |
| Soft-Plus | $$f(x) = \log_e(1+e^x)$$ |
| Rectified Linear Unit \(ReLU\) | $$f(x) = \left \{ \begin{matrix} 0 & \text{for} & x < 0 \\ x & \text{for} & x \ge 0 \end{matrix} \right .$$ |
| Parametric Rectified Linear Unit \(PReLU\) | $$f(x) = \left \{ \begin{matrix} \alpha x & \text{for} & x < 0 \\ x & \text{for} & x \ge 0 \end{matrix} \right .$$ |
| Exponential Rectified Linear Unit \(ELU\) | $$f(x) = \left \{ \begin{matrix} \alpha (e^x - 1) & \text{for} & x < 0 \\ x & \text{for} & x \ge 0 \end{matrix} \right .$$ |

### Numerical differentiation

Numerical differentiation will be described in [the next section](numerical-methods.md)

## Integration

[wiki](https://en.wikipedia.org/wiki/Integral)

## Vector calculus

[wiki](https://en.wikipedia.org/wiki/Vector_calculus)

## Multivariate calculus

[wiki](https://en.wikipedia.org/wiki/Multivariable_calculus)

## Taylor series

### Briefing

[A Taylor series](https://en.wikipedia.org/wiki/Taylor_series) is a representation of a function as an infinite sum of terms that are calculated from the values of the function's derivatives at a single point. Consequently, a function can be approximated by using a finite number of terms of its Taylor series.

The Taylor series of a function $$f(x)$$ that is infinitely differentiable at a point $$x = a$$ is the power series:

$$f(x) = f(a) + \frac{f^{(1)}(a)}{1!}(x-a) + \frac{f^{(2)}(a)}{2!}(x-a)^2 + ... = \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n$$

It is straight forward that we can derive the Taylor-series form of a function if we know the derivatives of that function. The following example illustrate how to do so by finding the Taylor-series form of function $$f = \sin(x)$$.

Firstly, we know that as $$f(x) = \sin(x), f^{(1)}(x) = \cos(x), f^{(2)}(x) = -\sin(x), f^{(3)}(x) = -\cos(x)...$$ so we get:

$$\sin(x) = \sin(a) + \frac{\cos(x)}{1!}(x-a) - \frac{\sin(x)}{2!}(x-a)^2 - \frac{\cos(x)}{3!}(x-a)^3 + ...$$

Now, put $$a = 0$$ leading to $$sin(0) = 0$$ and $$cos(0) = 1$$, we have:

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - ... = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1}$$

Another example of finding the Taylor series for $$f(x) = e^{-x}$$ at point $$x = -3$$. Firstly, we can easily derive $$f^{(n)}(x) = (-1)^n e^{-x}$$, hence $$f^{(n)}(-3) = (-1)^n e^{3}$$. Finally:

$$e^{-x} = \sum_{n = 0}^{\infty} \frac{(-1)^n e^3}{n!}(x+3)^n$$

From the two examples above, you can see that one of the application of the Taylor series is to approximate a function at a given point. Although the two example above are rather trivial, you may have to use the Taylor series in Machine Learning because, sometimes, the cost function optimisation can be rather complex.

### Taylor's theorem

[Taylor's theorem](https://en.wikipedia.org/wiki/Taylor\'s_theorem) gives an approximation of a $$k$$-times differentiable function around a given point by a $$k$$-th order Taylor polynomial. The most basic version of Taylor's theorem can be written as follows:

$$f(x) = f(a) + f^{(1)}(x-a) + \frac{f^{(2)}(a)}{2!}(x-a)^2 + ... + \frac{f^{(k)}(a)}{k!}(x-a)^k + h_k(x)(x-a)^k$$

with $$\lim_{x \rightarrow a} h_k(x) = 0$$

The polynomial appearing in Taylor's theorem is the k-th order Taylor polynomial $$P_{k}(x)$$.

$$P_{k}(x) = f(a) + f^{(1)}(x-a) + \frac{f^{(2)}(a)}{2!}(x-a)^2 + ... + \frac{f^{(k)}(a)}{k!}(x-a)^k$$

The approximation error when approximating $$f(x)$$ with its Taylor polynomial is:

$$R_{k}(x) = f(x) - P_{k}(x)$$

**Example ???**

## Fourier series

