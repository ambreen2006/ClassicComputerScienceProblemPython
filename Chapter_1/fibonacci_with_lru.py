"""
Excerpt from `https://docs.python.org/3/library/functools.html`:

Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.
....

In general, the LRU cache should only be used when you want to reuse previously computed values. Accordingly, it doesn’t make sense to cache functions with side-effects, functions that need to create distinct mutable objects on each call, or impure functions such as time() or random().
"""

from functools import lru_cache

@lru_cache(maxsize = None)
def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n-2)+fib1(n-1)

if __name__ == '__main__':
    fib_number = [70, 32, 56, 100]
    fib_values = [190392490709135, 2178309, 225851433717, 354224848179261915075]
    for number, known_value in zip(fib_number, fib_values):
        value = fib1(number)
        print(f'Fib({number}) = {value}')
        assert value == known_value, 'Incorrect value'
    print(fib1.cache_info())
