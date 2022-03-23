from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # PostViewSet,
    #PostSearchView
    PostListView
)

# router = DefaultRouter(trailing_slash=False)
# router.register('posts', PostViewSet)


urlpatterns = [
    path(r'post/list', PostListView.as_view())
]
# urlpatterns += router.urls

