
from django.urls import path
from todo_drf.api.views import TaskDetailApiView, TaskListApiView,ApiOverView

urlpatterns = [
    path("", ApiOverView.as_view()),
    path("tasks/", TaskListApiView.as_view()),
    path("tasks/<int:pk>/", TaskDetailApiView.as_view()),
]
