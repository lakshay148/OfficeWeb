from django.http import HttpResponse
from serializers import UserSerializer, TaskSerializer
from serializers import DomainSerializer, RoleSerializer
from serializers import ModuleSerializer, PriviligeSerializer
from models import Task, Domain, Role, Module, Privilige
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def index(request):
    return HttpResponse("Hello, You're using the apis for Office Office")


@csrf_exempt
def users(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)
    return HttpResponse(status=400)


class JSONResponse(HttpResponse):
    """An HttpResponse that renders its content into JSON."""

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JSONResponse(serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)

        else:
            return JSONResponse(serializer.errors, status=400)

    return HttpResponse(status=400)


@csrf_exempt
def domains(request):
    if request.method == 'GET':
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return JSONResponse(serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DomainSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)

        else:
            return JSONResponse(serializer.errors, status=400)

    return HttpResponse(status=400)


@csrf_exempt
def modules(request):
    if request.method == 'GET':
        modules = Module.objects.all()
        serializer = DomainSerializer(modules, many=True)
        return JSONResponse(serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ModuleSerializer(data=data)
        if serializer.is_valid:
            serializer.save()
            return JSONResponse(serializer.data, status=201)

        else:
            return JSONResponse(serializer.errors, status=400)

    return HttpResponse(status=400)


@csrf_exempt
def roles(request):
    if request.method == 'GET':
        modules = Role.objects.all()
        serializer = RoleSerializer(modules, many=True)
        return JSONResponse(serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(data=data)
        if serializer.is_valid:
            serializer.save()
            return JSONResponse(serializer.data, status=201)

        else:
            return JSONResponse(serializer.errors, status=400)

    return HttpResponse(status=400)


@csrf_exempt
def priviliges(request):
    if request.method == 'GET':
        modules = Privilige.objects.all()
        serializer = PriviligeSerializer(modules, many=True)
        return JSONResponse(serializer.data, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PriviligeSerializer(data=data)
        if serializer.is_valid:
            serializer.save()
            return JSONResponse(serializer.data, status=201)

        else:
            return JSONResponse(serializer.errors, status=400)

    return HttpResponse(status=400)
