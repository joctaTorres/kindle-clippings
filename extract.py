import sys
import re

from typing import Optional
from dataclasses import dataclass
from itertools import zip_longest


CLIPPING_SEPARATOR = "=========="
TITLE_AUTHOR_REGEX = re.compile(r"^(?P<book>.+)\s\((?P<author>.+)\)$")
DESCRIPTION_REGEX = re.compile(r"^\-\s(?P<description>.+?)\s\|\s((?P<location>.+)\s\|\s)?(?P<date>.+)$")
CLIPPING_SIZE_LINES = 5


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

@dataclass
class BookClipping:
    text: str
    title: str
    author: str
    description: str
    location: Optional[str]
    clip_date: str


def parse(filepath):
    with open(filepath, "r", encoding='utf-8-sig') as clippings:
        for title, description, _, clipping, _ in grouper(CLIPPING_SIZE_LINES, clippings):
            title_author_match = TITLE_AUTHOR_REGEX.match(title)
            description_match = DESCRIPTION_REGEX.match(description)

            yield BookClipping(
                clipping.strip(),
                title_author_match.group("book"),
                title_author_match.group("author"),
                description_match.group("description"),
                description_match.group("location"),
                description_match.group("date")
            )


def match_book(clippings, book_title):
    book_title =  book_title.strip().lower()

    def has_match(clipping):
        return book_title in clipping.title.strip().lower()
    
    for clipping in clippings:
        if has_match(clipping):
            print(clipping.text)
            print()



if __name__ == "__main__":
    clipping_filepath = sys.argv[1]
    book_title = sys.argv[2]

    clippings = parse(clipping_filepath)
    match_book(clippings, book_title)

