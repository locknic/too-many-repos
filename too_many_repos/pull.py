from typing import List

from too_many_repos.models.wrapped_repo import WrappedRepo


def repos_pull(repos: List[WrappedRepo], force_dirty: bool = False, force_merge: bool = False) -> None:
    for repo in repos:
        if repo.commits_behind_remote == 0:
            print(repo.name + ' [Success] : already up to date')
        elif repo.has_changes and not force_dirty:
            print(repo.name + ' [Failed] : repo is dirty')
        elif repo.commits_ahead_remote and not force_merge:
            print(repo.name + ' [Failed] : repo is ahead of master')
        else:
            try:
                repo.git.pull()
                print(repo.name + ' [Success]')
            except Exception:
                print(repo.name + ' [Failed] : pull error')
