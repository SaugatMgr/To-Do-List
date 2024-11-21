from django.http import JsonResponse
from django.views.generic import TemplateView, View
from django.db import transaction
from django.shortcuts import render

from apps.tasks.forms import ContactForm
from apps.tasks.models import Task
from utils.helpers import send_email


class HomePageView(TemplateView):
    template_name = "tasks/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context


def add_task(request):
    if request.method == "POST":
        with transaction.atomic():
            ajax_request = request.headers.get("X-Requested-With")

            if not ajax_request == "XMLHttpRequest":
                return JsonResponse(
                    {"success": False, "error": "Invalid request"}, status=400
                )
            task_name = request.POST.get("task_name")
            if task_name:
                task = Task.objects.create(title=task_name)
                return JsonResponse(
                    {
                        "success": True,
                        "task_id": task.id,
                        "task_name": task.title,
                        "message": "Task added.",
                    }
                )
            else:
                return JsonResponse(
                    {"success": False, "message": "Task name is required."}
                )
    return JsonResponse({"success": False, "message": "Invalid request."})


def manage_task(request, task_id):
    if request.method == "POST":
        with transaction.atomic():
            ajax_request = request.headers.get("X-Requested-With")

            if not ajax_request == "XMLHttpRequest":
                return JsonResponse(
                    {"success": False, "error": "Invalid request"}, status=400
                )
            task = Task.objects.get(id=task_id)
            action = request.POST.get("action")

            if action == "complete":
                task.completed = True
                task.save()
                return JsonResponse(
                    {"success": True, "message": "Task marked as completed."}
                )

            elif action == "edit":
                new_name = request.POST.get("task_name")
                if new_name:
                    task.title = new_name
                    task.save()
                    return JsonResponse(
                        {
                            "success": True,
                            "new_name": new_name,
                            "message": "Task updated.",
                        }
                    )

            elif action == "delete":
                task.delete()
                return JsonResponse({"success": True, "message": "Task deleted."})

        return JsonResponse({"success": False, "message": "Invalid action."})

    return JsonResponse(
        {"success": False, "message": "Method not allowed."}, status=405
    )


class ContactUsView(View):
    template_name = "contact/contact_us.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        initial_data = request.session.get("inquiry_data", {})
        form = ContactForm(initial=initial_data)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            ajax_request = request.headers.get("X-Requested-With")
            form = ContactForm(request.POST)

            if not ajax_request == "XMLHttpRequest":
                return JsonResponse(
                    {"success": False, "error": "Invalid request"}, status=400
                )
            if form.is_valid():
                form.save()
                send_email(form.cleaned_data)
                return JsonResponse(
                    {
                        "success": True,
                        "message": "Thank you for contacting us. We will get back to you soon.",
                    }
                )
            else:
                return JsonResponse({"errors": form.errors}, status=400)
