from django.shortcuts import HttpResponse
from .models import book

# Create your views here.
def index(request):
	return HttpResponse(request, 'template.html')

def store(request):
	count = book.objects.all().count()
	print(count)
	context = {
		'count' : '1'
	}
	return HttpResponse(request, 'store.html', context)
	#return render(request, 'store.html', count)

def chetan_bhagat(request):
	return HttpResponse(request, 'chetan_bhagat.html')