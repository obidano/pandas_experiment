import pandas as pd
from datetime import datetime
import sys
data=[
    dict(name="daniel",type="doc1", pay=1000, date=datetime(2020, 4,3)),
    dict(name="paul",type="doc2", pay=1300, date=datetime(2020, 4,3)),
    dict(name="daniel",type="doc2", pay=1300, date=datetime(2020, 4,4)),
    dict(name="paul",type="doc2", pay=1100, date=datetime(2020, 4,4)),
    dict(name="daniel",type="doc1", pay=1200, date=datetime(2020, 4,5)),
]

df=pd.DataFrame(data)
print(df)
print('###################')
group=df.groupby(by = ['name'])['pay'].sum().to_frame(name='sum').reset_index()
print(group)
#sys.exit()
print('###################')
print(group.set_index('name').T.to_dict('list'))