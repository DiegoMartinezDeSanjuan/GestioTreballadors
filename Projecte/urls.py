from django.contrib.auth.decorators import login_required
from django.urls import path, include

from Projecte.views import HomeView, ProjectsView, ProjectDetail, WorkersView, WorkerDetail, SignUpView

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('projects', login_required(ProjectsView.as_view()), name='projectList'),
    path('projects/<int:pk>/', login_required(ProjectDetail.as_view()), name='ProjectDetail'),
    path('workers', login_required(WorkersView.as_view()), name='workerList'),
    path('workers/<int:pk>/', login_required(WorkerDetail.as_view()), name='WorkerDetail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

]
