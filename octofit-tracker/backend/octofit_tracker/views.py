from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": "https://glorious-space-train-grwjqgw75x6cp5x-8000.app.github.dev/api/",
    })
