import xlrd
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
from pylab import rcParams
rcParams['figure.figsize'] = 13, 10
import json

from os.path import join, dirname, abspath

#upload excel with balance
fname = join(dirname(abspath('__file__')), 'ElementaryFlows.xlsx')

xls=pd.ExcelFile(fname)

df=xls.parse(skiprows=8,parse_cols="A:X")

#rename columns
new_columns=df.columns.values
new_columns[0]='Flows'
new_columns[1]='Flowtypes'
new_columns[2]='FlowtypesII'
df.columns=new_columns
df['Flows'].fillna("Flows", inplace=True)
df['Flowtypes'].fillna("Emissions to air", inplace=True)
#df=df.drop(['Total'], axis=1)
#df=df.set_index(['ElementaryFlows'])
df[:5]
#I feel I might need an extra header row
#df.columns=pd.MultiIndex.from_tuples(zip(df.columns,["DD","EE","FF"]))

#df.plot(kind='bar', stacked=True)



df.to_json()

#---------------------
#build a string array
#--------------------
#FlowArray=["Flows"]*43
#FlowSeries=pd.Series(FlowArray)

#ref=["Flows" for x in range(43)]
#pass it to Series
#refstr=pd.Series(ref)


"""
next steps:

---
-1-
---

Dataset shall look like:
Index   1       2       3       4
Plan    PlanA   PlanA   PlanA   PlanA
Process ProcA   ProcB   ProcC   ProcD
Resourc 1.0     0.9     0.1     0.0
Flows...
...

---
-2-
---

Represent this on my website
maybe using mongodb http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/

---
-3-
---

Modify presentation to have a mock-up

---
-4-
---

Convince Hannes/B�ttiger to invest in me



"""



#wname = join(dirname(abspath('__file__')), 'UserProfileUpdatePy.csv')

#df=pd.read_excel(fname, encoding="utf-8")
#pd.options.display.float_format = '{:.0f}'.format

#for utf-8 check http://stackoverflow.com/questions/12357261/handling-non-standard-american-english-characters-and-symbols-in-a-csv-using-py
#df=xl.parse("CSVProjectFinder", decoding="utf-8")
#type(xl)
#df1=df.replace(u"\u20ac",u"\x80")
#idf=df.set_index(['AccountName'])
#idf['ActiveEmployee']=True
#idf.to_csv(wname, sep='\t')