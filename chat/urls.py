from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.chat, name="home-chat"),
    path('<int:conversationId>/',
         views.chat_by_coversationId, name="chat_by_id"),
]
