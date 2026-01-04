import time
from contextlib import contextmanager
from datetime import datetime, timezone


@contextmanager
def timer(label: str = "Elapsed"):
    """
    Context manager for timing code blocks.
    """
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"{label}: {end - start:.6f}s")


def benchmark(func, *args, repeats=100, **kwargs):
    """
    Benchmark a function and return average time per run (seconds).
    """
    start = time.perf_counter()
    for _ in range(repeats):
        func(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / repeats


def now_utc():
    """
    Return the current UTC datetime.
    """
    return datetime.now(timezone.utc)


def now_iso(utc=True):
    """
    Return current time as an ISO-8601 string.
    If utc=True, returns UTC time; otherwise local time.
    """
    dt = now_utc() if utc else datetime.now()
    return dt.isoformat()


def unix_time():
    """
    Return current Unix timestamp in seconds (float).
    """
    return time.time()


def sleep_ms(ms: int):
    """
    Sleep for ms milliseconds.
    """
    if ms < 0:
        raise ValueError("sleep_ms(): ms must be non-negative")
    time.sleep(ms / 1000)


def format_duration(seconds: float) -> str:
    """
    Format seconds into a human-friendly string (e.g., '1m 03s', '250ms').
    """
    if seconds < 0:
        raise ValueError("format_duration(): seconds must be non-negative")

    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"

    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)

    secs_int = int(secs)
    if hrs >= 1:
        return f"{int(hrs)}h {int(mins)}m {secs_int:02d}s"
    if mins >= 1:
        return f"{int(mins)}m {secs_int:02d}s"
    return f"{secs:.2f}s"

