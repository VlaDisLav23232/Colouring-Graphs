"""Colouring graphs"""

import json
import networkx as nx
import matplotlib.pyplot as plt


def reading_json_file(filename):
    """
    Reads files
    """
    with open(filename, 'r', encoding = 'utf-8') as file:
        result = json.load(file)
    return result


def draw_graph(data):
    """
    Visualizes the graph based on the json file data.
    
    :data (dict): A dictionary containing data.
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
    print(reading_json_file('test_json_1.json'))
    filename = 'test_json_2.json'
    data = reading_json_file(filename)
    draw_graph(data)
