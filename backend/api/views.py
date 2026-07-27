from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    post_data = request.body
    print(post_data)
    return JsonResponse ({'name':'Brayann','info':'djangoRest','age':20})


