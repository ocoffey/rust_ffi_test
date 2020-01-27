# Python Testing

Using the Rust FFI in Python

## Iterative Python Function

Typehinting was used mostly as habit.

```python
def iterative_mult(a: int, b: int) -> int:
    mySum: int = 0
    for x in range(b):
        mySum += a
    return mySum
```

## Recursive Python Function

```python
def recursive_mult(a: int, b: int) -> int:
    if b <= 0:
        return 0
    else:
        return recursive_mult(a, b-1) + a
```

## Time Comparison

Now for the fun part! I compared them in Python, using the unittest library (although this was unneeded; it could have been run in a `main()` or equivalent function).

For background in your own comparisons, these tests were run on an old computer (built in 2010), using the Windows Subsystem for Linux remoted into with VSCode.

I had 3 sets of inputs, and ran comparisons for each method type against each set. All times reported are in seconds. Results are as follows:

### Iterative Multiplication Results

For very small sizes, Python beats out Rust in times (because of the overhead from using a FFI).

|Input Sizes:|    1, 2    |
|     ---    |     ---    |
|Python Time:|0.0000052452|
|Rust Time:  |0.0000190735|

> Python to Rust Speed Ratio: ~ 1:4

But even starting at reasonable sizes, we can start to see the difference between interpreted and compiled language speeds.

|Input Sizes:|   10, 20   |
|     ---    |     ---    |
|Python Time:|0.0000078678|
|Rust Time:  |0.0000054836|

> Python to Rust Speed Ratio: ~ 7:5

|Input Sizes:|  100, 200  |
|     ---    |     ---    |
|Python Time:|0.0000197887|
|Rust Time:  |0.0000045300|

> Python to Rust Speed Ratio: ~ 5:1

|Input Sizes:| 1000, 2000 |
|     ---    |     ---    |
|Python Time:|0.0001833439|
|Rust Time:  |0.0000040531|

> Python to Rust Speed Ratio: ~ 45:1

|Input Sizes:|5000, 10000 |
|     ---    |     ---    |
|Python Time:|0.0009775162|
|Rust Time:  |0.0000066757|

> The last size didn't increase by a full factor of 10 because it had a seg fault during recursion.

### Recursive Multiplication Results

Recursion for this small size has a fairly equivalent speed to the iterative method.

|Input Sizes:|    1, 2    |
|     ---    |     ---    |
|Python Time:|0.0000045300|
|Rust Time:  |0.0000183582|

> Python to Rust Speed Ratio: ~ 4:1

|Input Sizes:|   10, 20   |
|     ---    |     ---    |
|Python Time:|0.0000307560|
|Rust Time:  |0.0000047684|

> Python to Rust Speed Ratio: ~ 6:1

|Input Sizes:|  100, 200  |
|     ---    |     ---    |
|Python Time:|0.0003054142|
|Rust Time:  |0.0000054836|

> Python to Rust Speed Ratio: ~ 61:1

|Input Sizes:| 1000, 2000 |
|     ---    |     ---    |
|Python Time:|0.0043919086|
|Rust Time:  |0.0000073910|

> Python to Rust Speed Ratio: ~ 600:1

|Input Sizes:| 5000, 10000|
|     ---    |     ---    |
|Python Time:|0.0238883495|
|Rust Time:  |0.0000183582|

> Python to Rust Speed Ratio: ~ 1300:1

[Back to main page](https://github.com/ocoffey/rust_ffi_test, "Main Page")
