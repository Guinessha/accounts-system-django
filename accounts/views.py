from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        visitors = User.objects.create_user(username, email, pass1)
        visitors.save()
        
        messages.success(request, 'Your account has been successfully create, Please login your account!')
        return redirect('signin')
    
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            name = user.username
            return render(request, 'home.html', {'name':name})
        
        else:
            messages.error(request, 'Bad Credentials!')
            return redirect('home')
    
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged is successfully')
    return redirect('home')
