import logging
from config.celery import app
from apps.git_providers.facade import GithubFetcher
from apps.git_providers.models import Repo, Commit, CommitParenthood, CommitStatus


@app.task(bind=True)
def load_commits(self, repoid):
    logging.info("LADSDASDSADASDUHASDUAH")
    repo = Repo.objects.get(id=repoid)
    token = '3b3110c7a42db729ff64a110d960320e86c20bfd'
    username = 'ThiagoCodecov'
    fetcher = GithubFetcher(username, token)
    ids = []
    for commit_data in fetcher.list_master_commits(repo):
        commit, _ = Commit.objects.get_or_create(
            sha=commit_data['sha'],
            repo=repo
        )
        for p in commit_data['parents']:
            cp, _ = CommitParenthood.objects.get_or_create(
                commit=commit,
                parent_sha=p['sha']
            )
        load_commit_status.delay(commit.id)
        ids.append(commit.id)
    return ids


@app.task(bind=True)
def load_commit_status(self, commit_id):
    logging.info("load_commit_status")
    commit = Commit.objects.get(id=commit_id)
    token = '3b3110c7a42db729ff64a110d960320e86c20bfd'
    username = 'ThiagoCodecov'
    fetcher = GithubFetcher(username, token)
    ids = []
    for commit_data in fetcher.fetch_commit_statuses(commit):
        cs, _ = CommitStatus.objects.update_or_create(
            ext_id=commit_data['id'],
            commit=commit,
            status_context=commit_data['context'],
            defaults=dict(
                message=commit_data['description'],
                current_status=commit_data['state']
            )
        )
    return ids
