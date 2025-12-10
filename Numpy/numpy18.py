import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a,"\n")
print(a[:][:],"\n")
print(a[1:][1:],"\n")
print(a[1:,1:],"\n")
#[row,col]
print(a[1:,2:],"\n")
print(a[2:,1:],"\n")
print(a[:,2:],"\n")
print(a[::2,::2],"\n")