"""
Create decorator logger.
The decorator should print to the console information about function's
name and all its arguments separated with ',' for the function decorated with logger.

Create function concat with any numbers of any arguments which concatenates arguments and apply logger decorator for this function.

For example

print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two
onetwo
"""


def logger(func):
    def inner(*args, **kwargs):
        string = ''
        for arg in args:
            string += str(arg) + ", "
        for _, kwarg in kwargs.items():
            string += str(kwarg) + ", "
        ret = func(*args, **kwargs)
        print(f"Executing of function {func.__name__} with arguments {string[:-2]}...")

        return ret

    return inner



@logger
def concat(a='', *args, **kwargs):
    con = a
    for k in args:
        con += k
    for _, k in kwargs.items():
        con += str(k)

    return con


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


print(concat(1))
print(concat('first string', second=2, third='second string'))
dict_args = {'first kwarg': 0, 'second kwarg': 'second kwarg'}
print(concat(**dict_args))
