from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

from dashboard.forms import SignUpForm, LoginForm

# Create your views here.

class RegistrationView(View):
    
    def get(self, request):
        form = SignUpForm()
        return render(request, 'dashboard/register.html', {'form': form} )

    def post(self, request):
        try:
            form = SignUpForm(request.POST)
            print("form", form)
            if form.is_valid():
                user = form.save()
                return redirect('dashboard:login')
            return render(request, 'dashboard/register.html', {'form': form, 'error_message': 'invaild data'})
        except Exception as e:
            print("error--------------", str(e))
            return render(request, 'dashboard/register.html', {'form': form, 'error_message': str(e)})

class LoginView(View):
    
    def get(self, request):
        try:
            form = LoginForm()
            return render(request, 'dashboard/login.html',{'form': form} )
        except Exception as e:
            return render(request, 'dashboard/login.html', {'form': form, 'error_message': str(e)})

    def post(self, request):
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=password)
                if user is not None :
                    login(request, user)
                    return redirect('dashboard:dashboard')
                else:
                    error_message = "Invalid username or password."
                    return render(request, 'dashboard/login.html', {'form': form, 'error_message':error_message})
            else:
                return render(request, 'dashboard/login.html', {'form': form, 'error_message': 'invaild data'})
        except Exception as e:
            return render(request, 'dashboard/login.html', {'form': form, 'error_message': str(e)})

class DashboardView(View):
    
    def get(self, request):
        
        # data_labels = ["Label1", "Label2", "Label3"]
        # data_values = [10, 20, 30]

        # Pass the data to the template
        # context = {
        #     'labels': data_labels,
        #     'values': data_values,
        # }
        # return render(request, 'dashboard/dashboard_student_home.html',context )
        return render(request, 'dashboard/dashboard_student_home.html' )

class CandidateView(View):
    
    def get(self, request):

        return render(request, 'dashboard/dashboard_admin_candidate.html')

class VotersView(View):
    
    def get(self, request):

        return render(request, 'dashboard/dashboard_voters.html')

class CreatePollView(View):
    
    def get(self, request):

        return render(request, 'dashboard/dashboard_poll.html')
