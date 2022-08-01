from django.shortcuts import render
from django.views import generic
from .models import Uv


class UvListView(generic.ListView):
    model = Uv
    template_name = 'uvs/uv_list.html'
    context_object_name = 'uvs'


class UvDetailView(generic.DetailView):
    model = Uv
    template_name = 'uvs/uv_detail.html'
