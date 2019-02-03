from typing import List

from git import Repo


def repo_dirty_status(repo: Repo) -> str:
    dirty = repo.is_dirty(untracked_files=True)

    if dirty:
        return 'dirty'
    else:
        return 'clean'


def repo_commits_ahead_remote(repo: Repo) -> int:
    branch = repo.active_branch
    commits_ahead = repo.iter_commits(str(branch.tracking_branch().commit) + ".." + str(branch.commit))
    count_ahead = sum(1 for c in commits_ahead)

    return count_ahead


def repo_commits_behind_remote(repo: Repo) -> int:
    branch = repo.active_branch
    commits_behind = repo.iter_commits(str(branch.commit) + ".." + str(branch.tracking_branch().commit))
    count_behind = sum(1 for c in commits_behind)

    return count_behind


def repo_commits_ahead_master(repo: Repo) -> int:
    branch = repo.active_branch
    last_master_commit = repo.merge_base(branch, repo.heads.master)
    commits_ahead = repo.iter_commits(str(last_master_commit[0]) + ".." + str(branch.commit))
    count_ahead = sum(1 for c in commits_ahead)

    return count_ahead


def repo_commits_behind_master(repo: Repo) -> int:
    branch = repo.active_branch
    last_master_commit = repo.merge_base(branch, repo.heads.master)
    commits_ahead = repo.iter_commits(
        str(last_master_commit[0]) + ".." + str(repo.heads.master.tracking_branch().commit),
    )
    count_ahead = sum(1 for c in commits_ahead)

    return count_ahead


def repo_status(repo: Repo) -> None:
    repo_name = repo.remote().url.replace('git@github.com:', '').replace('.git', '')
    print(
        f'{repo_name} [{repo.active_branch}] [{repo_dirty_status(repo)}] '
        f'[> {repo_commits_ahead_remote(repo)}] [< {repo_commits_behind_remote(repo)}] '
        f'[> {repo_commits_ahead_master(repo)}] [< {repo_commits_behind_master(repo)}]',
    )
    # uncommitted changes
    # vs remote


def repos_status(repos: List[Repo]) -> None:
    for repo in repos:
        repo.git.fetch()
        repo_status(repo)
