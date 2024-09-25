
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"\nArguments: {args}, {kwargs}")
        result = list(func(*args, **kwargs))
        print(f"\nResult: {result}\n")
        return result

    return wrapper

def exception_decorator(func):
    def wrappper(*args,**kwargs):
        try:
            result = list(func(*args,**kwargs))
            return result
        except ValueError as expectation:
            print(f'\nUnpaired numbers from list: {result}\n')
    return wrappper


numbers_list = list(range(7))
generator_of_paired_numbers = (x for x in numbers_list if x % 2 == 0)
print(generator_of_paired_numbers)

for item in generator_of_paired_numbers:
    print(item)

print('\n')
def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

N = 8
for number in fibonacci_generator(N):
    print(number)


my_iterable = iter(reversed([1,2,3,4,5]))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))


try:
    print(next(my_iterable))
except StopIteration:
    print("\nStopIteration: Ітератор закінчився")

@logger
@exception_decorator
def iterator_of_paired_numbers(max_value):
    for num in range(max_value + 1):
        if num % 2 == 0:
            yield num

paired_numbers = iterator_of_paired_numbers(20)
for paired_number in paired_numbers:
    print(paired_number)



