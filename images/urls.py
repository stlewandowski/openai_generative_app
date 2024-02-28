from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("results/", views.results, name="results"),
    path("img/<int:img_id>/", views.img, name="img"),
    path("about/", views.about, name="about"),
    path('all_details/', views.all_details, name='all_details')
]