from rest_framework.response import Response
from rest_framework.decorators import api_view
from base import services


@api_view(["Get"])
def healthy(request):
    return Response("Healthy")


@api_view(["Get"])
def getAllUsers(request):
    return services.getAllUsers(request)


@api_view(["Get"])
def getAllActions(request):
    return services.getAllActions(request)


@api_view(["Get"])
def getAllPrompts(request):
    return services.getAllPrompts(request)


@api_view(["GET"])
def getMessagesForUser(request):
    if not request.query_params.get("userId"):
        return Response("Expects 'userId' integer", status=400)
    return services.getMessagesForUser(request)


@api_view(["POST"])
def selectAction(request):
    if not request.data.get("userId") or not request.data.get("actionId"):
        return Response("Expects 'userId' and 'actionId' integers", status=400)
    return services.selectAction(request)


@api_view(["POST"])
def uploadImage(request):
    if not request.FILES.get("image"):
        return Response("Expects an image file with key 'image'", status=400)
    return services.uploadImage(request)


@api_view(["POST"])
def recordClickEvent(request):
    if not request.data.get("userId") or not request.data.get("actionId"):
        return Response("Expects 'userId' and 'actionId' integers", status=400)
    return services.recordClickEvent(request)


@api_view(["POST"])
def recordImpression(request):
    if not request.data.get("userId") or not request.data.get("promptId"):
        return Response("Expects 'userId' and 'actionId' integers", status=400)
    return services.recordImpression(request)
