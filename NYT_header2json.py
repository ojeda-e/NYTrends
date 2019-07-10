import urllib.request
import requests
from string import ascii_lowercase, ascii_uppercase
from heapq import nlargest 
import operator
import matplotlib.pyplot as plt
from calendar import month_name
import string
import json

URL_ASEARCH = 'http://api.nytimes.com/svc/search/v2/articlesearch.'
URL_ARCHIVE = 'https://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}' 

def my_archive(year, month, key):
    "Calls the URL and returns a json of the search results"
        
    url = (URL_ARCHIVE.format(year, month, key))
    print("Checking url ... ", url)
    r = requests.get(url)

    return r.json()['response']





