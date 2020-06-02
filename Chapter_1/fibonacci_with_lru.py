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
