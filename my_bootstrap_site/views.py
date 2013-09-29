# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

def Home(request):
	#return HttpResponse('Aloha!')

	return render(request, 'aloha.html')


def SayMyName(request, called_name = None):

	if called_name != None:

		return render(request, 'content_aloha.html', { 'name': called_name, 'gender': 'male', 'BASE_URL': request.get_host() })

	else:

		return redirect('/site/say_my_name/Heisenberg')

