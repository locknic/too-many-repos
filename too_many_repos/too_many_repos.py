import argparse

from git import Repo

from too_many_repos.checkout_master import repos_checkout_master
from too_many_repos.pull import repos_pull
from too_many_repos.status import repos_status
from too_many_repos.utils.repo_finder import find_top_repos

COMMITS_TO_PRINT = 5


def git_pull_repo(repo: Repo) -> None:
    origin = repo.remotes.origin
    origin.fetch()
    origin.pull()


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='too-many-repos', description='A tool for managing multiple repos',
    )
    parser.add_argument('command', type=str, help='command help')
    parser.add_argument('root', type=str, help='root help')
    parser.add_argument(
        "-v", "--verbosity", action="count", default=0,
        help="increase output verbosity",
    )
    args = parser.parse_args()

    repos = find_top_repos(args.root)

    if args.command == 'status':
        repos_status(repos)
    elif args.command == 'master':
        repos_checkout_master(repos)
    elif args.command == 'fetch':
        raise NotImplementedError
    elif args.command == 'pull':
        repos_pull(repos)
    elif args.command == 'clean-merged':
        raise NotImplementedError

    # TODO:
    # display status
    # checkout master
    # fetch
    # pull
    #   default pull current branch
    #   optional checkout master
    #   optional stash changes
    #   optional reset changes
    # delete remote merged branches

    return 0


if __name__ == "__main__":
    exit(main())
