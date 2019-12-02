from django.shortcuts import render

import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addition_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers_data = json.loads(request.body)
            print(numbers_data)
            try:
                a = int(numbers_data['A'])
                b = int(numbers_data['B'])
            except ValueError:
                response = JsonResponse({'error': 'The data entered is not numbers'})
                response.status_code = 400
                return response
            answer = a + b
            print("answer", answer)
            return JsonResponse({'answer': answer})
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers_data = json.loads(request.body)
            try:
                a = int(numbers_data['A'])
                b = int(numbers_data['B'])
            except ValueError:
                response = JsonResponse({'error': 'The data entered is not numbers'})
                response.status_code = 400
                return response
            answer = a - b
            print("answer", answer)
            return JsonResponse({'answer': answer})
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers_data = json.loads(request.body)
            try:
                a = int(numbers_data['A'])
                b = int(numbers_data['B'])
            except ValueError:
                response = JsonResponse({'error': 'The data entered is not numbers'})
                response.status_code = 400
                return response
            answer = a * b
            print("answer", answer)
            return JsonResponse({'answer': answer})
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response


@csrf_exempt
def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers_data = json.loads(request.body)
            try:
                a = int(numbers_data['A'])
                b = int(numbers_data['B'])
            except ValueError:
                response = JsonResponse({'error': 'The data entered is not numbers'})
                response.status_code = 400
                return response
            if b == 0:
                response = JsonResponse({'error': 'Division by zero'})
                response.status_code = 400
                return response
            else:
                answer = a / b
                print("answer", answer)
                return JsonResponse({'answer': answer})
        else:
            response = JsonResponse({'error': 'No data provided!'})
            response.status_code = 400
            return response

