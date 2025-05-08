from django.shortcuts import render

def show_home(request):
    return render(request, 'home.html')

def show_contacts(request):
    return render(request, 'contacts.html')