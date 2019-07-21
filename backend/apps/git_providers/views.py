import logging

from rest_framework import viewsets
from apps.git_providers.models import Commit
from apps.git_providers.tasks import load_commits
from apps.git_providers.serializers import CommitSerializer, RepoSerializer


# Create your views here.


class CommitList(viewsets.ModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer


class RepoLoad(viewsets.ModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = RepoSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        load_commits.delay(repoid=obj.id)
