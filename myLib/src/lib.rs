#[pyfunction]
/// Basic recursive multiplication function
fn recursive_multiplication(a: usize, b: usize) -> PyResult<usize> {
    if b <= 0 {
        0
    } else {
        recursive_multiplication(a, b-1) + a
    }
}

/// Basic iterative multiplication function
fn iterative_multiplication(a: usize, b: usize) -> PyResult<usize> {
    let mut mult = 0;
    for _ in 0..b {
        mult += a;
    }
    mult
}

/*
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_recursive() {
        assert_eq!(recursive_multiplication(3, 5), 15);
    }
    #[test]
    fn test_iterative() {
        assert_eq!(iterative_multiplication(2, 4).ok(), Some(8));
        assert!(iterative_multiplication(2, 4).is_ok())
    }
    #[test]
    fn test_both() {
        assert_eq!(Some(recursive_multiplication(6, 7)), iterative_multiplication(6, 7).ok());
    }
}
*/