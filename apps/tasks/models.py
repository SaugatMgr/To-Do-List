from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["completed", "-created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
