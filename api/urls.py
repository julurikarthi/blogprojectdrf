from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('account/', include('Account.urls')),
    path('blog/', include('blogapp.urls')),
    path('api/data/', data_view, name='api-data'),
]



