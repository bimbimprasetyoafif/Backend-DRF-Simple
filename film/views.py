from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from django.http import Http404

from .serializers import FilmSerializer, GambarSerializer, Film, Gambar

class FilmList(APIView):
    serializer_class = FilmSerializer
    content = {}

    def get_queryset(self):
        temp = Film.objects.all()
        return temp

    def get(self, request):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        self.content["result"] = serializer.data
        return Response(self.content, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        data = request.data
        if serializer.is_valid():
            serializer.create(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilmDetail(APIView):
    serializer_class = FilmSerializer
    content = {
                'status': 'Not Found'
        }


    def get_object(self, pk):
        temp = Film.objects.get(pk=pk)
        return temp  
    
    def get(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            serializer = self.serializer_class(snippet)
            if serializer == None:
                return Response(self.content, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:        
            return Response(self.content, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer_class(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        print(request.data)
        file_serializer = GambarSerializer(data=request.data)
    
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GambarList(APIView):
    serializer_class = GambarSerializer
    content = {}

    def get_queryset(self):
        temp = Gambar.objects.all()
        return temp

    def get(self, request):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        self.content["result"] = serializer.data
        return Response(self.content, status=status.HTTP_200_OK)

class GambarDetail(APIView):
    serializer_class = GambarSerializer
    content = {}


    def get_object(self, pk):
        temp = Gambar.objects.get(pk=pk)
        return temp  
    
    def get(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            serializer = self.serializer_class(snippet)
            if serializer == None:
                return Response(self.content, status=status.HTTP_200_OK)
            else:
                self.content["result"] = serializer.data
                return Response(self.content, status=status.HTTP_200_OK)
        except:        
            return Response(self.content, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)