from rest_framework.response import Response
from api.serailizers import PromptSerializer, UserSerailizer, ActionSerailizer
from base.models import Prompt, Action, User


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

    user.prompts.add(action.nextPrompt)
    user.save()

    return Response("Action has been selected")


def getUser(request):
    data = request
    user = User.objects.get(pk=data["userId"])
    serializer = UserSerailizer(user)
    return Response(serializer.data)


def getAllUsers(request):
    users = User.objects.all()
    return Response(UserSerailizer(users, many=True).data)


def getAllActions(request):
    actions = Action.objects.all()
    return Response(ActionSerailizer(actions, many=True).data)


def getAllPrompts(request):
    prompts = Prompt.objects.all()
    return Response(PromptSerializer(prompts, many=True).data)


def getMessagesForUser(request):
    # Get a message for a prompt
    data = request.query_params
    user = User.objects.get(pk=data["userId"])

    prompt_list = []
    for prompt in user.prompts.all():
        # For each prompt our user has, add its associate actions
        prompt_dict = PromptSerializer(prompt).data

        actions = Action.objects.filter(prompt=prompt.id)
        actions_list = ActionSerailizer(actions, many=True).data
        prompt_dict["text"] = prompt_dict["text"].replace("USER_NAME", user.pk)
        prompt_dict["actions"] = actions_list

        prompt_list.append(prompt_dict)

    return Response(prompt_list)
