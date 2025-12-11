import pandas as pd 
import numpy as np
a = np.array([123,1234,"asdw","Ronnakon"])
print(a)
print(a.dtype)
b = pd.Series(a)
print(b)