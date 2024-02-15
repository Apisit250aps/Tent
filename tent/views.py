from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders

from django.db.models import Sum

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def register(request):
    http_status = HTTP_200_OK
    message = ""
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']

    if User.objects.filter(username=username).count() > 0:
        message = "username is exist!"
        http_status = HTTP_400_BAD_REQUEST

    elif User.objects.filter(email=email).count() > 0:
        message = "email is exist!"
        http_status = HTTP_400_BAD_REQUEST
    else:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        if user:
            http_status = HTTP_201_CREATED
        else:
            http_status = HTTP_400_BAD_REQUEST

    return Response(status=http_status, data={
        "message": message
    })


@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def login(request):
    http_status = HTTP_200_OK
    username = request.data['username']
    password = request.data['password']

    user = authenticate(
        username=username,
        password=password
    )
    if user is not None:
        if user.is_active:
            http_status = HTTP_202_ACCEPTED
            login(request, user)
        else:
            http_status = HTTP_406_NOT_ACCEPTABLE
    else:
        http_status = HTTP_400_BAD_REQUEST

    return Response(status=http_status)

