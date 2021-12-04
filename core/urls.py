import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from app.views import sample, cached_sample

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample', sample),
    path('cache', cached_sample),
    path('__debug__/', include(debug_toolbar.urls)),
]
