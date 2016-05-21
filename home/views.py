from django.shortcuts import render
from . import moviedb
import itertools
import urllib2
import json
# Create your views here.

book_api_url = "https://api.nytimes.com/svc/books/v3/lists/Combined-Print-and-E-Book-Fiction.json?api-key=708956a4bb4f47d2ab3b8bf2e9a12abe"

def index(request):
    dic = moviedb.get_data()
    title = dic[0][:12]
    image = dic[1][:12]
    res = urllib2.urlopen(book_api_url)
    book_obj = json.loads(res.read())
    book_title = []
    book_image = []
    for i in book_obj["results"]["books"]:
        if i["title"] and i["book_image"]:
            book_title.append(i["title"])
            book_image.append(i["book_image"])

    zipped_data = zip(title,image)
    book_data = zip(book_title[:12],book_image[:12])
    return render (request,'index.html',{'data': zipped_data,"book_data":book_data})
