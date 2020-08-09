import numpy as np
import sys

n = np.array([1, 2, 3])
#print(n)

nm = np.array([(1, 2, 3), (4, 5, 6)])

#print(nm)

#print(np.arange(1000))

l = range(100)
l = 1
#print(sys.getsizeof(l) * len(l))

y = np.arange(100)
y = np.array(1)
#print(y.size * y.itemsize)

#q = np.array([4, 5, 6])
#print(n / q)
q = np.array([[[1, 2], [3, 4]], [[4, 5], [6, 7]]])
print(q)
print(q.ndim)
print(q.shape)
print(len(q))