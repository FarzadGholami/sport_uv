from django.urls import path

from .views import UvListView, UvDetailView

urlpatterns = [
    path('', UvListView.as_view(), name='uv_list'),
    path('<int:pk>/', UvDetailView.as_view(), name='uv_detail'),
]