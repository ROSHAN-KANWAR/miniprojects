from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request,'blog/home.html')
  #about  
def about(request):
    return render(request,'blog/about.html')

#contact
def contact(request):
  return render(request, 'blog/contact.html')



  #logout
def logout(request):
  return render(request, 'blog/logout.html')



  #login
def login(request):
  if not request.user.is_authenticated:
    if request.method =='POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
          uname = fm.cleaned_data['username']
          upass = fm.cleaned_data['password']
          user = authenticate(username=uname, password=upass)
          if user is not None:
              login(request, user)
              messages.success(request, 'Logged in successfully !!')
              return HttpResponseRedirect('/dashboard/')
    else:
      fm = LoginForm()
    return render(request, 'enroll/login.html', {'form': fm})
  else:
    return HttpResponseRedirect('/dashboard/')




  #dashboard
def dashboard(request):
  return render(request, 'blog/dashboard.html')




#signup
def user_signup(request):
  if request.method == "POST":
    form=SignUpForm(request.POST)  
    if form.is_valid():
      messages.success(request, 'Congratulation !! You have become an Author.')
      form.save()    
  else:
      form = SignUpForm()
  return render(request, 'blog/signup.html',{'form':form})
 
