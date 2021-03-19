from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from .models import Profile
from .forms import UserForm , ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('/products')

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request , 'registration/signup.html' , context)


@login_required(login_url='/accounts/login/')
def profile(request , slug):
    profile = get_object_or_404(Profile , slug=slug)
    context = {'profile' : profile}
    return render(request , 'profile.html' , context)


@login_required(login_url='login')
def edit_profile(request,slug):
    
    my_profile   = Profile.objects.get(user=request.user)
    user_form    =  UserForm(instance=request.user)
    profile_form =  ProfileForm(instance=my_profile)

    if request.method == 'POST':

           user_form     =  UserForm(request.POST,instance=request.user)
           profile_form  =  ProfileForm(request.POST,request.FILES,instance=my_profile)

           if user_form.is_valid() and profile_form.is_valid():
               user_form.save()
               new_profile_form = profile_form.save(commit=False)
               new_profile_form.user = request.user
               new_profile_form.save()
               return redirect('accounts:profile',slug=slug)
    
           else :
                user_form    =  UserForm(request.POST,instance=request.user)
                profile_form =   ProfileForm(request.POST,request.FILES,instance=my_profile)

    context = {'user_form':user_form,'profile_form':profile_form}
    return render(request,'edit_profile.html',context)    