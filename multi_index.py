import pandas as pd
from datetime import datetime

data=[
    dict(name="daniel",type="doc1", pay=1000, date=datetime(2020, 4,3)),
    dict(name="paul",type="doc2", pay=1300, date=datetime(2020, 4,3)),
    dict(name="daniel",type="doc2", pay=1300, date=datetime(2020, 4,4)),
    dict(name="paul",type="doc2", pay=1100, date=datetime(2020, 4,4)),
    dict(name="daniel",type="doc3", pay=1200, date=datetime(2020, 4,5)),
]

df=pd.DataFrame(data)
print(df)

# GET INDEX VALUES FOR MULTI INDEX DF
types=df['type'].unique().tolist()
print(types)

print('###################')
group=df.groupby(by = ['date','type'], sort=False)['pay'].agg(['sum'])
print(group)

print('###################')
idx = pd.MultiIndex.from_product([group.index.levels[0], types])
linear_data=group.reindex(idx, fill_value=0)
print(linear_data)

# Multi Level list comprehension
print({level.strftime('%Y/%m/%d'): linear_data.xs(level).to_dict('index') for level in linear_data.index.levels[0]})

# RESULT
"""
INSPIRED BY
https://stackoverflow.com/questions/47372181/pandas-groupby-how-to-show-zero-counts-in-dataframe
{
 '2020/04/03': {'doc1': {'sum': 1000}, 'doc2': {'sum': 1300}, 'doc3': {'sum': 0}},
 '2020/04/04': {'doc1': {'sum': 0}, 'doc2': {'sum': 2400}, 'doc3': {'sum': 0}}, 
 '2020/04/05': {'doc1': {'sum': 0}, 'doc2': {'sum': 0}, 'doc3': {'sum': 1200}}}

"""

"""
https://stackoverflow.com/questions/42150769/pandas-multi-index-dataframe-to-nested-dictionary

MORE LEVELS, NOT TESTED


{level0: {level1: df.xs([level0, level1]).to_dict('index') for level1 in df.index.levels[1]} for level0 in df.index.levels[0]}


"""