from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers
from django.core.mail import send_mail
from django.conf import settings


def new_sub(request):
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) #we do not want to save just yet
        if NewsUsers.objects.filter(email=instance.email).exists():
            print('your email Already exists in our database')
        else:
            instance.save()
            print('your email has been submitted to our database')
            send_mail('Thanks for Subscribing!', 'Welcome to my Blog! Check your inbox for any new blog posts!', settings.DEFAULT_FROM_EMAIL,[instance.email], fail_silently=False)
            return HttpResponseRedirect('/')
    else:
        form = NewsUserForm()
    context = {'form':form}
    template = "subscribe.html"
    return render(request, template, context)
