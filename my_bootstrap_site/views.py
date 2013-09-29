# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
	#return HttpResponse('Aloha!')

	return render(request, 'aloha.html')


def SayMyName(request):

	return render(request, 'content_aloha.html', { 'name': 'Heisenberg', 'gender': 'male'})