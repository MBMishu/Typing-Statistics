from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


import json
import datetime
import csv
# Create your views here.
from .models import *
from .forms import *
from .decorators import *


@login_required(login_url='admin_Handlelogin')
def index(request):
    user = AdminUser.objects.get(user=request.user)
    form = AdminUserUpdateForm(instance=user)

    if request.method == 'POST':
        form = AdminUserUpdateForm(
            request.POST, request.FILES, instance=user)
        if form.is_valid():

            # img_file = request.FILES.get('file')
            # user.image = img_file
            # user.save()
            user = form.save()
            messages.success(request, "user info is updated.")

            return redirect('admin_home')

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'dashboard/home.html', context)


@unauthenticated_user
def Handlelogin(request):
    form = UserloginForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.groups.exists() and user.is_staff:
                login(request, user)

                messages.success(request, "Successfully Logged In.")
                return redirect('admin_home')
            else:
                messages.error(
                    request, 'You are not authorized')
                return redirect('admin_Handlelogin')
        else:
            messages.error(request, "Invalid Credentials!")

    context = {'form': form

               }
    return render(request, 'dashboard/login.html', context)


def Handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('admin_Handlelogin')


@login_required(login_url='admin_Handlelogin')
@allowed_users(allowed_roles=['admin'])
def upload_pdf(request):
    user = AdminUser.objects.get(user=request.user)
    list = PDFFile.objects.all().order_by('-date_created')

    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['file']
            if pdf_file.name.endswith('.pdf'):
                form.save()
                messages.success(request, "NEW PDF file Uploaded.")
                return redirect('upload_pdf')
            else:
                # form.add_error('file', 'Please upload a PDF file.')
                messages.warning(request, 'Please upload a PDF file.')
    else:
        form = PDFFileForm()

    context = {
        'user': user,
        'form': form,
        'list': list,
    }
    return render(request, 'dashboard/upload_pdf.html', context)


@login_required(login_url='admin_Handlelogin')
@allowed_users(allowed_roles=['admin'])
def PdfDelete(request, pk):
    list = PDFFile.objects.get(id=pk)
    list.delete()
    messages.error(request, "Deleted.")
    return redirect('upload_pdf')


@login_required(login_url='admin_Handlelogin')
@allowed_users(allowed_roles=['admin'])
def UserList(request):
    user = AdminUser.objects.get(user=request.user)

    group = Group.objects.get(name='user')
    group_user_list = group.user_set.all()
    list = GuestUser.objects.filter(
        role=group).order_by('-id')

    context = {
        'user': user,
        'list': list,
        'group_user_list': group_user_list,
    }

    return render(request, 'dashboard/RegisterdParticipants.html', context)


# @login_required(login_url='admin_Handlelogin')
# @allowed_users(allowed_roles=['admin'])
def details(request, pk):
    user = GuestUser.objects.get(id=pk)
    list = FormData.objects.filter(user=user.id)
    context = {
        'user': user,
        'list': list,
    }
    return render(request, 'dashboard/details.html', context)
