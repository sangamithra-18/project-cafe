from django.shortcuts import render,redirect 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Feedback

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Feedback.objects.create(name=name, email=email, message=message)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('/')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error'}, status=400)
            messages.error(request, 'Please fill out all fields.')
            return redirect('/')
    return render(request, 'index.html')    
# Create your views here.
