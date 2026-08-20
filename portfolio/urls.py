from django.urls import path
from . import views
from portfolio.views import test_email_view

urlpatterns = [
    path("", views.home, name="home"),
    path("api/ai-chat/", views.ai_chat_api, name="ai_chat_api"),
    path('test-email/', test_email_view, name='test_email'),
]