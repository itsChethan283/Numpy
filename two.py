import numpy as np


l = [1, 2, 3]

n = np.array(l)


n = n + 3

n.append(4)
for i in n:
    print(i)
    