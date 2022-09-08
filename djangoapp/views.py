#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1/world')

#Define Db Name
dbname = client['world']

#Define Collection
collection = dbname['factbook']



# Create your views here.
def index(request):


    mascot_details = collection.find({})

    for r in mascot_details:
        print(r)


    return HttpResponse("<h1>Hello Ed, and welcome to my first <u>Django App</u> project!</h1>")
