#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fibonacci_sequence = []
    elif length == 1:
        fibonacci_sequence = [0]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, length):
            next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_number)
    
    print(str(fibonacci_sequence))


print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)
