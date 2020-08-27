from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from facility.models import post
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

class SearchView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):

        word = request.GET['word']
        post_list = post.objects.filter(
        Q(name__icontains=word)|Q(address__icontains=word)|Q(description__icontains=word)
        ).distinct() #중복을 제거한다.
        context = []
        for i in post_list:
            param={}
            param['id']=i.id
            param['name']=i.name
            param['is_toilet']=i.is_toilet
            param['is_elibator']=i.is_elibator
            param['is_parking']=i.is_parking
            param['is_tuck']=i.is_tuck
            param['is_tuck']=i.is_tuck
            param['is_helper']=i.is_helper
            param['description']=i.description
            param['latitude']=i.latitude
            param['longitude']=i.longitude
            param['star']=i.star
            context.append(param)
        return Response({'msg': 'success', 'object_list': context})