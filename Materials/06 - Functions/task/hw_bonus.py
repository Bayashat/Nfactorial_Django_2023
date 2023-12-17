"""
💎 Exercise-1: Memoized Fibonacci
Implement a memoized version of the Fibonacci sequence. The function "memoized_fibonacci(n: int) -> int" should return the nth number in the Fibonacci sequence, and it should use a cache to improve performance on subsequent calls.

Example:
memoized_fibonacci(10) -> 55
"""

fib_cache = {}
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    # check if the value is already in the cache
    if n in fib_cache:
        return fib_cache[n]
    
    # If not in the cache, compute the Fibonacci value
    result = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
    fib_cache[n] = result
    return result
        
"""
💎 Exercise-2: Currying Function
Write a function "curry(func, *args)" that implements currying. The function should return a new function that when called will return the result of applying the input function to the provided arguments, followed by the new arguments.

Example:
def add_three_numbers(a, b, c):
    return a + b + c
add_five_and_six = curry(add_three_numbers, 5, 6)
add_five_and_six(7) -> 18
"""

def curry(func, *args):
    def wrapper(*nums):
        result = func(*args, *nums)
        return result
    return wrapper

"""
💎 Exercise-3: Implement zip() using map() and lambda
Write a function "my_zip(*iterables)" that takes in multiple iterables and returns an iterator that aggregates elements from each of the iterables.

Example:
my_zip([1, 2, 3], [4, 5, 6]) -> [(1, 4), (2, 5), (3, 6)]
"""

def my_zip(*iterables):
    return list(map(lambda *args: args, *iterables))

print(my_zip([1, 2], [3, 4], [5, 6]))
"""
💎 Exercise-4: Caching Decorator
Write a decorator "caching_decorator(func)" that caches the results of the function it decorates.

Example:
@caching_decorator
def expensive_function(x, y):
    # Simulate an expensive function by sleeping
    import time
    time.sleep(5)
    return x + y
"""

def caching_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        # Create a unique key based on the function name and its arguments
        key = (func.__name__, args, frozenset(kwargs.items()))

        # Check if the result is already in the cache
        if key in cache:
            print("Using cached result.")
            return cache[key]

        # If not in the cache, call the original function
        result = func(*args, **kwargs)

        # Cache the result
        cache[key] = result

        return result

    return wrapper
        

"""
💎 Exercise-5: Recursive Flattening
Write a function "recursive_flatten(input_list: list) -> list" that takes a nested list and flattens it.

Example:
recursive_flatten([1, [2, [3, 4], 5]]) -> [1, 2, 3, 4, 5]
"""

def recursive_flatten(input_list: list) -> list:
    flatten_list = []
    for item in input_list:
        if isinstance(item, list):
            flatten_list.extend(recursive_flatten(item))
        else:
            flatten_list.append(item)
    return flatten_list

"""
💎 Exercise-6: Decorator for Checking Function Arguments
Write a decorator "check_args(*arg_types)" that checks the types of the arguments passed to the function it decorates.

Example:
@check_args(int, int)
def add(a, b):
    return a + b
"""

def check_args(*arg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for arg, arg_type in zip(args, arg_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Argument {arg} must be of type {arg_type.__name__}")

            # Check keyword arguments
            # for arg_name, arg_value in kwargs.items():
            #     arg_type = arg_types[len(args) + list(kwargs.keys()).index(arg_name)]
            #     if not isinstance(arg_value, arg_type):
            #         raise TypeError(f"Argument {arg_name} must be of type {arg_type.__name__}")

            # Call the original function
            return func(*args, **kwargs)

        return wrapper

    return decorator