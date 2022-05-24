from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets, permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status


from django.http import HttpResponse, JsonResponse

#from django.http import HttpResponse
from ..core.models import Polity, Reference
from .serializers import UserSerializer, GroupSerializer, PolitySerializer, ReferenceSerializer, AlbumSerializer, Total_taxSerializer

from .models import Album, Track

#from .serializers import PolitySerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PolityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Polity.objects.all()
    serializer_class = PolitySerializer


@api_view(['GET', 'POST'])
def reference_list(request, format=None):
    """
    List all references, or create a new reference.
    """
    if request.method == 'GET':
        refs = Reference.objects.all()
        serializer = ReferenceSerializer(refs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = ReferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reference_detail(request, pk, format=None):
    """
    Retrieve, update or delete a reference.
    """
    try:
        ref = Reference.objects.get(pk=pk)
    except Reference.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReferenceSerializer(ref)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ReferenceSerializer(ref, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ref.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def album_list(request, format=None):
    """
    List all Albums, or create a new Album.
    """
    if request.method == 'GET':
        refs = Album.objects.all()
        serializer = AlbumSerializer(refs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, pk, format=None):
    """
    Retrieve, update or delete a album.
    """
    try:
        ref = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(ref)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = AlbumSerializer(ref, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ref.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# def VarDetail():
#     pass


# def VarList(request):
#     return HttpResponse('<h1>Hello World from api.</h1>')


# class PolityList(generics.ListCreateAPIView):
#     queryset = Polity.objects.all()
#     serializer_class = PolitySerializer
#     pass


# class PolityDetail(generics.RetrieveDestroyAPIView):
#     queryset = Polity.objects.all()
#     serializer_class = PolitySerializer
