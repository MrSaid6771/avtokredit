from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django.contrib.auth import login, authenticate


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
def sign_up(request):
    first_name = request.POST.get('first_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    usr = User.objects.create_user(username=username, password=password, first_name=first_name)
    usr.save()
    if usr is not None:
        login(request, usr)
        return Response(' successfully signed up ')
    else:
        return Response(status=404)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
def log_in(request):
    first_name = request.POST.get('first_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    usr = authenticate(username=username, password=password, first_name=first_name)
    if usr is not None:
        login(request, usr)
        return Response(' successfully loged in ')
    else:
        return Response('there is some issues in your log in please check ')

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
def calculate(request):
    user = request.POST.get('user')
    amount = request.POST.get('amount')
    request_credit = Credit.objects.create_user(username=user, amount=amount)
    return Response('Success uploaded')

@api_view(['GET'])
def credit(request):
    c = Credit.objects.all()
    ser = CreditSerializer(c, many=True)
    return Response(ser.data)