import pandas as pd
data_dict = {'banana':50,'papaya':40,'tomato':30}
ps = pd.Series(data_dict)
print(ps)
print(ps["banana"])
#ps[0],ps["key"]