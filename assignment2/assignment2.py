from typing import Any
from numpy import infty


def matrix_chain_order(p: list[int]) -> tuple[list[list[int]], list[list[int]]]:
    """Dynamic matrix chain order.

    Args:
        p: Dimensions of the matrix.

    Returns:
        m: Auxilary table for storing m[i, j] costs.
        s: Auxilary table for storing the k value that achieved the optimal cost.
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


def dynamic_knapsack_0_1(W: int, items: list[(int, int)]) -> int:
    """Dynamic 0-1 knapsack algorithm.

    Following the pseudocode from: https://en.wikipedia.org/wiki/Knapsack_problem#Dynamic_programming_in-advance_algorithm

    Ex:
    * W = 7
    * items = [(2, 3), (3, 4), (4, 5), (5, 6)]

    | n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    |---|---|---|---|---|---|---|---|---|
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | []
    | 1 | 0 | 0 | 3 | 3 | 3 | 3 | 3 | 3 | [(2, 3)]
    | 2 | 0 | 0 | 3 | 4 | 4 | 7 | 7 | 7 | [(2, 3), (3, 4)]
    | 3 | 0 | 0 | 3 | 4 | 5 | 7 | 8 | 9 | [(2, 3), (3, 4), (4, 5)]
    | 4 | 0 | 0 | 3 | 4 | 5 | 7 | 8 | 9 | [(2, 3), (3, 4), (4, 5), (5, 6)]

    Args:
        W: Maximum weight.
        items: Items to steal (weight, price).

    Returns:
        Maximum price that can be stolen.
    """
    n = len(items)
    table = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    v = [v for _, v in items]
    w = [w for w, _ in items]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i - 1] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(
                    table[i - 1][j], table[i - 1][j - w[i - 1]] + v[i - 1]
                )
    return table[n][W]


def greedy_fractional_knapsack_0_1(W: int, items: list[(int, int)]) -> float:
    """Greedy fractional knapsack algorithm.

    Args:
        W: Maximum weight.
        items: Items to steal (weight, price).

    Returns:
        Maximum price that can be stolen.
    """
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total = 0
    for w, v in items:
        if W >= w:
            total += v
            W -= w
        else:
            total += (W / w) * v
            break
    return total

def greedy_coins(coins: list[int], total: int) -> list[int]:
    """Greedy coin algorithm.

    Args:
        coins: List of coins to choose from.
        total: Value that combination of coins should reach.

    Returns:
        Ordered list of the coins added.
    """
    sum = 0
    n = 0
    result = []
    for coin in reversed(coins):
        while sum + coin <= total:
            sum += coin
            n += 1
            result.append(coin)
        if sum == total:
            break
    return result

def bottomup_coins(coins: list[int], total: int) -> list[int]:
    """Dynamic bottom-up coin algorithm.

    Args:
        coins: List of coins to choose from.
        total: Value that combination of coins should reach.

    Returns:
        Ordered list of the coins added.
    """
    steps = [float('inf')] * (total + 1)
    steps[0] = 0
    coin_used = [-1] * (total + 1)
    # For each value i up to total
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin and steps[i - coin] + 1 < steps[i]:
                steps[i] = steps[i - coin] + 1
                coin_used[i] = coin
    result = []
    while total > 0:
        result.append(coin_used[total])
        total -= coin_used[total]
    return result