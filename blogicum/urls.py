from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('pages.urls')),  # ← مهم: صفحات about و rules مباشرة في الجذر
]