import pandas as pd
data_ls = [50,700,"asdw","Ronnakon"]
idx = [10,20,30,40]
ps = pd.Series(data_ls,index=idx)
print(ps)