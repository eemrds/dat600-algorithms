"""Utility functions for the project."""
from typing import Callable
import networkx as nx
import matplotlib.pyplot as plt


def draw_heap(A):
    G = nx.DiGraph()
    for i in range(len(A)):
        G.add_node(i, label=A[i])
        left = lambda idx: 2 * idx + 1
        right = lambda idx: 2 * idx + 2

        if left(i) < len(A):
            G.add_edge(i, left(i))
        if right(i) < len(A):
            G.add_edge(i, right(i))

    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    labels = nx.get_node_attributes(G, "label")
    nx.draw(G, pos, with_labels=False, arrows=False)
    nx.draw_networkx_labels(G, pos, labels=labels)
    plt.show()
