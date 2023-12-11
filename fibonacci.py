import numpy as np


def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    Parameters:
    - n (int): The index of the Fibonacci number to be calculated.

    Returns:
    - int: The n-th Fibonacci number.

    Raises:
    - TypeError: If n is not a non-negative integer.
    - ValueError: If n is a negative integer.

    Algorithm:
    - If n is less than THREASHOLD, use the iterative method to calculate the n-th Fibonacci number.
    - Otherwise, use the matrix multiplication method to calculate the n-th Fibonacci number.

    Complexity:
    - if n < THREASHOLD, O(n)
    - otherwise, O(log(n))
    """

    if not isinstance(n, int):
        raise TypeError("n must be a non-negative integer")

    if n < 0:
        raise ValueError("n must be a non-negative integer")

    THREASHOLD = 400  # test on MAC M1
    if n < THREASHOLD:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    else:
        M = np.array([[1, 1], [1, 0]], dtype=object)
        F = np.linalg.matrix_power(M, n - 1)
        return F[0, 0]
