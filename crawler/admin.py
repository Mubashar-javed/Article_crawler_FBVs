from django.contrib import admin
from .models import Article

# Registering our models here. Only the registered models will be shown
# in the admin panel


admin.site.register(Article)
