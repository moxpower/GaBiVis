from pandas import Series, DataFrame
import pandas as pd

pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.4,2001:1.7,2002:3.8}}

df=DataFrame(pop)

print pop

json=df.to_json()

print json


