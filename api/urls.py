from django.urls import path, include
from django.contrib import admin
from . import api


urlpatterns = [
    path('account/', include('Account.urls')),
    path('blog/', include('blogapp.urls')),
    path('api/data/', api.data_view, name='api-data'),
]



