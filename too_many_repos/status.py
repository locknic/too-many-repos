from typing import List
from typing import Tuple

from git import Commit
from git import Repo


def repo_dirty_status(repo: Repo) -> str:
    dirty = repo.is_dirty(untracked_files=True)

    if dirty:
        return 'dirty'
    else:
        return 'clean'


def repo_commits_ahead_remote(repo: Repo) -> int:
    branch = repo.active_branch
    return count_commits_ahead(repo, branch.tracking_branch().commit, branch.commit)


def repo_commits_behind_remote(repo: Repo) -> int:
    branch = repo.active_branch
    return count_commits_ahead(repo, branch.commit, branch.tracking_branch().commit)


def repo_commits_ahead_behind_master(repo: Repo) -> Tuple[int, int]:
    branch = repo.active_branch
    last_master_commit = repo.merge_base(branch, repo.heads.master)
    ahead_master = count_commits_ahead(repo, last_master_commit[0], branch.commit)
    behind_master = count_commits_ahead(repo, last_master_commit[0], repo.heads.master.tracking_branch().commit)
    return ahead_master, behind_master


def count_commits_ahead(repo: Repo, starting_commit: Commit, ending_commit: Commit) -> int:
    commits_ahead = repo.iter_commits(str(starting_commit) + ".." + str(ending_commit))
    count_ahead = sum(1 for c in commits_ahead)

    return count_ahead


def repo_status(repo: Repo) -> None:
    repo_name = repo.remote().url.replace('git@github.com:', '').replace('.git', '')
    branch = repo.active_branch
    dirty_status = repo_dirty_status(repo)
    ahead_remote = repo_commits_ahead_remote(repo)
    behind_remote = repo_commits_behind_remote(repo)
    ahead_master, behind_master = repo_commits_ahead_behind_master(repo)

    print(
        f'{repo_name} [{branch}] [{dirty_status}] '
        f'[{ahead_remote}] [{behind_remote}] [{ahead_master}] [{behind_master}]',
    )


def repos_status(repos: List[Repo]) -> None:
    for repo in repos:
        repo.git.fetch()
        repo_status(repo)
