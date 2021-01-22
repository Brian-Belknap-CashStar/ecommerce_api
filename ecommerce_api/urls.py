from django.conf.urls import include, url
from ecommerce_api.test.views import TestForContextHandler

urlpatterns = [
    url(r'^test/hello_world', TestForContextHandler.as_view(), name='hello_world'),
]
