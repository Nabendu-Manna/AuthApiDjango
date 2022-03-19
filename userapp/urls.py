from django.urls import path

from . import views
from .views import StudentViews as student
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    path('students', student.as_view()),
    path('gettoken', obtain_auth_token),
    path('details', views.details)
]