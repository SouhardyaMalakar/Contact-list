from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('add-contact/', views.addcontact, name='add-contact'),
    path('delete-contact/<str:pk>', views.deletecontact, name='delete-contact'),
    path('edit-contact/<str:pk>', views.editcontact, name='edit-contact'),
    path('contact-profile/<str:pk>', views.contactprofile, name='contact-profile')
]