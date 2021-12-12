from django.urls import path
from django.urls.resolvers import URLPattern
from .views import JobAppView, JobAppThanksView

app_name = 'jobs'
urlpatterns = [
    path('job-app/', JobAppView.as_view(), name='app'),
    path('job-app/thanks/', JobAppThanksView.as_view(), name='thanks'),
]