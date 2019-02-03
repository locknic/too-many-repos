from typing import List

from too_many_repos.models.wrapped_repo import WrappedRepo


def repo_dirty_status(repo_stats: WrappedRepo) -> str:
    if repo_stats.has_changes:
        return 'dirty'
    else:
        return 'clean'


def repo_status(repo: WrappedRepo) -> None:
    repo_name = repo.name
    branch = repo.active_branch
    dirty_status = repo_dirty_status(repo)
    ahead_remote = repo.commits_ahead_remote
    behind_remote = repo.commits_behind_remote
    ahead_master = repo.commits_ahead_master
    behind_master = repo.commits_behind_master

    print(
        f'{repo_name} [{branch}] [{dirty_status}] '
        f'[{ahead_remote}] [{behind_remote}] [{ahead_master}] [{behind_master}]',
    )


def repos_status(repos: List[WrappedRepo]) -> None:
    for repo in repos:
        repo.git.fetch()
        repo_status(repo)
