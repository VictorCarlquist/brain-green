from django.contrib import admin
from farmer.models import Producer


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Producer, ProducerAdmin)

