from pathlib import Path
import shutil


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


# -----------------------------
# +5 NEW FUNCTIONS
# -----------------------------

def exists(path) -> bool:
    """
    Return True if path exists.
    """
    return Path(path).exists()


def ensure_dir(path):
    """
    Create directory if it doesn't exist (including parents).
    Returns the Path object.
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def list_files(folder, recursive=False):
    """
    List files in a folder.
    If recursive=True, includes subfolders.
    Returns a list of Paths.
    """
    p = Path(folder)
    if not p.is_dir():
        raise ValueError("list_files(): folder must be a directory")

    if recursive:
        return [x for x in p.rglob("*") if x.is_file()]
    return [x for x in p.iterdir() if x.is_file()]


def file_size(path) -> int:
    """
    Return file size in bytes.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"file_size(): '{path}' not found")
    return p.stat().st_size


def copy(src, dst, overwrite=True):
    """
    Copy a file from src to dst.
    If overwrite=False and dst exists, raises FileExistsError.
    Returns the destination Path.
    """
    src_p = Path(src)
    dst_p = Path(dst)

    if not src_p.is_file():
        raise FileNotFoundError(f"copy(): source file '{src}' not found")

    if dst_p.exists() and not overwrite:
        raise FileExistsError(f"copy(): destination '{dst}' already exists")

    dst_p.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_p, dst_p)
    return dst_p
