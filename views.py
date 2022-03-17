import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from grpc import Status
from matplotlib import artist
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import Article_serializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
# Create your views here.

# create an article list.
# the function are written in the views

# class based views.


class ArticleApiView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = Article_serializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Article_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):

    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(satus=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get.object(id)
        serializer = Article_serializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get.object(id)
        serializer = Article_serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get.object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# function based api
# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = Article_serializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = Article_serializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Article_serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return response(serializer.data, status=status.HTTP_201_CREATED)
    return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(satus=404)
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(satus=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     serializer = Article_serializer(article)
    #     return JsonResponse(serializer.data)
    if request.method == 'GET':
        serializer = Article_serializer(article)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = Article_serializer(article, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        serializer = Article_serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
