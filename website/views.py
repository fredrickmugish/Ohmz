from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about_page(request):
    return render(request, 'about.html')
def services_page(request):
    return render(request, 'services.html')
def contact_page(request):
    return render(request, 'contact.html')

def contact_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the message to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, 'Your message has been submitted successfully.')
        return redirect('contact')  

    return render(request, 'contact.html')

def consult_page(request):
    return render(request, 'consulting.html')
def cyber_page(request):
    return render(request, 'Cyber.html')
def domain_page(request):
    return render(request, 'domain_reg.html')
def grphics_page(request):
    return render(request, 'grphics_design.html')
def hosting_page(request):
    return render(request, 'hosting.html')
def network_page(request):
    return render(request, 'Netsecurity.html')
def system_page(request):
    return render(request, 'system_development.html')

