from flask import Flask
from flask import render_template
#from pymongo import MongoClient
import json
#from bson import json_util
#from bson.json_util import dumps

app = Flask(__name__)

#MONGODB_HOST = 'localhost'
#MONGODB_PORT = 27017
#DBS_NAME = 'donorschoose'
#COLLECTION_NAME = 'projects'
#FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}

#http://127.0.0.1:5000/
@app.route("/")
def test():
    return 'Everything is running!'

import xlrd
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
from pylab import rcParams
rcParams['figure.figsize'] = 13, 10
#import json

from os.path import join, dirname, abspath

#upload excel with balance
fname = join(dirname(abspath('__file__')), 'ElementaryFlows.xlsx')
oname = join(dirname(abspath('__file__')), 'ElementaryFlows.json')

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

#---------------------------------------
#-JSON needs to be adapted to vis needs-
#---------------------------------------

#http://127.0.0.1:5000/balance/elementaryresults
@app.route('/balance/elementaryresults')
def high_poverty_states():
 #   donors_choose_url = "http://api.donorschoose.org/common/json_feed.html?highLevelPoverty=true&APIKey=DONORSCHOOSE"
 #   response = urllib2.urlopen(donors_choose_url)
 #   json_response = json.load(response)
    return df.to_json()   

#    states = set()
#    for proposal in json_response["proposals"]:
#        states.add(proposal["state"])
#
#    return json.dumps(list(states))
  
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
    