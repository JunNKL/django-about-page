from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if username == "admin" and password == "admin123":
            return JsonResponse({
                "message": "Login successful",
                "username": username,
                "status": "success"
            })

        return JsonResponse({
            "message": "Invalid username or password",
            "status": "failed"
        }, status=401)

    return JsonResponse({
        "message": "Only POST method is allowed"
    }, status=405)


@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        return JsonResponse({
            "message": "Logout successful",
            "status": "success"
        })

    return JsonResponse({
        "message": "Only POST method is allowed"
    }, status=405)