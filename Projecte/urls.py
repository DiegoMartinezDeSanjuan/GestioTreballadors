from django.urls import path

from Projecte.views import HomeView, ProjectsView, ProjectDetail, WorkersView, WorkerDetail

urlpatterns = [
    path('home', HomeView.as_view()),
    path('projects', ProjectsView.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='ProjectDetail'),
    path('workers', WorkersView.as_view()),
    path('workers/<int:pk>/', WorkerDetail.as_view(), name='WorkerDetail'),

]
