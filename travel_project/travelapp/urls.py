
from django.urls import path

from travelapp import views

urlpatterns = [
    path('',views.demo,name="demo"),
    # path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('result/',views.result,name="result")
]