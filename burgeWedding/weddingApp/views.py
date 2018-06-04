from django.shortcuts import render
from weddingApp.models import RSVP
from django.views.generic import (TemplateView,ListView,
                                   DetailView,CreateView,
                                   UpdateView,DeleteView)

# Create your views here.
class HomeView(TemplateView):
    template_name = 'weddingApp_home.html'

class RSVPView(TemplateView):
    template_name = 'weddingApp_rsvp.html'

class InfoView(TemplateView):
    template_name = 'weddingApp_info.html'

class GalleryView(TemplateView):
    template_name = 'weddingApp_gallery.html'

class ShareView(TemplateView):
    template_name = 'weddingApp_share.html'

class ThanksView(TemplateView):
    template_name = 'weddingApp_thanks.html'

class RSVPCreateView(CreateView):
    model = RSVP
    fields = "__all__"
