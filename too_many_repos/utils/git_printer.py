from git import Commit
from git import Repo


def print_commit(commit: Commit) -> None:
    print('----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(
        commit.summary,
        commit.author.name,
        commit.author.email,
    ))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(
        commit.count(),
        commit.size,
    )))


def print_repository(repo: Repo) -> None:
    print(f'{repo.remote().url}: {repo.active_branch}')
