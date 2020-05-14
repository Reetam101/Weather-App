import os, requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.contrib import messages

# Create your views here.
def index(request):
    all_weather = []
   
    api_key = os.environ.get('API_KEY')
    cities = City.objects.all()

   
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            matching_city = City.objects.filter(name=name)
            if matching_city.exists():
                messages.add_message(request, messages.ERROR, f'{name} Already exits!')
            else:    
                form.save()
    form = CityForm()
    
    for city in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}'
        city_weather = requests.get(url).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        all_weather.append(weather)

    
    context = {
        'all_weather': all_weather,
        'form': form
    }

    return render(request, 'weather/index.html', context)