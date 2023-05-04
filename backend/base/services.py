from rest_framework.response import Response
from api.serailizers import (
    PromptSerializer,
    UserSerializer,
    ActionSerializer,
    MessageSerializer,
)
from base.models import Prompt, Action, User, Message


def uploadImage(request):
    objs = Prompt.objects.exclude(imageUrl__exact="")

    for obj in objs:
        obj.imageUrl.delete()
        obj.imageUrl = request.FILES.get("image")
        obj.save()

    return Response("Image was uploaded")


def recordClickEvent(request):
    data = request.data
    user = User.objects.get(pk=data["userId"])
    action = Action.objects.get(pk=data["actionId"])

    # Check if duplicate click
    if not user.clickEvents.filter(pk=action.pk).exists():
        # Record that user clicked on it
        user.clickEvents.add(action)

        # Increment the actions click count
        action.clickEventCount += 1

        user.save()
        action.save()

    return Response("Recorded action")


def recordImpression(request):
    data = request.data
    user = User.objects.get(pk=data["userId"])
    prompt = Prompt.objects.get(pk=data["promptId"])

    # Check if duplicate impression
    if not user.impressions.filter(pk=prompt.pk).exists():
        # Record user had the impression
        user.impressions.add(prompt)

        # Increment the prompts impression count
        prompt.impressionCount += 1

        user.save()
        prompt.save()

    return Response("Recorded impression")


def selectAction(request):
    data = request.data
    user = User.objects.get(pk=data["userId"])
    action = Action.objects.get(pk=data["actionId"])
    nextPrompt = action.nextPrompt

    if nextPrompt:
        newMessage = Message.objects.create(prompt=nextPrompt)
        newMessage.save()  # Necessary before calling add()
        newMessage.actions.add(*Action.objects.filter(prompt=nextPrompt.pk))
        user.messages.add(newMessage)
        user.save()

    return Response("Action has been selected")


def getUser(request):
    data = request
    user = User.objects.get(pk=data["userId"])
    serializer = UserSerializer(user)
    return Response(serializer.data)


def getAllUsers(request):
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append(user.pk)
    return Response(user_list)


def getAllActions(request):
    actions = Action.objects.all()
    return Response(ActionSerializer(actions, many=True).data)


def getAllPrompts(request):
    prompts = Prompt.objects.all()
    return Response(PromptSerializer(prompts, many=True).data)


def getMessagesForUser(request):
    data = request.query_params
    user = User.objects.get(pk=data["userId"])

    messages = user.messages.all().order_by("time")
    message_list = MessageSerializer(messages, many=True).data
    for message in message_list:
        message["prompt"]["text"] = message["prompt"]["text"].replace(
            "USER_NAME", user.pk
        )

    return Response(message_list)


def createUser(request):
    data = request.data
    userId = data["userId"]

    # Make user
    newUser = User(id=userId)

    # Get initial objs
    initialPrompt = Prompt.objects.get(pk=1)
    initialActions = Action.objects.filter(prompt=initialPrompt)

    # Make and set user's initial message
    initialMessage = Message.objects.create(prompt=initialPrompt)
    initialMessage.actions.add(*initialActions)
    newUser.save()  # Needed before we can do an add()
    newUser.messages.add(initialMessage)

    newUser.save()
    initialMessage.save()

    return Response("Created user {}".format(userId))
