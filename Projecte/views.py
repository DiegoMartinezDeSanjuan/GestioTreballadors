from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
from Projecte.models import Project, Worker


class HomeView(TemplateView):
    template_name = "Home.html"


class ProjectsView(ListView):
    model = Project
    paginate_by = 5
    template_name = "Projects.html"


class ProjectDetail(DetailView):
    model = Project
    template_name = "ProjectDetail.html"


class WorkersView(ListView):
    model = Worker
    paginate_by = 20
    template_name = "Workers.html"


class WorkerDetail(DetailView):
    model = Worker
    template_name = "WorkersDetail.html"
