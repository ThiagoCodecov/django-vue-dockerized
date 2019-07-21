import requests


class GithubFetcher(object):

    def __init__(self, username, access_token):
        self.username = username
        self.access_token = access_token

    def fetch_commit_statuses(self, commit):
        # /repos/:owner/:repo/commits/:ref/statuses
        slug = commit.repo.slug
        url = f'https://api.github.com/repos/{slug}/commits/{commit.sha}/statuses'
        return requests.get(url, auth=(self.username, self.access_token)).json()

    def list_master_commits(self, repo):
        slug = repo.slug
        url = f'https://api.github.com/repos/{slug}/commits'
        return requests.get(url, auth=(self.username, self.access_token)).json()
