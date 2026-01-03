import re

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
