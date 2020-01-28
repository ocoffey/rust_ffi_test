#!/usr/bin/env ruby
require 'ffi'

# loading our dll as a module
module Mults
    # was missing the second ':' for so long and running into errors;
    # that was fun
    extend FFI::Library
    # path to our file
    # the end bit is so this works even if
    # the library is compiled in a different environment
    ffi_lib '../my_lib/target/release/libembed.' + FFI::Platform::LIBSUFFIX
    # functions attached in the form <fn name>, [<fn param types>], <return type>
    attach_function :recursive_multiplication, [ :int, :int ], :int
    attach_function :iterative_multiplication, [ :int, :int ], :int
end

# basic iterative multiplication
def iterative_mult(a, b)
    sum = 0
    for i in 1..b do
        sum += a
    end
    sum
end

# basic iterative multiplication
def recursive_mult(a, b)
    if b <= 0
        0
    else
        recursive_mult(a, b-1) + a
    end
end

# 2d array of sizes
sizes = [[1, 2], [10, 20], [100, 200], [1000, 2000], [5000, 10000]]

puts "Iterative Multiplication"
puts
for size in sizes
    # ruby version
    tick = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    iterative_mult(size[0], size[1])
    tock = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    # ruby time
    ruby_rec = tock - tick
    # rust version
    tick = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    Mults::iterative_multiplication(size[0], size[1])
    tock = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    # rust time
    rust_rec = tock - tick
    puts "Input Sizes: %d, %d" % [size[0], size[1]]
    puts "Ruby Time:    %0.10f" % ruby_rec
    puts "Rust Time:    %0.10f" % rust_rec
    puts
end

puts "Recursive Multiplication"
for size in sizes
    puts
    # ruby version
    tick = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    recursive_mult(size[0], size[1])
    tock = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    # ruby time
    ruby_rec = tock - tick
    # rust version
    tick = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    Mults::recursive_multiplication(size[0], size[1])
    tock = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    # rust time
    rust_rec = tock - tick
    puts "Input Sizes: %d, %d" % [size[0], size[1]]
    puts "Ruby Time:    %0.10f" % ruby_rec
    puts "Rust Time:    %0.10f" % rust_rec
end