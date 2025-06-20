from django.http import HttpResponse
from django.shortcuts import render

from cars.forms import ContactMassageForm, SearchBrandForm, BookingPersonalForm, BookingCarForm, NewsletterForm, PaymentMethodForm
from cars.models import Car, Brend
from common.models import ContactMessage
from users.models import CustomUser, Viewer

def index(request):
    cars = Car.objects.all()

    users = CustomUser.objects.filter(
        is_active=True,
        is_staff=True,
        is_superuser=False,
    )
    viewers = Viewer.objects.filter(
        is_active=True,
        is_staff=False,
        is_superuser=False,
    )

    return render(
        request=request,
        template_name='index.html',
        context={
            'cars': cars,
            'users': users,
            'viewers': viewers,
        }

    )

def contact_message_handler(request):
    if request.method == 'POST':
        form = ContactMassageForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return render(request, 'index.html')

    return HttpResponse('Invalid request method.')

def search_car_handler(request):
    if request.method == 'POST':
        form= SearchBrandForm(request.POST)

        if form.is_valid():
            brand = form.cleaned_data['brand']
            
            cars = Car.objects.filter(brand=brand)
            users = CustomUser.objects.filter(
                is_active=True,
                is_staff=False,
                is_superuser=True,
            )
            brands= Brend.objects.all()
            return render(
                request=request,
                template_name='index.html',
                context={
                    'cars': cars,
                    'users': users,
                    'brands': brands,
                }
            )

    return HttpResponse('Invalid request method.')

def about(request):
    form = SearchBrandForm(request.POST or None)

    cars = []
    users = []
    brands = Brend.objects.all()

    if request.method == 'POST' and form.is_valid():
        brand = form.cleaned_data['brand']
        cars = Car.objects.filter(brand=brand)
        users = CustomUser.objects.filter(
            is_active=True,
            is_staff=False,
            is_superuser=True,
        )

    return render(
        request=request,
        template_name='about.html',
        context={
            'form': form,
            'cars': cars,
            'users': users,
            'brands': brands,
        }
    )
def booking(request):
    return render(request, 'booking.html')

def car(request):
    return render(request, 'car.html')

def newsletter(request):
    if request.method == 'POST':
        form= NewsletterForm(request.Post)

        if form.is_valid():
            email = form.cleaned_data['email']

            # Save the email to the database or perform any other action
            return HttpResponse('Newsletter subscription successful!')
        
    return render(request, 'index.html', {'form': form})

def booking_personal(request):
    if request.method == 'POST':
        form = BookingPersonalForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            # Save the data to the database or perform any other action
            return HttpResponse('Booking personal information saved successfully!')

    else:
        form = BookingPersonalForm()

    return render(request, 'booking.html', {'form': form})

def booking_car(request):
    if request.method == 'POST':
        form = BookingCarForm(request.POST)

        if form.is_valid():
            pickup_date = form.cleaned_data['date']
            pickup_time = form.cleaned_data['time']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            request = form.cleaned_data['request']

            # Save the data to the database or perform any other action
            return HttpResponse('Booking car information saved successfully!')

    else:
        form = BookingCarForm()

    return render(request, 'booking.html', {'form': form})

def payment_method(request):
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)

        if form.is_valid():
            method = form.cleaned_data['method']

            # Save the data to the database or perform any other action
            return HttpResponse('Payment method saved successfully!')

    else:
        form = PaymentMethodForm()

    return render(request, 'booking.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')