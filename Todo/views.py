from django.shortcuts import render
from .models import todoMaster
from django.http import HttpResponseRedirect


def todo(request):
    data = todoMaster.objects.all().order_by("-created_on")
    frontend_data = {
        'data': data,
    }
    return render(request, 'TodoApp.html', frontend_data)


def create_new(request):
    content = request.POST['content']
    if content != '':
        post_data = todoMaster.objects.create(content=content)

    return HttpResponseRedirect("/Todo/")


def delete_item(request, id):
    todoMaster.objects.get(id=id).delete()
    return HttpResponseRedirect("/Todo/")
