import os
from django.shortcuts import render
from .models import Student
import random
import requests
from datetime import datetime

def home(request):
    present = datetime.now()

    quotes = [
        "A room without books is like a body without a soul.",
        "Be the change that you wish to see in the world.",
        "If you tell the truth, you don't have to remember anything.",
        "A person who never made a mistake never tried anything new."
    ]

    random_quote = random.choice(quotes)

    def get_weather(city="ahmedabad"):
        api_key = os.getenv("WEATHER_API_KEY")  # Fetching API key from environment
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]

            temperature = main['temp']
            description = weather['description']

            return f"The temperature in {city}: {temperature}°C\nWeather Description: {description.capitalize()}"
        else:
            return "Unable to fetch weather data"

    weather_info = get_weather("ahmedabad")

    information = {
        'random_quote': random_quote,
        'weather_info': weather_info,
        'current_time': present.strftime('%Y-%m-%d %H:%M:%S'),
    }

    return render(request, 'studenthub/home.html', information)

def createstudent(request):
    present = datetime.now()

    quotes = [
        "A room without books is like a body without a soul.",
        "Be the change that you wish to see in the world.",
        "If you tell the truth, you don't have to remember anything.",
        "A person who never made a mistake never tried anything new."
    ]

    random_quote = random.choice(quotes)

    def get_weather(city="ahmedabad"):
        api_key = os.getenv("WEATHER_API_KEY")  # Fetching API key from environment
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]

            temperature = main['temp']
            description = weather['description']

            return f"The temperature in {city}: {temperature}°C\nWeather Description: {description.capitalize()}"
        else:
            return "Unable to fetch weather data"

    weather_info = get_weather("ahmedabad")

    information = {
        'random_quote': random_quote,
        'weather_info': weather_info,
        'current_time': present.strftime('%Y-%m-%d %H:%M:%S'),
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')

        Student.objects.create(name=name, email=email, mobile_number=mobile_number)

    return render(request, 'studenthub/register.html', information)

def list_students(request):
    present = datetime.now()

    quotes = [
        "A room without books is like a body without a soul.",
        "Be the change that you wish to see in the world.",
        "If you tell the truth, you don't have to remember anything.",
        "A person who never made a mistake never tried anything new."
    ]

    random_quote = random.choice(quotes)

    def get_weather(city="ahmedabad"):
        api_key = os.getenv("WEATHER_API_KEY")  # Fetching API key from environment
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]

            temperature = main['temp']
            description = weather['description']

            return f"The temperature in {city}: {temperature}°C\nWeather Description: {description.capitalize()}"
        else:
            return "Unable to fetch weather data"

    weather_info = get_weather("ahmedabad")

    students = Student.objects.all()

    information = {
        'random_quote': random_quote,
        'weather_info': weather_info,
        'current_time': present.strftime('%Y-%m-%d %H:%M:%S'),
        'students': students
    }

    return render(request, 'studenthub/students.html', information)
