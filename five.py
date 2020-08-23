import numpy as np

#ar = np.arange(20)
#ar[2] = 20                  

#ar = np.diag([1, 2, 3])
#ar[1] [1] = 5

ar = np.arange(4)
#ar[:] = ar[:: -1 ]

ar[::8] = [1]

print(ar)