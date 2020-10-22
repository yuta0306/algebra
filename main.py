import algebra as alg

x = alg.matrix([[0, 1, 2], [3, 4, 5]])
y = alg.matrix([[1, 2], [3, 4], [5, 6]])


print(x.T, x.T.shape)
# matrix([
#          [0, 3]
#          [1, 4]
#          [2, 5]
#        ])

print(x.trace)
# None

print(alg.is_zerovec(x), alg.is_zerovec([0, 0, 0]))
# False True

print(alg.zeros((3, 3)))
# matrix([
#          [0, 0, 0]
#          [0, 0, 0]
#          [0, 0, 0]
#        ])

print(alg.zeros_like(x))
# matrix([
#          [0, 0, 0]
#          [0, 0, 0]
#          [0, 0, 0]
#        ])

print(alg.ones((3, 3)))
# matrix([
#          [1, 0, 0]
#          [0, 1, 0]
#          [0, 0, 1]
#        ])

print(alg.ones_like(x))
# Traceback (most recent call last):
#   File "main.py", line 16, in <module>
#     print(alg.ones_like(x))
#   File "opt/algebra.py", line 217, in ones_like
#     raise ValueError('expect the shape ({0}, {0}), but ({1})'.format(array.row, array.shape))
# ValueError: expect the shape (2, 2), but ((2, 3))
