# Python Pandas Experiment

#### Python 3.6.8 and latest version of **Pandas**

I am formatting data from Pandas Dataframe in order to be used in charts with Javascript

All the outputs will be in **dictionnary**

Example

**Inputs**
```
[
    dict(name="daniel", type="doc1", pay=1000, date=datetime(2020, 4,3)),
    dict(name="paul", type="doc2", pay=1300, date=datetime(2020, 4,3)),
    dict(name="daniel", type="doc2", pay=1300, date=datetime(2020, 4,4)),
    dict(name="paul", type="doc2", pay=1100, date=datetime(2020, 4,4)),
    dict(name="daniel", type="doc3", pay=1200, date=datetime(2020, 4,5)),
]
```

**Outputs**
```
{
 '2020/04/03': {'doc1': {'sum': 1000}, 'doc2': {'sum': 1300}, 'doc3': {'sum': 0}},
 '2020/04/04': {'doc1': {'sum': 0}, 'doc2': {'sum': 2400}, 'doc3': {'sum': 0}}, 
 '2020/04/05': {'doc1': {'sum': 0}, 'doc2': {'sum': 0}, 'doc3': {'sum': 1200}}
 }

```
