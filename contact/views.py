from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.

def home(request):
    # Show the home page with the form
    form = ContactForm()
    return render(request, 'home.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Or do whatever processing you need
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')