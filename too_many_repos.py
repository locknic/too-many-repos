import os

from git import Commit
from git import Repo

COMMITS_TO_PRINT = 5


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
    print(f'Repo description: {repo.description}')
    print(f'Repo active branch is {repo.active_branch}')
    for remote in repo.remotes:
        print(f'Remote named "{remote}" with URL "{remote.url}"')
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


def main() -> int:
    repo_path = os.getenv('GIT_REPO_PATH')
    # Repo object used to programmatically interact with Git repositories
    repo = Repo(repo_path)
    # check that the repository loaded correctly
    if not repo.bare:
        print(f'Repo at {repo_path} successfully loaded.')
        print_repository(repo)
        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print(f'Could not load repository at {repo_path} :(')

    return 0


if __name__ == "__main__":
    exit(main())
