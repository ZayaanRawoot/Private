from django import forms



class ContactForm(forms.Form):
    SERVICE_CHOICES = [
        ('cctv', 'CCTV Installation'),
        ('alarm', 'Alarm System'),
        ('access', 'Access Control'),
        ('monitoring', '24/7 Monitoring'),
    ]

    name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20,required=True)
    service = forms.ChoiceField(choices=SERVICE_CHOICES,required=True)
    message = forms.CharField(widget=forms.Textarea)
    subscribe = forms.BooleanField(
        label="Subscribe to our newsletter", 
        required=False
    )