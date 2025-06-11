from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .swapi_client import SWAPIClient
import json

@csrf_exempt
@require_http_methods(["GET"])
def search_people(request):
    """
    Proxy endpoint to search for Star Wars characters
    Example: /api/swapi/people/?search=skywalker
    """
    search_query = request.GET.get('search', '')
    client = SWAPIClient()
    result = client.search_people(search_query)
    return JsonResponse(result)
