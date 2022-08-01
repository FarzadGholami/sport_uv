from django.urls import path

from .views import UvListView

urlpatterns = [
    path('', UvListView.as_view(), name='uv_list')
]