"""Colouring graphs"""

import json
import networkx as nx
import matplotlib.pyplot as plt


def reading_json_file(filename: str) -> dict:
    """
    Reads json files with information about nodes of the graph

    :param filename: str, file from which we read an info
    :return: dict, dictionary with nodes as a key and info about them as a value

    >>> reading_json_file("test_json_1.json")
    {'1': {'color': 'b', 'edge_with': [2, 3, 4]}, '2': {'color': 'b',\
 'edge_with': [1, 4]}, '3': {'color': 'g', 'edge_with': [1]},\
 '4': {'color': 'r', 'edge_with': [1, 2]}}
    """
    with open(filename, 'r', encoding = 'utf-8') as file:
        result = json.load(file)
    return result


def draw_graph(data: dict) -> None:
    """
    Visualizes the graph based on the graph data.

    :param data: dict, A dictionary containing data.
    :return: None, shows the vizualization of the graph
    """
    G = nx.Graph()
    for node, info in data.items():
        G.add_node(node, color=info["color"])
        G.add_edges_from((node, str(neighbor)) for neighbor in info["edge_with"])

    nx.draw_circular(
        G,
        with_labels=True,
        node_color=[G.nodes[node]['color'] for node in G],
    )
    plt.show()


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

    draw_graph(reading_json_file('test_json_2.json'))
