# Packages
from django.urls import re_path, include

# Modules
from . import views

urlpatterns = [
    re_path(
        r"^api/prices/btc/",
        views.get,
    ),
]
