from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact, Message, UniqueContactMessage
from django.db import IntegrityError
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Create or get existing contact
            contact_obj, created = Contact.objects.get_or_create(
                email=data['email'],
                defaults={'name': data['name'], 'phone': data['phone']}
            )

            # Update name/phone if changed
            if not created:
                contact_obj.name = data['name']
                contact_obj.phone = data['phone']
                contact_obj.save()

            # Add message to Message table (limit to 4 messages per user)
            Message.objects.create(
                contact=contact_obj,
                service=data['service'],
                message=data['message']
            )

            # Keep only latest 4 messages
            messages = contact_obj.messages.order_by('-timestamp')
            if messages.count() > 4:
                for m in messages[4:]:
                    m.delete()

            # Add to UniqueContactMessage (skip duplicates)
            try:
                UniqueContactMessage.objects.create(
                    name=data['name'],
                    email=data['email'],
                    phone=data['phone'],
                    service=data['service'],
                    message=data['message'],
                    subscribe=data.get('subscribe',False)
                )
            except IntegrityError:
                pass
            
            return redirect('thank_you')
    else:
        form = ContactForm()

    # Always render the form (with errors if any)
    return render(request, 'home.html', {'form': form})


def home(request):
    form = ContactForm()
    return render(request, 'home.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def send_test_email(request):
    send_mail(
        "Hello from Django",
        "This is a test email.",
        "your_email@gmail.com",  # Replace with your Gmail address
        ["recipient@example.com"],  # Replace with recipient address
        fail_silently=False
    )
    return HttpResponse("Email sent successfully!")
