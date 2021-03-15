from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from apps.api import schema
from graphql_jwt_auth import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(schema=schema,graphiql=True))),
    path('', csrf_exempt(GraphQLView.as_view(schema=schema,graphiql=True))),
]


if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    except ImportError:
        pass
