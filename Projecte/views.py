from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

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


class SignUpView(CreateView):
    model = User
    template_name = 'Form.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
