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

