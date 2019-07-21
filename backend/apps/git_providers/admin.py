from django.contrib import admin
from apps.git_providers.models import Commit, Repo, CommitParenthood, CommitStatus

# Register your models here.

admin.site.register(Commit)
admin.site.register(CommitParenthood)
admin.site.register(CommitStatus)
admin.site.register(Repo)
