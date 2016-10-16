from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from cazier_auto.claim.serializers import UserSerializer, GroupSerializer
from cazier_auto.claim.serializers import ClaimSerializer
from cazier_auto.claim.models import Claim


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ClaimViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows Claims to be viewed or created.
    """
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


def home(request):
    return render(request, 'home.html', {})


def team(request):
    return render(request, 'team.html', {})


def about(request):
    return render(request, 'about.html', {})


def claim(request):
    return render(request, 'claim.html', {})
