# \[nyf\] C/C++

This section will briefly summarise basic C++ knowledge that can be useful for the purpose of learning and practicing data structures and algorithms. Extensive reference to C++ can be found elsewhere.

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

This command produces a binary file `app_name` fron the source code `code_file_name.cpp` following the C++11 standard `-std=c++11` with an optimisation `-O2` and warnings about possible errors `-Wall`.
