import pandas as pd
from datetime import datetime

data=[
    dict(name="daniel", pay=1000, date=datetime(2020, 4,3)),
    dict(name="paul", pay=1300, date=datetime(2020, 4,3)),
    dict(name="daniel", pay=1300, date=datetime(2020, 4,4)),
    dict(name="paul", pay=1100, date=datetime(2020, 4,4)),
    dict(name="daniel", pay=1200, date=datetime(2020, 4,5)),
]

df=pd.DataFrame(data)
print(df)


# GROUP BY NAME AND COUNT
print('###################')
group=df.groupby(by = ['name'])['pay'].count().to_frame(name='count').reset_index()
print(group)

# TRANSPOSE DATAFRAME AND CONVERT TO DICT
print('###################')
print(group.set_index('name').T.to_dict('list'))

# RESULT
"""
{'daniel': [3], 'paul': [2]}

"""
