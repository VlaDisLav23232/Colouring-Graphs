import argparse

def run_program():
    args = arguments()

    if not args.input_file.endswith(".json"):
        raise argparse.ArgumentTypeError(f"The file {args.input_file} is not a JSON file!")
    
    data = reading_json_file(args.input_file)
    recolored_data = drawing_with_new_colours(data)

    print("Recolored graph data:")
    print(json.dumps(recolored_data, indent=4))

    if args.draw:
        draw_graph(recolored_data)

run_program()
