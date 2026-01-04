import math


# ==================================================
# BASIC MATH
# ==================================================

def factorial(n: int) -> int:
    """
    Return the factorial of a non-negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("factorial() only accepts integers")
    if n < 0:
        raise ValueError("factorial() not defined for negative numbers")
    return math.factorial(n)


def power(base, exp):
    """
    Return base raised to the power exp.
    """
    return base ** exp


def sqrt(x):
    """
    Return the square root of x.
    """
    if x < 0:
        raise ValueError("sqrt() not defined for negative numbers")
    return math.sqrt(x)


# ==================================================
# TRIGONOMETRY (DEGREES OR RADIANS)
# ==================================================

def _to_radians(theta, unit):
    """
    Convert degrees to radians if required.
    """
    unit = unit.lower()
    if unit == "degrees":
        return math.radians(theta)
    if unit == "radians":
        return theta
    raise ValueError("unit must be 'degrees' or 'radians'")


def sin(theta, unit="radians"):
    """Return sine of theta."""
    return math.sin(_to_radians(theta, unit))


def cos(theta, unit="radians"):
    """Return cosine of theta."""
    return math.cos(_to_radians(theta, unit))


def tan(theta, unit="radians"):
    """Return tangent of theta."""
    return math.tan(_to_radians(theta, unit))


def sec(theta, unit="radians"):
    """Return secant of theta (1 / cos)."""
    c = cos(theta, unit)
    if c == 0:
        raise ValueError("sec() undefined when cos(theta) = 0")
    return 1 / c


def cosec(theta, unit="radians"):
    """Return cosecant of theta (1 / sin)."""
    s = sin(theta, unit)
    if s == 0:
        raise ValueError("cosec() undefined when sin(theta) = 0")
    return 1 / s


def cot(theta, unit="radians"):
    """Return cotangent of theta (1 / tan)."""
    t = tan(theta, unit)
    if t == 0:
        raise ValueError("cot() undefined when tan(theta) = 0")
    return 1 / t


# ==================================================
# LOGARITHMS & NUMBER THEORY
# ==================================================

def log(x, base=10):
    """
    Return logarithm of x with the given base.
    """
    if x <= 0:
        raise ValueError("log() only defined for positive numbers")
    return math.log(x, base)


def gcd(a, b):
    """
    Return the greatest common divisor of a and b.
    """
    return math.gcd(a, b)


def lcm(a, b):
    """
    Return the least common multiple of a and b.
    """
    return abs(a * b) // gcd(a, b)
