from django.shortcuts import render
import requests
import json

def home(request):
	send_url = "http://api.ipstack.com/check?access_key=be2a093998316de88c9b49fb6176fe5c"
	geo_req = requests.get(send_url)
	geo_json = json.loads(geo_req.text)
	latitude = geo_json['latitude']
	longitude = geo_json['longitude']
	city = geo_json['city']
	country_name = geo_json['country_name']
	context = {"city":city,"country":country_name}
	return render(request, 'home/index.html', context)


def login_test(request):
	return render(request, 'home/login_test.html')
