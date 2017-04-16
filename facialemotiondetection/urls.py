from django.conf.urls import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views
#import website.image_recognition.views as detect


admin.autodiscover()


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # ... your url patterns
]
