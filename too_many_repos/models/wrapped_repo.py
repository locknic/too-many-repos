from git import Commit
from git import Repo


class WrappedRepo(Repo):
    @property
    def is_master(self) -> bool:
        return self.active_branch == self.heads.master

    @property
    def name(self) -> str:
        return self.remote().url.replace('git@github.com:', '').replace('.git', '')

    @property
    def has_changes(self) -> bool:
        return self.is_dirty(untracked_files=True)

    @property
    def commits_ahead_remote(self) -> int:
        return self._count_commits_ahead(self.active_branch.tracking_branch().commit, self.active_branch.commit)

    @property
    def commits_behind_remote(self) -> int:
        return self._count_commits_ahead(self.active_branch.commit, self.active_branch.tracking_branch().commit)

    @property
    def commits_ahead_master(self) -> int:
        return self._count_commits_ahead(self._last_master_commit, self.active_branch.commit)

    @property
    def commits_behind_master(self) -> int:
        return self._count_commits_ahead(self._last_master_commit, self.heads.master.tracking_branch().commit)

    @property
    def _last_master_commit(self) -> Commit:
        last_master_commit = self.merge_base(self.active_branch, self.heads.master)
        return last_master_commit[0]

    def _count_commits_ahead(self, starting_commit: Commit, ending_commit: Commit) -> int:
        commits_ahead = self.iter_commits(str(starting_commit) + ".." + str(ending_commit))
        count_ahead = sum(1 for _ in commits_ahead)

        return count_ahead
