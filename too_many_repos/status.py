from typing import List

from git import Repo


def repo_dirty_status(repo: Repo) -> str:
    dirty = repo.is_dirty(untracked_files=True)

    if dirty:
        return 'dirty'
    else:
        return 'clean'


def repo_status(repo: Repo) -> None:
    print(f'[{repo.active_branch}] [{repo_dirty_status(repo)}] - {repo.remote().url}')
    # uncommitted changes
    # vs remote


def repos_status(repos: List[Repo]) -> None:
    for repo in repos:
        repo_status(repo)
