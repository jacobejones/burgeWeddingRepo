from django.urls import path
from weddingApp import views

app_name = 'weddingApp'

urlpatterns = [

    path('',views.HomeView.as_view(),name='home'),
    path('rsvp/',views.RSVPCreateView.as_view(),name='rsvp'),
    path('info/',views.InfoView.as_view(),name='info'),
    path('gallery/',views.GalleryView.as_view(),name='gallery'),
    path('share/',views.ShareView.as_view(),name='share'),
    path('thanks/',views.ThanksView.as_view(),name='thanks'),

]
