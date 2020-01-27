#[no_mangle]
/// Basic recursive multiplication function
pub extern fn recursive_multiplication(a: usize, b: usize) -> usize {
    if b <= 0 {
        0
    } else {
        recursive_multiplication(a, b-1) + a
    }
}

#[no_mangle]
/// Basic iterative multiplication function
pub extern fn iterative_multiplication(a: usize, b: usize) -> usize {
    let mut mult = 0;
    for _ in 0..b {
        mult += a;
    }
    mult
}

#[cfg(test)]
/// Internal tests to ensure they actually work
mod tests {
    use super::*;
    #[test]
    fn test_recursive() {
        assert_eq!(recursive_multiplication(3, 5), 15);
    }
    #[test]
    fn test_iterative() {
        assert_eq!(iterative_multiplication(2, 4), 8);
    }
    #[test]
    fn test_both() {
        assert_eq!(recursive_multiplication(6, 7), iterative_multiplication(6, 7));
    }
}
