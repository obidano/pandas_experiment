import pandas as pd
from datetime import datetime
import sys
data=[
    dict(name="daniel",type="doc1", pay=1000, date=datetime(2020, 4,3)),
    dict(name="paul",type="doc2", pay=1300, date=datetime(2020, 4,3)),
    dict(name="daniel",type="doc2", pay=1300, date=datetime(2020, 4,4)),
    dict(name="paul",type="doc2", pay=1100, date=datetime(2020, 4,4)),
    dict(name="daniel",type="doc3", pay=1200, date=datetime(2020, 4,5)),
]

df=pd.DataFrame(data)
print(df)
types=df['type'].unique().tolist()
print(types)

print('###################')
#group0=df.groupby(by =  ['date','type'], sort=False)['type'].count().to_frame(name='sum').reset_index()
#print(group0)

print('###################')
group=df.groupby(by = ['date','type'], sort=False)['pay'].agg(['sum'])

#group.set_index("date", drop=True, inplace=True)
print(group)

print('###################')
idx = pd.MultiIndex.from_product([group.index.levels[0], types])
#print(idx)
linear_data=group.reindex(idx, fill_value=0)
#linear_data.index.levels[0]= linear_data.index.levels[0].strftime('%Y/%m/%d')
print(linear_data)
print(type(linear_data))
print({level.strftime('%Y/%m/%d'): linear_data.xs(level).to_dict('index') for level in linear_data.index.levels[0]})
sys.exit()

print('###################')
print(linear_data.index)
reset_df=linear_data.reset_index(level=[0,1])
print(reset_df)
print(reset_df.index)
#print(linear_data.reset_index(level=[1]).to_dict(orient='index'))
#print(linear_data.to_dict(orient='index'))
#sys.exit()

#print(reset_df.set_index('date').T.to_dict('dict'))
#print(group.set_index('date').T.to_dict('list'))