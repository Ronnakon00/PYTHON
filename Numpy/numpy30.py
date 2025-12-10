import numpy as np
a = np.arange(1,21)
print(a)
print(np.split(a,4))
#แบ่งเท่าๆกัน
b = np.arange(1,21)
c = b.reshape(5,4)
print(c)
print(np.hsplit(c,4))