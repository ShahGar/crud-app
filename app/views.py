from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

from .forms import UserForm
from .models import User

# Create your views here.


def home(request):
    users = User.objects.all()
    for user in users:
        print(user.id)
    return render(request, 'home.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'create.html', {'form': form})


def delete_user(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)#delete form table and databasae too
        user.delete()
        return redirect('home')
    else:
        return redirect('home')


def update(request, user_id):
    user = get_object_or_404(User, pk=user_id)#if erro get_object_or_404 handel the server
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():#if form is valid than save the databasae
            form.save()
            return redirect('home') 
    else:
        form = UserForm(instance=user)
        #constant username and email
        form.fields['email'].widget.attrs['readonly'] = True
        form.fields['username'].widget.attrs['readonly'] = True
    return render(request, 'update.html', {'form': form})