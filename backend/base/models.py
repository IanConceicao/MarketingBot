from django.conf import settings
from django.db import models

# Create your models here


class Prompt(models.Model):
    text = models.TextField()
    imageUrl = models.ImageField(blank=True, default="")
    impressionCount = models.IntegerField(
        default=0
    )  # Total number of impressions of this prompt


class Action(models.Model):
    text = models.TextField()
    redirect = models.TextField(blank=True, default="")
    prompt = models.ForeignKey(
        Prompt, models.SET_NULL, blank=True, null=True, related_name="+"
    )
    nextPrompt = models.ForeignKey(
        Prompt, models.SET_NULL, blank=True, null=True, related_name="+"
    )
    clickEventCount = models.IntegerField(
        default=0
    )  # Total number of clicks on this action


class Message(models.Model):
    prompt = models.ForeignKey(
        Prompt, models.CASCADE, blank=True, null=True, related_name="+"
    )
    actions = models.ManyToManyField(Action, related_name="+")
    time = models.DateTimeField(auto_now=True)



class User(models.Model):
    id = models.TextField(primary_key=True)
    messages = models.ManyToManyField(
        Message, related_name="+", blank=True
    )  # List of prompts served
    impressions = models.ManyToManyField(
        Prompt, related_name="+", blank=True
    )  # List of prompts viewed
    clickEvents = models.ManyToManyField(
        Action, related_name="+", blank=True
    )  # List of actions clicked
