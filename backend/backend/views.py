from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Hello my name os OIs")

def my_view(request):
    data_from_django = {
        'title': 'Hello from Django!',
        'content': 'This is dynamic data from Django view.',
    }

    data_for_react = json.dumps(data_from_django)

    return render(request, 'mytemplate.html', {'data_for_react': data_for_react})