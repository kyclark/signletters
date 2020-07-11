#!/usr/bin/env python3
"""tests for signletters.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './signletters.py'
letters1 = './letters/1.txt'
letters2 = './letters/2.txt'
letters3 = './letters/3.txt'
message1 = './messages/1.txt'
message2 = './messages/2.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """Dies on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -l {bad} -t foo')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_ok_command_line():
    """ok"""

    assert os.path.isfile(message1)
    rv, out = getstatusoutput(f'{prg} -l {letters1} -t foobar')
    assert rv == 0
    assert out.strip() == f'OK  : FOOBAR'


# --------------------------------------------------
def test_ok_file():
    """ok"""

    assert os.path.isfile(message1)
    rv, out = getstatusoutput(f'{prg} -l {letters1} -t {message1}')
    assert rv == 0
    msg = open(message1).read().rstrip().upper()
    assert out.strip() == f'OK  : {msg}'


# --------------------------------------------------
def test_not_ok_file():
    """not ok"""

    assert os.path.isfile(message2)
    rv, out = getstatusoutput(f'{prg} -l {letters3} -t {message2}')
    assert rv == 0
    msg = open(message2).read().rstrip().upper()
    assert out.strip() == f'Nope: {msg}'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
