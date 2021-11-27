from django.urls import path
from . import views


urlpatterns = [
    path('create', views.PageCreateView.as_view()),
    path('list', views.PagesListView.as_view()),
    path('page/<int:pk>', views.PageDetailView.as_view()),
    path(
        'page/<int:pk>/versions/list',
        views.VersionsListView.as_view()
    ),
    path(
        'page/<int:page>/versions/<int:pk>',
        views.VersionDetailView.as_view()
    ),

]
