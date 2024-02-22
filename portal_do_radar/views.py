from django.shortcuts import render

def index(request):
    return render(request, 'portal_do_radar/index.html')
