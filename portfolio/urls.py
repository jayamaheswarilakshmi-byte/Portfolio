from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/ai-chat/", views.ai_chat_api, name="ai_chat_api"),
]