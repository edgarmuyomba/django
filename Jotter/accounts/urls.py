from django.urls import path, include
from .views import SignUp

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name="signup"),
]