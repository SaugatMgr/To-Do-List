from django.urls import path

from apps.tasks.views import ContactUsView, HomePageView, add_task, manage_task

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tasks/add/", add_task, name="add_task"),
    path("tasks/<int:task_id>/", manage_task, name="manage_task"),
    path("contact/", ContactUsView.as_view(), name="contact"),
]
