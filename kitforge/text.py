import re
import string


def clean(s: str) -> str:
    """
    Strip whitespace and normalize internal spaces.
    """
    return " ".join(s.strip().split())


def slugify(s: str) -> str:
    """
    Convert text into a URL-safe slug.
    """
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    return s


def between(s: str, left: str, right: str) -> str:
    """
    Return text between two substrings.
    """
    try:
        return s.split(left, 1)[1].split(right, 1)[0]
    except IndexError:
        return ""


# -----------------------------
# +5 NEW FUNCTIONS
# -----------------------------

def contains_any(s: str, items) -> bool:
    """
    True if any item in items is a substring of s.
    """
    return any(item in s for item in items)


def contains_all(s: str, items) -> bool:
    """
    True if all items in items are substrings of s.
    """
    return all(item in s for item in items)


def truncate(s: str, max_len: int, ellipsis: str = "...") -> str:
    """
    Truncate string to max_len characters (including ellipsis).
    """
    if max_len < 0:
        raise ValueError("truncate(): max_len must be non-negative")
    if len(s) <= max_len:
        return s
    if max_len <= len(ellipsis):
        return ellipsis[:max_len]
    return s[: max_len - len(ellipsis)] + ellipsis


def remove_punct(s: str) -> str:
    """
    Remove punctuation characters from a string.
    """
    table = str.maketrans("", "", string.punctuation)
    return s.translate(table)


def is_blank(s: str) -> bool:
    """
    True if s is empty or contains only whitespace.
    """
    return len(s.strip()) == 0
