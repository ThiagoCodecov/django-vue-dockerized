from rest_framework import routers
from apps.users.views import UserViewSet
from apps.git_providers.views import RepoLoad, CommitList

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
api.register(r'repos', RepoLoad)
api.register(r'commits', CommitList)
