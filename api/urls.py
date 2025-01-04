from django.urls import path, include
from django.contrib import admin
from blogapp import viewsnew


urlpatterns = [
    path('account/', include('Account.urls')),
    path('blog/', include('blogapp.urls')),
     path('api/data/', viewsnew.data_view, name='api-data'),
]



