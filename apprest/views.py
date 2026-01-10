from django.shortcuts import render
from .models import Workers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import WorkerSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
# from djangorest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User
from .permissions import IsUser, IsStaff, IsAdmin

# Create your views here.
# @permission_classes([IsAuthenticated])
# @api_view(["GET"])
# def viewone(request):
#     w = Workers.objects.all()
#     serializer = WorkerSerializer(w,many = True) 
#     return Response(serializer.data,
#                     status = status.HTTP_200_OK )   

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def viewone(request):
    user = request.user
    # serializer = UserSerializer(user,many = True) 
    serializer = UserSerializer(user) 
    return Response(serializer.data,
                    status = status.HTTP_200_OK )   

@api_view(["POST"])
def post_data(request):
    s = UserSerializer(data = request.data)
    print(s)
    if s.is_valid():
        
        s.save()
        return Response({"message":"User registered Successfully"},
                        status = status.HTTP_201_CREATED)
    else:
        print(s.errors)

        return Response(status= status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT','DELETE'])
def methods(request, pk):
    try:
        user = Workers.objects.get(pk=pk)
    except Workers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = WorkerSerializer(user)
        return Response(serial.data)
    
    elif request.method == 'PUT':
        s = WorkerSerializer(user, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['POST'])
# def login_authentication(request):
#     if request.method == "POST": 
#         username = request.POST.get("username")   #this should be request.data.get() not post coz DRF requires request.data not post
#         password = request.POST.get("password")   # request.post will be empty in DRF
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             token = Token.objects.create(user=user)
#             return Response({"message": "Login successful"},
#                             {"token": str(token)}, 
#                             status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# def login_authentication_check(request):
#     token = Token.objects.create(user=request.user)
#     print(token.key)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_role(request):
    user = request.user

    if user.is_superuser:
        role = "admin"
    elif user.is_staff:
        role = "staff"
    else:
        role = "user"

    return Response({
        "username": user.username,
        "role": role
    })


@api_view(["GET"])
@permission_classes([IsAuthenticated,IsUser ])
def user_dashboard(request):
    return Response({
        "role" : "user",
        "username" : request.user.username,
        "email": request.user.email
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated,IsStaff ])
def staff_dashboard(request):
    return Response({
        "role" : "staff",
        "username" : request.user.username
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated,IsAdmin ])
def admin_dashboard(request):
    return Response({
        "role" : "admin",
        "username" : request.user.username
    })


