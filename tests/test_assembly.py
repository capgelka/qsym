import multiprocessing as mp
import os
import subprocess as sp
import sys
import shutil
import tempfile

import pytest
import tempfile

from test_utils import *


def pytest_generate_tests(metafunc):
    if 'target' in metafunc.fixturenames:
        testcases = get_testcases(os.path.join(TESTS_DIR, "assembly"))
        metafunc.parametrize('target', testcases)

def test_assembly(target):
    assert run_single_test(target)
