from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from slack_messages import views

# urlpatterns = patterns('',)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webhook', views.webhook, name='webhook'),
]