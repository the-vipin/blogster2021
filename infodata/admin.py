from django.contrib import admin
from infodata.models import FAQs


# Register your models here.
class FaqAdmin(admin.ModelAdmin):
    list_display = ('Que', 'Quetype')

admin.site.register(FAQs,FaqAdmin)