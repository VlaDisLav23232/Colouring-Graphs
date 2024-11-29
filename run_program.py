import argparse

def run_program():
    '''
    Runs the program: processes graph data, and optionally visualizes it.
    '''
    args = arguments()

    if not args.input_file.endswith(".json"):
        raise argparse.ArgumentTypeError(f"The file {args.input_file} is not a JSON file!")

    data = reading_json_file(args.input_file)
    recolored_data = drawing_with_new_colours(data)

    if recolored_data is None:
        print("The graph cannot be recolored!")

    if args.draw:
        draw_graph(data)
        draw_graph(recolored_data)

run_program()
