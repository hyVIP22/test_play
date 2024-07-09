from uuid import uuid4
from random import randint
"""公共的方法，测试过程中可以调用"""


def rand_str():
    res = str(uuid4()).replace("-", "")[:5]
    return res


def rand_str1(m=None, n=None):
    if m and n:
        res1 = str(uuid4()).replace("-", "")[:randint(m, n)]
    elif m and not n:
        res1 = str(uuid4()).replace("-", "")[:randint(m)]
    else:
        res1 = str(uuid4()).replace("-", "")[:10]
    return res1


if __name__ == '__main__':
    print(rand_str())
    print(rand_str1(5, 10))
