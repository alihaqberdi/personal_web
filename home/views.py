from django.shortcuts import render, redirect
from django.views import View
from .models import Blog, Contact
from django.contrib import messages
# Create your views here.


class IndexView(View):
    def get(self, request):
        sss = Blog.objects.all()
        context = {
            'profile': sss[0]
        }
        return render(request, 'index.html', context)
    def post(self, request):
        try:
            sender = Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                text=request.POST['text']
            )
            sender.save()
            messages.success("Message Sent Successfully")
        except:
            messages.error('Message Was Not Sent')
        return redirect('home')