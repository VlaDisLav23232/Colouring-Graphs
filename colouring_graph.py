"""Colouring graphs"""

import argparse
import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def arguments():
    """
    Reads arguments for argparse.
    """
    parser = argparse.ArgumentParser(description="Graph Recoloring Program")
    parser.add_argument("input_file", type=str, nargs = "?",\
        default=None, help="Path to the JSON file \
        containing graph data. Note: it should not be empty!",)
    parser.add_argument("--draw", action="store_true",\
        help="Visualizes the graph before and after after recoloring.\
        With --draw argument you should write the name of a json-file\
        which will contain the graph. This graph at first will be vizualized\
        on the separate window. After closing the window,\
        you will get another graph, recoloured one.",)
    parser.add_argument("--ani_draw", action="store_true",\
        help="Visualizes the recolouring of graph with special animation.\
        With --ani_draw argument you should write the name of a json-file\
        which will contain the graph. This graph will be vizualized\
        on the separate window. 1 second after the window was opened an animation\
        of recolouring starts. The interval of colouring every vertice is based\
        on amount of vertices in the graph",)

    args = parser.parse_args()

    return args


def run_program():
    '''
    Runs the program: processes graph data, and optionally visualizes it.
    '''
    args = arguments()


    if args.draw or args.ani_draw:
        try:
            if args.input_file is None:
                print("-----------------------------------\n\
You should input a name of the file!\n\
-----------------------------------")
            elif args.input_file.endswith(".json"):
                data = reading_json_file(args.input_file)
                recolored_data = drawing_with_new_colours(data)
                if recolored_data is None:
                    print("-----------------------------------\n\
The graph cannot be recoloured!\n\
-----------------------------------")
                elif not data:
                    print("--------------------------------------------------------\n\
This graph does not have vertices! Try something else!\n\
--------------------------------------------------------")
                else:
                    if args.draw:
                        print("------------------------------\n\
Here is your graph before recolouring!\n\
------------------------------")
                        draw_graph(data)
                        print("------------------------------\n\
Here is your graph after recolouring!\n\
------------------------------")
                        draw_graph(recolored_data)
                    elif args.ani_draw:
                        print("------------------------------\n\
Here is your animated graph!\n\
------------------------------")
                        draw_graph_animated(data, recolored_data)
            else:
                print(f"--------------------------------------------\n\
The file {args.input_file} is not a JSON file!\n\
--------------------------------------------")
        except FileNotFoundError:
            print("--------------------------------------\n\
File with such name does not exist!\n\
--------------------------------------")
    else:
        print("-------------------------------------------------------------------------\n\
WELCOME TO THE GRAPH RECOLOURER!\n\
\n\
Write to terminal 'colouring_graph.py *name of the file(json)* --draw'\n\
to see at first the graph before recolouring and then by closing the\n\
window of graph before recolouring see the graph after recolouring.\n\
Or write to terminal 'colouring_graph.py *name of the file(json)* --ani_draw'\n\
to see recolouring of the graph in a real time!\n\
-------------------------------------------------------------------------")


def reading_json_file(filename: str) -> dict:
    """
    Reads json files with information about nodes of the graph

    :param filename: str, file from which we read an info
    :return: dict, dictionary with nodes as a key and info about them as a value

    >>> reading_json_file("test_json_1.json")
    {'1': {'color': 'b', 'edge_with': [2, 3, 4]}, '2': {'color': 'b',\
 'edge_with': [1, 4]}, '3': {'color': 'g', 'edge_with': [1]},\
 '4': {'color': 'r', 'edge_with': [1, 2]}}
    >>> reading_json_file("test_json_2.json")
    {'1': {'color': 'b', 'edge_with': [2, 3, 4]}, '2': {'color': 'r',\
 'edge_with': [1, 3]}, '3': {'color': 'r', 'edge_with':\
 [1, 2, 4]}, '4': {'color': 'r', 'edge_with': [1, 3]}}
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

    >>> drawing_with_new_colours(reading_json_file("test_json_1.json"))
    {'1': {'color': 'r', 'edge_with': [2, 3, 4]}, '2': {'color': 'g',\
 'edge_with': [1, 4]}, '3': {'color': 'b', 'edge_with': [1]},\
 '4': {'color': 'b', 'edge_with': [1, 2]}}
    >>> drawing_with_new_colours(reading_json_file("test_json_2.json"))
    {'1': {'color': 'r', 'edge_with': [2, 3, 4]}, '2': {'color': 'g',\
 'edge_with': [1, 3]}, '3': {'color': 'b', 'edge_with':\
 [1, 2, 4]}, '4': {'color': 'g', 'edge_with': [1, 3]}}
    """

    if new_dict is None:
        new_dict = {}

    if len(data) < num:
        return new_dict

    available_colours = ["r", "g", "b"]
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


def draw_graph_animated(graph_before: dict, graph_after: dict) -> None:
    """
    Animates the transition from one graph to another by changing node colors.

    :param graph_before: dict, Initial graph data.
    :param graph_after: dict, Target graph data.
    :return: None, shows the animation of the transition.
    """

    #function for building a graph
    def build_graph(data):
        graph = nx.Graph()
        for node, info in data.items():
            graph.add_node(node, color=info["color"])
            graph.add_edges_from((node, str(neighbor)) for neighbor in info["edge_with"])
        return graph

    #making two graphs
    graph1 = build_graph(graph_before)
    graph2 = build_graph(graph_after)

    #making container and object that saves a graph
    fig, ax = plt.subplots()

    #drawing graph func
    def draw_graph_new(graph, ax, colors):
        ax.clear()
        nx.draw_circular(
            graph,
            with_labels=True,
            node_color=colors,
        )

    nodes = list(graph1.nodes)
    steps = len(nodes)
    color_frames = []

    #making a list of lists with info at every moment of animation
    for step in range(steps + 1):
        current_colors = [
            graph2.nodes[node]["color"] if idx < step else graph1.nodes[node]["color"]
            for idx, node in enumerate(nodes)
        ]
        color_frames.append(current_colors)

    #func that draws a new graph at exact moment
    def update(frame):
        draw_graph_new(graph1, ax, color_frames[frame])

    #starts animation
    if steps <= 10:
        _ = FuncAnimation(fig, update, frames=len(color_frames), repeat=False, interval=800)
    elif 10 < steps < 25:
        _ = FuncAnimation(fig, update, frames=len(color_frames), repeat=False, interval=550)
    elif steps >= 25:
        _ = FuncAnimation(fig, update, frames=len(color_frames), repeat=False, interval=250)
    plt.show()


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    run_program()
