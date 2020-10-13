import algebra as alg

x = alg.matrix([[0, 1, 2], [3, 4, 5]])
y = alg.matrix([[1, 2], [3, 4], [5, 6]])

print(x.T, x.T.shape)
# matrix([
#          [0, 3]
#          [1, 4]
#          [2, 5]
#        ])

print(alg.zeros((3, 3)))
#  (3, 2)

print(alg.zeros_like(x))
# matrix([
#          [0, 0, 0]
#          [0, 0, 0]
#          [0, 0, 0]
#        ])

print(alg.ones((3, 3)))
# matrix([
#          [0, 0, 0]
#          [0, 0, 0]
#        ])

print(alg.ones_like(x))
# matrix([
#          [1, 0, 0]
#          [0, 1, 0]
#          [0, 0, 1]
#        ])
