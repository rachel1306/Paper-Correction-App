from django.shortcuts import render
from rest_framework import viewsets
from .models import Correction
from .serializers import CorrectionSerializer
import json.decoder
import jsonify
from django.http import HttpResponse
# Create your views here.
result=[
    {
        'code': "789000",
        'name': "lsd"
    }
]

class CorrectionView(viewsets.ModelViewSet):
    queryset=Correction.objects.all()
    serializer_class=CorrectionSerializer

    def register(self,request):
        if request.method=='POST':
            request_data=request.data
            request_data=json.loads(request_data)
            code=request_data['code']
            name=request_data['name']
            new_obj={
                'code': code,
                'name': name
            }
            result.append(new_obj)
        #respone=f'Hi ${name}, in flask'
            return jsonify(result)
        elif request.method=='GET': 
            code=request.query_params['code']
            name=request.query_params['name']
            return jsonify({'code':code,'name':name})
