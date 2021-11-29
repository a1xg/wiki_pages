from django.urls import path
from . import views


urlpatterns = [
    path('create', views.PageCreateView.as_view()),
    path('pages/list', views.PageListView.as_view()),
    path('pages/<int:pk>', views.PageDetailView.as_view()),
    path(
        'pages/<int:pk>/versions/list',
        views.VersionListView.as_view()
    ),
    path(
        'pages/<int:page>/versions/<int:pk>',
        views.VersionDetailView.as_view()
    ),
    path(
        'pages/<int:pk>/versions/set-current',
        views.SetVersionView.as_view()
    )

]
