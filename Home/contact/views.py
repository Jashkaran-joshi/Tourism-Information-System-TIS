from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save data to the Contact model
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Replace 'contact' with your contact page URL name

    return render(request, 'contact.html')  # Replace with your actual template name