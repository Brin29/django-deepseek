from django.urls import path
from . import views

# router=routers.DefaultRouter()

urlpatterns=[
    # path('', include(router.urls))
    path('', views.chatbot, name='chatbot')
]