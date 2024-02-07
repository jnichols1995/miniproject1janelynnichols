import numpy as np 

import matplotlib.pyplot as plt

a = np.arange(15).reshape(3,5)

print(a)

print(a.shape)
print(a.dtype.name)

a = np.array([2,3,4])
print(a.max)
print(a)


plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()







