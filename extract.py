from io import BufferedIOBase
import sys
import re

from itertools import zip_longest


CLIPPING_SEPARATOR = "=========="
BOOK_AUTHOR_REGEX = re.compile(r"^(?P<book>.+)\s\((?P<author>.+)\)$")
HIGHLIGHT_DESCRIPTION = re.compile(r"^\-\s(?P<description>.+?)\s\|\s((?P<location>.+)\s\|\s)?(?P<date>.+)$")
CLIPPING_SIZE_LINES = 5



def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def parse(file):
    with open(file) as clippings:
        count = 0
        for title, description, _, clip, _ in grouper(CLIPPING_SIZE_LINES, clippings):
            print(title)
            print(description)
            print(clip)
            count +=1

            if count >= 5:
                break



if __name__ == "__main__":
    clipping_filepath = sys.argv[1]
    parse(clipping_filepath)
