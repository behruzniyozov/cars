from django.urls import path

from cars.views import (
        index, 
        contact_message_handler, 
        contact_message_handler,
        search_car_handler,
        about,
        booking,
        car,
        booking_car,
        booking_personal,
        payment_method,
        newsletter,
        contact,
        detail,
        services,
        team,
        testimonial
        ) 

app_name = "cars"


urlpatterns = [
    path("index/", index, name="index"),
    path("contactmessage/", contact_message_handler, name="contactmessage"),
    path("search/", search_car_handler, name="search-car"),
    path("about/", about, name="about"),
    path("booking/", booking, name="booking"),
    path("booking_personal/", booking_personal, name="booking_personal"),
    path("booking_car/", booking_car, name="booking_car"),
    path("newsletter/", newsletter, name="newsletter"),
    path("payment_method/", payment_method, name="payment_method"),
    path("car/", car, name="car"),
    path("contact/", contact, name="contact"),
    path("detail/", detail, name="detail"),
    path("services/", services, name="services"),
    path("team/", team, name="team"),
    path("testimonial/", testimonial, name="testimonial"),
]