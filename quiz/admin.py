from django.contrib import admin

# Register your models here.

from quiz.models import Question, Response


admin.site.register(Question)
admin.site.register(Response)