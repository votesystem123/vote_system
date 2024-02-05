from django.shortcuts import render
from django.views import View

# Create your views here.

class RegistrationView(View):
    
    def get(self, request):

        return render(request, 'dashboard/register.html' )

class LoginView(View):
    
    def get(self, request):

        return render(request, 'dashboard/login.html' )

class DashboardView(View):
    
    def get(self, request):
        data_labels = ["Label1", "Label2", "Label3"]
        data_values = [10, 20, 30]

        # Pass the data to the template
        context = {
            'labels': data_labels,
            'values': data_values,
        }
        return render(request, 'dashboard/dashboard_admin_home.html',context )

class CandidateView(View):
    
    def get(self, request):

        return render(request, 'dashboard/dashboard_admin_candidate.html')

class VotersView(View):
    
    def get(self, request):

        return render(request, 'dashboard/dashboard_voters.html')

class CreatePollView(View):
    
    def get(self, request):

        return render(request, 'dashboard/dashboard_poll.html')
