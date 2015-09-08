#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>To-Do lists</title><h1>Nama saya Gina Andriyani</h1></html>')
