from django import forms

from cars.models import Brend

class ContactMassageForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label="Name")
    email = forms.EmailField(max_length=255, required=True, label="Email")
    subject = forms.CharField(max_length=255, required=True, label="Subject")
    message = forms.CharField(widget=forms.Textarea, max_length=500, required=True, label="Message")

class SearchBrandForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Brend.objects.all())

class BookingPersonalForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label="First Name")
    last_name = forms.CharField(max_length=255, required=True, label="Last Name")
    email = forms.EmailField(max_length=255, required=True, label="Your Email")
    phone = forms.CharField(max_length=20, required=True, label="Phone Number")

class BookingCarForm(forms.Form):
    pickup_date = forms.DateField(required=True, label="Pickup Date")
    pickup_time = forms.TimeField(required=True, label="Pickup Time")
    age = forms.IntegerField(required=True, label="Age")
    address = forms.CharField(max_length=255, required=True, label="Address")
    request=forms.CharField(max_length=255, required=True, label="Special Request")

class NewsletterForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True, label="Your Email")

class PaymentMethodForm(forms.Form):
    method=forms.CharField(max_length=255, required=True, label="Payment Method")

