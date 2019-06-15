from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse(request, 'template.html')

def store(request):
	return HttpResponse(request, 'store.html')

def chetan_bhagat(request):
	return HttpResponse(request, 'chetan_bhagat.html')