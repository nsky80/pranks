from django.contrib import admin
from .models import Feedback, QuesSubject, SubSeries, Paper
# Register your models here.

admin.site.register(Feedback)
admin.site.register(QuesSubject)
admin.site.register(SubSeries)
admin.site.register(Paper)