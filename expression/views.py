from django.shortcuts import render
from django.http import JsonResponse
import json

def evaluate_expression(request):
    if request.method == 'GET':
    	return render(request, 'expression/index.html')
    if request.method == 'POST':
        try:
            #import pdb;pdb.set_trace()
            data = json.loads(request.body)
            expression = data.get('expression', '')

            result = eval(expression)
            return JsonResponse({'result': result})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

