# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 21:54:40 2017

@author: danna
"""

url = "https://v3v10.vitechinc.com/solr/policy_info/select?indent=on&q=*:*&wt=json"

def getmarket():
    
    page = urllib2.urlopen("http://bitcoincharts.com/t/markets.json")
    data = json.load(page)
    for elem in data:
        if elem['symbol'] == "mtgoxUSD":
            print(elem)