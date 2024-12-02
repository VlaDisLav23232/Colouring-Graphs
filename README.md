# Colouring-Graphs

## Project Info
A program returns a three-color coloring of a graph or reports that such a coloring is not possible

## Problem description
In an undirected graph, each vertex is colored red, green, or blue. The coloring of the graph is successful if any edge connects vertices of a different color. You need to change the color of each vertex so that the coloring of the graph is successful. You must change the color of each vertex of the graph, and the color cannot be changed to the same as it was. 

## Input data
The program is given a JSON file with a graph which coloring needs to be found.

## Installation and Using

1. Clone repository: https://github.com/VlaDisLav23232/Colouring-Graphs
2. Install necessary libraries:
    import argparse
    import json
    import networkx as nx
    import matplotlib.pyplot as plt
3. Write to terminal:  python testing_prog.py filename.json --draw  
(for example python testing_prog.py test_json_3.json --draw )
4. Now you can see graph before recoloring 
5. To see recolored graph you should close window of the before recoloring program. If graph can't be recolored you will see the message 'The graph cannot be recolored!' in terminal

## Our Functions:

1. arguments

The arguments function is used for processing command-line arguments with the argparse library. 
The first line creates a parser — an ArgumentParser object. Then, a required positional argument, input_file, is added, which expects a string value. This argument provides the initial graph in JSON format. The --draw argument is optional. If the user includes --draw, the value of this parameter will be True; otherwise, it will be False. This argument is used to determine whether the graph should be visualized after recoloring. The parser.parse_args method returns args, which contains all the arguments.

2. run_program

The run_program function works with graph data, reading it from a JSON file, changing the colors of the graph according to the algorithm, and, if necessary, visualizing the initial and modified graphs. At the beginning, the arguments function is called, which receives the program parameters, including the path to the JSON file and the flag for visualization. The file format is checked for correctness, and if it is not JSON, an error is thrown. Graph data is read via reading_json_file. Next, drawing_with_new_colours is called to change the colors of the graph. If recoloring is not possible, the message "The graph cannot be recolored!" is displayed. If visualization is enabled, the draw_graph function displays the initial and modified graphs.

3. reading_json_file

This function reads and processes data from a JSON file, which contains information about the nodes of a graph.
he algorithm itself works as follows:
Using the json.load() method, it reads and parses the JSON content into a Python dictionary.
The dictionary returned by the function contains nodes as keys and their associated information as values.
The keys is number of node and values are color and number of node with which there is a edge.

4. drawing_with_new_colours

The basic algorithm for coloring a graph. The function for this algorithm is given a dictionary data with all the data about the graph extracted from the file. There are also key arguments num and new_dict, which will be responsible for the number of the vertex we are coloring and the new recolored graph.

The algorithm itself works as follows: 

1) It takes the first vertice and creates a list of available colors (there are 3 of them by itself).

2) Then it removes its previous color from the list, and removes the colors of its neighboring vertices (if the following vertices are considered, and not the first).

3) After the list of available colors for selection has been formed, the algorithm iterates over it, and chooses the first color for this vertice.

4) Then a function is called recursively, which again repeats the same algorithm for the same vertices.

5) In the end, if all the colors for the vertices could be chosen, then it returns a dictionary with a recolored graph. Otherwise, if the color cannot be set, then the algorithm goes back and takes other colors for the previous vertices, and so on until the algorithm runs to the end and returns a recolored graph, or returns nothing if coloring is impossible.

5. draw_graph

The draw_graph function visualizes a graph based on the data provided in the form of a dictionary. It performs the following steps:

 1) Graph Creation: A graph object is created using the Graph class from the networkx library.
 2) Adding Nodes: Each node is added to the graph along with its color information (the node color is specified through the color attribute).
 3) Adding Edges: For each node, edges are added to other nodes it is connected to.
 4) Graph Visualization: The graph is visualized using the nx.draw_circular function. Nodes are displayed with appropriate numbering, and their colors correspond to the color attribute specified in the graph.
 5) Graph Display: The graph is shown in a new window using the plt.show() function.

 ## Discrete math knowledge used

 The concept of a simple and complete graph. We were also interested in the chromatic number, but did not use it in the algorithm

 ## Work branches

Development of the math part and analysis of graph variants - Daryna, Vlad
Writing the basis of the algorithm - Vlad
Creating a function for graph visualization - Yelizaveta
Creating functions for working with the graphical interface - Volodymyr and Diana
Creating files on which the program will be tested, and functions for reading and converting the JSON file - Daryna
Presentation - Volodymyr

## Impressions from the teamwork

Thanks to this computer project, we learned to distribute responsibilities much better, learned interesting properties of graphs. An interesting challenge for us was to develop our own algorithm for finding a successful coloring, because we did not find alternatives for creating. Thank you for this oportunity of teamwork! Thank for our assistent Sofia that help and mentoring us and for Ms. Julia and Mr. Andrew for high knowledge in discrete math!

## Developers
Vlad (shymanovskyi.pn@ucu.edu.ua)
Daryna (horetska.pn@ucu.edu.ua)
Vladimir (yanishevskyi.sn@ucu.edu.ua)
Liza (piletska.pn@ucu.edu.ua)
Diana(lyzenko.pn@ucu.edu.ua)
