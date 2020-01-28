# Ruby Testing

Using the Rust FFI in Ruby

## Iterative Ruby Function

```ruby
# basic iterative multiplication
def iterative_mult(a, b)
    sum = 0
    for i in 1..b do
        sum += a
    end
    sum
end
```

## Recursive Ruby Function

```ruby
# basic iterative multiplication
def recursive_mult(a, b)
    if b <= 0
        0
    else
        recursive_mult(a, b-1) + a
    end
end
```

## Time Comparison

Akin to Python, the Rust runtimes seem well worth it to use Ruby's FFI when you need a speedup.

The same input sizes are used across each language test.

### Iterative Multiplication Results

|Input Sizes: |     1, 2    |
|     ---     |     ---     |
|Ruby Time:   | 0.0000196000|
|Rust Time:   | 0.0000199000|

> Ruby to Rust Speed Ratio: ~ 1:1

|Input Sizes: |    10, 20   |
|     ---     |     ---     |
|Ruby Time:   | 0.0000063000|
|Rust Time:   | 0.0000036000|

> Ruby to Rust Speed Ratio: ~ 2:1

|Input Sizes: |   100, 200  |
|     ---     |     ---     |
|Ruby Time:   | 0.0000205000|
|Rust Time:   | 0.0000030000|

> Ruby to Rust Speed Ratio: ~ 6:1

|Input Sizes: |  1000, 2000 |
|     ---     |     ---     |
|Ruby Time:   | 0.0001719000|
|Rust Time:   | 0.0000028000|

> Ruby to Rust Speed Ratio: ~ 61:1

|Input Sizes: |  5000, 10000|
|     ---     |     ---     |
|Ruby Time:   | 0.0008479000|
|Rust Time:   | 0.0000030000|

> Ruby to Rust Speed Ratio: ~ 282:1

### Recursive Multiplication Results

|Input Sizes: |     1, 2    |
|     ---     |     ---     |
|Ruby Time:   | 0.0000041000|
|Rust Time:   | 0.0000038000|

> Ruby to Rust Speed Ratio: ~ 1:1

|Input Sizes: |    10, 20   |
|     ---     |     ---     |
|Ruby Time:   | 0.0000045000|
|Rust Time:   | 0.0000032000|

> Ruby to Rust Speed Ratio: ~ 3:2

|Input Sizes: |   100, 200  |
|     ---     |     ---     |
|Ruby Time:   | 0.0000491000|
|Rust Time:   | 0.0000030000|

> Ruby to Rust Speed Ratio: ~ 16:1

|Input Sizes: |  1000, 2000 |
|     ---     |     ---     |
|Ruby Time:   | 0.0004129000|
|Rust Time:   | 0.0000034000|

> Ruby to Rust Speed Ratio: ~ 121:1

|Input Sizes: |  5000, 10000|
|     ---     |     ---     |
|Ruby Time:   | 0.0018837000|
|Rust Time:   | 0.0000035000|

> Ruby to Rust Speed Ratio: ~ 538:1
