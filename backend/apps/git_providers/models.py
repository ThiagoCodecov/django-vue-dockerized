import uuid
from django.db import models


class Repo(models.Model):
    slug = models.CharField(max_length=100)


class Commit(models.Model):
    repo = models.ForeignKey(Repo, on_delete=models.deletion.CASCADE)
    object_id = models.UUIDField(default=uuid.uuid4)
    sha = models.CharField(max_length=100)


class CommitParenthood(models.Model):
    commit = models.ForeignKey(Commit, on_delete=models.deletion.CASCADE, related_name='parents')
    parent_sha = models.CharField(max_length=100, null=True)


class CommitStatus(models.Model):
    commit = models.ForeignKey(Commit, on_delete=models.deletion.CASCADE, related_name='statuses')
    message = models.TextField()
    ext_id = models.CharField(max_length=100)
    status_context = models.CharField(max_length=100)
    current_status = models.CharField(max_length=30)
