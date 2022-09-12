#ToDo
#  Remove random key associated with countries that are found in json.
#  Fix if statements in try/except blocks.

# Create your views here.

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import pymongo, random
from collections import OrderedDict

client = pymongo.MongoClient('mongodb://127.0.0.1/world')

#Define Db Name
dbname = client['world']

#Define Collection
collection = dbname['factbook']

#  Dictionary to hold results to pass to template.
info_dictionary = OrderedDict()

# Create your views here.
def index(request):

    conflict_details = collection.find({},{'Government':{'Country name':1},'Transnational Issues':{'Disputes - international':1}})

    for r in conflict_details:

        #  Temp key to use in dictionary. Fix this issue. 
        random_number = random.random()

        try:
            country_name = r['Government']['Country name']['conventional short form']['text']
            info_dictionary[country_name] = ''
        except:
            info_dictionary[str(random_number)] = ''

        try:
            if random_number not in info_dictionary:
                international_disputes = r['Transnational Issues']['Disputes - international']['text']
                info_dictionary[country_name] = international_disputes
            else:
                info_dictionary[str(random_number)] = international_disputes
        except:
            international_disputes = 'None.'
            info_dictionary[country_name] = 'None'

    sorted_info_dictionary = sorted(info_dictionary.items())

    return render(request, 'output.html', {'context':sorted_info_dictionary})
