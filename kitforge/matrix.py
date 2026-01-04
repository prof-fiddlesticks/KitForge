from __future__ import annotations

import math


# ==================================================
# VECTORS
# ==================================================

def dot(a, b):
    """
    Dot product of two vectors a and b.
    """
    if len(a) != len(b):
        raise ValueError("dot(): vectors must have the same length")
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    """
    Cross product of two 3D vectors a and b.
    Returns a 3D vector.
    """
    if len(a) != 3 or len(b) != 3:
        raise ValueError("cross(): only defined for 3D vectors")
    ax, ay, az = a
    bx, by, bz = b
    return [
        ay * bz - az * by,
        az * bx - ax * bz,
        ax * by - ay * bx,
    ]


def norm(v):
    """
    Euclidean length (magnitude) of vector v.
    """
    return math.sqrt(dot(v, v))


# ==================================================
# MATRICES (represented as list of rows)
# ==================================================

def shape(A):
    """
    Return (rows, cols) of matrix A.
    """
    if not A or not isinstance(A, list):
        raise ValueError("shape(): matrix must be a non-empty list of rows")
    r = len(A)
    c = len(A[0])
    if c == 0:
        raise ValueError("shape(): matrix rows must be non-empty")
    for row in A:
        if len(row) != c:
            raise ValueError("shape(): matrix rows must all have the same length")
    return r, c


def zeros(rows, cols, value=0.0):
    """
    Create a rows x cols matrix filled with value.
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("zeros(): rows and cols must be positive")
    return [[value for _ in range(cols)] for _ in range(rows)]


def identity(n):
    """
    Create an n x n identity matrix.
    """
    if n <= 0:
        raise ValueError("identity(): n must be positive")
    I = zeros(n, n, 0.0)
    for i in range(n):
        I[i][i] = 1.0
    return I


def transpose(A):
    """
    Transpose of matrix A.
    """
    r, c = shape(A)
    return [[A[i][j] for i in range(r)] for j in range(c)]


def matmul(A, B):
    """
    Matrix multiplication A * B.
    """
    ar, ac = shape(A)
    br, bc = shape(B)
    if ac != br:
        raise ValueError("matmul(): inner dimensions do not match")
    out = zeros(ar, bc, 0.0)
    for i in range(ar):
        for k in range(ac):
            aik = A[i][k]
            for j in range(bc):
                out[i][j] += aik * B[k][j]
    return out


def matvec(A, v):
    """
    Multiply matrix A by vector v (A * v).
    """
    r, c = shape(A)
    if len(v) != c:
        raise ValueError("matvec(): vector length must equal matrix columns")
    return [dot(row, v) for row in A]


def minor(A, row_to_remove, col_to_remove):
    """
    Return the minor matrix with one row and one column removed.
    """
    r, c = shape(A)
    return [
        [A[i][j] for j in range(c) if j != col_to_remove]
        for i in range(r)
        if i != row_to_remove
    ]


def det(A):
    """
    Determinant of a square matrix A.
    Uses Gaussian elimination (faster & better than recursive expansion).
    """
    n, m = shape(A)
    if n != m:
        raise ValueError("det(): matrix must be square")

    # Copy to avoid modifying original
    M = [row[:] for row in A]
    det_val = 1.0
    sign = 1.0
    eps = 1e-12

    for col in range(n):
        # Find pivot
        pivot_row = None
        max_abs = 0.0
        for r in range(col, n):
            val = abs(M[r][col])
            if val > max_abs:
                max_abs = val
                pivot_row = r

        if pivot_row is None or max_abs < eps:
            return 0.0

        # Swap if needed
        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]
            sign *= -1.0

        pivot = M[col][col]
        det_val *= pivot

        # Eliminate below
        for r in range(col + 1, n):
            factor = M[r][col] / pivot
            if abs(factor) < eps:
                continue
            for k in range(col, n):
                M[r][k] -= factor * M[col][k]

    return sign * det_val


def solve(A, b):
    """
    Solve the linear system A x = b using Gaussian elimination with partial pivoting.
    - A: square matrix (n x n)
    - b: vector length n
    Returns vector x length n.
    """
    n, m = shape(A)
    if n != m:
        raise ValueError("solve(): A must be square")
    if len(b) != n:
        raise ValueError("solve(): b length must match A rows")

    # Build augmented matrix [A | b]
    M = [A[i][:] + [float(b[i])] for i in range(n)]
    eps = 1e-12

    # Forward elimination
    for col in range(n):
        # Pivot row
        pivot_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot_row][col]) < eps:
            raise ValueError("solve(): system has no unique solution (singular matrix)")

        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]

        pivot = M[col][col]
        # Normalize pivot row (optional but helps stability/readability)
        for j in range(col, n + 1):
            M[col][j] /= pivot

        # Eliminate below
        for r in range(col + 1, n):
            factor = M[r][col]
            if abs(factor) < eps:
                continue
            for j in range(col, n + 1):
                M[r][j] -= factor * M[col][j]

    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))
    return x


def inverse(A):
    """
    Compute inverse of a square matrix A using Gauss-Jordan elimination.
    """
    n, m = shape(A)
    if n != m:
        raise ValueError("inverse(): matrix must be square")

    eps = 1e-12
    # Augment [A | I]
    M = [A[i][:] + identity(n)[i] for i in range(n)]

    for col in range(n):
        pivot_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot_row][col]) < eps:
            raise ValueError("inverse(): matrix is singular (not invertible)")

        if pivot_row != col:
            M[col], M[pivot_row] = M[pivot_row], M[col]

        pivot = M[col][col]
        # Normalize pivot row
        for j in range(2 * n):
            M[col][j] /= pivot

        # Eliminate other rows
        for r in range(n):
            if r == col:
                continue
            factor = M[r][col]
            if abs(factor) < eps:
                continue
            for j in range(2 * n):
                M[r][j] -= factor * M[col][j]

    # Extract right half
    return [row[n:] for row in M]


# ==================================================
# TRANSFORMATIONS (2D homogeneous 3x3)
# Points as (x, y) -> use apply_transform_2d
# ==================================================

def translate_2d(tx, ty):
    return [
        [1.0, 0.0, tx],
        [0.0, 1.0, ty],
        [0.0, 0.0, 1.0],
    ]


def scale_2d(sx, sy=None):
    if sy is None:
        sy = sx
    return [
        [sx,  0.0, 0.0],
        [0.0, sy,  0.0],
        [0.0, 0.0, 1.0],
    ]


def rotate_2d(theta, unit="radians"):
    if unit.lower() == "degrees":
        theta = math.radians(theta)
    elif unit.lower() != "radians":
        raise ValueError("rotate_2d(): unit must be 'degrees' or 'radians'")

    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [c, -s, 0.0],
        [s,  c, 0.0],
        [0.0, 0.0, 1.0],
    ]


def apply_transform_2d(T, point):
    """
    Apply 3x3 transform matrix T to a 2D point (x, y).
    """
    if len(point) != 2:
        raise ValueError("apply_transform_2d(): point must be (x, y)")
    x, y = point
    v = [x, y, 1.0]
    out = matvec(T, v)
    w = out[2]
    if w == 0:
        raise ValueError("apply_transform_2d(): invalid transform (w=0)")
    return (out[0] / w, out[1] / w)


# ==================================================
# BASIC 3D TRANSFORMATIONS (4x4 homogeneous)
# Points as (x, y, z) -> use apply_transform_3d
# ==================================================

def translate_3d(tx, ty, tz):
    return [
        [1.0, 0.0, 0.0, tx],
        [0.0, 1.0, 0.0, ty],
        [0.0, 0.0, 1.0, tz],
        [0.0, 0.0, 0.0, 1.0],
    ]


def scale_3d(sx, sy=None, sz=None):
    if sy is None:
        sy = sx
    if sz is None:
        sz = sx
    return [
        [sx,  0.0, 0.0, 0.0],
        [0.0, sy,  0.0, 0.0],
        [0.0, 0.0, sz,  0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def rotate_x(theta, unit="radians"):
    if unit.lower() == "degrees":
        theta = math.radians(theta)
    elif unit.lower() != "radians":
        raise ValueError("rotate_x(): unit must be 'degrees' or 'radians'")
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, c, -s, 0.0],
        [0.0, s,  c, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def rotate_y(theta, unit="radians"):
    if unit.lower() == "degrees":
        theta = math.radians(theta)
    elif unit.lower() != "radians":
        raise ValueError("rotate_y(): unit must be 'degrees' or 'radians'")
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [ c, 0.0, s, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-s, 0.0, c, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def rotate_z(theta, unit="radians"):
    if unit.lower() == "degrees":
        theta = math.radians(theta)
    elif unit.lower() != "radians":
        raise ValueError("rotate_z(): unit must be 'degrees' or 'radians'")
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [c, -s, 0.0, 0.0],
        [s,  c, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def apply_transform_3d(T, point):
    """
    Apply 4x4 transform matrix T to a 3D point (x, y, z).
    """
    if len(point) != 3:
        raise ValueError("apply_transform_3d(): point must be (x, y, z)")
    x, y, z = point
    v = [x, y, z, 1.0]
    out = matvec(T, v)
    w = out[3]
    if w == 0:
        raise ValueError("apply_transform_3d(): invalid transform (w=0)")
    return (out[0] / w, out[1] / w, out[2] / w)
