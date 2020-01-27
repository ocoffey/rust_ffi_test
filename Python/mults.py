from ctypes import cdll
import unittest
import time
import sys

sys.setrecursionlimit(10**6)

def recursive_mult(a: int, b: int) -> int:
    if b <= 0:
        return 0
    else:
        return recursive_mult(a, b-1) + a

def iterative_mult(a: int, b: int) -> int:
    mySum: int = 0
    for x in range(b):
        mySum += a
    return mySum

def main():
    # load our rust dll
    lib = cdll.LoadLibrary("../my_lib/target/release/libembed.so")
    # Recursive Multiplication
    print(recursive_mult(2, 4))
    print(lib.recursive_multiplication(2, 4))
    # Iterative Multiplication
    print(iterative_mult(3, 5))
    print(lib.iterative_multiplication(3, 5))

class Tests(unittest.TestCase):
    """Empiric testing of iterative and recursive functions"""

    def setUp(self):
        """Loads our dynamicically linked library, written in Rust"""
        self.lib = cdll.LoadLibrary("../my_lib/target/release/libembed.so")
        self.sizes = [[1, 2], [10, 20], [100, 200], [1000, 2000], [5000, 10000]]

    def test_functions(self):
        """Testing functions

        Preliminary tests to make sure that they all work as expected
        """
        # Store function names in a list
        func_names = [recursive_mult, iterative_mult, self.lib.recursive_multiplication, self.lib.iterative_multiplication]
        # iterate through, run each function and make sure they work as expected
        for f in func_names:
            self.assertEqual(f(3, 4), 12)
    
    def test_recursive(self):
        """Compares recursive implementations in rust and python
        
        Uses 3 different input size sets for comparisons of small, medium, and big numbers
        """
        print("\nRecursive Multiplication\n")
        for size in self.sizes:
            # python version
            tick = time.time()
            recursive_mult(size[0], size[1])
            tock = time.time()
            # record time difference
            py_rec = tock - tick
            # rust version
            tick = time.time()
            self.lib.recursive_multiplication(size[0], size[1])
            tock = time.time()
            rust_rec = tock - tick
            print("Input Sizes: {:d}, {:d}".format(size[0], size[1]))
            print("Python Time: {0:.10f}".format(py_rec))
            print("Rust Time:   {0:.10f}".format(rust_rec))
            print()
        # Arbitrary test, because this is a 'unit test' after all
        self.assertEqual(1, 1)


    def test_iterative(self):
        """Compares iterative implementations in rust and python
        
        Uses 3 different input size sets for comparisons of small, medium, and big numbers
        """
        print("\nIterative Multiplication\n")
        for size in self.sizes:
            # python version
            tick = time.time()
            iterative_mult(size[0], size[1])
            tock = time.time()
            # record time difference
            py_rec = tock - tick
            # rust version
            tick = time.time()
            self.lib.iterative_multiplication(size[0], size[1])
            tock = time.time()
            rust_rec = tock - tick
            print("Input Sizes: {:d}, {:d}".format(size[0], size[1]))
            print("Python Time: {0:.10f}".format(py_rec))
            print("Rust Time:   {0:.10f}".format(rust_rec))
            print()
        self.assertEqual(1, 1)

if __name__ == "__main__":
    #main()
    unittest.main()