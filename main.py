import algebra as alg

x = alg.matrix([[0, 1, 2], [3, 4, 5]])
y = alg.matrix([[1, 2], [3, 4], [5, 6]])
k = 2

print(x.T)
print(x * y * y, (x*y * y).shape)