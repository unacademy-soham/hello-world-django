from django.http import JsonResponse


def test_api(request):
    return JsonResponse({
        "message": "I have been deployed"
    }, status=200)
