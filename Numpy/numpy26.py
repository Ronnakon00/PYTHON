import numpy as np
a = np.array([3,4,5,6])
b = np.array([8,6,5,10])
print(np.concatenate((a,b)))
print(np.append(a,100))
c = np.array([[10,20],[30,40]])
print(c)
print(np.append(c,[[50],[60]],axis=1))
