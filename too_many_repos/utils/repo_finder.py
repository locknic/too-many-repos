import os
from typing import List

from git import Repo


def find_all_repos_paths(root: str) -> List[str]:
    repo_paths = []
    for (dirpath, dirnames, filenames) in os.walk(root):
        if '.git' in dirnames:
            repo_paths.append(os.path.abspath(dirpath))
    return repo_paths


def find_top_repos_paths(dirpath: str) -> List[str]:
    repo_paths = []
    itemnames = os.listdir(os.path.abspath(dirpath))

    if '.git' in itemnames:
        repo_paths.append(os.path.abspath(dirpath))
    else:
        for item in itemnames:
            item_path = os.path.join(dirpath, item)
            if os.path.isdir(item_path):
                repo_paths.extend(find_top_repos_paths(item_path))

    return repo_paths


def find_top_repos(dirpath: str) -> List[Repo]:
    return convert_paths_to_repos(find_top_repos_paths(dirpath))


def convert_paths_to_repos(repo_paths: List[str]) -> List[Repo]:
    repos = []
    for repo_path in repo_paths:
        repo = Repo(repo_path)
        if not repo.bare:
            repos.append(repo)
    return repos
