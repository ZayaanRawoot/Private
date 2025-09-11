from django.contrib import admin
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact, Message, UniqueContactMessage
# Register your models here.

def send_email_to_contacts(modeladmin, request, queryset):
    subject = "A message from our team"
    message = "Hello! This is a custom message from the admin panel."
    from_email = "your_email@gmail.com"  # Make sure this matches your SMTP config

    # Get all selected emails
    recipient_list = list(queryset.values_list('email', flat=True))

    if recipient_list:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request, f"Email sent to {len(recipient_list)} contacts.")
    else:
        messages.warning(request, "No valid emails found.")


send_email_to_contacts.short_description = "Send email to selected contacts"


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    ordering = ['-timestamp']
    max_num = 4


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    inlines = [MessageInline]
    actions = [send_email_to_contacts]  # Add the custom action here

@admin.register(UniqueContactMessage)
class UniqueContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'timestamp']
    search_fields = ['email', 'message']