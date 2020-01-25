import unittest
import time

def recursive_mult(a: int, b: int) -> int:
    if b <= 0:
        return 0
    else:
        return recursive_mult(a, b-1)

def iterative_mult(a: int, b: int) -> int:
    mySum: int = 0
    for x in range(b):
        mySum += a
    return mySum

class TestMults(unittest.TestCase):
    def test_functions(self):
        """Testing functions

        Preliminary tests to make sure that they all work as expected
        """
        # Store function names in a list
        func_names = [recursive_mult, iterative_mult]
        # iterate through, run each function and make sure they work as expected
        for f in func_names:
            self.assertEqual(f(3, 4), 12)
    
    def test_recursive(self):
        # python version
        tick = time.time()
        recursive_mult(5, 10)
        tock = time.time()
        # record time difference
        py_rec = tock - tick
        # rust version
        tick = time.time()
        recursive_multiplication(5, 10)
        tock = time.time()
        rust_rec = tock - tick
        print("Python Time: " + py_rec)
        print("Rust Time: " + rust_rec)


    def test_iterative(self):
        # python version
        tick = time.time()
        iterative_mult(5, 10)
        tock = time.time()
        # record time difference
        py_rec = tock - tick
        # rust version
        tick = time.time()
        iterative_multiplication(5, 10)
        tock = time.time()
        rust_rec = tock - tick
        print("Python Time: " + py_rec)
        print("Rust Time: " + rust_rec)
            