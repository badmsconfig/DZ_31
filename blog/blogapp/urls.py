from django.urls import path
from blogapp import views

app_name = 'blogapp'

#views.main_view()
urlpatterns = [
    path('', views.main_view, name='index'),
    path('create/', views.create_post, name='create'),
    path('post/<int:id>/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('anketa/', views.anketa, name='anketa'),
    path('search/', views.search, name='search'),
]


