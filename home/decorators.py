from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='user').exists():
            return redirect('Home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()

            for item in group:
                # print('group '+ item.name )
                if item.name in allowed_roles:

                    return view_func(request, *args, **kwargs)
                # else:
                # 	messages.error(request,'You are not authorized to view this page')

                # 	return redirect('Inchargehome')
                # return HttpResponse('You are not authorized to view this page')
            messages.error(request, 'You are not authorized to view this page')
            return redirect('Home')

        return wrapper_func
    return decorator
