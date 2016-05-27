from django.shortcuts import render
from django.http import HttpResponse
from serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def users(request):
	if request.method == 'POST' :
		data = JSONParser().parse(request)
		serializer = UserSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		else: 
			return JSONResponse(serializer.errors,status = 400)
	return HttpResponse(status=400)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)





