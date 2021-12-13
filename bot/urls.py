from django.urls import path
from . import views

urlpatterns = [
    path('bot', views.start_chatbot),
    path('devop', views.start_devopchatbot),
    path('', views.start_devopchatbot)

]