"""Colouring graphs"""

import argparse
import json
import networkx as nx
import matplotlib.pyplot as plt


def arguments():
    """
    Reads arguments for argparse.
    """
    parser = argparse.ArgumentParser(description="Graph Coloring Program")
    parser.add_argument("input_file", type=str, nargs = "?",\
    default=None, help="Path to the JSON file \
    containing graph data",)
    parser.add_argument("--draw", action="store_true",\
    help="Visualize the graph before and after after recoloring",)

    args = parser.parse_args()

    return args


def run_program():
    '''
    Runs the program: processes graph data, and optionally visualizes it.
    '''
    args = arguments()

    print("-------------------------------------------\n\
WELCOME TO THE GRAPH RECOULORER!\n\
-------------------------------------------")
    if args.draw:
        if args.input_file.endswith(".json"):
            data = reading_json_file(args.input_file)
            recolored_data = drawing_with_new_colours(data)
            if recolored_data is None:
                print("-----------------------------------\n\
The graph cannot be recoloured!\n\
-----------------------------------")
            elif not recolored_data:
                print("--------------------------------------------------------\n\
This graph does not have vertices! Try something else!\n\
--------------------------------------------------------")
            else:
                draw_graph(data)
                draw_graph(recolored_data)
        else:
            print(f"--------------------------------------------\n\
The file {args.input_file} is not a JSON file!\n\
--------------------------------------------")


def reading_json_file(filename: str) -> dict:
    """
    Reads json files with information about nodes of the graph

    :param filename: str, file from which we read an info
    :return: dict, dictionary with nodes as a key and info about them as a value
    """
    with open(filename, 'r', encoding = 'utf-8') as file:
        result = json.load(file)
    return result


def drawing_with_new_colours(data: dict, num: int = 1, new_dict: None|dict = None) -> dict:
    """
    Draws graph nodes with new colours, by taking into account, that
    two neighbouring nodes cannot be identically coloured and node cannot
    be coloured with its previous colour.

    :param data: dict, A dictionary containing data.
    :param num: int, graph node number
    :param new_dict: None or dict, None at the recursion depth 1 and
    dict at the recursion depth with 2 or more. Saves the data about recoloured graph
    :return: dict, recoloured graph
    """

    if new_dict is None:
        new_dict = {}

    if len(data) < num:
        return new_dict

    available_colours = ["r", "b", "g"]
    available_colours.remove(data[str(num)]["color"])
    new_dict.setdefault(str(num), {"color": "", "edge_with": data[str(num)]["edge_with"]})

    for el in data[str(num)]["edge_with"]:
        new_dict.setdefault(str(el), {"color": "", "edge_with": data[str(el)]["edge_with"]})
        if new_dict[str(el)]["color"] in available_colours and num > el:
            available_colours.remove(new_dict[str(el)]["color"])

    for colour in available_colours:
        new_dict[str(num)]["color"] = colour
        new_dict = drawing_with_new_colours(data, num+1, new_dict)
        if new_dict[str(len(new_dict))]["color"] != "":
            break

    if num == 1 and new_dict[str(len(new_dict))]["color"] == "":
        return None

    return new_dict

def draw_graph(data: dict) -> None:
    """
    Visualizes the graph based on the graph data.

    :param data: dict, A dictionary containing data.
    :return: None, shows the vizualization of the graph
    """

    graph = nx.Graph()
    for node, info in data.items():
        graph.add_node(node, color=info["color"])
        graph.add_edges_from((node, str(neighbor)) for neighbor in info["edge_with"])

    nx.draw_circular(
        graph,
        with_labels=True,
        node_color=[graph.nodes[node]['color'] for node in graph],
    )
    plt.show()


if __name__ == '__main__':
    run_program()
