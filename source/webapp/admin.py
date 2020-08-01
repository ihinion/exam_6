from django.contrib import admin
from webapp.models import Entry

# superuser
# login: admin
# password: admin
admin.site.register(Entry)
