from django.shortcuts import render
from rest_framework import generics
from .models import Account, Contact
from .serializers import AccountSerializer, ContactSerializer

# Create your views here.

class AccountAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
