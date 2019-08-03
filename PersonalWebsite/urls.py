from django.conf.urls import url, include # Add include to the imports here
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('website.urls'))
]
