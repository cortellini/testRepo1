import pandas as pd
import numpy as np

data =  [
        ['client_id','order_id','date','amount'],
        [1,1,'13/8/20 17:00',23.12],
        [2,2,'14/8/20 12:00',21.12],
        [3,3,'14/8/20 17:00',3.12],
        [3,4,'13/8/20 14:00',123.12]
        ]

df = pd.DataFrame(data=data[1:], columns=data[0])
df.index += 1

print(df)
