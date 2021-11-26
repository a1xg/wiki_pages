from django.urls import path
from . import views


urlpatterns = [
    path('create', views.WikiPageCreateView.as_view()),
    path('list', views.WikiPagesListView.as_view()),
    path('page/<int:pk>', views.WikiPageDetailView.as_view()),
    path('page/<int:pk>/versions', views.PageVersionsListView.as_view()),
    path('page/<int:page>/version/<int:pk>', views.PageVersionDetailView.as_view()),
]
