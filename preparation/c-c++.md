# \[nyf\] C/C++

This section will briefly summarise basic C++ knowledge that can be useful for the purpose of learning and practicing data structures and algorithms. The main references of this section are:

- Competitive programming 3ed
- Competitive programmer handbook 2018

More extensive reference to C++ can be found elsewhere. 


## C++ code template
A typical C++ code template looks like:

```c
#include <bits/stdc++.h>

using namespace std;

int main() {
    // solution comes here
}
```

Brief explaination for the syntax:

- `#include` allows us to include the entire standard library.
- `using namespace` declares that the classes and functions of the standard library can be used directly in the code. Without this declaration we would have to write `std::cout`.

The code can be compiled with the `g++` compiler using the following command:

```c
g++ -std=c++11 -O2 -Wall code_file_name.cpp -o app_name
```

This command produces a binary file `app_name` from the source code `code_file_name.cpp` following the C++11 standard `-std=c++11` with an optimisation `-O2` and warnings about possible errors `-Wall`.


## Input and Output
In C++, the standard streams are `cin` for input and `cout` for output. In addition, the C functions `scanf` and `printf` can be used.

The input for the program usually consists of numbers and strings that are separated with spaces and newlines. They can be conveniently read from the `cin` stream as follows:

```c
int a, b;
string x;
cin >> a >> b >> x;
```

The `cout` stream is used for output as follows (note that the newline `\n` works faster than `endl`):

```c
int a = 123, b = 456;
string x = "monkey";
cout << a << " " << b << " " << x << "\n";
```

Input and output is sometimes a bottleneck in the program. The following lines at the beginning of the code make input and output more efficient:

```c
ios::sync_with_stdio(0);
cin.tie(0);
```


The C functions `scanf` and `printf` are an alternative to the C++ standard streams. They are usually a bit faster, but they are also more difficult to use.

```c
int a, b;
scanf("%d %d", &a, &b);

int a = 123, b = 456;
printf("%d %d\n", a, b);
```

Sometimes, the program should read a whole line from the input, possibly containing spaces. This can be accomplished by using the `getline` function; and, if the amount of data is unknown, the `while loop` is useful:

```c
string s;
getline(cin, s);

while (cin >> x) {
    // code
}
```

Sometimes, it is convenient during testing to read the input from the file `input.txt` and wrtie the ouput file to the file `output.txt`. This can be done easily by including the following lines to the beginneing of the code:

```c
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
```


## Numbers `int`, `long`, `float`
### Integers
The most used integer type is `int` which is 32-bit type with a value range of $$-2^{31} \dots 2^{31}-1$$ or about $$-2*10^{9} \dots 2*10^{9}$$. If the type `int` is not enough, the 64-bit type `long long` can be used with a value range of $$-2^{63} \dots 2^{63}-1$$ or about $$-9*10^{18} \dots 9*10^{18}$$. The following code defines a long long variable (becareful to include the suffix `LL`):

```c
long long x = 135792468123456789LL
```

### Floating point numbers
The usual floating point types are the 64-bit `double` and, as an extension in the g++ compiler, the 80-bit `long double`. In most cases, `double` is enough, but `long double` is more accurate. The required precision of the answer is usually given in the problem statement. An easy way to output the answer is to use the `printf` function.

```c
double x = 0.3*3+0.1;
printf("%.20f\n", x);
```

A difficulty when using floating point numbers is that some numbers cannot be represented accurately as floating point numbers, and there will be rounding errors, therefore it is risky to compare floating point numbers with the `==` operator. A better way to compare floating point numbers is to assume that two numbers are equal if the difference between them is less a small number.

```c
if (abs(a-b) < 1e-9) {
    // a and b are equal
}
```


## Shortening code
Short code is ideal in competitive programming, hence shorter names are normally defined for datatypes and other parts of code.

### Type name
Using the command `typedef` it is possible to give a shorter name to a datatype.

```c
typedef long long ll;
long long a = 123456789;
ll b = 987654321;
cout << a*b << "\n";
```

The command `typedef` can also be used with more complex types.

```c
typedef vector<int> vi;
typedef pair<int,int> pi;
```

### Macros
Another way to shorten code is to define **macros**. A macro means that certain strings in the code will be changed before the compilation. In C++, macros are defined using the `#define` keyword. For example, we can define the following macros:

```c
#define F first
#define S second
#define PB push_back
#define MP make_pair
```

then the code:

```c
v.push_back(make_pair(y1,x1));
v.push_back(make_pair(y2,x2));
int d = v[i].first+v[i].second;
```

can be shorted as follows:

```c
v.PB(MP(y1,x1));
v.PB(MP(y2,x2));
int d = v[i].F+v[i].S;
```

A macro can also have parameters which makes it possible to shorten loops and other structures as follows:

```c
// Define a macro
#define REP(i,a,b) for (int i = a; i <= b; i++)

// Original code
for (int i = 1; i <= n; i++) {
    search(i);
}

// Shoertened version
REP(i,1,n) {
    search(i);
}
```











