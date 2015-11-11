#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from functools import partial, wraps

from plumbum import colors, cli
from plumbum.cli import SwitchAttr

from eatme import __version__, __date__
from eatme import hg


def print_time_spent(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        with colors.cyan:
            print('Done in {} sec'.format(finish - start))
        return result

    return wrapper


def get_repos(start_path='.'):
    for dir_path, subdir_list, file_list in os.walk(start_path):
        if '.hg' in subdir_list:
            yield dir_path

        # Удаляем скрытые директории из списка, чтобы не проходить по ним
        subdir_list[:] = [d for d in subdir_list if not d[0] == '.']


def run_for_all_repos(func, start_path='.'):
    for repo_path in get_repos(start_path):
        func(path=repo_path)


class EatMe(cli.Application):
    PROGNAME = 'eatme'
    VERSION = '%s (%s)' % (__version__, __date__)
    verbose = cli.Flag(["-v", "--verbose"], help="enable additional output")

    def main(self, *args):
        if args:
            with colors.red:
                print "Unknown command %r" % (args[0],)
            print "=" * 20
            self.help()
            return 1  # error exit code
        if not self.nested_command:  # will be ``None`` if no sub-command follows
            with colors.red:
                print "No command given"
            print "=" * 20
            self.help()
            return 1  # error exit code


@EatMe.subcommand("push")
class Push(cli.Application):
    new_branch = cli.Flag(["--new-branch"], help="hg push --new-branch")
    branch = SwitchAttr(["-b", "--branch"], argtype=str, help="hg update --rev BRANCH")

    @print_time_spent
    def main(self):
        hg_push = partial(hg.push, branch=self.branch, new_branch=self.new_branch)
        run_for_all_repos(hg_push)


@EatMe.subcommand("update")
class Update(cli.Application):
    clean = cli.Flag(["-C", "--clean"], help="hg update --clean")
    branch = SwitchAttr(["-b", "--branch"], argtype=str, help="hg update --rev BRANCH")

    @print_time_spent
    def main(self):
        hg_pull_update = partial(hg.pull_update, branch=self.branch, clean=self.clean)
        run_for_all_repos(hg_pull_update)


@EatMe.subcommand("status")
class Status(cli.Application):
    @print_time_spent
    def main(self):
        run_for_all_repos(hg.status)


@EatMe.subcommand("branch")
class Branch(cli.Application):
    @print_time_spent
    def main(self):
        run_for_all_repos(hg.branch)
