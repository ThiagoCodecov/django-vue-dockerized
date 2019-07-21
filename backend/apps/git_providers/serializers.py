from rest_framework import serializers

from apps.git_providers.models import Commit, Repo, CommitStatus


class CommitStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitStatus
        fields = ('message',  'status_context', 'current_status')


class CommitSerializer(serializers.ModelSerializer):
    parents = serializers.SerializerMethodField()
    statuses = CommitStatusSerializer(many=True, read_only=True)

    def get_parents(self, obj):
        return [o.parent_sha for o in obj.parents.all()]

    class Meta:
        model = Commit
        fields = ('sha', 'parents', 'statuses')


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repo
        fields = ('slug', )
