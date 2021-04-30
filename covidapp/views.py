from django.shortcuts import render

import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': #Your Rapid API Key#,
    'x-rapidapi-host': ####
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)


# Create your views here.

def helloworldview(request):
    countries = []
    total_results_fetched = int(response['results'])
    for i in range(0, total_results_fetched):
        countries.append(response['response'][i]['country'])

    countries.sort()


    #string = "Everyone"
    #mylist = [1, 2, 3, 4, 5]
    if request.method == 'POST':
        selected_country = request.POST['selected_country']
        #print(selected_country)
        total_results_fetched = int(response['results'])
        for i in range(0, total_results_fetched):
            if selected_country == response['response'][i]['country']:
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                critical = response['response'][i]['cases']['critical']
                recovered = response['response'][i]['cases']['recovered']
                total = response['response'][i]['cases']['total']
                if critical is None:
                    critical = "NA"
                if new is None:
                    new = "NA"
                try:
                    dead = int(total) - int(recovered) - int(active)
                except:
                    dead = "NA"
                    if total is None:
                        total = "NA"
                    if recovered is None:
                        recovered = "NA"
                    if active is None:
                        active = "NA"
                #print(response['response'][i]['cases'])
                selected_country = selected_country.upper()
                context = { 'selected_country' : selected_country, 'countries' : countries, 'new' : new, 'active' : active, 'critical' : critical, 'recovered' : recovered, 'total' : total, 'dead' : dead}
                return render(request, 'helloworld.html', context)

    

    context = { 'countries' : countries, }
    return render(request, 'helloworld.html', context)