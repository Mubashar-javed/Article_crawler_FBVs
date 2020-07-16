from . import views
from django.urls import path



# in this file we define all the urls where our different templates will be shown 


app_name = 'crawler' # app_name is necessary if you  have more than one apps.

urlpatterns = [
    
    path('', views.index, name='index'),  # http://localhost:8000/
    path('search/', views.Search, name='search'),  # http://localhost:8000/search/
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
]
