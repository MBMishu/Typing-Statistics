from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.base_user import BaseUserManager
from django.http import Http404

from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives


import json
import datetime
import csv


from admin_dashboard.models import *
from .forms import *
from .decorators import *


def Userindex(request):

    list = PDFFile.objects.all().order_by('-id')[:1]

    # print(list)
    context = {
        'list': list,
    }
    return render(request, 'index.html', context)


@login_required(login_url='user_Handlelogin')
def save_progress(request):
    last_pdf = PDFFile.objects.last()

    guest_user = GuestUser.objects.get(user=request.user)
    # print(last_pdf)
    if request.method == 'POST':
        data = json.loads(request.body)

        typing_time = data.get('typingTime')
        inactive_time = data.get('inactiveTime')
        word_count = data.get('wordCount')
        char_count = data.get('charCount')

        form_data = FormData.objects.create(

            user=guest_user,
            pdf_name=last_pdf,
            typingTime=typing_time,
            inactiveTime=inactive_time,
            wordCount=word_count,
            charCount=char_count
        )
        form_data.save()
        return redirect('Home')
    else:
        return redirect('Home')


@unauthenticated_user
def UserHandlelogin(request):

    form = UserloginForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.groups.filter(name='user').exists():
            request.session.set_expiry(300)
            login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect('Home')

        else:
            messages.error(
                request, 'You are not authorized')
            return redirect('user_Handlelogin')

    context = {'form': form

               }
    return render(request, 'interview/login.html', context)


def UserHandlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('user_Handlelogin')


@unauthenticated_user
def UserHandleregister(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            raw_password = User.objects.make_random_password()
            user.set_password(raw_password)
            user.save()

            fullname = request.POST['fullname']
            email = request.POST['username']

            group = Group.objects.get(name='user')
            user.groups.add(group)

            GuestUser.objects.create(
                user=user,
                name=fullname,
                email=email,
                role=group,
                password=raw_password
            )

            subject = "Website SignIn credentials"
            to_mail = email
            subject, from_email, to = f'{subject}', f'{email}', f'{to_mail}'
            cc_email = ['a.t.m.masum.billah@g.bracu.ac.bd']
            text_content = ''
            html_content = f'<p>Name :  {fullname}</p>\
                <p>Username :  {email}</p>\
                <p>Password :  {raw_password}</p>'

            try:
                msg = EmailMultiAlternatives(
                    subject, text_content, from_email, [to], cc=cc_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                print("send mail...........")
            except:
                print('mail does not send to -', to_mail)

            messages.success(request, 'Account was created for ',
                             email)
            return redirect('user_Handlelogin')
        else:
            messages.error(request, form.errors)
    context = {'form': form
               }
    return render(request, 'interview/register.html', context)
