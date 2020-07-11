#!/usr/bin/env python3
"""Spell messages with limited letters"""

import argparse
import io
import os
import re
from collections import Counter
from typing import TextIO, Dict, NewType

LetterFreq = NewType('LetterFreq', Dict[str, int])


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Spell messages with limited letters',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t',
                        '--text',
                        metavar='str',
                        help='Input message or file',
                        nargs='+')

    parser.add_argument('-l',
                        '--letters',
                        help='File with letter frequencies',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letters = read_letters(args.letters)

    for text in args.text:
        if os.path.isfile(text):
            text = open(text).read().rstrip()

        text = text.upper()
        print(f'{"OK" if check_text(text, letters) else "Nope":4}: {text}')


# --------------------------------------------------
def read_letters(fh: TextIO) -> LetterFreq:
    """Read the letter frequencies from a file"""

    freqs = {}
    for line in fh:
        if match := re.match(r'(\d+)\s*:\s*(.+)', line):
            num = int(match.group(1))
            for char in match.group(2).split():
                freqs[char] = num

    return LetterFreq(freqs)


# --------------------------------------------------
def test_read_letters() -> None:
    """Test read_letters"""

    t1 = io.StringIO('12: A E\n5: B C')
    assert read_letters(t1) == LetterFreq({'A': 12, 'B': 5, 'C': 5, 'E': 12})

    t2 = io.StringIO('6: X Y\n3: I U')
    assert read_letters(t2) == LetterFreq({'I': 3, 'U': 3, 'X': 6, 'Y': 6})


# --------------------------------------------------
def check_text(text: str, letters: LetterFreq) -> bool:
    """Check the chars in text with letters"""

    # put - at the end
    chars = ''.join(letters.keys()).replace('-', '') + '-'

    # anything not these
    pattern = '[^' + chars + ']'

    check = re.sub(pattern, '', text)
    freq = Counter(check)
    return all([letters[char] >= freq[char] for char in check])


# --------------------------------------------------
def test_check_test() -> None:
    """Test check_test"""

    freq = LetterFreq({'A': 3, 'B': 1})
    assert check_text('A B', freq)
    assert check_text('A AB', freq)
    assert check_text('AA AB', freq)
    assert not check_text('A AAA B', freq)
    assert not check_text('AAA BB', freq)


# --------------------------------------------------
if __name__ == '__main__':
    main()
