from django.urls import path
from .views import home,thank_you,send_test_email,contact

urlpatterns = [
    path('', home, name='home'),              # Home page (GET)
    path('contact/', contact, name='contact'),# Contact form submission (POST)
    path('thank-you/', thank_you, name='thank_you'),
    path('send-email/', send_test_email, name='send_email'),
]
