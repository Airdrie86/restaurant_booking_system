from django.shortcuts import render
from django.views import generic
from .models import Post


def get_booking(request):
    return render(request, 'booking/base.html')
