from django.urls import path, include


from blogapp.views import  BlogView, PublicBlogView
from . import views


urlpatterns = [
    path('blogs/', BlogView.as_view() , name='blogs'),
    path('publicblogs/', PublicBlogView.as_view(), name='publicblogs'),
]



