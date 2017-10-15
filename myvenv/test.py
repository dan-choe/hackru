# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:12:01 2017

@author: danna
"""

import json
import urllib.request
import ijson
import urllib.request as urlopen
from matplotlib import pyplot as plt

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app) 

url = "https://v3v10.vitechinc.com/solr/policy_info/select?indent=on&q=*:*&wt=json"
url_part = "https://v3v10.vitechinc.com/solr/participant/select?indent=on&q=*:*&wt=json"
url_ad = "https://v3v10.vitechinc.com/solr/activities/select?indent=on&q=*:*&wt=json"

#@app.route('url',methods=['GET'])
@app.route("/")
def index():
    data = urllib.request.urlopen(url)
    response = data.read().decode('utf-8')
    content = json.loads(response)
    results = content['response']['docs']

    for result in results:
        print(result['id'])
    
    plt.plot([1,2,4],[1,4,9])
    plt.plot([1,2,4],[1,4,9])
    plt.legend(['Data1','Data2'])
    plt.xlabel('this is x axis')
    plt.ylabel('this is y axis')
    plt.show()
    #export img in same directory
    #plt.savefig('exproted_img')
    return "hi"

@app.route("/product")
def product():
    product = '&rows=0&fl=numFound&fq=insurance_product:'
    labels = ['Dental','Accidental']
    numParticipants = []
    
    for label in labels:
        data = urllib.request.urlopen(url+product+label)
        response = data.read().decode('utf-8')
        content = json.loads(response)
        results = content['response']
        numParticipants.append(results['numFound'])

    plt.pie(numParticipants, labels=labels)
    plt.show()
    
    return "product"
    #return render_template('chart.html', set=zip(values, labels, colors))

#currID = 0
stateDict = {}

def loadInfoF(currID):
    participants = url_part + '&fq=id:' + str(currID) + '&fl=state'
    data = urllib.request.urlopen(participants)
    
#    print('url :', participants)
    
    response = data.read().decode('utf-8')    
    content = json.loads(response)
    
    state = content['response']['docs']
    
    for result in state:
        print('id: ', str(currID), ', state: ', result['state'], stateDict.get(result['state']))
        if(stateDict.get(result['state'])):
            stateDict[result['state']] = stateDict.get(result['state']) + 1
        else:
            stateDict[result['state']] = 1
#    print('stateDict length ', len(stateDict))
    
    
@app.route("/state/<int:id>/")
def state(id):
    product = '&fl=participant_id&fq=insurance_product:'
    labels = ['Dental','Accidental']
#    rows = '&rows=1482000'
    rows = '&rows=1000'

    # For All Participants (policy_info)
    f = urllib.request.urlopen(url+rows+product+labels[int(id)-1])
   
    # For check info of individual    
    count = 0
    
    for prefix, event, value in ijson.parse(f):
        if prefix == 'response.docs.item.participant_id':
#            print(prefix, ' ', event, ' ', value)
            loadInfoF(str(value))
            count += 1
    
    print('stateDict length ', len(stateDict))
    
    for key, value in stateDict:
        print('stateDict key: ', key,' value: ', value)
    
    return "state" + str(id)


@app.route("/stateProduct")
def stateProduct():
    product = '&fl=participant_id&fq=insurance_product:'
    labels = ['Dental','Accidental']
#    rows = '&rows=1482000'
    rows = '&rows=50'
    
    # For All Participants (policy_info)
    f = urllib.request.urlopen(url+rows+product+labels[1])
   
    # For check info of individual    
    count = 0
    
    for prefix, event, value in ijson.parse(f):
        if prefix == 'response.docs.item.participant_id':
#            print(prefix, ' ', event, ' ', value)
#            if(count == 40):
#                break
            #keys.append(str(value))
            print(count, ' ', prefix, ' ', value)
            loadInfoF(str(value))
            count += 1
    
    print('stateDict length ', len(stateDict))
    
    for key, value in stateDict.items():
        print('stateDict key: ', key,' value: ', value)
    
    return "state"

    
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')    

#@app.route("/hello")
#def hello():
#    return "Hello World!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html',name=name)
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=80)
    
#    
#    sql = """
#        select * 
#        from policy_info pi 
#        where pi.policy_start_date 
#        between to_date(\"2016/02/01\", "yyyy/mm/dd") 
#        and to_date(\"2016/03/01\", \"yyyy/mm/dd")
#        """
   