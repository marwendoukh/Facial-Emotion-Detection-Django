from django.conf.urls import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from facialemotiondetection import views
from . import view

# import website.image_recognition.view as detect


admin.autodiscover()


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # ... your url patterns
]
