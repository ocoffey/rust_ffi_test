#!/usr/bin/env ruby
require 'ffi'

module Mults
    extend FFI:Library
    ffi_lib '../my_lib/target/release/libembed.' + FFI::Platform::LIBSUFFIX
    attach_function :recursive_multiplication, [ :int, :int ], :int
    attach_function :iterative_multiplication, [ :int, :int ], :int
end
