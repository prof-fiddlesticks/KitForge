import random
import string


def pick(seq):
    """
    Pick a random element from a sequence.
    """
    return random.choice(seq)


def shuffle(seq):
    """
    Return a shuffled copy of a sequence.
    """
    new = list(seq)
    random.shuffle(new)
    return new


def random_name(length=8):
    """
    Generate a random lowercase name.
    """
    if length <= 0:
        raise ValueError("random_name(): length must be positive")
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


# -----------------------------
# +5 NEW FUNCTIONS
# -----------------------------

def randint(a: int, b: int) -> int:
    """
    Return a random integer N such that a <= N <= b.
    """
    return random.randint(a, b)


def randfloat(a=0.0, b=1.0) -> float:
    """
    Return a random float x such that a <= x < b.
    """
    return random.random() * (b - a) + a


def sample(seq, k: int):
    """
    Return k unique random elements from seq.
    """
    return random.sample(seq, k)


def weighted_choice(items, weights):
    """
    Pick one item using weights.
    items and weights must be same length.
    """
    if len(items) != len(weights):
        raise ValueError("weighted_choice(): items and weights must have same length")
    if len(items) == 0:
        raise ValueError("weighted_choice(): items must not be empty")
    return random.choices(items, weights=weights, k=1)[0]


def token(length=16):
    """
    Generate a random token (letters+digits).
    """
    if length <= 0:
        raise ValueError("token(): length must be positive")
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))
