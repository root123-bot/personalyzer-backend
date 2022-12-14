"""MiwaniPambeTz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from MiwaniPambeTz.Register import urls as register_urls
from MiwaniPambeTz.Customer import urls as customer_urls
from MiwaniPambeTz.User import urls as user_urls
from MiwaniPambeTz.api import urls as api_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^user/', include(user_urls)),
    url(r'^customer/', include(customer_urls)),
    url(r'^register/', include(register_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
With this you can serve the static media from Django when DEBUG = True (when you run on local computer) but you can let your web server configuration serve static media when you go to production and DEBUG = False
Sijui kama kuna umuhimu wa website yetu hii ya ku-disable mtu asione images... Koz ujue sisi tuna-frontend ko ni muhimu kwake ku-access images/static files.

if settings.DEBUT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''



