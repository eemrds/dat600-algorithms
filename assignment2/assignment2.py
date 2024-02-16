from numpy import infty


def matrix_chain_order(p: list[int]) -> tuple[list[list[int]], list[list[int]]]:
    """Dynamic matrix chain order.

    Args:
        p: Dimensions of the matrix.

    Returns:
        m: Auxilary table for storing m[i, j]
        s:
    """
    n = len(p) - 1
    tab = [0 for _ in range(n)]
    m = [tab[:] for _ in range(n)]
    s = [tab[:] for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = infty
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k + 1
    return m, s
