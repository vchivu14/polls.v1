from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.index, name="index"),
    path("createquestion/", views.createq, name="createq"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/addOpt/", views.addOpt, name="addOpt"),
    path("<int:question_id>/delete/", views.deleteq, name="deleteq"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]