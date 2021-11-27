from django.urls import path
from . import views


urlpatterns = [
    path('create', views.PageCreateView.as_view()),
    path('pages/list', views.PagesListView.as_view()),
    path('pages/detail/<int:pk>', views.PageDetailView.as_view()),
    path(
        'pages/detail/<int:pk>/versions/list',
        views.VersionsListView.as_view()
    ),
    path(
        'pages/detail/<int:page>/versions/<int:pk>',
        views.VersionDetailView.as_view()
    ),
    path('pages/detail/<int:page>/versions/<int:pk>/set-current',
         views.SetCurrentVersionView.as_view()
    )

]
