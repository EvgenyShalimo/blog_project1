from django.shortcuts import render, redirect
from .forms import UsersForm, Users
from django.views.generic import DetailView

def index (request):
    return render(request,'blog/index.html')

class NewsDetailView(DetailView):
    model = Users
    template_name = 'blog/user_room.html'
    context_object_name = 'article'


def contakts (request):
    return render(request,'blog/kontakts.html')

def contact(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
        else:
            error = 'error'


    form = UsersForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request,'blog/forma.html',data)

def list_user(request):
    listUser = Users.objects.all()
    return render(request,'blog/user_list.html', {'listUser': listUser} )


