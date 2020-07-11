#!/usr/bin/env python3
"""Spell messages with limited letters"""

import argparse
import os
import re
from collections import Counter


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Spell messages with limited letters',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Message to spell')

    parser.add_argument('-s',
                        '--sub',
                        help='Substitute numbers',
                        action='store_true')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()


    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    # 12 each - A E I N O R S
    # 8 each - L T (red) 5 6
    # 6 each - B C D F G H J K M P U W Y
    # 4 each - Q V X Z (red) 1 2 3 4 7 8 0 ! * .
    # 2 each - . - ! / % & (red) $ →

    args = get_args()
    letters = {'A': 12, 'B': 6, 'C': 6, 'D': 6, 'E': 12, 'F': 6, 'G': 6,
               'H': 6, 'I': 12, 'J': 6, 'K': 6, 'L': 8, 'M': 6, 'N': 12,
               'O': 12, 'P': 6, 'Q': 4, 'R': 12, 'S': 12, 'T': 8, 'U': 6,
               'V': 4, 'W': 6, 'X': 4, 'Y': 6, 'Z': 4, '1': 4, '2': 4, '3': 4,
               '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, '0': 4, '!': 4, '*': 4,
               '.': 4, '-': 2, '!': 2, '/': 2, '%': 2, '&': 2, '$': 2}


    chars = ''.join(letters.keys()).replace('-', '') + '-' # put - at the end
    pattern = '[^' + chars + ']' # anything not these
    text = re.sub(pattern, '', args.text.upper())
    print(text)
    freq = Counter(text)
    print(freq)
    print('OK' if all([letters[c] >= freq[c] for c in text]) else 'No')


# --------------------------------------------------
if __name__ == '__main__':
    main()
