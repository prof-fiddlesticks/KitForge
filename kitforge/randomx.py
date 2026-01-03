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
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))
