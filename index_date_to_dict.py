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

# GROUP BY DATE AND COUNT
print('###################')
group=df.groupby(by = ['date'])['pay'].count().to_frame(name='count').reset_index()
print(group)

# FORMAT DATE INDEX AND CONVERT TO DICT
print('###################')
group['date']= group['date'].dt.strftime('%Y/%m/%d')
print(group.set_index('date').T.to_dict('list'))

# RESULT
"""
{'2020/04/03': [2], '2020/04/04': [2], '2020/04/05': [1]}
"""