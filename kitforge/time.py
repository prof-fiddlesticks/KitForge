import time
from contextlib import contextmanager

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
    Benchmark a function.
    """
    start = time.perf_counter()
    for _ in range(repeats):
        func(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / repeats
