from django.urls import path
from .views import home,contact,thank_you

urlpatterns = [
    path('', home, name='home'),              # Home page
    path('contact/', contact, name='contact'), # Contact form submission
    path('thank-you/',thank_you, name='thank_you')
]
