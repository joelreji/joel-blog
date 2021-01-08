from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def new_sub(request):
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
        if NewsUsers.objects.filter(email=instance.email).exists():
            print('your email Already exists in our database')
            messages.error(request, 'This email is already subscribed, please enter another.')
            return HttpResponseRedirect('/subscribe/subscribe')
        else:
            instance.save()
            print('your email has been submitted to our database')
            send_mail('Thanks for Subscribing!', 'Welcome to my Blog! Check your inbox for any new blog posts!', settings.DEFAULT_FROM_EMAIL,[instance.email], fail_silently=False)
            messages.success(request, 'Thanks for subscribing! Check you email for confirmation email.')
            return HttpResponseRedirect('/subscribe/subscribe')
    else:
        form = NewsUserForm()
    context = {'form':form}
    template = "subscribe.html"
    return render(request, template, context)
