from django.http import HttpResponse
from django.shortcuts import render
import operator
import json
import requests

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()
    
    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            #increase
            wordDictionary[word] +=1
        else:
            #Add to the dictionary
            wordDictionary[word] = 1

    sortedwords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    data = requests.get("http://worldclockapi.com/api/json/est/now")
    time = data.json()
    print(time["currentDateTime"])
    return render(request, 'about.html',{'dictionary':time})