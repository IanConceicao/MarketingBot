from django.urls import path
from . import views

urlpatterns = [
    path("", views.healthy),
    path("getAllUsers/", views.getAllUsers),
    path("getAllPrompts/", views.getAllPrompts),
    path("getAllActions/", views.getAllActions),
    path("getMessagesForUser/", views.getMessagesForUser),
    path("selectAction/", views.selectAction),
    path("uploadImage/", views.uploadImage),
    path("recordClickEvent/", views.recordClickEvent),
    path("recordImpression/", views.recordImpression),
]
