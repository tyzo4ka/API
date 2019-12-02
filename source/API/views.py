import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def is_a_number(data):
    try:
        a = int(data['A'])
        b = int(data['B'])
    except ValueError:
        return False
    return True


@csrf_exempt
def addition_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            numbers_data = json.loads(request.body)
            print(numbers_data)
            if is_a_number(numbers_data):
                answer = int(numbers_data["A"]) + int(numbers_data["B"])
                print("answer", answer)
                return JsonResponse({'answer': answer})
            else:
                response = JsonResponse({'error': 'The data entered is not numbers'})
                response.status_code = 400
                return response
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

