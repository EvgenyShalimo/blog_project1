from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users
from django.views.generic import DetailView
from BlogApp.celery import app as celery_app
from BlogApp.tasks import add_numbers
from django.http import HttpResponse
from celery.result import AsyncResult

def index (request):
    return render(request,'blog/home.html')



class NewsDetailView(DetailView):
    model = Users
    template_name = 'blog/user_room.html'
    context_object_name = 'room'


def contakts (request):
    return render(request,'blog/kontakts.html')


def contact(request):
    error = ''
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
        else:
            error = 'Форма была не верной'
    form = UsersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/forma.html', data)





def list_user(request):
    listUser = Users.objects.all()
    return render(request,'blog/user_list.html', {'listUser': listUser} )

def test_celery(request):
    result = add_numbers.delay(2, 3)
    return HttpResponse(f'Result: {result.id}')


