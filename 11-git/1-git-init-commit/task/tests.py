#!/usr/bin/env python3
from unittest import TestCase
from git import Repo
from shutil import rmtree
import os, subprocess, sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

script = "./task/script.sh"

# This test is very basic
class GitTest(TestCase):

    # checks if the script runs successfully
    def test_0_run_script(self):
        cmd = ["/bin/sh", script]
        result = subprocess.run(cmd,
                                capture_output=True,
                                timeout=5)
        print(f"returncode: {result.returncode}")
        print(f"stdout: {result.stdout.decode('UTF-8')}")
        print(f"stderr: {result.stderr.decode('UTF-8')}")

        if result.returncode != 0:
            m = "Script execution failed (return code = {}).".format(result.returncode)
            raise AssertionError(m)

    # checks if commits have been made
    def test_1_commits_made(self):
        r = Repo("./")
        log = r.head.log()
        eprint("Commit Log has {} Entries:".format(len(log)))
        for l in log:
            eprint("- {}".format(l.message))
        self.assertTrue(len(log) > 0)

