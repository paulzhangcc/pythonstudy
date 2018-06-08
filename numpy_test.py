import numpy

import timeit

# a = np.arange(10)
# a.shape = (2,5)
# print(a)

persontype = numpy.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']
})


def test():
    numpy.array([('zhang', 1, '1.1'), ('feng', 2, '2.2')], dtype=persontype)[1]


print(timeit.Timer("test()", setup="from __main__ import test").timeit())


def test1():
    a = [0, 1, 2, 3]
    print(a)
    print(id(a))
    a *= 2
    print(a)
    print(id(a))
    print(a[1:3])


if __name__ == '__main__':
    b = b"example"
    print(type(b))
# a = numpy.random.rand(10, 2)
#    print(a)
