from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime, date
import requests
import json


def index(request):

    # if not a post request, display page
    if request.method != "POST":
        date_now = datetime.today().strftime('%Y-%m-%d')
        return render(request, 'base.html', {'date': date_now})

    # if post request are present, continue to process post request
    if request.POST['start-date'] and request.POST['end-date']:
        # convert to date string to datetime and validate that dates are valid format
        # if not, raise value error exception
        try:
            start_date = datetime.strptime(request.POST['start-date'], '%Y-%m-%d')
            end_date = datetime.strptime(request.POST['end-date'], '%Y-%m-%d')
            date_now = datetime.today()
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

        # validate that start date is less than end date and end_data is equal or less than todays date
        if start_date < end_date <= date_now:
            # convert dates back to string format
            start_date = datetime.strftime(start_date, '%Y-%m-%d')
            end_date = datetime.strftime(end_date, '%Y-%m-%d')

            # get results from search
            results = search_results(start_date, end_date)

            print(results)

            return render(request, 'home.html', {'results': results})

        else:
            print("ERRORRORORORORORORO")

        return render(request, 'base.html')


    else:
        return HttpResponse("FUCK YOU")


def search_results(start_date, end_date):
    # api key
    API_KEY = "EAnJsZsdRGv4hM0zeLUKosCya5AkJV1GP5jDHRxQ"

    # api url
    url = "https://api.nasa.gov/planetary/apod"

    # parameters used in query
    params = {'start_date': start_date,
              'end_date': end_date,
              'api_key': API_KEY}

    # try for a get request from url with parameters
    try:
        response = requests.get(url=url, params=params)
        json_data = response.json()
        return json_data
    except ConnectionError:
        return "There was a connection error. Please try again later."
