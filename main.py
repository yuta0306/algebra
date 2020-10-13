import algebra as alg

x = alg.matrix([[0, 1, 2], [3, 4, 5]])
y = alg.matrix([[1, 2], [3, 4], [5, 6]])
k = 2

print(x.T)
print(len(x))
print(alg.zeros((3, 3)))
print(alg.zeros_like(x))
print(alg.ones((3, 3)))
print(alg.ones_like(x))