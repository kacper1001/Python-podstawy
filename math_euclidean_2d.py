import math


def euclidean_distance(A, B):
    """
    >>> A = (1, 0)
    >>> B = (0, 1)
    >>> euclidean_distance(A, B)
    1.4142135623730951

    >>> euclidean_distance((0,0), (1,0))
    1.0

    >>> euclidean_distance((0,0), (1,1))
    1.4142135623730951

    >>> euclidean_distance((0,1), (1,1))
    1.0

    >>> euclidean_distance((0,10), (1,1))
    9.055385138137417
    """
    xa, yb = A[0], A[1]
    xb, yb = B[0], B[1]

    distance = math.sqrt((math.pow(xa, xb) + math.pow(yb, yb)))

    return (distance)
