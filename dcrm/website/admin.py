from django.contrib import admin
from .models import Record  # Model wird importiert, muss mit makemigration und dann migrate in die DB geschoben werden

# Register your models here.
admin.site.register(Record)   # wird im Admin-Interface registriert und kann dort angezeigt werden
