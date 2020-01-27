# Using Rust in Python

A simple test for trying to use some Rust methods in Python, with an empiric comparison between Rust and native Python for the process runtimes on varying input sizes.

Recursive and iterative multiplication methods are used, with equivalent methods written in each language.

This mini-project makes use of Rust's [FFI functionality](https://doc.rust-lang.org/1.2.0/book/rust-inside-other-languages.html, "FFI Functionality"), to create a DLL that Python can then link and use.

## Iterative Multiplication

A simple implementation; it doesn't account for negative numbers or anything, and was more used for testing a simple algorithm. Semi-pseudocode as follows:

```
<iterative function name>(a, b)
    sum = 0
    loop b times
        sum += a
    return sum
```

### Iterative Python

Typehinting was used mostly as habit.

```python
def iterative_mult(a: int, b: int) -> int:
    mySum: int = 0
    for x in range(b):
        mySum += a
    return mySum
```

### Iterative Rust

For those unfamiliar with Rust, `usize` is an unsigned integer of a size to be accomodated during runtime. This means that if a small number is entered, a comparative `short` is used, and that larger numbers would use comparative `long`s.

The `_` in the loop is because we don't actually use the iterator, and therefore don't care to store it in a variable.

`mult` is at the end by itself because of implicit returning.

The `pub extern` is for FFI use; pretty much saying "A public method, for external use".

```rust
pub extern fn iterative_multiplication(a: usize, b: usize) -> usize {
    let mut mult = 0;
    for _ in 0..b {
        mult += a;
    }
    mult
}
```

## Recursive Multiplication

Also a simple implementation for recursive multiplication (from recursion 101). Doesn't account for negatives, as that's outside the scope of this test. Pseudo-ish code is as follows:

```
<recursive function name>(a, b)
    if b <= 0
        return 0
    else
        return <fn name>(a, b - 1) + a
```

### Recursive Python

```python
def recursive_mult(a: int, b: int) -> int:
    if b <= 0:
        return 0
    else:
        return recursive_mult(a, b-1) + a
```

### Recursive Rust

```rust
pub extern fn recursive_multiplication(a: usize, b: usize) -> usize {
    if b <= 0 {
        0
    } else {
        recursive_multiplication(a, b-1) + a
    }
}
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

## Notes

* Writing this helper function in Rust was extremely easy to whip up
* Those runtimes speak for themselves

## Wrapping Up

If you were curious about using Rust's FFI, I hope this small look into it encourages you to tinker with it! I plan on looking at using the FFI in many other languages, and might continue documenting my journey!
