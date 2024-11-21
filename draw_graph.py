import networkx as nx
import matplotlib.pyplot as plt

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

# filename = 'test_json_1.json'
# data = reading_json_file(filename)
# draw_graph(data)
