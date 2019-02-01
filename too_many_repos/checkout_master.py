from typing import List

from git import CheckoutError
from git import Repo


def repo_checkout_master(repo: Repo) -> None:
    repo.git.checkout('master')


def repos_checkout_master(repos: List[Repo]) -> None:
    for repo in repos:
        try:
            repo_checkout_master(repo)
            print(repo.remote().url + ' : SUCCESS')
        except CheckoutError:
            print(repo.remote().url + ' : FAILED')
