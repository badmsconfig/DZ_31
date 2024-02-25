from django.urls import path
from blogapp import views

app_name = 'blogapp'

#views.main_view()
urlpatterns = [
    path('', views.main_view, name='index'),
    path('post/<int:id>/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('anketa/', views.anketa, name='anketa'),
    path('search/', views.search, name='search'),
    path('create/', views.create_post, name='create'),
    path('contact/', views.contact_view, name='contact'),
    path('tag-list/', views.TagListView.as_view(), name='tag_list'),
    path('tag-detail/<int:pk>/', views.TegDetailView.as_view(), name='tag_detail'),
    path('tag-create/', views.TagCreateView.as_view(), name='tag_create'),

]


