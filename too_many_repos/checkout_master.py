from typing import List

from git import CheckoutError

from too_many_repos.models.wrapped_repo import WrappedRepo


def repos_checkout_master(repos: List[WrappedRepo], force_dirty: bool = False, force_unpushed: bool = False) -> None:
    for repo in repos:
        if repo.is_master:
            print(repo.name + ' [Success] : already master')
        elif repo.has_changes and not force_dirty:
            print(repo.name + ' : [Failed] : repo is dirty')
        elif repo.commits_ahead_remote and not force_unpushed:
            print(repo.name + ' : [Failed] : unpushed commits')
        else:
            try:
                repo.git.checkout('master')
                print(repo.name + ' : [Success]')
            except CheckoutError:
                print(repo.name + ' : [Failed] : checkout error')
