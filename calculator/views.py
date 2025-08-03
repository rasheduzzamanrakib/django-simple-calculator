from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

def index(request):
    """Render the calculator homepage"""
    return render(request, 'calculator/index.html')

@csrf_exempt
@require_http_methods(["POST"])
def calculate(request):
    """Handle calculation requests"""
    try:
        data = json.loads(request.body)
        expression = data.get('expression', '')
        
        # Basic security check - only allow safe mathematical operations
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression):
            return JsonResponse({'error': 'Invalid characters in expression'}, status=400)
        
        # Replace display multiplication symbol with actual multiplication
        expression = expression.replace('×', '*')
        
        # Evaluate the expression safely
        result = eval(expression)
        return JsonResponse({'result': result})
        
    except (ValueError, SyntaxError, ZeroDivisionError) as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Calculation error'}, status=400)
