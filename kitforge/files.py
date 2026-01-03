from pathlib import Path

def count_lines(path) -> int:
    """
    Count number of lines in a text file.
    """
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return sum(1 for _ in f)

def read_text(path) -> str:
    """
    Read entire file as text.
    """
    return Path(path).read_text(encoding="utf-8")

def write_text(path, text: str):
    """
    Write text to a file.
    """
    Path(path).write_text(text, encoding="utf-8")
