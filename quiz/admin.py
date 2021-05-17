from django.contrib import admin
from .models import QandA,Subject,Score
# Register your models here.
admin.site.register(QandA)
admin.site.register(Subject)
admin.site.register(Score)