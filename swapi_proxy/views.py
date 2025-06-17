from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .swapi_client import SWAPIClient
import json
import requests
from urllib.parse import urljoin

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

@csrf_exempt
@require_http_methods(["GET"])
def proxy_swapi(request, path):
    """
    Proxy endpoint for all SWAPI resources
    Example: /api/swapi/planets/1/
    """
    # Remove any trailing slash
    path = path.rstrip('/')
    
    # Build the SWAPI URL
    swapi_base_url = 'https://swapi.dev/api/'
    swapi_url = urljoin(swapi_base_url, path + '/')
    
    # Add query parameters if any
    if request.GET:
        query_string = request.META.get('QUERY_STRING', '')
        if query_string:
            swapi_url = f"{swapi_url}?{query_string}"
    
    try:
        # Make the request to SWAPI with SSL verification disabled
        # In production, you should properly configure SSL certificates instead of disabling verification
        response = requests.get(swapi_url, verify=False)
        response.raise_for_status()
        
        # Return the JSON response with proper CORS headers
        return JsonResponse(response.json(), safe=False)
        
    except requests.RequestException as e:
        # Log the error for debugging
        print(f"Error fetching {swapi_url}: {str(e)}")
        # Return a generic error message to the client
        return JsonResponse(
            {"error": "Unable to fetch data from SWAPI. Please try again later."},
            status=502  # Bad Gateway
        )
