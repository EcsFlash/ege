import sys
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc

y = 0
z = 0
@bootstrap
def f(x):
    if x == 1:
        yield 1
    if x > 1:
        yield x * (yield f(x-1))



sys.setrecursionlimit(3000)
print(f(2023)/f(2020))



