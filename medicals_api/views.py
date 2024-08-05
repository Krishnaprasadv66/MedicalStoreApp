from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from medicals.forms import medicineForm
from medicals.models import login_details,signup_details,medicine_details
from .serializers import medicalsSerializer
from django.shortcuts import get_object_or_404





# SIGNUP PAGE

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)




# LOGIN PAGE


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please enter valid username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)




# CRUD SECTION......



# ADD MEDICINE


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_medicine(request):
    form = medicineForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



# VIEW MEDICINES


@api_view(['GET'])
@permission_classes((AllowAny,))
def list_medicines(request):
    products = medicine_details.objects.all()
    serializer = medicalsSerializer(products, many=True)
    return Response(serializer.data)




# EDIT MEDICINE DETAILS


@api_view(['PUT'])
@permission_classes(([IsAuthenticated]))
def edit_data(request, pk):
    product = get_object_or_404(medicine_details, pk=pk)
    form = medicineForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = medicalsSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    


# DELETE DATA


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_data(request, pk):
    try:
        product = medicine_details.objects.get(pk=pk)
    except medicine_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")
    


