# Asterisk
# 흔히 알고있는 *를 의미함.
# 단순 곱셈,제곱 연산, 가변 인자 활용 등 다양하게 사용가능
def asterisk_test1(a, *args):
    print(a, args)
    print(a, args[0])
    print(a, *args)
    print(type(args))


asterisk_test1(1, 2, 3, 4, 5, 6)


def asterisk_test2(a, **kargs):
    print(a, kargs)
    print(a, *kargs)
    print(type(kargs))


asterisk_test2(1, b=2, c=3, d=4, e=5, f=6)


a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)
data = ([1, 2], [3, 4], [5, 6])
print(*data)


def asterisk_test3(a, b, c, d,):
    print(a, b, c, d)


data = {"b": 1, "c": 2, "d": 3}
asterisk_test3(10, **data)


for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(data)


def asterisk_test4(a, b, c, d, e=0):
    print(a, b, c, d, e)


data = {"d": 1, "c": 2, "b": 3, "e": 56}
asterisk_test4(10, **data)
