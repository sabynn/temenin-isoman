from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sign_in(request):
    if request.method != "POST":
        return JsonResponse({"result": "Must use POST method!"})

    if not request.body:
        return JsonResponse({"result": "Must provide request body!"})

    print(request.body)

    username = request.POST['username']
    password = request.POST['password']

    if not username or not password:
        return JsonResponse({"result": "Must provide username and password!"})

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"result": "success"})
    else:
        return JsonResponse({"result": "failed"})


@csrf_exempt
def sign_out(request):
    if request.method != "POST":
        return JsonResponse({"result": "Must use POST method!"})

    if not request.user.is_authenticated:
        return JsonResponse({"result": "Not yet authenticated!"})

    logout(request)
    return JsonResponse({"result": "success"})


@csrf_exempt
def get_dummy(request):
    if request.method != "POST":
        return JsonResponse({"result": "Must use POST method!"})

    if not request.user.is_authenticated:
        return JsonResponse({"data": "unauthorized"})

    return JsonResponse({"data": "wowowowowoww"})
