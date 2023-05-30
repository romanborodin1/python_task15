# Файл servers_and_stats/urls.py

from django.urls import path
from .views import ServerViewSet, ServerDetailView, ServerAddView, ServerShortViewSet, ServerShortDetailView, \
    ServerShortAddView, ServerStatusViewSet, ServerStatusAddView, ServerStatusDetailView


urlpatterns = [
    path('servers/', ServerViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
    path('short_servers/', ServerShortViewSet.as_view()),
    path('short_servers/<int:pk>', ServerShortDetailView.as_view()),
    path('short_servers/add', ServerShortAddView.as_view()),
    path('servers/status/', ServerShortViewSet.as_view()),
    path('servers_status/', ServerStatusViewSet.as_view()),
    path('servers_status/<int:pk>', ServerStatusDetailView.as_view()),
    path('servers_status/add', ServerStatusAddView.as_view()),
]
