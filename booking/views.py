from django.shortcuts import render
from django.views import generic



def get_booking(request):
    return render(request, 'booking/base.html')
