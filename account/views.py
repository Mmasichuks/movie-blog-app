from django.shortcuts import render,redirect
from account.forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)
