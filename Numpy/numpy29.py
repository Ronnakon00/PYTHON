import numpy as np
a = np.arange(1,11)
print(a)
print(np.delete(a,2))
b = a.reshape(2,5)
print(b,"\n")
print(np.delete(b,2,axis=1),"\n")
print(np.delete(b,0,axis=0),"\n")
#axis = 0 คือแนวนอน, axis = 1 คือแนวตั้ง