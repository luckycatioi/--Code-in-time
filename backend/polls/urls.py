
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # example: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # example: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<str:json_data>/update/',views.update,name='update'),
    path('clear_all/',views.clear,name='clear'),
    path('get_all_people/',views.get_all_people,name='get_all_people')
]