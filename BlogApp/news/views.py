from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def news_home(request):
    return render(request,'news/news_home.html')

def about_us(request):
    return render(request,'news/abot_us.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hi')
    else:
        form = UserCreationForm()
    return render(request, 'news/registr_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hi')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login_user.html', {'form': form})


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')

def hi(request):
    return render(request,'news/main.html')