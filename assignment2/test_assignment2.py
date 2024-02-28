import pytest

from assignment2 import matrix_chain_order, dynamic_knapsack_0_1


@pytest.mark.parametrize(
    "p, m, s",
    [
        (
            [1, 2, 3, 4, 3],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 6, 18, 30],
                [0, 0, 0, 24, 48],
                [0, 0, 0, 0, 36],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 2, 3],
                [0, 0, 0, 2, 3],
                [0, 0, 0, 0, 3],
                [0, 0, 0, 0, 0],
            ],
        ),
        (
            [5, 4, 6, 2, 7],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 120, 88, 158],
                [0, 0, 0, 48, 104],
                [0, 0, 0, 0, 84],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 3],
                [0, 0, 0, 2, 3],
                [0, 0, 0, 0, 3],
                [0, 0, 0, 0, 0],
            ],
        ),
    ],
)
def test_matrix_chain_order(p, m, s):
    m_res, s_res = matrix_chain_order(p)
    for i in range(len(p) - 1):
        assert m_res[i] == m[i]
        assert s_res[i] == s[i]


@pytest.mark.parametrize(
    "W, items, result",
    [
        (1, [[1, 2], [3, 4], [5, 6], [7, 8]], 2),
        (3, [[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        (4, [[1, 2], [3, 4], [5, 6], [7, 8]], 6),
        (6, [[1, 2], [3, 4], [5, 6], [7, 8]], 8),
        (8, [[1, 2], [3, 4], [5, 6], [7, 8]], 10),
    ],
)
def test_dynamic_knapsack_0_1(W, items, result):
    knapsack = dynamic_knapsack_0_1(W, items)
    assert knapsack == result


@pytest.mark.parametrize(
    "W, items, result",
    [
        (1, [[1, 2], [3, 4], [5, 6], [7, 8]], 2),
        (3, [[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        (4, [[1, 2], [3, 4], [5, 6], [7, 8]], 6),
        (6, [[1, 2], [3, 4], [5, 6], [7, 8]], 8),
        (8, [[1, 2], [3, 4], [5, 6], [7, 8]], 10),
    ],
)
def test_greedy_factional_knapsack_0_1(W, items, result):
    knapsack = dynamic_knapsack_0_1(W, items)
    assert knapsack == result
