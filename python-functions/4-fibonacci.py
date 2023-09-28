fibonacci = lambda n: n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def fibonacci_sequence(n):
    return [fibonacci(i) for i in range(n)]
(fibonacci_sequence(10))