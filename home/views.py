from django.shortcuts import render
from . import moviedb
import itertools
# Create your views here.

def index(request):
    dic = moviedb.get_data()
    title = dic[0][:12]
    image = dic[1][:12]
    zipped_data = zip(title,image)
    return render (request,'index.html',{'data': zipped_data})
    

        