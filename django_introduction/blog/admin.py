from django.contrib import admin

# Register your models here.
from .models import Article

admin.site.register(Article)  # 把module注册到admin