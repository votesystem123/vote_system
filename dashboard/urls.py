from django.urls import path
from dashboard.views import RegistrationView, LoginView, DashboardView, CandidateView, CreatePollView, VotersView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'dashboard'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('candidates/', CandidateView.as_view(), name='candidates'),
    path('createpoll/', CreatePollView.as_view(), name='create_poll'),
    path('voters/', VotersView.as_view(), name='voters'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)