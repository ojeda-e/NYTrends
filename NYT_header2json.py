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
    """Calls the URL and returns a json of the search results"""
        
    url = (URL_ARCHIVE.format(year, month, key))
    print("Checking url ... ", url)
    r = requests.get(url)

    return r.json()['response']


def drop_key(dict):
	"""Drop missleading keys in dictionary"""

    # Remove articles, personal pronouns, prepositions, etc
    drop = ["the", "a", "A", "As", "as", "at", "At", "Against", "About", "By", "With", "It", "Is", "to", "To", "TO", "in", "In", "MARKETS:",
        "BRIEFING", "IN", "Into", "for", "For", "THE", "The", "An", "an", "and", "And", "Are", "After", "Of", "OF","of", "Off", "May",
        "On", "on", "or", 'OR', 'Out', "One", "Over", "by", "her", "Her", "his", "His", "From", "That", "This", "No", "but", "GUIDE",
        "But", "Not", "Paid", "Notice:", "Deaths", "New", "Corrections", "Memorials", "Back", "October", "First", "York", "You", "Your", "Times;",
        "Their", "It's", "Its", "How", "Two",  "Up", "Who", "What", "When", "Where", "We", "They", "vs.",
        "Journal.", "Books", "Sports", "Big", "Say", "Do", "Be", "Sports", "Will", "I", "Has", "Your", "SUMMARY",
        "TRANSACTIONS", "QUOTATION"]

    # Remove number in range [0,100], ascii characters, years and months.
    drop.extend(str(i) for i in range(101))
    drop.extend(letter+'.' for letter in ascii_uppercase)
    drop.extend(month_name[i] for i in range(1,13))
    drop.extend(string.printable[i] for i in range(62,94))
    drop.extend(str(year) for year in range(2000,2019))
    

    # Remove keys in dictionary
    for word in drop:
        dict.pop(word, None)
        
    return dict


def word_dict(top, month, year, my_key, csv_file):
    """ Return a dictionary {"word": frequency_of_word} """


    print(month, year)
    list_words_inheader = []
    
    data = my_archive(year, month, my_key)
    
    for element in range(len(data['docs'])):
        
        if 'main' in data['docs'][element]['headline']:
            list_words_inheader.extend(data['docs'][element]['headline']['main'].split() )
            
        else:
            csv_file.write(str(year)+','+str(month)+','+str(element)+"\n")
            print("No main for header for index", element)

    #print(list_words_inheader)
    # Delete multiple occurrence
    new_list = list(set(list_words_inheader))  
    
    #create dictionary dict-like withs keys from list with single occurrence
    for i in new_list:
        word_freq = {key : 0 for key in new_list}

        
    #count frequency of each word
    for key in list_words_inheader:
        word_freq[key] = word_freq[key] + 1
        
    word_freq_f = drop_key(word_freq)
    
    fwords = {key: word_freq_f[key] for key in nlargest(top, word_freq_f, key = word_freq_f.get)}
    


    return fwords





