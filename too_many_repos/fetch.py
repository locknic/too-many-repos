from typing import List

from too_many_repos.models.wrapped_repo import WrappedRepo


def repos_fetch(repos: List[WrappedRepo]) -> None:
    for repo in repos:
        try:
            repo.git.fetch()
            print(repo.name + " : [Success]")
        except Exception:
            print(repo.name + " : [Failed]")
