const {performance} = require('perf_hooks');

function iterative_mult(a, b) {
    var sum = 0;
    for (var i = 0; i < b; i++) {
        sum += a;
    }
    return sum;
}

function recursive_mult(a, b) {
    if (b <= 0) {
        return 0;
    }
    else {
        return recursive_mult(a, b-1) + a;
    }
}

const sizes = [[1, 2], [10, 20], [100, 200], [1000, 2000], [5000, 10000]];
// check iterative
console.log("Iterative Multiplication\n");
for (const size in sizes) {
    var tick = performance.now();
    iterative_mult(sizes[size][0], sizes[size][1]);
    var tock = performance.now();
    console.log(`Input Sizes: ${sizes[size][0]}, ${sizes[size][1]}`);
    console.log(`Javascript Time: ${((tock-tick) / 1000).toFixed(10)}\n`);
}

// check recursive
console.log("Recursive Multiplication\n");
for (const size in sizes) {
    var tick = performance.now();
    recursive_mult(sizes[size][0], sizes[size][1]);
    var tock = performance.now();
    console.log(`Input Sizes: ${sizes[size][0]}, ${sizes[size][1]}`);
    console.log(`Javascript Time: ${((tock-tick) / 1000).toFixed(10)}\n`);
}


/*
var ffi = require('ffi');

var lib = ffi.Library('../my_lib/target/release/libembed', {
    'recursive_multiplication': [ 'int', [ 'int', 'int' ] ],
    'iterative_multiplication': [ 'int', [ 'int', 'int' ] ]
})

console.log(lib.recursive_multiplication(3,5))
*/
