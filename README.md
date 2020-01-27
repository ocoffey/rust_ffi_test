# Using Rust in Different Languages

A simple test for trying to use some Rust methods across a few different languages, with an empiric comparison between Rust and the native language for process runtimes on varying input sizes.

Recursive and iterative multiplication methods are used, with equivalent methods written in each language.

This mini-project makes use of Rust's [FFI functionality](https://doc.rust-lang.org/1.2.0/book/rust-inside-other-languages.html, "FFI Functionality"), to create a DLL that languages can link to and use.

## Iterative Multiplication

A simple implementation; it doesn't account for negative numbers or anything, and was more used for testing a simple algorithm. Semi-pseudocode as follows:

```shell
<iterative function name>(a, b)
    sum = 0
    loop b times
        sum += a
    return sum
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

Also a simple implementation for recursive multiplication (recursion 101). Doesn't account for negatives, as that's outside the scope of this test. Pseudo-ish code is as follows:

```shell
<recursive function name>(a, b)
    if b <= 0
        return 0
    else
        return <fn name>(a, b - 1) + a
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

## Links to Implementations by Language

* [Python](https://github.com/ocoffey/rust_ffi_test/tree/master/Python/README.md, "Python Implementation")

## Notes

* Writing this helper function in Rust was extremely easy to whip up
* Those runtimes speak for themselves

## Wrapping Up

If you were curious about using Rust's FFI, I hope this small look into it encourages you to tinker with it! I plan on looking at using the FFI in many other languages, and might continue documenting my journey!
