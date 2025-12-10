import numpy as np
a = np.array([[1,2],[3,4]])
print(np.insert(a,1,100,axis=0))
print(np.insert(a,1,100,axis=1))